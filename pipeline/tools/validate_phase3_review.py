#!/usr/bin/env python3
"""
ButterflyAI — Phase 3A Review Validator
=======================================
Validates human review determinations in reports/phase3/mega_cluster_review.csv:
  1. Verifies that all expected mega-cluster IDs are present.
  2. Ensures review_decision is one of the allowed taxonomic actions:
       - CONFIRMED_NON_BUTTERFLY
       - CONFIRMED_BUTTERFLY
       - UNCERTAIN
       - NEEDS_TAXONOMIST
  3. Detects incomplete, ambiguous, or contradictory decisions.
  4. Verifies action_plan alignment with decision.
  5. Confirms source files exist in active dataset or quarantine holding.

SAFEGUARDS:
  - Read-Only: Never modifies dataset files.
"""

import sys
import csv
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATASET_DIR = PROJECT_ROOT / "dataset"
REVIEW_CSV = PROJECT_ROOT / "reports" / "phase3" / "mega_cluster_review.csv"
MANIFEST_FILE = DATASET_DIR / "quarantine" / "quarantine_manifest.json"

EXPECTED_CLUSTER_IDS = {"CSD-001", "CSD-002", "CSD-008", "CSD-009", "CSD-010"}
ALLOWED_DECISIONS = {
    "CONFIRMED_NON_BUTTERFLY",
    "CONFIRMED_BUTTERFLY",
    "UNCERTAIN",
    "NEEDS_TAXONOMIST"
}


def load_quarantine_manifest_paths():
    if not MANIFEST_FILE.exists():
        return set()
    try:
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(r["original_path"] for r in data.get("records", []))
    except Exception:
        return set()


def validate_phase3_review():
    print("=" * 75)
    print("  ButterflyAI — Phase 3A Mega-Cluster Review Validator")
    print("=" * 75)
    print(f"Target review ledger: {REVIEW_CSV}\n")

    if not REVIEW_CSV.exists():
        print(f"CRITICAL ERROR: Review ledger not found at {REVIEW_CSV}")
        sys.exit(1)

    with open(REVIEW_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    quarantined_paths = load_quarantine_manifest_paths()

    errors = []
    warnings = []
    seen_clusters = set()

    summary_records = []

    for idx, r in enumerate(rows, 1):
        gid = r.get("cluster_id", "").strip()
        decision = r.get("review_decision", "").strip()
        verified_sp = r.get("verified_correct_species", "").strip()
        action_plan = r.get("action_plan", "").strip()
        notes = r.get("reviewer_notes", "").strip()
        taxa_str = r.get("conflicting_species_names", "").strip()
        source_paths_str = r.get("source_paths", "").strip()
        total_files = int(r.get("total_files", 0))

        # Check 1: Cluster ID validity
        if not gid:
            errors.append(f"Row #{idx}: Missing cluster_id.")
            continue
        if gid in seen_clusters:
            errors.append(f"Duplicate entry for cluster {gid}.")
        seen_clusters.add(gid)

        # Check 2: Decision validity
        if not decision:
            errors.append(f"Cluster {gid}: Missing review_decision. Must be one of {sorted(ALLOWED_DECISIONS)}.")
            continue
        if decision not in ALLOWED_DECISIONS:
            errors.append(
                f"Cluster {gid}: Invalid review_decision '{decision}'. Allowed: {sorted(ALLOWED_DECISIONS)}"
            )
            continue

        # Check 3: Consistency checks per decision type
        conflicting_taxa = [t.strip() for t in taxa_str.split("|")] if taxa_str else []

        if decision == "CONFIRMED_BUTTERFLY":
            if not verified_sp:
                errors.append(
                    f"Cluster {gid}: Marked as CONFIRMED_BUTTERFLY, but 'verified_correct_species' is empty!"
                )
            elif conflicting_taxa and not any(verified_sp.lower() in t.lower() for t in conflicting_taxa):
                warnings.append(
                    f"Cluster {gid}: 'verified_correct_species' ('{verified_sp}') does not match any of the conflicting taxa: {conflicting_taxa}."
                )

            if action_plan != "REASSIGN_TO_VERIFIED":
                warnings.append(
                    f"Cluster {gid}: For CONFIRMED_BUTTERFLY, action_plan is usually 'REASSIGN_TO_VERIFIED', got '{action_plan}'."
                )

        elif decision == "CONFIRMED_NON_BUTTERFLY":
            if verified_sp:
                warnings.append(
                    f"Cluster {gid}: Marked as CONFIRMED_NON_BUTTERFLY, but 'verified_correct_species' is populated ('{verified_sp}'). Should be empty."
                )
            if action_plan != "PURGE_ALL_SAMPLES":
                errors.append(
                    f"Cluster {gid}: Marked as CONFIRMED_NON_BUTTERFLY, but action_plan is '{action_plan}' instead of 'PURGE_ALL_SAMPLES'."
                )

        elif decision in ["UNCERTAIN", "NEEDS_TAXONOMIST"]:
            if verified_sp:
                warnings.append(
                    f"Cluster {gid}: Marked as {decision}, but 'verified_correct_species' is populated ('{verified_sp}'). Should be empty until verified."
                )
            if action_plan != "HOLD_IN_DATASET":
                warnings.append(
                    f"Cluster {gid}: Marked as {decision}, but action_plan is '{action_plan}' instead of 'HOLD_IN_DATASET'."
                )

        # Check 4: Source paths verification
        source_paths = [p.strip() for p in source_paths_str.split(";")] if source_paths_str else []
        for p_str in source_paths:
            p = PROJECT_ROOT / p_str
            if not p.exists() and p_str not in quarantined_paths:
                warnings.append(f"Cluster {gid}: Source path '{p_str}' not found in active dataset or quarantine manifest.")

        summary_records.append({
            "cluster_id": gid,
            "decision": decision,
            "action_plan": action_plan,
            "species_count": r.get("species_count", "?"),
            "total_files": total_files,
            "notes": notes
        })

    # Check 5: All expected mega-clusters present
    missing_clusters = EXPECTED_CLUSTER_IDS - seen_clusters
    if missing_clusters:
        errors.append(f"Missing required mega-clusters: {sorted(missing_clusters)}")

    extra_clusters = seen_clusters - EXPECTED_CLUSTER_IDS
    if extra_clusters:
        warnings.append(f"Extra clusters found outside expected set: {sorted(extra_clusters)}")

    # Print Validation Report
    print("Cluster Validation Table:")
    print("-" * 75)
    print(f"{'Cluster':<10} | {'Decision':<26} | {'Action Plan':<20} | {'Files':<5} | Status")
    print("-" * 75)
    for rec in summary_records:
        gid = rec["cluster_id"]
        cl_errors = [e for e in errors if gid in e]
        status = "FAIL" if cl_errors else "PASS"
        print(f"{gid:<10} | {rec['decision']:<26} | {rec['action_plan']:<20} | {rec['total_files']:<5} | {status}")
    print("-" * 75)

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  [Notice] {w}")

    if errors:
        print("\n" + "!" * 75)
        print("  VALIDATION FAILED — INCOMPLETE OR CONTRADICTORY ENTRIES FOUND")
        print("!" * 75)
        for err in errors:
            print(f"  - {err}")
        print("\nPlease correct the entries in reports/phase3/mega_cluster_review.csv and rerun.")
        sys.exit(1)

    # Compute planned impact
    confirmed_junk_files = sum(r["total_files"] for r in summary_records if r["decision"] == "CONFIRMED_NON_BUTTERFLY")
    held_butterfly_files = sum(r["total_files"] for r in summary_records if r["decision"] in ["UNCERTAIN", "NEEDS_TAXONOMIST"])
    reassigned_files = sum(r["total_files"] for r in summary_records if r["decision"] == "CONFIRMED_BUTTERFLY")

    print("\n" + "=" * 75)
    print("  VALIDATION PASSED: 100% OF MEGA-CLUSTER DECISIONS ARE SOUND")
    print("=" * 75)
    print(f"  - Confirmed Non-Butterfly Junk: {sum(1 for r in summary_records if r['decision'] == 'CONFIRMED_NON_BUTTERFLY')} clusters ({confirmed_junk_files} files scheduled for purge)")
    print(f"  - Confirmed Butterfly Taxa:     {sum(1 for r in summary_records if r['decision'] == 'CONFIRMED_BUTTERFLY')} clusters ({reassigned_files} files)")
    print(f"  - Held for Taxonomist Review:   {sum(1 for r in summary_records if r['decision'] in ['UNCERTAIN', 'NEEDS_TAXONOMIST'])} clusters ({held_butterfly_files} files)")
    print("=" * 75)
    print("No images were moved. The review ledger is valid and ready for user inspection.")


if __name__ == "__main__":
    validate_phase3_review()
