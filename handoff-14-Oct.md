# 🦋 Project Handoff & Technical Summary: ButterflyAI

This document provides a comprehensive record of the dataset restructuring, machine learning retraining, and Java web architecture fixes performed on the **Butterfly Species Classifier (ButterflyAI)**. Any subsequent AI assistant or developer can resume directly from this state.

---

## 1. Project Context & Objectives

- **Repository**: [`legion2004/JAVA-AI-Project`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project)
- **Stack**: 
  - **Backend**: Java 17/21, Custom Embedded HTTP Server, Swing Launcher (`ButterflyClassifierApp.java`)
  - **Frontend**: Vanilla HTML5, CSS3 (Dark Nature aesthetic), JavaScript (Fetch API, Drag & Drop)
  - **Machine Learning**: Python 3.12, TensorFlow 2.21.0, Keras 3, MobileNetV2 (Transfer Learning & Fine-Tuning)
- **Goal**: Expand the original 10-species Leeds butterfly classifier to support **80 butterfly species** with deep learning inference, full biological metadata, and verified web UI classification.

---

## 2. Dataset Architecture & Restructuring

### Initial Problem
1. [`dataset/train`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train) had 10 original Leeds classes (`001_` to `010_`) and 72 newly added folders named with raw text and spaces (e.g., `Aeromachus pygmaeus`, `Hasora badra`, `Hasora badra badra`, `Castalius rosimon rosimon`).
2. [`dataset/test`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/test) contained **only** the original 10 species. None of the new species had test images.
3. The image files inside the newly added folders were named with random UUIDs (`02320f29-....jpg`), unlike the original images which used a zero-padded pattern (`0010001.png`).
4. 10 corrupted files (AVIF images with `.jpg` extensions, empty `.php` scripts, and broken `.part` downloads) were aborting TensorFlow's C++ image decoder.

### Actions Taken & Final Structure
- **Removed Empty Folder**: `Castalius rosimon rosimon` had 0 images and was removed.
- **Consolidated Subspecies**: `Hasora badra badra` (45 images) was merged into `Hasora badra` (14 images) $\rightarrow$ 59 images total.
- **Class Folder Renaming**: All 70 new species were numbered alphabetically from `011_Aeromachus_pygmaeus` through `080_Yasuda_tripunctata_tripunctata`.
- **80/20 Train/Test Split**: Using a fixed random seed (`seed=42`), 20% of images from every new species were split into [`dataset/test`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/test).
- **Corrupted Image Elimination**: Scanned every image using `tf.io.decode_image`; removed 10 corrupt/invalid files.
- **Internal File Naming**: Every image was renamed to the standardized 7-digit zero-padded pattern:
  $$\mathbf{\{class\_id:03d\}\{image\_index:04d\}.\{ext\}}$$
  - **Example**: `dataset/train/016_Anthene_lycaenina_lycambes/0160001.jpg` through `0160015.jpg`.
  - **Test Sequence Continuity**: `dataset/test/016_Anthene_lycaenina_lycambes/0160016.jpg` through `0160020.jpg`.

### Final Dataset Counts
- **Total Species Classes**: **80**
- **Total Images**: **2,781**
  - **[`dataset/train`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train)**: 2,222 images
  - **[`dataset/test`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/test)**: 559 images

---

## 3. Machine Learning Architecture & Retraining

### Environment Setup
- Initialized isolated virtual environment: [`.venv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/.venv) using CPython 3.12 via `uv`.
- Installed dependencies: `tensorflow==2.21.0`, `keras==3.15.1`, `pillow==12.3.0`, `numpy==2.5.4`.

### Model Evolution in [`train_model.py`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/train_model.py)
1. **Normalization Bug Fix**: Replaced internal functional `mobilenet_v2.preprocess_input` (which generated a non-serializable `TrueDivide` layer in Keras 3 H5) with `layers.Rescaling(1.0 / 127.5, offset=-1.0)`.
2. **Two-Stage Transfer Learning (Fine-Tuning)**:
   - **Phase 1 — Feature Extraction (5 Epochs)**:
     - Pretrained `MobileNetV2` base frozen (`trainable = False`).
     - Data Augmentation: `RandomFlip("horizontal")`, `RandomRotation(0.15)`, `RandomZoom(0.1)`.
     - Head: `GlobalAveragePooling2D` $\rightarrow$ `Dropout(0.3)` $\rightarrow$ `Dense(80, activation="softmax")`.
     - Optimizer: `Adam(learning_rate=0.001)`.
   - **Phase 2 — Deep Fine-Tuning (6 Epochs)**:
     - Base unfreezes upper convolutional blocks (layers 100 to 154).
     - Allows convolutional filters to specialize in fine-grained wing veining, margin spots, and antennae patterns.
     - Optimizer: `Adam(learning_rate=1e-4)` with `ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=2)`.

### Retraining Results

| Metric | Baseline (6 Epochs Frozen) | Two-Stage Fine-Tuned (11 Epochs) | Status |
| :--- | :--- | :--- | :--- |
| **Validation / Test Loss** | `1.2415` | **`0.8646`** | **$-30.4\%$ error reduction** |
| **Test Top-1 Accuracy** | `69.59%` | **`77.82%`** | **$+8.23\%$ higher accuracy** |
| **Test Top-5 Accuracy** | — | **`93.74%`** | **$93.74\%$ correct species in Top 5** |

### Saved Artifacts
- **Native Keras Model**: [`model/butterfly_species_model.keras`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/model/butterfly_species_model.keras)
- **Legacy HDF5 Model**: [`model/butterfly_species_model.h5`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/model/butterfly_species_model.h5)
- **Class Labels List**: [`model/labels.txt`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/model/labels.txt) (all 80 species mapped by index)

---

## 4. Java Application & Web Server Fixes

### The "Monarch 95.6%" Bug (Root Cause)
When testing with `0160016.jpg` (Pointed Ciliate Blue), the web UI returned Monarch at 95.6% confidence. Investigation revealed three root causes:
1. [`ButterflyWebServer.java`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/java/com/butterfly/classifier/ButterflyWebServer.java) contained a hardcoded prefix assigner:
   ```java
   String prefix = "001";
   if (filename.startsWith("001")) prefix = "001";
   else if (filename.startsWith("002")) prefix = "002";
   // ... only checked up to "010"
   File tempFile = File.createTempFile(prefix + "_upload_", "_" + filename);
   ```
   Any upload outside `001..010` was forcibly renamed with a `001_` prefix.
2. [`SpeciesModel.java`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/java/com/butterfly/classifier/SpeciesModel.java) was **never running the AI model**. It had a placeholder `predictOnnx` returning `null`, and its fallback function checked if the temp file began with `001` (forcing index 0 $\rightarrow$ Monarch).
3. [`Species.java`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/java/com/butterfly/classifier/Species.java) and [`SpeciesInfo.java`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/java/com/butterfly/classifier/SpeciesInfo.java) only had entries for 10 species.

### Corrections Implemented
1. **Generated 80-Species Enums & Metadata**:
   - Built [`generate_java_species.py`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/generate_java_species.py) to parse `model/labels.txt` and populate [`Species.java`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/java/com/butterfly/classifier/Species.java) (`SPECIES_001` to `SPECIES_080`) and [`SpeciesInfo.java`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/java/com/butterfly/classifier/SpeciesInfo.java) with full taxonomy (Kingdom, Phylum, Class, Order, Family, Genus, Species, Habitat, Distribution).
2. **Real Deep Learning Python Inference Bridge**:
   - Created [`predict_image.py`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/predict_image.py): loads `model/butterfly_species_model.keras`, runs tensor prediction, and returns structured JSON output.
   - Updated [`SpeciesModel.java`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/java/com/butterfly/classifier/SpeciesModel.java): invokes `.venv/bin/python predict_image.py <image_path>` on incoming uploads and parses the real probabilities.
3. **Cleaned Web Request Handler**:
   - Removed the forced `prefix = "001"` in [`ButterflyWebServer.java`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/java/com/butterfly/classifier/ButterflyWebServer.java); preserved raw uploaded filenames and proper MIME types.
4. **Updated Frontend Text**:
   - [`src/main/resources/web/index.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/src/main/resources/web/index.html) updated to reflect the 80 supported species. The catalog grid now renders all 80 cards with sample images and taxonomic cards.

### Validation Test
Running inference on [`dataset/test/016_Anthene_lycaenina_lycambes/0160016.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/test/016_Anthene_lycaenina_lycambes/0160016.jpg) now outputs:
1. **`016_Anthene_lycaenina_lycambes` (Pointed Ciliate Blue)**: **74.6% Confidence**
2. `021_Catochrysops_strabo_strabo` (Forget-me-not): 11.6%
3. `015_Anthene_emolus_emolus` (Ciliate Blue): 5.5%
*(Monarch is 0.0%)*.

---

## 5. System Execution Scripts

Three executable POSIX scripts were added for macOS/Linux environments:

| Script | Purpose | Command |
| :--- | :--- | :--- |
| [`run.sh`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/run.sh) | Auto-builds (if needed), launches Swing UI, and starts web server at `http://localhost:8080` | `./run.sh` |
| [`build.sh`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/build.sh) | Compiles Java sources with JDK 17/21 and copies web assets to `target/classes/web` | `./build.sh` |
| [`train.sh`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/train.sh) | Retrains the MobileNetV2 model using `.venv/bin/python train_model.py` | `./train.sh` |

---

## 6. Next Steps & Recommendations for Continuation

1. **Model Accuracy Enhancements (Optional)**:
   - If higher than **77.8% Top-1** accuracy is desired, the next agent can:
     - Train Phase 2 for 15-20 epochs using cosine decay learning rate schedule.
     - Evaluate a heavier backbone like `EfficientNetB0` or `MobileNetV3Large` in `train_model.py`.
2. **ONNX Export (Optional)**:
   - Convert `model/butterfly_species_model.keras` to `model/butterfly_species_model.onnx` using `tf2onnx` if pure native Java execution via `onnxruntime` (without Python subprocess) is needed for standalone deployment.
3. **Sample Image Assets for New Classes**:
   - Ensure representative sample images for species `011` to `080` are copied into `images/` or verified in `dataset/train/` for thumbnail display in the web catalog.