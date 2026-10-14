import os

with open('model/labels.txt') as f:
    labels = [l.strip() for l in f if l.strip()]

GENUS_TO_FAMILY = {
    'Danaus': 'Nymphalidae', 'Heliconius': 'Nymphalidae', 'Junonia': 'Nymphalidae',
    'Lycaena': 'Lycaenidae', 'Nymphalis': 'Nymphalidae', 'Papilio': 'Papilionidae',
    'Pieris': 'Pieridae', 'Vanessa': 'Nymphalidae', 'Aeromachus': 'Hesperiidae',
    'Ampittia': 'Hesperiidae', 'Ancema': 'Lycaenidae', 'Anthene': 'Lycaenidae',
    'Athyma': 'Nymphalidae', 'Badamia': 'Hesperiidae', 'Burara': 'Hesperiidae',
    'Caleta': 'Lycaenidae', 'Catochrysops': 'Lycaenidae', 'Celaenorrhinus': 'Hesperiidae',
    'Cethosia': 'Nymphalidae', 'Charaxes': 'Nymphalidae', 'Chilades': 'Lycaenidae',
    'Choaspes': 'Hesperiidae', 'Cupitha': 'Hesperiidae', 'Elymnias': 'Nymphalidae',
    'Ethope': 'Nymphalidae', 'Gerosis': 'Hesperiidae', 'Graphium': 'Papilionidae',
    'Halpe': 'Hesperiidae', 'Hasora': 'Hesperiidae', 'Heliophorus': 'Lycaenidae',
    'Jamides': 'Lycaenidae', 'Lethe': 'Nymphalidae', 'Loxura': 'Lycaenidae',
    'Megisba': 'Lycaenidae', 'Mooreana': 'Hesperiidae', 'Nacaduba': 'Lycaenidae',
    'Neopithecops': 'Lycaenidae', 'Notocrypta': 'Hesperiidae', 'Ochus': 'Hesperiidae',
    'Odontoptilum': 'Hesperiidae', 'Oriens': 'Hesperiidae', 'Pithauria': 'Hesperiidae',
    'Potanthus': 'Hesperiidae', 'Prosotas': 'Lycaenidae', 'Pseudocoladenia': 'Hesperiidae',
    'Psolos': 'Hesperiidae', 'Remelana': 'Lycaenidae', 'Sarangesa': 'Hesperiidae',
    'Sebastonyma': 'Hesperiidae', 'Seseria': 'Hesperiidae', 'Spindasis': 'Lycaenidae',
    'Surendra': 'Lycaenidae', 'Tagiades': 'Hesperiidae', 'Telicota': 'Hesperiidae',
    'Thoressa': 'Hesperiidae', 'Troides': 'Papilionidae', 'Yasuda': 'Lycaenidae'
}

COMMON_NAMES = {
    '001': 'Monarch', '002': 'Zebra Longwing', '003': 'Red Passion', '004': 'Common Buckeye',
    '005': 'Small Copper', '006': 'Mourning Cloak', '007': 'Giant Swallowtail', '008': 'Cabbage White',
    '009': 'Red Admiral', '010': 'Painted Lady', '011': 'Pygmy Scrub Hopper', '012': 'Bush Hopper',
    '013': 'Minturn Silverstreak', '014': 'Bi-spot Royal', '015': 'Ciliate Blue',
    '016': 'Pointed Ciliate Blue', '017': 'Common Sergeant', '018': 'Brown Awl',
    '019': 'Orange Awlet', '020': 'Elbowed Pierrot', '021': 'Forget-me-not',
    '022': 'Yellow-banded Flat', '023': 'Common Spotted Flat', '024': 'Leopard Lacewing',
    '025': 'Tawny Rajah', '026': 'Yellow Rajah', '027': 'Lime Blue',
    '028': 'Indian Awlking', '029': 'Wax Dart', '030': 'Common Palmfly',
    '031': 'Tiger Palmfly', '032': 'Dusky Diadem', '033': 'Great Yellow Sailer',
    '034': 'Tailed Jay', '035': 'Gold-spotted Ace', '036': 'Plain Ace',
    '037': "Moore's Ace", '038': 'Zema Ace', '039': 'Common Awl',
    '040': 'Purple Sapphire', '041': 'Sky Blue', '042': 'Common Cerulean',
    '043': 'Glistening Cerulean', '044': 'Angled Red Forester', '045': 'Common Treebrown',
    '046': 'Pallid Forester', '047': 'Black Forester', '048': 'Yamfly',
    '049': 'Malayan', '050': 'Yellow Flat', '051': 'Transparent 6-Line Blue',
    '052': 'Common Quaker', '053': 'Common Banded Demon', '054': 'Grass Demon',
    '055': 'Tiger Hopper', '056': 'Chestnut Angle', '057': 'Common Dartlet',
    '058': 'Paris Peacock', '059': 'Light Straw Ace', '060': 'Indian Dart',
    '061': 'Banded Lineblue', '062': 'Bhutya Lineblue', '063': 'Tailless Lineblue',
    '064': 'Common Lineblue', '065': 'Fulvous Pied Flat', '066': 'Coon',
    '067': 'Chocolate Royal', '068': 'Common Small Flat', '069': 'Tufted Ace',
    '070': 'Notched Flat', '071': 'Long-banded Silverline', '072': 'Common Acacia Blue',
    '073': 'Ravi Snow Flat', '074': 'Suffused Snow Flat', '075': 'Water Snow Flat',
    '076': 'Dark Palm Dart', '077': 'Pale Palm Dart', '078': 'Northern Spangle',
    '079': 'Golden Birdwing', '080': 'Three-spot Silverstreak'
}

# --- Generate Species.java ---
species_enum_entries = []
species_info_entries = []

for l in labels:
    parts = l.split('_')
    id_str = parts[0]
    num = int(id_str)
    
    if num <= 10:
        if num == 1:
            sci_name = "Danaus plexippus"
        elif num == 2:
            sci_name = "Heliconius charitonius"
        elif num == 3:
            sci_name = "Heliconius erato"
        elif num == 4:
            sci_name = "Junonia coenia"
        elif num == 5:
            sci_name = "Lycaena phlaeas"
        elif num == 6:
            sci_name = "Nymphalis antiopa"
        elif num == 7:
            sci_name = "Papilio cresphontes"
        elif num == 8:
            sci_name = "Pieris rapae"
        elif num == 9:
            sci_name = "Vanessa atalanta"
        elif num == 10:
            sci_name = "Vanessa cardui"
    else:
        sci_name = " ".join(parts[1:])
        
    common_name = COMMON_NAMES.get(id_str, sci_name)
    genus = sci_name.split()[0]
    family = GENUS_TO_FAMILY.get(genus, "Lepidoptera")
    
    enum_name = f"SPECIES_{id_str}"
    species_enum_entries.append(f'    {enum_name}("{id_str}", "{sci_name}", "{common_name}")')
    
    # Check if a sample image exists
    sample_img = f"dataset/train/{l}/{id_str}0001.jpg"
    if not os.path.exists(sample_img):
        sample_img = f"dataset/train/{l}/{id_str}0001.png"
    if not os.path.exists(sample_img):
        sample_img = f"images/{id_str}0001.png"

    habitat = "Tropical and subtropical forest edges, grasslands, and flowering canopies"
    distribution = "Indo-Malayan, Oriental, and South Asian bioregions"
    description = f"Distinctive butterfly species belonging to the {family} family. Exhibiting specialized wing markings and high visual acuity."
    
    if num == 1:
        habitat = "Fields, meadows, gardens, & milkweed patches"
        distribution = "North, Central, & South America, Caribbean, Australia"
        description = "Famous for its multi-generational annual migration across North America. Bright orange wings framed by black borders and white dots serve as warning coloration."
        sample_img = "images/0010001.png"
    elif num == 2:
        habitat = "Tropical hammocks, rainforest margins, & botanical gardens"
        distribution = "South & Central America, West Indies, Florida, Texas"
        description = "Features distinctive elongated black wings with bright yellow zebra stripes. Feeds on pollen in addition to nectar."
        sample_img = "images/0020003.png"

    species_info_entries.append(f'''        METADATA.put(Species.{enum_name}, new Details(
            "{id_str}", "{common_name}", "{sci_name}", "{family}",
            "{genus}", "{sci_name}",
            "{habitat}",
            "{distribution}",
            "{description}",
            "{sample_img}"
        ));''')

species_java = f'''package com.butterfly.classifier;

public enum Species {{
{",\n".join(species_enum_entries)};

    private final String id;
    private final String scientificName;
    private final String commonName;

    Species(String id, String scientificName, String commonName) {{
        this.id = id;
        this.scientificName = scientificName;
        this.commonName = commonName;
    }}

    public String getId() {{
        return id;
    }}

    public String getScientificName() {{
        return scientificName;
    }}

    public String getCommonName() {{
        return commonName;
    }}

    public static Species getById(String id) {{
        if (id == null) return null;
        for (Species s : values()) {{
            if (s.getId().equalsIgnoreCase(id)) {{
                return s;
            }}
        }}
        return null;
    }}

    public static Species getByIndex(int index) {{
        Species[] values = values();
        if (index >= 0 && index < values.length) {{
            return values[index];
        }}
        return null;
    }}
}}
'''

with open("src/main/java/com/butterfly/classifier/Species.java", "w") as f:
    f.write(species_java)

species_info_java = f'''package com.butterfly.classifier;

import java.util.HashMap;
import java.util.Map;

/**
 * Rich scientific metadata and classification details for all 80 supported butterfly species.
 */
public class SpeciesInfo {{

    public static class Details {{
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
                       String description, String sampleImagePath) {{
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
        }}
    }}

    private static final Map<Species, Details> METADATA = new HashMap<>();

    static {{
{"\n\n".join(species_info_entries)}
    }}

    public static Details getDetails(Species species) {{
        if (species == null) return null;
        return METADATA.get(species);
    }}

    public static Details getDetailsById(String id) {{
        Species s = Species.getById(id);
        return s != null ? getDetails(s) : null;
    }}
}}
'''

with open("src/main/java/com/butterfly/classifier/SpeciesInfo.java", "w") as f:
    f.write(species_info_java)

print("Generated Species.java and SpeciesInfo.java with all 80 species successfully!")
