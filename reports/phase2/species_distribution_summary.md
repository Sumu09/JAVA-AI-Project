# Active Dataset Species Distribution Analysis

**Analysis Date**: 2026-11-02 23:25:51  
**Total Active Images**: 4,085 across exactly 125 species  
**Train Set**: 3,113 images | **Test Set**: 972 images

---

## 1. Class Count Statistics

| Metric | Train Count | Test Count | Total Count per Class |
| :--- | :---: | :---: | :---: |
| **Minimum** | 1 | 1 | **2** |
| **Maximum** | 104 | 26 | **130** |
| **Mean (Average)** | 24.9 | 7.78 | **32.68** |
| **Median** | 24 | 7 | **33** |
| **Standard Deviation** | 16.71 | 4.29 | **20.29** |

---

## 2. Species Representation Tiers

- **Critically Underrepresented (< 15 images)**: **16 species**
- **Underrepresented (15–24 images)**: **17 species**
- **Moderately Populated (25–49 images)**: **80 species**
- **Well Represented (&ge; 50 images)**: **12 species**

### Critically Underrepresented Taxa (< 15 images)
These rare species have the fewest total images and require prioritized targeted augmentation:

| Class ID | Scientific Name | Common Name | Family | Train | Test | Total | Status |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| `042` | *Jamides celeno* | Common Cerulean | Lycaenidae | 1 | 1 | **2** | CRITICALLY_UNDERREPRESENTED |
| `048` | *Loxura atymnus continentalis* | Yamfly | Lycaenidae | 1 | 2 | **3** | CRITICALLY_UNDERREPRESENTED |
| `064` | *Prosotas nora ardates* | Common Lineblue | Lycaenidae | 1 | 2 | **3** | CRITICALLY_UNDERREPRESENTED |
| `063` | *Prosotas dubiosa indica* | Tailless Lineblue | Lycaenidae | 2 | 2 | **4** | CRITICALLY_UNDERREPRESENTED |
| `030` | *Elymnias hypermnestra undularis* | Common Palmfly | Nymphalidae | 3 | 2 | **5** | CRITICALLY_UNDERREPRESENTED |
| `071` | *Spindasis lohita himalayanus* | Long-banded Silverline | Lycaenidae | 3 | 2 | **5** | CRITICALLY_UNDERREPRESENTED |
| `027` | *Chilades lajus lajus* | Lime Blue | Lycaenidae | 5 | 3 | **8** | CRITICALLY_UNDERREPRESENTED |
| `012` | *Ampittia dioscorides* | Bush Hopper | Hesperiidae | 8 | 1 | **9** | CRITICALLY_UNDERREPRESENTED |
| `021` | *Catochrysops strabo strabo* | Forget-me-not | Lycaenidae | 6 | 3 | **9** | CRITICALLY_UNDERREPRESENTED |
| `040` | *Heliophorus epicles latilimbata* | Purple Sapphire | Lycaenidae | 6 | 3 | **9** | CRITICALLY_UNDERREPRESENTED |
| `072` | *Surendra quercetorum quercetorum* | Common Acacia Blue | Lycaenidae | 6 | 4 | **10** | CRITICALLY_UNDERREPRESENTED |
| `037` | *Halpe porus porus* | Moore's Ace | Hesperiidae | 9 | 4 | **13** | CRITICALLY_UNDERREPRESENTED |
| `049` | *Megisba malaya sikkima* | Malayan | Lycaenidae | 8 | 5 | **13** | CRITICALLY_UNDERREPRESENTED |
| `052` | *Neopithecops zalmora zalmora* | Common Quaker | Lycaenidae | 8 | 5 | **13** | CRITICALLY_UNDERREPRESENTED |
| `035` | *Halpe aucma* | Gold-spotted Ace | Hesperiidae | 11 | 3 | **14** | CRITICALLY_UNDERREPRESENTED |
| `076` | *Telicota bambusae bambusae* | Dark Palm Dart | Hesperiidae | 10 | 4 | **14** | CRITICALLY_UNDERREPRESENTED |

---

## 3. Split Balance Anomalies

There are **4 species** with irregular train-to-test ratios:

| Class ID | Scientific Name | Common Name | Train | Test | Ratio (Tr/Te) | Anomaly Type |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `048` | *Loxura atymnus continentalis* | Yamfly | 1 | 2 | 0.5 | `INVERTED_RATIO_TEST_HEAVY` |
| `064` | *Prosotas nora ardates* | Common Lineblue | 1 | 2 | 0.5 | `INVERTED_RATIO_TEST_HEAVY` |
| `060` | *Potanthus pseudomaesa* | Indian Dart | 27 | 3 | 9.0 | `TRAIN_HEAVY_SKEW` |
| `055` | *Ochus subvittatus subradiatus* | Tiger Hopper | 31 | 3 | 10.33 | `TRAIN_HEAVY_SKEW` |

---

## 4. Key Takeaways for Machine Learning

1. **Class Imbalance**: Dataset exhibits a long-tailed distribution (min: 2, max: 130). Training must employ focal loss, class-weighted cross-entropy, or stratified sampling.
2. **Rare Species Protection**: Species with $< 15$ images must not undergo aggressive validation splitting that starves training.
3. **Data Quality Ledger**: Detailed CSV generated at [`species_distribution.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/species_distribution.csv).
