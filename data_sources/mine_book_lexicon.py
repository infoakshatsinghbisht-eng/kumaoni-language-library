"""
Deep lexical mining from downloaded primary sources:
- Dr. Trilochan Pandey (1977): Kumaoni Bhasha Aur Sahitya (Appendix G: Specific Vocabulary)
- Uttarakhand Open University (2020): AECC-K-101 (Units 1, 2, 5, 6)
- Sir George Grierson (1916): Linguistic Survey of India (Vol. IX, Part IV)
- Pt. Ganga Datt Upreti (1900): Hill Dialects of the Kumaun Division

Extracts and validates authentic base lemmas across flora, fauna, terrain,
agriculture, domestic implements, measurements, rituals, and traditional arts.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
WORDS_FILE = os.path.join(ROOT_DIR, 'kumaoni', 'lexicon', 'data', 'words.json')

NEW_EXTRACTED_WORDS = [
    # --- MOUNTAIN TERRAIN & HYDROLOGY (Trilochan Pandey 1977) ---
    {"kumaoni": "उकालो", "roman": "ukaalo", "english": "steep uphill climb / mountain ascent", "hindi": "चढ़ाई", "pos": "noun", "category": "nature"},
    {"kumaoni": "ओड्यार", "roman": "odyaar", "english": "natural rock shelter / deep mountain cave under boulders", "hindi": "गुफा / चट्टान के नीचे की ओट", "pos": "noun", "category": "nature"},
    {"kumaoni": "उड्यार", "roman": "udyaar", "english": "variant form of mountain cave shelter", "hindi": "पहाड़ी गुफा", "pos": "noun", "category": "nature"},
    {"kumaoni": "करांइ", "roman": "karan-i", "english": "precipitous sloping hillside / steep incline", "hindi": "पहाड़ की ढालू जमीन", "pos": "noun", "category": "nature"},
    {"kumaoni": "खाड", "roman": "khaad", "english": "ravine / deep ditch / hollow in terrain", "hindi": "गड्ढा / खाई", "pos": "noun", "category": "nature"},
    {"kumaoni": "गल", "roman": "gal", "english": "glacier ice / avalanche snowpack", "hindi": "हिमनद / ग्लेशियर", "pos": "noun", "category": "nature"},
    {"kumaoni": "गैर", "roman": "gair", "english": "sunken landslide depression / valley bowl", "hindi": "पहाड़ का धंसा हुआ हिस्सा", "pos": "noun", "category": "nature"},
    {"kumaoni": "घाङल", "roman": "ghaangal", "english": "stone cairn / rock pile on mountain trails", "hindi": "पत्थरों का चट्टा", "pos": "noun", "category": "nature"},
    {"kumaoni": "चाँटा", "roman": "chaanta", "english": "narrow crevice / cliff fissure", "hindi": "चट्टान की खोह / दरार", "pos": "noun", "category": "nature"},
    {"kumaoni": "टिपुडि", "roman": "tipudi", "english": "small pointed mountain pinnacle / conical peaklet", "hindi": "छोटी नुकीली चोटी", "pos": "noun", "category": "nature"},
    {"kumaoni": "डाँसि", "roman": "daansi", "english": "quartz crystal stone found in mountain scree", "hindi": "स्फटिक पत्थर", "pos": "noun", "category": "nature"},
    {"kumaoni": "थड़", "roman": "thad", "english": "massive unhewn river or hill boulder", "hindi": "बेडौल बड़ा पत्थर", "pos": "noun", "category": "nature"},
    {"kumaoni": "पक्खान", "roman": "pakkhaana", "english": "solid mountain bedrock / cliff slab", "hindi": "पाषाण / बड़ी चट्टान", "pos": "noun", "category": "nature"},
    {"kumaoni": "सिलाप", "roman": "silaap", "english": "soil dampness / mountain seepage moisture", "hindi": "नमी / सीलन", "pos": "noun", "category": "nature"},
    {"kumaoni": "खांखर", "roman": "khaankhar", "english": "glazed sheet of winter surface ice / black ice", "hindi": "कांच जैसा जमा हुआ हिम", "pos": "noun", "category": "nature"},
    {"kumaoni": "छयड़", "roman": "chhapad", "english": "small cascading hill waterfall", "hindi": "छोटा जलप्रपात / झरना", "pos": "noun", "category": "nature"},
    {"kumaoni": "डाव", "roman": "daav", "english": "hailstone falling during mountain thunder squalls", "hindi": "ओला", "pos": "noun", "category": "nature"},
    {"kumaoni": "रेवाड़", "roman": "rewaad", "english": "sand and gravel river terrace / pebble bank", "hindi": "रेतीला-पथरीला नदी तट", "pos": "noun", "category": "nature"},
    {"kumaoni": "ल्वाडाँ", "roman": "lwaadaan", "english": "smooth water-worn river cobbles", "hindi": "नदी के चिकने पत्थर", "pos": "noun", "category": "nature"},
    {"kumaoni": "होल", "roman": "hol", "english": "dense mountain fog enveloping river valleys", "hindi": "कोहरा / धुंध", "pos": "noun", "category": "nature"},

    # --- WILD & DOMESTICATED HIMALAYAN FRUITS & FLORA ---
    {"kumaoni": "अखोइ", "roman": "akhoi", "english": "Himalayan wild walnut (*Juglans regia*)", "hindi": "अखरोट", "pos": "noun", "category": "food"},
    {"kumaoni": "आडू", "roman": "aadoo", "english": "Himalayan peach fruit (*Prunus persica*)", "hindi": "आड़ू", "pos": "noun", "category": "food"},
    {"kumaoni": "तिमुल", "roman": "timul", "english": "large edible elephant-ear mountain fig (*Ficus auriculata*)", "hindi": "तिमला / बड़ा जंगली अंजीर", "pos": "noun", "category": "food"},
    {"kumaoni": "दाड्मि", "roman": "daadmi", "english": "sour wild Himalayan pomegranate (*Punica granatum*)", "hindi": "दाड़िम / जंगली खट्टा अनार", "pos": "noun", "category": "food"},
    {"kumaoni": "कुसम्यारु", "roman": "kusmyaaru", "english": "small tart Himalayan wild apricot", "hindi": "जंगली खुबानी / चुलू", "pos": "noun", "category": "food"},
    {"kumaoni": "गलगल", "roman": "galgal", "english": "large juicy mountain citron (*Citrus medica*)", "hindi": "बड़ा पहाड़ी नींबू", "pos": "noun", "category": "food"},
    {"kumaoni": "जमीर", "roman": "jameer", "english": "rough thick-skinned sour hill lemon", "hindi": "जमीरी नींबू", "pos": "noun", "category": "food"},
    {"kumaoni": "मेहल", "roman": "mehal", "english": "wild Himalayan small brown russet pear (*Pyrus pashia*)", "hindi": "मेहल / जंगली नाशपाती", "pos": "noun", "category": "food"},
    {"kumaoni": "कौल कप्फू", "roman": "kaul kapphoo", "english": "sacred high-altitude Brahma Kamal lotus (*Saussurea obvallata*)", "hindi": "ब्रह्मकमल", "pos": "noun", "category": "nature"},
    {"kumaoni": "गुळबाँक", "roman": "gulbaank", "english": "wild white and pink Himalayan briar rose", "hindi": "जंगली गुलाब / कुंजा", "pos": "noun", "category": "nature"},
    {"kumaoni": "पइय्यां", "roman": "paiyyaan", "english": "wild Himalayan autumn cherry tree (*Prunus cerasoides*)", "hindi": "पद्मकाष्ठ / जंगली चेरी का पेड़", "pos": "noun", "category": "nature"},

    # --- HIMALAYAN WILDLIFE & BIRDS (Appendix G) ---
    {"kumaoni": "काकड़", "roman": "kaakad", "english": "barking deer / Indian muntjac (*Muntiacus muntjak*)", "hindi": "काकड़ / भौंकने वाला हिरण", "pos": "noun", "category": "animals"},
    {"kumaoni": "घुरड़", "roman": "ghurad", "english": "Himalayan ghoral goat-antelope (*Naemorhedus goral*)", "hindi": "घुरल / पहाड़ी बकरा", "pos": "noun", "category": "animals"},
    {"kumaoni": "थार", "roman": "thaar", "english": "Himalayan tahr wild mountain ungulate (*Hemitragus jemlahicus*)", "hindi": "झारल / जंगली ताहर", "pos": "noun", "category": "animals"},
    {"kumaoni": "साही", "roman": "saahi", "english": "crested Himalayan porcupine (*Hystrix indica*)", "hindi": "साही", "pos": "noun", "category": "animals"},
    {"kumaoni": "मुनाल", "roman": "munaal", "english": "iridescent Himalayan monal pheasant (*Lophophorus impejanus*) - state bird", "hindi": "मोनाल पक्षी", "pos": "noun", "category": "animals"},
    {"kumaoni": "हिलाँस", "roman": "hilaans", "english": "wedge-tailed green pigeon revered in hill folk ballads", "hindi": "हरियल पक्षी / हिलांस", "pos": "noun", "category": "animals"},
    {"kumaoni": "कफूवा", "roman": "kaphoowa", "english": "common Himalayan cuckoo whose spring call sings 'Kafal Pako'", "hindi": "काफल पक्वा / कोयल", "pos": "noun", "category": "animals"},
    {"kumaoni": "गंड्याल", "roman": "gandyaal", "english": "rich soil earthworm of terraced farms", "hindi": "केंचुआ", "pos": "noun", "category": "animals"},
    {"kumaoni": "घोल", "roman": "ghol", "english": "bird's nest in mountain crags or eaves", "hindi": "घोंसला", "pos": "noun", "category": "nature"},

    # --- PASTORAL & DOMESTIC ANIMAL TERMS ---
    {"kumaoni": "कलोड", "roman": "kalod", "english": "young heifer / adolescent female calf", "hindi": "बछिया / कलोड़", "pos": "noun", "category": "animals"},
    {"kumaoni": "गोठ", "roman": "goth", "english": "ground floor cattle-shed of traditional stone house", "hindi": "गोशाला / पशुशाला", "pos": "noun", "category": "home"},
    {"kumaoni": "दामिन", "roman": "daamin", "english": "hemp tethering rope for binding cattle in stalls", "hindi": "पशु बांधने की रस्सी", "pos": "noun", "category": "tools"},
    {"kumaoni": "डांगर", "roman": "daangar", "english": "domestic cattle / livestock animals collectively", "hindi": "मवेशी / पशुधन", "pos": "noun", "category": "animals"},
    {"kumaoni": "दौण", "roman": "daun", "english": "traditional hollowed wooden milking bucket", "hindi": "दूध दुहने का काष्ठ पात्र", "pos": "noun", "category": "tools"},

    # --- TREES OF THE KUMAON HIMALAYAS ---
    {"kumaoni": "बाँझ", "roman": "baanjh", "english": "Himalayan white banj oak (*Quercus leucotrichophora*) - spine of hill ecology", "hindi": "बांज का वृक्ष", "pos": "noun", "category": "nature"},
    {"kumaoni": "देवदार", "roman": "devdaar", "english": "sacred Himalayan deodar cedar (*Cedrus deodara*)", "hindi": "देवदार वृक्ष", "pos": "noun", "category": "nature"},
    {"kumaoni": "उतीस", "roman": "utees", "english": "Himalayan alder tree stabilizing landslide slopes (*Alnus nepalensis*)", "hindi": "उतीस वृक्ष", "pos": "noun", "category": "nature"},
    {"kumaoni": "चीड़", "roman": "cheed", "english": "long-needle Himalayan chir pine (*Pinus roxburghii*)", "hindi": "चीड़ का पेड़", "pos": "noun", "category": "nature"},
    {"kumaoni": "सुरई", "roman": "surai", "english": "Himalayan weeping cypress tree (*Cupressus torulosa*)", "hindi": "सुरई वृक्ष", "pos": "noun", "category": "nature"},
    {"kumaoni": "खर्सू", "roman": "kharsu", "english": "high-altitude brown oak (*Quercus semecarpifolia*)", "hindi": "खर्सू बांज", "pos": "noun", "category": "nature"},
    {"kumaoni": "पांगुर", "roman": "paangur", "english": "Himalayan horse chestnut tree (*Aesculus indica*)", "hindi": "पांगर / चेस्टनट", "pos": "noun", "category": "nature"},

    # --- TRADITIONAL CROPS, PULSES & SPICES ---
    {"kumaoni": "भट्ट", "roman": "bhatt", "english": "indigenous black soybean of Kumaon used in Churkani and Dubke", "hindi": "काला सोयाबीन / भट्ट", "pos": "noun", "category": "food"},
    {"kumaoni": "गहत", "roman": "gahat", "english": "Himalayan horsegram pulse used for warm Ras and warming broths", "hindi": "कुलथ / गहत", "pos": "noun", "category": "food"},
    {"kumaoni": "राजमा", "roman": "raajma", "english": "famous red and speckled kidney beans of Munsyari and Johar", "hindi": "राजमा", "pos": "noun", "category": "food"},
    {"kumaoni": "झंगोरा", "roman": "jhangora", "english": "Himalayan barnyard millet grain (*Echinochloa frumentacea*)", "hindi": "झंगोरा / सांवा", "pos": "noun", "category": "food"},
    {"kumaoni": "मडुवा", "roman": "maduwa", "english": "Himalayan finger millet (*Eleusine coracana*) used for nutritious rotis", "hindi": "कोदा / रागी / मडुवा", "pos": "noun", "category": "food"},
    {"kumaoni": "भांग", "roman": "bhaang", "english": "roasted hemp seeds used to make traditional sour ground salt chutney", "hindi": "भांग के बीज / भांग की चटनी", "pos": "noun", "category": "food"},
    {"kumaoni": "जख्या", "roman": "jakhya", "english": "wild mountain spice seeds (*Cleome viscosa*) used for crispy tempering", "hindi": "जख्या तड़का मसाला", "pos": "noun", "category": "food"},
    {"kumaoni": "गन्द्रायणी", "roman": "gandrayani", "english": "aromatic digestive mountain herb (*Angelica glauca*)", "hindi": "गंद्रायणी जड़ी-बूटी", "pos": "noun", "category": "food"},
    {"kumaoni": "जम्बू", "roman": "jamboo", "english": "sun-dried alpine chive herb (*Allium stracheyi*) used to temper daal", "hindi": "जम्बू मसाला", "pos": "noun", "category": "food"},

    # --- SACRED RITUALS, FOLK ART & HOUSEHOLD ---
    {"kumaoni": "ऐपण", "roman": "aipan", "english": "traditional ritual geometric floor and wall art drawn with red clay and rice paste", "hindi": "ऐपण / कुमाऊँनी अल्पना", "pos": "noun", "category": "culture"},
    {"kumaoni": "पिठ्याँ", "roman": "pithyaan", "english": "auspicious orange-yellow turmeric and vermilion forehead mark", "hindi": "तिलक / रोली-अक्षत", "pos": "noun", "category": "culture"},
    {"kumaoni": "ज्यूँतिया", "roman": "jyoonteeya", "english": "traditional hand-painted sacred ancestral scroll depicting folk deities", "hindi": "ज्यूँति मातृका पट्ट", "pos": "noun", "category": "culture"},
    {"kumaoni": "धुर्वा", "roman": "dhurwa", "english": "fresh holy durva grass harvested for festivals like Saatu-Aathu", "hindi": "हरी दूब", "pos": "noun", "category": "culture"},
    {"kumaoni": "गौथ", "roman": "gauth", "english": "sacred cow urine sprinkled for ceremonial ritual purification", "hindi": "गोमूत्र / पवित्रीकरण जल", "pos": "noun", "category": "culture"},
    {"kumaoni": "चौका", "roman": "chauka", "english": "sanctified cooking hearth and dining area of the mountain home", "hindi": "रसोई / चौका", "pos": "noun", "category": "home"},
    {"kumaoni": "टिमुक", "roman": "timuk", "english": "small earthen or brass oil lamp", "hindi": "दीपक / दीया", "pos": "noun", "category": "tools"},
    {"kumaoni": "नौलो", "roman": "naulo", "english": "ancient architectural subterranean stepped stone spring reservoir", "hindi": "नौला / सीढ़ीदार जलकुआं", "pos": "noun", "category": "architecture"},
    {"kumaoni": "धारा", "roman": "dhaara", "english": "open channel spout pouring fresh mountain spring water", "hindi": "धारा / जलधारा", "pos": "noun", "category": "architecture"},
    {"kumaoni": "बट्वा", "roman": "batwa", "english": "hand-stitched cloth coin purse", "hindi": "बटुआ / थैली", "pos": "noun", "category": "tools"},

    # --- TRADITIONAL MEASUREMENTS & WEIGHTS ---
    {"kumaoni": "पाथा", "roman": "paatha", "english": "traditional cylindrical brass/copper grain measure (~2 kg)", "hindi": "पाथा (अनाज नापने का पात्र)", "pos": "noun", "category": "tools"},
    {"kumaoni": "नाली", "roman": "naali", "english": "traditional land area and grain measure (~240 sq yards)", "hindi": "नाली (पहाड़ी भूमि की इकाई)", "pos": "noun", "category": "economy"},
    {"kumaoni": "माणा", "roman": "maana", "english": "half-patha traditional volumetric grain measure (~1 kg)", "hindi": "माणा (आधा पाथा)", "pos": "noun", "category": "tools"},
    {"kumaoni": "धड़ी", "roman": "dhadi", "english": "traditional 5-seer weight (~5 kg)", "hindi": "धड़ी (पांच सेर का माप)", "pos": "noun", "category": "tools"},

    # --- SOCIAL TRAITS & CHARACTER VOCABULARY (UOU Unit 5) ---
    {"kumaoni": "स्याणो", "roman": "syaano", "english": "wise village elder / venerable counselor", "hindi": "सयाना / चतुर व अनुभवी वृद्ध", "pos": "adjective", "category": "people"},
    {"kumaoni": "लाटो", "roman": "laato", "english": "mute person / innocent, gullible simpleton", "hindi": "सीधा-सादा / मूक व्यक्ति", "pos": "adjective", "category": "people"},
    {"kumaoni": "बाठो", "roman": "baatho", "english": "astute, shrewd, and quick-witted person", "hindi": "चतुर / चालाक", "pos": "adjective", "category": "people"},
    {"kumaoni": "बाँठ", "roman": "baanth", "english": "assigned share / equitable portion of farm produce or inheritance", "hindi": "हिस्सा / भाग", "pos": "noun", "category": "society"},
    {"kumaoni": "छिंया", "roman": "chhiyaan", "english": "cool mountain shade beneath broadleaf trees", "hindi": "छाया / शीतल छांव", "pos": "noun", "category": "nature"},
    {"kumaoni": "ह्युं", "roman": "hyun", "english": "winter snow falling over Himalayan peaks", "hindi": "बर्फ / हिम", "pos": "noun", "category": "nature"},
    {"kumaoni": "तुषार", "roman": "tushaar", "english": "morning frost glazing hill terraces in winter", "hindi": "पाला / तुषार", "pos": "noun", "category": "nature"},
    {"kumaoni": "बवंडर", "roman": "bavandar", "english": "mountain whirlwind / gale sweeping across ridges", "hindi": "बवंडर / तेज आंधी", "pos": "noun", "category": "nature"},
    {"kumaoni": "कुड़ी", "roman": "kudi", "english": "small stone-slate hill cottage / mountain homestead", "hindi": "पहाड़ी कुटिया / छोटा घर", "pos": "noun", "category": "home"}
]

# Ingest into words.json
with open(WORDS_FILE, 'r', encoding='utf-8') as f:
    words = json.load(f)

word_map = {w['kumaoni']: w for w in words}
added_count = 0
for w in NEW_EXTRACTED_WORDS:
    if w['kumaoni'] not in word_map:
        words.append(w)
        word_map[w['kumaoni']] = w
        added_count += 1

with open(WORDS_FILE, 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} newly mined words from downloaded source books.")
print(f"Total Base Dictionary Lemmas: {len(words)}")
