import os
import sys
import json
import numpy as np

# Suppress TF C++ logs and warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TEMPORARILY_DISABLE_PROTOBUF_VERSION_CHECK"] = "true"

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No image path provided"}))
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print(json.dumps({"error": f"Image file not found: {image_path}"}))
        sys.exit(1)

    project_root = os.path.dirname(os.path.abspath(__file__))
    model_path_keras = os.path.join(project_root, "model", "butterfly_species_model.keras")
    model_path_h5 = os.path.join(project_root, "model", "butterfly_species_model.h5")
    labels_path = os.path.join(project_root, "model", "labels.txt")

    if not os.path.exists(labels_path):
        print(json.dumps({"error": "labels.txt not found"}))
        sys.exit(1)

    with open(labels_path, "r", encoding="utf-8") as f:
        labels = [l.strip() for l in f if l.strip()]

    import tensorflow as tf
    from PIL import Image

    # Load model
    model = None
    if os.path.exists(model_path_keras):
        try:
            model = tf.keras.models.load_model(model_path_keras, compile=False)
        except Exception:
            pass

    if model is None and os.path.exists(model_path_h5):
        try:
            model = tf.keras.models.load_model(model_path_h5, compile=False)
        except Exception:
            pass

    if model is None:
        print(json.dumps({"error": "Could not load trained model from model/ folder"}))
        sys.exit(1)

    try:
        pil_img = Image.open(image_path).convert("RGB").resize((224, 224))
        arr = np.array(pil_img, dtype=np.float32)
        # Note: In train_model.py, Rescaling / preprocess is inside the model or normalized here
        # Model input shape (1, 224, 224, 3)
        input_tensor = np.expand_dims(arr, axis=0)

        preds = model(input_tensor, training=False).numpy()[0]
        
        # Sort predictions
        top_indices = np.argsort(preds)[::-1]

        predictions_list = []
        for idx in top_indices:
            label = labels[idx]
            class_id = label.split("_")[0]
            conf = float(preds[idx]) * 100.0
            predictions_list.append({
                "index": int(idx),
                "id": class_id,
                "label": label,
                "confidence": round(conf, 2)
            })

        output = {
            "success": True,
            "predictions": predictions_list
        }
        print(json.dumps(output))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
