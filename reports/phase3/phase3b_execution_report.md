# Phase 3B Mega-Cluster Quarantine Execution & Forensic Verification Report

**Execution Timestamp**: 2026-11-02 23:47:38  
**Verification Timestamp**: 2026-11-02 23:48:00  
**Operation Target**: 18 active files across confirmed non-butterfly mega-clusters (`CSD-001`, `CSD-002`, `CSD-008`)  
**Protected Taxa**: `CSD-009` (*Graphium*) and `CSD-010` (*Athyma*) remain **100% untouched**  
**Operation Manifest**: [`dataset/quarantine/phase3b_manifest.json`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/quarantine/phase3b_manifest.json)  
**Master Reversible Ledger**: [`dataset/quarantine/quarantine_manifest.json`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/quarantine/quarantine_manifest.json)  
**Execution Status**: **100% SUCCESSFUL (0 Errors, 0 Collisions, 0 Data Loss)**

---

## 1. Post-Execution Verification Matrix

| # | Verification Check | Target / Expected | Actual Post-Execution State | Status |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Operation-specific manifest generated | 18 records | [`dataset/quarantine/phase3b_manifest.json`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/quarantine/phase3b_manifest.json) (18 records) | **PASS** |
| **2** | All 18 quarantined files match SHA-256 hashes | 18 matches | **18 / 18 verified byte-for-byte identical** | **PASS** |
| **3** | Original source paths absent from `dataset/train/` | 18 absent | **18 / 18 confirmed absent** | **PASS** |
| **4** | Active dataset image count | 4,067 images | **4,067 images** (Train: 3,095, Test: 972) | **PASS** |
| **5** | Quarantine holding image count | 431 images | **431 images** (Phase 1: 413, Phase 3B: +18) | **PASS** |
| **6** | Total tracked images | 4,498 images | **4,498 images** ($4,067 + 431 = 4,498$) | **PASS** |
| **7** | Total bytes conserved (Active + Quarantine == Backup) | 1,195,959,551 B | **1,195,959,551 Bytes (Exact match)** | **PASS** |
| **8** | All 125 species folders populated in train and test | 125 train, 125 test | **125 train, 125 test populated (0 empty folders)** | **PASS** |
| **9** | Protected taxa `CSD-009` and `CSD-010` untouched | 5 active files | **5 / 5 confirmed present and untouched** | **PASS** |
| **10** | Full backup at `backups/dataset_backup_20261102_222309/` intact | 4,498 files | **4,498 files intact (3,277 train, 1,221 test)** | **PASS** |
| **11** | Master system files (`labels.txt`, Java enums) untouched | 0 modified | **100% untouched** | **PASS** |

---

## 2. Updated Dataset Inventory & Recalculation

| Split | Pre-Phase 3B Count | Quarantined in Phase 3B | Post-Phase 3B Count | Storage Size | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Train (`dataset/train/`)** | 3,113 | **-18 files** | **3,095 files** | 816.92 MB | 18 medical diagrams purged |
| **Test (`dataset/test/`)** | 972 | **0 files** | **972 files** | 244.17 MB | Clean benchmark unchanged |
| **Active Dataset Total** | **4,085** | **-18 files** | **4,067 files** | **1,061.09 MB** | Active ML dataset |
| **Quarantine (`dataset/quarantine/`)** | 413 | **+18 files** | **431 files** | **79.47 MB** | Reversible holding |
| **Total Tracked Images** | **4,498** | **0 net change** | **4,498 files** | **1,140.56 MB** | **Exact conservation** |

---

## 3. Inventory of the 18 Successfully Quarantined Files

| # | Cluster ID | Description | Class ID | Species Name | Original Path | Quarantine Destination Path | SHA-256 Hash |
| :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| 1 | `CSD-001` | Human Body Anatomy Diagram | `#090` | *Byasa crassipes* | `dataset/train/090_Byasa_crassipes/0900017.jpg` | `dataset/quarantine/train/090_Byasa_crassipes/0900017.jpg` | `ec3757e316e2...` |
| 2 | `CSD-001` | Human Body Anatomy Diagram | `#100` | *Euthalia telchinia* | `dataset/train/100_Euthalia_telchinia/1000017.jpg` | `dataset/quarantine/train/100_Euthalia_telchinia/1000017.jpg` | `ec3757e316e2...` |
| 3 | `CSD-001` | Human Body Anatomy Diagram | `#103` | *Pantoporia bieti* | `dataset/train/103_Pantoporia_bieti/1030010.jpg` | `dataset/quarantine/train/103_Pantoporia_bieti/1030010.jpg` | `ec3757e316e2...` |
| 4 | `CSD-001` | Human Body Anatomy Diagram | `#107` | *Athyma punctata* | `dataset/train/107_Athyma_punctata/1070017.jpg` | `dataset/quarantine/train/107_Athyma_punctata/1070017.jpg` | `ec3757e316e2...` |
| 5 | `CSD-001` | Human Body Anatomy Diagram | `#111` | *Pithecops fulgens* | `dataset/train/111_Pithecops_fulgens/1110004.jpg` | `dataset/quarantine/train/111_Pithecops_fulgens/1110004.jpg` | `ec3757e316e2...` |
| 6 | `CSD-001` | Human Body Anatomy Diagram | `#115` | *Simiskina phalena* | `dataset/train/115_Simiskina_phalena/1150019.jpg` | `dataset/quarantine/train/115_Simiskina_phalena/1150019.jpg` | `ec3757e316e2...` |
| 7 | `CSD-001` | Human Body Anatomy Diagram | `#116` | *Udara selma* | `dataset/train/116_Udara_selma/1160017.jpg` | `dataset/quarantine/train/116_Udara_selma/1160017.jpg` | `ec3757e316e2...` |
| 8 | `CSD-001` | Human Body Anatomy Diagram | `#119` | *Pyroneura margherita* | `dataset/train/119_Pyroneura_margherita/1190027.jpg` | `dataset/quarantine/train/119_Pyroneura_margherita/1190027.jpg` | `ec3757e316e2...` |
| 9 | `CSD-001` | Human Body Anatomy Diagram | `#120` | *Darpa pteria* | `dataset/train/120_Darpa_pteria/1200019.jpg` | `dataset/quarantine/train/120_Darpa_pteria/1200019.jpg` | `ec3757e316e2...` |
| 10 | `CSD-001` | Human Body Anatomy Diagram | `#122` | *Plastingia naga* | `dataset/train/122_Plastingia_naga/1220019.jpg` | `dataset/quarantine/train/122_Plastingia_naga/1220019.jpg` | `ec3757e316e2...` |
| 11 | `CSD-001` | Human Body Anatomy Diagram | `#124` | *Scobura woolletti* | `dataset/train/124_Scobura_woolletti/1240027.jpg` | `dataset/quarantine/train/124_Scobura_woolletti/1240027.jpg` | `ec3757e316e2...` |
| 12 | `CSD-002` | Spinal Cord Anatomy Diagram | `#099` | *Elymnias peali* | `dataset/train/099_Elymnias_peali/0990017.jpg` | `dataset/quarantine/train/099_Elymnias_peali/0990017.jpg` | `9b83cd4326f8...` |
| 13 | `CSD-002` | Spinal Cord Anatomy Diagram | `#102` | *Pantoporia assamica* | `dataset/train/102_Pantoporia_assamica/1020010.jpg` | `dataset/quarantine/train/102_Pantoporia_assamica/1020010.jpg` | `9b83cd4326f8...` |
| 14 | `CSD-002` | Spinal Cord Anatomy Diagram | `#115` | *Simiskina phalena* | `dataset/train/115_Simiskina_phalena/1150027.jpg` | `dataset/quarantine/train/115_Simiskina_phalena/1150027.jpg` | `9b83cd4326f8...` |
| 15 | `CSD-002` | Spinal Cord Anatomy Diagram | `#116` | *Udara selma* | `dataset/train/116_Udara_selma/1160026.jpg` | `dataset/quarantine/train/116_Udara_selma/1160026.jpg` | `9b83cd4326f8...` |
| 16 | `CSD-008` | Nerve Anatomy Illustration | `#119` | *Pyroneura margherita* | `dataset/train/119_Pyroneura_margherita/1190025.jpg` | `dataset/quarantine/train/119_Pyroneura_margherita/1190025.jpg` | `5906b80b585f...` |
| 17 | `CSD-008` | Nerve Anatomy Illustration | `#123` | *Salanoemia sala* | `dataset/train/123_Salanoemia_sala/1230021.jpg` | `dataset/quarantine/train/123_Salanoemia_sala/1230021.jpg` | `5906b80b585f...` |
| 18 | `CSD-008` | Nerve Anatomy Illustration | `#124` | *Scobura woolletti* | `dataset/train/124_Scobura_woolletti/1240017.jpg` | `dataset/quarantine/train/124_Scobura_woolletti/1240017.jpg` | `5906b80b585f...` |

*(Note: The other 2 files belonging to these 3 clusters were already in quarantine from Phase 1: `dataset/test/123_Salanoemia_sala/1230033.jpg` and `dataset/test/100_Euthalia_telchinia/1000031.jpg`)*

---

## 4. Protected Biological Taxa Status

The genuine butterfly clusters remain completely untouched in the active dataset:
- **`CSD-009` (*Graphium* swordtails/zebras)**:
  - `dataset/train/093_Graphium_agetes/0930023.jpg` (**Active & Intact**)
  - `dataset/train/095_Graphium_macareus/0950023.jpg` (**Active & Intact**)
- **`CSD-010` (*Athyma* sergeants)**:
  - `dataset/train/105_Athyma_ranga/1050023.jpg` (**Active & Intact**)
  - `dataset/train/106_Athyma_pravara/1060010.jpg` (**Active & Intact**)
  - `dataset/train/107_Athyma_punctata/1070023.jpg` (**Active & Intact**)

---

## 5. Reversibility & Rollback Protocol

The 18 files moved in this operation can be reversed back into `dataset/train/` independently from Phase 1 by running:
```bash
.venv/bin/python pipeline/tools/mega_cluster_quarantine_manager.py --restore
```
Alternatively, all 431 quarantined files can be restored to their pre-audit state at any time via:
```bash
.venv/bin/python pipeline/tools/quarantine_manager.py --restore
```
