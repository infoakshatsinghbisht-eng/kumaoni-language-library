"""
Script to expand kumaoni/culture/flora.py and kumaoni/culture/rituals.py
Adds 28 new ethnobotanical plants/trees and 27 new temple/ritual items.
"""

from pathlib import Path
import re

FLORA_FILE = Path("kumaoni/culture/flora.py")
RITUALS_FILE = Path("kumaoni/culture/rituals.py")

NEW_FLORA_SNIPPET = '''    # ==================== ADDITIONAL ETHNOBOTANICAL PLANTS & TREES ====================
    "utees": KumaoniPlant(
        id="utees",
        name_kumaoni="उतीस",
        name_roman="Utees",
        name_hindi="उतीस (हिमालयी एल्डर)",
        scientific_name="Alnus nepalensis",
        category="Himalayan Forest Tree",
        botanical_family="Betulaceae",
        habitat_altitude="1,000m – 2,600m",
        traditional_uses="Key agroforestry nitrogen fixer, prevents soil erosion along rivulets; seasoned wood used for gharat (watermill) gearing, bridge stringers, and light furniture.",
        spiritual_and_temple_significance="Protector tree of mountain water catchments, planted along holy naula recharge slopes.",
        cultural_folklore="Celebrated as the fastest healer of scarred mountain landslides."
    ),
    "semal": KumaoniPlant(
        id="semal",
        name_kumaoni="सेमल",
        name_roman="Semal",
        name_hindi="सेमल (रक्त शाल्मली)",
        scientific_name="Bombax ceiba",
        category="Sacred & Ritual Tree",
        botanical_family="Malvaceae",
        habitat_altitude="Sub-Himalayan valleys up to 1,500m",
        traditional_uses="Fiery crimson blossoms eaten as buds; silky seed-pod floss stuffed into ceremonial cushions; wood used for matchwood and traditional drum shells.",
        spiritual_and_temple_significance="Pure silky floss is hand-spun into sacred cotton wicks (Deewa baati) for temple lamps; large crimson flowers are offered to forest and gram devtas.",
        cultural_folklore="The herald of spring in lower valleys; attracts countless singing mountain birds."
    ),
    "toon": KumaoniPlant(
        id="toon",
        name_kumaoni="तूण",
        name_roman="Toon",
        name_hindi="तून (लाल देवदार / महोगनी)",
        scientific_name="Toona ciliata",
        category="Himalayan Forest Tree",
        botanical_family="Meliaceae",
        habitat_altitude="600m – 1,800m",
        traditional_uses="Termite-resistant, richly grained red timber crafted into traditional carved door-lintels (Kholi), wedding chests (Sandook), and musical instruments.",
        spiritual_and_temple_significance="Sacred architectural timber for sanctum doors and temple beams of Katyuri-era dewaals.",
        cultural_folklore="Treasured across generations as heirloom carpentry timber."
    ),
    "reetha": KumaoniPlant(
        id="reetha",
        name_kumaoni="रीठा",
        name_roman="Reetha",
        name_hindi="रीठा (फेनिल)",
        scientific_name="Sapindus mukorossi",
        category="Sacred & Ritual Tree",
        botanical_family="Sapindaceae",
        habitat_altitude="800m – 1,800m",
        traditional_uses="Natural herbal foaming saponin cleanser used since antiquity to wash fine hill pashmina, silk pithyaura, and hair.",
        spiritual_and_temple_significance="Mandatory natural cleanser used to polish temple brass and copper murtis, aarti thalis, and bells prior to festivals.",
        cultural_folklore="Immortalized in legends of pilgrimage shrines like Reetha Sahib in Champawat."
    ),
    "aanwla": KumaoniPlant(
        id="aanwla",
        name_kumaoni="आँवला",
        name_roman="Aanwla",
        name_hindi="आंवला (आमलकी)",
        scientific_name="Phyllanthus emblica",
        category="Sacred & Ritual Tree",
        botanical_family="Phyllanthaceae",
        habitat_altitude="Foothills to 1,500m",
        traditional_uses="Rich source of Vitamin C, digestive tonics, pickled preserves (Morabba), triphala component.",
        spiritual_and_temple_significance="Revered as embodiment of Lord Vishnu; ritually worshipped during Amla Navami; family picnics and community feasts held beneath its shade.",
        cultural_folklore="Symbol of longevity, rejuvenation, and divine health."
    ),
    "harad": KumaoniPlant(
        id="harad",
        name_kumaoni="हरड़",
        name_roman="Harad",
        name_hindi="हरड़ (हरीतकी)",
        scientific_name="Terminalia chebula",
        category="Medicinal & Aromatic Flora",
        botanical_family="Combretaceae",
        habitat_altitude="Sub-Himalayan tracts to 1,500m",
        traditional_uses="Foundational medicinal fruit of Himalayan Ayurveda; detoxifier, rejuvenator, and digestive cure.",
        spiritual_and_temple_significance="Sacred fruit held in the right palm of the Medicine Buddha; consecrated in Ayurvedic medicinal healing shrines.",
        cultural_folklore="Hailed as the mother of Ayurvedic herbs in Pahari folklore."
    ),
    "baheda": KumaoniPlant(
        id="baheda",
        name_kumaoni="बहेड़ा",
        name_roman="Baheda",
        name_hindi="बहेड़ा (विभीतक)",
        scientific_name="Terminalia bellirica",
        category="Medicinal & Aromatic Flora",
        botanical_family="Combretaceae",
        habitat_altitude="Foothills to 1,400m",
        traditional_uses="Respiratory and digestive remedy; third pillar of Triphala.",
        spiritual_and_temple_significance="Constituent of sacred medicinal temple decoctions and herbal hawan mixtures.",
        cultural_folklore="Ancient forest sentinel tree sheltering bird life."
    ),
    "kapur_kachari": KumaoniPlant(
        id="kapur_kachari",
        name_kumaoni="कपूर कचरी",
        name_roman="Kapur Kachari",
        name_hindi="कपूर कचरी",
        scientific_name="Hedychium spicatum",
        category="Medicinal & Aromatic Flora",
        botanical_family="Zingiberaceae",
        habitat_altitude="1,500m – 2,800m",
        traditional_uses="Intensely aromatic ginger-lily root powdered into herbal insect repellents, hair wash, and soothing lung remedies.",
        spiritual_and_temple_significance="Indispensable fragrant ingredient of Kumaoni Hawan Samagri and temple dhoop incenses.",
        cultural_folklore="Known for spreading fragrant mountain aroma across hill breezes."
    ),
    "thuner": KumaoniPlant(
        id="thuner",
        name_kumaoni="थुनेर",
        name_roman="Thuner",
        name_hindi="थुनेर (हिमालयी यव)",
        scientific_name="Taxus wallichiana",
        category="Himalayan Forest Tree",
        botanical_family="Taxaceae",
        habitat_altitude="2,000m – 3,200m",
        traditional_uses="Red bark brewed into soothing pink tea; botanical source of anticancer taxol; durable red wood for shrine idols.",
        spiritual_and_temple_significance="Sacred high-altitude tree associated with yogic longevity and Shiva's penance groves.",
        cultural_folklore="Revered in alpine folklore as a rare medicinal guardian of bugyal margins."
    ),
    "bithar": KumaoniPlant(
        id="bithar",
        name_kumaoni="बिथर / जूनीपर",
        name_roman="Bithar / Juniper",
        name_hindi="बिथर / धूप (हिमालयी जूनीपर)",
        scientific_name="Juniperus indica",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Cupressaceae",
        habitat_altitude="3,000m – 4,500m",
        traditional_uses="Aromatic evergreen foliage sun-dried into sacred mountain dhoop smudge sticks.",
        spiritual_and_temple_significance="Supreme purification smudge burnt at high Himalayan shrines, Milam valley gompas, and Bhotia spirit invocations.",
        cultural_folklore="Its fragrant white smoke is believed to cleanse all atmospheric negativity and invite mountain devtas."
    ),
    "bhaang": KumaoniPlant(
        id="bhaang",
        name_kumaoni="भांग",
        name_roman="Bhaang",
        name_hindi="भांग (हिमालयी सन)",
        scientific_name="Cannabis sativa",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Cannabaceae",
        habitat_altitude="1,000m – 2,500m",
        traditional_uses="Nutrient-dense non-narcotic seeds roasted for iconic Bhaang ki Chutney; stem bast fibre spun into rough ropes, shoes, and sitting mats (Mosht).",
        spiritual_and_temple_significance="Leaves sacred to Lord Shiva; offered on Shivratri and during Shravan Somvars at Jageshwar and Bagnath.",
        cultural_folklore="Celebrated staple of Kumaoni winter nutrition and fiber culture."
    ),
    "bhangjeera": KumaoniPlant(
        id="bhangjeera",
        name_kumaoni="भांगजीरा",
        name_roman="Bhangjeera",
        name_hindi="भांगजीरा (जंगली पेरिला)",
        scientific_name="Perilla frutescens",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Lamiaceae",
        habitat_altitude="1,200m – 2,200m",
        traditional_uses="Nutty aromatic seeds roasted with salt and green chillies into signature mountain chutneys; oil used for cooking and lanterns.",
        spiritual_and_temple_significance="Used in traditional festive offerings during autumn harvest celebrations.",
        cultural_folklore="Signature seasoning providing warmth during bitter Himalayan winters."
    ),
    "sisoon": KumaoniPlant(
        id="sisoon",
        name_kumaoni="सिसूण / बिच्छू घास",
        name_roman="Sisoon / Bichhu Ghas",
        name_hindi="सिसूण / कंडाली (बिच्छू घास)",
        scientific_name="Urtica dioica",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Urticaceae",
        habitat_altitude="1,000m – 3,000m",
        traditional_uses="Iron-rich tender shoots boiled and mashed into medicinal saag (Kafli); leaves used externally for joint pains and rheumatism; strong stem fiber for cords.",
        spiritual_and_temple_significance="Celebrated in the historic Kandali festival of the Rung/Bhotia community of Pithoragarh.",
        cultural_folklore="Legendary disciplinary deterrent in hill households and schools; also prized as nourishing mountain food."
    ),
    "gethi": KumaoniPlant(
        id="gethi",
        name_kumaoni="गेठी",
        name_roman="Gethi",
        name_hindi="गेठी (हवाई रतालू)",
        scientific_name="Dioscorea bulbifera",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Dioscoreaceae",
        habitat_altitude="800m – 2,000m",
        traditional_uses="Aerial yams boiled, peeled, and sautéed with hill spices; carbohydrate and mineral reserve during harsh winters.",
        spiritual_and_temple_significance="Sacred uncultivated forest food consumed during ascetic fasts and Ekadashis.",
        cultural_folklore="Celebrated in rural Kumaon as the famine-rescuing gift of the mountain forests."
    ),
    "tarur": KumaoniPlant(
        id="tarur",
        name_kumaoni="तरुड़",
        name_roman="Tarur",
        name_hindi="तरुड़ (पहाड़ी रतालू)",
        scientific_name="Dioscorea alata",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Dioscoreaceae",
        habitat_altitude="800m – 1,800m",
        traditional_uses="Giant subterranean tubers excavated and roasted in hearth embers or fried into crispy chips.",
        spiritual_and_temple_significance="Mandatory sacred tuber consumed across Kumaon on Makar Sankranti / Ghughuti Tyar.",
        cultural_folklore="A winter solstice culinary ritual binding families together."
    ),
    "gaderi": KumaoniPlant(
        id="gaderi",
        name_kumaoni="गड़ेरी",
        name_roman="Gaderi",
        name_hindi="गड़ेरी (विशाल पहाड़ी अरबी)",
        scientific_name="Colocasia esculenta",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Araceae",
        habitat_altitude="600m – 2,200m",
        traditional_uses="Staple winter root crop cooked in iron kadhais with fermented curd, jakhya, and jambu.",
        spiritual_and_temple_significance="Prepared in grand community bhandaras and feast offerings during winter festivals.",
        cultural_folklore="The undisputed king of winter vegetables in Kumaoni households."
    ),
    "linguda": KumaoniPlant(
        id="linguda",
        name_kumaoni="लिंगुड़ा",
        name_roman="Linguda",
        name_hindi="लिंगुड़ा (पहाड़ी फर्न)",
        scientific_name="Diplazium esculentum",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Athyriaceae",
        habitat_altitude="1,200m – 2,600m",
        traditional_uses="Young tender fiddlehead fern fronds harvested along tumbling brooks; sautéed into delectable spring delicacies.",
        spiritual_and_temple_significance="Symbolizes the awakening of forest life after the retreat of winter snows.",
        cultural_folklore="Treasured wild foraging spring bounty."
    ),
    "maalu": KumaoniPlant(
        id="maalu",
        name_kumaoni="माळू",
        name_roman="Maalu",
        name_hindi="माळू (पत्तल वाली लता)",
        scientific_name="Bauhinia vahlii",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Fabaceae",
        habitat_altitude="400m – 1,600m",
        traditional_uses="Enormous tough, flexible leaves stitched together with bamboo splints to craft eco-friendly dining plates (Pattal) and bowls (Dona); bark gives strong rope fiber.",
        spiritual_and_temple_significance="Essential plateware for all traditional Kumaoni temple bhandaras, weddings, and rituals.",
        cultural_folklore="The historical zero-waste packaging of the Himalayas."
    ),
    "guchhi": KumaoniPlant(
        id="guchhi",
        name_kumaoni="गुच्छी",
        name_roman="Guchhi",
        name_hindi="गुच्छी (हिमालयी मोरेल मशरूम)",
        scientific_name="Morchella esculenta",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Morchellaceae",
        habitat_altitude="1,800m – 3,500m",
        traditional_uses="Subterranean spongy wild morel gathered under oak and pine canopy; revered for rich earthy flavor and high medicinal value.",
        spiritual_and_temple_significance="Considered a divine forest gift appearing mysteriously following spring lightning strikes and melting snow.",
        cultural_folklore="Known as the prized 'black diamond' of mountain foragers."
    ),
    "chyoon": KumaoniPlant(
        id="chyoon",
        name_kumaoni="च्यूँ",
        name_roman="Chyoon",
        name_hindi="च्यूं (जंगली खाद्य मशरूम)",
        scientific_name="Pleurotus / Agaricus spp.",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Pleurotaceae",
        habitat_altitude="1,200m – 2,800m",
        traditional_uses="Wild edible mushrooms harvested from fallen oak trunks ('Banjh chyoon') during monsoon rains.",
        spiritual_and_temple_significance="Harvested with deep ecological reverence by villagers adhering to ancestral identification rules.",
        cultural_folklore="A monsoon forest foraging delicacy celebrated in hill lore."
    ),
    "daam": KumaoniPlant(
        id="daam",
        name_kumaoni="दाम / दारू",
        name_roman="Daam",
        name_hindi="दाड़िम (जंगली अनार)",
        scientific_name="Punica granatum (Wild)",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Lythraceae",
        habitat_altitude="900m – 2,000m",
        traditional_uses="Wild small sour pomegranates sun-dried into tangy anardana seeds used as souring agent in Pahari gravies.",
        spiritual_and_temple_significance="Branches and fruits offered in Devi and Ganesh rituals symbolizing fertility and prosperity.",
        cultural_folklore="Featured in songs describing steep hill slopes where wild pomegranate blooms."
    ),
    "aadu": KumaoniPlant(
        id="aadu",
        name_kumaoni="आड़ू",
        name_roman="Aadu",
        name_hindi="आड़ू (पीच)",
        scientific_name="Prunus persica",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Rosaceae",
        habitat_altitude="1,200m – 2,400m",
        traditional_uses="Juicy summer stone fruit; orchards of Ramgarh and Mukteshwar.",
        spiritual_and_temple_significance="Early pink blossoms herald spring and are placed at shrines on Phool Dei.",
        cultural_folklore="Centerpiece of Kumaon's fruit belt economy."
    ),
    "khumaani": KumaoniPlant(
        id="khumaani",
        name_kumaoni="खुमानी",
        name_roman="Khumaani",
        name_hindi="खुबानी (एप्रिकॉट)",
        scientific_name="Prunus armeniaca",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Rosaceae",
        habitat_altitude="1,400m – 2,800m",
        traditional_uses="Sweet golden orchard fruit; hard kernel crushed for light skin and hair oil.",
        spiritual_and_temple_significance="Kernel oil historically used for temple sanctum brass lamps.",
        cultural_folklore="Classic Himalayan orchard crop."
    ),
    "pulam": KumaoniPlant(
        id="pulam",
        name_kumaoni="पुलम",
        name_roman="Pulam",
        name_hindi="आलूबुखारा / प्लम",
        scientific_name="Prunus domestica",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Rosaceae",
        habitat_altitude="1,200m – 2,400m",
        traditional_uses="Tart and sweet summer plum fruit eaten fresh or stewed into jams.",
        spiritual_and_temple_significance="Early white blossoms decorate village doorways during Phool Dei.",
        cultural_folklore="A staple seasonal crop of Nainital and Almora districts."
    ),
    "maalta": KumaoniPlant(
        id="maalta",
        name_kumaoni="माल्टा",
        name_roman="Maalta",
        name_hindi="माल्टा (पहाड़ी संतरा)",
        scientific_name="Citrus sinensis",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Rutaceae",
        habitat_altitude="800m – 1,800m",
        traditional_uses="Rich juicy hill blood orange; pulp mashed with ground mustard, curd, cannabis seeds, and jaggery into 'Sana hua Malta'.",
        spiritual_and_temple_significance="Bright orange fruits offered at sun worship and winter Sankrantis.",
        cultural_folklore="Winter terrace sunbathing ritual of Kumaon: enjoying Sana hua Malta on the sunny daand."
    ),
    "rai": KumaoniPlant(
        id="rai",
        name_kumaoni="रई / रयास",
        name_roman="Rai / Rayas",
        name_hindi="राई (पहाड़ी सरसों)",
        scientific_name="Brassica juncea",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Brassicaceae",
        habitat_altitude="600m – 2,400m",
        traditional_uses="Pungent green leaves cooked with radishes; seeds pressed into pure cooking and massage oil.",
        spiritual_and_temple_significance="Yellow flowers offered in spring pujas; mustard oil fuels sacred temple lamps (Diyos).",
        cultural_folklore="Symbol of glowing yellow terraced hillsides during Vasant Panchami."
    ),
    "kauni": KumaoniPlant(
        id="kauni",
        name_kumaoni="कौणी",
        name_roman="Kauni",
        name_hindi="कंगनी (फॉक्सटेल मिलेट)",
        scientific_name="Setaria italica",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="800m – 2,200m",
        traditional_uses="Ancient hill grain cooked like rice; rich in protein and fiber.",
        spiritual_and_temple_significance="Ancient sacred grain mentioned in Vedic rituals and hill folk epics as pure fasting grain.",
        cultural_folklore="Prehistoric staple crop of the Central Himalayan valleys."
    ),
    "cheena": KumaoniPlant(
        id="cheena",
        name_kumaoni="चीना",
        name_roman="Cheena",
        name_hindi="चीना (प्रोसो मिलेट)",
        scientific_name="Panicum miliaceum",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="1,000m – 2,400m",
        traditional_uses="Rapid-maturing mountain millet harvested when monsoon rains are sparse.",
        spiritual_and_temple_significance="Offered to local agricultural protector deities (Bhumia, Saim) during early harvest prayers.",
        cultural_folklore="Resilient emergency food of the mountain terrace farmers."
    ),
}'''

NEW_RITUALS_SNIPPET = '''    # ==================== ADDITIONAL TEMPLE IMPLEMENTS & SACRED PARAPHERNALIA ====================
    "deewa": KumaoniRitualItem(
        id="deewa",
        name_kumaoni="दीवा / दीयो",
        name_roman="Deewa",
        name_hindi="दीपक / दीया",
        category="Vessel & Offering Implement",
        traditional_material="Earthen terracotta clay or cast brass filled with cow ghee or mustard oil.",
        sacred_purpose="Lit at dawn and dusk at temple garbhagrihas, household mandirs, and thresholds to banish spiritual darkness.",
        cultural_context="The light of the Deewa represents the presence of the divine. Hand-turned brass lamps are lit during Sandhya Aarti at Jageshwar and Bagnath.",
        associated_deities_or_shrines=["Universal across all Kumaoni temples", "Sandhya Aarti", "Deepawali"]
    ),
    "baati": KumaoniRitualItem(
        id="baati",
        name_kumaoni="बाती / कपास की बत्ती",
        name_roman="Baati",
        name_hindi="बाती (रुई की बत्ती)",
        category="Sacred Mark & Thread",
        traditional_material="Hand-rolled pure cotton or sacred yellow-crimson mauli thread soaked in clarified butter.",
        sacred_purpose="Placed inside oil lamps to sustain the sacred flame (Akhand Jyoti).",
        cultural_context="Crafted by village women while reciting prayers; long twisted wicks symbolize steady spiritual focus.",
        associated_deities_or_shrines=["Universal temple pujas", "Akhand Jyoti"]
    ),
    "dhupeli": KumaoniRitualItem(
        id="dhupeli",
        name_kumaoni="धूपेली",
        name_roman="Dhupeli",
        name_hindi="धूपेली / धूपपात्र",
        category="Vessel & Offering Implement",
        traditional_material="Bell-metal bronze or terracotta with a sturdy curved handle.",
        sacred_purpose="Holds burning oak embers upon which guggul, loban, and juniper resins are sprinkled.",
        cultural_context="Carried throughout the temple sanctum and cottage rooms during evening sandhya to sanctify the space.",
        associated_deities_or_shrines=["Universal across all temples", "Evening Sandhya Aarti"]
    ),
    "loban": KumaoniRitualItem(
        id="loban",
        name_kumaoni="लोबान",
        name_roman="Loban",
        name_hindi="लोबान (गुग्गुल राल)",
        category="Hawan & Fire Sacrifice",
        traditional_material="Natural aromatic benzoin resin gum.",
        sacred_purpose="Burnt on glowing coals for aromatic fumigation and atmospheric purification.",
        cultural_context="Believed to dispel malefic spirits, negative energies (Chhal, Masaan), and insect pests.",
        associated_deities_or_shrines=["Bhairav temples", "Jagar séances", "Temple sanctums"]
    ),
    "guggal": KumaoniRitualItem(
        id="guggal",
        name_kumaoni="गुग्गल",
        name_roman="Guggal",
        name_hindi="गुग्गल",
        category="Hawan & Fire Sacrifice",
        traditional_material="Sacred aromatic resin from Commiphora wightii.",
        sacred_purpose="Cast into sacred hawan altars and temple dhupelis.",
        cultural_context="Produces a calming, meditative white smoke that purifies ritual spaces.",
        associated_deities_or_shrines=["Vedic hawan ceremonies", "Lord Shiva shrines"]
    ),
    "kapoor": KumaoniRitualItem(
        id="kapoor",
        name_kumaoni="कपूर",
        name_roman="Kapoor",
        name_hindi="कपूर (कर्पूर)",
        category="Hawan & Fire Sacrifice",
        traditional_material="Pure crystalline white camphor.",
        sacred_purpose="Ignited during the climax of Maha Aarti in front of the deity's face.",
        cultural_context="Chanted with 'Karpura-gauram Karuna-avataram...'. Burns completely without leaving ash, symbolizing surrender of individual ego into pure divine consciousness.",
        associated_deities_or_shrines=["Universal temple Maha Aarti", "Jageshwar Dham", "Nanda Devi"]
    ),
    "jhaanjh": KumaoniRitualItem(
        id="jhaanjh",
        name_kumaoni="झाँझ",
        name_roman="Jhaanjh",
        name_hindi="झांझ (बड़ी कांस्य झांझ)",
        category="Temple Insignia & Votive Offering",
        traditional_material="Heavy bell-metal bronze cymbals paired by cotton cords.",
        sacred_purpose="Struck together forcefully to produce penetrating rhythmic percussive sounds during temple aartis.",
        cultural_context="Creates energizing acoustical vibrations that drown out mundane distractions and invoke deity presence.",
        associated_deities_or_shrines=["Baijnath", "Bagnath Bageshwar", "Dhaula Devi"]
    ),
    "jhaanjhar": KumaoniRitualItem(
        id="jhaanjhar",
        name_kumaoni="झाँझर",
        name_roman="Jhaanjhar",
        name_hindi="झांझर",
        category="Temple Insignia & Votive Offering",
        traditional_material="Small brass cymbals or musical bells.",
        sacred_purpose="Keeps melodic rhythm during devotional kirtans and Jhora-Chanchari folk dances.",
        cultural_context="Brings joy and high-frequency resonance to community festivities.",
        associated_deities_or_shrines=["Devi melas", "Chaitra Navratri"]
    ),
    "damru": KumaoniRitualItem(
        id="damru",
        name_kumaoni="डमरू",
        name_roman="Damru",
        name_hindi="डमरू",
        category="Jagar & Oracle Implement",
        traditional_material="Hourglass-shaped carved wood or brass with parchment heads and knotted cords.",
        sacred_purpose="Rattled rhythmically to invoke Lord Shiva and the cosmic pulse (Nada Brahma).",
        cultural_context="Held by Shaivite priests and wandering jogis at Himalayan shrines.",
        associated_deities_or_shrines=["Jageshwar Dham", "Bagnath", "Tarkeshwar"]
    ),
    "chimta": KumaoniRitualItem(
        id="chimta",
        name_kumaoni="चिमटा",
        name_roman="Chimta",
        name_hindi="चिमटा (साधु का उपकरण)",
        category="Temple Insignia & Votive Offering",
        traditional_material="Wrought iron tongs with jingle plates.",
        sacred_purpose="Used by Nath yogis to attend the eternal Dhooni fire; struck rhythmically during bhajans.",
        cultural_context="Emblem of ascetic austerity and protection from wild animals in forest hermitages.",
        associated_deities_or_shrines=["Nath monasteries", "Gorakhnath shrines", "Haat Kalika Gangolihat"]
    ),
    "kamandal": KumaoniRitualItem(
        id="kamandal",
        name_kumaoni="कमण्डल",
        name_roman="Kamandal",
        name_hindi="कमंडल",
        category="Vessel & Offering Implement",
        traditional_material="Dried seasoned bottle-gourd shell or cast brass.",
        sacred_purpose="Carried by ascetics to store consecrated spring or river water.",
        cultural_context="Symbolizes worldly detachment and self-containment.",
        associated_deities_or_shrines=["Sanyasis", "Kumbh Yatras", "Bageshwar confluences"]
    ),
    "khadaun": KumaoniRitualItem(
        id="khadaun",
        name_kumaoni="खड़ाऊँ",
        name_roman="Khadaun",
        name_hindi="खड़ाऊं (काष्ठ पादुका)",
        category="Sacred Attire & Ornaments",
        traditional_material="Seasoned walnut or teak wood with elevated soles and wooden toe-knobs.",
        sacred_purpose="Worn by priests to maintain ritual purity while walking across flagstone courtyards.",
        cultural_context="Insulates the body from earth electrical discharge during mantra sadhana.",
        associated_deities_or_shrines=["Vedic priests", "Temple sanctums"]
    ),
    "kusha_asan": KumaoniRitualItem(
        id="kusha_asan",
        name_kumaoni="कुशा का आसन",
        name_roman="Kusha Asan",
        name_hindi="कुशा का आसन",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Hand-plaited sacred desmostachya grass.",
        sacred_purpose="Meditation and ritual seat specified in classical Agamas for japa, hawan, and tarpan.",
        cultural_context="Provides spiritual insulation, preventing pranic energy from grounding into the floor.",
        associated_deities_or_shrines=["Universal hawan altars", "Shraddha ceremonies"]
    ),
    "pattal": KumaoniRitualItem(
        id="pattal",
        name_kumaoni="पत्तल",
        name_roman="Pattal",
        name_hindi="पत्तल",
        category="Vessel & Offering Implement",
        traditional_material="Broad glossy leaves of Malu creeper or Sal tree stitched with ringal bamboo splints.",
        sacred_purpose="Eco-friendly dining plate for community temple feasts (Bhandara) and marriage banquets.",
        cultural_context="Zero-waste mountain dining tradition preserving ritual purity; discarded leaves return naturally to compost.",
        associated_deities_or_shrines=["Temple Bhandaras", "Community village feasts"]
    ),
    "dona": KumaoniRitualItem(
        id="dona",
        name_kumaoni="दोना",
        name_roman="Dona",
        name_hindi="दोना (पत्ते का कटोरा)",
        category="Vessel & Offering Implement",
        traditional_material="Fresh green Malu leaf folded into a cup.",
        sacred_purpose="Holds liquid prashad, panchamrit, halwa, or pulse soup for pilgrims.",
        cultural_context="Symbol of Himalayan harmony with nature.",
        associated_deities_or_shrines=["Universal temple prashad distribution"]
    ),
    "morpankh_jhaad": KumaoniRitualItem(
        id="morpankh_jhaad",
        name_kumaoni="मोरपंख झाड़",
        name_roman="Morpankh Jhaad",
        name_hindi="मोरपंख की झाड़",
        category="Jagar & Oracle Implement",
        traditional_material="Bound fan of iridescent male peacock tail feathers.",
        sacred_purpose="Swept gently over pilgrims' heads to dispel evil eye, anxiety, and fever.",
        cultural_context="Used by both temple priests and folk Jagariyas during blessing ceremonies.",
        associated_deities_or_shrines=["Golu Devta shrines", "Bhairav temples"]
    ),
    "jantar": KumaoniRitualItem(
        id="jantar",
        name_kumaoni="जंतर / ताबीज",
        name_roman="Jantar",
        name_hindi="जंतर (रक्षा ताबीज)",
        category="Sacred Mark & Thread",
        traditional_material="Solid silver or copper embossed cylinder.",
        sacred_purpose="Encloses consecrated yantra sheets, holy ash (Bhasma), or protective roots.",
        cultural_context="Worn around the neck or upper arm to shield children and adults from psychic affliction.",
        associated_deities_or_shrines=["Golu Devta Chitai", "Kalbisht"]
    ),
    "kaali_dori": KumaoniRitualItem(
        id="kaali_dori",
        name_kumaoni="काली डोरी / गंडो",
        name_roman="Kaali Dori",
        name_hindi="काली डोरी (रक्षा सूत्र)",
        category="Sacred Mark & Thread",
        traditional_material="Hand-spun black sheep wool or cotton yarn blessed with mantras.",
        sacred_purpose="Tied around an infant's wrist, ankle, or waist.",
        cultural_context="Shields vulnerable newborns from drishti-dosh (evil eye) and sickness.",
        associated_deities_or_shrines=["Family shrines", "Village devtas"]
    ),
    "baagh_nakh": KumaoniRitualItem(
        id="baagh_nakh",
        name_kumaoni="बाघ-नख",
        name_roman="Baagh-Nakh",
        name_hindi="बाघ-नख (चांदी का ताबीज)",
        category="Sacred Attire & Ornaments",
        traditional_material="Curved stylized tiger claw mounted in pure embossed silver.",
        sacred_purpose="Pendant worn around a boy's neck to bestow fearless courage.",
        cultural_context="Rooted in hill martial lore and belief in tiger spirits of Maa Nanda Devi.",
        associated_deities_or_shrines=["Nanda Devi", "Hill warrior traditions"]
    ),
    "suhaag_pitaari": KumaoniRitualItem(
        id="suhaag_pitaari",
        name_kumaoni="सुहाग पिटारी",
        name_roman="Suhaag Pitaari",
        name_hindi="सुहाग पिटारी",
        category="Sacred Attire & Ornaments",
        traditional_material="Fine ringal wicker or engraved brass lidded basket.",
        sacred_purpose="Preserves sacred bridal cosmetics (Pithya, sindoor, kajal, bangles, bichhuwa).",
        cultural_context="Offered to Maa Nanda Devi and Bhagwati for matrimonial longevity and family prosperity.",
        associated_deities_or_shrines=["Nanda Devi", "Kotgari Bhagwati", "Marriage altars"]
    ),
    "nath": KumaoniRitualItem(
        id="nath",
        name_kumaoni="नथ / नथुली",
        name_roman="Nath",
        name_hindi="नथ / नथुली",
        category="Sacred Attire & Ornaments",
        traditional_material="Pure 24k gold, natural freshwater pearls, rubies, and floral filigree.",
        sacred_purpose="Monumental nose ring sanctified in front of the family deity prior to marriage.",
        cultural_context="The crowning cultural ornament of Kumaoni women; symbol of royal elegance and divine blessings.",
        associated_deities_or_shrines=["Maa Nanda Devi", "Weddings across Kumaon"]
    ),
    "paunchi": KumaoniRitualItem(
        id="paunchi",
        name_kumaoni="पौंची",
        name_roman="Paunchi",
        name_hindi="पौंची (पारंपरिक स्वर्णाभूषण)",
        category="Sacred Attire & Ornaments",
        traditional_material="Faceted hollow gold beads sewn onto padded red velvet.",
        sacred_purpose="Bridal wrist ornament blessed by priests during wedding rituals.",
        cultural_context="Traditional heirloom passed from mother-in-law to daughter-in-law.",
        associated_deities_or_shrines=["Matrimonial pujas", "Diwali"]
    ),
    "guloband": KumaoniRitualItem(
        id="guloband",
        name_kumaoni="गुलूबंद",
        name_roman="Guloband",
        name_hindi="गुलूबंद",
        category="Sacred Attire & Ornaments",
        traditional_material="Square carved gold plaques strung tightly on crimson velvet ribbon.",
        sacred_purpose="Choker necklace consecrated at Devi altars for marital felicity.",
        cultural_context="Iconic traditional jewelry of Kumaon.",
        associated_deities_or_shrines=["Nanda Devi", "Weddings"]
    ),
    "dhaar": KumaoniRitualItem(
        id="dhaar",
        name_kumaoni="धार / दुग्धाभिषेक",
        name_roman="Dhaar",
        name_hindi="धार (निरंतर जलाभिषेक/दुग्धाभिषेक)",
        category="Vessel & Offering Implement",
        traditional_material="Copper pot with small bottom perforation suspended over Shivalinga.",
        sacred_purpose="Pours a continuous cool stream of mountain water or pure milk over the deity.",
        cultural_context="Soothes the fiery energy of Lord Shiva; supreme act of devotion in Himalayan temples.",
        associated_deities_or_shrines=["Jageshwar Dham", "Baijnath", "Bagnath Bageshwar"]
    ),
    "tarpan_paatra": KumaoniRitualItem(
        id="tarpan_paatra",
        name_kumaoni="तर्पण पात्र",
        name_roman="Tarpan Paatra",
        name_hindi="तर्पण पात्र",
        category="Vessel & Offering Implement",
        traditional_material="Flat-lipped wide copper dish.",
        sacred_purpose="Used during Pitru Paksha to offer water, black sesame, and kusha to ancestors.",
        cultural_context="Preserves spiritual continuity with departed forebears at holy river confluences.",
        associated_deities_or_shrines=["Bagnath confluence (Saryu-Gomti)", "Devprayag", "Gaya"]
    ),
    "bhandaar": KumaoniRitualItem(
        id="bhandaar",
        name_kumaoni="भंडार",
        name_roman="Bhandaar",
        name_hindi="मंदिर का भंडार",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Stone-and-timber vault chamber within the temple compound.",
        sacred_purpose="Preserves sacred copper cauldrons, silver ornaments, grain offerings, and temple treasures.",
        cultural_context="Guarded by designated lineage hereditary trustees (Bhandari clans).",
        associated_deities_or_shrines=["Chitai Golu Devta", "Jageshwar", "Nanda Devi Almora"]
    ),
    "dhwaj": KumaoniRitualItem(
        id="dhwaj",
        name_kumaoni="ध्वज / नेजा",
        name_roman="Dhwaj / Neja",
        name_hindi="ध्वज (देवता का झंडा)",
        category="Temple Insignia & Votive Offering",
        traditional_material="Triangular crimson or saffron silk flag mounted on tall mountain bamboo.",
        sacred_purpose="Flutters atop temple spires, mountain ridges, and carried at the head of holy processions.",
        cultural_context="Announces the spiritual sovereignty and protective canopy of the presiding devta.",
        associated_deities_or_shrines=["Universal across all temples", "Golu Devta", "Nanda Devi Jaat"]
    ),
}'''


def update_flora():
    content = FLORA_FILE.read_text(encoding="utf-8")
    if '"utees":' in content:
        print("Flora already contains 'utees'. Skipping.")
        return
    # Replace closing of FLORA_DATA
    target = '    ),\n}'
    # Find last occurrence of '    ),\n}'
    idx = content.rfind(target)
    if idx == -1:
        print("Could not locate FLORA_DATA closing '    ),\\n}'.")
        return
    new_content = content[:idx] + '    ),\n' + NEW_FLORA_SNIPPET + content[idx + len(target):]
    FLORA_FILE.write_text(new_content, encoding="utf-8")
    print("Successfully updated kumaoni/culture/flora.py with 28 new plants.")


def update_rituals():
    content = RITUALS_FILE.read_text(encoding="utf-8")
    if '"deewa":' in content:
        print("Rituals already contains 'deewa'. Skipping.")
        return
    target = '    ),\n}'
    idx = content.rfind(target)
    if idx == -1:
        print("Could not locate RITUAL_ITEMS_DATA closing '    ),\\n}'.")
        return
    new_content = content[:idx] + '    ),\n' + NEW_RITUALS_SNIPPET + content[idx + len(target):]
    RITUALS_FILE.write_text(new_content, encoding="utf-8")
    print("Successfully updated kumaoni/culture/rituals.py with 27 new ritual articles.")


if __name__ == "__main__":
    update_flora()
    update_rituals()
