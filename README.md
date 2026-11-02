# Rare Butterfly Species Classifier: Assam and Northeast India Biodiversity

A computer vision application built to identify, document, and study butterfly and moth species, with a dedicated focus on the rare, endemic, and cryptic Lepidoptera of Assam and the greater Indo-Burma biodiversity hotspot.

The project pairs a fine-tuned MobileNetV2 deep learning model with an embedded Java server and a local web interface, allowing researchers, students, and naturalists to identify species directly from field photographs without requiring internet access or cloud services.

For technical architecture details, API route specifications, and design choices, refer to [PROJECT_DETAILS.md](PROJECT_DETAILS.md).

---

## What the System Does

ButterflyAI is designed as an end-to-end identification, taxonomy, and dataset research tool. Its core capabilities include:

1. **Deep Learning Image Classification**
   - Employs a fine-tuned MobileNetV2 convolutional neural network trained on more than 4,500 curated Lepidopteran images across 125 distinct species classes.
   - Processes input images through data augmentation layers (random rotation, zoom, horizontal flips) and normalized tensor inputs.
   - Delivers top ranked predictions with percentage confidence scores and ranked probability distributions.

2. **Full Biological Taxonomy and Field Notes**
   - Automatically retrieves full biological classification for every recognized species: Kingdom, Phylum, Class, Order, Family, Genus, and Species.
   - Displays ecological context including natural habitat preferences (such as primary rainforest canopy, riverine grasslands, or bamboo undergrowth) and documented geographic distribution across Indo-Malayan bioregions.

3. **Interactive Local Web Interface**
   - Responsive, dark-themed UI built with clean HTML5, CSS3, and modern JavaScript.
   - Drag-and-drop photo uploading with immediate client-side image preview and dimension detection.
   - Visual probability bars for top predictions and a one-click sample image browser for quick testing.

4. **Embedded Desktop Server and Control Panel**
   - Powered by an embedded Java `HttpServer` running directly inside the JVM without external web containers.
   - Includes a lightweight Java Swing controller window that handles port management, monitors background threads, and automatically opens the user's default browser on startup.

5. **Automated Dataset Extraction and Structuring Pipeline**
   - Includes `scripts/extract_structure_dataset.py`, which automates adding any new species to the dataset.
   - Automatically searches multiple biological image queries, downloads candidates, filters out corrupt files using PIL verification, and enforces a minimum threshold of 30 clean images.
   - Splits images into standard 80% training and 20% validation directories, formats file names sequentially (`0810001.jpg`, etc.), and updates labels and Java code automatically.

6. **Self-Contained Retraining Engine**
   - Includes `train_model.py` and `train.sh` for one-command model retraining.
   - Trains a two-phase transfer learning pipeline: frozen MobileNetV2 base followed by fine-tuning of upper convolutional layers with learning rate scheduling.
   - Always builds from official ImageNet weights to prevent weight accumulation artifacts and catastrophic forgetting.

7. **Zero-Crash Dual Inference Engine**
   - Primary: Fast Python bridge calling the trained MobileNetV2 native `.keras` neural network.
   - Fallback: Built-in pure Java color distribution and visual feature extractor that guarantees the application remains responsive even if Python or model weights are missing.

---

## Background and Research Context

Northeast India, especially the state of Assam, represents one of the world's richest biodiversity hotspots. From the lowland tropical rainforests of Dehing Patkai and the floodplains of Kaziranga and Manas to the hill tracts of the Barail and Karbi Anglong ranges, the region harbors hundreds of rare Lepidopteran species. Many of these butterflies spend their lives in high forest canopies or dense bamboo undergrowth and are rarely photographed or documented outside academic survey papers.

In field conditions, identifying these species by sight is notoriously challenging. Subtle variations in submarginal spots, ventral wing bands, antennae shape, and scale coloration often separate common species from endangered or newly discovered endemics. Mimetic complexes—such as swallowtails mimicking unpalatable Danaine crows—further complicate rapid visual assessment.

This project originated as a software tool inspired by research on the rare butterfly fauna of Assam. Its objective is to bridge computational computer vision and field taxonomy, providing an offline tool that helps researchers verify sightings and document rare species.

---

## Spotlight on Rare Species of Assam

The model is trained on 125 classes, with extensive coverage of rare, localized, and canopy-adapted butterflies of Assam and Northeast India:

- **Euthalia zubeengargi (Zubeen's Baron)**
  A recently described nymphalid species native to the rainforest margins of Upper Assam. Discovered and described in 2024 from the Panbari Reserve Forest in the Kaziranga landscape, it was named in honor of Assamese cultural icon and artist Zubeen Garg. It features dark olive-green marbling, white submarginal patches, and cryptic ventral coloration. Its dataset has been specially enriched with high-resolution field photographs and museum specimens to ensure robust identification across variable lighting conditions.

- **Teinopalpus imperialis (Kaiser-i-Hind)**
  One of the most revered swallowtail butterflies in the world, legally protected under Schedule II of the Indian Wildlife (Protection) Act. Inhabits high montane broadleaf canopies and cloud forest ridges above 2,000 meters in the Eastern Himalayas and hill tracts of Assam. Recognized by its shimmering iridescent green scales, curved tails, and rapid flight.

- **Elymnias peali (Peal's Palmfly)**
  One of the rarest satyrine butterflies in existence, originally discovered at Margherita in Upper Assam by naturalist S.E. Peal. Restricted to shaded bamboo brakes and dense evergreen understorey, this cryptic species is rarely encountered in the wild.

- **Papilio elephenor (Yellow-crested Spangle)**
  An extremely rare swallowtail endemic to Assam and Meghalaya. Noted for its distinctive yellow-crested scaling on dark forewings and spatulate hindwing tails, representing a key bioindicator of primary sub-Himalayan rainforest health.

- **Lamproptera curius (White Dragontail) & Lamproptera meges (Green Dragontail)**
  Extraordinary miniature swallowtails characterized by transparent glass-like wing windows and elongated dragonfly-like tails. They hover rapidly over rocky streams and gravel bars in the tropical rainforests of Assam and Arunachal Pradesh.

- **Meandrusa payeni (Yellow Gorgon) & Meandrusa lachinus (Brown Gorgon)**
  High-canopy sickle-winged swallowtails whose jagged wing outlines and muted saffron and brown hues provide camouflage against autumn leaves on windy mountain peaks.

- **Charaxes delphis (Jewelled Nawab) & Polyura schreiber (Blue Nawab)**
  Powerful canopy nymphalids with robust bodies and aggressive, territorial flight. The Jewelled Nawab features shimmering mother-of-pearl undersides, while the Blue Nawab displays deep turquoise-blue discal bands.

- **Pantoporia assamica (Conjoined Lascar)**
  A regional endemic lascar butterfly dwelling along shaded stream corridors in primary evergreen forests, recognized by its joined orange forewing bands.

- **Tajuria maculata (Spotted Royal) & Tajuria cippus (Peacock Royal)**
  Canopy-adapted members of the Lycaenidae family that spend most of their lifecycles around epiphytic mistletoes (Loranthaceae) high in the rainforest canopy.

- **Pyroneura margherita (Yellow-vein Lancer)**
  A rare hesperiid skipper whose type locality is the Margherita coalfield and rainforest belt of Upper Assam, distinguished by its radiant yellow wing veins.

- **Lethe satyavati (Pallid Forester)**
  An elusive satyrine butterfly originally described from Assam. Encounters in the wild remain rare due to its crepuscular habits and preference for shaded bamboo thickets.

- **Troides aeacus (Golden Birdwing)**
  One of the largest swallowtails in Asia, found along the foothill valleys of Assam and the Eastern Himalayas. Recognized by its brilliant golden-yellow hindwings, it serves as an important ecological indicator.

---

## All 125 Trained Species

The model has been trained and validated on the following 125 species, spanning major Lepidopteran families:

| ID | Scientific Name | Common Name | Family |
| :--- | :--- | :--- | :--- |
| 001 | *Danaus plexippus* | Monarch | Nymphalidae |
| 002 | *Heliconius charitonius* | Zebra Longwing | Nymphalidae |
| 003 | *Heliconius erato* | Red Passion | Nymphalidae |
| 004 | *Junonia coenia* | Common Buckeye | Nymphalidae |
| 005 | *Lycaena phlaeas* | Small Copper | Lycaenidae |
| 006 | *Nymphalis antiopa* | Mourning Cloak | Nymphalidae |
| 007 | *Papilio cresphontes* | Giant Swallowtail | Papilionidae |
| 008 | *Pieris rapae* | Cabbage White | Pieridae |
| 009 | *Vanessa atalanta* | Red Admiral | Nymphalidae |
| 010 | *Vanessa cardui* | Painted Lady | Nymphalidae |
| 011 | *Aeromachus pygmaeus* | Pygmy Scrub Hopper | Hesperiidae |
| 012 | *Ampittia dioscorides* | Bush Hopper | Hesperiidae |
| 013 | *Ancema blanka minturna* | Minturn Silverstreak | Lycaenidae |
| 014 | *Ancema ctesia ctesia* | Bi-spot Royal | Lycaenidae |
| 015 | *Anthene emolus emolus* | Ciliate Blue | Lycaenidae |
| 016 | *Anthene lycaenina lycambes* | Pointed Ciliate Blue | Lycaenidae |
| 017 | *Athyma perius* | Common Sergeant | Nymphalidae |
| 018 | *Badamia exclamationis* | Brown Awl | Hesperiidae |
| 019 | *Burara jaina* | Orange Awlet | Hesperiidae |
| 020 | *Caleta elna noliteia* | Elbowed Pierrot | Lycaenidae |
| 021 | *Catochrysops strabo strabo* | Forget-me-not | Lycaenidae |
| 022 | *Celaenorrhinus aurivittata aurivittata* | Yellow-banded Flat | Hesperiidae |
| 023 | *Celaenorrhinus leucocera* | Common Spotted Flat | Hesperiidae |
| 024 | *Cethosia cyane* | Leopard Lacewing | Nymphalidae |
| 025 | *Charaxes bernardus hierax* | Tawny Rajah | Nymphalidae |
| 026 | *Charaxes marmax marmax* | Yellow Rajah | Nymphalidae |
| 027 | *Chilades lajus lajus* | Lime Blue | Lycaenidae |
| 028 | *Choaspes benjaminii japonica* | Indian Awlking | Hesperiidae |
| 029 | *Cupitha purreea purreea* | Wax Dart | Hesperiidae |
| 030 | *Elymnias hypermnestra undularis* | Common Palmfly | Nymphalidae |
| 031 | *Elymnias nesaea* | Tiger Palmfly | Nymphalidae |
| 032 | *Ethope himachala* | Dusky Diadem | Nymphalidae |
| 033 | *Gerosis phisara phisara* | Great Yellow Sailer | Hesperiidae |
| 034 | *Graphium agamemnon* | Tailed Jay | Papilionidae |
| 035 | *Halpe aucma* | Gold-spotted Ace | Hesperiidae |
| 036 | *Halpe kusala* | Plain Ace | Hesperiidae |
| 037 | *Halpe porus porus* | Moore's Ace | Hesperiidae |
| 038 | *Halpe zema zema* | Zema Ace | Hesperiidae |
| 039 | *Hasora badra* | Common Awl | Hesperiidae |
| 040 | *Heliophorus epicles latilimbata* | Purple Sapphire | Lycaenidae |
| 041 | *Jamides caerulea* | Sky Blue | Lycaenidae |
| 042 | *Jamides celeno* | Common Cerulean | Lycaenidae |
| 043 | *Jamides elpis pseudelpis* | Glistening Cerulean | Lycaenidae |
| 044 | *Lethe chandica flanona* | Angled Red Forester | Nymphalidae |
| 045 | *Lethe mekara mekara* | Common Treebrown | Nymphalidae |
| 046 | *Lethe satyavati* | Pallid Forester | Nymphalidae |
| 047 | *Lethe vindhya vindhya* | Black Forester | Nymphalidae |
| 048 | *Loxura atymnus continentalis* | Yamfly | Lycaenidae |
| 049 | *Megisba malaya sikkima* | Malayan | Lycaenidae |
| 050 | *Mooreana trichoneura pralaya* | Yellow Flat | Hesperiidae |
| 051 | *Nacaduba kurava euplea* | Transparent 6-Line Blue | Lycaenidae |
| 052 | *Neopithecops zalmora zalmora* | Common Quaker | Lycaenidae |
| 053 | *Notocrypta curvifascia curvifascia* | Common Banded Demon | Hesperiidae |
| 054 | *Notocrypta paralysos asawa* | Grass Demon | Hesperiidae |
| 055 | *Ochus subvittatus subradiatus* | Tiger Hopper | Hesperiidae |
| 056 | *Odontoptilum angulata angulata* | Chestnut Angle | Hesperiidae |
| 057 | *Oriens gola pseudolus* | Common Dartlet | Hesperiidae |
| 058 | *Papilio paris* | Paris Peacock | Papilionidae |
| 059 | *Pithauria stramineipennis* | Light Straw Ace | Hesperiidae |
| 060 | *Potanthus pseudomaesa* | Indian Dart | Hesperiidae |
| 061 | *Prosotas aluta coelestis* | Banded Lineblue | Lycaenidae |
| 062 | *Prosotas bhutea* | Bhutya Lineblue | Lycaenidae |
| 063 | *Prosotas dubiosa indica* | Tailless Lineblue | Lycaenidae |
| 064 | *Prosotas nora ardates* | Common Lineblue | Lycaenidae |
| 065 | *Pseudocoladenia dan fabia* | Fulvous Pied Flat | Hesperiidae |
| 066 | *Psolos fuligo subfasciatus* | Coon | Hesperiidae |
| 067 | *Remelana jangala ravata* | Chocolate Royal | Lycaenidae |
| 068 | *Sarangesa dasahara dasahara* | Common Small Flat | Hesperiidae |
| 069 | *Sebastonyma dolopia* | Tufted Ace | Hesperiidae |
| 070 | *Seseria sambara sambara* | Notched Flat | Hesperiidae |
| 071 | *Spindasis lohita himalayanus* | Long-banded Silverline | Lycaenidae |
| 072 | *Surendra quercetorum quercetorum* | Common Acacia Blue | Lycaenidae |
| 073 | *Tagiades dynamicus ravi* | Ravi Snow Flat | Hesperiidae |
| 074 | *Tagiades gana gana* | Suffused Snow Flat | Hesperiidae |
| 075 | *Tagiades litigiosa litigiosa* | Water Snow Flat | Hesperiidae |
| 076 | *Telicota bambusae bambusae* | Dark Palm Dart | Hesperiidae |
| 077 | *Telicota colon* | Pale Palm Dart | Hesperiidae |
| 078 | *Thoressa cerata* | Northern Spangle | Hesperiidae |
| 079 | *Troides aeacus* | Golden Birdwing | Papilionidae |
| 080 | *Yasuda tripunctata tripunctata* | Three-spot Silverstreak | Lycaenidae |
| 081 | *Euthalia zubeengargi* | Zubeen's Baron | Nymphalidae |
| 082 | *Papilio elephenor* | Yellow-crested Spangle | Papilionidae |
| 083 | *Papilio paradoxa* | Great Blue Mime | Papilionidae |
| 084 | *Papilio bootes* | Tailed Redbreast | Papilionidae |
| 085 | *Papilio slateri* | Blue-striped Mime | Papilionidae |
| 086 | *Lamproptera curius* | White Dragontail | Papilionidae |
| 087 | *Lamproptera meges* | Green Dragontail | Papilionidae |
| 088 | *Meandrusa payeni* | Yellow Gorgon | Papilionidae |
| 089 | *Meandrusa lachinus* | Brown Gorgon | Papilionidae |
| 090 | *Byasa crassipes* | Black Windmill | Papilionidae |
| 091 | *Byasa nevilli* | Nevill's Windmill | Papilionidae |
| 092 | *Byasa polla* | De Nicéville's Windmill | Papilionidae |
| 093 | *Graphium agetes* | Fourbar Swallowtail | Papilionidae |
| 094 | *Graphium aristeus* | Chain Swordtail | Papilionidae |
| 095 | *Graphium macareus* | Lesser Zebra | Papilionidae |
| 096 | *Graphium xenocles* | Great Zebra | Papilionidae |
| 097 | *Losaria doubledayi* | Common Clubtail | Papilionidae |
| 098 | *Teinopalpus imperialis* | Kaiser-i-Hind | Papilionidae |
| 099 | *Elymnias peali* | Peal's Palmfly | Nymphalidae |
| 100 | *Euthalia telchinia* | Blue Baron | Nymphalidae |
| 101 | *Charaxes delphis* | Jewelled Nawab | Nymphalidae |
| 102 | *Pantoporia assamica* | Conjoined Lascar | Nymphalidae |
| 103 | *Pantoporia bieti* | Tytler's Lascar | Nymphalidae |
| 104 | *Chersonesia rahria* | Wavy Maplet | Nymphalidae |
| 105 | *Athyma ranga* | Blackvein Sergeant | Nymphalidae |
| 106 | *Athyma pravara* | Unbroken Sergeant | Nymphalidae |
| 107 | *Athyma punctata* | White-bordered Sergeant | Nymphalidae |
| 108 | *Polyura schreiber* | Blue Nawab | Nymphalidae |
| 109 | *Tajuria maculata* | Spotted Royal | Lycaenidae |
| 110 | *Tajuria cippus* | Peacock Royal | Lycaenidae |
| 111 | *Pithecops fulgens* | Blue Quaker | Lycaenidae |
| 112 | *Shijimia moorei* | Moore's Cupid | Lycaenidae |
| 113 | *Arhopala silhetensis* | Sylhet Oakblue | Lycaenidae |
| 114 | *Arhopala oenea* | Hewitson's Dull Oakblue | Lycaenidae |
| 115 | *Simiskina phalena* | Broad-branded Brilliant | Lycaenidae |
| 116 | *Udara selma* | Bi-coloured Hedge Blue | Lycaenidae |
| 117 | *Poritia hewitsoni* | Common Gem | Lycaenidae |
| 118 | *Capila pieridoides* | White Dawnfly | Hesperiidae |
| 119 | *Pyroneura margherita* | Yellow-vein Lancer | Hesperiidae |
| 120 | *Darpa pteria* | Snowy Angle | Hesperiidae |
| 121 | *Hidari bhawani* | Veined Palmer | Hesperiidae |
| 122 | *Plastingia naga* | Chequered Lancer | Hesperiidae |
| 123 | *Salanoemia sala* | Maculate Lancer | Hesperiidae |
| 124 | *Scobura woolletti* | Brown Forest Bob | Hesperiidae |
| 125 | *Polytremis minuta* | Baby Swift | Hesperiidae |

---

## How to Build and Run

### Prerequisites

- **Java**: JDK 17 or JDK 21 configured on your PATH (`java`, `javac`).
- **Python**: Python 3.10 to 3.12 (in `.venv` with `tensorflow`, `numpy`, and `pillow`).

### Quick Start (macOS & Linux)

1. Ensure the scripts are executable:
   ```bash
   chmod +x build.sh run.sh train.sh
   ```

2. Compile the Java source files:
   ```bash
   ./build.sh
   ```

3. Launch the application:
   ```bash
   ./run.sh
   ```

The script will launch the Java desktop window and open `http://localhost:8080` in your web browser.

### Quick Start (Windows)

1. Compile the project:
   ```cmd
   build.bat
   ```

2. Run the application:
   ```cmd
   run.bat
   ```

---

## Adding New Species and Retraining

The project is structured so that you can easily add more butterfly or moth species without manual file renaming or data partitioning.

### 1. Extract and Structure Images Automatically

Open `scripts/extract_structure_dataset.py` and add your species to `TARGET_SPECIES`:

```python
TARGET_SPECIES = [
    "Euthalia zubeengargi",
    "Actias luna",       # Luna Moth
    "Attacus atlas",     # Atlas Moth
]
```

Run the script:

```bash
.venv/bin/python scripts/extract_structure_dataset.py
```

The script will:
- Query image sources across biological and field terms.
- Validate image integrity, remove corrupted files, and ensure at least 30 clean images are collected.
- Assign the next numeric class folder (e.g. `126_Actias_luna`).
- Partition images into 80% `dataset/train/` and 20% `dataset/test/` with standard sequential naming.
- Update `model/labels.txt`, regenerate `Species.java` and `SpeciesInfo.java`, and recompile the project.

### 2. Retraining the Neural Network

To retrain MobileNetV2 on the updated dataset:

```bash
./train.sh
```

**Retraining Details**:
- Re-initializes from official ImageNet weights and builds a new classification head matching the updated class count.
- Trains across all classes simultaneously to prevent catastrophic forgetting and avoid weight accumulation from previous runs.
- Automatically saves the trained weights to `model/butterfly_species_model.keras` and updates `model/labels.txt`.

---

## Project Structure

```
JAVA-AI-Project/
├── src/main/java/com/butterfly/classifier/
│   ├── ButterflyClassifierApp.java    # Desktop Swing controller and browser auto-launcher
│   ├── ButterflyWebServer.java        # Embedded HTTP server and REST endpoints
│   ├── SpeciesModel.java              # Python AI bridge with Java fallback inference
│   ├── SpeciesInfo.java               # Taxonomy, habitat notes, and distribution store (125 species)
│   ├── Species.java                   # Enumeration of all registered species (125 classes)
│   └── DatasetPreparer.java           # Standalone dataset partitioning utility
├── src/main/resources/web/
│   ├── index.html                     # Web application structure
│   ├── styles.css                     # Dark nature theme and responsive styles
│   └── app.js                         # Frontend controller and asynchronous API client
├── scripts/
│   ├── extract_structure_dataset.py   # Automated image scraping, validation, and structuring
│   ├── download_and_structure_rare_species.py # Dedicated downloader for Assam rare fauna
│   ├── predict_image.py               # Python deep learning inference bridge
│   ├── generate_java_species.py       # Code generator for Species.java and SpeciesInfo.java
│   └── restructure_dataset.py         # Batch normalization utility for folder structures
├── dataset/
│   ├── train/                         # Structured training images partitioned by species (125 classes)
│   └── test/                          # Structured test images partitioned by species (125 classes)
├── model/
│   ├── butterfly_species_model.keras  # Trained MobileNetV2 weights (native Keras format)
│   ├── butterfly_species_model.h5     # Trained MobileNetV2 weights (HDF5 format)
│   └── labels.txt                     # Ordered class labels matching model output nodes (125 classes)
├── predict_image.py                   # Root alias of inference bridge
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
