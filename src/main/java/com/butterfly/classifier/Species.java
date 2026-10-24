package com.butterfly.classifier;

public enum Species {
    SPECIES_001("001", "Danaus plexippus", "Monarch"),
    SPECIES_002("002", "Heliconius charitonius", "Zebra Longwing"),
    SPECIES_003("003", "Heliconius erato", "Red Passion"),
    SPECIES_004("004", "Junonia coenia", "Common Buckeye"),
    SPECIES_005("005", "Lycaena phlaeas", "Small Copper"),
    SPECIES_006("006", "Nymphalis antiopa", "Mourning Cloak"),
    SPECIES_007("007", "Papilio cresphontes", "Giant Swallowtail"),
    SPECIES_008("008", "Pieris rapae", "Cabbage White"),
    SPECIES_009("009", "Vanessa atalanta", "Red Admiral"),
    SPECIES_010("010", "Vanessa cardui", "Painted Lady"),
    SPECIES_011("011", "Aeromachus pygmaeus", "Pygmy Scrub Hopper"),
    SPECIES_012("012", "Ampittia dioscorides", "Bush Hopper"),
    SPECIES_013("013", "Ancema blanka minturna", "Minturn Silverstreak"),
    SPECIES_014("014", "Ancema ctesia ctesia", "Bi-spot Royal"),
    SPECIES_015("015", "Anthene emolus emolus", "Ciliate Blue"),
    SPECIES_016("016", "Anthene lycaenina lycambes", "Pointed Ciliate Blue"),
    SPECIES_017("017", "Athyma perius", "Common Sergeant"),
    SPECIES_018("018", "Badamia exclamationis", "Brown Awl"),
    SPECIES_019("019", "Burara jaina", "Orange Awlet"),
    SPECIES_020("020", "Caleta elna noliteia", "Elbowed Pierrot"),
    SPECIES_021("021", "Catochrysops strabo strabo", "Forget-me-not"),
    SPECIES_022("022", "Celaenorrhinus aurivittata aurivittata", "Yellow-banded Flat"),
    SPECIES_023("023", "Celaenorrhinus leucocera", "Common Spotted Flat"),
    SPECIES_024("024", "Cethosia cyane", "Leopard Lacewing"),
    SPECIES_025("025", "Charaxes bernardus hierax", "Tawny Rajah"),
    SPECIES_026("026", "Charaxes marmax marmax", "Yellow Rajah"),
    SPECIES_027("027", "Chilades lajus lajus", "Lime Blue"),
    SPECIES_028("028", "Choaspes benjaminii japonica", "Indian Awlking"),
    SPECIES_029("029", "Cupitha purreea purreea", "Wax Dart"),
    SPECIES_030("030", "Elymnias hypermnestra undularis", "Common Palmfly"),
    SPECIES_031("031", "Elymnias nesaea", "Tiger Palmfly"),
    SPECIES_032("032", "Ethope himachala", "Dusky Diadem"),
    SPECIES_033("033", "Gerosis phisara phisara", "Great Yellow Sailer"),
    SPECIES_034("034", "Graphium agamemnon", "Tailed Jay"),
    SPECIES_035("035", "Halpe aucma", "Gold-spotted Ace"),
    SPECIES_036("036", "Halpe kusala", "Plain Ace"),
    SPECIES_037("037", "Halpe porus porus", "Moore's Ace"),
    SPECIES_038("038", "Halpe zema zema", "Zema Ace"),
    SPECIES_039("039", "Hasora badra", "Common Awl"),
    SPECIES_040("040", "Heliophorus epicles latilimbata", "Purple Sapphire"),
    SPECIES_041("041", "Jamides caerulea", "Sky Blue"),
    SPECIES_042("042", "Jamides celeno", "Common Cerulean"),
    SPECIES_043("043", "Jamides elpis pseudelpis", "Glistening Cerulean"),
    SPECIES_044("044", "Lethe chandica flanona", "Angled Red Forester"),
    SPECIES_045("045", "Lethe mekara mekara", "Common Treebrown"),
    SPECIES_046("046", "Lethe satyavati", "Pallid Forester"),
    SPECIES_047("047", "Lethe vindhya vindhya", "Black Forester"),
    SPECIES_048("048", "Loxura atymnus continentalis", "Yamfly"),
    SPECIES_049("049", "Megisba malaya sikkima", "Malayan"),
    SPECIES_050("050", "Mooreana trichoneura pralaya", "Yellow Flat"),
    SPECIES_051("051", "Nacaduba kurava euplea", "Transparent 6-Line Blue"),
    SPECIES_052("052", "Neopithecops zalmora zalmora", "Common Quaker"),
    SPECIES_053("053", "Notocrypta curvifascia curvifascia", "Common Banded Demon"),
    SPECIES_054("054", "Notocrypta paralysos asawa", "Grass Demon"),
    SPECIES_055("055", "Ochus subvittatus subradiatus", "Tiger Hopper"),
    SPECIES_056("056", "Odontoptilum angulata angulata", "Chestnut Angle"),
    SPECIES_057("057", "Oriens gola pseudolus", "Common Dartlet"),
    SPECIES_058("058", "Papilio paris", "Paris Peacock"),
    SPECIES_059("059", "Pithauria stramineipennis", "Light Straw Ace"),
    SPECIES_060("060", "Potanthus pseudomaesa", "Indian Dart"),
    SPECIES_061("061", "Prosotas aluta coelestis", "Banded Lineblue"),
    SPECIES_062("062", "Prosotas bhutea", "Bhutya Lineblue"),
    SPECIES_063("063", "Prosotas dubiosa indica", "Tailless Lineblue"),
    SPECIES_064("064", "Prosotas nora ardates", "Common Lineblue"),
    SPECIES_065("065", "Pseudocoladenia dan fabia", "Fulvous Pied Flat"),
    SPECIES_066("066", "Psolos fuligo subfasciatus", "Coon"),
    SPECIES_067("067", "Remelana jangala ravata", "Chocolate Royal"),
    SPECIES_068("068", "Sarangesa dasahara dasahara", "Common Small Flat"),
    SPECIES_069("069", "Sebastonyma dolopia", "Tufted Ace"),
    SPECIES_070("070", "Seseria sambara sambara", "Notched Flat"),
    SPECIES_071("071", "Spindasis lohita himalayanus", "Long-banded Silverline"),
    SPECIES_072("072", "Surendra quercetorum quercetorum", "Common Acacia Blue"),
    SPECIES_073("073", "Tagiades dynamicus ravi", "Ravi Snow Flat"),
    SPECIES_074("074", "Tagiades gana gana", "Suffused Snow Flat"),
    SPECIES_075("075", "Tagiades litigiosa litigiosa", "Water Snow Flat"),
    SPECIES_076("076", "Telicota bambusae bambusae", "Dark Palm Dart"),
    SPECIES_077("077", "Telicota colon", "Pale Palm Dart"),
    SPECIES_078("078", "Thoressa cerata", "Northern Spangle"),
    SPECIES_079("079", "Troides aeacus", "Golden Birdwing"),
    SPECIES_080("080", "Yasuda tripunctata tripunctata", "Three-spot Silverstreak"),
    SPECIES_081("081", "Euthalia zubeengargi", "Basar Duke");

    private final String id;
    private final String scientificName;
    private final String commonName;

    Species(String id, String scientificName, String commonName) {
        this.id = id;
        this.scientificName = scientificName;
        this.commonName = commonName;
    }

    public String getId() {
        return id;
    }

    public String getScientificName() {
        return scientificName;
    }

    public String getCommonName() {
        return commonName;
    }

    public static Species getById(String id) {
        if (id == null) return null;
        for (Species s : values()) {
            if (s.getId().equalsIgnoreCase(id)) {
                return s;
            }
        }
        return null;
    }

    public static Species getByIndex(int index) {
        Species[] values = values();
        if (index >= 0 && index < values.length) {
            return values[index];
        }
        return null;
    }
}
