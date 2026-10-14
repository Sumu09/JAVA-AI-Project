import os
import sys

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
        print(f"  Class {idx}: {name}")

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

    print("\n[2/5] Building MobileNetV2 transfer learning architecture...")
    # Data Augmentation layer
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.15),
        layers.RandomZoom(0.1),
    ], name="data_augmentation")

    # MobileNetV2 Pretrained Base
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights="imagenet"
    )
    base_model.trainable = False  # Freeze pretrained weights for phase 1

    inputs = tf.keras.Input(shape=(224, 224, 3), name="input_image")
    x = data_augmentation(inputs)
    # Rescaling normalizes pixel range from [0, 255] to [-1.0, 1.0]
    x = layers.Rescaling(1.0 / 127.5, offset=-1.0, name="rescaling")(x)
    x = base_model(x, training=False)
    x = layers.GlobalAveragePooling2D(name="global_avg_pool")(x)
    x = layers.Dropout(0.3, name="dropout")(x)
    outputs = layers.Dense(num_classes, activation="softmax", name="predictions")(x)

    model = tf.keras.Model(inputs, outputs, name="ButterflyAI_MobileNetV2")

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy", tf.keras.metrics.SparseTopKCategoricalAccuracy(k=5, name="top_5_accuracy")]
    )

    model.summary()

    epochs_phase1 = 5
    print(f"\n[3/5] Phase 1: Training top classification layers ({epochs_phase1} epochs)...")
    model.fit(
        train_ds,
        validation_data=test_ds,
        epochs=epochs_phase1,
        verbose=1
    )

    print("\n[4/5] Phase 2: Fine-tuning upper MobileNetV2 layers specifically for butterfly features...")
    base_model.trainable = True
    # Freeze lower generic layers and unfreeze specialized upper convolutional filters
    for layer in base_model.layers[:100]:
        layer.trainable = False

    fine_tune_lr = 1e-4
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=fine_tune_lr),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy", tf.keras.metrics.SparseTopKCategoricalAccuracy(k=5, name="top_5_accuracy")]
    )

    epochs_phase2 = 6
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
    
    labels_file = os.path.join(model_dir, "labels.txt")
    with open(labels_file, "w", encoding="utf-8") as f:
        for name in class_names:
            f.write(f"{name}\n")
    print(f"Saved {num_classes} species class labels to '{labels_file}'")

    print("\nSUCCESS: Model training & fine-tuning complete and saved successfully!")

if __name__ == "__main__":
    train()
