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
    SPECIES_081("081", "Euthalia zubeengargi", "Zubeen's Baron"),
    SPECIES_082("082", "Papilio elephenor", "Yellow-crested Spangle"),
    SPECIES_083("083", "Papilio paradoxa", "Great Blue Mime"),
    SPECIES_084("084", "Papilio bootes", "Tailed Redbreast"),
    SPECIES_085("085", "Papilio slateri", "Blue-striped Mime"),
    SPECIES_086("086", "Lamproptera curius", "White Dragontail"),
    SPECIES_087("087", "Lamproptera meges", "Green Dragontail"),
    SPECIES_088("088", "Meandrusa payeni", "Yellow Gorgon"),
    SPECIES_089("089", "Meandrusa lachinus", "Brown Gorgon"),
    SPECIES_090("090", "Byasa crassipes", "Black Windmill"),
    SPECIES_091("091", "Byasa nevilli", "Nevill's Windmill"),
    SPECIES_092("092", "Byasa polla", "De Nicéville's Windmill"),
    SPECIES_093("093", "Graphium agetes", "Fourbar Swallowtail"),
    SPECIES_094("094", "Graphium aristeus", "Chain Swordtail"),
    SPECIES_095("095", "Graphium macareus", "Lesser Zebra"),
    SPECIES_096("096", "Graphium xenocles", "Great Zebra"),
    SPECIES_097("097", "Losaria doubledayi", "Common Clubtail"),
    SPECIES_098("098", "Teinopalpus imperialis", "Kaiser-i-Hind"),
    SPECIES_099("099", "Elymnias peali", "Peal's Palmfly"),
    SPECIES_100("100", "Euthalia telchinia", "Blue Baron"),
    SPECIES_101("101", "Charaxes delphis", "Jewelled Nawab"),
    SPECIES_102("102", "Pantoporia assamica", "Conjoined Lascar"),
    SPECIES_103("103", "Pantoporia bieti", "Tytler's Lascar"),
    SPECIES_104("104", "Chersonesia rahria", "Wavy Maplet"),
    SPECIES_105("105", "Athyma ranga", "Blackvein Sergeant"),
    SPECIES_106("106", "Athyma pravara", "Unbroken Sergeant"),
    SPECIES_107("107", "Athyma punctata", "White-bordered Sergeant"),
    SPECIES_108("108", "Polyura schreiber", "Blue Nawab"),
    SPECIES_109("109", "Tajuria maculata", "Spotted Royal"),
    SPECIES_110("110", "Tajuria cippus", "Peacock Royal"),
    SPECIES_111("111", "Pithecops fulgens", "Blue Quaker"),
    SPECIES_112("112", "Shijimia moorei", "Moore's Cupid"),
    SPECIES_113("113", "Arhopala silhetensis", "Sylhet Oakblue"),
    SPECIES_114("114", "Arhopala oenea", "Hewitson's Dull Oakblue"),
    SPECIES_115("115", "Simiskina phalena", "Broad-branded Brilliant"),
    SPECIES_116("116", "Udara selma", "Bi-coloured Hedge Blue"),
    SPECIES_117("117", "Poritia hewitsoni", "Common Gem"),
    SPECIES_118("118", "Capila pieridoides", "White Dawnfly"),
    SPECIES_119("119", "Pyroneura margherita", "Yellow-vein Lancer"),
    SPECIES_120("120", "Darpa pteria", "Snowy Angle"),
    SPECIES_121("121", "Hidari bhawani", "Veined Palmer"),
    SPECIES_122("122", "Plastingia naga", "Chequered Lancer"),
    SPECIES_123("123", "Salanoemia sala", "Maculate Lancer"),
    SPECIES_124("124", "Scobura woolletti", "Brown Forest Bob"),
    SPECIES_125("125", "Polytremis minuta", "Baby Swift");

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
