import os
import sys

# Ensure protobuf compatibility and suppress verbose C++ logs on Python 3.13
os.environ["TEMPORARILY_DISABLE_PROTOBUF_VERSION_CHECK"] = "true"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
from tensorflow.keras import layers, models

def train():
    print("=" * 60)
    print("  Butterfly Species Classifier — Model Retraining")
    print("  Framework: TensorFlow", tf.__version__)
    print("=" * 60)

    train_dir = os.path.join("dataset", "train")
    test_dir = os.path.join("dataset", "test")
    model_dir = "model"
    model_save_path = os.path.join(model_dir, "butterfly_species_model.h5")

    if not os.path.exists(train_dir) or not os.path.exists(test_dir):
        print(f"Error: Dataset folders not found at '{train_dir}' or '{test_dir}'.")
        sys.exit(1)

    os.makedirs(model_dir, exist_ok=True)

    batch_size = 32
    img_size = (224, 224)

    print("\n[1/4] Loading dataset splits...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        train_dir,
        image_size=img_size,
        batch_size=batch_size,
        shuffle=True,
        seed=42
    )

    test_ds = tf.keras.utils.image_dataset_from_directory(
        test_dir,
        image_size=img_size,
        batch_size=batch_size,
        shuffle=False
    )

    class_names = train_ds.class_names
    num_classes = len(class_names)
    print(f"Found {num_classes} species classes:")
    for idx, name in enumerate(class_names):
        print(f"  Class {idx}: {name}")

    # Optimize data pipeline for CPU execution
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
    test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

    print("\n[2/4] Building MobileNetV2 transfer learning architecture...")
    # Data Augmentation layer
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
    ], name="data_augmentation")

    # MobileNetV2 Pretrained Base
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights="imagenet"
    )
    base_model.trainable = False  # Freeze pretrained weights

    inputs = tf.keras.Input(shape=(224, 224, 3), name="input_image")
    x = data_augmentation(inputs)
    # MobileNetV2 normalizes pixel range from [0, 255] to [-1.0, 1.0]
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
    x = base_model(x, training=False)
    x = layers.GlobalAveragePooling2D(name="global_avg_pool")(x)
    x = layers.Dropout(0.2, name="dropout")(x)
    outputs = layers.Dense(num_classes, activation="softmax", name="predictions")(x)

    model = tf.keras.Model(inputs, outputs, name="ButterflyAI_MobileNetV2")

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    model.summary()

    epochs = 6
    print(f"\n[3/4] Training model for {epochs} epochs...")
    history = model.fit(
        train_ds,
        validation_data=test_ds,
        epochs=epochs,
        verbose=1
    )

    print("\n[4/4] Evaluating final model on test dataset...")
    test_loss, test_acc = model.evaluate(test_ds, verbose=0)
    print(f"--> Test Loss:     {test_loss:.4f}")
    print(f"--> Test Accuracy: {test_acc * 100:.2f}%")

    print(f"\nSaving trained weights to '{model_save_path}'...")
    model.save(model_save_path)
    print("SUCCESS: Model retraining complete and saved successfully!")

if __name__ == "__main__":
    train()
