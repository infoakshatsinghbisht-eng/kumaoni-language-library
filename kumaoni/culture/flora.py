"""
Kumaoni ethnobotany, sacred Himalayan flora, indigenous trees, medicinal herbs, and wildflowers.
Catalogues sacred trees, oaks, alpine florals, wild fruits, and agricultural flora of Kumaon.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class KumaoniPlant:
    id: str
    name_kumaoni: str
    name_roman: str
    name_hindi: str
    scientific_name: str
    category: str  # "Sacred & Ritual Tree", "Himalayan Forest Tree", "Alpine Flower & Sacred Herb", "Wild Mountain Fruit & Shrub", "Medicinal & Aromatic Flora", "Sacred Grass & Agricultural Flora"
    botanical_family: str
    habitat_altitude: str
    traditional_uses: str
    spiritual_and_temple_significance: str
    cultural_folklore: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


FLORA_DATA: Dict[str, KumaoniPlant] = {
    # ==================== SACRED & RITUAL TREES ====================
    "banjh": KumaoniPlant(
        id="banjh",
        name_kumaoni="बाँझ",
        name_roman="Banjh",
        name_hindi="बांज (सफेद बांज)",
        scientific_name="Quercus leucotrichophora",
        category="Himalayan Forest Tree",
        botanical_family="Fagaceae",
        habitat_altitude="1,200m – 2,400m",
        traditional_uses="Nutritious evergreen cattle fodder, humus-rich soil conservation, pristine water aquifer preservation, traditional farm implement handles.",
        spiritual_and_temple_significance="Revered as the maternal forest goddess ('Hariyali Devi'). Sacred groves of Banjh shelter village deities (Bhumia, Saim, Kalbisht). Banjh branches are placed at shrines during Harela.",
        cultural_folklore="Immortalized in Kumaoni folk songs as the mother of the mountains: 'Banjh raula ta paani raulo, paani raula ta zindagani rauli' (If oak survives, water survives; if water survives, life survives)."
    ),
    "buransh": KumaoniPlant(
        id="buransh",
        name_kumaoni="बुराँश / बुरांश",
        name_roman="Buransh",
        name_hindi="बुरांश",
        scientific_name="Rhododendron arboreum",
        category="Sacred & Ritual Tree",
        botanical_family="Ericaceae",
        habitat_altitude="1,500m – 3,000m",
        traditional_uses="Flowers squeezed into refreshing mountain squash; medicinal cardiovascular tonic; light firewood.",
        spiritual_and_temple_significance="State Tree of Uttarakhand. Fresh crimson blossoms are offered directly to Lord Shiva on Shivratri and to Maa Nanda Devi during spring festivals. Petals adorn temple thresholds on Phool Dei.",
        cultural_folklore="Celebrated as the fiery crimson pride of Kumaoni spring. Featured prominently in classic folk poetry and songs like 'Pahada ma phooli ge buransh'."
    ),
    "deodar": KumaoniPlant(
        id="deodar",
        name_kumaoni="देवदार",
        name_roman="Deodar",
        name_hindi="देवदार",
        scientific_name="Cedrus deodara",
        category="Sacred & Ritual Tree",
        botanical_family="Pinaceae",
        habitat_altitude="1,800m – 3,000m",
        traditional_uses="Resilient aromatic temple architecture timber; insect-repellent wood; aromatic cedar oil.",
        spiritual_and_temple_significance="Sanskrit 'Devadaru' (Tree of the Gods). The sacred 124 stone temples of Jageshwar Dham and Katarmal Sun Temple stand within primordial Deodar groves. Sacred abodes of Lord Shiva.",
        cultural_folklore="Believed to be Shiva's own forest (Daru Vana) where sages meditated. Cutting live deodars in temple groves has been strictly taboo for centuries."
    ),
    "panya": KumaoniPlant(
        id="panya",
        name_kumaoni="पैंया / पदम",
        name_roman="Panya / Padam",
        name_hindi="पद्मकाष्ठ (जंगली हिमालयी चेरी)",
        scientific_name="Prunus cerasoides",
        category="Sacred & Ritual Tree",
        botanical_family="Rosaceae",
        habitat_altitude="1,200m – 2,400m",
        traditional_uses="Autumn-blooming cherry wood; bark used in indigenous cosmetics and Ayurvedic formulations.",
        spiritual_and_temple_significance="Considered the most sacred wood for fire sacrifices (Samidha). Twigs are mandatory for Hawan altars, marriage Mandaps, and constructing temple flagstaffs (Nishan).",
        cultural_folklore="Its delicate pink blossoms blooming in October-November signal the arrival of the auspicious wedding season and festive winter in Kumaon."
    ),
    "surai": KumaoniPlant(
        id="surai",
        name_kumaoni="सुरई",
        name_roman="Surai",
        name_hindi="सुरई (हिमालयी सरू)",
        scientific_name="Cupressus torulosa",
        category="Sacred & Ritual Tree",
        botanical_family="Cupressaceae",
        habitat_altitude="1,800m – 2,800m",
        traditional_uses="Tall spire-shaped timber used for temple roofing, prayer masts, and woodcarving.",
        spiritual_and_temple_significance="Planted around sacred temples, cliff monasteries, and shrines to symbolize spiritual ascent and eternal vigilance.",
        cultural_folklore="Associated with austere Himalayan ascetics; fragrant needles are dried and powdered as incense."
    ),
    "bhojpatra": KumaoniPlant(
        id="bhojpatra",
        name_kumaoni="भोजपत्र",
        name_roman="Bhojpatra",
        name_hindi="भोजपत्र (हिमालयी बर्च)",
        scientific_name="Betula utilis",
        category="Sacred & Ritual Tree",
        botanical_family="Betulaceae",
        habitat_altitude="3,000m – 4,200m",
        traditional_uses="Papery peeling bark historically used for writing manuscripts, wrapping butter and food for mountain crossings.",
        spiritual_and_temple_significance="Ancient sacred writing medium for Vedic mantras, Tantric yantras, and Kumaoni royal land grants. Used as protective amulets (Yantra taweez) blessed at temples.",
        cultural_folklore="Marks the subalpine treeline below Himalayan glaciers (Milam, Pindari); tree of Shiva's hermits."
    ),
    "ringal": KumaoniPlant(
        id="ringal",
        name_kumaoni="रिंगाल",
        name_roman="Ringal",
        name_hindi="रिंगाल (पहाड़ी बांस)",
        scientific_name="Thamnocalamus spathiflorus",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="1,500m – 3,200m",
        traditional_uses="Pliable mountain bamboo woven into storage baskets (Mosta, Doka, Kandi, Supa), fishing traps, and mats.",
        spiritual_and_temple_significance="Mandatory sacred bamboo used to weave the royal ceremonial umbrella (Chhatoli) of Goddess Nanda Devi during the holy Nanda Raj Jaat. Baskets used for carrying temple offerings.",
        cultural_folklore="Symbolizes humble hill craft; artisan communities (Rudyas) traditionally weave ringal as a sacred vocation."
    ),
    "bheemal": KumaoniPlant(
        id="bheemal",
        name_kumaoni="भीमल / भिमुल",
        name_roman="Bheemal",
        name_hindi="भीमल",
        scientific_name="Grewia optiva",
        category="Himalayan Forest Tree",
        botanical_family="Malvaceae",
        habitat_altitude="500m – 1,800m",
        traditional_uses="Supreme winter cattle fodder; inner bark retted in streams to produce strong organic rope fibre (Selu); dried twigs used as torchwood.",
        spiritual_and_temple_significance="Twigs are burned as holy torches during the Kumaoni festival of Khatarwa and Diwali (Bhelo). Used to tie temple sheaf offerings.",
        cultural_folklore="Regarded as the mountain farmer's closest tree companion, planted on the terrace walls of every Kumaoni farm."
    ),
    "pipal": KumaoniPlant(
        id="pipal",
        name_kumaoni="पीपल",
        name_roman="Pipal",
        name_hindi="पीपल",
        scientific_name="Ficus religiosa",
        category="Sacred & Ritual Tree",
        botanical_family="Moraceae",
        habitat_altitude="300m – 1,600m",
        traditional_uses="Medicinal bark; shade tree at village crossroads.",
        spiritual_and_temple_significance="Abode of Lord Vishnu and the Trimurti. Worshipped on Somvati Amavasya; planted with Banyan to create sacred marriage platforms (Pipal-Bar vivah). Village open shrines sit beneath it.",
        cultural_folklore="Cutting a pipal tree is considered a grave sin in Kumaoni custom."
    ),
    "bar": KumaoniPlant(
        id="bar",
        name_kumaoni="बड़ / बरगद",
        name_roman="Bar / Bargad",
        name_hindi="बरगद (वटवृक्ष)",
        scientific_name="Ficus benghalensis",
        category="Sacred & Ritual Tree",
        botanical_family="Moraceae",
        habitat_altitude="300m – 1,500m",
        traditional_uses="Extensive aerial root shade; latex used in folk medicine.",
        spiritual_and_temple_significance="Symbol of immortality (Akshaya Vat). Worshipped by women during Vat Savitri festival for spousal longevity. Ancestor rituals performed under its canopy.",
        cultural_folklore="Traditional gathering place for village councils (Panchayats) and traveling bard storytellers."
    ),
    "bel": KumaoniPlant(
        id="bel",
        name_kumaoni="बेल / बिल्व",
        name_roman="Bel / Bilva",
        name_hindi="बेल (बिल्वपत्र)",
        scientific_name="Aegle marmelos",
        category="Sacred & Ritual Tree",
        botanical_family="Rutaceae",
        habitat_altitude="300m – 1,200m",
        traditional_uses="Cooling digestive fruit pulp; sacred wood for hawan.",
        spiritual_and_temple_significance="Supreme offering to Lord Shiva. Its trifoliate leaf represents the Trishul and the three eyes of Shiva. Indispensable for jalabhishek at Bagnath and Jageshwar.",
        cultural_folklore="Said to cool the fiery cosmic heat absorbed by Shiva when he drank the Halahala poison."
    ),
    "shami": KumaoniPlant(
        id="shami",
        name_kumaoni="शमीर / छौंकर",
        name_roman="Shami / Chhonkar",
        name_hindi="शमी (खेजड़ी)",
        scientific_name="Prosopis cineraria",
        category="Sacred & Ritual Tree",
        botanical_family="Fabaceae",
        habitat_altitude="400m – 1,400m",
        traditional_uses="Sacred wood twigs for sacrificial fire (Arani); leaves used in ritual purification.",
        spiritual_and_temple_significance="Worshipped on Vijayadashami (Dussehra). Legend tells that the Pandavas hid their divine weapons in the Shami tree during their exile in the Himalayas.",
        cultural_folklore="Believed to extinguish malefic astrological influences of Saturn (Shani)."
    ),

    # ==================== ALPINE FLOWERS & SACRED HERBS ====================
    "brahmakamal": KumaoniPlant(
        id="brahmakamal",
        name_kumaoni="ब्रह्मकमल",
        name_roman="Brahmakamal",
        name_hindi="ब्रह्मकमल",
        scientific_name="Saussurea obvallata",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Asteraceae",
        habitat_altitude="3,800m – 4,800m",
        traditional_uses="Alpine medicinal herb; used in bone-setting and urinary disorders.",
        spiritual_and_temple_significance="State Flower of Uttarakhand. Mythological lotus that Lord Brahma used to revive Lord Ganesha. Supreme sacred floral offering to Goddess Nanda Devi and Lord Kedarnath / Badrinath.",
        cultural_folklore="Blooms in the dead of monsoon night amidst mist and moraines. Plucked only with ritual fasting and bare feet during the Nanda Ashtami pilgrimage."
    ),
    "phen_kamal": KumaoniPlant(
        id="phen_kamal",
        name_kumaoni="फेन कमल",
        name_roman="Phen Kamal",
        name_hindi="फेन कमल",
        scientific_name="Saussurea simpsoniana",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Asteraceae",
        habitat_altitude="4,200m – 5,500m",
        traditional_uses="High-altitude herb used by high-Himalayan pastoralists for wounds.",
        spiritual_and_temple_significance="Woolly snow lotus offered to Lord Shiva at Adi Kailash, Om Parvat, and high Himalayan glacial passes.",
        cultural_folklore="Survives beneath heavy snow packs; enveloped in white woolly filaments like sage's beard."
    ),
    "kasturi_kamal": KumaoniPlant(
        id="kasturi_kamal",
        name_kumaoni="कस्तूरी कमल",
        name_roman="Kasturi Kamal",
        name_hindi="कस्तूरी कमल",
        scientific_name="Saussurea gossypiphora",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Asteraceae",
        habitat_altitude="4,300m – 5,600m",
        traditional_uses="Aromatic sacred plant emitting musk-like fragrance.",
        spiritual_and_temple_significance="Offered at high altitude passes (Darma, Vyas, Johar) to mountain guardian deities (Gabla Devta, Chipla Kedar).",
        cultural_folklore="Regarded as the rarest holy flower of the Trans-Himalayan crags."
    ),
    "phyunli": KumaoniPlant(
        id="phyunli",
        name_kumaoni="फ्यूँली / प्यूँली",
        name_roman="Phyunli",
        name_hindi="प्यूँली (बसंती फूल)",
        scientific_name="Reinwardtia indica",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Linaceae",
        habitat_altitude="800m – 2,200m",
        traditional_uses="Yellow spring flower; natural herbal pigment.",
        spiritual_and_temple_significance="Primary sacred flower of Phool Dei festival. Children collect early spring Phyunli blossoms to place on the stone doorsteps (Dehli) of every village household to usher in fortune.",
        cultural_folklore="Associated in folklore with a tender mountain maiden 'Phyunli' who loved forest nature and whose spirit lives in these yellow blossoms."
    ),
    "tulsi": KumaoniPlant(
        id="tulsi",
        name_kumaoni="तुलसी",
        name_roman="Tulsi",
        name_hindi="तुलसी (पवित्र तुलसी)",
        scientific_name="Ocimum sanctum",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Lamiaceae",
        habitat_altitude="300m – 1,800m",
        traditional_uses="Immunity booster, respiratory healer, sacred tea infusion.",
        spiritual_and_temple_significance="Worshipped daily in a raised stone pedestal (Chauri) in every Kumaoni courtyard. Leaves are mandatory in Vishnu and Krishna pujas and float in Charanamrit.",
        cultural_folklore="Married to the Shaligram stone on Tulsi Vivah (Kartik Shukla Ekadashi) with full wedding fanfares."
    ),
    "dhatura": KumaoniPlant(
        id="dhatura",
        name_kumaoni="धतूरा",
        name_roman="Dhatura",
        name_hindi="धतूरा",
        scientific_name="Datura stramonium",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Solanaceae",
        habitat_altitude="500m – 2,200m",
        traditional_uses="Tantric ritual offering; external poultice for swellings.",
        spiritual_and_temple_significance="Intensely offered to Lord Shiva, Bhairav, and Gorakhnath. Represents transcendence of poison and illusion.",
        cultural_folklore="Planted near cremation grounds and rural Shiva temples as a sacred guardian herb."
    ),
    "bhang": KumaoniPlant(
        id="bhang",
        name_kumaoni="भांग",
        name_roman="Bhang",
        name_hindi="भांग",
        scientific_name="Cannabis sativa",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Cannabaceae",
        habitat_altitude="800m – 2,600m",
        traditional_uses="Non-narcotic roasted seeds crushed with mint and lime into famous Kumaoni 'Bhang ki Chutney'; stem bast fibre spun into hemp ropes and bags.",
        spiritual_and_temple_significance="Offered to Lord Shiva on Maha Shivratri at Jageshwar and Bagnath. Leaves sanctified in Shaivite ritual jagars.",
        cultural_folklore="Traditional winter warm-food ingredient across Almora, Pithoragarh, and Champawat."
    ),
    "genda": KumaoniPlant(
        id="genda",
        name_kumaoni="गेंदा",
        name_roman="Genda",
        name_hindi="गेंदा (हजारा)",
        scientific_name="Tagetes erecta",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Asteraceae",
        habitat_altitude="300m – 2,200m",
        traditional_uses="Natural insect repellent; dye extraction; ornamental decoration.",
        spiritual_and_temple_significance="Primary flower woven into thick yellow and orange garlands (Mala) for temple idols, village shrines, cattle horns during Diwali, and festive Torans.",
        cultural_folklore="Its vibrant color represents sacrificial fire and solar blessings."
    ),
    "kunja": KumaoniPlant(
        id="kunja",
        name_kumaoni="कुंजा",
        name_roman="Kunja",
        name_hindi="कुंजा (हिमालयी जंगली सफेद गुलाब)",
        scientific_name="Rosa brunonii",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Rosaceae",
        habitat_altitude="1,200m – 2,600m",
        traditional_uses="Distilled for rose water; rosehips eaten by birds; decorative climber.",
        spiritual_and_temple_significance="Wild white fragrant rose climbing over oak branches in May; offered to mountain goddesses and village kuldevis.",
        cultural_folklore="Fills valley breezes with perfume; celebrated in romantic Pahari folk verses."
    ),

    # ==================== MEDICINAL & AROMATIC FLORA ====================
    "jatamansi": KumaoniPlant(
        id="jatamansi",
        name_kumaoni="जटामांसी / बालबछ",
        name_roman="Jatamansi / Balbachh",
        name_hindi="जटामांसी (बालछड़)",
        scientific_name="Nardostachys jatamansi",
        category="Medicinal & Aromatic Flora",
        botanical_family="Caprifoliaceae",
        habitat_altitude="3,200m – 5,000m",
        traditional_uses="Deep nerve calming Ayurvedic medicine, memory tonic, hair nourishment.",
        spiritual_and_temple_significance="Essential Himalayan root incense used in Hawan fires, temple Dhoopdanis, and shamanic Jagar invocations to cleanse sacred spaces and induce calm meditation.",
        cultural_folklore="High alpine root wrapped in dense hair-like fibers resembling ascetic matted dreadlocks (Jata)."
    ),
    "dhoop_lakdi": KumaoniPlant(
        id="dhoop_lakdi",
        name_kumaoni="धूप-लकड़ी",
        name_roman="Dhoop-lakdi",
        name_hindi="धूप जड़ (गुग्गल धूप)",
        scientific_name="Jurinea macrocephala",
        category="Medicinal & Aromatic Flora",
        botanical_family="Asteraceae",
        habitat_altitude="3,000m – 4,500m",
        traditional_uses="Fragrant mountain incense root; burned during spiritual rituals.",
        spiritual_and_temple_significance="Burned in open temple braziers and stone sanctuaries; essential fragrance of Kumaoni temple aarti.",
        cultural_folklore="Gathered by high-altitude shepherds on alpine meadows (Bugyals) in late autumn."
    ),
    "guggul": KumaoniPlant(
        id="guggul",
        name_kumaoni="गुग्गुल",
        name_roman="Guggul",
        name_hindi="गुग्गुल",
        scientific_name="Commiphora mukul",
        category="Medicinal & Aromatic Flora",
        botanical_family="Burseraceae",
        habitat_altitude="Himalayan foothills & dry tracts",
        traditional_uses="Anti-inflammatory resin, joint healer, sacred purifier.",
        spiritual_and_temple_significance="Fragrant oleo-gum resin dropped onto red-hot embers in temple braziers to repel negativity and invoke deities.",
        cultural_folklore="Standard component of every authentic temple ritual pouch in Uttarakhand."
    ),
    "gandrayani": KumaoniPlant(
        id="gandrayani",
        name_kumaoni="गन्द्रायणी / गंदेरायण",
        name_roman="Gandrayani",
        name_hindi="गंदरायण",
        scientific_name="Angelica glauca",
        category="Medicinal & Aromatic Flora",
        botanical_family="Apiaceae",
        habitat_altitude="2,800m – 3,800m",
        traditional_uses="Digestive tonic, carminative spice for high-altitude pulses (Gahat, Bhatt), warming spice.",
        spiritual_and_temple_significance="Offered at village Thans and alpine stone altars during cross-pass pilgrimages in Johar, Darma, and Byas valleys.",
        cultural_folklore="Pungent aromatic mountain root traded along ancient Indo-Tibetan trade routes."
    ),
    "jambu": KumaoniPlant(
        id="jambu",
        name_kumaoni="जम्बू / जंबू / फरण",
        name_roman="Jambu / Faran",
        name_hindi="जंबू (हिमालयी छौंक)",
        scientific_name="Allium stracheyi",
        category="Medicinal & Aromatic Flora",
        botanical_family="Amaryllidaceae",
        habitat_altitude="2,500m – 4,200m",
        traditional_uses="Sun-dried aromatic Himalayan chive used as quintessential tadka in Kumaoni dal and vegetables.",
        spiritual_and_temple_significance="Harvested with blessings of mountain deities; offered during high alpine ceremonies.",
        cultural_folklore="Key culinary export of the Shauka communities of Johar and Munsyari."
    ),
    "jakhya": KumaoniPlant(
        id="jakhya",
        name_kumaoni="जख्या",
        name_roman="Jakhya",
        name_hindi="जख्या (जंगली सरसों)",
        scientific_name="Cleome viscosa",
        category="Medicinal & Aromatic Flora",
        botanical_family="Cleomaceae",
        habitat_altitude="500m – 1,800m",
        traditional_uses="Crunchy dark tempering seed used for iconic potato delicacy 'Aloo ke Gutke'.",
        spiritual_and_temple_significance="Essential condiment in festive temple community meals (Bhandara).",
        cultural_folklore="Grows wild on terrace margins; crunchy texture is the signature taste of Kumaon."
    ),
    "kutki": KumaoniPlant(
        id="kutki",
        name_kumaoni="कुटकी",
        name_roman="Kutki",
        name_hindi="कुटकी",
        scientific_name="Picrorhiza kurroa",
        category="Medicinal & Aromatic Flora",
        botanical_family="Plantaginaceae",
        habitat_altitude="3,000m – 4,500m",
        traditional_uses="Potent bitter hepatoprotective herb; liver detoxifier, fever reliever.",
        spiritual_and_temple_significance="Regarded as divine herbal ambrosia gifted by mountain deities for survival in harsh Himalayan winters.",
        cultural_folklore="Collected in subalpine rocks with reverence and prayers for safe descent."
    ),
    "chirayata": KumaoniPlant(
        id="chirayata",
        name_kumaoni="चिरैता",
        name_roman="Chirayata",
        name_hindi="चिरायता",
        scientific_name="Swertia chirayita",
        category="Medicinal & Aromatic Flora",
        botanical_family="Gentianaceae",
        habitat_altitude="1,200m – 3,000m",
        traditional_uses="Legendary bitter blood purifier, malaria remedy, digestive stimulant.",
        spiritual_and_temple_significance="Included in traditional Ayurvedic consecrated temple medicines distributed by temple Vaidyas.",
        cultural_folklore="Its bitterness is proverbially cited in Kumaoni conversation to describe harsh truth."
    ),

    # ==================== WILD MOUNTAIN FRUITS & SHRUBS ====================
    "kafal": KumaoniPlant(
        id="kafal",
        name_kumaoni="काफल",
        name_roman="Kafal",
        name_hindi="काफल",
        scientific_name="Myrica esculenta",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Myricaceae",
        habitat_altitude="1,300m – 2,100m",
        traditional_uses="Succulent sweet-and-sour crimson bayberry; astringent medicinal bark (Katphala).",
        spiritual_and_temple_significance="Offered at village shrines upon first ripening in Chaitra-Baisakh. First berries taken to temple before family consumption.",
        cultural_folklore="Legend of the bird singing 'Kafal pako chait, mai ni chakho bhoot' (Kafal ripened in Chait, but I didn't taste it, daughter!). Foremost cultural berry of Kumaon."
    ),
    "bedu": KumaoniPlant(
        id="bedu",
        name_kumaoni="बेड़ू",
        name_roman="Bedu",
        name_hindi="बेड़ू (जंगली अंजीर)",
        scientific_name="Ficus palmata",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Moraceae",
        habitat_altitude="800m – 2,200m",
        traditional_uses="Edible sweet wild figs; young leaves and green fruit cooked into traditional hill sabzi.",
        spiritual_and_temple_significance="Foliage used in rural village offerings and sacred feasts.",
        cultural_folklore="Immortalized in the global Kumaoni anthem: 'Bedu pako baro masa, narana kafal pako chait meri chhaila!'."
    ),
    "timul": KumaoniPlant(
        id="timul",
        name_kumaoni="तिमिल / तिमुल",
        name_roman="Timul",
        name_hindi="तिमुल (हाथी अंजीर)",
        scientific_name="Ficus auriculata",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Moraceae",
        habitat_altitude="800m – 2,000m",
        traditional_uses="Large plate-sized leaves stitched with bamboo slivers into sacred eco-friendly dinner plates (Patrawali); fruit eaten fresh or cooked.",
        spiritual_and_temple_significance="Stitched Timul leaf plates are mandatory for serving temple feasts (Bhandara), marriage Dham meals, and Jagar community dinners.",
        cultural_folklore="Provides sacred zero-waste tableware integral to Himalayan ritual hospitality."
    ),
    "kilmora": KumaoniPlant(
        id="kilmora",
        name_kumaoni="किल्मोड़ा / किलमोड़ा",
        name_roman="Kilmora",
        name_hindi="किल्मोड़ा (दारुहरिद्रा)",
        scientific_name="Berberis asiatica",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Berberidaceae",
        habitat_altitude="1,200m – 2,500m",
        traditional_uses="Sweet purple-blue berries eaten fresh; yellow root bark boiled into 'Rasaut' ointment for eye infections and jaundice.",
        spiritual_and_temple_significance="Thorny protective hedge planted around sacred groves and village stone borders.",
        cultural_folklore="Beloved wild berry of hill children grazing sheep on mountain ridges."
    ),
    "hisolu": KumaoniPlant(
        id="hisolu",
        name_kumaoni="हिसोलू / हिसाव",
        name_roman="Hisolu",
        name_hindi="हिसोलू (पीली रसभरी)",
        scientific_name="Rubus ellipticus",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Rosaceae",
        habitat_altitude="1,000m – 2,300m",
        traditional_uses="Golden yellow sweet juicy wild raspberry; rich in antioxidants; thorny living hedge.",
        spiritual_and_temple_significance="Early summer fruit offered to village forest spirits (Bhumia, Ainchari).",
        cultural_folklore="Symbol of untouched mountain sweetness; sung in summer pastoral folk songs."
    ),
    "akhod": KumaoniPlant(
        id="akhod",
        name_kumaoni="अखोड़ / ओखड़",
        name_roman="Akhod / Okhad",
        name_hindi="अखरोट",
        scientific_name="Juglans regia",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Juglandaceae",
        habitat_altitude="1,500m – 2,800m",
        traditional_uses="Nutritious oil-rich nuts; walnut tree bark (Dandasa) used as natural teeth whitening stick; hardwood timber.",
        spiritual_and_temple_significance="Walnuts are broken and offered at village thans and temples during Bikhoti and autumn pujas. Traditional prasad.",
        cultural_folklore="Walnut groves on hillsides are family heirlooms passed through generations."
    ),
    "choolu": KumaoniPlant(
        id="choolu",
        name_kumaoni="चूलू",
        name_roman="Choolu",
        name_hindi="चूलू (जंगली खुबानी)",
        scientific_name="Prunus armeniaca",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Rosaceae",
        habitat_altitude="1,600m – 3,000m",
        traditional_uses="Sweet-tart fruit dried for winter; pure cold-pressed kernel oil used for temple lighting, cooking, and joint ache relief.",
        spiritual_and_temple_significance="Pure Choolu kernel oil was traditionally burned in silver lamps in inner temple sanctums where cow ghee was scarce.",
        cultural_folklore="Characteristic tree of high Kumaoni valleys like Johar and Darma."
    ),
    "galgal": KumaoniPlant(
        id="galgal",
        name_kumaoni="गलगल / गलगली",
        name_roman="Galgal",
        name_hindi="गलगल (बड़ा पहाड़ी नींबू)",
        scientific_name="Citrus pseudolimon",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Rutaceae",
        habitat_altitude="600m – 1,800m",
        traditional_uses="Giant juicy mountain lemon used to prepare iconic winter sun-basking dish 'Saani hui Nimbu' with curd, jaggery, and hemp seeds.",
        spiritual_and_temple_significance="Offered at Devi shrines during Navratri for vitality and protection.",
        cultural_folklore="Community gathering around sunny courtyards eating seasoned Galgal is a signature winter tradition."
    ),
    "darim": KumaoniPlant(
        id="darim",
        name_kumaoni="दाड़िम / दाड़िम",
        name_roman="Darim",
        name_hindi="दाड़िम (जंगली अनार)",
        scientific_name="Punica granatum",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Lythraceae",
        habitat_altitude="900m – 2,000m",
        traditional_uses="Dried seeds (Anardana) used as tangy spice; fruit rind used in bowel medicine and natural textile dyes.",
        spiritual_and_temple_significance="Offered to Goddess Shakti and Ganesha as symbol of fertility and divine abundance.",
        cultural_folklore="Wild pomegranate flowers celebrated in traditional bridal songs."
    ),

    # ==================== SACRED GRASSES & CROPS ====================
    "kush": KumaoniPlant(
        id="kush",
        name_kumaoni="कुश",
        name_roman="Kush",
        name_hindi="कुश (डाभ)",
        scientific_name="Desmostachya bipinnata",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="River valleys & foothills",
        traditional_uses="Sacred insulating mats for meditation; purification water sprinkler.",
        spiritual_and_temple_significance="The most sacred ritual grass in Hindu worship. Ring woven from Kush (Pavitri) is worn on the right ring finger by priests during Hawan, Tarpan, Pithya, and funeral rites.",
        cultural_folklore="Believed to block negative energy currents and maintain ritual purity."
    ),
    "doob": KumaoniPlant(
        id="doob",
        name_kumaoni="दूर्वा / दूब",
        name_roman="Durva / Doob",
        name_hindi="दूर्वा (दूब घास)",
        scientific_name="Cynodon dactylon",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="Widespread across plains and hills",
        traditional_uses="Cooling pasture grass; wound styptic.",
        spiritual_and_temple_significance="Supreme green offering to Lord Ganesha (21 shoots of Durva). Mandatory in marriage Dhuli-argh, temple consecration, and Harela pots.",
        cultural_folklore="Symbolizes perennial regeneration and eternal family lineage."
    ),
    "jhangora": KumaoniPlant(
        id="jhangora",
        name_kumaoni="झंगोरा",
        name_roman="Jhangora",
        name_hindi="झंगोरा (सांवा)",
        scientific_name="Echinochloa frumentacea",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="800m – 2,200m",
        traditional_uses="Nutritious low-glycemic millet; cooked as mountain rice substitute or sweet kheer.",
        spiritual_and_temple_significance="Permitted sacred non-cereal grain eaten during religious fasts (Vrat) and temple vigils (Navratri, Janamashtami, Shivratri).",
        cultural_folklore="Staple of Himalayan fasting food; paired with spicy potato curry."
    ),
    "maduwa": KumaoniPlant(
        id="maduwa",
        name_kumaoni="मडुवा / कोदा",
        name_roman="Maduwa / Koda",
        name_hindi="मड़ुआ (रागी)",
        scientific_name="Eleusine coracana",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="600m – 2,400m",
        traditional_uses="Calcium-rich finger millet; ground into dark, warming flatbreads (Roti), halwa, and gruel for mountain winters.",
        spiritual_and_temple_significance="Offered at harvest rituals (Olgia / Ghee Sankranti) to thank Mother Earth and village guardians for rain and crop abundance.",
        cultural_folklore="Core food of the hardy Pahari farmer: 'Maduwa ki roti, lai ki sabzi'."
    ),
    "bhatt": KumaoniPlant(
        id="bhatt",
        name_kumaoni="भट्ट",
        name_roman="Bhatt",
        name_hindi="काला भट्ट (हिमालयी सोयाबीन)",
        scientific_name="Glycine max",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Fabaceae",
        habitat_altitude="800m – 2,200m",
        traditional_uses="Indigenous high-protein black soybean cooked into signature Kumaoni dishes: 'Bhatwani' and 'Churkani'.",
        spiritual_and_temple_significance="Prepared in community temple feasts and family gatherings during winter Sankrantis.",
        cultural_folklore="Signature pulse of Kumaon celebrated in culinary proverbs."
    ),
}


class FloraTreasury:
    """Query, inspect, and explore Kumaoni indigenous flora and sacred trees."""

    @classmethod
    def list(cls, category: Optional[str] = None) -> List[KumaoniPlant]:
        if category:
            cat_lower = category.strip().lower()
            return [p for p in FLORA_DATA.values() if cat_lower in p.category.lower()]
        return list(FLORA_DATA.values())

    @classmethod
    def get(cls, id_or_name: str) -> Optional[KumaoniPlant]:
        if not id_or_name:
            return None
        key = id_or_name.strip().lower().replace(" ", "_")
        if key in FLORA_DATA:
            return FLORA_DATA[key]
        for p in FLORA_DATA.values():
            if (id_or_name in p.name_kumaoni or
                key == p.name_roman.lower() or
                key == p.name_hindi.lower() or
                key in p.scientific_name.lower()):
                return p
        return None

    @classmethod
    def search(cls, query: str) -> List[KumaoniPlant]:
        if not query:
            return cls.list()
        q = query.strip().lower()
        results = []
        for p in FLORA_DATA.values():
            if (q in p.name_kumaoni.lower() or
                q in p.name_roman.lower() or
                q in p.name_hindi.lower() or
                q in p.scientific_name.lower() or
                q in p.category.lower() or
                q in p.botanical_family.lower() or
                q in p.traditional_uses.lower() or
                q in p.spiritual_and_temple_significance.lower() or
                q in p.cultural_folklore.lower()):
                results.append(p)
        return results

    @classmethod
    def stats(cls) -> Dict[str, Any]:
        categories: Dict[str, int] = {}
        for p in FLORA_DATA.values():
            categories[p.category] = categories.get(p.category, 0) + 1
        return {
            "total_plants": len(FLORA_DATA),
            "categories": categories,
        }
