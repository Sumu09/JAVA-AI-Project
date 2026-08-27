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
    SPECIES_010("010", "Vanessa cardui", "Painted Lady");

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
