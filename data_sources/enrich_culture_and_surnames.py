"""
Enrich words.json with authentic Kumaoni vocabulary for:
1. Musical instruments & folk performance (हुड़का, दमुवां, तुरही, रणसिंगा, मसकबीन, मोचंग, etc.)
2. Marriage & wedding ceremonies (ब्याव, जन्यांत, धुलिअर्घ, पिथ्याँ, रंग्वाली पिछौड़ा, रतजगा, etc.)
3. Extended family, kinship & social ties (काका, काकी, मामा, मामी, बड़ाबाबु, बड़ीईजा, दगड़्या, गौंत्यार, etc.)
4. Temples, holy rivers, glaciers & landscape (धाम, देवाल, थान, नौला, संगम, बुग्याल, हिमनद, etc.)
5. Caste, surnames, gotras, and social institutions (गोत्र, थात, थातवान, धड़ा, बिरादरी, पंत, जोशी, बिष्ट, etc.)
"""

import json
from pathlib import Path

DATA_PATH = Path("kumaoni/lexicon/data/words.json")

CULTURE_AND_SURNAME_WORDS = [
    # ==================== MUSICAL INSTRUMENTS & PERFORMANCE ====================
    {
        "kumaoni": "हुड़का",
        "roman": "hurka",
        "english": "traditional two-headed hourglass-shaped mountain drum played with one hand while modulating pitch with the leather shoulder strap",
        "hindi": "हुड़का (कुमाऊँनी का पारंपरिक डमरू जैसा मुख्य वाद्य)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "दमुवां",
        "roman": "damuwa",
        "english": "traditional copper kettle-drum beaten with two curved wooden sticks",
        "hindi": "दमुवां / दमामा (नगाड़े जैसा तांबे का वाद्य)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "रणसिंगा",
        "roman": "ransingha",
        "english": "ancient S-shaped long curved copper or brass war-horn blown at sacred processions and weddings",
        "hindi": "रणसिंगा (एस-आकार का युद्ध व शुभ अवसरों का बिगुल)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "तुरही",
        "roman": "turahi",
        "english": "traditional long straight brass trumpet used in temple ceremonies and folk jaats",
        "hindi": "तुरही (लंबा पीतल का फूँक वाद्य)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "डौंर",
        "roman": "daunr",
        "english": "small brass or bronze hour-glass hand drum played during esoteric Jagar spirit invocations",
        "hindi": "डौंर (जागर में प्रयुक्त होने वाला छोटा डमरू वाद्य)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "कांसी की थाली",
        "roman": "kaansi ki thaali",
        "english": "bell-metal bronze platter beaten rhythmically with a wooden stick during folk jagars and ballads",
        "hindi": "कांसी की थाली (जागर में लकड़ी की तीली से बजाई जाने वाली थाली)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "मसकबीन",
        "roman": "masakbeen",
        "english": "traditional Scottish Highland bagpipe integrated into Kumaoni weddings and festive processions",
        "hindi": "मसकबीन (पहाड़ी शादियों में बजने वाला बैगपाइप)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "मोचंग",
        "roman": "mochang",
        "english": "traditional iron jaw harp / Jew's harp held between teeth and plucked by pastoral bards",
        "hindi": "मोचंग (दाँतों में दबाकर बजाया जाने वाला लोहे का लोक वाद्य)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "हुड़किया",
        "roman": "hurkiya",
        "english": "traditional folk bard and master drummer who plays the Hurka and sings heroic ballads (Pawada) and Jagars",
        "hindi": "हुड़किया (हुड़का बजाने और गाथा गाने वाला पारंपरिक गायक)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "डांगरिया",
        "roman": "dangariya",
        "english": "medium or spiritual dancer through whom the deity or ancestral spirit speaks during a Jagar",
        "hindi": "डांगरिया (जागर में जिस पर देवता अवतरित होता है, पश्वा)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "जागरिया",
        "roman": "jagariya",
        "english": "master priest-singer who conducts the Jagar ritual and invokes the deities through sacred chants",
        "hindi": "जागरिया (जागर अनुष्ठान का मुख्य गायक व पुरोहित)",
        "pos": "noun",
        "category": "religion"
    },

    # ==================== MARRIAGE & WEDDING CEREMONIES ====================
    {
        "kumaoni": "ब्याव",
        "roman": "byaav",
        "english": "marriage / traditional wedding ceremony",
        "hindi": "विवाह / ब्याह",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "ब्यो",
        "roman": "byo",
        "english": "wedding / marriage celebration",
        "hindi": "विवाह / शादी",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "जन्यांत",
        "roman": "janyaant",
        "english": "marriage procession / groom's bridal party (baraat)",
        "hindi": "बारात (वरयात्रा)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "जंत",
        "roman": "jant",
        "english": "wedding procession / baraat",
        "hindi": "बारात",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "जन्यांती",
        "roman": "janyaanti",
        "english": "member of the groom's wedding procession / wedding guest (barati)",
        "hindi": "बाराती",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "धुलिअर्घ",
        "roman": "dhuliargh",
        "english": "sacred Vedic threshold ritual where the bride's father welcomes the groom with water, honey, curd and sacred chants",
        "hindi": "धूलिअर्घ्य (द्वार पर वर का वेदोक्त स्वागत सत्कार)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "पिथ्याँ",
        "roman": "pithyaan",
        "english": "sacred orange vermilion and turmeric rice paste mark applied on the forehead from bridge of nose to hairline with blessings",
        "hindi": "पिथ्याँ / पिथ्या (कुमाऊँनी पारंपरिक हल्दी-रोली का तिलक)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "रंग्वाली पिछौड़ा",
        "roman": "rangwali pichhauda",
        "english": "traditional saffron-yellow dupatta dyed with saffron-red concentric paisley dots and solar symbols worn by married Kumaoni women",
        "hindi": "रंग्वाली पिछौड़ा (कुमाऊँनी महिलाओं का पारंपरिक मांगलिक दुपट्टा)",
        "pos": "noun",
        "category": "clothing"
    },
    {
        "kumaoni": "अंचल",
        "roman": "anchal",
        "english": "ceremonial tying of the groom's scarf with the bride's Pichhauda during wedding circumambulations",
        "hindi": "गठबंधन / आंचल जोड़ना",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "रतजगा",
        "roman": "ratajaga",
        "english": "all-night female singing vigil held prior to a wedding or sacred ceremony with traditional mangal geet",
        "hindi": "रतजगा (मांगलिक उत्सव से पूर्व रात्रि जागरण व मंगल गायन)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "मातृका पूजा",
        "roman": "matrika puja",
        "english": "worship of the ancestral divine mothers and deities depicted in Aipan art prior to marriage",
        "hindi": "मातृका पूजा (ऐपण द्वारा चित्रित कुल देवियों की पूजा)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "शकुनाखर",
        "roman": "shakunakhar",
        "english": "auspicious traditional women's blessing hymns (Mangal Geet) sung at the commencement of all Kumaoni life-cycle rituals",
        "hindi": "शकुनाखर (मांगलिक गीतों का गायन)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "गौना",
        "roman": "gauna",
        "english": "ceremonial departure of the bride from her natal home to her husband's residence",
        "hindi": "गौना / वधू का विदा होना",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "सुहाग",
        "roman": "suhaag",
        "english": "marital auspiciousness and longevity of husband",
        "hindi": "सुहाग / सौभाग्य",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "कन्यादान",
        "roman": "kanyadaan",
        "english": "sacred ritual giving away of the bride by her parents with Vedic waters",
        "hindi": "कन्यादान",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "भातखाई",
        "roman": "bhaat-khai",
        "english": "ceremonial post-wedding feast where the newly married bride first serves boiled rice to her new in-laws",
        "hindi": "भातखाई (विवाह पश्चात पहली बार वधू द्वारा परिवार को भात परोसने की रस्म)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "सौरास",
        "roman": "sauraas",
        "english": "in-laws' home / husband's village and household",
        "hindi": "ससुराल",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "मैत",
        "roman": "mait",
        "english": "bride's parental home / maternal village (maika)",
        "hindi": "मायका / पीहर",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "दामकाज",
        "roman": "daamkaaj",
        "english": "wedding expenditures, gifts, and reciprocal hospitality arrangements",
        "hindi": "विवाह का लेन-देन व खर्च",
        "pos": "noun",
        "category": "culture"
    },

    # ==================== EXTENDED FAMILY & SOCIAL KINSHIP ====================
    {
        "kumaoni": "बड़ाबाबु",
        "roman": "badabaabu",
        "english": "father's elder brother / senior paternal uncle (tau)",
        "hindi": "ताऊजी / बड़े पिताजी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "बड़ीईजा",
        "roman": "badi-eeja",
        "english": "father's elder brother's wife / senior paternal aunt (tai)",
        "hindi": "ताईजी / बड़ी माताजी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "काका",
        "roman": "kaaka",
        "english": "paternal uncle / father's younger brother (chacha)",
        "hindi": "चाचा",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "काकी",
        "roman": "kaaki",
        "english": "paternal uncle's wife / aunt (chachi)",
        "hindi": "चाची",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "मामा",
        "roman": "maama",
        "english": "maternal uncle / mother's brother",
        "hindi": "मामा",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "मामी",
        "roman": "maami",
        "english": "maternal uncle's wife / maternal aunt",
        "hindi": "मामी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "मौसा",
        "roman": "mausa",
        "english": "mother's sister's husband / uncle",
        "hindi": "मौसाजी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "मौसी",
        "roman": "mausi",
        "english": "mother's sister / maternal aunt",
        "hindi": "मौसी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "फुफा",
        "roman": "phupha",
        "english": "father's sister's husband / uncle",
        "hindi": "फूफाजी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "फूफू",
        "roman": "phoophoo",
        "english": "father's sister / paternal aunt (bua)",
        "hindi": "बुआजी / फूफी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "भाणज",
        "roman": "bhaanaj",
        "english": "sister's son / nephew",
        "hindi": "भांजा",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "भाणजी",
        "roman": "bhaanaji",
        "english": "sister's daughter / niece",
        "hindi": "भांजी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "सौर्या",
        "roman": "saurya",
        "english": "father-in-law",
        "hindi": "ससुर",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "सासू",
        "roman": "saasu",
        "english": "mother-in-law",
        "hindi": "सास",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "जेठ",
        "roman": "jeth",
        "english": "husband's elder brother",
        "hindi": "जेठ",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "जेठानी",
        "roman": "jethaani",
        "english": "husband's elder brother's wife",
        "hindi": "जेठानी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "देवर",
        "roman": "devar",
        "english": "husband's younger brother",
        "hindi": "देवर",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "देवरानी",
        "roman": "devraani",
        "english": "husband's younger brother's wife",
        "hindi": "देवरानी",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "नणद",
        "roman": "nanad",
        "english": "husband's sister / sister-in-law",
        "hindi": "ननद",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "नंदोई",
        "roman": "nandoi",
        "english": "husband's sister's husband / brother-in-law",
        "hindi": "नंदोई",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "साला",
        "roman": "saala",
        "english": "wife's brother / brother-in-law",
        "hindi": "साला",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "साली",
        "roman": "saali",
        "english": "wife's sister / sister-in-law",
        "hindi": "साली",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "साढू",
        "roman": "saadhoo",
        "english": "co-brother-in-law / wife's sister's husband",
        "hindi": "साढ़ू भाई",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "गौंत्यार",
        "roman": "gauntyaar",
        "english": "fellow villager sharing common village territory and fellowship",
        "hindi": "गाँव का साथी / ग्रामवासी",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "हितैषी",
        "roman": "hitaishi",
        "english": "benevolent well-wisher / loyal family friend",
        "hindi": "शुभचिंतक / हितैषी",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "नातेदार",
        "roman": "naatedaar",
        "english": "relatives / kinfolk related by marriage or blood",
        "hindi": "रिश्तेदार / नातेदार",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "कुटुंब",
        "roman": "kutumb",
        "english": "extended joint family and household clan",
        "hindi": "कुटुंब / संयुक्त परिवार",
        "pos": "noun",
        "category": "kinship"
    },
    {
        "kumaoni": "खानदान",
        "roman": "khaandaan",
        "english": "ancestral family lineage / noble pedigree",
        "hindi": "खानदान / कुल",
        "pos": "noun",
        "category": "kinship"
    },

    # ==================== TEMPLES, HOLY GEOGRAPHY & NATURE ====================
    {
        "kumaoni": "धाम",
        "roman": "dhaam",
        "english": "sacred Himalayan pilgrimage sanctuary or divine abode (e.g. Jageshwar Dham, Kainchi Dham)",
        "hindi": "पवित्र धाम / तीर्थ",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "देवाल",
        "roman": "devaal",
        "english": "temple / holy house of the deity",
        "hindi": "देवालय / मन्दिर",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "मन्दिरा",
        "roman": "mandira",
        "english": "temple / shrine",
        "hindi": "मन्दिर",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "थान",
        "roman": "thaan",
        "english": "open-air village shrine or sacred sanctum where village deities are enthroned",
        "hindi": "स्थान / देवस्थान (खुला मंदिर)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "द्युप्त",
        "roman": "dyupt",
        "english": "deity / god / divine spiritual presence",
        "hindi": "देवता / देव",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "नौला",
        "roman": "naula",
        "english": "ancient architectural closed stone water sanctuary and spring temple built with stepped roofs to collect pure sub-surface groundwater",
        "hindi": "नौला (कुमाऊँनी बावड़ी / मंदिरनुमा जलस्रोत)",
        "pos": "noun",
        "category": "architecture"
    },
    {
        "kumaoni": "धारा",
        "roman": "dhaara",
        "english": "natural mountain fresh water spout flowing from carved stone animal mouths (Dhara)",
        "hindi": "धारा (पहाड़ी प्राकृतिक जलधारा / नल)",
        "pos": "noun",
        "category": "nature"
    },
    {
        "kumaoni": "कुंड",
        "roman": "kund",
        "english": "sacred stone-lined mountain water reservoir or thermal tank",
        "hindi": "कुंड / जलकुंड",
        "pos": "noun",
        "category": "nature"
    },
    {
        "kumaoni": "संगम",
        "roman": "sangam",
        "english": "sacred confluence of two or more holy Himalayan rivers (e.g. Saryu and Gomti)",
        "hindi": "संगम / दो नदियों का मिलन स्थल",
        "pos": "noun",
        "category": "geography"
    },
    {
        "kumaoni": "प्रयाग",
        "roman": "prayaag",
        "english": "holy river junction of cosmic spiritual sanctity",
        "hindi": "प्रयाग (पवित्र संगम)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "तीरथ",
        "roman": "teerath",
        "english": "holy pilgrimage destination / sacred ford",
        "hindi": "तीर्थ स्थल",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "परिक्रमा",
        "roman": "parikrama",
        "english": "ritual circumambulation around a sacred peak, temple or holy lake",
        "hindi": "परिक्रमा / प्रदक्षिणा",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "जात",
        "roman": "jaat",
        "english": "traditional sacred barefoot Himalayan pilgrimage procession (e.g. Nanda Raj Jaat, Chhipla Jaat)",
        "hindi": "जात (पहाड़ी धार्मिक तीर्थ यात्रा)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "डोलि",
        "roman": "doli",
        "english": "wooden palanquin used to carry the sacred murtis of the deities or a bride across mountain trails",
        "hindi": "डोली (देवता अथवा वधू की पालकी)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "निशान",
        "roman": "nishaan",
        "english": "sacred consecrated ceremonial banner or brass standard carried at the vanguard of deity processions",
        "hindi": "निशान (देवता का मांगलिक ध्वज)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "हिमनद",
        "roman": "himnad",
        "english": "glacier / perpetual mountain ice river (e.g. Pindari, Milam)",
        "hindi": "हिमनद / ग्लेशियर",
        "pos": "noun",
        "category": "nature"
    },
    {
        "kumaoni": "डांडा",
        "roman": "daanda",
        "english": "high mountain ridge / mountain spine",
        "hindi": "डांडा (ऊँची पर्वत श्रेणी)",
        "pos": "noun",
        "category": "geography"
    },
    {
        "kumaoni": "धुरा",
        "roman": "dhura",
        "english": "high mountain pass or crest (e.g. Devidhura, Lipudhura)",
        "hindi": "धुरा (पहाड़ी दर्रा अथवा चोटी)",
        "pos": "noun",
        "category": "geography"
    },

    # ==================== CASTE, SURNAMES, GOTRAS & SOCIAL INSTITUTIONS ====================
    {
        "kumaoni": "गोत्र",
        "roman": "gotra",
        "english": "ancestral Vedic lineage tracing patrilineal descent from a primeval sage (Bharadwaj, Kashyapa, Shandilya, Garga)",
        "hindi": "गोत्र (ऋषि परंपरा वंश)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "शाखा",
        "roman": "shaakha",
        "english": "Vedic recitation branch or genealogical subdivision of a gotra",
        "hindi": "शाखा (वैदिक शाखा / वंश की उप-शाखा)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "कुल",
        "roman": "kul",
        "english": "family dynasty / clan / lineage",
        "hindi": "कुल / वंश",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "वंश",
        "roman": "vansh",
        "english": "lineage / descent / pedigree",
        "hindi": "वंश",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "बिरादरी",
        "roman": "biraadari",
        "english": "clan brotherhood / kinship group of identical sub-caste observing mutual lifecycle duties",
        "hindi": "बिरादरी / समाज",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "थात",
        "roman": "thaat",
        "english": "ancestral landed estate and patrimony inherited across centuries",
        "hindi": "थात (पुश्तैनी भूमि व पैतृक संपत्ति)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "थातवान",
        "roman": "thaatwaan",
        "english": "original hereditary land proprietor or village founder holding ancestral soil rights",
        "hindi": "थातवान (गाँव का मूल पैतृक भूमिस्वामी)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "धड़ा",
        "roman": "dhadha",
        "english": "historic political factional alliance in medieval Kumaon (the Mahara and Fartyal factions)",
        "hindi": "धड़ा (मध्यकालीन कुमाऊँ के दो प्रमुख राजनीतिक गुट: महरा व फर्त्याल)",
        "pos": "noun",
        "category": "history"
    },
    {
        "kumaoni": "जाति",
        "roman": "jaati",
        "english": "caste / community / social group",
        "hindi": "जाति",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "जजमानी",
        "roman": "jajmaani",
        "english": "traditional patron-client economic network of mutual ritual services between landholders, priests, and artisans",
        "hindi": "जजमानी प्रथा (पारस्परिक सेवा व संबंध व्यवस्था)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "नेग-जोग",
        "roman": "neg-jog",
        "english": "customary ceremonial perquisites and cash or clothing gifts distributed during rites of passage",
        "hindi": "नेग-जोग (शुभ अवसरों पर दिया जाने वाला पारंपरिक उपहार)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "हुक्का-पाणी",
        "roman": "hukka-paani",
        "english": "social commensality and community acceptance within the clan assembly",
        "hindi": "हुक्का-पानी (सामाजिक सहभोज व बिरादरी संबंध)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "शिल्पकार",
        "roman": "shilpkaar",
        "english": "traditional master artisan communities of Kumaon (coppersmiths, masons, ironsmiths, weavers)",
        "hindi": "शिल्पकार (कुमाऊँ के पारंपरिक दस्तकार व कारीगर)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "ताम्रकार",
        "roman": "taamrakaar",
        "english": "master coppersmith artisans of Almora famous for handcrafted hammered vessels",
        "hindi": "ताम्रकार / टम्टा (तांबे के बर्तन बनाने वाले कारीगर)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "शौका",
        "roman": "shauka",
        "english": "trans-Himalayan high-altitude trader community of Johar, Darma, and Byans valleys (Bhotia)",
        "hindi": "शौका (जोहार व दारमा के उच्च हिमालयी व्यापारी व निवासी)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "खस",
        "roman": "khas",
        "english": "ancient indigenous Aryan hill folk who inhabited the Central Himalayas since Vedic times",
        "hindi": "खस (मध्य हिमालय की प्राचीन निवासी जाति)",
        "pos": "noun",
        "category": "history"
    },

    # ==================== HISTORICAL KUMAONI SURNAMES AS DICTIONARY WORDS ====================
    {
        "kumaoni": "पंत",
        "roman": "pant",
        "english": "Pant (prominent Kumaoni Brahmin surname tracing to Jaideo Pant; scholars, physicians, and poets)",
        "hindi": "पंत (कुमाऊँ का प्रतिष्ठित ब्राह्मण उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "जोशी",
        "roman": "joshi",
        "english": "Joshi (esteemed Kumaoni Brahmin surname of prime ministers, astrologers, and diwans under Chand kings)",
        "hindi": "जोशी (कुमाऊँ के दीवान व ज्योतिषी ब्राह्मण)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "पाण्डे",
        "roman": "pande",
        "english": "Pande / Pandey (historic Kumaoni Brahmin surname of preceptors, scholars, and historians)",
        "hindi": "पाण्डे / पांडे (कुमाऊँनी ब्राह्मण उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "उप्रेती",
        "roman": "upreti",
        "english": "Upreti (prominent Kumaoni Brahmin surname originating from Uprara village; scholars and priests)",
        "hindi": "उप्रेती (उपराड़ा गाँव से उद्भूत ब्राह्मण उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "तिवारी",
        "roman": "tiwari",
        "english": "Tiwari / Tripathi (prominent Kumaoni Brahmin surname of Vedic preceptors)",
        "hindi": "तिवारी (कुमाऊँनी ब्राह्मण उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "पाठक",
        "roman": "pathak",
        "english": "Pathak (Kumaoni Brahmin surname of Vedic reciters and scholars)",
        "hindi": "पाठक (कुमाऊँनी ब्राह्मण उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "भट्ट",
        "roman": "bhatt",
        "english": "Bhatt (historic Kumaoni Brahmin surname of hereditary priests at Jageshwar and major shrines)",
        "hindi": "भट्ट (जागेश्वर आदि धामों के मुख्य पुजारी ब्राह्मण)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "बिष्ट",
        "roman": "bisht",
        "english": "Bisht (widespread Kumaoni Kshatriya/Rajput surname derived from Sanskrit 'Vishisht'; military commanders and feudal lords)",
        "hindi": "बिष्ट (विशिष्ट से उद्भूत कुमाऊँनी क्षत्रिय/राजपूत उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "रावत",
        "roman": "rawat",
        "english": "Rawat (esteemed Kumaoni Kshatriya and Johari Shauka surname of feudal chiefs and explorers)",
        "hindi": "रावत (कुमाऊँनी राजपूत व जोहारी शौका उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "नेगी",
        "roman": "negi",
        "english": "Negi (renowned martial Kumaoni and Garhwali Rajput surname of military officers holding 'Neg' entitlements)",
        "hindi": "नेगी (सैनिक व प्रशासनिक राजपूत उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "मेहरा",
        "roman": "mehra",
        "english": "Mehra / Mahara (influential Kumaoni Rajput clan of Kali Kumaon; leaders of the Mahara faction)",
        "hindi": "मेहरा / महरा (काली कुमाऊँ का प्रमुख राजपूत कुल)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "फर्त्याल",
        "roman": "fartyal",
        "english": "Fartyal (historic Kumaoni Rajput clan of Kali Kumaon; leaders of the Fartyal faction)",
        "hindi": "फर्त्याल (काली कुमाऊँ का प्रमुख राजपूत कुल)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "भंडारी",
        "roman": "bhandari",
        "english": "Bhandari (Kumaoni Rajput surname of royal treasury custodians and military generals)",
        "hindi": "भंडारी (राजकीय कोषाध्यक्ष व वीर योद्धा राजपूत)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "कार्की",
        "roman": "karki",
        "english": "Karki (martial Kumaoni Rajput surname of Kali Kumaon and border fortresses)",
        "hindi": "कार्की (काली कुमाऊँ का क्षत्रिय उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "रौतेला",
        "roman": "rautela",
        "english": "Rautela (royal Kshatriya surname of younger princes and cadet branches of the Chand dynasty)",
        "hindi": "रौतेला (चंद राजवंश के राजकुमारों का कुल)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "मनराल",
        "roman": "manral",
        "english": "Manral (royal Kshatriya surname of Katyuri dynasty descendant princes in Pali-Pachhaun)",
        "hindi": "मनराल (कत्यूरी राजवंश के वंशज)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "बोरा",
        "roman": "bora",
        "english": "Bora (prominent Kumaoni agricultural and administrative Rajput clan)",
        "hindi": "बोरा (कुमाऊँनी क्षत्रिय कुल)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "अधिकारी",
        "roman": "adhikari",
        "english": "Adhikari (Kumaoni Rajput surname representing royal officers of administrative authority)",
        "hindi": "अधिकारी (प्रशासनिक अधिकारी राजपूत उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "मेहता",
        "roman": "mehta",
        "english": "Mehta (Kumaoni Rajput surname of village nobles and estate managers)",
        "hindi": "मेहता (कुमाऊँनी क्षत्रिय उपनाम)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "दानू",
        "roman": "danu",
        "english": "Danu (martial Rajput chieftains of Danpur and upper Pindar valley)",
        "hindi": "दानू (दानपुर के क्षत्रिय)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "कोरंगा",
        "roman": "koranga",
        "english": "Koranga (valiant highland Rajput clan of Bageshwar and Kapkot)",
        "hindi": "कोरंगा (बागेश्वर व दानपुर का क्षत्रिय कुल)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "पांगती",
        "roman": "pangtey",
        "english": "Pangtey (renowned Johar Shauka clan of scholars, alpine merchants, and cartographers)",
        "hindi": "पांगती (जोहार शौका का प्रतिष्ठित विद्वान व व्यापारी कुल)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "मर्तोलिया",
        "roman": "martolia",
        "english": "Martolia (illustrious Johar Shauka clan of Martoli village beneath Nanda Devi)",
        "hindi": "मर्तोलिया (मर्तोली गाँव के उच्च हिमालयी व्यापारी)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "टम्टा",
        "roman": "tamta",
        "english": "Tamta (master coppersmith artisan clan of Almora renowned for hand-hammered copper vessels and social reform)",
        "hindi": "टम्टा (अल्मोड़ा के विश्वविख्यात ताम्रकार व समाज सुधारक कुल)",
        "pos": "noun",
        "category": "society"
    },
    {
        "kumaoni": "आर्य",
        "roman": "arya",
        "english": "Arya (Kumaoni surname adopted by freedom fighters and reformers during the social awakening of the early 20th century)",
        "hindi": "आर्य (कुमाऊँ में स्वाधीनता व सामाजिक जागरण का उपनाम)",
        "pos": "noun",
        "category": "society"
    }
]


def enrich():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        existing_words = json.load(f)

    existing_kumaoni_set = {w["kumaoni"].strip() for w in existing_words}
    added_count = 0

    for item in CULTURE_AND_SURNAME_WORDS:
        k = item["kumaoni"].strip()
        if k not in existing_kumaoni_set:
            existing_words.append(item)
            existing_kumaoni_set.add(k)
            added_count += 1

    # Sort alphabetically by Kumaoni word
    existing_words.sort(key=lambda x: x["kumaoni"])

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(existing_words, f, ensure_ascii=False, indent=2)

    print(f"Successfully added {added_count} new cultural, musical, marriage, kinship, and surname words.")
    print(f"Total base dictionary size is now: {len(existing_words)} lemmas.")


if __name__ == "__main__":
    enrich()
