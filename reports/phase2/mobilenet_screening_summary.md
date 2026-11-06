# MobileNetV2 Visual Screening Forensic Report

**Analysis Date**: 2026-11-02 23:25:51  
**Total Images Screened**: **155 images** across 77 distinct ImageNet classes  
**Interactive Visual Contact Sheet**: [`mobilenet_review_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/mobilenet_review_contact_sheets.html)  
**Review Decision Ledger Template**: [`mobilenet_review_template.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/mobilenet_review_template.csv)

---

## 1. Summary of Visual Screening Categories

| Category | Count | Proportion | Key Identifying Characteristics | Action Policy |
| :--- | :---: | :---: | :--- | :--- |
| **Specimen Context False Alarms** | **35** | 22.6% | Genuine butterflies photographed with mounting pins (`hair_slide`), scale bars (`rule`), spread wing shapes (`bow_tie`), or on perching flowers (`daisy`). | **PRESERVE IN DATASET**. High biological value. |
| **Probable Non-Butterfly Junk** | **120** | 77.4% | Websites, digital screenshots, electric guitars, jerseys, envelopes, spiders, centipedes, mushrooms, reptiles. | **CANDIDATES FOR PHASE 3 PURGE** following manual confirmation. |

---

## 2. Key Specimen False Alarms to Protect

1. **`081_Euthalia_zubeengargi/0810045.jpg`**: Predicted as `bow_tie` (96.5%). Genuine dorsal wing view of the rare Assam Duke butterfly. Must be protected.
2. **`083_Papilio_paradoxa/0830017.jpg`**: Predicted as `hair_slide` (92.0%). Authentic museum specimen pinned on mounting board.
3. **`114_Arhopala_oenea/1140011.jpg`**: Predicted as `rule` (51.7%). Authentic museum specimen alongside a scientific scale bar.
4. **`002_Heliconius_charitonius/0020143.png`**: Predicted as `daisy` (66.8%). Live butterfly nectaring on a composite flower.

---

## 3. High-Confidence Crawler Junk by Class

- **Websites & Banners (13 files)**: Web crawler downloaded full HTML page screenshots or banner sidebars.
- **Electric Guitars (11 files)**: Downloaded as repeated stock placeholders for 11 different rare Assam species (Cluster `CSD-001`).
- **Spiders & Non-Insect Arthropods (14 files)**: Spiders (`barn_spider`, `wolf_spider`, `black_and_gold_garden_spider`), centipedes (3), scorpions (1), harvestmen (1).
- **Clothing & Equipment (15+ files)**: Jerseys (4), gowns (2), oxygen masks (2), crash helmet (1), lab coat (1), pajamas (1).
