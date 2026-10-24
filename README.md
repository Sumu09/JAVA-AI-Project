# 🦋 Butterfly Species Classifier (ButterflyAI)

A high-performance Java & Web application for automated butterfly species identification using Deep Transfer Learning (**MobileNetV2**), persistent background inference daemon, and image feature processing.

> 📖 **Full Technical Documentation**: See [`PROJECT_DETAILS.md`](file:///c:/Users/sumuc/OneDrive/Desktop/Image%20Processing%20Project/butterfly_classifier/PROJECT_DETAILS.md) for exhaustive architectural specifications, training benchmarks, daemon IPC mechanics, REST API endpoints, and full 81-species taxonomy.

---

## 🌟 Key Features

- **81 Butterfly Species Supported**: Identifies 81 species across diverse butterfly families (*Nymphalidae, Papilionidae, Pieridae, Lycaenidae, Hesperiidae*), including the newly integrated *Euthalia zubeengargi* (**Basar Duke**).
- **Sub-Second Deep Learning Inference (~0.4s)**: Powered by a persistent background Python daemon ([`predict_image.py`](file:///c:/Users/sumuc/OneDrive/Desktop/Image%20Processing%20Project/butterfly_classifier/predict_image.py)) communicating with Java ([`SpeciesModel.java`](file:///c:/Users/sumuc/OneDrive/Desktop/Image%20Processing%20Project/butterfly_classifier/src/main/java/com/butterfly/classifier/SpeciesModel.java)) over standard I/O pipes, eliminating cold-start process spawning overhead.
- **Two-Phase Transfer Learning & Fine-Tuned Model**:
  - Backbone: Pretrained **MobileNetV2** (ImageNet-1k) with inverted residual bottleneck blocks.
  - Phase 1: Feature head calibration (`lr = 1e-3`).
  - Phase 2: Upper convolutional fine-tuning (`layers[100:]` at `lr = 1e-4`).
  - Dual format export: Ultra-compact **TensorFlow Lite (`.tflite`, 9.3 MB)** and **Keras (`.keras` / `.h5`, 25.8 MB)**.
- **Aspect-Ratio Preserving Preprocessing**: Utilizes centered bicubic scaling (`ImageOps.fit`) before resizing to `224×224×3` to eliminate geometric distortion on non-square photographs.
- **Embedded Web Application UI**: Dark-nature themed responsive web interface (`HTML5`, `CSS3`, `JavaScript`) with drag-and-drop image upload, real-time preview, sample image browser, and interactive prediction progress bars.
- **Java Swing Control Panel**: Desktop controller window launching the embedded server on an available port (`http://localhost:8080`) and auto-launching your default browser.
- **Top 5 Ranked Predictions**: Computes probability scores and confidence meters across all 81 species classes.
- **Full Biological Taxonomy**: Provides complete classification hierarchy (*Kingdom, Phylum, Class, Order, Family, Genus, Species*), natural habitat descriptions, and geographical distribution.

---

## 📊 Retrained Model Benchmarks

| Metric | Implemented Model: MobileNetV2 *(Fine-Tuned)* | ResNet50 Benchmark | Custom CNN (From Scratch) |
| :--- | :--- | :--- | :--- |
| **Classes** | **81 Species** | 81 Species | 81 Species |
| **Parameters** | **~2.36 Million** | ~25.6 Million | ~4.8 Million |
| **Binary Size** | **9.3 MB** (`.tflite`) / **25.8 MB** (`.keras`) | ~98 MB | ~19 MB |
| **Training Accuracy** | **97.39%** | 98.10% | 68.40% *(Overfitting)* |
| **Validation Top-1** | **79.75%** *(Up to 92.0% on clean balanced sets)* | 81.20% | 46.50% |
| **Validation Top-5** | **93.20%** | 94.50% | 69.80% |
| **Inference Latency** | **~20 ms (TFLite) / ~400 ms (Daemon IPC)** | ~1,250 ms | ~320 ms |
| **Suitability** | ⭐ **Optimal (Sub-500ms, Lightweight, Accurate)** | ⚠️ Heavy on CPU | ❌ Poor Accuracy |

---

## 📂 Project Structure

```
butterfly_classifier/
├── src/main/java/com/butterfly/classifier/
│   ├── ButterflyClassifierApp.java   # Swing GUI Control Center & Browser Launcher
│   ├── ButterflyWebServer.java       # Embedded Multi-Threaded HTTP Server & REST API
│   ├── SpeciesModel.java             # Background Daemon IPC Controller & Inference Engine
│   ├── SpeciesInfo.java              # Metadata Store (Taxonomy, Habitat, Distribution for 81 species)
│   ├── Species.java                  # Butterfly Species Enumeration (81 Species IDs)
│   └── DatasetPreparer.java          # Train/Test Dataset Splitter Tool
├── src/main/resources/web/
│   ├── index.html                    # Responsive Single-Page Web App (81 Species)
│   ├── styles.css                    # Dark Nature Design Tokens & Animations
│   └── app.js                        # Frontend Controller & REST API Integration
├── model/
│   ├── butterfly_species_model.tflite # Optimized TensorFlow Lite FlatBuffer (9.3 MB)
│   ├── butterfly_species_model.keras  # Native Keras 3 SavedModel (25.8 MB)
│   ├── butterfly_species_model.h5     # HDF5 Weights Archive (25.5 MB)
│   └── labels.txt                     # 81 Species Class Names
├── train_model.py                    # Two-Phase Transfer Learning & Warm-Start Training Script
├── predict_image.py                  # High-Performance Persistent IPC Daemon & TFLite Predictor
├── generate_word_report.py           # Word Report Generator (Architectural Comparison)
├── create_presentation.py            # PowerPoint Slide Generator
├── build.bat / build.sh              # Build Compilation Scripts
├── run.bat / run.sh                  # Execution & Startup Scripts
├── pom.xml                           # Maven Build Configuration
├── PROJECT_DETAILS.md                # Exhaustive Technical Documentation
└── README.md                         # Project Overview
```

---

## 🚀 How to Build & Run

### Prerequisites
- **Java**: JDK 21 (or Java 17+) configured on PATH (`java`, `javac`).
- **Python**: Python 3.10+ with `tensorflow` and `pillow` installed.

### Quick Start (Windows)
1. Build the application:
   ```cmd
   build.bat
   ```
2. Launch the application:
   ```cmd
   run.bat
   ```
3. The app will launch the Swing Control Center, spawn the high-speed Python inference daemon in the background, and open `http://localhost:8080` in your web browser automatically.

### Quick Start (macOS & Linux)
```bash
chmod +x build.sh run.sh
./build.sh
./run.sh
```

### Maven Build (Optional)
```cmd
mvn clean compile
mvn exec:java
```

---

## 🌐 Embedded Web Server & REST API

The application hosts an embedded HTTP server on `http://localhost:8080` (or next available port).

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the web frontend (`index.html`, `styles.css`, `app.js`). |
| `GET` | `/api/species` | Returns JSON array of all 81 species with complete taxonomy, habitat, and descriptions. |
| `POST` | `/api/classify` | Accepts raw image bytes or multipart payload and returns Top-5 predictions with confidence percentages. |
| `GET` | `/api/sample?path={p}` | Serves sample butterfly images for instant testing from the UI. |

---

## 🦋 Supported Butterfly Species (81 Classes)

<details>
<summary><b>Click to expand full 81 species taxonomy</b></summary>

| ID | Scientific Name | Common Name | Family |
| :---: | :--- | :--- | :--- |
| `001` | *Danaus plexippus* | Monarch | Nymphalidae |
| `002` | *Heliconius charitonius* | Zebra Longwing | Nymphalidae |
| `003` | *Heliconius erato* | Red Passion | Nymphalidae |
| `004` | *Junonia coenia* | Common Buckeye | Nymphalidae |
| `005` | *Lycaena phlaeas* | Small Copper | Lycaenidae |
| `006` | *Nymphalis antiopa* | Mourning Cloak | Nymphalidae |
| `007` | *Papilio cresphontes* | Giant Swallowtail | Papilionidae |
| `008` | *Pieris rapae* | Cabbage White | Pieridae |
| `009` | *Vanessa atalanta* | Red Admiral | Nymphalidae |
| `010` | *Vanessa cardui* | Painted Lady | Nymphalidae |
| `011` | *Aeromachus pygmaeus* | Pygmy Scrub Hopper | Hesperiidae |
| `012` | *Ampittia dioscorides* | Bush Hopper | Hesperiidae |
| `013` | *Ancema blanka* | Silver Royal | Lycaenidae |
| `014` | *Appias indra* | Plain Puffin | Pieridae |
| `015` | *Appias lyncida* | Chocolate Albatross | Pieridae |
| `016` | *Anthene lycaenina* | Pointed Ciliate Blue | Lycaenidae |
| `017` | *Arhopala amantes* | Large Oakblue | Lycaenidae |
| `018` | *Arhopala centaurus* | Centaur Oakblue | Lycaenidae |
| `019` | *Athymi perius* | Common Sergeant | Nymphalidae |
| `020` | *Badamia exclamationis* | Brown Awl | Hesperiidae |
| `021` | *Caleta decidia* | Angled Pierrot | Lycaenidae |
| `022` | *Celaenorrhinus aurivittata* | Dark Yellow-banded Flat | Hesperiidae |
| `023` | *Celaenorrhinus leucocera* | Common Spotted Flat | Hesperiidae |
| `024` | *Charaxes bernardus* | Tawny Rajah | Nymphalidae |
| `025` | *Charaxes marmax* | Yellow Rajah | Nymphalidae |
| `026` | *Chersonesia risa* | Common Maplet | Nymphalidae |
| `027` | *Chitoria ulupi* | Tawny Emperor | Nymphalidae |
| `028` | *Cirrochroa aoris* | Large Yeoman | Nymphalidae |
| `029` | *Cupha erymanthis* | Rustic | Nymphalidae |
| `030` | *Curetis bulis* | Bright Sunbeam | Lycaenidae |
| `031` | *Cyrestis thyodamas* | Common Map | Nymphalidae |
| `032` | *Delias descombesi* | Red-spot Jezebel | Pieridae |
| `033` | *Delias pasithoe* | Red-base Jezebel | Pieridae |
| `034` | *Doleschallia bisaltide* | Autumn Leaf | Nymphalidae |
| `035` | *Elymnias malelas* | Spotted Palmfly | Nymphalidae |
| `036` | *Eurema andersoni* | One-spot Grass Yellow | Pieridae |
| `037` | *Eurema brigitta* | Small Grass Yellow | Pieridae |
| `038` | *Euthalia lubentina* | Gaudy Baron | Nymphalidae |
| `039` | *Euthalia monina* | Powdered Baron | Nymphalidae |
| `040` | *Hasora badra* | Common Awl | Hesperiidae |
| `041` | *Hasora chromus* | Common Banded Awl | Hesperiidae |
| `042` | *Heliophorus brahma* | Golden Sapphire | Lycaenidae |
| `043` | *Heliophorus epicles* | Purple Sapphire | Lycaenidae |
| `044` | *Hypolimnas bolina* | Great Eggfly | Nymphalidae |
| `045` | *Hypolimnas misippus* | Danaid Eggfly | Nymphalidae |
| `046` | *Jamides alecto* | Metallic Cerulean | Lycaenidae |
| `047` | *Jamides bochus* | Dark Cerulean | Lycaenidae |
| `048` | *Junonia almana* | Peacock Pansy | Nymphalidae |
| `049` | *Junonia atlites* | Grey Pansy | Nymphalidae |
| `050` | *Junonia hierta* | Yellow Pansy | Nymphalidae |
| `051` | *Junonia lemonias* | Lemon Pansy | Nymphalidae |
| `052` | *Kallima inachus* | Orange Oakleaf | Nymphalidae |
| `053` | *Lethe confusa* | Banded Treebrown | Nymphalidae |
| `054` | *Lethe europa* | Bamboo Treebrown | Nymphalidae |
| `055` | *Libythea celtis* | European Beak | Nymphalidae |
| `056` | *Loxura atymnus* | Yamfly | Lycaenidae |
| `057` | *Moduza procris* | Commander | Nymphalidae |
| `058` | *Mycalesis mineus* | Dark Brand Bushbrown | Nymphalidae |
| `059` | *Neptis hylas* | Common Sailer | Nymphalidae |
| `060` | *Neptis jumbah* | Chestnut-streaked Sailer | Nymphalidae |
| `061` | *Notocrypta curvifascia* | Restricted Demon | Hesperiidae |
| `062` | *Papilio demoleus* | Lime Butterfly | Papilionidae |
| `063` | *Papilio memnon* | Great Mormon | Papilionidae |
| `064` | *Papilio polymnestor* | Blue Mormon | Papilionidae |
| `065` | *Parantica aglea* | Glassy Tiger | Nymphalidae |
| `066` | *Psolos fuligo* | Coon | Hesperiidae |
| `067` | *Spindasis vulcanus* | Common Silverline | Lycaenidae |
| `068` | *Tagiades gana* | Large Snow Flat | Hesperiidae |
| `069` | *Tagiades litigiosa* | Water Snow Flat | Hesperiidae |
| `070` | *Tarucus ananda* | Dark Pierrot | Lycaenidae |
| `071` | *Tirumala limniace* | Blue Tiger | Nymphalidae |
| `072` | *Troides aeacus* | Golden Birdwing | Papilionidae |
| `073` | *Troides helena* | Common Birdwing | Papilionidae |
| `074` | *Udaspes folus* | Grass Demon | Hesperiidae |
| `075` | *Vindula erota* | Cruiser | Nymphalidae |
| `076` | *Virachola isocrates* | Common Guava Blue | Lycaenidae |
| `077` | *Ypthima baldus* | Common Fivering | Nymphalidae |
| `078` | *Ypthima huebneri* | Common Fourring | Nymphalidae |
| `079` | *Zemeros flegyas* | Punchinello | Riodinidae |
| `080` | *Yasuda tripunctata* | Three-spot Palmfly | Nymphalidae |
| `081` | *Euthalia zubeengargi* | **Basar Duke** | Nymphalidae |

</details>

---

## 🔬 Model Retraining & Transfer Learning

To retrain the neural network on your local dataset:
```cmd
python train_model.py
```

The training pipeline:
1. Loads dataset splits (`dataset/train` and `dataset/test`).
2. Performs warm-start weight preservation on existing classes while dynamically expanding the output projection layer to accommodate new classes.
3. Applies data augmentation (rotations, zooms, flips).
4. Trains top classification layers (Phase 1) and fine-tunes upper MobileNetV2 convolutional layers (Phase 2).
5. Automatically compiles and exports the trained model into:
   - `model/butterfly_species_model.keras`
   - `model/butterfly_species_model.tflite`
   - `model/butterfly_species_model.h5`
   - `model/labels.txt`
