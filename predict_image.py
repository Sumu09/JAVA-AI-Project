import os
import sys
import json
import numpy as np

# Suppress TF C++ logs and warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TEMPORARILY_DISABLE_PROTOBUF_VERSION_CHECK"] = "true"

import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
logging.getLogger("absl").setLevel(logging.ERROR)

def get_labels(project_root):
    labels_path = os.path.join(project_root, "model", "labels.txt")
    if not os.path.exists(labels_path):
        train_dir = os.path.join(project_root, "dataset", "train")
        if os.path.exists(train_dir):
            labels = sorted([d for d in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, d))])
            try:
                with open(labels_path, "w", encoding="utf-8") as f:
                    for l in labels:
                        f.write(f"{l}\n")
            except Exception:
                pass
            return labels
        else:
            return None
    with open(labels_path, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]

def load_predictor(project_root):
    import tensorflow as tf

    model_path_tflite = os.path.join(project_root, "model", "butterfly_species_model.tflite")
    model_path_keras = os.path.join(project_root, "model", "butterfly_species_model.keras")
    model_path_h5 = os.path.join(project_root, "model", "butterfly_species_model.h5")

    # 1. Try TFLite interpreter for ultra-fast (20ms) inference
    if os.path.exists(model_path_tflite):
        try:
            interpreter = tf.lite.Interpreter(model_path=model_path_tflite)
            interpreter.allocate_tensors()
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()

            def predict_tflite(arr):
                interpreter.set_tensor(input_details[0]['index'], arr)
                interpreter.invoke()
                return interpreter.get_tensor(output_details[0]['index'])[0]

            # Warmup
            dummy = np.zeros((1, 224, 224, 3), dtype=np.float32)
            predict_tflite(dummy)
            return predict_tflite
        except Exception:
            pass

    # 2. Try native Keras model
    model = None
    if os.path.exists(model_path_keras):
        try:
            model = tf.keras.models.load_model(model_path_keras, compile=False)
        except Exception:
            pass

    # 3. Fallback to .h5 model
    if model is None and os.path.exists(model_path_h5):
        try:
            model = tf.keras.models.load_model(model_path_h5, compile=False)
        except Exception:
            try:
                import keras
                orig_g = keras.initializers.GlorotUniform.__init__
                def patched_g(self, *args, **kwargs):
                    kwargs.pop("input_axes", None)
                    kwargs.pop("output_axes", None)
                    orig_g(self, *args, **kwargs)
                keras.initializers.GlorotUniform.__init__ = patched_g

                orig_bn = keras.layers.BatchNormalization.__init__
                def patched_bn(self, *args, **kwargs):
                    kwargs.pop("renorm", None)
                    kwargs.pop("renorm_clipping", None)
                    kwargs.pop("renorm_momentum", None)
                    orig_bn(self, *args, **kwargs)
                keras.layers.BatchNormalization.__init__ = patched_bn

                model = tf.keras.models.load_model(model_path_h5, compile=False)
            except Exception:
                pass

    if model is not None:
        def predict_keras(arr):
            return model(arr, training=False).numpy()[0]
        # Warmup
        dummy = np.zeros((1, 224, 224, 3), dtype=np.float32)
        predict_keras(dummy)
        return predict_keras

    return None

def predict_image_file(predict_fn, labels, image_path):
    from PIL import Image, ImageOps
    if not os.path.exists(image_path):
        return {"error": f"Image file not found: {image_path}"}

    pil_raw = Image.open(image_path).convert("RGB")
    orig_w, orig_h = pil_raw.size

    # Fit image to 224x224 maintaining aspect ratio (smart center crop)
    pil_img = ImageOps.fit(pil_raw, (224, 224), method=Image.Resampling.BILINEAR)
    arr = np.array(pil_img, dtype=np.float32)
    input_tensor = np.expand_dims(arr, axis=0)

    preds = predict_fn(input_tensor)
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

    return {
        "success": True,
        "width": orig_w,
        "height": orig_h,
        "predictions": predictions_list
    }

def run_daemon():
    project_root = os.path.dirname(os.path.abspath(__file__))
    labels = get_labels(project_root)
    if not labels:
        print(json.dumps({"error": "labels.txt not found"}), flush=True)
        sys.exit(1)

    predict_fn = load_predictor(project_root)
    if not predict_fn:
        print(json.dumps({"error": "Could not load trained model"}), flush=True)
        sys.exit(1)

    # Signal to Java that the model is fully loaded and ready for instant inference
    print("READY", flush=True)

    for line in sys.stdin:
        img_path = line.strip()
        if not img_path:
            continue
        if img_path in ("QUIT", "EXIT"):
            break
        try:
            res = predict_image_file(predict_fn, labels, img_path)
            print(json.dumps(res), flush=True)
        except Exception as e:
            print(json.dumps({"error": str(e)}), flush=True)

def run_oneshot(image_path):
    project_root = os.path.dirname(os.path.abspath(__file__))
    labels = get_labels(project_root)
    if not labels:
        print(json.dumps({"error": "labels.txt not found"}))
        sys.exit(1)

    predict_fn = load_predictor(project_root)
    if not predict_fn:
        print(json.dumps({"error": "Could not load trained model"}))
        sys.exit(1)

    res = predict_image_file(predict_fn, labels, image_path)
    print(json.dumps(res))

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No arguments provided"}))
        sys.exit(1)

    arg = sys.argv[1]
    if arg == "--daemon":
        run_daemon()
    else:
        run_oneshot(arg)

if __name__ == "__main__":
    main()
