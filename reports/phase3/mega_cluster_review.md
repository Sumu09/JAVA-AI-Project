# Phase 3A: Cross-Species Mega-Clusters Forensic Review

**Review Date**: 2026-11-02 23:33:16  
**Target Clusters**: **5 Mega-Clusters** (&ge; 3 species, 26 total files)  
**Interactive Visual Contact Sheet**: [`mega_cluster_contact_sheet.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_contact_sheet.html)  
**Review Decision Ledger**: [`mega_cluster_review.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_review.csv)  
**Validator Tool**: [`pipeline/tools/validate_phase3_review.py`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/pipeline/tools/validate_phase3_review.py)

---

## 1. Executive Summary

In a butterfly classification dataset, a single image hash appearing under 3 or more species represents high-severity cross-contamination. These 5 clusters account for **26 total image files** spanning across **26 species folders**.

| Cluster ID | Conflicting Species | Total Files | Sample Image | AI Screen | Pre-filled Determination | Recommended Action |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **`CSD-001`** | **11 species** | 11 files | `0900017.jpg` | `electric_guitar (53.3%)` | **`CONFIRMED_NON_BUTTERFLY`** | Purge from all 11 folders |
| **`CSD-002`** | **5 species** | 5 files | `0990017.jpg` | `envelope (14.5%)` | **`CONFIRMED_NON_BUTTERFLY`** | Purge from all 5 folders |
| **`CSD-008`** | **4 species** | 4 files | `1190025.jpg` | `stethoscope (21.0%)` | **`CONFIRMED_NON_BUTTERFLY`** | Purge from all 4 folders |
| **`CSD-009`** | **3 species** | 3 files | `0930023.jpg` | `lycaenid (22.7%)` | **`UNCERTAIN`** | Hold pending taxonomist review |
| **`CSD-010`** | **3 species** | 3 files | `1050023.jpg` | `admiral (69.4%)` | **`UNCERTAIN`** | Hold pending taxonomist review |

---

## 2. Cluster Details & Evidence

### Cluster `CSD-001` (11 Species &bull; 11 Files)
- **SHA-256**: `ec3757e316e21cac4ddc101e55a1d025a79b3f6666bfc75ff622a4b92e3a3ade`
- **Sample Image**: [`dataset/train/090_Byasa_crassipes/0900017.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/090_Byasa_crassipes/0900017.jpg) (1000&times;1429 px, JPEG, Status: `ACTIVE`)
- **Predicted Subject**: `electric_guitar (53.3%)`
- **Pre-filled Determination**: **`CONFIRMED_NON_BUTTERFLY`**
- **Action Plan**: `PURGE_ALL_SAMPLES`
- **Reviewer Notes**: Electric guitar stock photo downloaded for 11 rare species. High-confidence non-biological noise.

| Class ID | Scientific Name | Common Name | Family | File Path | Split |
| :---: | :--- | :--- | :--- | :--- | :---: |
| `090` | *Byasa crassipes* | Black Windmill | Papilionidae | `dataset/train/090_Byasa_crassipes/0900017.jpg` | `train` |
| `100` | *Euthalia telchinia* | Blue Baron | Nymphalidae | `dataset/train/100_Euthalia_telchinia/1000017.jpg` | `train` |
| `103` | *Pantoporia bieti* | Tytler's Lascar | Nymphalidae | `dataset/train/103_Pantoporia_bieti/1030010.jpg` | `train` |
| `107` | *Athyma punctata* | White-bordered Sergeant | Nymphalidae | `dataset/train/107_Athyma_punctata/1070017.jpg` | `train` |
| `111` | *Pithecops fulgens* | Blue Quaker | Lycaenidae | `dataset/train/111_Pithecops_fulgens/1110004.jpg` | `train` |
| `115` | *Simiskina phalena* | Broad-branded Brilliant | Lycaenidae | `dataset/train/115_Simiskina_phalena/1150019.jpg` | `train` |
| `116` | *Udara selma* | Bi-coloured Hedge Blue | Lycaenidae | `dataset/train/116_Udara_selma/1160017.jpg` | `train` |
| `119` | *Pyroneura margherita* | Yellow-vein Lancer | Hesperiidae | `dataset/train/119_Pyroneura_margherita/1190027.jpg` | `train` |
| `120` | *Darpa pteria* | Snowy Angle | Hesperiidae | `dataset/train/120_Darpa_pteria/1200019.jpg` | `train` |
| `122` | *Plastingia naga* | Chequered Lancer | Hesperiidae | `dataset/train/122_Plastingia_naga/1220019.jpg` | `train` |
| `124` | *Scobura woolletti* | Brown Forest Bob | Hesperiidae | `dataset/train/124_Scobura_woolletti/1240027.jpg` | `train` |

---

### Cluster `CSD-002` (5 Species &bull; 5 Files)
- **SHA-256**: `9b83cd4326f842169566119b55013d6593f19e9d382c41cafccf5189a23c23dc`
- **Sample Image**: [`dataset/train/099_Elymnias_peali/0990017.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/099_Elymnias_peali/0990017.jpg) (500&times;341 px, JPEG, Status: `ACTIVE`)
- **Predicted Subject**: `envelope (14.5%)`
- **Pre-filled Determination**: **`CONFIRMED_NON_BUTTERFLY`**
- **Action Plan**: `PURGE_ALL_SAMPLES`
- **Reviewer Notes**: Envelope / document web graphic placeholder downloaded for 5 rare species. Non-biological noise.

| Class ID | Scientific Name | Common Name | Family | File Path | Split |
| :---: | :--- | :--- | :--- | :--- | :---: |
| `099` | *Elymnias peali* | Peal's Palmfly | Nymphalidae | `dataset/train/099_Elymnias_peali/0990017.jpg` | `train` |
| `102` | *Pantoporia assamica* | Conjoined Lascar | Nymphalidae | `dataset/train/102_Pantoporia_assamica/1020010.jpg` | `train` |
| `115` | *Simiskina phalena* | Broad-branded Brilliant | Lycaenidae | `dataset/train/115_Simiskina_phalena/1150027.jpg` | `train` |
| `116` | *Udara selma* | Bi-coloured Hedge Blue | Lycaenidae | `dataset/train/116_Udara_selma/1160026.jpg` | `train` |
| `123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `dataset/test/123_Salanoemia_sala/1230033.jpg` | `test` |

---

### Cluster `CSD-008` (4 Species &bull; 4 Files)
- **SHA-256**: `5906b80b585fb9f9fad213f6ddef84e3f613780e3d9e13ba0b4c0baa55b98dd3`
- **Sample Image**: [`dataset/train/119_Pyroneura_margherita/1190025.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/119_Pyroneura_margherita/1190025.jpg) (1000&times;521 px, JPEG, Status: `ACTIVE`)
- **Predicted Subject**: `stethoscope (21.0%)`
- **Pre-filled Determination**: **`CONFIRMED_NON_BUTTERFLY`**
- **Action Plan**: `PURGE_ALL_SAMPLES`
- **Reviewer Notes**: Web banner / medical graphic placeholder downloaded across 4 species. Non-biological noise.

| Class ID | Scientific Name | Common Name | Family | File Path | Split |
| :---: | :--- | :--- | :--- | :--- | :---: |
| `119` | *Pyroneura margherita* | Yellow-vein Lancer | Hesperiidae | `dataset/train/119_Pyroneura_margherita/1190025.jpg` | `train` |
| `123` | *Salanoemia sala* | Maculate Lancer | Hesperiidae | `dataset/train/123_Salanoemia_sala/1230021.jpg` | `train` |
| `124` | *Scobura woolletti* | Brown Forest Bob | Hesperiidae | `dataset/train/124_Scobura_woolletti/1240017.jpg` | `train` |
| `100` | *Euthalia telchinia* | Blue Baron | Nymphalidae | `dataset/test/100_Euthalia_telchinia/1000031.jpg` | `test` |

---

### Cluster `CSD-009` (3 Species &bull; 3 Files)
- **SHA-256**: `bad15e057e4c381095c5d0ac6ce07f6f5d9782a35a70bf3e4b1394aeef178f66`
- **Sample Image**: [`dataset/train/093_Graphium_agetes/0930023.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/093_Graphium_agetes/0930023.jpg) (1483&times;1080 px, JPEG, Status: `ACTIVE`)
- **Predicted Subject**: `lycaenid (22.7%)`
- **Pre-filled Determination**: **`UNCERTAIN`**
- **Action Plan**: `HOLD_IN_DATASET`
- **Reviewer Notes**: Authentic butterfly specimen in genus Graphium (Swordtail/Zebra). Pending taxonomist assignment between G. agetes, G. macareus, and G. xenocles.

| Class ID | Scientific Name | Common Name | Family | File Path | Split |
| :---: | :--- | :--- | :--- | :--- | :---: |
| `093` | *Graphium agetes* | Fourbar Swallowtail | Papilionidae | `dataset/train/093_Graphium_agetes/0930023.jpg` | `train` |
| `095` | *Graphium macareus* | Lesser Zebra | Papilionidae | `dataset/train/095_Graphium_macareus/0950023.jpg` | `train` |
| `096` | *Graphium xenocles* | Great Zebra | Papilionidae | `dataset/test/096_Graphium_xenocles/0960029.jpg` | `test` |

---

### Cluster `CSD-010` (3 Species &bull; 3 Files)
- **SHA-256**: `2e090123be4252434eab1549ca4b86cc0286de518fabf3c58624db4602a60298`
- **Sample Image**: [`dataset/train/105_Athyma_ranga/1050023.jpg`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/train/105_Athyma_ranga/1050023.jpg) (1600&times;1152 px, JPEG, Status: `ACTIVE`)
- **Predicted Subject**: `admiral (69.4%)`
- **Pre-filled Determination**: **`UNCERTAIN`**
- **Action Plan**: `HOLD_IN_DATASET`
- **Reviewer Notes**: Authentic butterfly specimen in genus Athyma (Sergeant). Pending taxonomist assignment between A. ranga, A. pravara, and A. punctata.

| Class ID | Scientific Name | Common Name | Family | File Path | Split |
| :---: | :--- | :--- | :--- | :--- | :---: |
| `105` | *Athyma ranga* | Blackvein Sergeant | Nymphalidae | `dataset/train/105_Athyma_ranga/1050023.jpg` | `train` |
| `106` | *Athyma pravara* | Unbroken Sergeant | Nymphalidae | `dataset/train/106_Athyma_pravara/1060010.jpg` | `train` |
| `107` | *Athyma punctata* | White-bordered Sergeant | Nymphalidae | `dataset/train/107_Athyma_punctata/1070023.jpg` | `train` |

---

## 3. Human Review Instructions

1. Open [`mega_cluster_contact_sheet.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_contact_sheet.html) in your web browser.
2. Inspect the high-resolution images for each of the 5 clusters.
3. Review or adjust determinations in [`mega_cluster_review.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_review.csv).
4. Run the validator to verify decision consistency:
   ```bash
   .venv/bin/python pipeline/tools/validate_phase3_review.py
   ```
5. No images will be moved or quarantined until you review and approve the validated plan.
