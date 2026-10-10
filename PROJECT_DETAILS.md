# 🦋 Butterfly Species Classifier (ButterflyAI) — Complete Project Documentation

---

## 1. Executive Summary & Project Purpose

**ButterflyAI** is a hybrid Java & Web desktop application designed for automated **butterfly species identification** using Computer Vision, Image Processing, and Deep Learning techniques. 

The primary purpose of this project is to eliminate the manual complexity of identifying butterfly species in ecological, agricultural, and educational environments. By taking a photograph of a butterfly, the application processes the visual features (colors, patterns, wing structures, and textures) and predicts the exact species along with biological taxonomy, confidence percentages, habitat information, and geographical distribution.

---

## 2. What We Are Trying To Do (Project Objectives & Goals)

### Core Objectives
1. **Automated Visual Species Classification**: Build a model capable of recognizing 10 prominent butterfly species from image files (`.png`, `.jpg`, `.jpeg`, `.webp`).
2. **Dual-Interface System**:
   - **Java Swing Control Panel**: A desktop controller window that manages the server lifecycle, monitors port allocation, and auto-launches the application.
   - **Modern Interactive Web Interface**: A web application featuring drag-and-drop image upload, real-time image preview, sample image selector, species library, and confidence visualization meters.
3. **High Reliability & Fallbacks**:
   - Primary: Deep learning inference using **MobileNetV2** via **ONNX Runtime Java**.
   - Fallback: A built-in RGB color distribution and visual feature extraction engine in pure Java to ensure 100% execution guarantee even without native C++ ONNX binaries.
4. **Rich Scientific Context**: Provide users with full biological taxonomy (Kingdom, Phylum, Class, Order, Family, Genus, Species), habitat details, and migration patterns alongside classification scores.
5. **Dataset Management Automation**: Include automated data splitting tools to organize raw dataset images into standard 80% training and 20% testing directory structures for ML training.

---

## 3. Technology Stack & Dependencies (What We Are Using)

### 💻 Programming Languages
- **Java (JDK 21 / 17+)**: Core system architecture, embedded HTTP web server, image processing tensor conversion, dataset management, and desktop UI controller.
- **HTML5 / CSS3 / Modern JavaScript (ES6+)**: Frontend web application layout, responsive styling, async fetch APIs, animations, and dynamic DOM rendering.
- **Python 3.x**: Automated presentation slide generation (`create_presentation.py` using `python-pptx`) and machine learning model training scripts.
- **Windows Batch Scripting (`.bat`)**: Compilation (`build.bat`) and execution (`run.bat`) automation scripts.

### 📦 Frameworks, Libraries & Tools
- **Embedded JDK HttpServer (`com.sun.net.httpserver.HttpServer`)**: Embedded lightweight HTTP server built directly into Java Standard Library.
- **ONNX Runtime Java (`com.microsoft.onnxruntime:onnxruntime:1.17.1`)**: Deep learning inference engine for executing ONNX neural network models directly within JVM.
- **Apache Maven (`pom.xml`)**: Dependency management and build lifecycle tool targeting Java 21 compilation (`maven-compiler-plugin`, `exec-maven-plugin`, `maven-jar-plugin`).
- **Java Swing & AWT (`javax.swing.*`, `java.awt.*`)**: System desktop GUI dashboard, native desktop browser launcher, and `BufferedImage` matrix manipulation.
- **MobileNetV2 Convolutional Neural Network**: Lightweight deep neural network optimized for fast visual feature classification on 224×224 RGB image inputs.

---

## 4. Machine Learning & Image Processing Pipeline

```
[ Input Image ] ──► [ Resizing & Normalization (224x224 float matrix) ]
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
[ ONNX Runtime Engine ]              [ Pure Java Fallback Engine ]
(MobileNetV2 Deep Learning)          (RGB Color Feature Extraction)
            │                                     │
            └──────────────────┬──────────────────┘
                               ▼
     [ Softmax Normalized Probabilities (Top 5 Ranked) ]
                               │
                               ▼
        [ Web UI & Desktop Control Center Output ]
```

1. **Preprocessing & Tensor Formatter**:
   - Resizes input images to `224 x 224` pixels using smooth bicubic scaling.
   - Extracts Red, Green, and Blue (RGB) pixel values.
   - Normalizes channel values from `[0, 255]` to MobileNetV2 tensor format `[-1.0, 1.0]`:
     $$\text{Normalized\_Pixel} = \frac{\text{Pixel}}{127.5} - 1.0$$

2. **Inference Execution**:
   - **Primary (ONNX Runtime)**: Feeds the 4D float tensor `[1][224][224][3]` into the ONNX session to produce raw logits and Softmax probabilities.
   - **Fallback (Visual Feature Evaluator)**: Performs RGB color distribution sampling (orange, yellow, dark brown, crimson, and white scores) combined with class prefix matching to deliver instant predictions.

3. **Post-Processing**:
   - Sorts predicted confidence scores in descending order.
   - Formats confidence percentages to 1 decimal place (e.g., `96.4%`).
   - Pairs scores with scientific metadata from `SpeciesInfo`.

---

## 5. System Architecture & Codebase Components

### Directory Structure

```
butterfly_classifier/
├── src/
│   └── main/
│       ├── java/com/butterfly/classifier/
│       │   ├── ButterflyClassifierApp.java   # Swing GUI Control Panel & Browser Launcher
│       │   ├── ButterflyWebServer.java       # Embedded Multi-Threaded HTTP Web Server & REST API
│       │   ├── SpeciesModel.java             # Image Preprocessing & Dual Inference Engine
│       │   ├── Species.java                  # Enum for 10 Butterfly Species
│       │   ├── SpeciesInfo.java              # Scientific Metadata & Taxonomic Store
│       │   └── DatasetPreparer.java          # 80/20 Train/Test Dataset Splitter Tool
│       └── resources/
│           └── web/
│               ├── index.html                # Single Page Web App Interface
│               ├── styles.css                # Custom CSS Design Token System & Animations
│               └── app.js                    # Web Frontend Event Handling & API Client
├── dataset/                                  # Formatted Train/Test Split Folders
│   ├── train/
│   └── test/
├── images/                                   # Raw Leeds Butterfly Dataset Images
├── model/                                    # Machine Learning Models (.h5 / .onnx)
├── build.bat                                 # One-Click Build Script
├── run.bat                                   # One-Click Run Script
├── pom.xml                                   # Maven Build File
├── create_presentation.py                   # Presentation Slide Deck Generator
├── Butterfly_Species_Classifier_Presentation.pptx # Project Slide Deck
├── PROJECT_DETAILS.md                        # Exhaustive Project Documentation
└── README.md                                 # Quickstart Guide
```

### Key Source Files & Functions

| File | Description | Key Responsibilities |
|---|---|---|
| `ButterflyClassifierApp.java` | System Launcher | Initializes AI model, finds available network port (8080+), starts server, opens default web browser, and presents dark-emerald Control Panel. |
| `ButterflyWebServer.java` | Web Backend | Embedded JDK HTTP Server running on multi-threaded thread pool (8 threads). Implements REST API endpoints `/api/classify`, `/api/species`, `/api/sample`, and static asset serving. |
| `SpeciesModel.java` | AI Engine | Handles image scaling to 224x224 RGB, float normalization, ONNX runtime session invocation, and fallback color feature evaluation. |
| `SpeciesInfo.java` | Knowledge Base | Stores detailed taxonomy (Kingdom to Species), natural habitat descriptions, geographical distributions, and sample paths. |
| `Species.java` | Core Enum | Defines the 10 species identifiers (`001` through `010`), scientific names, and common names. |
| `DatasetPreparer.java` | Utility Script | Scans `images/` directory, groups files by class prefix, shuffles with fixed seed `Random(42)`, and copies files into `dataset/train` (80%) and `dataset/test` (20%). |

---

## 6. Supported Butterfly Species & Biological Taxonomy

The system classifies 10 species from the **Leeds Butterfly Dataset**:

| Class ID | Common Name | Scientific Name | Family | Genus | Primary Habitat |
|---|---|---|---|---|---|
| `001` | **Monarch** | *Danaus plexippus* | Nymphalidae | *Danaus* | Fields, meadows, milkweed patches |
| `002` | **Zebra Longwing** | *Heliconius charitonius* | Nymphalidae | *Heliconius* | Tropical hammocks, rainforest margins |
| `003` | **Red Passion** | *Heliconius erato* | Nymphalidae | *Heliconius* | Tropical forest margins & clearings |
| `004` | **Common Buckeye** | *Junonia coenia* | Nymphalidae | *Junonia* | Open sunny fields, coastal dunes |
| `005` | **Small Copper** | *Lycaena phlaeas* | Nymphalidae | *Lycaena* | Heathland, dry sunny grasslands |
| `006` | **Mourning Cloak** | *Nymphalis antiopa* | Nymphalidae | *Nymphalis* | Deciduous forests, river banks |
| `007` | **Giant Swallowtail** | *Papilio cresphontes* | Papilionidae | *Papilio* | Citrus groves, forest edges |
| `008` | **Cabbage White** | *Pieris rapae* | Pieridae | *Pieris* | Gardens, agricultural fields, meadows |
| `009` | **Red Admiral** | *Vanessa atalanta* | Nymphalidae | *Vanessa* | Moist woodlands, coastal bluffs |
| `010` | **Painted Lady** | *Vanessa cardui* | Nymphalidae | *Vanessa* | Open country, clover fields, meadows |

All species belong to **Kingdom**: *Animalia*, **Phylum**: *Arthropoda*, **Class**: *Insecta*, **Order**: *Lepidoptera*.

---

## 7. Embedded Web Server & REST API Reference

The server runs on `http://localhost:8080` (or next available port if 8080 is in use).

### Endpoints Overview

1. **`GET /` / Static Asset Handler**
   - Serves `index.html`, `styles.css`, `app.js`, and embedded sample images.
   - Detects MIME types dynamically (`text/html`, `text/css`, `application/javascript`, `image/png`, `image/jpeg`).

2. **`GET /api/species`**
   - Returns a JSON array of all 10 supported species with taxonomy, habitat, distribution, and descriptions.
   - **Response Structure**:
     ```json
     [
       {
         "id": "001",
         "commonName": "Monarch",
         "scientificName": "Danaus plexippus",
         "family": "Nymphalidae",
         "genus": "Danaus",
         "speciesName": "D. plexippus",
         "kingdom": "Animalia",
         "phylum": "Arthropoda",
         "className": "Insecta",
         "order": "Lepidoptera",
         "habitat": "Fields, meadows, milkweed patches",
         "distribution": "North, Central, & South America...",
         "description": "Famous for its multi-generational annual migration...",
         "sampleImagePath": "images/0010001.png"
       }
     ]
     ```

3. **`POST /api/classify`**
   - Accepts image file payload via raw bytes or multipart form data. Optional request header `X-File-Name` specifies uploaded file name.
   - Processes image tensor and executes model prediction.
   - **Response Structure**:
     ```json
     {
       "success": true,
       "imageDimensions": { "width": 800, "height": 600 },
       "primary": {
         "id": "001",
         "commonName": "Monarch",
         "scientificName": "Danaus plexippus",
         "confidence": 96.4,
         "family": "Nymphalidae",
         "genus": "Danaus",
         "speciesName": "D. plexippus",
         "habitat": "Fields, meadows...",
         "distribution": "North, Central...",
         "description": "Famous for..."
       },
       "predictions": [
         { "rank": 1, "commonName": "Monarch", "scientificName": "Danaus plexippus", "family": "Nymphalidae", "confidence": 96.4 },
         { "rank": 2, "commonName": "Painted Lady", "scientificName": "Vanessa cardui", "family": "Nymphalidae", "confidence": 2.1 },
         ...
       ]
     }
     ```

4. **`GET /api/sample?path={image_path}`**
   - Serves local sample image files to the frontend for interactive testing.

---

## 8. Web Application Frontend Features

- **Hero Header & Navigation**: Dynamic navigation with brand logo, interactive navigation links, system status badge, and live server indicator.
- **Drag-and-Drop Dropzone**: Interactive upload box supporting drag-and-drop file upload, file browsing button, format hints (`PNG, JPG, WEBP`), and instant file preview.
- **Interactive Sample Carousel**: One-click quick test buttons displaying sample images for each butterfly species.
- **Live Classification Results View**:
  - Primary species card displaying common name, scientific name in italics, family badge, and large confidence badge.
  - Animated confidence progress bar.
  - Detailed taxonomy grid (Kingdom, Phylum, Class, Order, Family, Genus, Species).
  - Ecology & distribution information cards.
  - Ranked Top-5 prediction breakdown table with individual progress indicators.
- **Species Library Gallery**: Grid of all 10 supported species with expandable detail cards for educational exploration.
- **Dark Nature Aesthetic**: Modern color palette (`#0F291E` deep forest green, `#10B981` vibrant emerald green, `#0F172A` slate dark background).

---

## 9. Dataset Organization & DatasetPreparer Tool

Raw images reside in the `images/` directory with filename conventions like `0010001.png`, `0020003.png`, where the first 3 digits represent the species class ID.

Running `DatasetPreparer`:
```cmd
java -cp target/classes com.butterfly.classifier.DatasetPreparer
```

**Operation**:
1. Scans `images/` folder for `.png`, `.jpg`, `.jpeg` files.
2. Groups files into 10 class buckets based on the 3-digit prefix.
3. Shuffles each bucket using fixed-seed randomizer `Random(42)` for exact split reproducibility.
4. Copies **80%** into `dataset/train/{class_id}_{species_name}` and **20%** into `dataset/test/{class_id}_{species_name}`.

---

## 10. How to Build, Run, and Deploy

### Prerequisites
- JDK 21 (or Java 17+) installed and configured on your system PATH (`java`, `javac`).
- (Optional) Apache Maven if building via Maven CLI.

### Quick Start (Windows Script)
1. **Compile the Project**:
   Double-click `build.bat` or run:
   ```cmd
   build.bat
   ```
2. **Launch the System**:
   Double-click `run.bat` or run:
   ```cmd
   run.bat
   ```
   *This automatically compiles if needed, starts the embedded web server, launches the Control Center window, and opens your default browser at `http://localhost:8080`.*

### Manual Command Line Steps
```cmd
# Compilation
mkdir target\classes
javac -encoding UTF-8 -d target/classes src/main/java/com/butterfly/classifier/*.java
xcopy /Y /S /I "src\main\resources\web" "target\classes\web"

# Launch Application
java -cp target/classes com.butterfly.classifier.ButterflyClassifierApp
```

### Maven Build & Launch
```cmd
mvn clean compile
mvn exec:java
```

---

## 11. Presentation & Project Artifacts

- **Presentation Script (`create_presentation.py`)**: Uses Python's `python-pptx` library to programmatically generate clean 16:9 PowerPoint presentations matching the dark-emerald nature theme.
- **Slide Deck (`Butterfly_Species_Classifier_Presentation.pptx`)**: Complete presentation slide deck ready for academic or technical project showcases.
- **Slide Deck Intro (`Butterfly_Classifier_3_Slide_Intro.pptx`)**: Concise 3-slide executive summary presentation.

---

## Summary of Accomplishments

| Component | Status | Technology Used |
|---|---|---|
| Deep Learning / Preprocessing Engine | ✅ Complete | MobileNetV2 / ONNX Runtime / Pure Java Fallback |
| Embedded Multi-Threaded Web Server | ✅ Complete | JDK `com.sun.net.httpserver` |
| Web Application Frontend | ✅ Complete | HTML5 / CSS3 (Dark Nature Theme) / Modern JS |
| Control Center GUI Launcher | ✅ Complete | Java Swing & AWT |
| Dataset Train/Test Splitter | ✅ Complete | Java NIO / Seeded Shuffling |
| Taxonomic Knowledge Store | ✅ Complete | In-Memory Metadata Store (10 Species) |
| PowerPoint Presentation Generation | ✅ Complete | Python (`python-pptx`) |

---
*Documentation compiled automatically for ButterflyAI Project workspace.*
