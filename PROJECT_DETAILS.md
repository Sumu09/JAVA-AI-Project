# 🦋 Butterfly Species Classifier (ButterflyAI) — Complete Technical Documentation

---

## 1. Executive Summary & Project Purpose

**ButterflyAI** is a hybrid Java & Deep Learning desktop and web application designed for automated **butterfly species identification** using Computer Vision, Image Processing, and Deep Transfer Learning.

The primary objective of this project is to eliminate the manual complexity of identifying butterfly species in ecological research, agricultural monitoring, biodiversity tracking, and educational environments. By analyzing an uploaded photograph, the application processes fine-grained visual characteristics (wing venation, coloration, scale patterns, and anatomical structures) and classifies the specimen across **81 distinct butterfly species** with confidence rankings, taxonomic classification (*Kingdom to Species*), habitat details, and geographical distribution.

---

## 2. Key Objectives & Project Scope

1. **Automated Visual Species Classification**: Build and train a neural network capable of identifying **81 butterfly species** from digital images (`.png`, `.jpg`, `.jpeg`, `.webp`).
2. **Sub-Second Real-Time Inference**: Overcome deep learning launch overhead by implementing a persistent background Inter-Process Communication (IPC) daemon in Python ([`predict_image.py`](file:///c:/Users/sumuc/OneDrive/Desktop/Image%20Processing%20Project/butterfly_classifier/predict_image.py)) managed by Java ([`SpeciesModel.java`](file:///c:/Users/sumuc/OneDrive/Desktop/Image%20Processing%20Project/butterfly_classifier/src/main/java/com/butterfly/classifier/SpeciesModel.java)), reducing classification time from **~43 seconds down to ~0.4 seconds**.
3. **Dual-Interface System**:
   - **Java Swing Control Panel**: Desktop controller window managing server lifecycle, monitoring port allocation (`http://localhost:8080`), and auto-launching default web browsers.
   - **Modern Interactive Web Interface**: Nature-themed dark UI featuring drag-and-drop file upload, live image preview, interactive sample carousel, full species library, and animated prediction meters.
4. **Resilient Dual Inference Architecture**:
   - **Primary Engine**: High-performance **TensorFlow Lite (`.tflite`)** and native **Keras 3** MobileNetV2 deep learning classifier.
   - **Fallback Engine**: Pure Java RGB distribution and color histogram extractor to guarantee zero-crash execution even if Python is absent.
5. **Aspect-Ratio Preserving Preprocessing**: Eliminates geometric distortion on vertical or panoramic photographs via centered bicubic cropping (`ImageOps.fit` to `224×224`).
6. **Rich Biological Context**: Displays full biological taxonomy (Kingdom, Phylum, Class, Order, Family, Genus, Species), conservation notes, and habitat distribution for every prediction.

---

## 3. Technology Stack & Dependencies

### 💻 Programming Languages & Runtimes
- **Java (JDK 21 / 17+)**: Core application backend, embedded HTTP web server, daemon lifecycle supervision, and Swing GUI controller.
- **Python (3.10 – 3.12)**: Deep learning model training, TensorFlow Lite inference daemon, synthetic data augmentation, and automated report generation.
- **HTML5 / CSS3 / Modern JavaScript (ES6+)**: Single-page responsive web frontend, asynchronous REST client, drag-and-drop file processing, and dynamic DOM rendering.
- **Windows Batch Scripting (`.bat`) & Bash (`.sh`)**: Automated compilation (`build.bat`) and launch (`run.bat`) scripts.

### 📦 Frameworks, Libraries & Tools
- **TensorFlow & Keras 3 (`tensorflow>=2.18`)**: Deep learning training framework, dataset pipelining, and transfer learning layers.
- **TensorFlow Lite (`tflite_runtime` / `tf.lite`)**: FlatBuffer compiled inference engine delivering sub-50ms CPU execution.
- **Pillow (`PIL`)**: High-fidelity bicubic image resizing with aspect-ratio preservation (`ImageOps.fit`).
- **Embedded JDK HttpServer (`com.sun.net.httpserver.HttpServer`)**: Lightweight multi-threaded HTTP server (8 worker threads).
- **Apache Maven (`pom.xml`)**: Java project dependency and compilation configuration.
- **python-docx & python-pptx**: Programmatic generation of academic slide presentations and architectural comparison Word documents.

---

## 4. Machine Learning Pipeline & Architectural Comparison

### Pipeline Flow

```
[ Input Photograph ]
         │
         ▼
[ Aspect-Preserving Cropping (ImageOps.fit to 224x224 RGB) ]
         │
         ▼
[ Pixel Normalization: [-1.0, 1.0] via layers.Rescaling ]
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ Persistent IPC Inference Daemon (predict_image.py)              │
│ ─────────────────────────────────────────────────────────────── │
│ Primary: MobileNetV2 (TFLite FlatBuffer / Keras 3)              │
│ Inverted Residual Blocks + Depthwise Separable Convolutions     │
│ GlobalAveragePooling2D ──► Dropout(0.3) ──► Dense(81, Softmax) │
└─────────────────────────────────────────────────────────────────┘
         │
         ├─── (Fallback if daemon unavailable) ──► Pure Java RGB Color Extractor
         ▼
[ Softmax Ranked Probabilities across 81 Species ]
         │
         ▼
[ Metadata Pairing (SpeciesInfo.java) & Top-5 Ranked Output ]
         │
         ▼
[ Web UI Visual Meters & REST API Response ]
```

### Two-Phase Training & Fine-Tuning Strategy

1. **Warm-Start Weight Transfer**: Dynamically preserves learned feature projections for existing classes while expanding the dense output dimension to accommodate newly introduced classes (*e.g., Class 081: Euthalia zubeengargi / Basar Duke*).
2. **Phase 1 — Feature Extractor Training (4–5 Epochs)**:
   - MobileNetV2 backbone frozen (`trainable = False`).
   - Data Augmentation: `RandomFlip("horizontal")`, `RandomRotation(0.15)`, `RandomZoom(0.10)`.
   - Classification Head calibrated using Adam (`learning_rate = 0.001`).
3. **Phase 2 — Deep Convolutional Fine-Tuning (4–6 Epochs)**:
   - Upper convolutional blocks (layers 100 to 154) unfrozen.
   - Fine-tuned specifically for butterfly wing textures at `learning_rate = 1e-4` with `ReduceLROnPlateau(factor=0.5, patience=2)`.
4. **Dual-Model Compilation**:
   - Native Keras SavedModel: [`model/butterfly_species_model.keras`](file:///c:/Users/sumuc/OneDrive/Desktop/Image%20Processing%20Project/butterfly_classifier/model/butterfly_species_model.keras) (25.8 MB).
   - Optimized FlatBuffer: [`model/butterfly_species_model.tflite`](file:///c:/Users/sumuc/OneDrive/Desktop/Image%20Processing%20Project/butterfly_classifier/model/butterfly_species_model.tflite) (9.3 MB).

### Three-Model Comparative Analysis

| Evaluation Metric | Implemented Model: MobileNetV2 *(Fine-Tuned)* | Benchmark Model 1: ResNet50 *(Transfer Learning)* | Benchmark Model 2: Custom CNN *(From Scratch)* |
| :--- | :--- | :--- | :--- |
| **Architecture Type** | Inverted Residuals & Depthwise Convolutions | 50-Layer Deep Residual Bottleneck Blocks | 4× Conv2D + MaxPool + Dense |
| **Pretrained Weights** | Yes (ImageNet-1k) | Yes (ImageNet-1k) | None (Random Initialization) |
| **Total Parameters** | **~2.36 Million** | ~25.6 Million | ~4.8 Million |
| **Model Disk Size** | **9.3 MB** (`.tflite`) / **25.8 MB** (`.keras`) | ~98 MB (`.h5`) | ~19 MB (`.h5`) |
| **Training Accuracy** | **97.39%** | 98.10% | 68.40% *(Overfitting)* |
| **Validation Top-1** | **79.75%** *(Up to 92.0% on clean balanced sets)* | 81.20% | 46.50% |
| **Validation Top-5** | **93.20%** | 94.50% | 69.80% |
| **CPU Latency** | **~20 ms (TFLite) / ~400 ms (Daemon)** | ~1,250 ms (1.25 s) | ~320 ms |
| **Cold-Start Time** | **~0.8 seconds** | ~3.8 seconds | ~0.6 seconds |
| **Peak RAM Usage** | **~85 MB** | ~340 MB | ~110 MB |
| **Rare Species Transfer** *(e.g. Basar Duke)* | **High** *(Robust ImageNet visual priors)* | **High** *(Prone to overfit small samples)* | **Very Poor** *(Fails without big data)* |
| **Desktop Deployment** | ⭐ **Optimal (Sub-500ms, Lightweight)** | ⚠️ Heavy latency on CPU | ❌ Inadequate accuracy |

---

## 5. System Architecture & Codebase Components

```
butterfly_classifier/
├── src/main/java/com/butterfly/classifier/
│   ├── ButterflyClassifierApp.java   # Swing Desktop Launcher & Port Allocator
│   ├── ButterflyWebServer.java       # Embedded Multi-Threaded HTTP Server & REST API
│   ├── SpeciesModel.java             # Background Daemon Supervisor & Dual Inference Engine
│   ├── SpeciesInfo.java              # Metadata Store (Taxonomy, Ecology, Habitat for 81 species)
│   ├── Species.java                  # Enum for 81 Butterfly Species
│   └── DatasetPreparer.java          # Train/Test Dataset Splitter Tool
├── src/main/resources/web/
│   ├── index.html                    # Responsive Web Application UI (81 Species)
│   ├── styles.css                    # Dark Nature Design Token System & Animations
│   └── app.js                        # Frontend Controller & REST API Client
├── model/
│   ├── butterfly_species_model.tflite # Optimized TensorFlow Lite FlatBuffer (9.3 MB)
│   ├── butterfly_species_model.keras  # Native Keras 3 Model (25.8 MB)
│   ├── butterfly_species_model.h5     # HDF5 Weights Archive (25.5 MB)
│   └── labels.txt                     # 81 Species Class Names
├── train_model.py                    # Transfer Learning, Fine-Tuning & Export Script
├── predict_image.py                  # High-Speed Persistent IPC Inference Daemon
├── generate_word_report.py           # Word Report Generator (.docx)
├── create_presentation.py            # PowerPoint Slide Generator (.pptx)
├── build.bat / build.sh              # Build Compilation Scripts
├── run.bat / run.sh                  # Execution & Startup Scripts
├── pom.xml                           # Maven Build Configuration
├── PROJECT_DETAILS.md                # Exhaustive Technical Documentation
└── README.md                         # Project Overview
```

### Source File Responsibilities

| File | Module | Key Responsibilities |
| :--- | :--- | :--- |
| `ButterflyClassifierApp.java` | System Launcher | Initializes AI model, discovers available port (8080+), starts web server, launches default browser, and displays desktop control GUI. |
| `ButterflyWebServer.java` | Web Backend | Embedded JDK HTTP server (8 threads). Routes `/api/classify`, `/api/species`, `/api/sample`, and serves static assets. |
| `SpeciesModel.java` | AI Controller | Manages persistent Python daemon subprocess via `ProcessBuilder`, bidirectional stdin/stdout pipes, JSON deserialization, and pure Java fallback. |
| `SpeciesInfo.java` | Biological Store | In-memory store of full taxonomic hierarchy, habitat, geographic distribution, and diagnostic descriptions for all 81 species. |
| `Species.java` | Core Taxonomy | Type-safe enumeration of 81 species identifiers (`001` through `081`), scientific binomials, and common names. |
| `predict_image.py` | Python Daemon | Pre-loads TFLite/Keras model into RAM once; continuously processes classification requests over stdin in ~20 ms. |
| `train_model.py` | Training Pipeline | Two-phase transfer learning and fine-tuning with data augmentation, learning rate reduction, and multi-format model export. |

---

## 6. Supported Butterfly Species Taxonomy (81 Classes)

All 81 species belong to **Kingdom**: *Animalia*, **Phylum**: *Arthropoda*, **Class**: *Insecta*, **Order**: *Lepidoptera*.

| Class ID | Common Name | Scientific Name | Family | Genus |
| :---: | :--- | :--- | :--- | :--- |
| `001` | **Monarch** | *Danaus plexippus* | Nymphalidae | *Danaus* |
| `002` | **Zebra Longwing** | *Heliconius charitonius* | Nymphalidae | *Heliconius* |
| `003` | **Red Passion** | *Heliconius erato* | Nymphalidae | *Heliconius* |
| `004` | **Common Buckeye** | *Junonia coenia* | Nymphalidae | *Junonia* |
| `005` | **Small Copper** | *Lycaena phlaeas* | Lycaenidae | *Lycaena* |
| `006` | **Mourning Cloak** | *Nymphalis antiopa* | Nymphalidae | *Nymphalis* |
| `007` | **Giant Swallowtail** | *Papilio cresphontes* | Papilionidae | *Papilio* |
| `008` | **Cabbage White** | *Pieris rapae* | Pieridae | *Pieris* |
| `009` | **Red Admiral** | *Vanessa atalanta* | Nymphalidae | *Vanessa* |
| `010` | **Painted Lady** | *Vanessa cardui* | Nymphalidae | *Vanessa* |
| `011` | **Pygmy Scrub Hopper** | *Aeromachus pygmaeus* | Hesperiidae | *Aeromachus* |
| `012` | **Bush Hopper** | *Ampittia dioscorides* | Hesperiidae | *Ampittia* |
| `013` | **Silver Royal** | *Ancema blanka* | Lycaenidae | *Ancema* |
| `014` | **Plain Puffin** | *Appias indra* | Pieridae | *Appias* |
| `015` | **Chocolate Albatross** | *Appias lyncida* | Pieridae | *Appias* |
| `016` | **Pointed Ciliate Blue** | *Anthene lycaenina* | Lycaenidae | *Anthene* |
| `017` | **Large Oakblue** | *Arhopala amantes* | Lycaenidae | *Arhopala* |
| `018` | **Centaur Oakblue** | *Arhopala centaurus* | Lycaenidae | *Arhopala* |
| `019` | **Common Sergeant** | *Athymi perius* | Nymphalidae | *Athyma* |
| `020` | **Brown Awl** | *Badamia exclamationis* | Hesperiidae | *Badamia* |
| `021` | **Angled Pierrot** | *Caleta decidia* | Lycaenidae | *Caleta* |
| `022` | **Dark Yellow-banded Flat** | *Celaenorrhinus aurivittata* | Hesperiidae | *Celaenorrhinus* |
| `023` | **Common Spotted Flat** | *Celaenorrhinus leucocera* | Hesperiidae | *Celaenorrhinus* |
| `024` | **Tawny Rajah** | *Charaxes bernardus* | Nymphalidae | *Charaxes* |
| `025` | **Yellow Rajah** | *Charaxes marmax* | Nymphalidae | *Charaxes* |
| `026` | **Common Maplet** | *Chersonesia risa* | Nymphalidae | *Chersonesia* |
| `027` | **Tawny Emperor** | *Chitoria ulupi* | Nymphalidae | *Chitoria* |
| `028` | **Large Yeoman** | *Cirrochroa aoris* | Nymphalidae | *Cirrochroa* |
| `029` | **Rustic** | *Cupha erymanthis* | Nymphalidae | *Cupha* |
| `030` | **Bright Sunbeam** | *Curetis bulis* | Lycaenidae | *Curetis* |
| `031` | **Common Map** | *Cyrestis thyodamas* | Nymphalidae | *Cyrestis* |
| `032` | **Red-spot Jezebel** | *Delias descombesi* | Pieridae | *Delias* |
| `033` | **Red-base Jezebel** | *Delias pasithoe* | Pieridae | *Delias* |
| `034` | **Autumn Leaf** | *Doleschallia bisaltide* | Nymphalidae | *Doleschallia* |
| `035` | **Spotted Palmfly** | *Elymnias malelas* | Nymphalidae | *Elymnias* |
| `036` | **One-spot Grass Yellow** | *Eurema andersoni* | Pieridae | *Eurema* |
| `037` | **Small Grass Yellow** | *Eurema brigitta* | Pieridae | *Eurema* |
| `038` | **Gaudy Baron** | *Euthalia lubentina* | Nymphalidae | *Euthalia* |
| `039` | **Powdered Baron** | *Euthalia monina* | Nymphalidae | *Euthalia* |
| `040` | **Common Awl** | *Hasora badra* | Hesperiidae | *Hasora* |
| `041` | **Common Banded Awl** | *Hasora chromus* | Hesperiidae | *Hasora* |
| `042` | **Golden Sapphire** | *Heliophorus brahma* | Lycaenidae | *Heliophorus* |
| `043` | **Purple Sapphire** | *Heliophorus epicles* | Lycaenidae | *Heliophorus* |
| `044` | **Great Eggfly** | *Hypolimnas bolina* | Nymphalidae | *Hypolimnas* |
| `045` | **Danaid Eggfly** | *Hypolimnas misippus* | Nymphalidae | *Hypolimnas* |
| `046` | **Metallic Cerulean** | *Jamides alecto* | Lycaenidae | *Jamides* |
| `047` | **Dark Cerulean** | *Jamides bochus* | Lycaenidae | *Jamides* |
| `048` | **Peacock Pansy** | *Junonia almana* | Nymphalidae | *Junonia* |
| `049` | **Grey Pansy** | *Junonia atlites* | Nymphalidae | *Junonia* |
| `050` | **Yellow Pansy** | *Junonia hierta* | Nymphalidae | *Junonia* |
| `051` | **Lemon Pansy** | *Junonia lemonias* | Nymphalidae | *Junonia* |
| `052` | **Orange Oakleaf** | *Kallima inachus* | Nymphalidae | *Kallima* |
| `053` | **Banded Treebrown** | *Lethe confusa* | Nymphalidae | *Lethe* |
| `054` | **Bamboo Treebrown** | *Lethe europa* | Nymphalidae | *Lethe* |
| `055` | **European Beak** | *Libythea celtis* | Nymphalidae | *Libythea* |
| `056` | **Yamfly** | *Loxura atymnus* | Lycaenidae | *Loxura* |
| `057` | **Commander** | *Moduza procris* | Nymphalidae | *Moduza* |
| `058` | **Dark Brand Bushbrown** | *Mycalesis mineus* | Nymphalidae | *Mycalesis* |
| `059` | **Common Sailer** | *Neptis hylas* | Nymphalidae | *Neptis* |
| `060` | **Chestnut-streaked Sailer** | *Neptis jumbah* | Nymphalidae | *Neptis* |
| `061` | **Restricted Demon** | *Notocrypta curvifascia* | Hesperiidae | *Notocrypta* |
| `062` | **Lime Butterfly** | *Papilio demoleus* | Papilionidae | *Papilio* |
| `063` | **Great Mormon** | *Papilio memnon* | Papilionidae | *Papilio* |
| `064` | **Blue Mormon** | *Papilio polymnestor* | Papilionidae | *Papilio* |
| `065` | **Glassy Tiger** | *Parantica aglea* | Nymphalidae | *Parantica* |
| `066` | **Coon** | *Psolos fuligo* | Hesperiidae | *Psolos* |
| `067` | **Common Silverline** | *Spindasis vulcanus* | Lycaenidae | *Spindasis* |
| `068` | **Large Snow Flat** | *Tagiades gana* | Hesperiidae | *Tagiades* |
| `069` | **Water Snow Flat** | *Tagiades litigiosa* | Hesperiidae | *Tagiades* |
| `070` | **Dark Pierrot** | *Tarucus ananda* | Lycaenidae | *Tarucus* |
| `071` | **Blue Tiger** | *Tirumala limniace* | Nymphalidae | *Tirumala* |
| `072` | **Golden Birdwing** | *Troides aeacus* | Papilionidae | *Troides* |
| `073` | **Common Birdwing** | *Troides helena* | Papilionidae | *Troides* |
| `074` | **Grass Demon** | *Udaspes folus* | Hesperiidae | *Udaspes* |
| `075` | **Cruiser** | *Vindula erota* | Nymphalidae | *Vindula* |
| `076` | **Common Guava Blue** | *Virachola isocrates* | Lycaenidae | *Virachola* |
| `077` | **Common Fivering** | *Ypthima baldus* | Nymphalidae | *Ypthima* |
| `078` | **Common Fourring** | *Ypthima huebneri* | Nymphalidae | *Ypthima* |
| `079` | **Punchinello** | *Zemeros flegyas* | Riodinidae | *Zemeros* |
| `080` | **Three-spot Palmfly** | *Yasuda tripunctata* | Nymphalidae | *Yasuda* |
| `081` | **Basar Duke** | *Euthalia zubeengargi* | Nymphalidae | *Euthalia* |

---

## 7. Embedded REST API Reference

The embedded HTTP server runs on `http://localhost:8080`.

### 1. `GET /` — Web Client Handler
Serves `index.html`, `styles.css`, and `app.js` with appropriate MIME types.

### 2. `GET /api/species` — Species Catalog
Returns a JSON array containing biological taxonomy, habitat, geographical distribution, and sample image pointers for all 81 species.

### 3. `POST /api/classify` — Image Classification
Accepts raw image bytes or multipart payload with an optional `X-File-Name` header.

**Sample JSON Response**:
```json
{
  "success": true,
  "primary": {
    "id": "081",
    "commonName": "Basar Duke",
    "scientificName": "Euthalia zubeengargi",
    "confidence": 94.6,
    "family": "Nymphalidae",
    "genus": "Euthalia",
    "speciesName": "E. zubeengargi",
    "habitat": "Dense tropical wet evergreen rainforests & subtropical hill tracts",
    "distribution": "Eastern Himalayas, Arunachal Pradesh (Basar region), Northeast India",
    "description": "Rare brush-footed nymphalid with deep forest camouflage and iridescent green-bronze bands."
  },
  "predictions": [
    { "rank": 1, "commonName": "Basar Duke", "scientificName": "Euthalia zubeengargi", "confidence": 94.6 },
    { "rank": 2, "commonName": "Gaudy Baron", "scientificName": "Euthalia lubentina", "confidence": 2.4 },
    { "rank": 3, "commonName": "Powdered Baron", "scientificName": "Euthalia monina", "confidence": 1.1 },
    { "rank": 4, "commonName": "Common Sailer", "scientificName": "Neptis hylas", "confidence": 0.7 },
    { "rank": 5, "commonName": "Commander", "scientificName": "Moduza procris", "confidence": 0.4 }
  ]
}
```

### 4. `GET /api/sample?path={path}` — Sample Images
Serves local benchmark images directly to the frontend for one-click testing.

---

## 8. Build, Execution & Deployment

### Quick Start (Windows)
```cmd
build.bat
run.bat
```

### Quick Start (Linux / macOS)
```bash
chmod +x build.sh run.sh
./build.sh
./run.sh
```

### Maven Build
```cmd
mvn clean compile
mvn exec:java
```

---

## 9. Generated Artifacts & Reports

- **Comparative Analysis Word Document (`Butterfly_Classifier_Model_Comparison.docx`)**: Comprehensive academic document comparing MobileNetV2, ResNet50, and Custom CNN with formatted tables and metric justifications.
- **Presentation Deck (`Butterfly_Species_Classifier_Presentation.pptx`)**: Complete 16:9 widescreen presentation slide deck.
- **Executive Presentation Deck (`Butterfly_Classifier_3_Slide_Intro.pptx`)**: 3-slide executive summary presentation.

---

## Summary of Accomplishments

| Component | Status | Description |
| :--- | :---: | :--- |
| **81 Species Taxonomy** | ✅ Complete | Complete biological metadata store, enum, and UI integration. |
| **Two-Phase Deep Learning** | ✅ Complete | MobileNetV2 fine-tuned with 97.39% train and 93.20% Top-5 test accuracy. |
| **Sub-Second IPC Daemon** | ✅ Complete | Persistent Python stdin/stdout daemon achieving ~0.4s response times. |
| **TensorFlow Lite Compilation** | ✅ Complete | 9.3 MB FlatBuffer export enabling sub-50ms CPU execution. |
| **Embedded Java Web Server** | ✅ Complete | Multi-threaded JDK HttpServer with REST endpoints. |
| **Responsive Web Frontend** | ✅ Complete | Dark Nature theme, drag-and-drop, sample carousel, and Top-5 meters. |
| **Git & GitHub Exclusions** | ✅ Complete | Complete exclusion of all PPTX, DOCX, images, and model binaries. |
