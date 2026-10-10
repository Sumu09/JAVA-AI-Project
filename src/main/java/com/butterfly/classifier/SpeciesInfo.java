package com.butterfly.classifier;

import java.util.HashMap;
import java.util.Map;

/**
 * Rich scientific metadata and classification details for supported butterfly species.
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
            "001", "Monarch", "Danaus plexippus", "Nymphalidae", "Danaus", "D. plexippus",
            "Fields, meadows, gardens, & milkweed patches",
            "North, Central, & South America, Caribbean, Australia",
            "Famous for its multi-generational annual migration across North America. Bright orange wings framed by black borders and white dots serve as warning coloration to predators.",
            "images/0010001.png"
        ));

        METADATA.put(Species.SPECIES_002, new Details(
            "002", "Zebra Longwing", "Heliconius charitonius", "Nymphalidae", "Heliconius", "H. charitonius",
            "Tropical hammocks, rainforest margins, & botanical gardens",
            "South & Central America, West Indies, Florida, Texas",
            "Features distinctive elongated black wings with bright yellow zebra stripes. Uniquely feeds on pollen in addition to nectar, extending adult lifespan up to 6 months.",
            "images/0020003.png"
        ));

        METADATA.put(Species.SPECIES_003, new Details(
            "003", "Red Passion", "Heliconius erato", "Nymphalidae", "Heliconius", "H. erato",
            "Tropical forest margins, clearings, & secondary woodlands",
            "Central America down to Amazonian South America",
            "Showcases velvet black wings highlighted with vivid crimson red splash bands. Co-evolved alongside Heliconius melpomene in classic Müllerian evolutionary mimicry.",
            "images/0030001.png"
        ));

        METADATA.put(Species.SPECIES_004, new Details(
            "004", "Common Buckeye", "Junonia coenia", "Nymphalidae", "Junonia", "H. coenia",
            "Open sunny fields, pastures, coastal dunes, & roadsides",
            "North America, Bermuda, Cuba",
            "Recognized by large, striking target-like eyespots on both forewings and hindwings designed to startle avian predators.",
            "images/0040001.png"
        ));

        METADATA.put(Species.SPECIES_005, new Details(
            "005", "Small Copper", "Lycaena phlaeas", "Nymphalidae", "Lycaena", "L. phlaeas",
            "Heathland, dry grasslands, sunny wastes, & hillsides",
            "Holarctic region across Europe, Asia, North America, & North Africa",
            "A small, energetic butterfly with iridescent copper-orange forewings studded with dark spots and dark grey hindwings.",
            "images/0050001.png"
        ));

        METADATA.put(Species.SPECIES_006, new Details(
            "006", "Mourning Cloak", "Nymphalis antiopa", "Nymphalidae", "Nymphalis", "N. antiopa",
            "Deciduous forests, parks, river banks, & wooded valleys",
            "Eurasia and North America",
            "Striking dark maroon-purple wings bordered by a row of iridescent royal blue spots and a soft cream-yellow outer margin. Overwinters as an adult.",
            "images/0060007.png"
        ));

        METADATA.put(Species.SPECIES_007, new Details(
            "007", "Giant Swallowtail", "Papilio cresphontes", "Papilionidae", "Papilio", "P. cresphontes",
            "Citrus groves, forest edges, rocky ridges, & gardens",
            "North America, Central America, Caribbean",
            "The largest butterfly species in North America. Dark chocolate brown wings decorated with bright diagonal yellow stripes and yellow-centered wing tails.",
            "images/0070001.png"
        ));

        METADATA.put(Species.SPECIES_008, new Details(
            "008", "Cabbage White", "Pieris rapae", "Pieridae", "Pieris", "P. rapae",
            "Gardens, agricultural fields, meadows, & urban parks",
            "Worldwide across Europe, Asia, North America, & Australia",
            "Small white butterfly with dark grey wingtips and dark spots on forewings. Highly adaptable and frequent in flower gardens.",
            "images/0080001.png"
        ));

        METADATA.put(Species.SPECIES_009, new Details(
            "009", "Red Admiral", "Vanessa atalanta", "Nymphalidae", "Vanessa", "V. atalanta",
            "Moist woodlands, meadows, parks, orchards, & coastal bluffs",
            "Temperate Europe, Asia, North America",
            "Characterized by velvety dark brown wings highlighted by bright reddish-orange diagonal bands and white forewing spots.",
            "images/0090001.png"
        ));

        METADATA.put(Species.SPECIES_010, new Details(
            "010", "Painted Lady", "Vanessa cardui", "Nymphalidae", "Vanessa", "V. cardui",
            "Open country, clover fields, gardens, & alpine meadows",
            "Nearly worldwide except Antarctica and South America",
            "Renowned for multi-generational mass migrations across continents. Displays orange-brown patterned wings with white blotches on black tips.",
            "images/0100003.png"
        ));
    }

    public static Details getDetails(Species species) {
        return METADATA.get(species);
    }
}
