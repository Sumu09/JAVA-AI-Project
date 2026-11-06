# Cross-Species Duplicates Forensic Biological Assessment

**Analysis Date**: 2026-11-02 23:25:51  
**Total Duplicate Clusters**: **60 clusters** (146 total files)  
**Interactive Visual Contact Sheet**: [`cross_species_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/cross_species_contact_sheets.html)  
**Review Decision Ledger Template**: [`cross_species_review_template.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/cross_species_review_template.csv)

---

## 1. Typology of Cross-Species Contamination

Cross-species duplicates occur when identical image files were downloaded and deposited into two or more distinct species folders. Forensic categorization reveals three distinct etiologies:

| Cluster Category | Count | Primary Cause / Biological Significance | Recommended Human Action |
| :--- | :---: | :--- | :--- |
| **Multi-Species Mega-Clusters (&ge; 3 taxa)** | **5 clusters** (25 files) | Automated crawler downloading identical fallback thumbnails, stock photos, or placeholders across multiple rare search queries. (e.g. CSD-001 electric guitar across 11 species). | **Purge from all species.** High probability of complete non-biological junk. |
| **Congeneric Species Pairs (Same Genus)** | **12 clusters** (24 files) | Crawler ambiguity between visually similar sister species within the same genus (e.g. *Papilio paradoxa* vs *Papilio slateri*, *Halpe porus* vs *Halpe kusala*). | **Entomological Review**: Identify the single genuine species label; purge the incorrect one. |
| **Intergeneric Species Pairs (Different Genera)** | **43 clusters** (97 files) | Web search cross-pollution (e.g. multi-species biodiversity survey plates or generic Assam butterfly blog posts). | **Visual Verification**: Determine if one folder is correct or if image is generic stock. |

---

## 2. Multi-Species Mega-Clusters Detail

These clusters represent the highest noise concentration:
1. **`CSD-001` (11 species, 11 files)**: Hash `ec3757e316...` assigned to *Byasa crassipes*, *Euthalia telchinia*, *Pantoporia bieti*, *Athyma punctata*, *Pithecops fulgens*, *Simiskina phalena*, *Udara selma*, *Pyroneura margherita*, *Darpa pteria*, *Plastingia naga*, and *Scobura woolletti*. (MobileNet: `electric_guitar`).
2. **`CSD-002` (5 species, 5 files)**: Hash `9b83cd4326...` assigned to *Udara selma*, *Pantoporia assamica*, *Simiskina phalena*, *Elymnias peali*, and *Salanoemia sala*. (MobileNet: `envelope`).
3. **`CSD-003` (4 species, 4 files)**: Hash `2215c2ec0f...` assigned to *Byasa polla*, *Losaria doubledayi*, *Pantoporia assamica*, and *Chersonesia rahria*.
4. **`CSD-004` (3 species, 3 files)**: Hash `2e090123be...` assigned to *Athyma ranga*, *Athyma pravara*, and *Athyma punctata*.
5. **`CSD-005` (3 species, 3 files)**: Hash `5a1ba480ea...` assigned to *Tagiades gana gana*, *Cupitha purreea purreea*, and *Seseria sambara sambara*.

---

## 3. Human Review Workflow

1. Open [`cross_species_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/cross_species_contact_sheets.html) in a browser to visually inspect each duplicate cluster.
2. Fill out decisions in [`cross_species_review_template.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase2/cross_species_review_template.csv):
   - Column `decision_action`: `PURGE_ALL`, `REASSIGN`, or `EXPERT_REVIEW`.
   - Column `verified_correct_species`: Enter the correct scientific name if one is valid.
   - Column `reviewer_notes`: Provide rationale for the determination.
