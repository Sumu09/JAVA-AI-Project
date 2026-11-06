# Mega-Cluster Review Guide (Phase 3A)

This guide provides instructions for conducting human-in-the-loop biological review of the **5 cross-species mega-clusters** identified in the ButterflyAI dataset.

---

## 1. Files & Tooling

| Artifact | Path | Purpose |
| :--- | :--- | :--- |
| **Interactive Contact Sheet** | [`reports/phase3/mega_cluster_contact_sheet.html`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_contact_sheet.html) | Self-contained visual sheet with embedded high-res images and conflicting taxa. |
| **Review Decision Ledger** | [`reports/phase3/mega_cluster_review.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_review.csv) | The authoritative CSV where human determinations are recorded. |
| **Cluster Review Report** | [`reports/phase3/mega_cluster_review.md`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_review.md) | Detailed forensic background and path breakdown. |
| **Decision Validator** | [`pipeline/tools/validate_phase3_review.py`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/pipeline/tools/validate_phase3_review.py) | Automated script to validate reviewer decisions before execution. |

---

## 2. Review Decision Rules

For each of the 5 clusters, the `review_decision` field in [`mega_cluster_review.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_review.csv) must be set to exactly one of the following 4 values:

1. **`CONFIRMED_NON_BUTTERFLY`**:
   - **Criteria**: The image is unambiguous web crawler noise (e.g. electric guitar, postal envelope, website header, medical diagram, unrelated animal).
   - **Action Plan**: Automatically set to `PURGE_ALL_SAMPLES`.
   - **Verified Species**: Leave empty.

2. **`CONFIRMED_BUTTERFLY`**:
   - **Criteria**: The image is a genuine butterfly and you have verified the single correct species among the conflicting options.
   - **Action Plan**: Automatically set to `REASSIGN_TO_VERIFIED`.
   - **Verified Species**: Must be set to the exact scientific name (e.g. `Graphium agetes`).

3. **`UNCERTAIN`**:
   - **Criteria**: The image is a genuine butterfly, but visual ambiguity prevents assigning it to one species without dissection or expert specimen comparison.
   - **Action Plan**: Automatically set to `HOLD_IN_DATASET`.
   - **Verified Species**: Leave empty.

4. **`NEEDS_TAXONOMIST`**:
   - **Criteria**: The image requires consultation with an entomologist or specimen voucher specialist.
   - **Action Plan**: Automatically set to `HOLD_IN_DATASET`.
   - **Verified Species**: Leave empty.

---

## 3. Step-by-Step Instructions

1. **Open the visual contact sheet**:
   ```bash
   open reports/phase3/mega_cluster_contact_sheet.html
   ```
   Or double-click the file in Finder to view it in Safari / Chrome.

2. **Edit the decision ledger**:
   Open [`reports/phase3/mega_cluster_review.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/phase3/mega_cluster_review.csv) in VS Code or any text editor.
   Review each cluster row and adjust `review_decision` or `reviewer_notes` if needed.

3. **Validate decisions**:
   Run the validator script:
   ```bash
   .venv/bin/python pipeline/tools/validate_phase3_review.py
   ```
   The validator will verify that:
   - All 5 cluster IDs are present.
   - Every decision is one of the 4 allowed values.
   - No contradictory fields exist (e.g. `CONFIRMED_BUTTERFLY` without specifying the species).

4. **Approval**:
   Once validated, you can approve Phase 3B (quarantine execution of confirmed junk). Zero files are moved until you approve.
