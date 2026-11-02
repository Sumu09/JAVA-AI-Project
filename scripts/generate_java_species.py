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
    'Thoressa': 'Hesperiidae', 'Troides': 'Papilionidae', 'Yasuda': 'Lycaenidae',
    'Euthalia': 'Nymphalidae', 'Actias': 'Saturniidae', 'Attacus': 'Saturniidae',
    'Manduca': 'Sphingidae', 'Acherontia': 'Sphingidae', 'Hyalophora': 'Saturniidae',
    'Antheraea': 'Saturniidae', 'Samia': 'Saturniidae',
    'Lamproptera': 'Papilionidae', 'Meandrusa': 'Papilionidae', 'Byasa': 'Papilionidae',
    'Losaria': 'Papilionidae', 'Teinopalpus': 'Papilionidae', 'Pantoporia': 'Nymphalidae',
    'Chersonesia': 'Nymphalidae', 'Polyura': 'Nymphalidae', 'Tajuria': 'Lycaenidae',
    'Pithecops': 'Lycaenidae', 'Shijimia': 'Lycaenidae', 'Arhopala': 'Lycaenidae',
    'Simiskina': 'Lycaenidae', 'Udara': 'Lycaenidae', 'Poritia': 'Lycaenidae',
    'Capila': 'Hesperiidae', 'Pyroneura': 'Hesperiidae', 'Darpa': 'Hesperiidae',
    'Hidari': 'Hesperiidae', 'Plastingia': 'Hesperiidae', 'Salanoemia': 'Hesperiidae',
    'Scobura': 'Hesperiidae', 'Polytremis': 'Hesperiidae'
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
    '079': 'Golden Birdwing', '080': 'Three-spot Silverstreak',
    '081': "Zubeen's Baron",
    '082': 'Yellow-crested Spangle', '083': 'Great Blue Mime', '084': 'Tailed Redbreast',
    '085': 'Blue-striped Mime', '086': 'White Dragontail', '087': 'Green Dragontail',
    '088': 'Yellow Gorgon', '089': 'Brown Gorgon', '090': 'Black Windmill',
    '091': "Nevill's Windmill", '092': "De Nicéville's Windmill", '093': 'Fourbar Swallowtail',
    '094': 'Chain Swordtail', '095': 'Lesser Zebra', '096': 'Great Zebra',
    '097': 'Common Clubtail', '098': 'Kaiser-i-Hind', '099': "Peal's Palmfly",
    '100': 'Blue Baron', '101': 'Jewelled Nawab', '102': 'Conjoined Lascar',
    '103': "Tytler's Lascar", '104': 'Wavy Maplet', '105': 'Blackvein Sergeant',
    '106': 'Unbroken Sergeant', '107': 'White-bordered Sergeant', '108': 'Blue Nawab',
    '109': 'Spotted Royal', '110': 'Peacock Royal', '111': 'Blue Quaker',
    '112': "Moore's Cupid", '113': 'Sylhet Oakblue', '114': "Hewitson's Dull Oakblue",
    '115': 'Broad-branded Brilliant', '116': 'Bi-coloured Hedge Blue', '117': 'Common Gem',
    '118': 'White Dawnfly', '119': 'Yellow-vein Lancer', '120': 'Snowy Angle',
    '121': 'Veined Palmer', '122': 'Chequered Lancer', '123': 'Maculate Lancer',
    '124': 'Brown Forest Bob', '125': 'Baby Swift'
}

SPECIAL_HABITATS = {
    '081': ("Panbari Reserve Forest, lowland wet evergreen rainforest understorey, Golaghat / Kaziranga landscape",
            "Endemic to Assam, Northeast India (Indo-Burma biodiversity hotspot)",
            "Discovered and described in 2024 from the Panbari Reserve Forest in Assam. Named in honor of cultural icon Zubeen Garg. Cryptic understorey dweller with rapid flight and distinct dorsal-ventral pattern."),
    '082': ("Primary tropical rainforests, foothills, and damp river banks of Assam",
            "Endemic to Northeast India (Assam, Meghalaya) and adjacent Myanmar",
            "Extremely rare swallowtail featuring prominent yellow-crested scaling on dark forewings and spatulate hindwing tails."),
    '083': ("Dense evergreen rainforest canopies and wet lowland forest corridors",
            "Assam, Northeast India, Sundaland, and Indo-China",
            "Magnificent mimic of Euploea crows, displaying deep iridescent blue gloss across its broad wings."),
    '084': ("Subtropical montane forests, moist stream beds, and bamboo thickets",
            "Eastern Himalayas, Assam, Nagaland, and northern Myanmar",
            "Distinctive swallowtail with bright red basal patches on ventral surfaces and spatulate tails."),
    '085': ("Dense evergreen forests and forest paths, mimics Danaine crows",
            "Assam, Meghalaya, Northeast India to Vietnam and Sundaland",
            "Remarkable mimic of Euploea radamanthus featuring crisp blue-white radial stripes on velvety black wings."),
    '086': ("Fast-flowing rocky streams and clearings in humid tropical rainforests",
            "Assam, Arunachal Pradesh, Northeast India, Southeast Asia",
            "Peculiar miniature swallowtail with transparent glass-like wing windows and elongated dragonfly-like tails."),
    '087': ("Sunlit riparian corridors and gravel shores of forest streams",
            "Northeast India (Assam, Cachar), Myanmar, Malaysia, Indonesia",
            "Brilliant emerald-banded dragontail adapted for high-speed hovering and rapid darting over forest rapids."),
    '088': ("High sub-Himalayan forest canopies, ridge tops, and sun-warmed peaks",
            "Assam, Sikkim, Arunachal Pradesh, Southeast Asia",
            "Striking sickle-winged swallowtail with bright saffron-yellow ground color and jagged wing outlines."),
    '089': ("Dense oak-laurel forests and cloud forest ridges",
            "Eastern Himalayas, Assam hill tracts, Myanmar",
            "Cryptic brown swallowtail mimicking dried leaves when at rest in deep montane forest canopies."),
    '090': ("Moist montane forests and steep wooded valleys",
            "Assam, Manipur, Nagaland, northern Myanmar",
            "Heavy-bodied black windmill swallowtail with crimson body markings and spatulate tails."),
    '091': ("Deep riverine gorges, primary evergreen forests",
            "Assam, Arunachal Pradesh, SW China, Myanmar",
            "Rare windmill species documented along isolated forest river corridors in Upper Assam."),
    '092': ("Subtropical forest tracts and flowering ravines",
            "Assam, Nagaland, Manipur, Myanmar",
            "Rare aristolochia-feeding windmill with bright white submarginal spots on velvety wings."),
    '093': ("Sandy riverbeds, damp forest clearings, and riparian margins",
            "Assam, Sikkim, Northeast India, Indo-China",
            "Elongated swordtail with pale greenish-white wings traversed by four distinct dark transverse bars."),
    '094': ("Deciduous to semi-evergreen forest margins and river banks",
            "Assam, Western Ghats, Indo-Malayan realm to Australasia",
            "Fast-flying swordtail decorated with chained rows of dark spots and needle-sharp hindwing tails."),
    '095': ("Lowland evergreen and semi-evergreen forests, damp patches on paths",
            "Assam, Sikkim, Southeast Asia",
            "Zebra-patterned swallowtail mimicking milkweed butterflies while mud-puddling on wet sand."),
    '096': ("Subtropical forest riverbeds, mud-puddling sites in sunny clearings",
            "Assam, Eastern Himalayas, Myanmar, Thailand",
            "Large, striking black and cream-striped zebra swallowtail of sub-Himalayan forest streams."),
    '097': ("Humid lowland rainforests, forest understorey, and stream courses",
            "Assam, Northeast India, Myanmar, Malay Peninsula",
            "Clubtail swallowtail displaying crimson thoracic patches and prominent spatulate wing clubs."),
    '098': ("High montane broadleaf canopy, cloud forest ridges above 2,000 meters",
            "Eastern Himalayas, Assam hill ranges, Arunachal Pradesh, Vietnam",
            "The legendary Kaiser-i-Hind, one of the world's most revered swallowtails with brilliant iridescent green scales and double tails."),
    '099': ("Deep shade of bamboo brakes, riverine evergreen forests of Upper Assam",
            "Extremely rare endemic to Assam (Sibsagar, Margherita) and Nagaland",
            "One of the rarest butterflies in the world, discovered in Margherita, Assam by S.E. Peal. Highly shade-loving."),
    '100': ("Wet evergreen forest undergrowth, decaying fruit along shaded trails",
            "Assam, Sikkim, Meghalaya, Myanmar",
            "Magnificent forest nymphalid where the male possesses an intense electric cobalt-blue border on deep brown wings."),
    '101': ("Dense tropical rainforest canopy, sap oozing trees and ridge tops",
            "Assam, Meghalaya, Southeast Asia to Borneo and Sumatra",
            "The Jewelled Nawab features shimmering mother-of-pearl undersides with delicate crimson and yellow markings."),
    '102': ("Shaded stream corridors, primary evergreen forest undergrowth",
            "Endemic to Assam and neighbouring tracts of Northeast India",
            "Rare endemic lascar featuring joined orange bands on the forewing, adapted for low gliding flight."),
    '103': ("Montane forest paths and bamboo clearings",
            "Assam, Nagaland, Manipur, SW China",
            "High-elevation lascar with crisp black-and-white bands and delicate yellow margins."),
    '104': ("Subcanopy of lowland dipterocarp and wet evergreen rainforests of Assam",
            "Assam, Northeast India, Sundaland",
            "Exquisite orange maplet with undulating transverse lines resembling delicate contour maps."),
    '105': ("Damp forest clearings, waterfalls, and sunlit stream rocks",
            "Assam, Western Ghats, Eastern Himalayas, Indo-China",
            "Blackvein Sergeant with crisp white longitudinal bands framed by rich velvet black margins."),
    '106': ("Evergreen forest trails and forest margins",
            "Assam, Northeast India, Southeast Asia",
            "Unbroken Sergeant distinguished by a continuous, unbroken white discal band across both wings."),
    '107': ("Primary sub-Himalayan forest trails and wet understory",
            "Assam, Eastern Himalayas, Myanmar, Southern China",
            "Rare sergeant characterized by wide white borders and distinct postdiscal white spots."),
    '108': ("High rainforest canopy and sunlit tree crowns",
            "Assam, Western Ghats, Indo-Malayan bioregions",
            "Blue Nawab with a heavy, robust build, turquoise-blue central patch, and powerful, aggressive flight."),
    '109': ("Tree tops with mistletoe (Loranthaceae), subcanopy in dense forests",
            "Assam, Sikkim, Myanmar, Peninsular Malaysia, Borneo",
            "Rare spotted lycaenid royal with bold black spots beneath gleaming silver-grey undersides."),
    '110': ("Forest canopy, gardens with mistletoe and flowering trees",
            "Throughout Assam and South/Southeast Asia",
            "Peacock Royal displays shimmering peacock-blue uppersides and delicate orange-crowned tails."),
    '111': ("Deep shaded understorey in primary evergreen rainforest",
            "Assam, Meghalaya, Nagaland, Myanmar",
            "Tiny, elusive lycaenid characterized by brilliant shining blue dorsal scales and spotless pure white ventral surfaces."),
    '112': ("Rocky stream beds, damp sandbanks in subtropical forests",
            "Assam, Eastern Himalayas, China, Japan",
            "Delicate cupid lycaenid adapted to rocky riparian clearings with complex ventral ocelli."),
    '113': ("Lowland wet evergreen forests, oak and dipterocarp undergrowth",
            "Assam (Sylhet historical tract, Cachar), Bangladesh, Myanmar",
            "Cryptic oakblue named after the historical Sylhet/Cachar tract of Assam, displaying deep purple gloss."),
    '114': ("Shaded evergreen understorey, wet forest ravines",
            "Assam, Sikkim, Myanmar",
            "Dull oakblue adapted for deep camouflage amongst fallen leaves, with bronze-tinged dorsal reflection."),
    '115': ("Dense tropical rainforest undergrowth, shaded ravines",
            "Assam, Myanmar, Thailand, Malaysia",
            "Poritiine lycaenid with broad velvety scent brands in males and intense metallic blue-purple reflection."),
    '116': ("Subtropical forest paths, damp gravel beside mountain brooks",
            "Assam, Eastern Himalayas, Southeast Asia",
            "Bi-coloured Hedge Blue with delicate frosted blue uppersides and fine peppered ventral speckling."),
    '117': ("Sunlit clearings, forest borders, and secondary evergreen growth",
            "Assam, Eastern Himalayas, Indo-China",
            "Brilliant gem lycaenid whose emerald-green or sky-blue dorsal luster flashes when basking."),
    '118': ("Deep evergreen forest undergrowth, crepuscular flights at dawn/dusk",
            "Assam, Meghalaya, Eastern Himalayas, Indo-China",
            "Large, striking skipper flying actively at dusk and dawn with broad white-bordered wings."),
    '119': ("Dense lowland rainforests, bamboo brakes in Upper Assam",
            "Endemic type locality Margherita (Assam), Arunachal Pradesh",
            "Discovered at Margherita in Upper Assam, featuring distinctive radiant yellow wing veins."),
    '120': ("Moist shady forest tracks, resting beneath broad leaves",
            "Assam, Eastern Himalayas, Southeast Asia",
            "Snowy Angle skipper with stark snow-white ventral patches providing disruptive shadow camouflage."),
    '121': ("Lowland riverine forests, marshes, and bamboo groves",
            "Rare endemic of Assam (Golaghat, Kaziranga), Indo-China",
            "Veined Palmer skipper documented in the Brahmaputra floodplains, displaying stark pale veins on chocolate ground."),
    '122': ("Dense forest clearings, damp leaf litter along streams",
            "Assam, Nagaland, Southeast Asia to Borneo",
            "Chequered Lancer adorned with neat golden-yellow chequered spots across dark chocolate wings."),
    '123': ("Evergreen rainforest fringes, bamboo thickets",
            "Assam, Southern India, Southeast Asia",
            "Maculate Lancer with crisp hyaline spots and rapid skipping flight around bamboo fringes."),
    '124': ("Dark forest understorey, resting on low foliage",
            "Assam, Northeast India, Myanmar, Borneo",
            "Forest bob skipper dwelling in the lowest, darkest stratum of the wet evergreen jungle."),
    '125': ("Grassy forest openings, damp soil along streams",
            "Assam, Eastern Himalayas, Indo-China",
            "Miniature swift skipper with pale hyaline markings, completing the regional Assam Lepidoptera survey.")
}

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

    if id_str in SPECIAL_HABITATS:
        habitat, distribution, description = SPECIAL_HABITATS[id_str]
    elif num == 1:
        habitat = "Fields, meadows, gardens, & milkweed patches"
        distribution = "North, Central, & South America, Caribbean, Australia"
        description = "Famous for its multi-generational annual migration across North America. Bright orange wings framed by black borders and white dots serve as warning coloration."
        sample_img = "images/0010001.png"
    elif num == 2:
        habitat = "Tropical hammocks, rainforest margins, & botanical gardens"
        distribution = "South & Central America, West Indies, Florida, Texas"
        description = "Features distinctive elongated black wings with bright yellow zebra stripes. Feeds on pollen in addition to nectar."
        sample_img = "images/0020003.png"
    else:
        habitat = "Tropical and subtropical forest edges, grasslands, and flowering canopies"
        distribution = "Indo-Malayan, Oriental, and South Asian bioregions"
        description = f"Distinctive butterfly species belonging to the {family} family. Exhibiting specialized wing markings and high visual acuity."

    # Escape quotes
    description = description.replace('"', '\\"')
    habitat = habitat.replace('"', '\\"')
    distribution = distribution.replace('"', '\\"')

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
 * Rich scientific metadata and classification details for all supported species.
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

print(f"Generated Species.java and SpeciesInfo.java with all {len(labels)} species successfully!")
