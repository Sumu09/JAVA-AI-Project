#!/usr/bin/env python3
"""
Butterfly Species Image Downloader & Dataset Balancer
=====================================================
Fetches high-quality, research-grade, verified butterfly species observations
from the open iNaturalist and Wikimedia APIs to augment under-represented classes
in the dataset.

Features:
- Auto-detects under-represented classes in dataset/train and dataset/test
- Queries verified research-grade photos (no API key required)
- Validates image integrity using PIL to prevent corrupt or non-image files
- Maintains the standard 7-digit zero-padded naming convention (e.g., 0420005.jpg)
- Automatically balances newly downloaded images between train (80%) and test (20%)
- Includes --dry-run, --summary, --min-images, and --species selection flags
"""

import os
import sys
import time
import json
import argparse
import urllib.request
import urllib.parse
from io import BytesIO
from PIL import Image

USER_AGENT = "ButterflyClassifier-DatasetBuilder/1.0 (Educational Image Processing Project)"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRAIN_DIR = os.path.join(BASE_DIR, "dataset", "train")
TEST_DIR = os.path.join(BASE_DIR, "dataset", "test")

# Fallback mapping of class ID to scientific names
TAXONOMY_MAP = {
    "001": ("Danaus plexippus", "Monarch"),
    "002": ("Heliconius charitonius", "Zebra Longwing"),
    "003": ("Heliconius erato", "Red Passion"),
    "004": ("Junonia coenia", "Common Buckeye"),
    "005": ("Lycaena phlaeas", "Small Copper"),
    "006": ("Nymphalis antiopa", "Mourning Cloak"),
    "007": ("Papilio cresphontes", "Giant Swallowtail"),
    "008": ("Pieris rapae", "Cabbage White"),
    "009": ("Vanessa atalanta", "Red Admiral"),
    "010": ("Vanessa cardui", "Painted Lady"),
    "011": ("Aeromachus pygmaeus", "Pygmy Scrub Hopper"),
    "012": ("Ampittia dioscorides", "Bush Hopper"),
    "013": ("Ancema blanka minturna", "Minturn Silverstreak"),
    "014": ("Ancema ctesia ctesia", "Bi-spot Royal"),
    "015": ("Anthene emolus emolus", "Ciliate Blue"),
    "016": ("Anthene lycaenina lycambes", "Pointed Ciliate Blue"),
    "017": ("Athyma perius", "Common Sergeant"),
    "018": ("Badamia exclamationis", "Brown Awl"),
    "019": ("Burara jaina", "Orange Awlet"),
    "020": ("Caleta elna noliteia", "Elbowed Pierrot"),
    "021": ("Catochrysops strabo strabo", "Forget-me-not"),
    "022": ("Celaenorrhinus aurivittata aurivittata", "Yellow-banded Flat"),
    "023": ("Celaenorrhinus leucocera", "Common Spotted Flat"),
    "024": ("Cethosia cyane", "Leopard Lacewing"),
    "025": ("Charaxes bernardus hierax", "Tawny Rajah"),
    "026": ("Charaxes marmax marmax", "Yellow Rajah"),
    "027": ("Chilades lajus lajus", "Lime Blue"),
    "028": ("Choaspes benjaminii japonica", "Indian Awlking"),
    "029": ("Cupitha purreea purreea", "Wax Dart"),
    "030": ("Elymnias hypermnestra undularis", "Common Palmfly"),
    "031": ("Elymnias nesaea", "Tiger Palmfly"),
    "032": ("Ethope himachala", "Dusky Diadem"),
    "033": ("Gerosis phisara phisara", "Great Yellow Sailer"),
    "034": ("Graphium agamemnon", "Tailed Jay"),
    "035": ("Halpe aucma", "Gold-spotted Ace"),
    "036": ("Halpe kusala", "Plain Ace"),
    "037": ("Halpe porus porus", "Moore's Ace"),
    "038": ("Halpe zema zema", "Zema Ace"),
    "039": ("Hasora badra", "Common Awl"),
    "040": ("Heliophorus epicles latilimbata", "Purple Sapphire"),
    "041": ("Jamides caerulea", "Sky Blue"),
    "042": ("Jamides celeno", "Common Cerulean"),
    "043": ("Jamides elpis pseudelpis", "Glistening Cerulean"),
    "044": ("Lethe chandica flanona", "Angled Red Forester"),
    "045": ("Lethe mekara mekara", "Common Treebrown"),
    "046": ("Lethe satyavati", "Pallid Forester"),
    "047": ("Lethe vindhya vindhya", "Black Forester"),
    "048": ("Loxura atymnus continentalis", "Yamfly"),
    "049": ("Megisba malaya sikkima", "Malayan"),
    "050": ("Mooreana trichoneura pralaya", "Yellow Flat"),
    "051": ("Nacaduba kurava euplea", "Transparent 6-Line Blue"),
    "052": ("Neopithecops zalmora zalmora", "Common Quaker"),
    "053": ("Notocrypta curvifascia curvifascia", "Common Banded Demon"),
    "054": ("Notocrypta paralysos asawa", "Grass Demon"),
    "055": ("Ochus subvittatus subradiatus", "Tiger Hopper"),
    "056": ("Odontoptilum angulata angulata", "Chestnut Angle"),
    "057": ("Oriens gola pseudolus", "Common Dartlet"),
    "058": ("Papilio paris", "Paris Peacock"),
    "059": ("Pithauria stramineipennis", "Light Straw Ace"),
    "060": ("Potanthus pseudomaesa", "Indian Dart"),
    "061": ("Prosotas aluta coelestis", "Banded Lineblue"),
    "062": ("Prosotas bhutea", "Bhutya Lineblue"),
    "063": ("Prosotas dubiosa indica", "Tailless Lineblue"),
    "064": ("Prosotas nora ardates", "Common Lineblue"),
    "065": ("Pseudocoladenia dan fabia", "Fulvous Pied Flat"),
    "066": ("Psolos fuligo subfasciatus", "Coon"),
    "067": ("Remelana jangala ravata", "Chocolate Royal"),
    "068": ("Sarangesa dasahara dasahara", "Common Small Flat"),
    "069": ("Sebastonyma dolopia", "Tufted Ace"),
    "070": ("Seseria sambara sambara", "Notched Flat"),
    "071": ("Spindasis lohita himalayanus", "Long-banded Silverline"),
    "072": ("Surendra quercetorum quercetorum", "Common Acacia Blue"),
    "073": ("Tagiades dynamicus ravi", "Ravi Snow Flat"),
    "074": ("Tagiades gana gana", "Suffused Snow Flat"),
    "075": ("Tagiades litigiosa litigiosa", "Water Snow Flat"),
    "076": ("Telicota bambusae bambusae", "Dark Palm Dart"),
    "077": ("Telicota colon", "Pale Palm Dart"),
    "078": ("Thoressa cerata", "Northern Spangle"),
    "079": ("Troides aeacus", "Golden Birdwing"),
    "080": ("Yasuda tripunctata tripunctata", "Three-spot Silverstreak"),
}


def make_request(url: str, timeout: int = 15) -> bytes:
    """Performs HTTP GET with polite User-Agent."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def get_existing_classes():
    """Scans dataset/train and returns dict of class_id -> folder name."""
    if not os.path.exists(TRAIN_DIR):
        print(f"Error: {TRAIN_DIR} not found.")
        sys.exit(1)

    classes = {}
    for d in sorted(os.listdir(TRAIN_DIR)):
        full = os.path.join(TRAIN_DIR, d)
        if os.path.isdir(full):
            cid = d.split("_")[0]
            classes[cid] = d
    return classes


def get_class_image_counts(class_folder: str):
    """Counts valid images in train and test for a class folder."""
    train_path = os.path.join(TRAIN_DIR, class_folder)
    test_path = os.path.join(TEST_DIR, class_folder)

    train_files = [f for f in os.listdir(train_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))] if os.path.exists(train_path) else []
    test_files = [f for f in os.listdir(test_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))] if os.path.exists(test_path) else []

    return len(train_files), len(test_files), train_files, test_files


def get_max_image_index(class_id: str, all_files: list) -> int:
    """Finds highest index among existing files (e.g., 0420005.jpg -> 5)."""
    max_idx = 0
    prefix = f"{int(class_id):03d}"
    for fn in all_files:
        name, _ = os.path.splitext(fn)
        if name.startswith(prefix) and len(name) == 7:
            try:
                idx = int(name[3:])
                if idx > max_idx:
                    max_idx = idx
            except ValueError:
                pass
    return max_idx


def fetch_inaturalist_photos(scientific_name: str, max_needed: int):
    """
    Queries iNaturalist for research-grade observations of a species.
    Returns list of high-quality image URLs.
    """
    photos = []
    queries = [scientific_name]

    # If trinomial (e.g. 'Loxura atymnus continentalis'), also add binomial fallback ('Loxura atymnus')
    words = scientific_name.split()
    if len(words) > 2:
        queries.append(f"{words[0]} {words[1]}")

    seen_ids = set()

    for q in queries:
        if len(photos) >= max_needed:
            break

        encoded = urllib.parse.quote_plus(q)
        per_page = min(100, max(10, max_needed * 2))
        url = (
            f"https://api.inaturalist.org/v1/observations?"
            f"taxon_name={encoded}&quality_grade=research&photos=true"
            f"&per_page={per_page}&order=desc&order_by=votes"
        )

        try:
            raw = make_request(url)
            data = json.loads(raw.decode("utf-8"))
            results = data.get("results", [])

            for obs in results:
                if len(photos) >= max_needed:
                    break
                obs_photos = obs.get("photos", [])
                for p in obs_photos:
                    pid = p.get("id")
                    if pid in seen_ids:
                        continue
                    seen_ids.add(pid)

                    purl = p.get("url")
                    if purl:
                        # Convert square thumbnail to high-res medium (500px) or original
                        img_url = purl.replace("square.", "medium.").replace("square/", "medium/")
                        photos.append(img_url)
                        if len(photos) >= max_needed:
                            break

            time.sleep(0.6)  # Polite API rate limit (<= 60 req/min)

        except Exception as e:
            print(f"    [iNaturalist query '{q}' warning: {e}]")

    return photos


def fetch_wikimedia_photos(scientific_name: str, max_needed: int):
    """Fallback query to Wikimedia Commons."""
    photos = []
    encoded = urllib.parse.quote_plus(scientific_name)
    url = (
        f"https://commons.wikimedia.org/w/api.php?action=query&generator=search"
        f"&gsrsearch={encoded}&gsrnamespace=6&prop=imageinfo&iiprop=url&format=json"
        f"&gsrlimit={min(20, max_needed * 2)}"
    )

    try:
        raw = make_request(url)
        data = json.loads(raw.decode("utf-8"))
        pages = data.get("query", {}).get("pages", {})
        for _, page in pages.items():
            info = page.get("imageinfo", [])
            if info:
                iurl = info[0].get("url")
                if iurl and iurl.lower().endswith(('.jpg', '.jpeg', '.png')):
                    photos.append(iurl)
                    if len(photos) >= max_needed:
                        break
        time.sleep(0.5)
    except Exception as e:
        print(f"    [Wikimedia query warning: {e}]")

    return photos


def download_and_verify_image(image_url: str, min_size: int = 160) -> Image.Image:
    """Downloads an image, validates with PIL, and returns RGB Image."""
    try:
        img_bytes = make_request(image_url, timeout=12)
        img = Image.open(BytesIO(img_bytes))
        img.verify()  # Check for corruption

        # Reopen after verify() (PIL requirement)
        img = Image.open(BytesIO(img_bytes)).convert("RGB")
        w, h = img.size
        if w < min_size or h < min_size:
            return None  # Too small or icon
        return img
    except Exception:
        return None


def show_summary(classes: dict):
    """Prints a clear report of all 80 species and their image counts."""
    print("=" * 80)
    print(f"{'ID':<5} {'Common Name':<28} {'Scientific Name':<30} {'Train':<6} {'Test':<6} {'Total':<6}")
    print("=" * 80)

    total_train = 0
    total_test = 0
    under_25 = []

    for cid, folder in sorted(classes.items()):
        tr, te, _, _ = get_class_image_counts(folder)
        total_train += tr
        total_test += te
        tot = tr + te
        sci, com = TAXONOMY_MAP.get(cid, (folder, "Unknown"))

        flag = " [LOW]" if tot < 20 else ""
        if tot < 20:
            under_25.append((cid, com, sci, tot))

        print(f"{cid:<5} {com[:26]:<28} {sci[:28]:<30} {tr:<6} {te:<6} {tot:<6}{flag}")

    print("=" * 80)
    print(f"TOTAL: 80 species | Train Images: {total_train} | Test Images: {total_test} | Total: {total_train + total_test}")
    print(f"Classes with < 20 total images: {len(under_25)}")
    print("=" * 80)


def balance_dataset(min_images: int, target_species: list = None, dry_run: bool = False, max_per_class: int = 40):
    """
    Downloads images for species falling below min_images threshold
    and distributes them 80/20 into train/test.
    """
    classes = get_existing_classes()

    to_process = []
    for cid, folder in sorted(classes.items()):
        if target_species and cid not in target_species:
            continue

        tr, te, tr_files, te_files = get_class_image_counts(folder)
        tot = tr + te

        if tot < min_images:
            needed = min_images - tot
            needed = min(needed, max_per_class)
            to_process.append((cid, folder, tr, te, tot, needed, tr_files + te_files))

    if not to_process:
        print(f"\nAll specified species currently meet or exceed the target of {min_images} images.")
        return

    print(f"\nFound {len(to_process)} species below threshold of {min_images} images:")
    for cid, folder, tr, te, tot, needed, _ in to_process:
        sci, com = TAXONOMY_MAP.get(cid, (folder, "Unknown"))
        print(f"  [{cid}] {com} ({sci}): current={tot} (train={tr}, test={te}) -> will fetch +{needed}")

    if dry_run:
        print("\n[Dry Run Mode] No files were downloaded or modified.")
        return

    print("\nStarting downloads...")
    total_added_train = 0
    total_added_test = 0

    for idx, (cid, folder, tr, te, tot, needed, all_files) in enumerate(to_process, 1):
        sci, com = TAXONOMY_MAP.get(cid, (folder, "Unknown"))
        print(f"\n({idx}/{len(to_process)}) [{cid}] {com} ({sci}) -> target: +{needed} images")

        # 1. Fetch URLs
        urls = fetch_inaturalist_photos(sci, needed)
        if len(urls) < needed:
            wiki_urls = fetch_wikimedia_photos(sci, needed - len(urls))
            urls.extend(wiki_urls)

        if not urls:
            print(f"    [Notice] No candidate photos found on iNaturalist or Wikimedia.")
            continue

        print(f"    Found {len(urls)} observation photos. Downloading & validating...")

        # 2. Download and save
        class_train_dir = os.path.join(TRAIN_DIR, folder)
        class_test_dir = os.path.join(TEST_DIR, folder)
        os.makedirs(class_train_dir, exist_ok=True)
        os.makedirs(class_test_dir, exist_ok=True)

        curr_max_idx = get_max_image_index(cid, all_files)
        success_count = 0

        for u in urls:
            if success_count >= needed:
                break

            img = download_and_verify_image(u)
            if img is None:
                continue

            curr_max_idx += 1
            filename = f"{int(cid):03d}{curr_max_idx:04d}.jpg"

            # 80/20 train/test split: every 5th image (20%) goes to test
            if (success_count + 1) % 5 == 0:
                dest_dir = class_test_dir
                total_added_test += 1
                target_split = "test"
            else:
                dest_dir = class_train_dir
                total_added_train += 1
                target_split = "train"

            save_path = os.path.join(dest_dir, filename)
            try:
                # Save as clean standard JPEG (quality=92)
                img.save(save_path, "JPEG", quality=92, optimize=True)
                success_count += 1
                print(f"    + Saved {filename} -> {target_split}/")
            except Exception as e:
                print(f"    Error saving {filename}: {e}")

        print(f"    Successfully added {success_count} images for [{cid}] {com}.")

    print("\n" + "=" * 60)
    print(f"Augmentation complete!")
    print(f"  + Added to train: {total_added_train} images")
    print(f"  + Added to test:  {total_added_test} images")
    print(f"  + Total new:      {total_added_train + total_added_test} images")
    print("=" * 60)
    print("Next step: Retrain model with './train.sh' or 'python train_model.py'")


def main():
    parser = argparse.ArgumentParser(
        description="Download butterfly images from iNaturalist & Wikimedia to augment training dataset."
    )
    parser.add_argument(
        "--summary", action="store_true", help="Print table of image counts across all 80 species."
    )
    parser.add_argument(
        "--min-images", type=int, default=30,
        help="Target minimum total images per species (default: 30)."
    )
    parser.add_argument(
        "--species", nargs="+",
        help="Specific 3-digit class ID(s) to augment (e.g. --species 042 048)."
    )
    parser.add_argument(
        "--max-fetch", type=int, default=30,
        help="Maximum images to download for any single class in one run (default: 30)."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Inspect which species would be augmented without downloading anything."
    )

    args = parser.parse_args()

    classes = get_existing_classes()
    if args.summary:
        show_summary(classes)
        return

    balance_dataset(
        min_images=args.min_images,
        target_species=args.species,
        dry_run=args.dry_run,
        max_per_class=args.max_fetch
    )


if __name__ == "__main__":
    main()
