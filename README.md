git push -u origin main
# Butterfly Species Classifier (Java Edition)

A modern Java GUI desktop application for identifying butterfly species from images based on MobileNetV2 transfer learning.

## Features
- **Java Swing Desktop Interface**: Clean, styled UI matching modern color palettes (`#0D1B2A` header, `#00A896` primary teal, `#F0F4F8` background).
- **Asynchronous Execution**: Background model loading and non-blocking image inference using Java background workers.
- **Top 3 Classification**: Computes confidence scores and displays top 3 predicted species.
- **Dataset Management**: Includes `DatasetPreparer` to split raw images into 80/20 train/test split.

## Supported Butterfly Species
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

## Project Structure
```
butterfly_classifier/
├── src/main/java/com/butterfly/classifier/
│   ├── ButterflyClassifierApp.java   # Swing GUI Application
│   ├── SpeciesModel.java             # Image preprocessing and model inference
│   ├── DatasetPreparer.java          # 80/20 train/test dataset splitter
│   └── Species.java                  # Butterfly species enumeration
├── build.bat                         # Build script for Windows
├── run.bat                           # Run script for Windows
├── pom.xml                           # Maven project configuration
└── images/                           # Raw image dataset
```

## How to Build & Run

### Prerequisites
- JDK 21 or Java 17+ installed and configured on PATH (`javac`, `java`).

### Quick Run (Windows)
1. Double-click `build.bat` (or run in CMD / PowerShell) to compile the Java project:
   ```cmd
   build.bat
   ```
2. Run `run.bat` to launch the GUI:
   ```cmd
   run.bat
   ```

### Using Maven (Optional)
If Maven is installed:
```cmd
mvn clean compile
mvn exec:java
```

### Organize Dataset
To run the dataset splitting tool manually:
```cmd
java -cp target/classes com.butterfly.classifier.DatasetPreparer
```
