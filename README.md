# 🦋 Butterfly Species Classifier (ButterflyAI)

A modern, high-performance Java & Web application for identifying butterfly species from images using Deep Learning (MobileNetV2) and Image Feature Processing.

> 📖 **Full Technical Documentation**: See [`PROJECT_DETAILS.md`](file:///c:/Users/sumuc/OneDrive/Desktop/Image%20Processing%20Project/butterfly_classifier/PROJECT_DETAILS.md) for exhaustive details on architecture, machine learning pipeline, REST API endpoints, taxonomy, and frontend components.

---

## 🌟 Key Features

- **Embedded Web Application UI**: A sleek, dark-nature themed responsive web interface (`HTML5`, `CSS3`, `JavaScript`) with drag-and-drop image upload, real-time preview, sample image browser, and interactive prediction progress bars.
- **Java Swing Control Panel**: Desktop controller window launching the embedded server on an available port (`http://localhost:8080`) and auto-launching your browser.
- **Dual Inference Engine**:
  - **Primary**: Deep Learning inference with MobileNetV2 via **ONNX Runtime Java**.
  - **Fallback**: Built-in RGB color distribution & visual feature extractor in pure Java to guarantee 100% functionality without native C++ binaries.
- **Full Biological Taxonomy**: Provides complete classification hierarchy (*Kingdom, Phylum, Class, Order, Family, Genus, Species*), natural habitat descriptions, and geographical distribution.
- **Top 5 Ranked Predictions**: Computes probability scores across all supported species classes.
- **Automated Dataset Organization**: Includes `DatasetPreparer` to split raw dataset images into reproducible 80% training and 20% testing directory structures.

---

## 🦋 Supported Butterfly Species (Leeds Dataset)

1. **Danaus plexippus** (Monarch)
2. **Heliconius charitonius** (Zebra Longwing)
3. **Heliconius erato** (Red Passion)
4. **Junonia coenia** (Common Buckeye)
5. **Lycaena phlaeas** (Small Copper)
6. **Nymphalis antiopa** (Mourning Cloak)
7. **Papilio cresphontes** (Giant Swallowtail)
8. **Pieris rapae** (Cabbage White)
9. **Vanessa atalanta** (Red Admiral)
10. **Vanessa cardui** (Painted Lady)

---

## 📂 Project Structure

```
butterfly_classifier/
├── src/main/java/com/butterfly/classifier/
│   ├── ButterflyClassifierApp.java   # Swing GUI & Browser Auto-Launcher
│   ├── ButterflyWebServer.java       # Embedded Multi-Threaded HTTP Server & REST API
│   ├── SpeciesModel.java             # Image Preprocessing & Dual Inference Engine
│   ├── SpeciesInfo.java              # Metadata Store (Taxonomy, Habitat, Distribution)
│   ├── Species.java                  # Butterfly Species Enumeration
│   └── DatasetPreparer.java          # 80/20 Train/Test Split Tool
├── src/main/resources/web/
│   ├── index.html                    # Web UI HTML Structure
│   ├── styles.css                    # Dark Nature Design Tokens & Animations
│   └── app.js                        # Frontend Controller & API Integration
├── build.bat                         # Windows Build Script
├── run.bat                           # Windows Launch Script
├── pom.xml                           # Maven Build Configuration
├── create_presentation.py            # PowerPoint Slide Generator
├── PROJECT_DETAILS.md                # Exhaustive Technical Documentation
└── README.md                         # Project Overview
```

---

## 🚀 How to Build & Run

### Prerequisites
- JDK 21 or Java 17+ configured on PATH (`java`, `javac`).

### Quick Start (macOS & Linux)
1. Build the project:
   ```bash
   chmod +x build.sh run.sh
   ./build.sh
   ```
2. Launch the app:
   ```bash
   ./run.sh
   ```

### Quick Start (Windows)
1. Build the project:
   ```cmd
   build.bat
   ```
2. Launch the app:
   ```cmd
   run.bat
   ```
3. The app will launch the Swing Control Center and open `http://localhost:8080` in your web browser automatically.

### Maven Command (Optional)
```cmd
mvn clean compile
mvn exec:java
```

### Dataset Splitter Tool
To split raw images into `dataset/train` (80%) and `dataset/test` (20%):
```cmd
java -cp target/classes com.butterfly.classifier.DatasetPreparer
```

