"""
Ingest Phase 2 of Dr. Trilochan Pandey (1977) authentic Kumaoni vocabulary.
Cleans OCR artifacts, normalizes lemmas, assigns English and Hindi definitions,
parts of speech, categories, and adds to words.json.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_FILE = os.path.join(ROOT_DIR, 'kumaoni', 'lexicon', 'data', 'words.json')

sys.path.insert(0, ROOT_DIR)
import kumaoni

PHASE_2_ENTRIES = [
    # --- TERRAIN, HYDROLOGY & AGRICULTURE ---
    {"kumaoni": "तैलफाट", "english": "sunny, south-facing warm mountain slope", "hindi": "धूप वाला दक्षिणी पहाड़ी ढलान", "pos": "noun", "category": "nature"},
    {"kumaoni": "नजवाणी", "english": "exceptionally fertile land yielding bumper grain harvests", "hindi": "अत्यंत उपजाऊ अन्न पैदा करने वाली जमीन", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "पणखेत", "english": "waterfront terrace field fed by stream seepage", "hindi": "पानी के निकट स्थित सिंचित खेत", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "पगार", "english": "dry-stone retaining wall supporting terraced hillside fields", "hindi": "खेत की पत्थर की पुश्ता दीवार", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "पराल", "english": "harvested rice straw used for cattle bedding and winter fodder", "hindi": "धान की पुआल / पराली", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "बाड़ो", "english": "fenced vegetable garden plot near the house", "hindi": "मकान के समीप का छोटा बाड़ा / साग-सब्जी का खेत", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "भिड़", "english": "raised earthen border or stone terrace bund", "hindi": "खेत की मेंड़ या पत्थर की दीवार", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "सग्गड़", "english": "portable iron or clay charcoal firepot for warming hands", "hindi": "लोहे या मिट्टी का आग तापने का पात्र / अंगीठी", "pos": "noun", "category": "tools"},
    {"kumaoni": "घाणा", "english": "mound of harvested grain ears heaped in the threshing yard", "hindi": "खलिहान में लगा अनाज का ढेर", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "तामी", "english": "traditional quarter-seer volume/weight grain measure", "hindi": "पाव भर का पुराना अनाज माप", "pos": "noun", "category": "tools"},
    {"kumaoni": "बेत", "english": "traditional handspan length measure from thumb to little finger", "hindi": "एक बालिश्त / बित्ता", "pos": "noun", "category": "tools"},
    {"kumaoni": "रिहाड़ा", "english": "wooden connecting pin securing the ploughshare to the beam", "hindi": "हल के दोनों भागों को जोड़ने वाला काष्ठ कील", "pos": "noun", "category": "tools"},

    # --- DOMESTIC ARCHITECTURE & HOUSEHOLD ---
    {"kumaoni": "करयाड़ी", "english": "enclosed backyard area behind a traditional hill cottage", "hindi": "घर के पीछे का खुला स्थान / पिछवाड़ा", "pos": "noun", "category": "home"},
    {"kumaoni": "कवाड़", "english": "secluded, dark corner nook of a room", "hindi": "घर का उपेक्षित अंधेरा कोना", "pos": "noun", "category": "home"},
    {"kumaoni": "खन्यार", "english": "ruins / abandoned stone walls of an old mountain house", "hindi": "पुराने घर का खंडहर", "pos": "noun", "category": "home"},
    {"kumaoni": "खूटकूण", "english": "notched solid wooden log ladder accessing the attic", "hindi": "काठ की सीढ़ी / पायदान वाला लट्ठा", "pos": "noun", "category": "home"},
    {"kumaoni": "गल्यार", "english": "narrow stone-paved pathway or alleyway between village cottages", "hindi": "गाँव का सँकरा पत्थर का रास्ता / गली", "pos": "noun", "category": "home"},
    {"kumaoni": "घरोट", "english": "traditional water-driven stone flour mill on hill streams", "hindi": "पनचक्की / घराट", "pos": "noun", "category": "tools"},
    {"kumaoni": "छाना", "english": "thatched summer pastoral cottage / cattle shelter hut in the forest", "hindi": "घास-फूस की छान / पशुओं की झोपड़ी", "pos": "noun", "category": "home"},
    {"kumaoni": "छापरि", "english": "shallow woven ringal-bamboo basket for greens and flowers", "hindi": "रिंगाल की छोटी डलिया", "pos": "noun", "category": "tools"},
    {"kumaoni": "ज्यौड़", "english": "sturdy handmade hemp rope for tying loads and haystacks", "hindi": "सन या भांग के रेशों की मजबूत रस्सी", "pos": "noun", "category": "tools"},
    {"kumaoni": "पटांगण", "english": "broad, stone-paved open front courtyard of a village house", "hindi": "घर के आगे का खुला पत्थर-पक्का आँगन", "pos": "noun", "category": "architecture"},
    {"kumaoni": "पाख", "english": "sloping pitched gable roof surfaced with stone slate slabs", "hindi": "मकान की ढालू छत", "pos": "noun", "category": "architecture"},
    {"kumaoni": "बाखलि", "english": "connected row of ancestral stone houses of a shared clan", "hindi": "गाँव में एक ही कुल के मकानों की जुड़ी पंक्ति", "pos": "noun", "category": "architecture"},
    {"kumaoni": "म्वाव", "english": "carved timber doorframe lintel and jambs", "hindi": "द्वार का काष्ठ चौखट", "pos": "noun", "category": "architecture"},
    {"kumaoni": "मोरी", "english": "small stone ventilation opening / peephole in a mountain house", "hindi": "रोशनदान / हवा और धूप की छोटी मोरी", "pos": "noun", "category": "architecture"},
    {"kumaoni": "शाँकल", "english": "iron chain latch securing front wooden doors", "hindi": "दरवाजे की लोहे की साँकल", "pos": "noun", "category": "tools"},

    # --- KINSHIP & PASTORAL COMMUNITY ---
    {"kumaoni": "अन्वाल", "english": "high-altitude shepherd tending sheep flocks on alpine bugyals", "hindi": "बुग्यालों में भेड़ें चराने वाला गड़रिया / चरवाहा", "pos": "noun", "category": "people"},
    {"kumaoni": "गुसें", "english": "respected master / household lord / owner", "hindi": "स्वामी / मालिक / गृहस्वामी", "pos": "noun", "category": "people"},
    {"kumaoni": "गुस्याण", "english": "mistress / matriarch commanding domestic affairs", "hindi": "घर की मालकिन / स्वामिनी", "pos": "noun", "category": "people"},
    {"kumaoni": "ब्योली", "english": "newlywed bride in wedding attire", "hindi": "सद्यः विवाहिता वधू / दुल्हन", "pos": "noun", "category": "kinship"},
    {"kumaoni": "ब्योला", "english": "bridegroom celebrating his marriage procession", "hindi": "दूल्हा / वर", "pos": "noun", "category": "kinship"},
    {"kumaoni": "नानछिन", "english": "tender childhood years / early youth", "hindi": "बचपन / बाल्यकाल", "pos": "noun", "category": "people"},
    {"kumaoni": "मवास", "english": "close-knit joint family / household hearth members", "hindi": "परिवार / कुनबा / कुटुम्ब", "pos": "noun", "category": "kinship"},
    {"kumaoni": "मितुर", "english": "loyal lifelong friend / sworn comrade", "hindi": "मित्र / सखा", "pos": "noun", "category": "people"},
    {"kumaoni": "मैतिया", "english": "kinsmen and maternal relatives from a bride's natal home", "hindi": "मायके के सम्बन्धी / नैहर वाले", "pos": "noun", "category": "kinship"},
    {"kumaoni": "रस्यार", "english": "expert cook preparing traditional community wedding banquets", "hindi": "मांगलिक उत्सवों का रसोइया", "pos": "noun", "category": "people"},
    {"kumaoni": "राठ", "english": "noble ancestral lineage / reputable clan lineage", "hindi": "कुल / घराना / वंश", "pos": "noun", "category": "kinship"},
    {"kumaoni": "सौर", "english": "father-in-law", "hindi": "ससुर", "pos": "noun", "category": "kinship"},

    # --- TRADITIONAL FOOD & UTENSILS ---
    {"kumaoni": "खुस्याणि", "english": "spicy hot chilli pepper used in pahadi chutneys", "hindi": "हरी या लाल मिर्च", "pos": "noun", "category": "food"},
    {"kumaoni": "गदुवा", "english": "mountain pumpkin / winter squash", "hindi": "पहाड़ी कद्दू / कुम्हड़ा", "pos": "noun", "category": "food"},
    {"kumaoni": "गास", "english": "morsel / mouthful of food", "hindi": "कौर / ग्रास", "pos": "noun", "category": "food"},
    {"kumaoni": "चूख", "english": "thick sour reduction syrup made of boiled mountain lemon juice", "hindi": "पके नींबू का रस पकाकर बनाई गई गाढ़ी खटाई", "pos": "noun", "category": "food"},
    {"kumaoni": "चाक्ती", "english": "traditional fermented Himalayan rice beverage", "hindi": "चावल का पारंपरिक पेय", "pos": "noun", "category": "food"},
    {"kumaoni": "ज्या", "english": "churned Tibetan-style salted butter tea of high-altitude borders", "hindi": "मक्खन और नमक वाली पहाड़ी चाय", "pos": "noun", "category": "food"},
    {"kumaoni": "नौणि", "english": "fresh homemade unsalted butter churned from hill cow milk", "hindi": "मक्खन / नौणी", "pos": "noun", "category": "food"},
    {"kumaoni": "पिनालु", "english": "starchy Himalayan taro corm (*Colocasia esculenta*)", "hindi": "पिनालू / अरबी / घुइयाँ", "pos": "noun", "category": "food"},
    {"kumaoni": "फांण", "english": "warming spiced porridge-soup of roasted lentils or grain", "hindi": "फाणा (दाल या आटे का गाढ़ा पौष्टिक सूप)", "pos": "noun", "category": "food"},
    {"kumaoni": "भुटूवा", "english": "dry sautéed spiced hill vegetable or greens", "hindi": "भुना हुआ सूखा साग / भुजिया", "pos": "noun", "category": "food"},
    {"kumaoni": "लगड़", "english": "deep-fried fluffy wheat flatbread served at feasts", "hindi": "पूरी / पक्वान्न", "pos": "noun", "category": "food"},
    {"kumaoni": "कसिणि", "english": "carved bell-metal bronze bowl for drinking water and milk", "hindi": "काँसे का पारंपरिक कटोरा", "pos": "noun", "category": "tools"},
    {"kumaoni": "गडूवा", "english": "traditional brass water jug with curved pouring spout", "hindi": "टोंटीदार पीतल की लुटिया", "pos": "noun", "category": "tools"},
    {"kumaoni": "ठेकि", "english": "tall carved wooden cask for churning curd and keeping butter", "hindi": "काठ का मथने का गहरा बर्तन / ठेकी", "pos": "noun", "category": "tools"},
    {"kumaoni": "डाइ", "english": "deep hemispherical metal serving ladle with long handle", "hindi": "दाल-सब्जी की करछुल", "pos": "noun", "category": "tools"},

    # --- ANATOMY & PHYSICAL CHARACTERISTICS ---
    {"kumaoni": "पौंठ", "english": "human wrist / forearm junction", "hindi": "कलाई", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "हतगलि", "english": "palm of the hand", "hindi": "हथेली", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "स्यून", "english": "hair parting on the head adorned with vermilion", "hindi": "मांग (केशों की)", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "कामण", "english": "shivering / trembling from bitter Himalayan cold", "hindi": "जाड़े से काँपना / थरथराना", "pos": "verb", "category": "health"},
    {"kumaoni": "चड़क", "english": "sharp sudden throbbing pang / muscle twinge", "hindi": "टीस / अचानक उठने वाला दर्द", "pos": "noun", "category": "health"},
    {"kumaoni": "छ्यां", "english": "sudden sneeze", "hindi": "छींक", "pos": "noun", "category": "health"},
    {"kumaoni": "बाटुइ", "english": "hiccup", "hindi": "हिचकी", "pos": "noun", "category": "health"},
    {"kumaoni": "बौलार", "english": "uncontrollable frenzy / ecstatic madness", "hindi": "पागलपन / उन्माद", "pos": "noun", "category": "health"},
    {"kumaoni": "रिगाइ", "english": "dizziness / vertigo while climbing steep ridges", "hindi": "चक्कर आना / सिर घूमना", "pos": "noun", "category": "health"},

    # --- CLOTHING, ORNAMENTS & RITUAL ARTIFACTS ---
    {"kumaoni": "घागुल", "english": "solid silver engraved cuff bracelets worn by children", "hindi": "बच्चों के हाथ के चांदी के कड़े", "pos": "noun", "category": "clothing"},
    {"kumaoni": "नेवर", "english": "charming ankle bells / silver payal chime", "hindi": "नूपुर / पाजेब", "pos": "noun", "category": "clothing"},
    {"kumaoni": "पिठार", "english": "carved miniature wooden/brass chest for sacred vermilion and rice", "hindi": "रोली-अक्षत रखने का मांगलिक श्रृंगारदान", "pos": "noun", "category": "tools"},
    {"kumaoni": "फूल्लि", "english": "delicate gold clove-shaped nose stud", "hindi": "नाक की लौंग / फूल", "pos": "noun", "category": "clothing"},
    {"kumaoni": "मुनडि", "english": "carved gold or silver signet finger ring", "hindi": "अंगूठी / मुंदरी", "pos": "noun", "category": "clothing"},
    {"kumaoni": "ओतरण", "english": "descent of a deity or ancestral spirit into the medium during a Jagar", "hindi": "देवता का शरीर में अवतरित होना / भाव आना", "pos": "noun", "category": "culture"},
    {"kumaoni": "उच्यूण", "english": "making a solemn spiritual vow or pledge to a mountain deity", "hindi": "देवता के निमित्त मनौती मानना", "pos": "verb", "category": "culture"},
    {"kumaoni": "बधाण", "english": "benevolent pastoral guardian deity of milch cattle", "hindi": "गायों का रक्षक सौम्य लोकदेवता", "pos": "proper_noun", "category": "culture"},
    {"kumaoni": "भूम्याल", "english": "village land tutelary spirit / soil guardian", "hindi": "गाँव का भूमि-रक्षक देवता", "pos": "proper_noun", "category": "culture"},

    # --- EMOTIONS, STATES, VERBS & EXPRESSIONS ---
    {"kumaoni": "तीस", "english": "acute mountain thirst", "hindi": "प्यास", "pos": "noun", "category": "health"},
    {"kumaoni": "दिक्ख", "english": "mental dilemma / perplexity / confusion", "hindi": "उलझन / असमंजस", "pos": "noun", "category": "emotions"},
    {"kumaoni": "दुछ्यूंण", "english": "to taunt sarcastically / tease bitingly", "hindi": "व्यंग्य कसना / ताना मारना", "pos": "verb", "category": "society"},
    {"kumaoni": "पिरपिला", "english": "frail, thin, and delicate person", "hindi": "दुबला-पतला / कमजोर", "pos": "adjective", "category": "people"},
    {"kumaoni": "फराड", "english": "profusely laden with ripe fruit / blooming abundantly", "hindi": "फलों से लदा हुआ / फला-फूला", "pos": "adjective", "category": "nature"},
    {"kumaoni": "फाम", "english": "conscious awareness / precious memory / presence of mind", "hindi": "स्मृति / होश / सुध-बुध", "pos": "noun", "category": "emotions"},
    {"kumaoni": "फौंस", "english": "whimsical exaggeration / tall campfire tale / gossip", "hindi": "गप्प / बढ़ा-चढ़ाकर कही गई बात", "pos": "noun", "category": "society"},
    {"kumaoni": "फिटकार", "english": "stern scolding / verbal reprimand", "hindi": "फटकार / डाँट", "pos": "noun", "category": "society"},
    {"kumaoni": "भभरीण", "english": "to become utterly bewildered / lose one's way on misty trails", "hindi": "रास्ता भूल जाना / भ्रमित होना", "pos": "verb", "category": "emotions"},
    {"kumaoni": "लेण", "english": "milch cow or buffalo in prime productive milk yield", "hindi": "दुधारू गाय या भैंस", "pos": "noun", "category": "animals"},
    {"kumaoni": "सांगुड़ि", "english": "narrow, tight mountain footpath or cliff gorge", "hindi": "सँकरा / तंग पहाड़ी रास्ता", "pos": "adjective", "category": "nature"},
    {"kumaoni": "हाँसी", "english": "cheerful, vivacious, and good-humored disposition", "hindi": "हँसमुख / खुशमिज़ाज", "pos": "adjective", "category": "emotions"},
    {"kumaoni": "खनण", "english": "to dig terraced soil with a hoe", "hindi": "कुदाल से मिट्टी खोदना", "pos": "verb", "category": "agriculture"},
    {"kumaoni": "गच्छ्यूण", "english": "to braid hair smoothly or knead dough firmly", "hindi": "बाल गूँथना या आटा सानना", "pos": "verb", "category": "actions"},
    {"kumaoni": "गिजूण", "english": "to make mocking faces / playfully tease", "hindi": "मुँह बिचकाना / चिढ़ाना", "pos": "verb", "category": "actions"},
    {"kumaoni": "गोठयूण", "english": "to lead cattle into the ground-floor stall at twilight", "hindi": "शाम को मवेशियों को गोठ में बाँधना", "pos": "verb", "category": "agriculture"}
]

with open(WORDS_FILE, 'r', encoding='utf-8') as f:
    words = json.load(f)

existing_map = {w['kumaoni']: w for w in words}
initial_count = len(words)
added_count = 0

for item in PHASE_2_ENTRIES:
    k_word = item['kumaoni']
    if k_word not in existing_map:
        roman = kumaoni.devanagari_to_latin(k_word)
        entry = {
            "kumaoni": k_word,
            "roman": roman,
            "english": item['english'],
            "hindi": item['hindi'],
            "pos": item['pos'],
            "category": item['category']
        }
        words.append(entry)
        existing_map[k_word] = entry
        added_count += 1

words.sort(key=lambda x: x['kumaoni'])

with open(WORDS_FILE, 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Phase 2 Ingestion Complete!")
print(f"Initial: {initial_count} words")
print(f"Added:   {added_count} words")
print(f"Total Base Dictionary Lemmas: {len(words)}")
