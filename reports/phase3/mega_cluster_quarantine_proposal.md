# Phase 3B Mega-Cluster Quarantine Dry-Run Proposal

**Generated**: 2026-11-02 23:47:30  
**Status**: **DRY-RUN ONLY (Zero files moved or deleted)**  
**Target Clusters for Purge**: `CSD-001`, `CSD-002`, `CSD-008` (Anatomical / non-butterfly diagrams)  
**Untouched Clusters Preserved**: `CSD-009`, `CSD-010` (*Graphium* and *Athyma* genuine butterflies)

---

## 1. Executive Summary & Impact Table

| Dataset Split | Active Count Before | Proposed for Quarantine | Expected Active After | Expected Status |
| :--- | :---: | :---: | :---: | :--- |
| **Train (`dataset/train/`)** | 3,113 | **18 files** | **3,095 files** | 18 non-butterfly diagrams removed |
| **Test (`dataset/test/`)** | 972 | **0 files** | **972 files** | Clean benchmark unchanged |
| **Active Dataset Total** | **4,085** | **18 files** | **4,067 files** | Non-butterfly noise removed |
| **Quarantine (`dataset/quarantine/`)** | 413 | **+18 files** | **431 files** | Reversibly preserved |
| **Total Tracked Dataset** | **4,498** | **0 net change** | **4,498 files** | Exact conservation |

---

## 2. Full Inventory of the 20 Mega-Cluster Files

### A. The 18 Active Files Proposed to be Moved (dataset/train/ &rarr; dataset/quarantine/)

| # | Cluster | Class ID | Scientific Name | Original Dataset Path | Destination Quarantine Path | SHA-256 Hash |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| 1 | `CSD-001` | `#090` | *Byasa crassipes* | `dataset/train/090_Byasa_crassipes/0900017.jpg` | `dataset/quarantine/train/090_Byasa_crassipes/0900017.jpg` | `<code>ec3757e316e2...</code>` |
| 2 | `CSD-001` | `#100` | *Euthalia telchinia* | `dataset/train/100_Euthalia_telchinia/1000017.jpg` | `dataset/quarantine/train/100_Euthalia_telchinia/1000017.jpg` | `<code>ec3757e316e2...</code>` |
| 3 | `CSD-001` | `#103` | *Pantoporia bieti* | `dataset/train/103_Pantoporia_bieti/1030010.jpg` | `dataset/quarantine/train/103_Pantoporia_bieti/1030010.jpg` | `<code>ec3757e316e2...</code>` |
| 4 | `CSD-001` | `#107` | *Athyma punctata* | `dataset/train/107_Athyma_punctata/1070017.jpg` | `dataset/quarantine/train/107_Athyma_punctata/1070017.jpg` | `<code>ec3757e316e2...</code>` |
| 5 | `CSD-001` | `#111` | *Pithecops fulgens* | `dataset/train/111_Pithecops_fulgens/1110004.jpg` | `dataset/quarantine/train/111_Pithecops_fulgens/1110004.jpg` | `<code>ec3757e316e2...</code>` |
| 6 | `CSD-001` | `#115` | *Simiskina phalena* | `dataset/train/115_Simiskina_phalena/1150019.jpg` | `dataset/quarantine/train/115_Simiskina_phalena/1150019.jpg` | `<code>ec3757e316e2...</code>` |
| 7 | `CSD-001` | `#116` | *Udara selma* | `dataset/train/116_Udara_selma/1160017.jpg` | `dataset/quarantine/train/116_Udara_selma/1160017.jpg` | `<code>ec3757e316e2...</code>` |
| 8 | `CSD-001` | `#119` | *Pyroneura margherita* | `dataset/train/119_Pyroneura_margherita/1190027.jpg` | `dataset/quarantine/train/119_Pyroneura_margherita/1190027.jpg` | `<code>ec3757e316e2...</code>` |
| 9 | `CSD-001` | `#120` | *Darpa pteria* | `dataset/train/120_Darpa_pteria/1200019.jpg` | `dataset/quarantine/train/120_Darpa_pteria/1200019.jpg` | `<code>ec3757e316e2...</code>` |
| 10 | `CSD-001` | `#122` | *Plastingia naga* | `dataset/train/122_Plastingia_naga/1220019.jpg` | `dataset/quarantine/train/122_Plastingia_naga/1220019.jpg` | `<code>ec3757e316e2...</code>` |
| 11 | `CSD-001` | `#124` | *Scobura woolletti* | `dataset/train/124_Scobura_woolletti/1240027.jpg` | `dataset/quarantine/train/124_Scobura_woolletti/1240027.jpg` | `<code>ec3757e316e2...</code>` |
| 12 | `CSD-002` | `#099` | *Elymnias peali* | `dataset/train/099_Elymnias_peali/0990017.jpg` | `dataset/quarantine/train/099_Elymnias_peali/0990017.jpg` | `<code>9b83cd4326f8...</code>` |
| 13 | `CSD-002` | `#102` | *Pantoporia assamica* | `dataset/train/102_Pantoporia_assamica/1020010.jpg` | `dataset/quarantine/train/102_Pantoporia_assamica/1020010.jpg` | `<code>9b83cd4326f8...</code>` |
| 14 | `CSD-002` | `#115` | *Simiskina phalena* | `dataset/train/115_Simiskina_phalena/1150027.jpg` | `dataset/quarantine/train/115_Simiskina_phalena/1150027.jpg` | `<code>9b83cd4326f8...</code>` |
| 15 | `CSD-002` | `#116` | *Udara selma* | `dataset/train/116_Udara_selma/1160026.jpg` | `dataset/quarantine/train/116_Udara_selma/1160026.jpg` | `<code>9b83cd4326f8...</code>` |
| 16 | `CSD-008` | `#119` | *Pyroneura margherita* | `dataset/train/119_Pyroneura_margherita/1190025.jpg` | `dataset/quarantine/train/119_Pyroneura_margherita/1190025.jpg` | `<code>5906b80b585f...</code>` |
| 17 | `CSD-008` | `#123` | *Salanoemia sala* | `dataset/train/123_Salanoemia_sala/1230021.jpg` | `dataset/quarantine/train/123_Salanoemia_sala/1230021.jpg` | `<code>5906b80b585f...</code>` |
| 18 | `CSD-008` | `#124` | *Scobura woolletti* | `dataset/train/124_Scobura_woolletti/1240017.jpg` | `dataset/quarantine/train/124_Scobura_woolletti/1240017.jpg` | `<code>5906b80b585f...</code>` |

### B. The 2 Files Already Safely in Quarantine from Phase 1

| # | Cluster | Class ID | Scientific Name | Original Path | Current Location in Quarantine | SHA-256 Hash |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| 1 | `CSD-002` | `#123` | *Salanoemia sala* | `dataset/test/123_Salanoemia_sala/1230033.jpg` | `dataset/quarantine/test/123_Salanoemia_sala/1230033.jpg` | `<code>9b83cd4326f8...</code>` |
| 2 | `CSD-008` | `#100` | *Euthalia telchinia* | `dataset/test/100_Euthalia_telchinia/1000031.jpg` | `dataset/quarantine/test/100_Euthalia_telchinia/1000031.jpg` | `<code>5906b80b585f...</code>` |

---

## 3. Species Completeness & Preservation Guarantee

Post-quarantine simulation across all affected species folders confirms:
- **0 species folders are left empty**.
- Every affected folder retains at least **26 active training images**.
- `CSD-009` (3 files, *Graphium*) and `CSD-010` (3 files, *Athyma*) remain **100% untouched in the active dataset**.
- The full snapshot in `backups/dataset_backup_20261102_222309/` remains byte-for-byte intact.

---

## 4. Next Step: Execution Protocol

No files have been moved. To execute this safe quarantine when you approve, run:
```bash
.venv/bin/python pipeline/tools/mega_cluster_quarantine_manager.py --execute
```
To reverse and restore all 18 files at any time:
```bash
.venv/bin/python pipeline/tools/mega_cluster_quarantine_manager.py --restore
```
