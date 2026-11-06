# ButterflyAI — Phase 3C: Cross-Species Duplicate Review Report
**Generated**: 2026-11-03 07:51:57  
**Dataset Scope**: 55 Pairwise Cross-Species Clusters &bull; 120 Total Image Files &bull; 97 Active &bull; 23 Quarantined  
**Target Ledger**: [`cross_species_review.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/cross_species_review.csv)  
**Visual Contact Sheet**: [`cross_species_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/cross_species_contact_sheets.html)

---

## 1. Executive Summary

Phase 3C investigates all 55 pairwise cross-species duplicate clusters remaining after the completion of Phase 3A/3B (which safely audited and quarantined the 5 high-order mega-clusters `CSD-001`, `CSD-002`, `CSD-008`, `CSD-009`, and `CSD-010`).

### Key Quantitative Findings:
- **Total Clusters**: **55** duplicate clusters (`CSD-003` to `CSD-007`, `CSD-011` to `CSD-060`).
- **Total Duplicate Files**: **120** files tracked.
- **Active Files in Dataset**: **97** images (84 active files in train conflicts, 2 files in pure test conflicts, 11 active files in resolved train conflicts).
- **Quarantined Files**: **23** files safely isolated during Phase 1 (21 test-leakage files + 2 internal train duplicates).
- **Active Multi-Species Conflicts**: **42 clusters** still have active duplicate copies in multiple species folders.
- **Quarantine-Resolved Provenance Clusters**: **13 clusters** have active image(s) in only 1 species folder (their cross-species duplicate counterpart in test was quarantined in Phase 1 for evaluation leakage).
- **Historic Train-Test Split Leakage**: **18 clusters** originally crossed train and test split boundaries. In all 18, the test split duplicate was quarantined in Phase 1, eliminating active leakage.

---

## 2. Taxonomic Breakdown

The 55 duplicate clusters fall into three distinct biological tiers:

| Taxonomic Tier | Cluster Count | File Count | Description | Primary Risk |
| :--- | :---: | :---: | :--- | :--- |
| **Congeneric (Same Genus)** | **39** | 88 | Duplicate shared between sister species in the same genus (e.g. *Halpe aucma* vs *Halpe zema*, *Papilio paradoxa* vs *Papilio slateri*, *Arhopala silhetensis* vs *Arhopala oenea*). | Sub-species / morphological confusion during scraping. Usually genuine butterfly. |
| **Intergeneric (Same Family)** | **10** | 20 | Duplicate shared across different genera in the same family (e.g. Hesperiidae skippers *Halpe* vs *Thoressa*, *Pyroneura* vs *Salanoemia*). | Web template re-use or scraper confusion among similar skipper/nymphalid morphs. |
| **Interfamily (Different Family)** | **6** | 12 | Duplicate shared across completely different butterfly families (e.g. Swallowtail *Papilio elephenor* vs Skipper *Salanoemia sala*, or Lycaenid *Udara selma* vs Skipper *Darpa pteria*). | High probability of non-biological noise, web page graphic, or scraper bug. |
| **Total** | **55** | **120** | | |

---

## 3. High-Priority Review Categories

### Priority A: Historic Split Leakage Clusters (18 Clusters)
These 18 clusters originally spanned both `train` and `test` splits. Although their test split files were quarantined during Phase 1, biological review is necessary to verify whether the remaining training image is assigned to the correct species.

| Cluster ID | Active Status | Conflicting Species 1 | Conflicting Species 2 | AI Prediction | Suggestion |
| :---: | :---: | :--- | :--- | :--- | :--- |
| `CSD-003` | ACTIVE (2) | *Halpe aucma* | *Halpe zema zema* | lycaenid (17.9%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-004` | ACTIVE (2) | *Halpe kusala* | *Halpe zema zema* | cricket (25.5%) | `UNCERTAIN` |
| `CSD-005` | ACTIVE (2) | *Halpe kusala* | *Halpe porus porus* | lycaenid (62.4%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-006` | ACTIVE (2) | *Halpe zema zema* | *Thoressa cerata* | ringlet (16.4%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-007` | ACTIVE (2) | *Ochus subvittatus subradiatus* | *Pithauria stramineipennis* | ringlet (68.5%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-014` | RESOLVED (1) | *Lethe chandica flanona* | *Lethe mekara mekara* | ringlet (57.7%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-016` | RESOLVED (1) | *Euthalia zubeengargi* | *Euthalia telchinia* | leafhopper (20.3%) | `UNCERTAIN` |
| `CSD-021` | RESOLVED (1) | *Papilio elephenor* | *Papilio bootes* | web_site (5.1%) | `LIKELY_NON_BUTTERFLY` |
| `CSD-024` | RESOLVED (1) | *Papilio paradoxa* | *Papilio bootes* | admiral (23.9%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-033` | RESOLVED (1) | *Byasa crassipes* | *Byasa polla* | lycaenid (20.5%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-038` | RESOLVED (1) | *Euthalia zubeengargi* | *Euthalia telchinia* | ringlet (10.3%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-040` | RESOLVED (1) | *Pantoporia assamica* | *Pantoporia bieti* | lycaenid (13.7%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-041` | RESOLVED (1) | *Pantoporia assamica* | *Pantoporia bieti* | custard_apple (13.5%) | `UNCERTAIN` |
| `CSD-043` | RESOLVED (1) | *Athyma ranga* | *Athyma punctata* | admiral (90.8%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-044` | RESOLVED (1) | *Athyma pravara* | *Athyma punctata* | admiral (34.8%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-045` | RESOLVED (1) | *Athyma pravara* | *Athyma punctata* | admiral (72.1%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-055` | RESOLVED (1) | *Udara selma* | *Darpa pteria* | web_site (20.0%) | `LIKELY_NON_BUTTERFLY` |
| `CSD-058` | RESOLVED (1) | *Plastingia naga* | *Salanoemia sala* | lycaenid (89.4%) | `GENUINE_BUTTERFLY_MISLABELING` |

### Priority B: Suspected Non-Butterfly / Artifact Clusters (7 Clusters)
Visual screening identified 7 clusters whose predictions and aspect ratios indicate non-biological images (web graphics, templates, drawings, or food items).

| Cluster ID | Conflict Status | Species 1 | Species 2 | AI Prediction | Recommended Action |
| :---: | :---: | :--- | :--- | :--- | :--- |
| `CSD-015` | ACTIVE | *Lethe satyavati* | *Lethe vindhya vindhya* | hatchet (68.8%) | Inspect for low-res tool icon or diagram |
| `CSD-020` | ACTIVE | *Papilio elephenor* | *Salanoemia sala* | web_site (25.2%) | Inspect for web template / website banner |
| `CSD-021` | RESOLVED | *Papilio elephenor* | *Papilio bootes* | web_site (5.1%) | Inspect for web template / website banner |
| `CSD-028` | ACTIVE | *Byasa crassipes* | *Byasa polla* | pretzel (45.2%) | Inspect for non-insect object |
| `CSD-055` | RESOLVED | *Udara selma* | *Darpa pteria* | web_site (20.0%) | Inspect for web banner across families |
| `CSD-056` | ACTIVE | *Darpa pteria* | *Hidari bhawani* | web_site (74.2%) | Inspect for web banner / template |
| `CSD-057` | ACTIVE | *Salanoemia sala* | *Scobura woolletti* | envelope (49.5%) | Inspect for document graphic / envelope |

---

## 4. Comprehensive Catalog of All 55 Clusters

### Cluster `CSD-003` — *Halpe aucma* vs *Halpe zema zema*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Hesperiidae)
- **SHA-256**: `f33986bbf9f0d4b7a794c40b304f822e858f44b32baf8f2371b2c0e00eb75b78`
- **Active Files**: `2` active | `2` quarantined (Total: `4`)
- **Sample Image**: [`dataset/train/035_Halpe_aucma/0350006.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/035_Halpe_aucma/0350006.jpg) (1300&times;1065 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (17.9%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 17.9%). Duplicate across sister species: 'Halpe aucma' vs 'Halpe zema zema'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#035` | *Halpe aucma* | Gold-spotted Ace | Hesperiidae | `train` | `dataset/train/035_Halpe_aucma/0350006.jpg` | `ACTIVE` |
| `#038` | *Halpe zema zema* | Zema Ace | Hesperiidae | `train` | `dataset/train/038_Halpe_zema_zema/0380019.jpg` | `ACTIVE` |
| `#035` | *Halpe aucma* | Gold-spotted Ace | Hesperiidae | `test` | `dataset/test/035_Halpe_aucma/0350010.jpg` | `QUARANTINED (Phase 1)` |
| `#038` | *Halpe zema zema* | Zema Ace | Hesperiidae | `test` | `dataset/test/038_Halpe_zema_zema/0380029.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-004` — *Halpe kusala* vs *Halpe zema zema*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Hesperiidae)
- **SHA-256**: `222470c6a3a37058e57ccae5dce5bb10bf71a44da3f2f82237832ab0163d8902`
- **Active Files**: `2` active | `2` quarantined (Total: `4`)
- **Sample Image**: [`dataset/train/036_Halpe_kusala/0360001.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/036_Halpe_kusala/0360001.jpg) (1000&times;667 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `cricket (25.5%)`
- **Suggested Determination**: **`UNCERTAIN`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Ambiguous prediction (cricket (25.5%)). Specimen context artifact or difficult angle. Species involved: 'Halpe kusala' vs 'Halpe zema zema'.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#036` | *Halpe kusala* | Plain Ace | Hesperiidae | `train` | `dataset/train/036_Halpe_kusala/0360001.jpg` | `ACTIVE` |
| `#036` | *Halpe kusala* | Plain Ace | Hesperiidae | `train` | `dataset/train/036_Halpe_kusala/0360005.jpg` | `QUARANTINED (Phase 1)` |
| `#038` | *Halpe zema zema* | Zema Ace | Hesperiidae | `train` | `dataset/train/038_Halpe_zema_zema/0380011.jpg` | `ACTIVE` |
| `#038` | *Halpe zema zema* | Zema Ace | Hesperiidae | `test` | `dataset/test/038_Halpe_zema_zema/0380012.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-005` — *Halpe kusala* vs *Halpe porus porus*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Hesperiidae)
- **SHA-256**: `e0ef5ce668d9ea10794cee635ea1c5ee402652a2ed9f2cb7e0bbf024bcaac25d`
- **Active Files**: `2` active | `2` quarantined (Total: `4`)
- **Sample Image**: [`dataset/train/036_Halpe_kusala/0360007.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/036_Halpe_kusala/0360007.jpg) (1242&times;1012 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (62.4%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 62.4%). Duplicate across sister species: 'Halpe kusala' vs 'Halpe porus porus'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#036` | *Halpe kusala* | Plain Ace | Hesperiidae | `train` | `dataset/train/036_Halpe_kusala/0360007.jpg` | `ACTIVE` |
| `#037` | *Halpe porus porus* | Moore's Ace | Hesperiidae | `train` | `dataset/train/037_Halpe_porus_porus/0370011.jpg` | `ACTIVE` |
| `#036` | *Halpe kusala* | Plain Ace | Hesperiidae | `test` | `dataset/test/036_Halpe_kusala/0360020.jpg` | `QUARANTINED (Phase 1)` |
| `#037` | *Halpe porus porus* | Moore's Ace | Hesperiidae | `test` | `dataset/test/037_Halpe_porus_porus/0370010.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-006` — *Halpe zema zema* vs *Thoressa cerata*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `ee1ffadefc99a7f2f52492c016d3d89c3acbfe94c11840fadca28f7b0cbb1e8b`
- **Active Files**: `2` active | `2` quarantined (Total: `4`)
- **Sample Image**: [`dataset/train/038_Halpe_zema_zema/0380040.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/038_Halpe_zema_zema/0380040.jpg) (900&times;600 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `ringlet (16.4%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 16.4%). Duplicate across sister species: 'Halpe zema zema' vs 'Thoressa cerata'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#038` | *Halpe zema zema* | Zema Ace | Hesperiidae | `train` | `dataset/train/038_Halpe_zema_zema/0380040.jpg` | `ACTIVE` |
| `#078` | *Thoressa cerata* | Northern Spangle | Hesperiidae | `train` | `dataset/train/078_Thoressa_cerata/0780021.jpg` | `ACTIVE` |
| `#078` | *Thoressa cerata* | Northern Spangle | Hesperiidae | `train` | `dataset/train/078_Thoressa_cerata/0780027.jpg` | `QUARANTINED (Phase 1)` |
| `#038` | *Halpe zema zema* | Zema Ace | Hesperiidae | `test` | `dataset/test/038_Halpe_zema_zema/0380048.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-007` — *Ochus subvittatus subradiatus* vs *Pithauria stramineipennis*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `9a3ff9e578b95efce6727353bfbb308efe3154d59b8d296b5025afe56ee04370`
- **Active Files**: `2` active | `2` quarantined (Total: `4`)
- **Sample Image**: [`dataset/train/055_Ochus_subvittatus_subradiatus/0550015.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/055_Ochus_subvittatus_subradiatus/0550015.jpg) (900&times;600 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `ringlet (68.5%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 68.5%). Duplicate across sister species: 'Ochus subvittatus subradiatus' vs 'Pithauria stramineipennis'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#055` | *Ochus subvittatus subradiatus* | Tiger Hopper | Hesperiidae | `train` | `dataset/train/055_Ochus_subvittatus_subradiatus/0550015.jpg` | `ACTIVE` |
| `#059` | *Pithauria stramineipennis* | Light Straw Ace | Hesperiidae | `train` | `dataset/train/059_Pithauria_stramineipennis/0590010.jpg` | `ACTIVE` |
| `#055` | *Ochus subvittatus subradiatus* | Tiger Hopper | Hesperiidae | `test` | `dataset/test/055_Ochus_subvittatus_subradiatus/0550002.jpg` | `QUARANTINED (Phase 1)` |
| `#059` | *Pithauria stramineipennis* | Light Straw Ace | Hesperiidae | `test` | `dataset/test/059_Pithauria_stramineipennis/0590049.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-014` — *Lethe chandica flanona* vs *Lethe mekara mekara*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `d52098f12391dfc117917a997059084148b109a46f7a8c589b3987c945919fa3`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/045_Lethe_mekara_mekara/0450014.jpeg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/045_Lethe_mekara_mekara/0450014.jpeg) (1620&times;1080 px, `WEBP`, `ACTIVE`)
- **AI Screening**: `ringlet (57.7%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 57.7%). Duplicate across sister species: 'Lethe chandica flanona' vs 'Lethe mekara mekara'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#045` | *Lethe mekara mekara* | Common Treebrown | Nymphalidae | `train` | `dataset/train/045_Lethe_mekara_mekara/0450014.jpeg` | `ACTIVE` |
| `#044` | *Lethe chandica flanona* | Angled Red Forester | Nymphalidae | `test` | `dataset/test/044_Lethe_chandica_flanona/0440006.jpeg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-016` — *Euthalia zubeengargi* vs *Euthalia telchinia*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `c1209e10487bdd2160a6572dd8ae8472e3dbad0f2afc909f5ec7e69d05f2300c`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/081_Euthalia_zubeengargi/0810004.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/081_Euthalia_zubeengargi/0810004.jpg) (480&times;360 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `leafhopper (20.3%)`
- **Suggested Determination**: **`UNCERTAIN`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Ambiguous prediction (leafhopper (20.3%)). Specimen context artifact or difficult angle. Species involved: 'Euthalia zubeengargi' vs 'Euthalia telchinia'.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#081` | *Euthalia zubeengargi* | Zubeen's Baron | Nymphalidae | `train` | `dataset/train/081_Euthalia_zubeengargi/0810004.jpg` | `ACTIVE` |
| `#100` | *Euthalia telchinia* | Blue Baron | Nymphalidae | `test` | `dataset/test/100_Euthalia_telchinia/1000032.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-021` — *Papilio elephenor* vs *Papilio bootes*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `f981f23e04bc5901580efb8fe55ff8f74316d4d88d0dc688ca3d0e49ca0ed803`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/082_Papilio_elephenor/0820009.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/082_Papilio_elephenor/0820009.jpg) (700&times;573 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `web_site (5.1%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (web_site). Cross-congeneric collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#082` | *Papilio elephenor* | Yellow-crested Spangle | Papilionidae | `train` | `dataset/train/082_Papilio_elephenor/0820009.jpg` | `ACTIVE` |
| `#084` | *Papilio bootes* | Tailed Redbreast | Papilionidae | `test` | `dataset/test/084_Papilio_bootes/0840033.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-024` — *Papilio paradoxa* vs *Papilio bootes*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `0b1e98ee2a6ac301dbef1af3557d6cced14577e4b5f20ef2c86c77af8cae1582`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/083_Papilio_paradoxa/0830010.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/083_Papilio_paradoxa/0830010.jpg) (800&times;511 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (23.9%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 23.9%). Duplicate across sister species: 'Papilio paradoxa' vs 'Papilio bootes'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#083` | *Papilio paradoxa* | Great Blue Mime | Papilionidae | `train` | `dataset/train/083_Papilio_paradoxa/0830010.jpg` | `ACTIVE` |
| `#084` | *Papilio bootes* | Tailed Redbreast | Papilionidae | `test` | `dataset/test/084_Papilio_bootes/0840032.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-033` — *Byasa crassipes* vs *Byasa polla*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `07c29ba4066b7280b1dd9af6cd0b4ffa980446fee327d426fe3b39cf4bc5dd08`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/090_Byasa_crassipes/0900025.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/090_Byasa_crassipes/0900025.jpg) (1000&times;630 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (20.5%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 20.5%). Duplicate across sister species: 'Byasa crassipes' vs 'Byasa polla'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#090` | *Byasa crassipes* | Black Windmill | Papilionidae | `train` | `dataset/train/090_Byasa_crassipes/0900025.jpg` | `ACTIVE` |
| `#092` | *Byasa polla* | De Nicéville's Windmill | Papilionidae | `test` | `dataset/test/092_Byasa_polla/0920029.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-038` — *Euthalia zubeengargi* vs *Euthalia telchinia*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `3a6088c022411c4260f4a5c79c1e243a000620aee255a57813474652caceebf8`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/100_Euthalia_telchinia/1000006.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/100_Euthalia_telchinia/1000006.jpg) (580&times;389 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `ringlet (10.3%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 10.3%). Duplicate across sister species: 'Euthalia zubeengargi' vs 'Euthalia telchinia'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#100` | *Euthalia telchinia* | Blue Baron | Nymphalidae | `train` | `dataset/train/100_Euthalia_telchinia/1000006.jpg` | `ACTIVE` |
| `#081` | *Euthalia zubeengargi* | Zubeen's Baron | Nymphalidae | `test` | `dataset/test/081_Euthalia_zubeengargi/0810142.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-040` — *Pantoporia assamica* vs *Pantoporia bieti*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `24f7a01d71d41030d1040cac2ea47b566cdf258147eab329348e79dce497efd5`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/102_Pantoporia_assamica/1020016.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/102_Pantoporia_assamica/1020016.jpg) (400&times;600 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (13.7%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 13.7%). Duplicate across sister species: 'Pantoporia assamica' vs 'Pantoporia bieti'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#102` | *Pantoporia assamica* | Conjoined Lascar | Nymphalidae | `train` | `dataset/train/102_Pantoporia_assamica/1020016.jpg` | `ACTIVE` |
| `#103` | *Pantoporia bieti* | Tytler's Lascar | Nymphalidae | `test` | `dataset/test/103_Pantoporia_bieti/1030030.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-041` — *Pantoporia assamica* vs *Pantoporia bieti*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `f2cae82a05ffc35a6faac37a9e55b60f0c6585db7d640f6a32592ba8560d57e7`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/102_Pantoporia_assamica/1020019.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/102_Pantoporia_assamica/1020019.jpg) (333&times;500 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `custard_apple (13.5%)`
- **Suggested Determination**: **`UNCERTAIN`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Ambiguous prediction (custard_apple (13.5%)). Specimen context artifact or difficult angle. Species involved: 'Pantoporia assamica' vs 'Pantoporia bieti'.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#102` | *Pantoporia assamica* | Conjoined Lascar | Nymphalidae | `train` | `dataset/train/102_Pantoporia_assamica/1020019.jpg` | `ACTIVE` |
| `#103` | *Pantoporia bieti* | Tytler's Lascar | Nymphalidae | `test` | `dataset/test/103_Pantoporia_bieti/1030033.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-043` — *Athyma ranga* vs *Athyma punctata*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `dbd28ae1520892922ae4510d1f77b5018689d2c64001409e468bc60b398021d4`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/105_Athyma_ranga/1050024.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/105_Athyma_ranga/1050024.jpg) (600&times;400 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (90.8%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 90.8%). Duplicate across sister species: 'Athyma ranga' vs 'Athyma punctata'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#105` | *Athyma ranga* | Blackvein Sergeant | Nymphalidae | `train` | `dataset/train/105_Athyma_ranga/1050024.jpg` | `ACTIVE` |
| `#107` | *Athyma punctata* | White-bordered Sergeant | Nymphalidae | `test` | `dataset/test/107_Athyma_punctata/1070033.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-044` — *Athyma pravara* vs *Athyma punctata*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `d304e84216897f187a346f0abca37e2f25f90a8d42e96b9d763cf81cfce9b94c`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/107_Athyma_punctata/1070011.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/107_Athyma_punctata/1070011.jpg) (1300&times;1390 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (34.8%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 34.8%). Duplicate across sister species: 'Athyma pravara' vs 'Athyma punctata'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#107` | *Athyma punctata* | White-bordered Sergeant | Nymphalidae | `train` | `dataset/train/107_Athyma_punctata/1070011.jpg` | `ACTIVE` |
| `#106` | *Athyma pravara* | Unbroken Sergeant | Nymphalidae | `test` | `dataset/test/106_Athyma_pravara/1060032.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-045` — *Athyma pravara* vs *Athyma punctata*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `bb889b8a85abeada3679df9e75d8fd73b962106e579236054968fee38fcee1a7`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/107_Athyma_punctata/1070024.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/107_Athyma_punctata/1070024.jpg) (2000&times;1333 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (72.1%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 72.1%). Duplicate across sister species: 'Athyma pravara' vs 'Athyma punctata'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#107` | *Athyma punctata* | White-bordered Sergeant | Nymphalidae | `train` | `dataset/train/107_Athyma_punctata/1070024.jpg` | `ACTIVE` |
| `#106` | *Athyma pravara* | Unbroken Sergeant | Nymphalidae | `test` | `dataset/test/106_Athyma_pravara/1060030.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-055` — *Udara selma* vs *Darpa pteria*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `INTERFAMILY` (Lycaenidae, Hesperiidae)
- **SHA-256**: `6b180fb7c583c93d3b46bc68a54f443a9bc9e44334a68f7de35933cebac3da1f`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/120_Darpa_pteria/1200005.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/120_Darpa_pteria/1200005.jpg) (593&times;445 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `web_site (20.0%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (web_site). Cross-interfamily collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#120` | *Darpa pteria* | Snowy Angle | Hesperiidae | `train` | `dataset/train/120_Darpa_pteria/1200005.jpg` | `ACTIVE` |
| `#116` | *Udara selma* | Bi-coloured Hedge Blue | Lycaenidae | `test` | `dataset/test/116_Udara_selma/1160031.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-058` — *Plastingia naga* vs *Salanoemia sala*
- **Status**: `[RESOLVED BY PHASE 1 QUARANTINE]` `[HISTORIC TRAIN-TEST LEAKAGE]`
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `e5362b2dbab38a7382f3e3e3a4c1a204b340a515abf162cba876a819bf553457`
- **Active Files**: `1` active | `1` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/123_Salanoemia_sala/1230020.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/123_Salanoemia_sala/1230020.jpg) (800&times;498 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (89.4%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 89.4%). Duplicate across sister species: 'Plastingia naga' vs 'Salanoemia sala'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `train` | `dataset/train/123_Salanoemia_sala/1230020.jpg` | `ACTIVE` |
| `#122` | *Plastingia naga* | Chequered Lancer | Hesperiidae | `test` | `dataset/test/122_Plastingia_naga/1220034.jpg` | `QUARANTINED (Phase 1)` |

### Cluster `CSD-011` — *Ancema blanka minturna* vs *Notocrypta paralysos asawa*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERFAMILY` (Lycaenidae, Hesperiidae)
- **SHA-256**: `ea80daac4eb0b06069bad3c50f66104eac01263477d31dbf51f72f6b1b23e477`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/013_Ancema_blanka_minturna/0130004.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/013_Ancema_blanka_minturna/0130004.jpg) (660&times;440 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (41.4%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 41.4%). Duplicate across sister species: 'Ancema blanka minturna' vs 'Notocrypta paralysos asawa'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#013` | *Ancema blanka minturna* | Minturn Silverstreak | Lycaenidae | `train` | `dataset/train/013_Ancema_blanka_minturna/0130004.jpg` | `ACTIVE` |
| `#054` | *Notocrypta paralysos asawa* | Grass Demon | Hesperiidae | `train` | `dataset/train/054_Notocrypta_paralysos_asawa/0540017.jpg` | `ACTIVE` |

### Cluster `CSD-012` — *Halpe aucma* vs *Halpe kusala*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Hesperiidae)
- **SHA-256**: `999fe7f434dd8ade5bf867586e78ed8fbb2af2aa13eeddc44ab8d9c4d723b8ff`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/035_Halpe_aucma/0350005.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/035_Halpe_aucma/0350005.jpg) (800&times;593 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `ringlet (82.0%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 82.0%). Duplicate across sister species: 'Halpe aucma' vs 'Halpe kusala'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#035` | *Halpe aucma* | Gold-spotted Ace | Hesperiidae | `train` | `dataset/train/035_Halpe_aucma/0350005.jpg` | `ACTIVE` |
| `#036` | *Halpe kusala* | Plain Ace | Hesperiidae | `train` | `dataset/train/036_Halpe_kusala/0360008.jpg` | `ACTIVE` |

### Cluster `CSD-013` — *Halpe aucma* vs *Halpe kusala*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Hesperiidae)
- **SHA-256**: `e2bd76e88d29059eb2a3fcdb5cafa8520c7fe056bb6af601aa307b6030c3de4d`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/035_Halpe_aucma/0350014.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/035_Halpe_aucma/0350014.jpg) (700&times;587 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `leafhopper (26.2%)`
- **Suggested Determination**: **`UNCERTAIN`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Ambiguous prediction (leafhopper (26.2%)). Specimen context artifact or difficult angle. Species involved: 'Halpe aucma' vs 'Halpe kusala'.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#035` | *Halpe aucma* | Gold-spotted Ace | Hesperiidae | `train` | `dataset/train/035_Halpe_aucma/0350014.jpg` | `ACTIVE` |
| `#036` | *Halpe kusala* | Plain Ace | Hesperiidae | `train` | `dataset/train/036_Halpe_kusala/0360011.jpg` | `ACTIVE` |

### Cluster `CSD-015` — *Lethe satyavati* vs *Lethe vindhya vindhya*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `d2b66f40e3412394432d5dec02b52508f4702fc9e5e2226ef63d4236c46db735`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/046_Lethe_satyavati/0460019.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/046_Lethe_satyavati/0460019.jpg) (120&times;96 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `hatchet (68.8%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (hatchet). Cross-congeneric collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#046` | *Lethe satyavati* | Pallid Forester | Nymphalidae | `train` | `dataset/train/046_Lethe_satyavati/0460019.jpg` | `ACTIVE` |
| `#047` | *Lethe vindhya vindhya* | Black Forester | Nymphalidae | `train` | `dataset/train/047_Lethe_vindhya_vindhya/0470008.jpg` | `ACTIVE` |

### Cluster `CSD-017` — *Euthalia zubeengargi* vs *Euthalia telchinia*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `0113fb9c0b5df2863bf30b8fc9ba6c7e6d6a236de11007f14d86a8f41df0ef26`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/081_Euthalia_zubeengargi/0810023.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/081_Euthalia_zubeengargi/0810023.jpg) (664&times;465 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `ringlet (60.1%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 60.1%). Duplicate across sister species: 'Euthalia zubeengargi' vs 'Euthalia telchinia'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#081` | *Euthalia zubeengargi* | Zubeen's Baron | Nymphalidae | `train` | `dataset/train/081_Euthalia_zubeengargi/0810023.jpg` | `ACTIVE` |
| `#100` | *Euthalia telchinia* | Blue Baron | Nymphalidae | `train` | `dataset/train/100_Euthalia_telchinia/1000008.jpg` | `ACTIVE` |

### Cluster `CSD-018` — *Euthalia zubeengargi* vs *Euthalia telchinia*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `9364335d3d893ebdf7eb29f3ce514ea470e06adfdd79dd80d60950fdc9b43be8`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/081_Euthalia_zubeengargi/0810093.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/081_Euthalia_zubeengargi/0810093.jpg) (1080&times;1443 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `pinwheel (38.1%)`
- **Suggested Determination**: **`UNCERTAIN`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Ambiguous prediction (pinwheel (38.1%)). Specimen context artifact or difficult angle. Species involved: 'Euthalia zubeengargi' vs 'Euthalia telchinia'.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#081` | *Euthalia zubeengargi* | Zubeen's Baron | Nymphalidae | `train` | `dataset/train/081_Euthalia_zubeengargi/0810093.jpg` | `ACTIVE` |
| `#100` | *Euthalia telchinia* | Blue Baron | Nymphalidae | `train` | `dataset/train/100_Euthalia_telchinia/1000001.jpg` | `ACTIVE` |

### Cluster `CSD-019` — *Euthalia zubeengargi* vs *Euthalia telchinia*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `a414c3eee203dfc26e2ad431ea9e68b161ae367565a3a84c4b15ce5f9400c165`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/081_Euthalia_zubeengargi/0810102.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/081_Euthalia_zubeengargi/0810102.jpg) (1859&times;1080 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `sulphur_butterfly (30.1%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (sulphur_butterfly, 30.1%). Duplicate across sister species: 'Euthalia zubeengargi' vs 'Euthalia telchinia'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#081` | *Euthalia zubeengargi* | Zubeen's Baron | Nymphalidae | `train` | `dataset/train/081_Euthalia_zubeengargi/0810102.jpg` | `ACTIVE` |
| `#100` | *Euthalia telchinia* | Blue Baron | Nymphalidae | `train` | `dataset/train/100_Euthalia_telchinia/1000028.jpg` | `ACTIVE` |

### Cluster `CSD-020` — *Papilio elephenor* vs *Salanoemia sala*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERFAMILY` (Papilionidae, Hesperiidae)
- **SHA-256**: `7c5a9a4b93ecdc9782151a210f43ca74fd0a09800e65f4af06b99fe47fdfb307`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/082_Papilio_elephenor/0820006.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/082_Papilio_elephenor/0820006.jpg) (500&times;275 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `web_site (25.2%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (web_site). Cross-interfamily collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#082` | *Papilio elephenor* | Yellow-crested Spangle | Papilionidae | `train` | `dataset/train/082_Papilio_elephenor/0820006.jpg` | `ACTIVE` |
| `#123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `train` | `dataset/train/123_Salanoemia_sala/1230011.jpg` | `ACTIVE` |

### Cluster `CSD-022` — *Papilio elephenor* vs *Papilio paradoxa*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `a14a3ecdcaf5564e77eff5784e2ffbfd1d9efdb1b823800073d33499da130f8f`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/082_Papilio_elephenor/0820019.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/082_Papilio_elephenor/0820019.jpg) (250&times;167 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `hair_slide (92.0%)`
- **Suggested Determination**: **`UNCERTAIN`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Ambiguous prediction (hair_slide (92.0%)). Specimen context artifact or difficult angle. Species involved: 'Papilio elephenor' vs 'Papilio paradoxa'.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#082` | *Papilio elephenor* | Yellow-crested Spangle | Papilionidae | `train` | `dataset/train/082_Papilio_elephenor/0820019.jpg` | `ACTIVE` |
| `#083` | *Papilio paradoxa* | Great Blue Mime | Papilionidae | `train` | `dataset/train/083_Papilio_paradoxa/0830017.jpg` | `ACTIVE` |

### Cluster `CSD-023` — *Papilio paradoxa* vs *Papilio slateri*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `189bdb6e4b7ab5b0ab8f78453edfea23b14d1fae05687434cdfe1dabaf0b62de`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/083_Papilio_paradoxa/0830007.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/083_Papilio_paradoxa/0830007.jpg) (640&times;493 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (78.0%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 78.0%). Duplicate across sister species: 'Papilio paradoxa' vs 'Papilio slateri'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#083` | *Papilio paradoxa* | Great Blue Mime | Papilionidae | `train` | `dataset/train/083_Papilio_paradoxa/0830007.jpg` | `ACTIVE` |
| `#085` | *Papilio slateri* | Blue-striped Mime | Papilionidae | `train` | `dataset/train/085_Papilio_slateri/0850023.jpg` | `ACTIVE` |

### Cluster `CSD-025` — *Papilio paradoxa* vs *Papilio slateri*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `6a463d82b347079a361f0ed8db4c01905ae11069ffd5ab52e78bfe8ed59cf924`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/083_Papilio_paradoxa/0830023.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/083_Papilio_paradoxa/0830023.jpg) (640&times;461 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (53.9%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 53.9%). Duplicate across sister species: 'Papilio paradoxa' vs 'Papilio slateri'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#083` | *Papilio paradoxa* | Great Blue Mime | Papilionidae | `train` | `dataset/train/083_Papilio_paradoxa/0830023.jpg` | `ACTIVE` |
| `#085` | *Papilio slateri* | Blue-striped Mime | Papilionidae | `train` | `dataset/train/085_Papilio_slateri/0850015.jpg` | `ACTIVE` |

### Cluster `CSD-026` — *Meandrusa payeni* vs *Meandrusa lachinus*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `f09f90c6b34ffa5ef42bcbc829bbc8dc1537f5986ac5267d233f53bca6254bc5`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/088_Meandrusa_payeni/0880003.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/088_Meandrusa_payeni/0880003.jpg) (170&times;165 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `hair_slide (20.2%)`
- **Suggested Determination**: **`UNCERTAIN`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Ambiguous prediction (hair_slide (20.2%)). Specimen context artifact or difficult angle. Species involved: 'Meandrusa payeni' vs 'Meandrusa lachinus'.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#088` | *Meandrusa payeni* | Yellow Gorgon | Papilionidae | `train` | `dataset/train/088_Meandrusa_payeni/0880003.jpg` | `ACTIVE` |
| `#089` | *Meandrusa lachinus* | Brown Gorgon | Papilionidae | `train` | `dataset/train/089_Meandrusa_lachinus/0890018.jpg` | `ACTIVE` |

### Cluster `CSD-027` — *Meandrusa payeni* vs *Meandrusa lachinus*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `eb414e6ab9368760ccfb452fb03dc9d74f5ff72559de7ab6461b0d299c2a79fa`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/088_Meandrusa_payeni/0880012.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/088_Meandrusa_payeni/0880012.jpg) (250&times;258 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `ringlet (28.0%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 28.0%). Duplicate across sister species: 'Meandrusa payeni' vs 'Meandrusa lachinus'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#088` | *Meandrusa payeni* | Yellow Gorgon | Papilionidae | `train` | `dataset/train/088_Meandrusa_payeni/0880012.jpg` | `ACTIVE` |
| `#089` | *Meandrusa lachinus* | Brown Gorgon | Papilionidae | `train` | `dataset/train/089_Meandrusa_lachinus/0890002.jpg` | `ACTIVE` |

### Cluster `CSD-028` — *Byasa crassipes* vs *Byasa polla*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `3677435d5a344e725757361cc51eadc4303f0c7cee6ab41224d7e1b124e70f55`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/090_Byasa_crassipes/0900003.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/090_Byasa_crassipes/0900003.jpg) (887&times;695 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `pretzel (45.2%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (pretzel). Cross-congeneric collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#090` | *Byasa crassipes* | Black Windmill | Papilionidae | `train` | `dataset/train/090_Byasa_crassipes/0900003.jpg` | `ACTIVE` |
| `#092` | *Byasa polla* | De Nicéville's Windmill | Papilionidae | `train` | `dataset/train/092_Byasa_polla/0920024.jpg` | `ACTIVE` |

### Cluster `CSD-029` — *Byasa crassipes* vs *Byasa polla*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `0e30afd4cc6a7f93960ac297ed9d55437d1b9b430955c6f1e248a795b586ac96`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/090_Byasa_crassipes/0900004.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/090_Byasa_crassipes/0900004.jpg) (1000&times;667 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (11.9%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 11.9%). Duplicate across sister species: 'Byasa crassipes' vs 'Byasa polla'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#090` | *Byasa crassipes* | Black Windmill | Papilionidae | `train` | `dataset/train/090_Byasa_crassipes/0900004.jpg` | `ACTIVE` |
| `#092` | *Byasa polla* | De Nicéville's Windmill | Papilionidae | `train` | `dataset/train/092_Byasa_polla/0920012.jpg` | `ACTIVE` |

### Cluster `CSD-030` — *Byasa crassipes* vs *Byasa polla*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `3a30d958e277c474fd81eb354c17f52da014495ed71ec893cf01fdba01029953`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/090_Byasa_crassipes/0900005.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/090_Byasa_crassipes/0900005.jpg) (3176&times;2117 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (20.4%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 20.4%). Duplicate across sister species: 'Byasa crassipes' vs 'Byasa polla'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#090` | *Byasa crassipes* | Black Windmill | Papilionidae | `train` | `dataset/train/090_Byasa_crassipes/0900005.jpg` | `ACTIVE` |
| `#092` | *Byasa polla* | De Nicéville's Windmill | Papilionidae | `train` | `dataset/train/092_Byasa_polla/0920006.jpg` | `ACTIVE` |

### Cluster `CSD-031` — *Byasa crassipes* vs *Byasa polla*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `40ed5ea0b22a1aba05a905fd444ae0617980e85b90679747f8bad19a721b3122`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/090_Byasa_crassipes/0900015.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/090_Byasa_crassipes/0900015.jpg) (1000&times;667 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (25.3%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 25.3%). Duplicate across sister species: 'Byasa crassipes' vs 'Byasa polla'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#090` | *Byasa crassipes* | Black Windmill | Papilionidae | `train` | `dataset/train/090_Byasa_crassipes/0900015.jpg` | `ACTIVE` |
| `#092` | *Byasa polla* | De Nicéville's Windmill | Papilionidae | `train` | `dataset/train/092_Byasa_polla/0920008.jpg` | `ACTIVE` |

### Cluster `CSD-032` — *Byasa crassipes* vs *Byasa polla*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `433808102fbd80c2245fea52473fb7274d917884771b258bea7b61e283ffdc1f`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/090_Byasa_crassipes/0900022.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/090_Byasa_crassipes/0900022.jpg) (735&times;608 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `ringlet (45.2%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 45.2%). Duplicate across sister species: 'Byasa crassipes' vs 'Byasa polla'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#090` | *Byasa crassipes* | Black Windmill | Papilionidae | `train` | `dataset/train/090_Byasa_crassipes/0900022.jpg` | `ACTIVE` |
| `#092` | *Byasa polla* | De Nicéville's Windmill | Papilionidae | `train` | `dataset/train/092_Byasa_polla/0920018.jpg` | `ACTIVE` |

### Cluster `CSD-034` — *Byasa polla* vs *Scobura woolletti*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERFAMILY` (Papilionidae, Hesperiidae)
- **SHA-256**: `f9cf4bd522d5588a8510f7274e911fd6ef4345aa968651e9c53aee7e98059069`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/092_Byasa_polla/0920010.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/092_Byasa_polla/0920010.jpg) (700&times;563 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (71.6%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 71.6%). Duplicate across sister species: 'Byasa polla' vs 'Scobura woolletti'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#092` | *Byasa polla* | De Nicéville's Windmill | Papilionidae | `train` | `dataset/train/092_Byasa_polla/0920010.jpg` | `ACTIVE` |
| `#124` | *Scobura woolletti* | Brown Forest Bob | Hesperiidae | `train` | `dataset/train/124_Scobura_woolletti/1240010.jpg` | `ACTIVE` |

### Cluster `CSD-035` — *Graphium macareus* vs *Graphium xenocles*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `73ce17f188f6125819b70f8245cc2b2bc8833942cfbe908871e7b9aa67267260`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/095_Graphium_macareus/0950003.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/095_Graphium_macareus/0950003.jpg) (800&times;533 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (61.7%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 61.7%). Duplicate across sister species: 'Graphium macareus' vs 'Graphium xenocles'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#095` | *Graphium macareus* | Lesser Zebra | Papilionidae | `train` | `dataset/train/095_Graphium_macareus/0950003.jpg` | `ACTIVE` |
| `#096` | *Graphium xenocles* | Great Zebra | Papilionidae | `train` | `dataset/train/096_Graphium_xenocles/0960015.jpg` | `ACTIVE` |

### Cluster `CSD-036` — *Graphium macareus* vs *Graphium xenocles*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `d48ff4aa17fbc64be6bfb8f08c548bf78c65bb65a40ab7890c7e45544be51cd0`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/095_Graphium_macareus/0950012.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/095_Graphium_macareus/0950012.jpg) (910&times;727 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `monarch (12.9%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (monarch, 12.9%). Duplicate across sister species: 'Graphium macareus' vs 'Graphium xenocles'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#095` | *Graphium macareus* | Lesser Zebra | Papilionidae | `train` | `dataset/train/095_Graphium_macareus/0950012.jpg` | `ACTIVE` |
| `#096` | *Graphium xenocles* | Great Zebra | Papilionidae | `train` | `dataset/train/096_Graphium_xenocles/0960008.jpg` | `ACTIVE` |

### Cluster `CSD-037` — *Graphium macareus* vs *Graphium xenocles*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Papilionidae)
- **SHA-256**: `5f5aaf9e41399e86b95fd6a9ea71560e6306dd643fadd3764a29bae8a92c0958`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/095_Graphium_macareus/0950016.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/095_Graphium_macareus/0950016.jpg) (300&times;200 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (31.4%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 31.4%). Duplicate across sister species: 'Graphium macareus' vs 'Graphium xenocles'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#095` | *Graphium macareus* | Lesser Zebra | Papilionidae | `train` | `dataset/train/095_Graphium_macareus/0950016.jpg` | `ACTIVE` |
| `#096` | *Graphium xenocles* | Great Zebra | Papilionidae | `train` | `dataset/train/096_Graphium_xenocles/0960019.jpg` | `ACTIVE` |

### Cluster `CSD-039` — *Pantoporia assamica* vs *Udara selma*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERFAMILY` (Lycaenidae, Nymphalidae)
- **SHA-256**: `01af609606f2b2508e58856970c7e8f1ad35710d105fdf4b0e9ad99c55e662cf`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/102_Pantoporia_assamica/1020006.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/102_Pantoporia_assamica/1020006.jpg) (500&times;368 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `book_jacket (27.8%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (book_jacket). Cross-interfamily collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#102` | *Pantoporia assamica* | Conjoined Lascar | Nymphalidae | `train` | `dataset/train/102_Pantoporia_assamica/1020006.jpg` | `ACTIVE` |
| `#116` | *Udara selma* | Bi-coloured Hedge Blue | Lycaenidae | `train` | `dataset/train/116_Udara_selma/1160019.jpg` | `ACTIVE` |

### Cluster `CSD-042` — *Pantoporia assamica* vs *Pantoporia bieti*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Nymphalidae)
- **SHA-256**: `4479d534b1e3d02f260e822a779149ae030b10af59eacc75d7f2633d57155232`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/102_Pantoporia_assamica/1020021.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/102_Pantoporia_assamica/1020021.jpg) (750&times;505 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `admiral (44.3%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (admiral, 44.3%). Duplicate across sister species: 'Pantoporia assamica' vs 'Pantoporia bieti'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#102` | *Pantoporia assamica* | Conjoined Lascar | Nymphalidae | `train` | `dataset/train/102_Pantoporia_assamica/1020021.jpg` | `ACTIVE` |
| `#103` | *Pantoporia bieti* | Tytler's Lascar | Nymphalidae | `train` | `dataset/train/103_Pantoporia_bieti/1030006.jpg` | `ACTIVE` |

### Cluster `CSD-046` — *Pithecops fulgens* vs *Arhopala silhetensis*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Lycaenidae)
- **SHA-256**: `977784e88f986c48a3bf33a0cce341efacb532b34236bb50fdd20000e58e9cd4`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/111_Pithecops_fulgens/1110005.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/111_Pithecops_fulgens/1110005.jpg) (1280&times;720 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (86.8%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 86.8%). Duplicate across sister species: 'Pithecops fulgens' vs 'Arhopala silhetensis'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#111` | *Pithecops fulgens* | Blue Quaker | Lycaenidae | `train` | `dataset/train/111_Pithecops_fulgens/1110005.jpg` | `ACTIVE` |
| `#113` | *Arhopala silhetensis* | Sylhet Oakblue | Lycaenidae | `train` | `dataset/train/113_Arhopala_silhetensis/1130025.jpg` | `ACTIVE` |

### Cluster `CSD-047` — *Pithecops fulgens* vs *Hidari bhawani*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERFAMILY` (Lycaenidae, Hesperiidae)
- **SHA-256**: `d6b869dd00f4a3e05bc8f22c488f1a957dc3fbb815043ea16036da4262d9bdcc`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/111_Pithecops_fulgens/1110011.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/111_Pithecops_fulgens/1110011.jpg) (2047&times;1229 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `bow (27.9%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (bow). Cross-interfamily collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#111` | *Pithecops fulgens* | Blue Quaker | Lycaenidae | `train` | `dataset/train/111_Pithecops_fulgens/1110011.jpg` | `ACTIVE` |
| `#121` | *Hidari bhawani* | Veined Palmer | Hesperiidae | `train` | `dataset/train/121_Hidari_bhawani/1210027.jpg` | `ACTIVE` |

### Cluster `CSD-048` — *Arhopala silhetensis* vs *Arhopala oenea*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Lycaenidae)
- **SHA-256**: `cf0d9e887edc32f80c3b9794ef3cc55cbb563db756854d6a22faee8f48397c1f`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/113_Arhopala_silhetensis/1130001.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/113_Arhopala_silhetensis/1130001.jpg) (1116&times;1080 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (93.6%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 93.6%). Duplicate across sister species: 'Arhopala silhetensis' vs 'Arhopala oenea'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#113` | *Arhopala silhetensis* | Sylhet Oakblue | Lycaenidae | `train` | `dataset/train/113_Arhopala_silhetensis/1130001.jpg` | `ACTIVE` |
| `#114` | *Arhopala oenea* | Hewitson's Dull Oakblue | Lycaenidae | `train` | `dataset/train/114_Arhopala_oenea/1140013.jpg` | `ACTIVE` |

### Cluster `CSD-049` — *Arhopala silhetensis* vs *Arhopala oenea*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Lycaenidae)
- **SHA-256**: `1dd446b3d1dfef4aded54fb1fbe6b4d140e33d557ace20aad30492b8d4936063`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/113_Arhopala_silhetensis/1130015.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/113_Arhopala_silhetensis/1130015.jpg) (700&times;667 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (98.8%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 98.8%). Duplicate across sister species: 'Arhopala silhetensis' vs 'Arhopala oenea'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#113` | *Arhopala silhetensis* | Sylhet Oakblue | Lycaenidae | `train` | `dataset/train/113_Arhopala_silhetensis/1130015.jpg` | `ACTIVE` |
| `#114` | *Arhopala oenea* | Hewitson's Dull Oakblue | Lycaenidae | `train` | `dataset/train/114_Arhopala_oenea/1140001.jpg` | `ACTIVE` |

### Cluster `CSD-050` — *Arhopala silhetensis* vs *Arhopala oenea*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Lycaenidae)
- **SHA-256**: `ac46c4a4dce4a9f73c6a192820290c1ac9f6f1e4f85e31aa0c15c98508af6331`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/113_Arhopala_silhetensis/1130019.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/113_Arhopala_silhetensis/1130019.jpg) (700&times;587 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (96.6%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 96.6%). Duplicate across sister species: 'Arhopala silhetensis' vs 'Arhopala oenea'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#113` | *Arhopala silhetensis* | Sylhet Oakblue | Lycaenidae | `train` | `dataset/train/113_Arhopala_silhetensis/1130019.jpg` | `ACTIVE` |
| `#114` | *Arhopala oenea* | Hewitson's Dull Oakblue | Lycaenidae | `train` | `dataset/train/114_Arhopala_oenea/1140017.jpg` | `ACTIVE` |

### Cluster `CSD-051` — *Arhopala silhetensis* vs *Arhopala oenea*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Lycaenidae)
- **SHA-256**: `1c827ab8f19c96755194cfa024d3dadf7eb5762f0502a3ed9d512ae98f8a3795`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/113_Arhopala_silhetensis/1130023.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/113_Arhopala_silhetensis/1130023.jpg) (1067&times;1107 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (95.1%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 95.1%). Duplicate across sister species: 'Arhopala silhetensis' vs 'Arhopala oenea'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#113` | *Arhopala silhetensis* | Sylhet Oakblue | Lycaenidae | `train` | `dataset/train/113_Arhopala_silhetensis/1130023.jpg` | `ACTIVE` |
| `#114` | *Arhopala oenea* | Hewitson's Dull Oakblue | Lycaenidae | `train` | `dataset/train/114_Arhopala_oenea/1140004.jpg` | `ACTIVE` |

### Cluster `CSD-052` — *Pyroneura margherita* vs *Salanoemia sala*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `c297d3667b59dec3244cdfb6fcc0c11f41935d73cf08e0d3eb8cfaf94dce6d50`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/119_Pyroneura_margherita/1190016.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/119_Pyroneura_margherita/1190016.jpg) (3000&times;2000 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `monarch (48.2%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (monarch, 48.2%). Duplicate across sister species: 'Pyroneura margherita' vs 'Salanoemia sala'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#119` | *Pyroneura margherita* | Yellow-vein Lancer | Hesperiidae | `train` | `dataset/train/119_Pyroneura_margherita/1190016.jpg` | `ACTIVE` |
| `#123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `train` | `dataset/train/123_Salanoemia_sala/1230016.jpg` | `ACTIVE` |

### Cluster `CSD-053` — *Pyroneura margherita* vs *Salanoemia sala*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `aea95cf4aa0a4461bd687f11038340acc263b8d69c85f3347ba1ee96035c35df`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/119_Pyroneura_margherita/1190023.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/119_Pyroneura_margherita/1190023.jpg) (600&times;400 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (40.5%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 40.5%). Duplicate across sister species: 'Pyroneura margherita' vs 'Salanoemia sala'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#119` | *Pyroneura margherita* | Yellow-vein Lancer | Hesperiidae | `train` | `dataset/train/119_Pyroneura_margherita/1190023.jpg` | `ACTIVE` |
| `#123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `train` | `dataset/train/123_Salanoemia_sala/1230028.jpg` | `ACTIVE` |

### Cluster `CSD-054` — *Pyroneura margherita* vs *Salanoemia sala*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `f1179f7fad38133ad555e1cb19936e162a93c2babdc8ff79099623e2acc8be60`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/119_Pyroneura_margherita/1190028.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/119_Pyroneura_margherita/1190028.jpg) (3000&times;2000 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (48.1%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 48.1%). Duplicate across sister species: 'Pyroneura margherita' vs 'Salanoemia sala'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#119` | *Pyroneura margherita* | Yellow-vein Lancer | Hesperiidae | `train` | `dataset/train/119_Pyroneura_margherita/1190028.jpg` | `ACTIVE` |
| `#123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `train` | `dataset/train/123_Salanoemia_sala/1230024.jpg` | `ACTIVE` |

### Cluster `CSD-056` — *Darpa pteria* vs *Hidari bhawani*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `2839e0b44cd69974eb2e967a089b6c40684734724d881d3db843e7cd42e09297`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/120_Darpa_pteria/1200006.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/120_Darpa_pteria/1200006.jpg) (2048&times;1152 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `web_site (74.2%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (web_site). Cross-intergeneric same family collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#120` | *Darpa pteria* | Snowy Angle | Hesperiidae | `train` | `dataset/train/120_Darpa_pteria/1200006.jpg` | `ACTIVE` |
| `#121` | *Hidari bhawani* | Veined Palmer | Hesperiidae | `train` | `dataset/train/121_Hidari_bhawani/1210019.jpg` | `ACTIVE` |

### Cluster `CSD-057` — *Salanoemia sala* vs *Scobura woolletti*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `4af8dee2467f5fa7d312a5565c45c3ff3b45c3ed1bc8d4bc8395e02535d1836f`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/train/123_Salanoemia_sala/1230002.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/123_Salanoemia_sala/1230002.jpg) (388&times;339 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `envelope (49.5%)`
- **Suggested Determination**: **`LIKELY_NON_BUTTERFLY`**
- **Suggested Action**: `PURGE_ALL_SAMPLES`
- **Taxonomic Notes**: Flagged by visual screening (envelope). Cross-intergeneric same family collision. Likely non-biological stock graphic, book scan, or web template.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `train` | `dataset/train/123_Salanoemia_sala/1230002.jpg` | `ACTIVE` |
| `#124` | *Scobura woolletti* | Brown Forest Bob | Hesperiidae | `train` | `dataset/train/124_Scobura_woolletti/1240022.jpg` | `ACTIVE` |

### Cluster `CSD-059` — *Halpe aucma* vs *Halpe kusala*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `CONGENERIC` (Hesperiidae)
- **SHA-256**: `b9e499ed40755f2bfe96bf1a24587584b66bbc7455eabaa5f153a7a5966456cc`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/test/035_Halpe_aucma/0350020.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/test/035_Halpe_aucma/0350020.jpg) (800&times;533 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `lycaenid (35.2%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (lycaenid, 35.2%). Duplicate across sister species: 'Halpe aucma' vs 'Halpe kusala'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#035` | *Halpe aucma* | Gold-spotted Ace | Hesperiidae | `test` | `dataset/test/035_Halpe_aucma/0350020.jpg` | `ACTIVE` |
| `#036` | *Halpe kusala* | Plain Ace | Hesperiidae | `test` | `dataset/test/036_Halpe_kusala/0360019.jpg` | `ACTIVE` |

### Cluster `CSD-060` — *Pyroneura margherita* vs *Salanoemia sala*
- **Status**: `[ACTIVE MULTI-SPECIES CONFLICT]` 
- **Taxonomic Relation**: `INTERGENERIC_SAME_FAMILY` (Hesperiidae)
- **SHA-256**: `77e71fe8c8bd5526c2e194c7ddf11a3316a7f34f4193f24dba117cfd38bc415f`
- **Active Files**: `2` active | `0` quarantined (Total: `2`)
- **Sample Image**: [`dataset/test/119_Pyroneura_margherita/1190035.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/test/119_Pyroneura_margherita/1190035.jpg) (600&times;316 px, `JPEG`, `ACTIVE`)
- **AI Screening**: `ringlet (34.7%)`
- **Suggested Determination**: **`GENUINE_BUTTERFLY_MISLABELING`**
- **Suggested Action**: `HOLD_IN_DATASET`
- **Taxonomic Notes**: Specimen appears to be authentic butterfly (ringlet, 34.7%). Duplicate across sister species: 'Pyroneura margherita' vs 'Salanoemia sala'. Taxonomist review required to assign true species.

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| `#119` | *Pyroneura margherita* | Yellow-vein Lancer | Hesperiidae | `test` | `dataset/test/119_Pyroneura_margherita/1190035.jpg` | `ACTIVE` |
| `#123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `test` | `dataset/test/123_Salanoemia_sala/1230035.jpg` | `ACTIVE` |
