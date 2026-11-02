package com.butterfly.classifier;

import java.util.HashMap;
import java.util.Map;

/**
 * Rich scientific metadata and classification details for all supported species.
 */
public class SpeciesInfo {

    public static class Details {
        public final String id;
        public final String commonName;
        public final String scientificName;
        public final String family;
        public final String genus;
        public final String speciesName;
        public final String kingdom = "Animalia";
        public final String phylum = "Arthropoda";
        public final String className = "Insecta";
        public final String order = "Lepidoptera";
        public final String habitat;
        public final String distribution;
        public final String description;
        public final String sampleImagePath;

        public Details(String id, String commonName, String scientificName, String family,
                       String genus, String speciesName, String habitat, String distribution,
                       String description, String sampleImagePath) {
            this.id = id;
            this.commonName = commonName;
            this.scientificName = scientificName;
            this.family = family;
            this.genus = genus;
            this.speciesName = speciesName;
            this.habitat = habitat;
            this.distribution = distribution;
            this.description = description;
            this.sampleImagePath = sampleImagePath;
        }
    }

    private static final Map<Species, Details> METADATA = new HashMap<>();

    static {
        METADATA.put(Species.SPECIES_001, new Details(
            "001", "Monarch", "Danaus plexippus", "Nymphalidae",
            "Danaus", "Danaus plexippus",
            "Fields, meadows, gardens, & milkweed patches",
            "North, Central, & South America, Caribbean, Australia",
            "Famous for its multi-generational annual migration across North America. Bright orange wings framed by black borders and white dots serve as warning coloration.",
            "images/0010001.png"
        ));

        METADATA.put(Species.SPECIES_002, new Details(
            "002", "Zebra Longwing", "Heliconius charitonius", "Nymphalidae",
            "Heliconius", "Heliconius charitonius",
            "Tropical hammocks, rainforest margins, & botanical gardens",
            "South & Central America, West Indies, Florida, Texas",
            "Features distinctive elongated black wings with bright yellow zebra stripes. Feeds on pollen in addition to nectar.",
            "images/0020003.png"
        ));

        METADATA.put(Species.SPECIES_003, new Details(
            "003", "Red Passion", "Heliconius erato", "Nymphalidae",
            "Heliconius", "Heliconius erato",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/003_Heliconius_erato_Red_Passion/0030001.png"
        ));

        METADATA.put(Species.SPECIES_004, new Details(
            "004", "Common Buckeye", "Junonia coenia", "Nymphalidae",
            "Junonia", "Junonia coenia",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0040001.png"
        ));

        METADATA.put(Species.SPECIES_005, new Details(
            "005", "Small Copper", "Lycaena phlaeas", "Lycaenidae",
            "Lycaena", "Lycaena phlaeas",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/005_Lycaena_phlaeas_Small_Copper/0050001.png"
        ));

        METADATA.put(Species.SPECIES_006, new Details(
            "006", "Mourning Cloak", "Nymphalis antiopa", "Nymphalidae",
            "Nymphalis", "Nymphalis antiopa",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0060001.png"
        ));

        METADATA.put(Species.SPECIES_007, new Details(
            "007", "Giant Swallowtail", "Papilio cresphontes", "Papilionidae",
            "Papilio", "Papilio cresphontes",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Papilionidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/007_Papilio_cresphontes_Giant_Swallowtail/0070001.png"
        ));

        METADATA.put(Species.SPECIES_008, new Details(
            "008", "Cabbage White", "Pieris rapae", "Pieridae",
            "Pieris", "Pieris rapae",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Pieridae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/008_Pieris_rapae_Cabbage_White/0080001.png"
        ));

        METADATA.put(Species.SPECIES_009, new Details(
            "009", "Red Admiral", "Vanessa atalanta", "Nymphalidae",
            "Vanessa", "Vanessa atalanta",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0090001.png"
        ));

        METADATA.put(Species.SPECIES_010, new Details(
            "010", "Painted Lady", "Vanessa cardui", "Nymphalidae",
            "Vanessa", "Vanessa cardui",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0100001.png"
        ));

        METADATA.put(Species.SPECIES_011, new Details(
            "011", "Pygmy Scrub Hopper", "Aeromachus pygmaeus", "Hesperiidae",
            "Aeromachus", "Aeromachus pygmaeus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/011_Aeromachus_pygmaeus/0110001.jpg"
        ));

        METADATA.put(Species.SPECIES_012, new Details(
            "012", "Bush Hopper", "Ampittia dioscorides", "Hesperiidae",
            "Ampittia", "Ampittia dioscorides",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0120001.png"
        ));

        METADATA.put(Species.SPECIES_013, new Details(
            "013", "Minturn Silverstreak", "Ancema blanka minturna", "Lycaenidae",
            "Ancema", "Ancema blanka minturna",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/013_Ancema_blanka_minturna/0130001.jpg"
        ));

        METADATA.put(Species.SPECIES_014, new Details(
            "014", "Bi-spot Royal", "Ancema ctesia ctesia", "Lycaenidae",
            "Ancema", "Ancema ctesia ctesia",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/014_Ancema_ctesia_ctesia/0140001.jpg"
        ));

        METADATA.put(Species.SPECIES_015, new Details(
            "015", "Ciliate Blue", "Anthene emolus emolus", "Lycaenidae",
            "Anthene", "Anthene emolus emolus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/015_Anthene_emolus_emolus/0150001.jpg"
        ));

        METADATA.put(Species.SPECIES_016, new Details(
            "016", "Pointed Ciliate Blue", "Anthene lycaenina lycambes", "Lycaenidae",
            "Anthene", "Anthene lycaenina lycambes",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/016_Anthene_lycaenina_lycambes/0160001.jpg"
        ));

        METADATA.put(Species.SPECIES_017, new Details(
            "017", "Common Sergeant", "Athyma perius", "Nymphalidae",
            "Athyma", "Athyma perius",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0170001.png"
        ));

        METADATA.put(Species.SPECIES_018, new Details(
            "018", "Brown Awl", "Badamia exclamationis", "Hesperiidae",
            "Badamia", "Badamia exclamationis",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/018_Badamia_exclamationis/0180001.jpg"
        ));

        METADATA.put(Species.SPECIES_019, new Details(
            "019", "Orange Awlet", "Burara jaina", "Hesperiidae",
            "Burara", "Burara jaina",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/019_Burara_jaina/0190001.jpg"
        ));

        METADATA.put(Species.SPECIES_020, new Details(
            "020", "Elbowed Pierrot", "Caleta elna noliteia", "Lycaenidae",
            "Caleta", "Caleta elna noliteia",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/020_Caleta_elna_noliteia/0200001.jpg"
        ));

        METADATA.put(Species.SPECIES_021, new Details(
            "021", "Forget-me-not", "Catochrysops strabo strabo", "Lycaenidae",
            "Catochrysops", "Catochrysops strabo strabo",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/021_Catochrysops_strabo_strabo/0210001.jpg"
        ));

        METADATA.put(Species.SPECIES_022, new Details(
            "022", "Yellow-banded Flat", "Celaenorrhinus aurivittata aurivittata", "Hesperiidae",
            "Celaenorrhinus", "Celaenorrhinus aurivittata aurivittata",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/022_Celaenorrhinus_aurivittata_aurivittata/0220001.jpg"
        ));

        METADATA.put(Species.SPECIES_023, new Details(
            "023", "Common Spotted Flat", "Celaenorrhinus leucocera", "Hesperiidae",
            "Celaenorrhinus", "Celaenorrhinus leucocera",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/023_Celaenorrhinus_leucocera/0230001.jpg"
        ));

        METADATA.put(Species.SPECIES_024, new Details(
            "024", "Leopard Lacewing", "Cethosia cyane", "Nymphalidae",
            "Cethosia", "Cethosia cyane",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/024_Cethosia_cyane/0240001.jpg"
        ));

        METADATA.put(Species.SPECIES_025, new Details(
            "025", "Tawny Rajah", "Charaxes bernardus hierax", "Nymphalidae",
            "Charaxes", "Charaxes bernardus hierax",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/025_Charaxes_bernardus_hierax/0250001.jpg"
        ));

        METADATA.put(Species.SPECIES_026, new Details(
            "026", "Yellow Rajah", "Charaxes marmax marmax", "Nymphalidae",
            "Charaxes", "Charaxes marmax marmax",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/026_Charaxes_marmax_marmax/0260001.jpg"
        ));

        METADATA.put(Species.SPECIES_027, new Details(
            "027", "Lime Blue", "Chilades lajus lajus", "Lycaenidae",
            "Chilades", "Chilades lajus lajus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/027_Chilades_lajus_lajus/0270001.jpg"
        ));

        METADATA.put(Species.SPECIES_028, new Details(
            "028", "Indian Awlking", "Choaspes benjaminii japonica", "Hesperiidae",
            "Choaspes", "Choaspes benjaminii japonica",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/028_Choaspes_benjaminii_japonica/0280001.jpg"
        ));

        METADATA.put(Species.SPECIES_029, new Details(
            "029", "Wax Dart", "Cupitha purreea purreea", "Hesperiidae",
            "Cupitha", "Cupitha purreea purreea",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/029_Cupitha_purreea_purreea/0290001.jpg"
        ));

        METADATA.put(Species.SPECIES_030, new Details(
            "030", "Common Palmfly", "Elymnias hypermnestra undularis", "Nymphalidae",
            "Elymnias", "Elymnias hypermnestra undularis",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0300001.png"
        ));

        METADATA.put(Species.SPECIES_031, new Details(
            "031", "Tiger Palmfly", "Elymnias nesaea", "Nymphalidae",
            "Elymnias", "Elymnias nesaea",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/031_Elymnias_nesaea/0310001.jpg"
        ));

        METADATA.put(Species.SPECIES_032, new Details(
            "032", "Dusky Diadem", "Ethope himachala", "Nymphalidae",
            "Ethope", "Ethope himachala",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0320001.png"
        ));

        METADATA.put(Species.SPECIES_033, new Details(
            "033", "Great Yellow Sailer", "Gerosis phisara phisara", "Hesperiidae",
            "Gerosis", "Gerosis phisara phisara",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/033_Gerosis_phisara_phisara/0330001.jpg"
        ));

        METADATA.put(Species.SPECIES_034, new Details(
            "034", "Tailed Jay", "Graphium agamemnon", "Papilionidae",
            "Graphium", "Graphium agamemnon",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Papilionidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/034_Graphium_agamemnon/0340001.jpg"
        ));

        METADATA.put(Species.SPECIES_035, new Details(
            "035", "Gold-spotted Ace", "Halpe aucma", "Hesperiidae",
            "Halpe", "Halpe aucma",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/035_Halpe_aucma/0350001.png"
        ));

        METADATA.put(Species.SPECIES_036, new Details(
            "036", "Plain Ace", "Halpe kusala", "Hesperiidae",
            "Halpe", "Halpe kusala",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/036_Halpe_kusala/0360001.jpg"
        ));

        METADATA.put(Species.SPECIES_037, new Details(
            "037", "Moore's Ace", "Halpe porus porus", "Hesperiidae",
            "Halpe", "Halpe porus porus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0370001.png"
        ));

        METADATA.put(Species.SPECIES_038, new Details(
            "038", "Zema Ace", "Halpe zema zema", "Hesperiidae",
            "Halpe", "Halpe zema zema",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/038_Halpe_zema_zema/0380001.jpg"
        ));

        METADATA.put(Species.SPECIES_039, new Details(
            "039", "Common Awl", "Hasora badra", "Hesperiidae",
            "Hasora", "Hasora badra",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0390001.png"
        ));

        METADATA.put(Species.SPECIES_040, new Details(
            "040", "Purple Sapphire", "Heliophorus epicles latilimbata", "Lycaenidae",
            "Heliophorus", "Heliophorus epicles latilimbata",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0400001.png"
        ));

        METADATA.put(Species.SPECIES_041, new Details(
            "041", "Sky Blue", "Jamides caerulea", "Lycaenidae",
            "Jamides", "Jamides caerulea",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/041_Jamides_caerulea/0410001.jpg"
        ));

        METADATA.put(Species.SPECIES_042, new Details(
            "042", "Common Cerulean", "Jamides celeno", "Lycaenidae",
            "Jamides", "Jamides celeno",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/042_Jamides_celeno/0420001.jpg"
        ));

        METADATA.put(Species.SPECIES_043, new Details(
            "043", "Glistening Cerulean", "Jamides elpis pseudelpis", "Lycaenidae",
            "Jamides", "Jamides elpis pseudelpis",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0430001.png"
        ));

        METADATA.put(Species.SPECIES_044, new Details(
            "044", "Angled Red Forester", "Lethe chandica flanona", "Nymphalidae",
            "Lethe", "Lethe chandica flanona",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/044_Lethe_chandica_flanona/0440001.jpg"
        ));

        METADATA.put(Species.SPECIES_045, new Details(
            "045", "Common Treebrown", "Lethe mekara mekara", "Nymphalidae",
            "Lethe", "Lethe mekara mekara",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0450001.png"
        ));

        METADATA.put(Species.SPECIES_046, new Details(
            "046", "Pallid Forester", "Lethe satyavati", "Nymphalidae",
            "Lethe", "Lethe satyavati",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/046_Lethe_satyavati/0460001.jpg"
        ));

        METADATA.put(Species.SPECIES_047, new Details(
            "047", "Black Forester", "Lethe vindhya vindhya", "Nymphalidae",
            "Lethe", "Lethe vindhya vindhya",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Nymphalidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/047_Lethe_vindhya_vindhya/0470001.jpg"
        ));

        METADATA.put(Species.SPECIES_048, new Details(
            "048", "Yamfly", "Loxura atymnus continentalis", "Lycaenidae",
            "Loxura", "Loxura atymnus continentalis",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0480001.png"
        ));

        METADATA.put(Species.SPECIES_049, new Details(
            "049", "Malayan", "Megisba malaya sikkima", "Lycaenidae",
            "Megisba", "Megisba malaya sikkima",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/049_Megisba_malaya_sikkima/0490001.jpg"
        ));

        METADATA.put(Species.SPECIES_050, new Details(
            "050", "Yellow Flat", "Mooreana trichoneura pralaya", "Hesperiidae",
            "Mooreana", "Mooreana trichoneura pralaya",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/050_Mooreana_trichoneura_pralaya/0500001.jpg"
        ));

        METADATA.put(Species.SPECIES_051, new Details(
            "051", "Transparent 6-Line Blue", "Nacaduba kurava euplea", "Lycaenidae",
            "Nacaduba", "Nacaduba kurava euplea",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/051_Nacaduba_kurava_euplea/0510001.jpg"
        ));

        METADATA.put(Species.SPECIES_052, new Details(
            "052", "Common Quaker", "Neopithecops zalmora zalmora", "Lycaenidae",
            "Neopithecops", "Neopithecops zalmora zalmora",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/052_Neopithecops_zalmora_zalmora/0520001.jpg"
        ));

        METADATA.put(Species.SPECIES_053, new Details(
            "053", "Common Banded Demon", "Notocrypta curvifascia curvifascia", "Hesperiidae",
            "Notocrypta", "Notocrypta curvifascia curvifascia",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/053_Notocrypta_curvifascia_curvifascia/0530001.jpg"
        ));

        METADATA.put(Species.SPECIES_054, new Details(
            "054", "Grass Demon", "Notocrypta paralysos asawa", "Hesperiidae",
            "Notocrypta", "Notocrypta paralysos asawa",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0540001.png"
        ));

        METADATA.put(Species.SPECIES_055, new Details(
            "055", "Tiger Hopper", "Ochus subvittatus subradiatus", "Hesperiidae",
            "Ochus", "Ochus subvittatus subradiatus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0550001.png"
        ));

        METADATA.put(Species.SPECIES_056, new Details(
            "056", "Chestnut Angle", "Odontoptilum angulata angulata", "Hesperiidae",
            "Odontoptilum", "Odontoptilum angulata angulata",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/056_Odontoptilum_angulata_angulata/0560001.jpg"
        ));

        METADATA.put(Species.SPECIES_057, new Details(
            "057", "Common Dartlet", "Oriens gola pseudolus", "Hesperiidae",
            "Oriens", "Oriens gola pseudolus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/057_Oriens_gola_pseudolus/0570001.jpg"
        ));

        METADATA.put(Species.SPECIES_058, new Details(
            "058", "Paris Peacock", "Papilio paris", "Papilionidae",
            "Papilio", "Papilio paris",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Papilionidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/058_Papilio_paris/0580001.jpg"
        ));

        METADATA.put(Species.SPECIES_059, new Details(
            "059", "Light Straw Ace", "Pithauria stramineipennis", "Hesperiidae",
            "Pithauria", "Pithauria stramineipennis",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/059_Pithauria_stramineipennis/0590001.jpg"
        ));

        METADATA.put(Species.SPECIES_060, new Details(
            "060", "Indian Dart", "Potanthus pseudomaesa", "Hesperiidae",
            "Potanthus", "Potanthus pseudomaesa",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/060_Potanthus_pseudomaesa/0600001.jpg"
        ));

        METADATA.put(Species.SPECIES_061, new Details(
            "061", "Banded Lineblue", "Prosotas aluta coelestis", "Lycaenidae",
            "Prosotas", "Prosotas aluta coelestis",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/061_Prosotas_aluta_coelestis/0610001.jpg"
        ));

        METADATA.put(Species.SPECIES_062, new Details(
            "062", "Bhutya Lineblue", "Prosotas bhutea", "Lycaenidae",
            "Prosotas", "Prosotas bhutea",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/062_Prosotas_bhutea/0620001.jpg"
        ));

        METADATA.put(Species.SPECIES_063, new Details(
            "063", "Tailless Lineblue", "Prosotas dubiosa indica", "Lycaenidae",
            "Prosotas", "Prosotas dubiosa indica",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0630001.png"
        ));

        METADATA.put(Species.SPECIES_064, new Details(
            "064", "Common Lineblue", "Prosotas nora ardates", "Lycaenidae",
            "Prosotas", "Prosotas nora ardates",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/064_Prosotas_nora_ardates/0640001.jpg"
        ));

        METADATA.put(Species.SPECIES_065, new Details(
            "065", "Fulvous Pied Flat", "Pseudocoladenia dan fabia", "Hesperiidae",
            "Pseudocoladenia", "Pseudocoladenia dan fabia",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/065_Pseudocoladenia_dan_fabia/0650001.jpg"
        ));

        METADATA.put(Species.SPECIES_066, new Details(
            "066", "Coon", "Psolos fuligo subfasciatus", "Hesperiidae",
            "Psolos", "Psolos fuligo subfasciatus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/066_Psolos_fuligo_subfasciatus/0660001.jpg"
        ));

        METADATA.put(Species.SPECIES_067, new Details(
            "067", "Chocolate Royal", "Remelana jangala ravata", "Lycaenidae",
            "Remelana", "Remelana jangala ravata",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/067_Remelana_jangala_ravata/0670001.jpg"
        ));

        METADATA.put(Species.SPECIES_068, new Details(
            "068", "Common Small Flat", "Sarangesa dasahara dasahara", "Hesperiidae",
            "Sarangesa", "Sarangesa dasahara dasahara",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0680001.png"
        ));

        METADATA.put(Species.SPECIES_069, new Details(
            "069", "Tufted Ace", "Sebastonyma dolopia", "Hesperiidae",
            "Sebastonyma", "Sebastonyma dolopia",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/069_Sebastonyma_dolopia/0690001.jpg"
        ));

        METADATA.put(Species.SPECIES_070, new Details(
            "070", "Notched Flat", "Seseria sambara sambara", "Hesperiidae",
            "Seseria", "Seseria sambara sambara",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/070_Seseria_sambara_sambara/0700001.png"
        ));

        METADATA.put(Species.SPECIES_071, new Details(
            "071", "Long-banded Silverline", "Spindasis lohita himalayanus", "Lycaenidae",
            "Spindasis", "Spindasis lohita himalayanus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/071_Spindasis_lohita_himalayanus/0710001.jpg"
        ));

        METADATA.put(Species.SPECIES_072, new Details(
            "072", "Common Acacia Blue", "Surendra quercetorum quercetorum", "Lycaenidae",
            "Surendra", "Surendra quercetorum quercetorum",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/072_Surendra_quercetorum_quercetorum/0720001.jpg"
        ));

        METADATA.put(Species.SPECIES_073, new Details(
            "073", "Ravi Snow Flat", "Tagiades dynamicus ravi", "Hesperiidae",
            "Tagiades", "Tagiades dynamicus ravi",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0730001.png"
        ));

        METADATA.put(Species.SPECIES_074, new Details(
            "074", "Suffused Snow Flat", "Tagiades gana gana", "Hesperiidae",
            "Tagiades", "Tagiades gana gana",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/074_Tagiades_gana_gana/0740001.jpg"
        ));

        METADATA.put(Species.SPECIES_075, new Details(
            "075", "Water Snow Flat", "Tagiades litigiosa litigiosa", "Hesperiidae",
            "Tagiades", "Tagiades litigiosa litigiosa",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/075_Tagiades_litigiosa_litigiosa/0750001.jpg"
        ));

        METADATA.put(Species.SPECIES_076, new Details(
            "076", "Dark Palm Dart", "Telicota bambusae bambusae", "Hesperiidae",
            "Telicota", "Telicota bambusae bambusae",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "images/0760001.png"
        ));

        METADATA.put(Species.SPECIES_077, new Details(
            "077", "Pale Palm Dart", "Telicota colon", "Hesperiidae",
            "Telicota", "Telicota colon",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/077_Telicota_colon/0770001.jpg"
        ));

        METADATA.put(Species.SPECIES_078, new Details(
            "078", "Northern Spangle", "Thoressa cerata", "Hesperiidae",
            "Thoressa", "Thoressa cerata",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Hesperiidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/078_Thoressa_cerata/0780001.jpg"
        ));

        METADATA.put(Species.SPECIES_079, new Details(
            "079", "Golden Birdwing", "Troides aeacus", "Papilionidae",
            "Troides", "Troides aeacus",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Papilionidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/079_Troides_aeacus/0790001.jpg"
        ));

        METADATA.put(Species.SPECIES_080, new Details(
            "080", "Three-spot Silverstreak", "Yasuda tripunctata tripunctata", "Lycaenidae",
            "Yasuda", "Yasuda tripunctata tripunctata",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/080_Yasuda_tripunctata_tripunctata/0800001.jpg"
        ));

        METADATA.put(Species.SPECIES_081, new Details(
            "081", "Zubeen's Baron", "Euthalia zubeengargi", "Nymphalidae",
            "Euthalia", "Euthalia zubeengargi",
            "Panbari Reserve Forest, lowland wet evergreen rainforest understorey, Golaghat / Kaziranga landscape",
            "Endemic to Assam, Northeast India (Indo-Burma biodiversity hotspot)",
            "Discovered and described in 2024 from the Panbari Reserve Forest in Assam. Named in honor of cultural icon Zubeen Garg. Cryptic understorey dweller with rapid flight and distinct dorsal-ventral pattern.",
            "dataset/train/081_Euthalia_zubeengargi/0810001.jpg"
        ));

        METADATA.put(Species.SPECIES_082, new Details(
            "082", "Yellow-crested Spangle", "Papilio elephenor", "Papilionidae",
            "Papilio", "Papilio elephenor",
            "Primary tropical rainforests, foothills, and damp river banks of Assam",
            "Endemic to Northeast India (Assam, Meghalaya) and adjacent Myanmar",
            "Extremely rare swallowtail featuring prominent yellow-crested scaling on dark forewings and spatulate hindwing tails.",
            "dataset/train/082_Papilio_elephenor/0820001.jpg"
        ));

        METADATA.put(Species.SPECIES_083, new Details(
            "083", "Great Blue Mime", "Papilio paradoxa", "Papilionidae",
            "Papilio", "Papilio paradoxa",
            "Dense evergreen rainforest canopies and wet lowland forest corridors",
            "Assam, Northeast India, Sundaland, and Indo-China",
            "Magnificent mimic of Euploea crows, displaying deep iridescent blue gloss across its broad wings.",
            "dataset/train/083_Papilio_paradoxa/0830001.jpg"
        ));

        METADATA.put(Species.SPECIES_084, new Details(
            "084", "Tailed Redbreast", "Papilio bootes", "Papilionidae",
            "Papilio", "Papilio bootes",
            "Subtropical montane forests, moist stream beds, and bamboo thickets",
            "Eastern Himalayas, Assam, Nagaland, and northern Myanmar",
            "Distinctive swallowtail with bright red basal patches on ventral surfaces and spatulate tails.",
            "dataset/train/084_Papilio_bootes/0840001.jpg"
        ));

        METADATA.put(Species.SPECIES_085, new Details(
            "085", "Blue-striped Mime", "Papilio slateri", "Papilionidae",
            "Papilio", "Papilio slateri",
            "Dense evergreen forests and forest paths, mimics Danaine crows",
            "Assam, Meghalaya, Northeast India to Vietnam and Sundaland",
            "Remarkable mimic of Euploea radamanthus featuring crisp blue-white radial stripes on velvety black wings.",
            "dataset/train/085_Papilio_slateri/0850001.jpg"
        ));

        METADATA.put(Species.SPECIES_086, new Details(
            "086", "White Dragontail", "Lamproptera curius", "Papilionidae",
            "Lamproptera", "Lamproptera curius",
            "Fast-flowing rocky streams and clearings in humid tropical rainforests",
            "Assam, Arunachal Pradesh, Northeast India, Southeast Asia",
            "Peculiar miniature swallowtail with transparent glass-like wing windows and elongated dragonfly-like tails.",
            "dataset/train/086_Lamproptera_curius/0860001.jpg"
        ));

        METADATA.put(Species.SPECIES_087, new Details(
            "087", "Green Dragontail", "Lamproptera meges", "Papilionidae",
            "Lamproptera", "Lamproptera meges",
            "Sunlit riparian corridors and gravel shores of forest streams",
            "Northeast India (Assam, Cachar), Myanmar, Malaysia, Indonesia",
            "Brilliant emerald-banded dragontail adapted for high-speed hovering and rapid darting over forest rapids.",
            "dataset/train/087_Lamproptera_meges/0870001.jpg"
        ));

        METADATA.put(Species.SPECIES_088, new Details(
            "088", "Yellow Gorgon", "Meandrusa payeni", "Papilionidae",
            "Meandrusa", "Meandrusa payeni",
            "High sub-Himalayan forest canopies, ridge tops, and sun-warmed peaks",
            "Assam, Sikkim, Arunachal Pradesh, Southeast Asia",
            "Striking sickle-winged swallowtail with bright saffron-yellow ground color and jagged wing outlines.",
            "dataset/train/088_Meandrusa_payeni/0880001.jpg"
        ));

        METADATA.put(Species.SPECIES_089, new Details(
            "089", "Brown Gorgon", "Meandrusa lachinus", "Papilionidae",
            "Meandrusa", "Meandrusa lachinus",
            "Dense oak-laurel forests and cloud forest ridges",
            "Eastern Himalayas, Assam hill tracts, Myanmar",
            "Cryptic brown swallowtail mimicking dried leaves when at rest in deep montane forest canopies.",
            "dataset/train/089_Meandrusa_lachinus/0890001.jpg"
        ));

        METADATA.put(Species.SPECIES_090, new Details(
            "090", "Black Windmill", "Byasa crassipes", "Papilionidae",
            "Byasa", "Byasa crassipes",
            "Moist montane forests and steep wooded valleys",
            "Assam, Manipur, Nagaland, northern Myanmar",
            "Heavy-bodied black windmill swallowtail with crimson body markings and spatulate tails.",
            "dataset/train/090_Byasa_crassipes/0900001.jpg"
        ));

        METADATA.put(Species.SPECIES_091, new Details(
            "091", "Nevill's Windmill", "Byasa nevilli", "Papilionidae",
            "Byasa", "Byasa nevilli",
            "Deep riverine gorges, primary evergreen forests",
            "Assam, Arunachal Pradesh, SW China, Myanmar",
            "Rare windmill species documented along isolated forest river corridors in Upper Assam.",
            "dataset/train/091_Byasa_nevilli/0910001.jpg"
        ));

        METADATA.put(Species.SPECIES_092, new Details(
            "092", "De Nicéville's Windmill", "Byasa polla", "Papilionidae",
            "Byasa", "Byasa polla",
            "Subtropical forest tracts and flowering ravines",
            "Assam, Nagaland, Manipur, Myanmar",
            "Rare aristolochia-feeding windmill with bright white submarginal spots on velvety wings.",
            "dataset/train/092_Byasa_polla/0920001.jpg"
        ));

        METADATA.put(Species.SPECIES_093, new Details(
            "093", "Fourbar Swallowtail", "Graphium agetes", "Papilionidae",
            "Graphium", "Graphium agetes",
            "Sandy riverbeds, damp forest clearings, and riparian margins",
            "Assam, Sikkim, Northeast India, Indo-China",
            "Elongated swordtail with pale greenish-white wings traversed by four distinct dark transverse bars.",
            "dataset/train/093_Graphium_agetes/0930001.jpg"
        ));

        METADATA.put(Species.SPECIES_094, new Details(
            "094", "Chain Swordtail", "Graphium aristeus", "Papilionidae",
            "Graphium", "Graphium aristeus",
            "Deciduous to semi-evergreen forest margins and river banks",
            "Assam, Western Ghats, Indo-Malayan realm to Australasia",
            "Fast-flying swordtail decorated with chained rows of dark spots and needle-sharp hindwing tails.",
            "dataset/train/094_Graphium_aristeus/0940001.jpg"
        ));

        METADATA.put(Species.SPECIES_095, new Details(
            "095", "Lesser Zebra", "Graphium macareus", "Papilionidae",
            "Graphium", "Graphium macareus",
            "Lowland evergreen and semi-evergreen forests, damp patches on paths",
            "Assam, Sikkim, Southeast Asia",
            "Zebra-patterned swallowtail mimicking milkweed butterflies while mud-puddling on wet sand.",
            "dataset/train/095_Graphium_macareus/0950001.jpg"
        ));

        METADATA.put(Species.SPECIES_096, new Details(
            "096", "Great Zebra", "Graphium xenocles", "Papilionidae",
            "Graphium", "Graphium xenocles",
            "Subtropical forest riverbeds, mud-puddling sites in sunny clearings",
            "Assam, Eastern Himalayas, Myanmar, Thailand",
            "Large, striking black and cream-striped zebra swallowtail of sub-Himalayan forest streams.",
            "dataset/train/096_Graphium_xenocles/0960001.jpg"
        ));

        METADATA.put(Species.SPECIES_097, new Details(
            "097", "Common Clubtail", "Losaria doubledayi", "Papilionidae",
            "Losaria", "Losaria doubledayi",
            "Humid lowland rainforests, forest understorey, and stream courses",
            "Assam, Northeast India, Myanmar, Malay Peninsula",
            "Clubtail swallowtail displaying crimson thoracic patches and prominent spatulate wing clubs.",
            "dataset/train/097_Losaria_doubledayi/0970001.jpg"
        ));

        METADATA.put(Species.SPECIES_098, new Details(
            "098", "Kaiser-i-Hind", "Teinopalpus imperialis", "Papilionidae",
            "Teinopalpus", "Teinopalpus imperialis",
            "High montane broadleaf canopy, cloud forest ridges above 2,000 meters",
            "Eastern Himalayas, Assam hill ranges, Arunachal Pradesh, Vietnam",
            "The legendary Kaiser-i-Hind, one of the world's most revered swallowtails with brilliant iridescent green scales and double tails.",
            "dataset/train/098_Teinopalpus_imperialis/0980001.jpg"
        ));

        METADATA.put(Species.SPECIES_099, new Details(
            "099", "Peal's Palmfly", "Elymnias peali", "Nymphalidae",
            "Elymnias", "Elymnias peali",
            "Deep shade of bamboo brakes, riverine evergreen forests of Upper Assam",
            "Extremely rare endemic to Assam (Sibsagar, Margherita) and Nagaland",
            "One of the rarest butterflies in the world, discovered in Margherita, Assam by S.E. Peal. Highly shade-loving.",
            "dataset/train/099_Elymnias_peali/0990001.jpg"
        ));

        METADATA.put(Species.SPECIES_100, new Details(
            "100", "Blue Baron", "Euthalia telchinia", "Nymphalidae",
            "Euthalia", "Euthalia telchinia",
            "Wet evergreen forest undergrowth, decaying fruit along shaded trails",
            "Assam, Sikkim, Meghalaya, Myanmar",
            "Magnificent forest nymphalid where the male possesses an intense electric cobalt-blue border on deep brown wings.",
            "dataset/train/100_Euthalia_telchinia/1000001.jpg"
        ));

        METADATA.put(Species.SPECIES_101, new Details(
            "101", "Jewelled Nawab", "Charaxes delphis", "Nymphalidae",
            "Charaxes", "Charaxes delphis",
            "Dense tropical rainforest canopy, sap oozing trees and ridge tops",
            "Assam, Meghalaya, Southeast Asia to Borneo and Sumatra",
            "The Jewelled Nawab features shimmering mother-of-pearl undersides with delicate crimson and yellow markings.",
            "dataset/train/101_Charaxes_delphis/1010001.jpg"
        ));

        METADATA.put(Species.SPECIES_102, new Details(
            "102", "Conjoined Lascar", "Pantoporia assamica", "Nymphalidae",
            "Pantoporia", "Pantoporia assamica",
            "Shaded stream corridors, primary evergreen forest undergrowth",
            "Endemic to Assam and neighbouring tracts of Northeast India",
            "Rare endemic lascar featuring joined orange bands on the forewing, adapted for low gliding flight.",
            "dataset/train/102_Pantoporia_assamica/1020001.jpg"
        ));

        METADATA.put(Species.SPECIES_103, new Details(
            "103", "Tytler's Lascar", "Pantoporia bieti", "Nymphalidae",
            "Pantoporia", "Pantoporia bieti",
            "Montane forest paths and bamboo clearings",
            "Assam, Nagaland, Manipur, SW China",
            "High-elevation lascar with crisp black-and-white bands and delicate yellow margins.",
            "dataset/train/103_Pantoporia_bieti/1030001.jpg"
        ));

        METADATA.put(Species.SPECIES_104, new Details(
            "104", "Wavy Maplet", "Chersonesia rahria", "Nymphalidae",
            "Chersonesia", "Chersonesia rahria",
            "Subcanopy of lowland dipterocarp and wet evergreen rainforests of Assam",
            "Assam, Northeast India, Sundaland",
            "Exquisite orange maplet with undulating transverse lines resembling delicate contour maps.",
            "dataset/train/104_Chersonesia_rahria/1040001.jpg"
        ));

        METADATA.put(Species.SPECIES_105, new Details(
            "105", "Blackvein Sergeant", "Athyma ranga", "Nymphalidae",
            "Athyma", "Athyma ranga",
            "Damp forest clearings, waterfalls, and sunlit stream rocks",
            "Assam, Western Ghats, Eastern Himalayas, Indo-China",
            "Blackvein Sergeant with crisp white longitudinal bands framed by rich velvet black margins.",
            "dataset/train/105_Athyma_ranga/1050001.jpg"
        ));

        METADATA.put(Species.SPECIES_106, new Details(
            "106", "Unbroken Sergeant", "Athyma pravara", "Nymphalidae",
            "Athyma", "Athyma pravara",
            "Evergreen forest trails and forest margins",
            "Assam, Northeast India, Southeast Asia",
            "Unbroken Sergeant distinguished by a continuous, unbroken white discal band across both wings.",
            "dataset/train/106_Athyma_pravara/1060001.jpg"
        ));

        METADATA.put(Species.SPECIES_107, new Details(
            "107", "White-bordered Sergeant", "Athyma punctata", "Nymphalidae",
            "Athyma", "Athyma punctata",
            "Primary sub-Himalayan forest trails and wet understory",
            "Assam, Eastern Himalayas, Myanmar, Southern China",
            "Rare sergeant characterized by wide white borders and distinct postdiscal white spots.",
            "dataset/train/107_Athyma_punctata/1070001.jpg"
        ));

        METADATA.put(Species.SPECIES_108, new Details(
            "108", "Blue Nawab", "Polyura schreiber", "Nymphalidae",
            "Polyura", "Polyura schreiber",
            "High rainforest canopy and sunlit tree crowns",
            "Assam, Western Ghats, Indo-Malayan bioregions",
            "Blue Nawab with a heavy, robust build, turquoise-blue central patch, and powerful, aggressive flight.",
            "dataset/train/108_Polyura_schreiber/1080001.jpg"
        ));

        METADATA.put(Species.SPECIES_109, new Details(
            "109", "Spotted Royal", "Tajuria maculata", "Lycaenidae",
            "Tajuria", "Tajuria maculata",
            "Tree tops with mistletoe (Loranthaceae), subcanopy in dense forests",
            "Assam, Sikkim, Myanmar, Peninsular Malaysia, Borneo",
            "Rare spotted lycaenid royal with bold black spots beneath gleaming silver-grey undersides.",
            "dataset/train/109_Tajuria_maculata/1090001.jpg"
        ));

        METADATA.put(Species.SPECIES_110, new Details(
            "110", "Peacock Royal", "Tajuria cippus", "Lycaenidae",
            "Tajuria", "Tajuria cippus",
            "Forest canopy, gardens with mistletoe and flowering trees",
            "Throughout Assam and South/Southeast Asia",
            "Peacock Royal displays shimmering peacock-blue uppersides and delicate orange-crowned tails.",
            "dataset/train/110_Tajuria_cippus/1100001.jpg"
        ));

        METADATA.put(Species.SPECIES_111, new Details(
            "111", "Blue Quaker", "Pithecops fulgens", "Lycaenidae",
            "Pithecops", "Pithecops fulgens",
            "Deep shaded understorey in primary evergreen rainforest",
            "Assam, Meghalaya, Nagaland, Myanmar",
            "Tiny, elusive lycaenid characterized by brilliant shining blue dorsal scales and spotless pure white ventral surfaces.",
            "dataset/train/111_Pithecops_fulgens/1110001.jpg"
        ));

        METADATA.put(Species.SPECIES_112, new Details(
            "112", "Moore's Cupid", "Shijimia moorei", "Lycaenidae",
            "Shijimia", "Shijimia moorei",
            "Rocky stream beds, damp sandbanks in subtropical forests",
            "Assam, Eastern Himalayas, China, Japan",
            "Delicate cupid lycaenid adapted to rocky riparian clearings with complex ventral ocelli.",
            "dataset/train/112_Shijimia_moorei/1120001.jpg"
        ));

        METADATA.put(Species.SPECIES_113, new Details(
            "113", "Sylhet Oakblue", "Arhopala silhetensis", "Lycaenidae",
            "Arhopala", "Arhopala silhetensis",
            "Lowland wet evergreen forests, oak and dipterocarp undergrowth",
            "Assam (Sylhet historical tract, Cachar), Bangladesh, Myanmar",
            "Cryptic oakblue named after the historical Sylhet/Cachar tract of Assam, displaying deep purple gloss.",
            "dataset/train/113_Arhopala_silhetensis/1130001.jpg"
        ));

        METADATA.put(Species.SPECIES_114, new Details(
            "114", "Hewitson's Dull Oakblue", "Arhopala oenea", "Lycaenidae",
            "Arhopala", "Arhopala oenea",
            "Shaded evergreen understorey, wet forest ravines",
            "Assam, Sikkim, Myanmar",
            "Dull oakblue adapted for deep camouflage amongst fallen leaves, with bronze-tinged dorsal reflection.",
            "dataset/train/114_Arhopala_oenea/1140001.jpg"
        ));

        METADATA.put(Species.SPECIES_115, new Details(
            "115", "Broad-branded Brilliant", "Simiskina phalena", "Lycaenidae",
            "Simiskina", "Simiskina phalena",
            "Dense tropical rainforest undergrowth, shaded ravines",
            "Assam, Myanmar, Thailand, Malaysia",
            "Poritiine lycaenid with broad velvety scent brands in males and intense metallic blue-purple reflection.",
            "dataset/train/115_Simiskina_phalena/1150001.jpg"
        ));

        METADATA.put(Species.SPECIES_116, new Details(
            "116", "Bi-coloured Hedge Blue", "Udara selma", "Lycaenidae",
            "Udara", "Udara selma",
            "Subtropical forest paths, damp gravel beside mountain brooks",
            "Assam, Eastern Himalayas, Southeast Asia",
            "Bi-coloured Hedge Blue with delicate frosted blue uppersides and fine peppered ventral speckling.",
            "dataset/train/116_Udara_selma/1160001.jpg"
        ));

        METADATA.put(Species.SPECIES_117, new Details(
            "117", "Common Gem", "Poritia hewitsoni", "Lycaenidae",
            "Poritia", "Poritia hewitsoni",
            "Sunlit clearings, forest borders, and secondary evergreen growth",
            "Assam, Eastern Himalayas, Indo-China",
            "Brilliant gem lycaenid whose emerald-green or sky-blue dorsal luster flashes when basking.",
            "dataset/train/117_Poritia_hewitsoni/1170001.jpg"
        ));

        METADATA.put(Species.SPECIES_118, new Details(
            "118", "White Dawnfly", "Capila pieridoides", "Hesperiidae",
            "Capila", "Capila pieridoides",
            "Deep evergreen forest undergrowth, crepuscular flights at dawn/dusk",
            "Assam, Meghalaya, Eastern Himalayas, Indo-China",
            "Large, striking skipper flying actively at dusk and dawn with broad white-bordered wings.",
            "dataset/train/118_Capila_pieridoides/1180001.jpg"
        ));

        METADATA.put(Species.SPECIES_119, new Details(
            "119", "Yellow-vein Lancer", "Pyroneura margherita", "Hesperiidae",
            "Pyroneura", "Pyroneura margherita",
            "Dense lowland rainforests, bamboo brakes in Upper Assam",
            "Endemic type locality Margherita (Assam), Arunachal Pradesh",
            "Discovered at Margherita in Upper Assam, featuring distinctive radiant yellow wing veins.",
            "dataset/train/119_Pyroneura_margherita/1190001.jpg"
        ));

        METADATA.put(Species.SPECIES_120, new Details(
            "120", "Snowy Angle", "Darpa pteria", "Hesperiidae",
            "Darpa", "Darpa pteria",
            "Moist shady forest tracks, resting beneath broad leaves",
            "Assam, Eastern Himalayas, Southeast Asia",
            "Snowy Angle skipper with stark snow-white ventral patches providing disruptive shadow camouflage.",
            "dataset/train/120_Darpa_pteria/1200001.jpg"
        ));

        METADATA.put(Species.SPECIES_121, new Details(
            "121", "Veined Palmer", "Hidari bhawani", "Hesperiidae",
            "Hidari", "Hidari bhawani",
            "Lowland riverine forests, marshes, and bamboo groves",
            "Rare endemic of Assam (Golaghat, Kaziranga), Indo-China",
            "Veined Palmer skipper documented in the Brahmaputra floodplains, displaying stark pale veins on chocolate ground.",
            "dataset/train/121_Hidari_bhawani/1210001.jpg"
        ));

        METADATA.put(Species.SPECIES_122, new Details(
            "122", "Chequered Lancer", "Plastingia naga", "Hesperiidae",
            "Plastingia", "Plastingia naga",
            "Dense forest clearings, damp leaf litter along streams",
            "Assam, Nagaland, Southeast Asia to Borneo",
            "Chequered Lancer adorned with neat golden-yellow chequered spots across dark chocolate wings.",
            "dataset/train/122_Plastingia_naga/1220001.jpg"
        ));

        METADATA.put(Species.SPECIES_123, new Details(
            "123", "Maculate Lancer", "Salanoemia sala", "Hesperiidae",
            "Salanoemia", "Salanoemia sala",
            "Evergreen rainforest fringes, bamboo thickets",
            "Assam, Southern India, Southeast Asia",
            "Maculate Lancer with crisp hyaline spots and rapid skipping flight around bamboo fringes.",
            "dataset/train/123_Salanoemia_sala/1230001.jpg"
        ));

        METADATA.put(Species.SPECIES_124, new Details(
            "124", "Brown Forest Bob", "Scobura woolletti", "Hesperiidae",
            "Scobura", "Scobura woolletti",
            "Dark forest understorey, resting on low foliage",
            "Assam, Northeast India, Myanmar, Borneo",
            "Forest bob skipper dwelling in the lowest, darkest stratum of the wet evergreen jungle.",
            "dataset/train/124_Scobura_woolletti/1240001.jpg"
        ));

        METADATA.put(Species.SPECIES_125, new Details(
            "125", "Baby Swift", "Polytremis minuta", "Hesperiidae",
            "Polytremis", "Polytremis minuta",
            "Grassy forest openings, damp soil along streams",
            "Assam, Eastern Himalayas, Indo-China",
            "Miniature swift skipper with pale hyaline markings, completing the regional Assam Lepidoptera survey.",
            "dataset/train/125_Polytremis_minuta/1250001.jpg"
        ));
    }

    public static Details getDetails(Species species) {
        if (species == null) return null;
        return METADATA.get(species);
    }

    public static Details getDetailsById(String id) {
        Species s = Species.getById(id);
        return s != null ? getDetails(s) : null;
    }
}
