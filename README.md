# Rare Butterfly Species Classifier: Assam and Northeast India Biodiversity

A computer vision application built to identify and document butterfly and moth species, with a particular focus on the rare, endemic, and cryptic Lepidoptera of Assam and the greater Indo-Burma biodiversity hotspot.

The application pairs a fine-tuned MobileNetV2 deep learning model with an embedded Java server and a local web interface, allowing field researchers, students, and naturalists to identify species from photographs without relying on external cloud APIs.

For detailed architecture notes, endpoint documentation, and technical design decisions, refer to [PROJECT_DETAILS.md](PROJECT_DETAILS.md).

---

## Background and Research Motivation

Northeast India, especially the state of Assam, is one of the world's most ecologically critical biodiversity hotspots. From the lowland rainforests of Dehing Patkai and the floodplains of Kaziranga and Manas to the lush hill tracts of the Barail and Karbi ranges, Assam shelters hundreds of butterfly species. Many of these are cryptic, canopy-dwelling, or rarely documented outside specialized entomological survey papers.

In field conditions, identifying these rare species by sight can be exceptionally difficult. Subtle variations in wing venation, scale coloration, submarginal spots, and ventral fascia often separate an ordinary skipper or nymphalid from an endangered or newly described species. 

This project began as a software tool inspired by research on the rare butterfly fauna of Assam. Its goal is to make identification practical and accurate by combining field taxonomy with transfer learning, giving researchers an immediate visual prediction alongside scientific classification, habitat notes, and known geographical distribution.

---

## Spotlight on Rare Species of Assam

The classifier includes 81+ distinct species. While it includes standard reference species for baseline benchmarking, the core of the dataset is dedicated to the rare, localized, and canopy-dwelling species documented across Assam and Northeast India:

- **Euthalia zubeengargi (Zubeen's Baron)**
  A recently described nymphalid butterfly native to the rainforest margins of Upper Assam. Named after the celebrated Assamese cultural icon and singer Zubeen Garg, this species exhibits delicate olive-green and brown marbling with distinctive submarginal markings on the ventral wing surface.

- **Lethe satyavati (Pallid Forester)**
  An exceptionally rare satyrine butterfly originally documented from Assam. Encounters in the wild remain infrequent due to its crepuscular habits and preference for shaded bamboo thickets and dense primary forest undergrowth.

- **Troides aeacus (Golden Birdwing)**
  One of the largest and most magnificent swallowtails in Asia. Found in the foothill forests of Assam and the Eastern Himalayas, its brilliant golden-yellow hindwings and soaring flight make it an ecological flagship species under active conservation monitoring.

- **Yasuda tripunctata tripunctata (Three-spot Silverstreak)** & **Ancema ctesia ctesia (Bi-spot Royal)**
  Elusive, fast-flying members of the Lycaenidae family that spend most of their lives in the forest canopy. Their cryptic underside bands of silver and metallic blue make visual confirmation difficult from ground-level observation.

- **Charaxes bernardus hierax (Tawny Rajah)** & **Charaxes marmax marmax (Yellow Rajah)**
  Powerful, canopy-adapted nymphalids found in undisturbed evergreen forest patches. They serve as reliable bioindicators of pristine forest ecosystems across the Brahmaputra valley and surrounding hills.

- **Ethope himachala (Dusky Diadem)**
  A localized, dark-winged satyrine species endemic to the moist deciduous and evergreen forests of Northeast India, recognizable by its pale post-discal ocular rings.

- **Rare Skippers and Flats (Hesperiidae)**
  Including *Mooreana trichoneura pralaya* (Yellow Flat), *Tagiades dynamicus ravi* (Ravi Snow Flat), *Choaspes benjaminii japonica* (Indian Awlking), and *Burara jaina* (Orange Awlet). These species inhabit shaded forest streams and ravines and are notorious for rapid, darting flight patterns that make photographic identification essential.

---

## How the Application Works

The system operates entirely on your local machine, making it suitable for field stations and offline research environments:

1. **User Interface (`src/main/resources/web/`)**
   A dark-themed, responsive web application built with clean HTML5, CSS, and modern JavaScript. Users can drag and drop field photographs, review an instant preview, browse sample images, and inspect confidence scores through interactive progress meters.

2. **Backend Application Server (`src/main/java/com/butterfly/classifier/`)**
   An embedded HTTP server running directly on top of the standard Java `HttpServer` library. It manages image uploads, serves the frontend assets, and exposes REST endpoints for predictions and taxonomy queries. A lightweight Java Swing window monitors port allocation and automatically launches your web browser.

3. **Inference Pipeline (`model/` & `scripts/predict_image.py`)**
   - **Deep Learning Engine (Primary)**: When Python and our virtual environment are available, the server invokes a fine-tuned MobileNetV2 convolutional neural network. The model runs image tensor inference and returns ranked probability distributions across all classes.
   - **Visual Feature Engine (Fallback)**: If Python is unavailable on a machine, the system uses an internal Java color-distribution and visual feature analyzer, ensuring the application remains testable and responsive in any environment.

---

## Getting Started

### Prerequisites

- **Java**: JDK 17 or JDK 21 installed and available on your PATH (`java`, `javac`).
- **Python**: Python 3.10 to 3.12 (recommended for running deep learning inference and training).

### Running on macOS and Linux

1. Make sure the scripts have executable permissions:
   ```bash
   chmod +x build.sh run.sh train.sh
   ```

2. Compile the Java application:
   ```bash
   ./build.sh
   ```

3. Launch the application:
   ```bash
   ./run.sh
   ```

The script will launch the embedded server and open `http://localhost:8080` in your web browser.

### Running on Windows

1. Compile the project:
   ```cmd
   build.bat
   ```

2. Start the application:
   ```cmd
   run.bat
   ```

### Building with Maven (Alternative)

```bash
mvn clean compile
mvn exec:java
```

---

## Adding New Species and Retraining

The project includes an end-to-end dataset pipeline designed to help researchers easily add more species (such as newly recorded regional butterflies, moths, or related insects).

### 1. Collect and Structure Images Automatically

Open `scripts/extract_structure_dataset.py` and append any target species to the list:

```python
TARGET_SPECIES = [
    "Euthalia zubeengargi",
    "Actias luna",       # Luna Moth
    "Attacus atlas",     # Atlas Moth
]
```

Run the extraction script:

```bash
.venv/bin/python scripts/extract_structure_dataset.py
```

What the script handles automatically:
- Searches across multiple biological and field query terms.
- Downloads candidates, validates file integrity with PIL, strips corrupt files, and verifies a minimum of 30 clean, non-corrupted images.
- Assigns the next numerical class index (for example, `082_Actias_luna`).
- Splits the images into 80% training (`dataset/train/`) and 20% validation (`dataset/test/`) using standardized naming (`0820001.jpg`, `0820002.jpg`, etc.).
- Updates `model/labels.txt`, regenerates `Species.java` and `SpeciesInfo.java`, and recompiles the Java backend.

### 2. Retraining the Neural Network

To retrain MobileNetV2 on the updated dataset:

```bash
./train.sh
```

**Training Safety & Accuracy**: Every training run re-initializes from official ImageNet weights and constructs a new classification head matching the exact number of active classes. It trains on the entire dataset simultaneously, which prevents catastrophic forgetting and eliminates the risk of weight accumulation or overfitting from repeated runs.

---

## Project Structure

```
JAVA-AI-Project/
├── src/main/java/com/butterfly/classifier/
│   ├── ButterflyClassifierApp.java    # Desktop Swing window and browser launcher
│   ├── ButterflyWebServer.java        # Embedded HTTP server and REST endpoints
│   ├── SpeciesModel.java              # Python AI bridge with Java fallback logic
│   ├── SpeciesInfo.java               # Taxonomy, habitat notes, and distribution store
│   ├── Species.java                   # Enumeration of all registered species
│   └── DatasetPreparer.java           # Standalone dataset partitioning utility
├── src/main/resources/web/
│   ├── index.html                     # Web application structure
│   ├── styles.css                     # Dark nature theme and responsive styles
│   └── app.js                         # Frontend controller and asynchronous API client
├── scripts/
│   ├── extract_structure_dataset.py   # Automated image scraping, validation, and structuring
│   ├── predict_image.py               # Standalone Python inference script for images
│   ├── generate_java_species.py       # Code generator for Species.java and SpeciesInfo.java
│   └── restructure_dataset.py         # Batch normalization utility for folder structures
├── dataset/
│   ├── train/                         # Structured training images partitioned by species
│   └── test/                          # Structured test images partitioned by species
├── model/
│   ├── butterfly_species_model.keras  # Trained MobileNetV2 weights (native Keras format)
│   └── labels.txt                     # Ordered class labels matching model output nodes
├── build.sh                           # Build script for macOS and Linux
├── run.sh                             # Run script for macOS and Linux
├── train.sh                           # Retraining launcher for macOS and Linux
├── build.bat                          # Build script for Windows
├── run.bat                            # Run script for Windows
├── pom.xml                            # Maven build configuration
├── PROJECT_DETAILS.md                 # Detailed technical documentation
└── README.md                          # Project overview and research guide
```

---

## Taxonomic Scope and Credits

This project synthesizes data from field observations, regional research papers on the butterfly biodiversity of Assam and Northeast India, and standard reference datasets (including the Leeds Butterfly Dataset used for baseline validation). It is developed for academic, ecological, and conservation research.
