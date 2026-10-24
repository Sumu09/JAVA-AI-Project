#!/usr/bin/env python3
"""
Unified Dataset Extractor & Structurer for Butterfly and Moth Species Classifier
================================================================================
This script automates adding new species to your dataset:
  1. Pulls candidate images (minimum 30 clean, non-corrupted images).
  2. Validates image integrity and filters broken/corrupt files.
  3. Assigns the next sequential class index (e.g. 081_...).
  4. Automatically splits into 80% train and 20% test sets.
  5. Formats internal image filenames sequentially (e.g. 0810001.jpg, 0810002.jpg).
  6. Synchronizes model/labels.txt, updates Java species metadata, and recompiles.
  7. Prepares everything so you only need to run ./train.sh to train the new model!
"""

import os
import sys
import time
import random
import shutil
import urllib.request
from pathlib import Path
from PIL import Image

# Import DDGS from ddgs (or duckduckgo_search fallback)
try:
    from ddgs import DDGS
except ImportError:
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        print("Error: ddgs library not installed. Run: .venv/bin/python -m pip install ddgs")
        sys.exit(1)

# ==============================================================================
# 1. USER CONFIGURATION
# Add any new butterfly or moth species to this list!
# ==============================================================================
TARGET_SPECIES = [
    "Euthalia zubeengargi",
    "Badamia exclamationis",
    "Hasora badra badra",
    "Choaspes benjaminii japonica",
    "Burara jaina",
    "Sarangesa dasahara dasahara",
    "Celaenorrhinus leucocera",
    "Celaenorrhinus aurivittata aurivittata",
    "Pseudocoladenia dan fabia",
    "Tagiades dynamicus ravi",
    "Tagiades litigiosa litigiosa",
    "Tagiades gana gana",
    "Gerosis phisara phisara",
    "Mooreana trichoneura pralaya",
    "Seseria sambara sambara",
    "Odontoptilum angulata angulata",
    "Psolos fuligo subfasciatus",
    "Ochus subvittatus subradiatus",
    "Ampittia dioscorides",
    "Aeromachus pygmaeus",
    "Pithauria stramineipennis",
    "Thoressa cerata",
    "Halpe zema zema",
    "Halpe aucma",
    "Halpe porus porus",
    "Halpe kusala",
    "Sebastonyma dolopia",
    "Cupitha purreea purreea",
    "Potanthus pseudomaesa",
    "Telicota colon",
    "Telicota bambusae bambusae",
    "Oriens gola pseudolus",
    "Notocrypta paralysos asawa",
    "Notocrypta curvifascia curvifascia",
    "Ancema ctesia ctesia",
    "Remelana jangala ravata",
    "Ancema blanka minturna",
    "Surendra quercetorum quercetorum",
    "Yasuda tripunctata tripunctata",
    "Loxura atymnus continentalis",
    "Spindasis lohita himalayanus",
    "Heliophorus epicles latilimbata",
    "Catochrysops strabo strabo",
    "Anthene emolus emolus",
    "Anthene lycaenina lycambes",
    "Prosotas aluta coelestis",
    "Chilades lajus lajus",
    "Caleta elna noliteia",
    "Castalius rosimon rosimon",
    "Jamides celeno",
    "Jamides caerulea",
    "Jamides elpis pseudelpis",
    "Prosotas nora ardates",
    "Prosotas dubiosa indica",
    "Prosotas bhutea",
    "Nacaduba kurava euplea",
    "Megisba malaya sikkima",
    "Neopithecops zalmora zalmora",
    "Charaxes bernardus hierax",
    "Charaxes marmax marmax",
    "Elymnias hypermnestra undularis",
    "Elymnias nesaea",
    "Ethope himachala",
    "Lethe chandica flanona",
    "Lethe vindhya vindhya",
    "Lethe mekara mekara",
    "Lethe satyavati"
    "Euthalia zubeengargi"
]

# Minimum valid images required per species for robust training
MIN_IMAGES_REQUIRED = 30

# Dataset train/test split ratio (80% train, 20% test)
TRAIN_RATIO = 0.80

PROJECT_ROOT = Path(__file__).resolve().parent
if PROJECT_ROOT.name == "scripts":
    PROJECT_ROOT = PROJECT_ROOT.parent
DATASET_DIR = PROJECT_ROOT / "dataset"
TRAIN_DIR = DATASET_DIR / "train"
TEST_DIR = DATASET_DIR / "test"
TEMP_DIR = DATASET_DIR / "_temp_downloads"
LABELS_FILE = PROJECT_ROOT / "model" / "labels.txt"


def get_existing_classes():
    """Scans dataset/train and returns a dictionary of existing class info."""
    TRAIN_DIR.mkdir(parents=True, exist_ok=True)
    TEST_DIR.mkdir(parents=True, exist_ok=True)

    classes = {}
    max_idx = 0

    for d in sorted(TRAIN_DIR.iterdir()):
        if d.is_dir() and not d.name.startswith("."):
            parts = d.name.split("_", 1)
            if len(parts) == 2 and parts[0].isdigit():
                idx = int(parts[0])
                clean_name = parts[1].replace("_", " ").lower()
                classes[clean_name] = {
                    "id": parts[0],
                    "idx": idx,
                    "folder_name": d.name,
                    "train_path": d,
                    "test_path": TEST_DIR / d.name
                }
                if idx > max_idx:
                    max_idx = idx

    return classes, max_idx


def count_valid_images(folder_path):
    """Counts non-corrupt, valid images in a folder."""
    if not folder_path or not folder_path.exists():
        return 0
    count = 0
    for f in folder_path.iterdir():
        if f.is_file() and not f.name.startswith(".") and f.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            try:
                with Image.open(f) as img:
                    img.verify()
                count += 1
            except Exception:
                pass
    return count


def fetch_image_urls(species_name, target_count=50):
    """Searches DuckDuckGo across multiple query variations to collect unique image URLs."""
    queries = [
        f"{species_name} butterfly",
        f"{species_name} insect",
        f"{species_name} species",
        f"{species_name} moth",
        f"{species_name} dorsal ventral",
        f"{species_name}",
    ]

    collected_urls = set()
    print(f"  Searching image sources for '{species_name}'...")

    for q in queries:
        if len(collected_urls) >= target_count:
            break
        try:
            with DDGS() as ddgs:
                results = ddgs.images(q, max_results=35)
                for r in results:
                    url = r.get("image")
                    if url and url.startswith("http") and not url.lower().endswith((".svg", ".gif")):
                        collected_urls.add(url)
            # Short sleep between queries to prevent rate-limiting
            time.sleep(random.uniform(1.2, 2.0))
        except Exception as e:
            print(f"    Notice: Search query '{q}' encounter ({e}). Continuing...")
            time.sleep(2.0)

    print(f"  Found {len(collected_urls)} candidate image URLs.")
    return list(collected_urls)


def download_and_validate_images(species_name, urls, output_temp_dir, min_required=30):
    """Downloads candidate images and filters out corrupted or invalid files."""
    output_temp_dir.mkdir(parents=True, exist_ok=True)
    valid_files = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"  Downloading and validating candidate images...")
    counter = 1

    for url in urls:
        raw_path = output_temp_dir / f"cand_{counter:04d}.tmp"
        clean_path = output_temp_dir / f"valid_{counter:04d}.jpg"
        counter += 1

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read()

            if len(content) < 4000:  # Skip tiny placeholder images (< 4KB)
                continue

            with open(raw_path, "wb") as f:
                f.write(content)

            # Validate with PIL
            with Image.open(raw_path) as img:
                img.verify()

            # Re-open, check dimensions and convert to RGB JPEG
            with Image.open(raw_path) as img:
                w, h = img.size
                if w < 100 or h < 100:
                    raw_path.unlink(missing_ok=True)
                    continue
                rgb_img = img.convert("RGB")
                rgb_img.save(clean_path, "JPEG", quality=95)

            raw_path.unlink(missing_ok=True)
            valid_files.append(clean_path)

            if len(valid_files) >= min_required + 10:
                break

        except Exception:
            raw_path.unlink(missing_ok=True)
            continue

    print(f"  Successfully verified {len(valid_files)} clean images.")
    return valid_files


def structure_species_dataset(clean_files, class_id, class_name, train_dest, test_dest):
    """Splits images into train/test and renames them to standard class format."""
    train_dest.mkdir(parents=True, exist_ok=True)
    test_dest.mkdir(parents=True, exist_ok=True)

    random.seed(42)
    random.shuffle(clean_files)

    total = len(clean_files)
    test_count = max(5, round(total * (1.0 - TRAIN_RATIO))) if total >= 25 else max(1, round(total * 0.20))
    train_count = total - test_count

    train_files = clean_files[:train_count]
    test_files = clean_files[train_count:]

    # Copy & rename train files: 0810001.jpg, 0810002.jpg ...
    seq = 1
    for f in train_files:
        dest_filename = f"{class_id}{seq:04d}.jpg"
        shutil.copy2(f, train_dest / dest_filename)
        seq += 1

    # Copy & rename test files: 0810027.jpg ...
    for f in test_files:
        dest_filename = f"{class_id}{seq:04d}.jpg"
        shutil.copy2(f, test_dest / dest_filename)
        seq += 1

    return len(train_files), len(test_files)


def update_labels_file():
    """Generates model/labels.txt sorted by numeric class prefix."""
    classes = []
    for d in sorted(TRAIN_DIR.iterdir()):
        if d.is_dir() and not d.name.startswith("."):
            classes.append(d.name)

    LABELS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LABELS_FILE, "w", encoding="utf-8") as f:
        for c in classes:
            f.write(f"{c}\n")

    print(f"\n[✓] Updated '{LABELS_FILE}' with {len(classes)} classes.")
    return len(classes)


def update_java_and_recompile():
    """Runs generate_java_species.py and compiles Java application."""
    gen_script = PROJECT_ROOT / "generate_java_species.py"
    if gen_script.exists():
        print("[✓] Regenerating Java Species and metadata...")
        python_exec = sys.executable
        os.system(f'"{python_exec}" "{gen_script}"')

    build_script = PROJECT_ROOT / "build.sh"
    if build_script.exists() and os.name != "nt":
        print("[✓] Compiling Java application...")
        os.system(f'bash "{build_script}" >/dev/null 2>&1')


def main():
    print("=" * 70)
    print("  Butterfly & Moth Species Dataset Extraction & Structuring Engine")
    print("=" * 70)

    existing_classes, max_idx = get_existing_classes()
    print(f"Current highest class prefix in dataset: {max_idx:03d}")
    print(f"Total existing classes in train: {len(existing_classes)}")

    processed_summary = []

    for species in TARGET_SPECIES:
        norm_name = species.strip().replace("_", " ").lower()
        formatted_name = species.strip().replace(" ", "_")

        print(f"\nProcessing species: '{species}'...")

        if norm_name in existing_classes:
            info = existing_classes[norm_name]
            cid = info["id"]
            tr_count = count_valid_images(info["train_path"])
            te_count = count_valid_images(info["test_path"])
            total_count = tr_count + te_count

            if total_count >= MIN_IMAGES_REQUIRED:
                print(f"  [✓] Species '{species}' already exists as '{info['folder_name']}'.")
                print(f"      Valid images: {total_count} (Train: {tr_count}, Test: {te_count}). Skipping download.")
                processed_summary.append((info["folder_name"], tr_count, te_count, "Already Present"))
                continue
            else:
                print(f"  Notice: '{species}' exists with only {total_count} images (< {MIN_IMAGES_REQUIRED}).")
                print(f"          Augmenting images for class {cid}...")
                class_id = cid
                folder_name = info["folder_name"]
        else:
            max_idx += 1
            class_id = f"{max_idx:03d}"
            folder_name = f"{class_id}_{formatted_name}"

        train_dest = TRAIN_DIR / folder_name
        test_dest = TEST_DIR / folder_name
        temp_download_dest = TEMP_DIR / folder_name

        # 1. Fetch URLs
        urls = fetch_image_urls(species, target_count=50)

        # 2. Download and validate
        valid_files = download_and_validate_images(
            species_name=species,
            urls=urls,
            output_temp_dir=temp_download_dest,
            min_required=MIN_IMAGES_REQUIRED
        )

        if len(valid_files) < MIN_IMAGES_REQUIRED:
            print(f"  Warning: Only {len(valid_files)} valid images found for '{species}'. Trying fallback queries...")
            more_urls = fetch_image_urls(f"{species} high resolution", target_count=35)
            more_valid = download_and_validate_images(
                species_name=species,
                urls=more_urls,
                output_temp_dir=temp_download_dest,
                min_required=MIN_IMAGES_REQUIRED - len(valid_files)
            )
            valid_files.extend(more_valid)

        # 3. Structure into train / test
        tr, te = structure_species_dataset(
            clean_files=valid_files,
            class_id=class_id,
            class_name=folder_name,
            train_dest=train_dest,
            test_dest=test_dest
        )

        # Clean up temp files
        shutil.rmtree(temp_download_dest, ignore_errors=True)

        processed_summary.append((folder_name, tr, te, "Newly Added"))
        print(f"  [✓] Successfully structured: {folder_name} (Train: {tr}, Test: {te})")

    # Clean up top-level temp dir
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR, ignore_errors=True)

    # 4. Synchronize labels and Java files
    total_classes = update_labels_file()
    update_java_and_recompile()

    # 5. Display Summary
    print("\n" + "=" * 70)
    print("  Dataset Extraction & Structuring Summary")
    print("=" * 70)
    print(f"{'Folder / Class':<45} | {'Train':<6} | {'Test':<6} | {'Status'}")
    print("-" * 70)
    for folder, tr, te, status in processed_summary:
        print(f"{folder:<45} | {tr:<6} | {te:<6} | {status}")
    print("-" * 70)
    print(f"Total Species Classes in Project: {total_classes}")
    print("=" * 70)
    print("\nNEXT STEP: Train your AI model on the updated dataset by running:")
    print("  ./train.sh\n")


if __name__ == "__main__":
    main()
