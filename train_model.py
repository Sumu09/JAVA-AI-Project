import os
import sys
import numpy as np

# Ensure protobuf compatibility and suppress verbose C++ logs on Python 3.12/3.13
os.environ["TEMPORARILY_DISABLE_PROTOBUF_VERSION_CHECK"] = "true"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
from tensorflow.keras import layers, models

def train():
    print("=" * 60)
    print("  Butterfly Species Classifier — Deep Transfer Learning & Fine-Tuning")
    print("  Framework: TensorFlow", tf.__version__)
    print("=" * 60)

    train_dir = os.path.join("dataset", "train")
    test_dir = os.path.join("dataset", "test")
    model_dir = "model"
    model_save_path = os.path.join(model_dir, "butterfly_species_model.h5")
    model_save_keras = os.path.join(model_dir, "butterfly_species_model.keras")
    model_save_tflite = os.path.join(model_dir, "butterfly_species_model.tflite")

    if not os.path.exists(train_dir) or not os.path.exists(test_dir):
        print(f"Error: Dataset folders not found at '{train_dir}' or '{test_dir}'.")
        sys.exit(1)

    os.makedirs(model_dir, exist_ok=True)

    batch_size = 32
    img_size = (224, 224)

    print("\n[1/5] Loading dataset splits...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        train_dir,
        image_size=img_size,
        batch_size=batch_size,
        shuffle=True,
        seed=42
    )

    class_names = train_ds.class_names
    num_classes = len(class_names)
    print(f"Found {num_classes} species classes:")
    for idx, name in enumerate(class_names):
        print(f"  Class {idx:02d}: {name}")

    test_ds = tf.keras.utils.image_dataset_from_directory(
        test_dir,
        image_size=img_size,
        batch_size=batch_size,
        shuffle=False,
        class_names=class_names
    )

    # Optimize data pipeline for execution
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
    test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

    # Check for warm-start from existing checkpoint
    loaded_existing = False
    model = None

    if os.path.exists(model_save_keras) and "--scratch" not in sys.argv:
        try:
            print(f"\n[2/5] Warm-starting from existing model '{model_save_keras}'...")
            old_model = tf.keras.models.load_model(model_save_keras, compile=False)
            old_dense = old_model.get_layer("predictions")
            old_w, old_b = old_dense.get_weights()
            old_classes = old_w.shape[1]
            in_dim = old_w.shape[0]

            print(f"Existing model has {old_classes} classes. Upgrading to {num_classes} classes...")

            new_w = np.zeros((in_dim, num_classes), dtype=np.float32)
            new_b = np.zeros((num_classes,), dtype=np.float32)

            copy_classes = min(old_classes, num_classes)
            new_w[:, :copy_classes] = old_w[:, :copy_classes]
            new_b[:copy_classes] = old_b[:copy_classes]

            # Initialize any new classes with normalized weights
            if num_classes > copy_classes:
                scale = np.sqrt(2.0 / (in_dim + num_classes))
                new_w[:, copy_classes:] = np.random.normal(0, scale, size=(in_dim, num_classes - copy_classes))
                new_b[copy_classes:] = 0.0

            x = old_model.get_layer("dropout").output
            outputs = layers.Dense(num_classes, activation="softmax", name="predictions")(x)
            model = tf.keras.Model(old_model.inputs, outputs, name="ButterflyAI_MobileNetV2")
            model.get_layer("predictions").set_weights([new_w, new_b])

            # Freeze backbone for top head calibration
            base_layer = None
            for l in model.layers:
                if "mobilenetv2" in l.name.lower():
                    base_layer = l
                    break

            if base_layer:
                base_layer.trainable = False

            loaded_existing = True
            print("Successfully transferred existing feature representations and class weights!")
        except Exception as e:
            print(f"Note: Could not warm-start from existing checkpoint ({e}). Building fresh model.")

    if not loaded_existing:
        print("\n[2/5] Building MobileNetV2 transfer learning architecture from ImageNet base...")
        data_augmentation = tf.keras.Sequential([
            layers.RandomFlip("horizontal"),
            layers.RandomRotation(0.15),
            layers.RandomZoom(0.1),
        ], name="data_augmentation")

        base_model = tf.keras.applications.MobileNetV2(
            input_shape=(224, 224, 3),
            include_top=False,
            weights="imagenet"
        )
        base_model.trainable = False

        inputs = tf.keras.Input(shape=(224, 224, 3), name="input_image")
        x = data_augmentation(inputs)
        x = layers.Rescaling(1.0 / 127.5, offset=-1.0, name="rescaling")(x)
        x = base_model(x, training=False)
        x = layers.GlobalAveragePooling2D(name="global_avg_pool")(x)
        x = layers.Dropout(0.3, name="dropout")(x)
        outputs = layers.Dense(num_classes, activation="softmax", name="predictions")(x)

        model = tf.keras.Model(inputs, outputs, name="ButterflyAI_MobileNetV2")

    # Phase 1: Train/Calibrate top head
    epochs_phase1 = 4 if loaded_existing else 5
    lr_phase1 = 0.001 if not loaded_existing else 0.0005

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=lr_phase1),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy", tf.keras.metrics.SparseTopKCategoricalAccuracy(k=5, name="top_5_accuracy")]
    )

    print(f"\n[3/5] Phase 1: Training top classification layers ({epochs_phase1} epochs)...")
    model.fit(
        train_ds,
        validation_data=test_ds,
        epochs=epochs_phase1,
        verbose=1
    )

    # Phase 2: Fine-tune upper convolutional filters
    print("\n[4/5] Phase 2: Fine-tuning upper MobileNetV2 layers specifically for butterfly features...")
    base_layer = None
    for l in model.layers:
        if "mobilenetv2" in l.name.lower():
            base_layer = l
            break

    if base_layer:
        base_layer.trainable = True
        for layer in base_layer.layers[:100]:
            layer.trainable = False

    fine_tune_lr = 1e-4
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=fine_tune_lr),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy", tf.keras.metrics.SparseTopKCategoricalAccuracy(k=5, name="top_5_accuracy")]
    )

    epochs_phase2 = 4 if loaded_existing else 6
    total_epochs = epochs_phase1 + epochs_phase2
    lr_callback = tf.keras.callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=2, verbose=1)

    model.fit(
        train_ds,
        validation_data=test_ds,
        initial_epoch=epochs_phase1,
        epochs=total_epochs,
        callbacks=[lr_callback],
        verbose=1
    )

    print("\n[5/5] Evaluating final model on test dataset...")
    eval_results = model.evaluate(test_ds, verbose=0)
    test_loss = eval_results[0]
    test_acc = eval_results[1]
    top5_acc = eval_results[2] if len(eval_results) > 2 else 0.0

    print(f"--> Test Loss:           {test_loss:.4f}")
    print(f"--> Test Top-1 Accuracy: {test_acc * 100:.2f}%")
    print(f"--> Test Top-5 Accuracy: {top5_acc * 100:.2f}%")

    print(f"\nSaving model to '{model_save_keras}' and '{model_save_path}'...")
    model.save(model_save_keras)
    try:
        model.save(model_save_path)
    except Exception as e:
        print(f"Note: Saved .keras model successfully ({e})")

    # Export to optimized TFLite for sub-50ms inference
    print(f"Exporting optimized TFLite model to '{model_save_tflite}'...")
    try:
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_bytes = converter.convert()
        with open(model_save_tflite, "wb") as f:
            f.write(tflite_bytes)
        print(f"Saved TFLite model successfully! Size: {len(tflite_bytes) // 1024} KB")
    except Exception as e:
        print(f"Note: TFLite export encountered ({e})")

    labels_file = os.path.join(model_dir, "labels.txt")
    with open(labels_file, "w", encoding="utf-8") as f:
        for name in class_names:
            f.write(f"{name}\n")
    print(f"Saved {num_classes} species class labels to '{labels_file}'")

    print("\nSUCCESS: Model training & fine-tuning complete and saved successfully!")

if __name__ == "__main__":
    train()
