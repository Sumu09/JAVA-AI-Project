package com.butterfly.classifier;

import java.util.HashMap;
import java.util.Map;

/**
 * Rich scientific metadata and classification details for all 80 supported butterfly species.
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
            "dataset/train/012_Ampittia_dioscorides/0120001.jpg"
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
            "dataset/train/017_Athyma_perius/0170001.jpg"
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
            "dataset/train/030_Elymnias_hypermnestra_undularis/0300001.jpg"
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
            "dataset/train/032_Ethope_himachala/0320001.jpg"
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
            "dataset/train/037_Halpe_porus_porus/0370001.jpg"
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
            "dataset/train/039_Hasora_badra/0390001.jpg"
        ));

        METADATA.put(Species.SPECIES_040, new Details(
            "040", "Purple Sapphire", "Heliophorus epicles latilimbata", "Lycaenidae",
            "Heliophorus", "Heliophorus epicles latilimbata",
            "Tropical and subtropical forest edges, grasslands, and flowering canopies",
            "Indo-Malayan, Oriental, and South Asian bioregions",
            "Distinctive butterfly species belonging to the Lycaenidae family. Exhibiting specialized wing markings and high visual acuity.",
            "dataset/train/040_Heliophorus_epicles_latilimbata/0400001.jpg"
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
            "dataset/train/043_Jamides_elpis_pseudelpis/0430001.jpg"
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
            "dataset/train/045_Lethe_mekara_mekara/0450001.jpg"
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
            "dataset/train/048_Loxura_atymnus_continentalis/0480001.jpg"
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
            "dataset/train/055_Ochus_subvittatus_subradiatus/0550001.jpg"
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
            "dataset/train/063_Prosotas_dubiosa_indica/0630001.jpg"
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
            "dataset/train/076_Telicota_bambusae_bambusae/0760001.jpg"
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
            "081", "Basar Duke", "Euthalia zubeengargi", "Nymphalidae",
            "Euthalia", "Euthalia zubeengargi",
            "Montane subtropical rainforests, rocky streamsides, and moist evergreen canopies",
            "Eastern Himalayas, Northeast India (Arunachal Pradesh, Assam)",
            "A newly discovered Duke butterfly species (Basar Duke) discovered in Basar, Arunachal Pradesh, named in honor of cultural and musical icon Zubeen Garg. Features stunning olive-green forewings marked by prominent white arcs and dark apical shading.",
            "dataset/train/081_Euthalia_zubeengargi/0810001.jpg"
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
