"""
Comprehensive enrichment pipeline for Kumaoni language library:
Ingests authentic vocabulary, plants, temple implements, and child lifecycle words into:
1. kumaoni/lexicon/data/words.json (250+ new authenticated base lemmas)
2. kumaoni/culture/flora.py (28 new sacred trees, alpine blooms, medicinal herbs, crops)
3. kumaoni/culture/rituals.py (27 new temple implements, hawan vessels, ritual articles)
"""

import json
from pathlib import Path

# Paths
WORDS_JSON_PATH = Path("kumaoni/lexicon/data/words.json")

NEW_DICTIONARY_WORDS = [
    # ==================== 1. SCHOOL & EDUCATION ====================
    {
        "kumaoni": "ईस्कूल",
        "roman": "eeskool",
        "english": "school / village educational academy",
        "hindi": "विद्यालय / स्कूल / पाठशाला",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "चटशाल",
        "roman": "chatshaal",
        "english": "traditional elementary pathshala / primary village school",
        "hindi": "चटशाल / प्रारंभिक पाठशाला",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "मास्साब",
        "roman": "maassaab",
        "english": "schoolteacher / master / schoolmaster",
        "hindi": "मास्टर साहब / शिक्षक / अध्यापक",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "गुरुजी",
        "roman": "guruji",
        "english": "respected teacher / spiritual preceptor",
        "hindi": "गुरुजी / शिक्षक",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "च्यला",
        "roman": "chyala",
        "english": "male pupil / schoolboy / disciple",
        "hindi": "छात्र / शिष्य / बालक",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "च्यली",
        "roman": "chyali",
        "english": "female pupil / schoolgirl / disciple",
        "hindi": "छात्रा / शिष्या / बालिका",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "पाथरी",
        "roman": "paathri",
        "english": "slate tablet split from mountain rock for school writing",
        "hindi": "पाथरी / स्लेट (पत्थर की पट्टी)",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "बत्ती",
        "roman": "batti",
        "english": "slate pencil carved from soft soapstone for writing on slate",
        "hindi": "बत्ती / स्लेटी (स्लेट पर लिखने की खड़िया)",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "दुधि-खड़िया",
        "roman": "dudhi-khadiya",
        "english": "white mineral chalk dug from mountain lime deposits for writing",
        "hindi": "खड़िया / सफेद चाक",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "मसवाणी",
        "roman": "maswaani",
        "english": "traditional brass or terracotta inkpot",
        "hindi": "दवात / मसिया / मसिपात्र",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "मसि",
        "roman": "masi",
        "english": "black permanent ink brewed from pine soot lampblack",
        "hindi": "स्याही / मसि",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "नरकट",
        "roman": "narkat",
        "english": "sharpened hollow river-reed pen / reed quill",
        "hindi": "नरकट की कलम",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "कागत",
        "roman": "kaagat",
        "english": "paper sheet / document leaf",
        "hindi": "कागज / पन्ना",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "पोथी",
        "roman": "pothi",
        "english": "manuscript volume / scholarly book / sacred scripture",
        "hindi": "पोथी / पुस्तक / ग्रंथ",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "चोपड़ी",
        "roman": "chopdi",
        "english": "hand-stitched exercise notebook / student writing booklet",
        "hindi": "कापी / छोटी पुस्तिका",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "झोली",
        "roman": "jholi",
        "english": "cloth shoulder bag / fabric satchel for slates and primers",
        "hindi": "झोली / कंधे का बस्ता",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "बस्ता",
        "roman": "basta",
        "english": "school satchel / book knapsack",
        "hindi": "बस्ता / स्कूल बैग",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "घंटी",
        "roman": "ghanti",
        "english": "brass school bell ringing to mark periods and dismissal",
        "hindi": "घंटी",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "बांचण",
        "roman": "baanchan",
        "english": "to read aloud / to recite lessons or letters",
        "hindi": "बांचना / सस्वर पढ़ना",
        "pos": "verb",
        "category": "education"
    },
    {
        "kumaoni": "घोटण",
        "roman": "ghotan",
        "english": "to memorize rigorously by rote / to cram tables and poems",
        "hindi": "घोटना / रटना / कंठस्थ करना",
        "pos": "verb",
        "category": "education"
    },
    {
        "kumaoni": "परखा",
        "roman": "parkha",
        "english": "examination / trial of scholarship / academic test",
        "hindi": "परीक्षा / परख / जांच",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "गुणी",
        "roman": "guni",
        "english": "learned / intellectually accomplished scholar",
        "hindi": "गुणी / विद्वान / शिक्षित",
        "pos": "adjective",
        "category": "education"
    },
    {
        "kumaoni": "पठवार",
        "roman": "pathwaar",
        "english": "studious scholar / attentive reader",
        "hindi": "विद्यार्थी / अध्येता",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "बेत",
        "roman": "bet",
        "english": "thin flexible cane used by teachers for school discipline",
        "hindi": "बेंत / छड़ी",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "हाजिरी",
        "roman": "haajiri",
        "english": "morning roll-call attendance in class",
        "hindi": "उपस्थिति / हाजिरी",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "छुट्टी",
        "roman": "chhutti",
        "english": "school vacation / recess / dismissal bell",
        "hindi": "छुट्टी / अवकाश",
        "pos": "noun",
        "category": "education"
    },
    {
        "kumaoni": "साबासी",
        "roman": "saabaasi",
        "english": "verbal praise / teacher's blessing for academic excellence",
        "hindi": "शाबाशी / प्रशंसा",
        "pos": "noun",
        "category": "education"
    },

    # ==================== 2. JOBS, GOVERNMENT JOBS, OFFICE & WORK ====================
    {
        "kumaoni": "सरकारी नौकरी",
        "roman": "sarkaari naukari",
        "english": "permanent government job / civil service post",
        "hindi": "सरकारी नौकरी",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "सर्करी नकर",
        "roman": "sarkari naukar",
        "english": "government employee / public civil servant",
        "hindi": "सरकारी कर्मचारी / मुलाजिम",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "रोजगार",
        "roman": "rojgaar",
        "english": "gainful employment / livelihood / vocation",
        "hindi": "रोजगार / आजीविका",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "काज",
        "roman": "kaaj",
        "english": "official assigned work / duty / task",
        "hindi": "काज / कार्य / काम",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "तलब",
        "roman": "talab",
        "english": "monthly wage stipend / salary pay",
        "hindi": "वेतन / तलब / पगार",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "तनख्वाह",
        "roman": "tankhaah",
        "english": "monthly fixed salary wages",
        "hindi": "तनख्वाह / पगार",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "ब्याण",
        "roman": "byaan",
        "english": "daily wage paid for manual agricultural or mason labor",
        "hindi": "दहाड़ी / दैनिक मजदूरी",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "पैंसन",
        "roman": "paensan",
        "english": "monthly post-retirement government pension stipend",
        "hindi": "पेंशन / सेवानिवृत्ति भत्ता",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "भत्ता",
        "roman": "bhatta",
        "english": "daily subsistence allowance / official travel stipend",
        "hindi": "भत्ता",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "हाकिम",
        "roman": "haakim",
        "english": "presiding magistrate / supreme executive officer",
        "hindi": "हाकिम / उच्चाधिकारी / मजिस्ट्रेट",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "अफसर",
        "roman": "afsar",
        "english": "gazetted officer / bureaucrat",
        "hindi": "अफसर / अधिकारी",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "पटवारी",
        "roman": "patwari",
        "english": "hill revenue officer possessing combined police and land registration powers in Uttarakhand",
        "hindi": "पटवारी (राजस्व व पुलिस शक्ति युक्त अधिकारी)",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "कानूनगो",
        "roman": "kanoongo",
        "english": "supervisory land records revenue officer above the patwari",
        "hindi": "कानूनगो",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "बाबू",
        "roman": "babu",
        "english": "desk clerk / office copyist / administrative assistant",
        "hindi": "बाबू / लिपिक",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "मुंशी",
        "roman": "munshi",
        "english": "court record-keeper / lawyer's legal clerk / accountant",
        "hindi": "मुंशी / लेखक",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "चपरासी",
        "roman": "chapraasi",
        "english": "office peon / attendant messenger",
        "hindi": "चपरासी / अर्दली",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "अर्दली",
        "roman": "ardali",
        "english": "personal orderly assigned to high district judges and magistrates",
        "hindi": "अर्दली / सेवक",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "चौकीदार",
        "roman": "chaukidaar",
        "english": "village sentry / night guard / watchman",
        "hindi": "चौकीदार / पहरेदार",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "दफ्तर",
        "roman": "daftar",
        "english": "administrative government office / workplace",
        "hindi": "कार्यालय / दफ्तर",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "कचहरी",
        "roman": "kachhari",
        "english": "judicial courthouse and district collectorate complex",
        "hindi": "कचहरी / न्यायालय",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "तहसील",
        "roman": "tehsil",
        "english": "sub-divisional revenue administrative headquarters",
        "hindi": "तहसील",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "ठाणा",
        "roman": "thaana",
        "english": "police outpost / station",
        "hindi": "थाना / पुलिस चौकी",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "डाकखाना",
        "roman": "daakkhaana",
        "english": "postal mail delivery office",
        "hindi": "डाकघर",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "अर्जी",
        "roman": "arzi",
        "english": "formal handwritten legal petition or citizen appeal to authority",
        "hindi": "प्रार्थना-पत्र / अर्जी",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "दरखास्त",
        "roman": "darkhaast",
        "english": "formal employment or grievance application",
        "hindi": "दरख्वास्त / आवेदन",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "मिसिल",
        "roman": "misil",
        "english": "bound official case dossier / historical legal record file",
        "hindi": "मिसिल / केस फाइल",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "मोहर",
        "roman": "mohar",
        "english": "official brass or rubber seal of administrative authority",
        "hindi": "मुहर / सील",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "दस्तखत",
        "roman": "dastkhat",
        "english": "formal handwritten signature on official parchment",
        "hindi": "हस्ताक्षर / दस्तखत",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "सही",
        "roman": "sahi",
        "english": "signature / endorsement approval mark",
        "hindi": "हस्ताक्षर / सही करना",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "अंगूठा छापो",
        "roman": "angootha chhaapo",
        "english": "thumb impression fingerprint endorsement on land deeds",
        "hindi": "अंगूठे का निशान",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "बही-खाता",
        "roman": "bahi-khaata",
        "english": "traditional red cloth-bound accounting ledger and land registry",
        "hindi": "बही-खाता / रजिस्टर",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "टिकट",
        "roman": "tikat",
        "english": "revenue stamp affixed to legal petitions and court plaints",
        "hindi": "राजस्व टिकट",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "हुकमनामा",
        "roman": "hukamnaama",
        "english": "written executive decree / judicial writ",
        "hindi": "आदेश-पत्र / हुक्मनामा",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "परवाना",
        "roman": "parwaana",
        "english": "official court warrant / authoritative summon notice",
        "hindi": "परवाना / अधिपत्र",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "तबादला",
        "roman": "tabaadla",
        "english": "administrative transfer of a government officer to another post",
        "hindi": "स्थानांतरण / तबादला",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "तरक्की",
        "roman": "tarakki",
        "english": "job promotion / official rank advancement",
        "hindi": "पदोन्नति / तरक्की",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "रुकसत",
        "roman": "ruksat",
        "english": "sanctioned official leave of absence from employment",
        "hindi": "अवकाश / छुट्टी",
        "pos": "noun",
        "category": "work"
    },
    {
        "kumaoni": "इस्तिफा",
        "roman": "istipha",
        "english": "formal voluntary resignation from service",
        "hindi": "इस्तीफा / त्यागपत्र",
        "pos": "noun",
        "category": "work"
    },

    # ==================== 3. BUSINESS, COMMERCE & TRADE ====================
    {
        "kumaoni": "ब्यापार",
        "roman": "byaapaar",
        "english": "commercial trade / merchant business enterprise",
        "hindi": "व्यापार / वाणिज्य",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "कारोबार",
        "roman": "kaarobaar",
        "english": "business affairs / market transactions",
        "hindi": "कारोबार / व्यवसाय",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "दुकान",
        "roman": "dukaan",
        "english": "retail shop / merchant stall in bazaar",
        "hindi": "दुकान",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "बणिया",
        "roman": "baniya",
        "english": "traditional hill grocer / merchant shopkeeper",
        "hindi": "बनिया / दुकानदार",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "महाजन",
        "roman": "mahaajan",
        "english": "rural financier / affluent moneylender",
        "hindi": "महाजन / साहूकार",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "साहुकार",
        "roman": "saahukaar",
        "english": "merchant banker extending agricultural credit",
        "hindi": "साहूकार",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "गराक",
        "roman": "garaak",
        "english": "purchasing customer / retail client",
        "hindi": "ग्राहक / खरीदार",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "लेणहार",
        "roman": "lenhaar",
        "english": "creditor / one who has legal claims to receive funds",
        "hindi": "लेनदार / ग्राहक",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "सौदा",
        "roman": "sauda",
        "english": "mercantile trade deal / commercial bargain",
        "hindi": "सौदा / व्यापारिक समझौता",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "बयाना",
        "roman": "bayaana",
        "english": "earnest money / advance cash sealing a purchase contract",
        "hindi": "बयाना / अग्रिम राशि",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "पूँजी",
        "roman": "poonji",
        "english": "commercial capital / principal investment money",
        "hindi": "पूंजी / मूलधन",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "लागत",
        "roman": "laagat",
        "english": "cost of production / total capital expended",
        "hindi": "लागत",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "नफा",
        "roman": "napha",
        "english": "net financial profit / financial gain",
        "hindi": "लाभ / नफा",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "मुनाफा",
        "roman": "munaapha",
        "english": "commercial profit margin / business return",
        "hindi": "मुनाफा / लाभ",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "तोटा",
        "roman": "tota",
        "english": "financial shortfall / commercial loss",
        "hindi": "घाटा / नुकसान / तोटा",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "घाटा",
        "roman": "ghaata",
        "english": "monetary loss / operating deficit",
        "hindi": "घाटा",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "उधारी",
        "roman": "udhaari",
        "english": "goods taken on credit / deferred debt",
        "hindi": "उधार / उधारी",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "ऋण",
        "roman": "rin",
        "english": "monetary loan / formal indebtedness",
        "hindi": "ऋण / कर्ज",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "सूद",
        "roman": "sood",
        "english": "accrued interest charge on borrowed money",
        "hindi": "ब्याज / सूद",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "ब्याज",
        "roman": "byaaj",
        "english": "interest percentage on cash debts",
        "hindi": "ब्याज",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "बट्टा",
        "roman": "batta",
        "english": "commercial discount / deduction given on cash payment",
        "hindi": "बट्टा / छूट / डिस्काउंट",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "मंडी",
        "roman": "mandi",
        "english": "wholesale grain and fruit marketplace",
        "hindi": "मंडी / थोक बाजार",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "तराजू",
        "roman": "taraaju",
        "english": "twin-pan mechanical balance scale for weighing merchandise",
        "hindi": "तराजू",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "बाँट",
        "roman": "baant",
        "english": "stamped iron weight standards (seer, chhatak, tola, kilogram)",
        "hindi": "बाट / वजन",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "गुदाम",
        "roman": "gudaam",
        "english": "storage warehouse for merchant cargo and grains",
        "hindi": "गोदाम",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "शौका ब्यापारी",
        "roman": "shauka byaapaari",
        "english": "heroic trans-Himalayan Johari salt, borax, and pashmina wool merchant",
        "hindi": "शौका व्यापारी (तिब्बत-भारत व्यापार करने वाले)",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "सट्टा",
        "roman": "satta",
        "english": "speculative trade wagering / betting on market futures",
        "hindi": "सट्टा / जुआ",
        "pos": "noun",
        "category": "economy"
    },
    {
        "kumaoni": "हाट",
        "roman": "haat",
        "english": "weekly pastoral market bazaar in mountain valleys",
        "hindi": "हाट / साप्ताहिक बाजार",
        "pos": "noun",
        "category": "economy"
    },

    # ==================== 4. CORRUPTION, SCAMS, ROBBERY, CRIME & JUSTICE ====================
    {
        "kumaoni": "घूस",
        "roman": "ghoos",
        "english": "illicit bribe paid to bureaucrats to subvert justice",
        "hindi": "रिश्वत / घूस",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "रिश्वत",
        "roman": "rishwat",
        "english": "underhand bribe / illegal gratification",
        "hindi": "रिश्वत",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "डाली-भेंट",
        "roman": "daali-bhent",
        "english": "customary ceremonial fruit basket morphed into coerced bureaucratic tribute",
        "hindi": "डाली-भेंट (अफसरों को दी जाने वाली भेंट)",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "हाथ गरम करण",
        "roman": "haath garam karan",
        "english": "to bribe someone / grease someone's palm (idiom)",
        "hindi": "हाथ गर्म करना (रिश्वत देना)",
        "pos": "verb",
        "category": "crime"
    },
    {
        "kumaoni": "घोटाला",
        "roman": "ghotaala",
        "english": "major financial embezzlement scam / swindle of public funds",
        "hindi": "घोटाला / गबन",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "गोलमाल",
        "roman": "golmaal",
        "english": "fraudulent manipulation / underhand financial foul play",
        "hindi": "गोलमाल / धांधली",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "ठग",
        "roman": "thag",
        "english": "deceitful conman / imposter swindler",
        "hindi": "ठग / धोखेबाज",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "ठगी",
        "roman": "thagi",
        "english": "crafty confidence trick / fraud racket",
        "hindi": "ठगी / धोखाधड़ी",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "छल-कपट",
        "roman": "chhal-kapat",
        "english": "malicious deceit / treacherous treachery",
        "hindi": "छल-कपट / धोखा",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "धोखाधड़ी",
        "roman": "dhokhaadhadi",
        "english": "deliberate fraud / criminal breach of trust",
        "hindi": "धोखाधड़ी",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "जालसाजी",
        "roman": "jaalsaaji",
        "english": "forgery of revenue records, stamps, or official seals",
        "hindi": "जालसाजी / कूट-रचना",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "हक मारण",
        "roman": "hak maaran",
        "english": "usurping or stealing someone's rightful legal or moral due",
        "hindi": "हक मारना / अधिकार छीनना",
        "pos": "verb",
        "category": "crime"
    },
    {
        "kumaoni": "चूंघण",
        "roman": "choonghan",
        "english": "extorting resources parasitical to the bone / bloodsucking",
        "hindi": "चूसना / शोषण करना",
        "pos": "verb",
        "category": "crime"
    },
    {
        "kumaoni": "चोरी",
        "roman": "chori",
        "english": "larceny / theft / clandestine stealing",
        "hindi": "चोरी",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "चोर",
        "roman": "chor",
        "english": "burglary thief / prowler",
        "hindi": "चोर",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "डाका",
        "roman": "daaka",
        "english": "armed raid / gang robbery of a household",
        "hindi": "डाका / डकैती",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "डकैती",
        "roman": "dakaiti",
        "english": "armed gang robbery with violence",
        "hindi": "डकैती",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "डकैत",
        "roman": "dakait",
        "english": "armed highwayman / bandit / dacoit",
        "hindi": "डकैत / डाकू",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "लुटैर",
        "roman": "lutair",
        "english": "plunderer / violent highway robber",
        "hindi": "लुटेरा",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "लूट-खसोट",
        "roman": "loont-khasot",
        "english": "violent extortion, pillage, and systemic looting",
        "hindi": "लूट-खसोट / लूटपाट",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "सेंध मारण",
        "roman": "sendh maaran",
        "english": "breaking through the stone wall of a house for nighttime burglary",
        "hindi": "सेंध मारना (घर की दीवार फोड़कर चोरी)",
        "pos": "verb",
        "category": "crime"
    },
    {
        "kumaoni": "जेबकटो",
        "roman": "jebkato",
        "english": "pickpocket active in crowded weekly haats and fairs",
        "hindi": "जेबकतरा",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "झपटमारी",
        "roman": "jhapatmaari",
        "english": "snatching ornaments or purses from pedestrians",
        "hindi": "झपटमारी",
        "pos": "noun",
        "category": "crime"
    },
    {
        "kumaoni": "हथकड़ी",
        "roman": "hathkadi",
        "english": "iron handcuffs applied upon arrested culprits",
        "hindi": "हथकड़ी",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "हवालात",
        "roman": "hawaalaat",
        "english": "police lockup holding cell prior to magistrate remand",
        "hindi": "हवालात / बंदीगृह",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "कैदखाना",
        "roman": "kaidkhaana",
        "english": "district prison / penitentiary jail",
        "hindi": "जेल / कारागार",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "कैदी",
        "roman": "kaidi",
        "english": "incarcerated convict / prisoner",
        "hindi": "कैदी / बंदी",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "मुलजिम",
        "roman": "muljim",
        "english": "accused defendant undergoing trial",
        "hindi": "आरोपी / मुलजिम",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "गवाह",
        "roman": "gawaah",
        "english": "eyewitness presenting factual evidence in court",
        "hindi": "गवाह / साक्षी",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "गवाही",
        "roman": "gawaahi",
        "english": "sworn deposition / witness statement",
        "hindi": "गवाही / बयान",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "फैसला",
        "roman": "faisla",
        "english": "binding judicial judgment / verdict of justice",
        "hindi": "निर्णय / फैसला",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "सजा",
        "roman": "saja",
        "english": "judicial sentence / penal punishment",
        "hindi": "सजा / दंड",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "जमानत",
        "roman": "zamaanat",
        "english": "court surety release / bail bond",
        "hindi": "जमानत",
        "pos": "noun",
        "category": "governance"
    },
    {
        "kumaoni": "दण्ड",
        "roman": "dand",
        "english": "judicial penalty / monetary fine",
        "hindi": "दंड / जुर्माना",
        "pos": "noun",
        "category": "governance"
    },

    # ==================== 5. HOME THINGS, UTENSILS, KITCHENWARE & CROCKERY ====================
    {
        "kumaoni": "भाण्ड",
        "roman": "bhaand",
        "english": "general domestic utensils, crockery, and tableware",
        "hindi": "बर्तन / बासन",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "बासन",
        "roman": "baasan",
        "english": "kitchen cooking pots and eating vessels",
        "hindi": "बर्तन / बासन",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "ताँबी",
        "roman": "taambi",
        "english": "large hammered pure copper urn for mountain spring water",
        "hindi": "तांबे की गागर",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "लोटा",
        "roman": "lota",
        "english": "traditional round brass or bronze water pitcher",
        "hindi": "लोटा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "मटुको",
        "roman": "matuko",
        "english": "earthen terracotta pot for chilling mountain drinking water",
        "hindi": "मटका / घड़ा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "हँड़िया",
        "roman": "handiya",
        "english": "wide-bellied earthen clay pot for slow cooking hill lentils",
        "hindi": "हांड़ी / मटकी",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "थलिया",
        "roman": "thaliya",
        "english": "small brass dinner platter for children or side dishes",
        "hindi": "छोटी थाली",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "बटकी",
        "roman": "batki",
        "english": "traditional deep bell-metal bronze bowl for lentil soup and jholi",
        "hindi": "कटोरी / बटकी (कांसे की कटोरी)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "डब्बू",
        "roman": "dabbu",
        "english": "deep hemispherical metal ladle for scooping dal and gravies",
        "hindi": "डब्बू / गहरा चमचा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "कड़छी",
        "roman": "kadchhi",
        "english": "curved serving spoon / metal ladle",
        "hindi": "कड़छी",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "तवा",
        "roman": "tawa",
        "english": "heavy circular convex iron griddle for baking wheat rotis",
        "hindi": "तवा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "कड़ाही",
        "roman": "kadaahi",
        "english": "deep heavy-gauge iron or brass wok for frying and curries",
        "hindi": "कड़ाही",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "चिमटो",
        "roman": "chimto",
        "english": "wrought-iron hearth tongs for holding coals and turning breads",
        "hindi": "चिमटा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "सँड़ासी",
        "roman": "sandaasi",
        "english": "hinged iron pincers used to safely lift boiling pots off the fire",
        "hindi": "सँड़ासी",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "फुकणी",
        "roman": "phukni",
        "english": "hollow metal or bamboo blowpipe for blowing air into the hearth fire",
        "hindi": "फुकनी",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "सिल-लोटा",
        "roman": "sil-lota",
        "english": "granite grinding slab and cylindrical muller stone for fresh chutneys",
        "hindi": "सिल-बट्टा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "जांतो",
        "roman": "jaanto",
        "english": "paired rotary stone mill quern for grinding wheat and mandua flour",
        "hindi": "जांत / हाथ की चक्की",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "ढीकी",
        "roman": "dheeki",
        "english": "foot-operated lever wooden treadle for husking paddy into rice",
        "hindi": "ढेंकी (पैर से चलने वाली धान कूटनी)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "ठेकी",
        "roman": "theki",
        "english": "artisan-turned wooden cylinder for churning mountain yoghurt into butter",
        "hindi": "ठेकी (दही मथने का लकड़ी का बर्तन)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "मधानी",
        "roman": "madhaani",
        "english": "serrated wooden churner rod inserted into the yoghurt theki",
        "hindi": "मथानी",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "नेती",
        "roman": "neti",
        "english": "double leather pulling rope wrapped around the madhani churner",
        "hindi": "नेती (मथानी की रस्सी)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "सुपो",
        "roman": "supo",
        "english": "woven hill bamboo winnowing fan for separating grain from chaff",
        "hindi": "सूप / सूपड़ा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "डलिया",
        "roman": "daliya",
        "english": "circular shallow basket woven from fine ringal mountain bamboo",
        "hindi": "डलिया / छोटी टोकरी",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "डोका",
        "roman": "doka",
        "english": "tall conical bamboo back-basket supported by a forehead tumpline strap",
        "hindi": "डोका (पीठ पर लादने वाली बड़ी टोकरी)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "नाम",
        "roman": "naam",
        "english": "braided hemp tumpline headstrap worn across forehead to support doka basket",
        "hindi": "नाम (डोके का माथे पर लगने वाला पट्टा)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "पीढ़ा",
        "roman": "peedha",
        "english": "low four-legged pine wood seat used during meals and puja",
        "hindi": "पीढ़ा / पाटा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "पिंगलो",
        "roman": "pinglo",
        "english": "miniature wooden low stool for sitting near the hearth",
        "hindi": "छोटा पीढ़ा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "चुलहो",
        "roman": "chulho",
        "english": "three-stone clay-plastered cooking hearth and domestic fireplace",
        "hindi": "चूल्हा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "ओदान",
        "roman": "odaan",
        "english": "triangular wrought-iron tripod trivet set over burning coals",
        "hindi": "ओदान (चूल्हे का लोहे का तिपाया)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "कौलो",
        "roman": "kaulo",
        "english": "glowing live ember bed resting inside the chulha hearth",
        "hindi": "दहकता अंगारा / कौला",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "छार",
        "roman": "chhaar",
        "english": "fine white wood ash residue from hearth fire, used to scrub copper vessels",
        "hindi": "राख / छार",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "ताखली",
        "roman": "taakhli",
        "english": "arched recessed wall niche for keeping lamps and small trinkets",
        "hindi": "ताक / आले की ताखली",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "सन्दूक",
        "roman": "sandook",
        "english": "massive iron-reinforced heirloom wooden storage chest for blankets and valuables",
        "hindi": "संदूक / बड़ा बक्सा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "पेटी",
        "roman": "peti",
        "english": "wooden or sheet-metal storage trunk for blankets and dowry fabrics",
        "hindi": "पेटी / ट्रंक",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "खाट",
        "roman": "khaat",
        "english": "solid pine four-legged string cot bed",
        "hindi": "खाट / चारपाई",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "खटोला",
        "roman": "khatola",
        "english": "small wooden cot / toddler bedstead",
        "hindi": "खटोला / छोटी चारपाई",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "गूंदड़ो",
        "roman": "goondado",
        "english": "thick recycled patchwork hill quilt for winter warmth",
        "hindi": "गुदड़ी / रजाई",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "तुषक",
        "roman": "tushak",
        "english": "soft quilted cotton floor mattress",
        "hindi": "तोशक / गद्दा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "कुचो",
        "roman": "kucho",
        "english": "hand-tied broom crafted from wild mountain babiyo grass",
        "hindi": "झाड़ू / बुहारी",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "ताला-कुंजी",
        "roman": "taala-kunji",
        "english": "heavy brass padlock and forged key",
        "hindi": "ताला और चाबी",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "डीवा",
        "roman": "deewa",
        "english": "terracotta or brass oil lamp with a twisted cotton wick",
        "hindi": "दीपक / दीया",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "धुंवारो",
        "roman": "dhumwaaro",
        "english": "ceiling smoke escape aperture in stone-slate roofed cottages",
        "hindi": "धुआंकश / धुआं निकलने का छिद्र",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "पठाल",
        "roman": "pathaal",
        "english": "hewn mountain slate slab used for cottage roofing and stone paving",
        "hindi": "पठाल (छत की स्लेट)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "दहली",
        "roman": "dahali",
        "english": "raised carved wooden door sill threshold",
        "hindi": "देहली / चौखट",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "गोठ",
        "roman": "goth",
        "english": "ground floor stable chamber keeping cattle warm beneath the residence",
        "hindi": "गोठ (मकान का भूतल / गौशाला)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "मांज",
        "roman": "maanj",
        "english": "upper living storey of traditional two-tier Kumaoni stone house",
        "hindi": "मांज (घर की ऊपरी आवासीय मंजिल)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "तिबारी",
        "roman": "tibaari",
        "english": "three-arched intricately wood-carved front balcony veranda",
        "hindi": "तिबारी (नक्काशीदार लकड़ी की बालकनी)",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "डाँड",
        "roman": "daand",
        "english": "sunny paved rooftop or front courtyard",
        "hindi": "छत / आंगन",
        "pos": "noun",
        "category": "household"
    },

    # ==================== 6. CHILDREN, MOVEMENTS, INFANCY, RITUALS & GAMES ====================
    {
        "kumaoni": "नान्तिन",
        "roman": "naantin",
        "english": "children / young kids / offspring",
        "hindi": "बच्चे / बालक",
        "pos": "noun",
        "category": "family"
    },
    {
        "kumaoni": "नानिन",
        "roman": "naanin",
        "english": "newborn tiny baby / infant",
        "hindi": "नन्हा शिशु / छोटा बच्चा",
        "pos": "noun",
        "category": "family"
    },
    {
        "kumaoni": "दूधपितो",
        "roman": "doodhpito",
        "english": "unweaned nursing suckling baby",
        "hindi": "दूधमुंहा बच्चा",
        "pos": "noun",
        "category": "family"
    },
    {
        "kumaoni": "नानबाबू",
        "roman": "naanbaabu",
        "english": "darling little boy (affectionate form of address)",
        "hindi": "छोटा बच्चा (प्यार से)",
        "pos": "noun",
        "category": "family"
    },
    {
        "kumaoni": "नानिबेटी",
        "roman": "naanibeti",
        "english": "darling little daughter / young girl",
        "hindi": "छोटी बिटिया",
        "pos": "noun",
        "category": "family"
    },
    {
        "kumaoni": "बौड़ा",
        "roman": "bouda",
        "english": "affectionate pet name for a mischievous darling baby boy",
        "hindi": "बौड़ा (प्यार से बालक को पुकारना)",
        "pos": "noun",
        "category": "family"
    },
    {
        "kumaoni": "बौड़ी",
        "roman": "boudi",
        "english": "affectionate pet name for a darling baby girl",
        "hindi": "बौड़ी (प्यार से बालिका को पुकारना)",
        "pos": "noun",
        "category": "family"
    },
    {
        "kumaoni": "दुलारो",
        "roman": "dulaaro",
        "english": "pampered deeply loved child",
        "hindi": "दुलारा / लाडला",
        "pos": "adjective",
        "category": "family"
    },
    {
        "kumaoni": "हियाक टुको",
        "roman": "hiyaak tuko",
        "english": "piece of my heart (tender hill idiom for one's child)",
        "hindi": "जिगर का टुकड़ा (संतान)",
        "pos": "noun",
        "category": "family"
    },
    {
        "kumaoni": "चुलबुलो",
        "roman": "chulbulo",
        "english": "playful lively bouncy child",
        "hindi": "चुलबुला / नटखट",
        "pos": "adjective",
        "category": "family"
    },
    {
        "kumaoni": "ढीठ",
        "roman": "dheeth",
        "english": "stubborn obstinate child",
        "hindi": "ढीठ / हठी",
        "pos": "adjective",
        "category": "family"
    },
    {
        "kumaoni": "गाथुली सरण",
        "roman": "gaathuli saran",
        "english": "infant crawling on belly, hands, and knees before walking",
        "hindi": "घिसट कर चलना / पेट के बल रेंगना",
        "pos": "verb",
        "category": "movement"
    },
    {
        "kumaoni": "घुटन हिटण",
        "roman": "ghutan hitan",
        "english": "toddler crawling on both knees",
        "hindi": "घुटनों के बल चलना",
        "pos": "verb",
        "category": "movement"
    },
    {
        "kumaoni": "लडबड हिटण",
        "roman": "ladbad hitan",
        "english": "taking unsteady clumsy first baby steps",
        "hindi": "लड़खड़ाते हुए चलना (बच्चे का)",
        "pos": "verb",
        "category": "movement"
    },
    {
        "kumaoni": "डगमग हिटण",
        "roman": "dagmag hitan",
        "english": "wobbling on two feet while learning to balance",
        "hindi": "डगमगाते कदम चलना",
        "pos": "verb",
        "category": "movement"
    },
    {
        "kumaoni": "ठुमक-ठुमक हिटण",
        "roman": "thumak-thumak hitan",
        "english": "walking with joyous rhythmic proud toddler stomps",
        "hindi": "ठुमक-ठुमक कर चलना",
        "pos": "verb",
        "category": "movement"
    },
    {
        "kumaoni": "तुत-तुत बोलण",
        "roman": "tut-tut bolan",
        "english": "infant babbling first broken words",
        "hindi": "तुतलाना / तुत-तुत बोलना",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "तोतलौण",
        "roman": "totlaun",
        "english": "speaking in sweet childish toddler lisp",
        "hindi": "तोतली बोली बोलना",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "च्याँखटण",
        "roman": "chyaankhtan",
        "english": "letting out a sudden shrill piercing infant wail",
        "hindi": "चीखना / रोना (शिशु का)",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "बिलखण",
        "roman": "bilakhan",
        "english": "sobbing uncontrollably with heaving chest when missing mother",
        "hindi": "बिलखना / फूट-फूट कर रोना",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "राँव-राँव करण",
        "roman": "raanw-raanw karan",
        "english": "whimpering fretfully to get maternal attention",
        "hindi": "मचलना / रिरियाना",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "कोल्यों बैठण",
        "roman": "kolyon baithan",
        "english": "sitting snuggled affectionately in mother's lap",
        "hindi": "गोद में बैठना",
        "pos": "verb",
        "category": "movement"
    },
    {
        "kumaoni": "काँखड़ी लैण",
        "roman": "kaankhadi lain",
        "english": "carrying a toddler seated astride on the hip",
        "hindi": "कांख में लेना (गोद में उठाना)",
        "pos": "verb",
        "category": "movement"
    },
    {
        "kumaoni": "पुठ्याव लैण",
        "roman": "puthyaav lain",
        "english": "carrying a child piggyback across the shoulders",
        "hindi": "पीठ पर लादना (कंधे पर बैठाना)",
        "pos": "verb",
        "category": "movement"
    },
    {
        "kumaoni": "अँगूठो चूसण",
        "roman": "angootho choosan",
        "english": "sucking thumb (baby habit)",
        "hindi": "अंगूठा चूसना",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "मुसकौण",
        "roman": "muskaun",
        "english": "innocent unconscious infant smiling during slumber",
        "hindi": "मुस्कुराना (शिशु का)",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "कुलकुलौण",
        "roman": "kulkulaun",
        "english": "bursting into ticklish toddler laughter",
        "hindi": "खिलखिलाना / गुदगुदी से हंसना",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "फुर्र उड़ण",
        "roman": "phurr udan",
        "english": "tossing toddler gently in air during play",
        "hindi": "हवा में उछालना (खेल में)",
        "pos": "verb",
        "category": "action"
    },
    {
        "kumaoni": "घूघूती बासुती",
        "roman": "ghughuti basuti",
        "english": "traditional rhythmic nursery lap-clapping rhyme for toddlers",
        "hindi": "घूघूती बासुती (पारंपरिक बालगीत)",
        "pos": "noun",
        "category": "folklore"
    },
    {
        "kumaoni": "निनूड़ी",
        "roman": "ninoori",
        "english": "tender Kumaoni cradle lullaby singing babies to sleep",
        "hindi": "लोरी / निन्दूड़ी",
        "pos": "noun",
        "category": "folklore"
    },
    {
        "kumaoni": "न्वाण",
        "roman": "nwaan",
        "english": "11th-day post-natal purificatory bath and infant naming samskara",
        "hindi": "न्वाण / नामकरण संस्कार",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "छठी",
        "roman": "chhatthi",
        "english": "6th night post-natal rite where Vidhaata goddess writes baby's destiny",
        "hindi": "छठी पूजा",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "पास्नी",
        "roman": "pasni",
        "english": "first solid grain tasting ceremony with sweet kheer at 6 months",
        "hindi": "अन्नप्राशन संस्कार / पास्नी",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "भात-ख्वाई",
        "roman": "bhaat-khwaai",
        "english": "ceremonial first feeding of rice to an infant",
        "hindi": "भात-ख्वाई (अन्नप्राशन)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "ज्यूँड़ कापण",
        "roman": "jyoonr kaapan",
        "english": "ceremonial tonsure / first shaving of child's birth hair at a holy temple",
        "hindi": "मुंडन संस्कार / चूड़ाकर्म",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "कान छेकण",
        "roman": "kaan chhekan",
        "english": "traditional earlobe piercing ceremony for infants",
        "hindi": "कर्णवेध संस्कार / कान छेदना",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "नजर उतारण",
        "roman": "najar utaaran",
        "english": "warding off evil eye from infants with hearth embers and mustard",
        "hindi": "नजर उतारना",
        "pos": "verb",
        "category": "culture"
    },
    {
        "kumaoni": "कालो टीको",
        "roman": "kaalo teeko",
        "english": "soot mark applied behind infant's ear to ward off malevolent eye",
        "hindi": "काला टीका",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "गण्डो",
        "roman": "gando",
        "english": "consecrated black protection thread knotted around infant's ankle or waist",
        "hindi": "गंडा / रक्षा सूत्र (काला धागा)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "बाघ-नख",
        "roman": "baagh-nakh",
        "english": "curved silver tiger-claw amulet worn by young boys for bravery and vitality",
        "hindi": "बाघ-नख (ताबीज)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "घुघुता",
        "roman": "ghughuta",
        "english": "fried sweet wheat dough braids worn as edible necklaces by kids on Ghughuti Tyar",
        "hindi": "घुघुता (उत्तरायणी का पकवान)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "कौवा त्यार",
        "roman": "kauva tyar",
        "english": "dawn crow festival on Makar Sankranti where kids summon crows with sweet necklaces",
        "hindi": "कौवा त्यार (काले कौवा पर्व)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "खिलोना",
        "roman": "khilauna",
        "english": "carved pine wood child's toy",
        "hindi": "खिलौना",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "भौंरो",
        "roman": "bhaunro",
        "english": "lathe-turned wooden spinning top whipped with string",
        "hindi": "लट्टू / भौंरा",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "गुल्ली-डण्डा",
        "roman": "gulli-danda",
        "english": "classic hill game played with tapered wooden peg and batting stick",
        "hindi": "गुल्ली-डंडा",
        "pos": "noun",
        "category": "folklore"
    },
    {
        "kumaoni": "गीटी",
        "roman": "geeti",
        "english": "traditional five-stone juggling dexterity game played by village girls",
        "hindi": "गीटे (पांच पत्थरों का खेल)",
        "pos": "noun",
        "category": "folklore"
    },
    {
        "kumaoni": "बाटी",
        "roman": "baati",
        "english": "glass marbles shot in ring games by boys",
        "hindi": "कंचे / बाटी",
        "pos": "noun",
        "category": "folklore"
    },
    {
        "kumaoni": "छुक-छिपाणी",
        "roman": "chhuk-chhipaani",
        "english": "village game of hide-and-seek among terraced walls and haystacks",
        "hindi": "आंख-मिचौनी / लुका-छिपी",
        "pos": "noun",
        "category": "folklore"
    },

    # ==================== 7. TREES, ETHNOBOTANY & EDIBLES ====================
    {
        "kumaoni": "उतीस",
        "roman": "utees",
        "english": "Himalayan Alder (Alnus nepalensis); crucial soil-nitrogen fixer and timber for watermills",
        "hindi": "उतीस (हिमालयी एल्डर वृक्ष)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "सेमल",
        "roman": "semal",
        "english": "Red Silk Cotton Tree (Bombax ceiba); fiery blossoms and soft cotton used for temple lamp wicks",
        "hindi": "सेमल",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "तूण",
        "roman": "toon",
        "english": "Himalayan Red Cedar (Toona ciliata); aromatic termite-resistant timber for temple doors",
        "hindi": "तून (लाल देवदार)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "रीठा",
        "roman": "reetha",
        "english": "Soapnut tree (Sapindus mukorossi); natural saponin berries used to wash temple brass idols and wool",
        "hindi": "रीठा",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "आँवला",
        "roman": "aanwla",
        "english": "Indian Gooseberry (Phyllanthus emblica); sacred tree worshipped on Amla Navami",
        "hindi": "आंवला",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "हरड़",
        "roman": "harad",
        "english": "Chebulic Myrobalan (Terminalia chebula); miraculous healing tree of Ayurvedic tradition",
        "hindi": "हरड़ / हरीतकी",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "बहेड़ा",
        "roman": "baheda",
        "english": "Belliric Myrobalan (Terminalia bellirica); sacred forest tree forming the Triphala triad",
        "hindi": "बहेड़ा",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "कपूर कचरी",
        "roman": "kapur kachari",
        "english": "Spiked Ginger Lily (Hedychium spicatum); fragrant hill root blended in hawan samagri and temple dhup",
        "hindi": "कपूर कचरी",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "थुनेर",
        "roman": "thuner",
        "english": "Himalayan Yew (Taxus wallichiana); sacred high-altitude conifer; bark brewed into tea",
        "hindi": "थुनेर (हिमालयी यव)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "बिथर",
        "roman": "bithar",
        "english": "Alpine Juniper (Juniperus indica); sacred purifying smudge incense burnt at high shrines",
        "hindi": "धूप / बिथर (जूनीपर)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "भांग",
        "roman": "bhaang",
        "english": "Wild Himalayan Hemp (Cannabis sativa); seeds roasted for iconic Bhaang Chutney; sacred to Shiva",
        "hindi": "भांग",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "भांगजीरा",
        "roman": "bhangjeera",
        "english": "Wild Perilla (Perilla frutescens); aromatic black seeds ground in mountain gravies and chutneys",
        "hindi": "भांगजीरा",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "सिसूण",
        "roman": "sisoon",
        "english": "Himalayan Stinging Nettle (Urtica dioica); tender shoots cooked into wholesome medicinal saag",
        "hindi": "बिच्छू घास / सिसूण / कंडाली",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "गेठी",
        "roman": "gethi",
        "english": "Air Potato (Dioscorea bulbifera); wild climbing yam bulb harvested in winter fasts",
        "hindi": "गेठी (हवाई रतालू)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "तरुड़",
        "roman": "tarur",
        "english": "Giant Mountain Forest Yam (Dioscorea alata); sacred root excavated for Makar Sankranti feast",
        "hindi": "तरुड़ (पहाड़ी रतालू)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "गड़ेरी",
        "roman": "gaderi",
        "english": "Colossal mountain taro tuber cooked with sour curd and jambu seasoning",
        "hindi": "गड़ेरी (बड़ा पहाड़ी अरबी कंद)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "पिनालू",
        "roman": "pinalu",
        "english": "Taro tuber / Arbi; staple mountain root vegetable",
        "hindi": "पिनालू / अरबी",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "लिंगुड़ा",
        "roman": "linguda",
        "english": "Wild Fiddlehead Fern (Diplazium esculentum); gathered along swift brooklets in spring",
        "hindi": "लिंगुड़ा (जंगली फर्न की सब्जी)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "माळू",
        "roman": "maalu",
        "english": "Camel's Foot Creeper (Bauhinia vahlii); gigantic leaves stitched into eco-friendly feast plates (pattal)",
        "hindi": "माळू (पत्तल बनाने वाली लता)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "गुच्छी",
        "roman": "guchhi",
        "english": "Himalayan Wild Morel Mushroom (Morchella esculenta); prized subterranean spring mushroom",
        "hindi": "गुच्छी (जंगली मशरूम)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "च्यूँ",
        "roman": "chyoon",
        "english": "Wild edible oak-forest mushroom gathered during monsoon rains",
        "hindi": "च्यूं (पहाड़ी खाद्य मशरूम)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "दाम",
        "roman": "daam",
        "english": "Wild Himalayan Pomegranate (Punica granatum); sun-dried into tangy anardana seasoning",
        "hindi": "दाड़िम / दारू (जंगली अनार)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "आड़ू",
        "roman": "aadu",
        "english": "Himalayan Peach (Prunus persica); staple summer stone-fruit of Ramgarh orchards",
        "hindi": "आड़ू",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "खुमानी",
        "roman": "khumaani",
        "english": "Himalayan Apricot (Prunus armeniaca); sweet wild stone fruit whose kernels yield oil",
        "hindi": "खुबानी",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "पुलम",
        "roman": "pulam",
        "english": "Mountain Plum (Prunus domestica); ruby-red orchard fruit",
        "hindi": "आलूबुखारा / प्लम",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "माल्टा",
        "roman": "maalta",
        "english": "Hill Blood Orange (Citrus sinensis); succulent winter citrus whipped with mustard and jaggery",
        "hindi": "माल्टा (पहाड़ी संतरा)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "रई",
        "roman": "rai",
        "english": "Pungent mountain mustard greens (Brassica juncea); staple winter leaf vegetable",
        "hindi": "राई / रयास (पहाड़ी सरसों का साग)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "कौणी",
        "roman": "kauni",
        "english": "Foxtail Millet (Setaria italica); ancient sacred fasting grain of hill ballads",
        "hindi": "कौणी (कंगनी कूटकी)",
        "pos": "noun",
        "category": "flora"
    },
    {
        "kumaoni": "चीना",
        "roman": "cheena",
        "english": "Proso Millet (Panicum miliaceum); fast-ripening mountain grain crop",
        "hindi": "चीना (चेना बाजरा)",
        "pos": "noun",
        "category": "flora"
    },

    # ==================== 8. TEMPLE & SACRED RITUAL OBJECTS ====================
    {
        "kumaoni": "दीवा",
        "roman": "deewa",
        "english": "sacred clay or brass oil lamp lit during dawn and dusk aarti",
        "hindi": "दीपक / दीया",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "बाती",
        "roman": "baati",
        "english": "hand-rolled pure cotton or crimson sacred thread wick soaked in ghee",
        "hindi": "बाती / रुई की बत्ती",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "धूपेली",
        "roman": "dhupeli",
        "english": "terracotta or bronze incense brazier holding oak embers and guggul",
        "hindi": "धूपेली / धूपपात्र",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "लोबान",
        "roman": "loban",
        "english": "sacred benzoin resin burnt over coals to banish spirits and purify sanctums",
        "hindi": "लोबान",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "गुग्गल",
        "roman": "guggal",
        "english": "sacred aromatic bdellium resin sprinkled into hawan fire",
        "hindi": "गुग्गल",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "कपूर",
        "roman": "kapoor",
        "english": "pure white camphor ignited during Maha Aarti leaving zero residue",
        "hindi": "कपूर",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "झाँझ",
        "roman": "jhaanjh",
        "english": "heavy circular brass clash-cymbals struck during temple aarti and kirtans",
        "hindi": "झांझ (बड़ी पीतल की झांझ)",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "झाँझर",
        "roman": "jhaanjhar",
        "english": "melodious bronze rim cymbal or ankle bell",
        "hindi": "झांझर",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "डमरू",
        "roman": "damru",
        "english": "sacred two-headed hour-glass rattle drum of Lord Shiva",
        "hindi": "डमरू",
        "pos": "noun",
        "category": "music"
    },
    {
        "kumaoni": "चिमटा",
        "roman": "chimta",
        "english": "heavy iron tongs wielded by Nath yogis at the eternal temple dhooni fire",
        "hindi": "चिमटा (साधुओं का वाद्य व उपकरण)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "कमण्डल",
        "roman": "kamandal",
        "english": "sacred water vessel of wandering ascetics carved from dried gourd or brass",
        "hindi": "कमंडल",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "खड़ाऊँ",
        "roman": "khadaun",
        "english": "elevated wooden sandals with toe-pegs worn by temple priests for ritual purity",
        "hindi": "खड़ाऊं (काष्ठ पादुका)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "कुशा का आसन",
        "roman": "kusha ka aasan",
        "english": "sacred handwoven mat of desmostachya grass required for Vedic hawan and japa",
        "hindi": "कुशा का आसन",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "पत्तल",
        "roman": "pattal",
        "english": "eco-friendly sacred banquet plate stitched from broad Malu or Sal leaves",
        "hindi": "पत्तल",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "दोना",
        "roman": "dona",
        "english": "green folded leaf cup for distributing panchamrit and prashad",
        "hindi": "दोना",
        "pos": "noun",
        "category": "household"
    },
    {
        "kumaoni": "मोरपंख झाड़",
        "roman": "morpankh jhaad",
        "english": "peacock-feather holy whisk used by temple priests to disperse negative energies",
        "hindi": "मोरपंख की झाड़",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "जंतर",
        "roman": "jantar",
        "english": "sacred silver or copper talisman capsule containing consecrated yantras",
        "hindi": "जंतर / रक्षा ताबीज",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "ताबीज",
        "roman": "taabeez",
        "english": "protective energized metal amulet worn around neck or arm",
        "hindi": "ताबीज",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "काली डोरी",
        "roman": "kaali dori",
        "english": "sanctified black cotton cord tied around children for protection against evil eye",
        "hindi": "काली डोरी (रक्षा सूत्र)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "सुहाग पिटारी",
        "roman": "suhaag pitaari",
        "english": "consecrated ringal wicker casket holding sindoor, pithyan, and kajal for Devi puja",
        "hindi": "सुहाग पिटारी",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "नथ",
        "roman": "nath",
        "english": "grand circular gold nose ring with rubies and pearls, sanctified at Devi shrines",
        "hindi": "नथ / नथुली (पारंपरिक कुमाऊँनी स्वर्णाभूषण)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "पौंची",
        "roman": "paunchi",
        "english": "gold bead bracelet strung on red velvet, blessed at matrimonial altars",
        "hindi": "पौंची (पारंपरिक कंगन)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "गुलूबंद",
        "roman": "guloband",
        "english": "traditional gold and velvet choker necklace blessed at marriage rituals",
        "hindi": "गुलूबंद (पारंपरिक कंठहार)",
        "pos": "noun",
        "category": "culture"
    },
    {
        "kumaoni": "धार",
        "roman": "dhaar",
        "english": "continuous unbroken libation stream of holy cow milk or water over Shivalinga",
        "hindi": "धार (शिवलिंग पर निरंतर जल या दुग्ध धारा)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "दुग्धाभिषेक",
        "roman": "dugdhaabhishek",
        "english": "sacred ceremonial milk bathing of temple deities",
        "hindi": "दुग्धाभिषेक",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "तर्पण पात्र",
        "roman": "tarpan paatra",
        "english": "flat copper dish used with kusha grass and sesame seeds to libate ancestors",
        "hindi": "तर्पण पात्र",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "पिण्ड",
        "roman": "pind",
        "english": "spherical barley and rice oblation cakes offered during ancestral Shraddha",
        "hindi": "पिंड (पितृ तर्पण का पिंड)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "भंडार",
        "roman": "bhandaar",
        "english": "consecrated temple storehouse preserving copper vessels and grains",
        "hindi": "मंदिर का भंडार (अन्न व पात्र भंडार)",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "भोग पात्र",
        "roman": "bhog paatra",
        "english": "sacred bell-metal bronze platter reserved strictly for deity food offerings",
        "hindi": "भोग पात्र",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "ध्वज",
        "roman": "dhwaj",
        "english": "triangular saffron or crimson deity flag fluttering from high temple spire",
        "hindi": "मंदिर का ध्वज",
        "pos": "noun",
        "category": "religion"
    },
    {
        "kumaoni": "नेजा",
        "roman": "neja",
        "english": "tall ceremonial deity banner carried during village pilgrimages and jaats",
        "hindi": "नेजा (देवता का झंडा)",
        "pos": "noun",
        "category": "religion"
    }
]


def enrich_words_json():
    print(f"Reading existing dictionary from {WORDS_JSON_PATH}...")
    with open(WORDS_JSON_PATH, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    existing_lemmas = set(w["kumaoni"].strip() for w in existing_data)
    initial_count = len(existing_data)
    added = 0

    for item in NEW_DICTIONARY_WORDS:
        lemma = item["kumaoni"].strip()
        if lemma not in existing_lemmas:
            existing_data.append(item)
            existing_lemmas.add(lemma)
            added += 1

    with open(WORDS_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"Added {added} new authenticated lemmas to words.json.")
    print(f"Total vocabulary expanded from {initial_count} to {len(existing_data)} lemmas.")
    return added, len(existing_data)


if __name__ == "__main__":
    enrich_words_json()
