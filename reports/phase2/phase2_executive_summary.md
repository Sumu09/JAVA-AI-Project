# Phase 2: Biological Review & Dataset Quality Assessment — Executive Summary

**Date**: 2026-11-02 23:25:51  
**Active Dataset Status**: **4,085 images** across exactly **125 species**  
**Quarantine Holding Status**: **413 images** safely isolated in `dataset/quarantine/`  
**Safeguard Commitment**: Zero files moved, renamed, deleted, or downloaded during Phase 2.

---

## 1. Key Analytical Pillars & Deliverables

| Analytical Pillar | Key Findings | Deliverables Generated |
| :--- | :--- | :--- |
| **Pillar 1: Species Distribution** | Mean: 32.68 imgs/class; Median: 33; Range: 2–130. 32 species underrepresented (< 25 imgs). | [`species_distribution.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/species_distribution.csv)<br>[`species_distribution_summary.md`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/species_distribution_summary.md) |
| **Pillar 2: Cross-Species Duplicates** | 60 duplicate clusters (146 files) analyzed. 5 mega-clusters (&ge; 3 species), 12 congeneric pairs, 43 intergeneric pairs. | [`cross_species_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/cross_species_contact_sheets.html)<br>[`cross_species_review_template.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/cross_species_review_template.csv)<br>[`cross_species_analysis.md`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/cross_species_analysis.md) |
| **Pillar 3: MobileNet Visual Flags** | 155 images screened. 35 verified specimen context false alarms (pins, rulers, flowers), 120 probable web crawler junk. | [`mobilenet_review_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/mobilenet_review_contact_sheets.html)<br>[`mobilenet_review_template.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/mobilenet_review_template.csv)<br>[`mobilenet_screening_summary.md`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/mobilenet_screening_summary.md) |
| **Pillar 4: Image Quality & Geometry** | Median: 600&times;450 px; 0 corrupt files; 521 low-res photos identified as authentic historical specimen photos. | [`image_quality_assessment.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/image_quality_assessment.csv)<br>[`image_quality_summary.md`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/image_quality_summary.md) |

---

## 2. Species Requiring Urgent Review & Targeted Data Collection

The following taxa have fewer than 15 total images and represent the most vulnerable classes for machine learning:

| Class ID | Scientific Name | Common Name | Family | Active Train | Active Test | Total |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: |
| `042` | *Jamides celeno* | Common Cerulean | Lycaenidae | 1 | 1 | **2** |
| `048` | *Loxura atymnus continentalis* | Yamfly | Lycaenidae | 1 | 2 | **3** |
| `064` | *Prosotas nora ardates* | Common Lineblue | Lycaenidae | 1 | 2 | **3** |
| `063` | *Prosotas dubiosa indica* | Tailless Lineblue | Lycaenidae | 2 | 2 | **4** |
| `030` | *Elymnias hypermnestra undularis* | Common Palmfly | Nymphalidae | 3 | 2 | **5** |
| `071` | *Spindasis lohita himalayanus* | Long-banded Silverline | Lycaenidae | 3 | 2 | **5** |
| `027` | *Chilades lajus lajus* | Lime Blue | Lycaenidae | 5 | 3 | **8** |
| `012` | *Ampittia dioscorides* | Bush Hopper | Hesperiidae | 8 | 1 | **9** |
| `021` | *Catochrysops strabo strabo* | Forget-me-not | Lycaenidae | 6 | 3 | **9** |
| `040` | *Heliophorus epicles latilimbata* | Purple Sapphire | Lycaenidae | 6 | 3 | **9** |

---

## 3. Recommended Roadmap for Phase 3 (Human-in-the-Loop Review & Cleanup)

1. **Step 1: Complete Reviewer Ledgers**:
   - Open [`cross_species_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/cross_species_contact_sheets.html) to confirm purging the 5 mega-clusters (electric guitars, envelopes) and assign correct labels to congeneric pairs.
   - Open [`mobilenet_review_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/mobilenet_review_contact_sheets.html) to confirm preservation of the 35 specimen context photos and approve purging the 120 non-butterfly objects.
2. **Step 2: Safe Human-Guided Quarantine**:
   - Once review CSVs are populated with reviewer determinations, an automated script will move only the confirmed junk into `dataset/quarantine/phase2/` with full reversibility.
3. **Step 3: Targeted Ethical Augmentation**:
   - Download authentic specimen photos for the underrepresented species using verified entomological portals (e.g. Butterflies of India, iNaturalist research-grade) rather than generic search engines.
