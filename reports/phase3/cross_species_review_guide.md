# ButterflyAI — Phase 3C Human Review Guide
**Scope**: 55 Pairwise Cross-Species Duplicate Clusters (`CSD-003` to `CSD-007`, `CSD-011` to `CSD-060`)  
**Target Ledger**: [`cross_species_review.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/cross_species_review.csv)  
**Interactive Sheet**: [`cross_species_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/cross_species_contact_sheets.html)  
**Validator Script**: `pipeline/tools/validate_phase3c_review.py`

---

## 1. Review Objectives

In Phase 3C, we examine all 55 pairwise cross-species clusters where an identical image hash was found across two different species folders.

### The Four Review Determinations:

1. **`CONFIRMED_NON_BUTTERFLY`**
   - **When to use**: The image is clearly not a butterfly (e.g., website graphic, anatomy diagram, document scan, unrelated animal, or tool).
   - **Required fields**:
     * `review_decision`: `CONFIRMED_NON_BUTTERFLY`
     * `verified_correct_species`: *(Must be empty)*
     * `action_plan`: `PURGE_ALL_SAMPLES`
   - **Resulting action**: In Phase 3D, all copies of this hash across all folders will be safely moved to quarantine.

2. **`CONFIRMED_BUTTERFLY`**
   - **When to use**: The image is a genuine butterfly specimen, and the reviewer can confidently assign it to the correct species among the conflicting folders.
   - **Required fields**:
     * `review_decision`: `CONFIRMED_BUTTERFLY`
     * `verified_correct_species`: Exact scientific name or Class ID of the true species (must match one of the conflicting taxa).
     * `action_plan`: `REASSIGN_TO_VERIFIED`
   - **Resulting action**: In Phase 3D, the copy in the verified species folder is retained, and erroneous copies in the conflicting species folders will be quarantined.

3. **`UNCERTAIN`**
   - **When to use**: The image is a butterfly specimen or biological insect, but morphological ambiguity prevents a definitive assignment between the sister species without high-magnification genitalia or molecular data.
   - **Required fields**:
     * `review_decision`: `UNCERTAIN`
     * `verified_correct_species`: *(Must be empty)*
     * `action_plan`: `HOLD_IN_DATASET`
   - **Resulting action**: No images are moved. Both copies are preserved in active training splits to avoid premature loss of training samples.

4. **`NEEDS_TAXONOMIST`**
   - **When to use**: Complex cryptic species pairs requiring consultation with a Lepidopterist.
   - **Required fields**:
     * `review_decision`: `NEEDS_TAXONOMIST`
     * `verified_correct_species`: *(Must be empty)*
     * `action_plan`: `HOLD_IN_DATASET`
   - **Resulting action**: Retained in active dataset and logged for expert consultation.

---

## 2. Recommended Workflow

1. Open [`cross_species_contact_sheets.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/cross_species_contact_sheets.html) in your browser.
2. Review the **Priority A: Historic Split Leakage** clusters (18 clusters).
3. Review the **Priority B: Suspected Non-Butterfly** clusters (7 clusters).
4. Review the remaining congeneric and intergeneric clusters.
5. Record your decisions in [`cross_species_review.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/cross_species_review.csv).
6. Run the validator:
   ```bash
   .venv/bin/python pipeline/tools/validate_phase3c_review.py
   ```
7. Once validation passes with zero errors, present your final decisions for quarantine planning.
