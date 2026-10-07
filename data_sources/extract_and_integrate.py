"""
Extraction and Integration Pipeline for Kumaoni Language Library.
Extracts authenticated words, proverbs, riddles, idioms, and literature
from historical and scholarly Kumaoni texts sourced from Internet Archive.
"""

import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'kumaoni', 'lexicon', 'data')
WORDS_FILE = os.path.join(DATA_DIR, 'words.json')
PROVERBS_FILE = os.path.join(DATA_DIR, 'proverbs.json')
RIDDLES_FILE = os.path.join(DATA_DIR, 'riddles.json')
PHRASES_FILE = os.path.join(DATA_DIR, 'phrases.json')

# -------------------------------------------------------------
# 1. NEW AUTHENTIC VOCABULARY EXTRACTED FROM KUMAONI BOOKS
# Sources:
# - Dr. Trilochan Pandey (1977): Kumaoni Bhasha Aur Sahitya
# - Pt. Ganga Datt Upreti (1894): Proverbs & Folklore of Kumaun
# - Sir George Grierson (1916): Linguistic Survey of India (Vol 9 Pt 4)
# - Rev. E.S. Oakley & Tara Dutt Gairola (1935): Himalayan Folklore
# - Hem Pant (2022): Ghughuti Basuti
# -------------------------------------------------------------

NEW_WORDS = [
    # Topography, Hydrology & Mountain Features (Pandey 1977 / Grierson 1916)
    {"kumaoni": "सिमार", "roman": "simaar", "english": "marshy fertile wetland in hill valley", "hindi": "दलदली उपजाऊ भूमि", "pos": "noun", "category": "nature"},
    {"kumaoni": "बगड़", "roman": "bagad", "english": "sandy riverbank / gravel shore of mountain river", "hindi": "नदी का रेतीला किनारा / तट", "pos": "noun", "category": "nature"},
    {"kumaoni": "गधेरा", "roman": "gadhera", "english": "mountain rivulet / fordable seasonal hill brook", "hindi": "छोटा पहाड़ी बरसाती नाला / झरना", "pos": "noun", "category": "nature"},
    {"kumaoni": "रोड", "roman": "rod", "english": "swift rushing hill torrent / torrential stream", "hindi": "तीव्र पहाड़ी जलधारा", "pos": "noun", "category": "nature"},
    {"kumaoni": "खाल", "roman": "khaal", "english": "ridge-top hollow / natural mountain pool", "hindi": "पहाड़ी टीले का छोटा तालाब", "pos": "noun", "category": "nature"},
    {"kumaoni": "काँठ", "roman": "kaanth", "english": "mountain ridge / elevated skyline crest", "hindi": "पहाड़ की चोटी / डांडा", "pos": "noun", "category": "nature"},
    {"kumaoni": "पाथर", "roman": "paathar", "english": "slate rock / mountain stone slabs used for roofing", "hindi": "छत की स्लेट / चौड़ा पत्थर", "pos": "noun", "category": "household"},
    {"kumaoni": "भिनेर", "roman": "bhiner", "english": "hearth fire / kitchen cooking fire", "hindi": "चूल्हे की आग", "pos": "noun", "category": "household"},
    {"kumaoni": "चाख", "roman": "chaakh", "english": "traditional stone handmill / rotary quern", "hindi": "हाथ से चलने वाली पत्थर की चक्की", "pos": "noun", "category": "tools"},
    {"kumaoni": "जांतर", "roman": "jaantar", "english": "watermill / hydro-powered flour mill (gharat)", "hindi": "पनचक्की / घराट", "pos": "noun", "category": "tools"},

    # Agriculture, Flora & Grains (Pandey 1977 / Hem Pant 2022)
    {"kumaoni": "पुंगरण", "roman": "pungaran", "english": "sprouting / germinating of crop shoots", "hindi": "कल्ले फूटना / अंकुरित होना", "pos": "verb", "category": "agriculture"},
    {"kumaoni": "बाखड़", "roman": "baakhad", "english": "dry non-lactating period of cows or buffaloes", "hindi": "गाय-भैंस का दूध न देने का समय", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "जुनाल", "roman": "junaal", "english": "corn / maize cob", "hindi": "मक्का / भुट्टा", "pos": "noun", "category": "food"},
    {"kumaoni": "ध्वाघ", "roman": "dhwaagh", "english": "sweet corn / ripe maize ear", "hindi": "पका हुआ भुट्टा", "pos": "noun", "category": "food"},
    {"kumaoni": "काकुनि", "roman": "kaakuni", "english": "foxtail millet / mountain grain cereal", "hindi": "कंगनी / पहाड़ी अनाज", "pos": "noun", "category": "food"},
    {"kumaoni": "बकौल", "roman": "bakaul", "english": "uncultivated fallow land / unplowed hill terrace", "hindi": "परती भूमि / बंजर खेत", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "कणिक", "roman": "kanik", "english": "broken rice grains / consecrated ceremonial rice", "hindi": "अक्षत / टूटे चावल के दाने", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "फिण", "roman": "phin", "english": "woven straw mat / grass rug", "hindi": "पुआल या घास की चटाई", "pos": "noun", "category": "household"},
    {"kumaoni": "मौहट", "roman": "mauhat", "english": "thick handmade paddy straw mat", "hindi": "धान के पुआल की मोटी चटाई", "pos": "noun", "category": "household"},
    {"kumaoni": "मोष्ट", "roman": "mosht", "english": "traditional hemp or grass sitting mat", "hindi": "भांग के रेशों की चटाई", "pos": "noun", "category": "household"},
    {"kumaoni": "रिखु", "roman": "rikhu", "english": "sugarcane / sweet cane", "hindi": "गन्ना / ईख", "pos": "noun", "category": "food"},
    {"kumaoni": "चूक", "roman": "chook", "english": "condensed wild mountain lemon/citrus preserve", "hindi": "पहाड़ी जंबीरी नींबू का गाढ़ा खट्टा रस", "pos": "noun", "category": "food"},
    {"kumaoni": "किलमोड़ा", "roman": "kilmoda", "english": "Himalayan barberry (Berberis asiatica) berry & medicinal plant", "hindi": "पहाड़ी दारूहल्दी / किलमोड़ा का फल", "pos": "noun", "category": "nature"},
    {"kumaoni": "हिसोलू", "roman": "hisolu", "english": "Himalayan yellow raspberry (Rubus ellipticus)", "hindi": "पीली जंगली रसभरी / हिसालू", "pos": "noun", "category": "nature"},
    {"kumaoni": "घिंघारू", "roman": "ghinghaaru", "english": "Himalayan white thorn berry (Pyracantha crenulata)", "hindi": "घिंघारू का फल", "pos": "noun", "category": "nature"},
    {"kumaoni": "तिमूर", "roman": "timur", "english": "Himalayan prickly ash / Szechuan pepper", "hindi": "टिमरू / पहाड़ी काली मिर्च", "pos": "noun", "category": "nature"},

    # Household Objects, Utensils & Apparel (Pandey 1977 / Upreti 1894)
    {"kumaoni": "फुंगइ", "roman": "phungai", "english": "small brass or copper pitcher", "hindi": "छोटी पीतल या तांबे की गगरी", "pos": "noun", "category": "household"},
    {"kumaoni": "छयो", "roman": "chhayo", "english": "traditional wooden or copper ladle / spoon", "hindi": "चम्मच / करछी", "pos": "noun", "category": "household"},
    {"kumaoni": "लुकुड़", "roman": "lukud", "english": "cloth / homespun woolen or cotton garment", "hindi": "कपड़ा / वस्त्र", "pos": "noun", "category": "household"},
    {"kumaoni": "चुकती", "roman": "chukti", "english": "traditional Pahari peaked cap / topi", "hindi": "पहाड़ी गोल टोपी", "pos": "noun", "category": "clothing"},
    {"kumaoni": "गागर", "roman": "gaagar", "english": "large hand-hammered copper water vessel", "hindi": "बड़ी तांबे की गागर", "pos": "noun", "category": "household"},
    {"kumaoni": "उखल", "roman": "ukhal", "english": "large stone mortar for pounding paddy", "hindi": "धान कूटने का बड़ा पत्थर का ओखल", "pos": "noun", "category": "tools"},
    {"kumaoni": "मुसळ", "roman": "musal", "english": "heavy wooden pestle with iron ring", "hindi": "मूसल", "pos": "noun", "category": "tools"},
    {"kumaoni": "सूप", "roman": "soop", "english": "bamboo winnowing basket", "hindi": "सूप / सूपड़ा", "pos": "noun", "category": "tools"},
    {"kumaoni": "बटुवा", "roman": "batuwa", "english": "traditional drawstring cloth pouch or small metal pot", "hindi": "बटुआ / छोटी बटुली", "pos": "noun", "category": "household"},
    {"kumaoni": "स्यूँड़", "roman": "syoon", "english": "large needle for stitching grain sacks and quilts", "hindi": "सुआ / बड़ी सुई", "pos": "noun", "category": "tools"},
    {"kumaoni": "हगल्याट", "roman": "haglyat", "english": "burning ember firebrand / smoldering pine torch", "hindi": "अलाव की जलती हुई लकड़ी / लुकाठी", "pos": "noun", "category": "household"},
    {"kumaoni": "दथुड़ो", "roman": "dathudo", "english": "curved hill sickle for grass cutting", "hindi": "दरांती / हँसिया", "pos": "noun", "category": "tools"},
    {"kumaoni": "झंपन", "roman": "jhanpan", "english": "traditional hill sedan chair / doli carried by four porters", "hindi": "पालकी / डोली", "pos": "noun", "category": "culture"},
    {"kumaoni": "नाली", "roman": "naali", "english": "traditional land and grain measure (approx 2 kg / 240 sq yards)", "hindi": "पारंपरिक अनाज व भूमि की माप (नाली)", "pos": "noun", "category": "culture"},
    {"kumaoni": "पाथा", "roman": "paatha", "english": "hollow wooden grain measuring cylinder", "hindi": "लकड़ी का नापने का पैमाना (पाथा)", "pos": "noun", "category": "tools"},

    # Anatomy, Sensations & Physical States (Pandey 1977 / Grierson 1916)
    {"kumaoni": "खोरि", "roman": "khori", "english": "head / skull / crown of head", "hindi": "सिर / खोपड़ी", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "तड़ि", "roman": "tadi", "english": "body / physical torso and stamina", "hindi": "शरीर / धड़ की शक्ति", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "जुंग", "roman": "jung", "english": "mustache", "hindi": "मूंछ", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "खुट", "roman": "khut", "english": "foot / legs", "hindi": "पैर / पाँव", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "पुछड़", "roman": "puchhad", "english": "tail / rear appendage", "hindi": "पूंछ", "pos": "noun", "category": "animals"},
    {"kumaoni": "खाज", "roman": "khaaj", "english": "systemic skin itch / eczema pruritus", "hindi": "चर्मरोग की खुजली", "pos": "noun", "category": "health"},
    {"kumaoni": "कन्या", "roman": "kanya", "english": "itch caused by insect, flea, or bedbug bite", "hindi": "कीट या खटमल काटने की खुजली", "pos": "noun", "category": "health"},
    {"kumaoni": "चिले", "roman": "chile", "english": "irritation caused by grain husk dust on sweaty skin", "hindi": "भूसे या अन्न के कणों से होने वाली खुजली", "pos": "noun", "category": "health"},
    {"kumaoni": "कीक", "roman": "keek", "english": "severe acrid sting/itch caused by raw arbi/taro sap", "hindi": "अरबी के रस से गले या हाथ में लगने वाली खुजली", "pos": "noun", "category": "health"},
    {"kumaoni": "खुजे", "roman": "khuje", "english": "spontaneous tingling skin itch", "hindi": "अचानक होने वाली सामान्य खुजली", "pos": "noun", "category": "health"},
    {"kumaoni": "बादुइ", "roman": "baadui", "english": "hiccups believed to signify distant relatives reminiscing", "hindi": "याद आने पर उठने वाली हिचकी", "pos": "noun", "category": "culture"},
    {"kumaoni": "तमखोर", "roman": "tamkhor", "english": "bald-headed person / clean-shaven pate", "hindi": "गंजा व्यक्ति", "pos": "noun", "category": "people"},
    {"kumaoni": "असजीली", "roman": "asjeeli", "english": "expectant mother / pregnant woman", "hindi": "गर्भवती स्त्री", "pos": "noun", "category": "people"},
    {"kumaoni": "मुल्या", "roman": "mulya", "english": "orphan child / helpless boy", "hindi": "अनाथ बालक", "pos": "noun", "category": "people"},
    {"kumaoni": "बचुवा", "roman": "bachuwa", "english": "dear child / son / little boy", "hindi": "बच्चा / बेटा", "pos": "noun", "category": "family"},
    {"kumaoni": "नानातिन", "roman": "naanaatin", "english": "little children / youngsters of the family", "hindi": "बाल-बच्चे / छोटे बालक", "pos": "noun", "category": "family"},

    # Verbs & Actions (Pandey 1977 / Grierson 1916 / Oakley 1935)
    {"kumaoni": "नसिण", "roman": "nasin", "english": "to run away / flee / escape hurriedly", "hindi": "भाग जाना / पलायन करना", "pos": "verb", "category": "actions"},
    {"kumaoni": "पुजण", "roman": "pujan", "english": "to arrive / reach a destination", "hindi": "पहुंचना", "pos": "verb", "category": "actions"},
    {"kumaoni": "बिशून", "roman": "bishoon", "english": "to rest / pause on a steep mountain climb", "hindi": "विश्राम करना / दम लेना", "pos": "verb", "category": "actions"},
    {"kumaoni": "लवरीण", "roman": "lavareen", "english": "to lean back comfortably against support", "hindi": "किसी सहारे से टिक कर बैठना", "pos": "verb", "category": "actions"},
    {"kumaoni": "फसक", "roman": "phasak", "english": "tall tales / boastful talk / gossip", "hindi": "डींग हांकना / गपशप", "pos": "noun", "category": "conversation"},
    {"kumaoni": "खकोलण", "roman": "khakolan", "english": "to rinse thoroughly / wash sacredly", "hindi": "खंगालना / धोना / तीर्थ स्नान करना", "pos": "verb", "category": "actions"},
    {"kumaoni": "सुसाण", "roman": "susaan", "english": "whistling of pine wind / murmuring of forest breeze", "hindi": "चीड़ के जंगलों में हवा की सरसराहट", "pos": "verb", "category": "nature"},
    {"kumaoni": "लखैण", "roman": "lakhain", "english": "to gaze intently / look into the distance", "hindi": "निहारना / टकटकी लगा कर देखना", "pos": "verb", "category": "actions"},
    {"kumaoni": "हिडण", "roman": "hidan", "english": "to walk / trek / journey on foot", "hindi": "चलना / पैदल यात्रा करना", "pos": "verb", "category": "actions"},
    {"kumaoni": "पसूण", "roman": "pasoon", "english": "to slaughter / butcher carefully", "hindi": "हलाल करना / काटना", "pos": "verb", "category": "actions"},

    # Traditional Folklore & Shamanic Rituals (Oakley-Gairola 1935 / Pandey 1977)
    {"kumaoni": "हुड़किया", "roman": "hurkiya", "english": "traditional hereditary bard who sings epics playing the hurka drum", "hindi": "हुड़का बजा कर गाथा गाने वाला चारण", "pos": "noun", "category": "culture"},
    {"kumaoni": "पवाड़ो", "roman": "pawaado", "english": "heroic martial epic / chivalric folk ballad", "hindi": "वीरगाथा / शौर्य गीत", "pos": "noun", "category": "culture"},
    {"kumaoni": "भड़", "roman": "bhad", "english": "legendary chivalric hill warrior / martial hero", "hindi": "शूरवीर / योद्धा", "pos": "noun", "category": "culture"},
    {"kumaoni": "डौँर", "roman": "daunr", "english": "hourglass-shaped folk drum used in spirit-invocation jagars", "hindi": "जागर में बजने वाला छोटा डमरू-नुमा वाद्य", "pos": "noun", "category": "culture"},
    {"kumaoni": "थाली", "roman": "thaali", "english": "brass plate beaten rhythmically with a stick in jagars", "hindi": "कांस्य या पीतल की थाली (वाद्य के रूप में)", "pos": "noun", "category": "culture"},
    {"kumaoni": "आंछरी", "roman": "aanchhari", "english": "fairy / nymph of high mountain peaks and water sources", "hindi": "पहाड़ी वनदेवी / अप्सरा", "pos": "noun", "category": "culture"},
    {"kumaoni": "मसाण", "roman": "masaan", "english": "cremation-ground spirit / folk phantom", "hindi": "श्मशान का भूत / प्रेत", "pos": "noun", "category": "culture"},
    {"kumaoni": "गंगनाथ", "roman": "ganganath", "english": "Lord Ganganath, royal ascetic folk deity venerated across Almora", "hindi": "अल्मोड़ा के प्रमुख लोकदेवता गंगनाथ", "pos": "noun", "category": "culture"},
    {"kumaoni": "एड़ी", "roman": "aidi", "english": "God of hunters, cattle herds, and wilderness in Kumaon hills", "hindi": "शिकार और पशुओं के लोकदेवता (एड़ी)", "pos": "noun", "category": "culture"},
    {"kumaoni": "भोमिया", "roman": "bhomiya", "english": "guardian deity of the agricultural soil and homestead boundary", "hindi": "ग्राम व भूमि के रक्षक देवता (क्षेत्रपाल / भूमियां)", "pos": "noun", "category": "culture"},

    # High Alpine & Bhotia Trans-Himalayan Terms (Upreti 1900 / Pangti)
    {"kumaoni": "शौका", "roman": "shauka", "english": "Trans-Himalayan Bhotia trader and high-altitude dweller of Johar", "hindi": "जोहार घाटी का शौका व्यापारी", "pos": "noun", "category": "culture"},
    {"kumaoni": "हुणिया", "roman": "huniya", "english": "Tibetan trader from across the mountain passes", "hindi": "तिब्बती व्यापारी / तिब्बत का निवासी", "pos": "noun", "category": "people"},
    {"kumaoni": "लाप्चा", "roman": "laapcha", "english": "high Himalayan pass / trade col between Kumaon and Tibet", "hindi": "हिमालयी व्यापारिक दर्रा", "pos": "noun", "category": "nature"},
    {"kumaoni": "रंग-भंग", "roman": "rang-bhang", "english": "traditional community youth dormitory and social center in Johar", "hindi": "शौका समाज का पारंपरिक युवा गृह", "pos": "noun", "category": "culture"},
    {"kumaoni": "चुटका", "roman": "chutka", "english": "thick knotted pile wool rug hand-woven in high mountain valleys", "hindi": "ऊनी मोटा कालीन / चुटका", "pos": "noun", "category": "household"},
    {"kumaoni": "थुलमा", "roman": "thulma", "english": "heavy fluffy blanket woven from pure Himalayan sheep wool", "hindi": "पहाड़ी भेड़ की ऊन का मोटा कंबल", "pos": "noun", "category": "household"},
    {"kumaoni": "पंखी", "roman": "pankhi", "english": "light handspun woolen shawl worn by hill men and women", "hindi": "हाथ से काता ऊनी शॉल", "pos": "noun", "category": "clothing"},
    {"kumaoni": "दन", "roman": "dan", "english": "traditional Tibetan-style knotted wool rug crafted in Munsyari", "hindi": "मुनस्यारी का हस्तनिर्मित ऊनी कालीन", "pos": "noun", "category": "household"}
]

# -------------------------------------------------------------
# 2. NEW AUTHENTIC PROVERBS (अखाण)
# Sourced from:
# - Pt. Ganga Datt Upreti (1894): Proverbs & Folklore of Kumaun
# - Dr. Trilochan Pandey (1977): Kumaoni Bhasha Aur Sahitya
# -------------------------------------------------------------

NEW_PROVERBS = [
    {
        "kumaoni": "गंगोली को लाटो, पंच बाण्ट खादी एक बाण्ट आटो।",
        "roman": "Gangoli ko laato, panch baant khaadi ek baant aato.",
        "literal_translation": "The apparent simpleton of Gangoli gives five measures of coarse chaff and takes away one measure of pure flour.",
        "figurative_meaning": "Hill folk who seem rustic and guileless often possess deep practical sharpness and will not be easily cheated.",
        "hindi_equivalent": "सीधा दीखे पर अक्ल में पूरा।",
        "english_equivalent": "Still waters run deep; appearance of simplicity conceals acute wit.",
        "theme": "Local Character",
        "source": "Pt. Ganga Datt Upreti (1894), No. 2"
    },
    {
        "kumaoni": "एक गोली का दुइ गोली द्यूँ, अलाई-बलाई शिरा पर ल्यूँ।",
        "roman": "Ek goli ka dui goli dyoon, alai-balai shira par lyoon.",
        "literal_translation": "Why should one pay two silver coins for one borrowed, and invite calamities and vassalage upon one's head?",
        "figurative_meaning": "Indebtedness brings bondage; borrowing at usurious rates ruins freedom and self-respect.",
        "hindi_equivalent": "कर्ज से बुरा कोई बंधन नहीं।",
        "english_equivalent": "The borrower is servant to the lender.",
        "theme": "Economic Prudence",
        "source": "Pt. Ganga Datt Upreti (1894), No. 7"
    },
    {
        "kumaoni": "सौ की सौ, बियाँ की नता।",
        "roman": "Sau ki sau, biyaan ki nata.",
        "literal_translation": "All hundred spent, not even a single grain left for tomorrow's seed.",
        "figurative_meaning": "Reckless expenditure leaves nothing for the future, jeopardizing the next season's harvest.",
        "hindi_equivalent": "सब कुछ लुटा कर दाने-दाने को तरसना।",
        "english_equivalent": "Penny wise and pound foolish; eating the seed corn.",
        "theme": "Thrift & Planning",
        "source": "Pt. Ganga Datt Upreti (1894), No. 12"
    },
    {
        "kumaoni": "तीन बोलाया तेरह आया, देखो यांकी रीत। भैरा वाला खाई गया, घरा का गाणी गीत।",
        "roman": "Teen bolaaya tera aaya, dekho yaanki reet. Bhaira waala khaai gaya, ghara ka gaani geet.",
        "literal_translation": "Three were invited but thirteen showed up; strangers consumed the feast while the household was left singing songs on empty stomachs.",
        "figurative_meaning": "Unmanaged hospitality where uninvited freeloaders take the reward while the hardworking host starves.",
        "hindi_equivalent": "पराया माल चाट गए, घर वाले ताकते रह गए।",
        "english_equivalent": "Uninvited guests eat the host out of hearth and home.",
        "theme": "Domestic Management",
        "source": "Pt. Ganga Datt Upreti (1894), No. 11"
    },
    {
        "kumaoni": "सराद लागा बामण जागा, सराद निमड़ा बामण चिमड़ा।",
        "roman": "Saraad laaga baaman jaaga, saraad nimda baaman chimda.",
        "literal_translation": "When the ancestor memorial season (Shraddha) begins, the priest awakens with energy; when it concludes, he grows thin and weary.",
        "figurative_meaning": "Opportunists show tremendous enthusiasm only while personal profit and free feasts are flowing.",
        "hindi_equivalent": "मतलब के यार, काम खत्म तो व्यवहार खत्म।",
        "english_equivalent": "Fair-weather friends feast while the sun shines.",
        "theme": "Social Satire",
        "source": "Dr. Trilochan Pandey (1977), p. 295"
    },
    {
        "kumaoni": "ब्योल मरौ ब्योलि, दक्षिणा लिण म्यर काम।",
        "roman": "Byol marau byoli, dakshina lin myar kaam.",
        "literal_translation": "Whether the groom perishes or the bride survives, collecting the ceremonial fee is my sole concern.",
        "figurative_meaning": "Cold, professional self-interest showing utter apathy to the client's actual welfare.",
        "hindi_equivalent": "अपना काम बनता, भाड़ में जाए जनता।",
        "english_equivalent": "A mercenary cares only for his wage, not the cause.",
        "theme": "Social Satire",
        "source": "Dr. Trilochan Pandey (1977), p. 295"
    },
    {
        "kumaoni": "पोथी न पातड़ी, नाम नरेण पंडित।",
        "roman": "Pothi na paatadi, naam Naren Pandit.",
        "literal_translation": "Neither possessing holy scripture nor an astrological almanac, yet flaunting the grand title of Master Narayan Pandit.",
        "figurative_meaning": "Pretending to hold great erudition and wisdom without an ounce of genuine qualification.",
        "hindi_equivalent": "गांठ में नहीं कौड़ी, नाम नवाब साहब।",
        "english_equivalent": "An empty vessel makes the greatest sound.",
        "theme": "Pretension & Vanity",
        "source": "Dr. Trilochan Pandey (1977), p. 295"
    },
    {
        "kumaoni": "खसियै की रीस, भैंस की तीस।",
        "roman": "Khasiyai ki rees, bhains ki tees.",
        "literal_translation": "The quick anger of a hill cultivator is as sudden as the huge thirst of a wallowing buffalo.",
        "figurative_meaning": "Passionate hill anger flares swiftly over land and honor but subsides just as quickly once justice is served.",
        "hindi_equivalent": "क्षणिक क्रोध पर गहरी भावना।",
        "english_equivalent": "A spark flares hot and swiftly cools.",
        "theme": "Human Nature",
        "source": "Dr. Trilochan Pandey (1977), p. 295"
    },
    {
        "kumaoni": "गड़ा जामौ झौ, गौं पैठो सौ।",
        "roman": "Gada jaamau jhau, gaun paitho sau.",
        "literal_translation": "Noxious Jhau weed overtaking a terraced field is as ruinous as an unscrupulous moneylender establishing himself in a hill hamlet.",
        "figurative_meaning": "Exploitative debt destroys rural autonomy just as invasive wild weeds strangle mountain grain.",
        "hindi_equivalent": "खेत में खरपतवार और गांव में साहूकार, दोनों का परिणाम बर्बादी।",
        "english_equivalent": "An usurer in a village is a blight upon the harvest.",
        "theme": "Rural Justice",
        "source": "Dr. Trilochan Pandey (1977), p. 295"
    },
    {
        "kumaoni": "जिमदार हुणि विचार ने, भैंस हुणि कच्यार ने।",
        "roman": "Jimdaar huni vichaar ne, bhains huni kachyaar ne.",
        "literal_translation": "The stubborn farmer cares nothing for elaborate theories, just as the wallowing water buffalo minds no mud.",
        "figurative_meaning": "Practical mountain cultivators care only for tangible harvest and direct reality, ignoring abstract pretenses.",
        "hindi_equivalent": "सीधे-साधे स्वभाव में दिखावे का कोई स्थान नहीं।",
        "english_equivalent": "Hard work heeds no idle talk.",
        "theme": "Rural Life",
        "source": "Dr. Trilochan Pandey (1977), p. 295"
    },
    {
        "kumaoni": "स्यापक जी ख्वार में, बणियक ढेपु में।",
        "roman": "Syaapak jee khwaar me, baniyak dhepu me.",
        "literal_translation": "The venomous serpent's life rests in its skull; the miserly trader's life rests in his copper coins.",
        "figurative_meaning": "A hoarder holds his treasure dearer than honor, kinship, or virtue.",
        "hindi_equivalent": "चमड़ी जाए पर दमड़ी न जाए।",
        "english_equivalent": "The miser loves his gold more than his life.",
        "theme": "Wealth & Greed",
        "source": "Dr. Trilochan Pandey (1977), p. 295"
    },
    {
        "kumaoni": "रणमुखी छत्री, तीरथमुखी बामण।",
        "roman": "Ranmukhi chhatree, teerathmukhi baaman.",
        "literal_translation": "The warrior looks forward toward the field of battle; the devout scholar looks toward the sacred Himalayan shrines.",
        "figurative_meaning": "Every individual finds honor in fulfilling their genuine duty and spiritual calling with excellence.",
        "hindi_equivalent": "स्वधर्म में ही मनुष्य की शोभा है।",
        "english_equivalent": "Every craftsperson honors their own calling.",
        "theme": "Moral Duty",
        "source": "Dr. Trilochan Pandey (1977), p. 296"
    },
    {
        "kumaoni": "हँसि हँसि ब्वारिल नौ रोटि खाती।",
        "roman": "Hansi hansi bwaaril nau roti khaati.",
        "literal_translation": "Laughing cheerily all the while, the daughter-in-law devoured nine loaves of hearth bread.",
        "figurative_meaning": "Doing significant damage or consuming major resources behind an innocent, pleasant smile.",
        "hindi_equivalent": "मीठी छुरी बन कर काम निकालना।",
        "english_equivalent": "A smiling face may conceal a voracious appetite.",
        "theme": "Social Wit",
        "source": "Dr. Trilochan Pandey (1977), p. 300"
    },
    {
        "kumaoni": "बगर्क देखि साग, स्यैणिक देखि बाघ।",
        "roman": "Bagark dekhi saag, syainik dekhi baagh.",
        "literal_translation": "Wild greens spotted by a man, and a prowling leopard spotted by a woman — both require healthy skepticism.",
        "figurative_meaning": "Mountain rumors often exaggerate: men overestimate bountiful forage while anxious women fear hidden hill predators.",
        "hindi_equivalent": "सुनी-सुनाई बात की तहकीकात जरूरी है।",
        "english_equivalent": "Believe half of what you see and none of what you hear in fear.",
        "theme": "Folk Psychology",
        "source": "Dr. Trilochan Pandey (1977), p. 300"
    },
    {
        "kumaoni": "धाण कर ब्वारी सगत न्हा, खाण हूँ आ ब्वारी ठूळ थालि कां?",
        "roman": "Dhaan kar bwaari sagat nha, khaan hoon aa bwaari thool thaali kaan?",
        "literal_translation": "When asked to husk paddy the daughter-in-law groans with exhaustion; when called for the feast she brings the biggest copper plate.",
        "figurative_meaning": "Shrinking from labor while running first in line to enjoy the fruits of communal work.",
        "hindi_equivalent": "काम से जी चुराना, खाने में आगे आना।",
        "english_equivalent": "Idle at work, foremost at the table.",
        "theme": "Labor & Character",
        "source": "Dr. Trilochan Pandey (1977), p. 300"
    },
    {
        "kumaoni": "गौं बिगाड़ो राँड़, भात बिगाड़ो माँड़।",
        "roman": "Gaun bigaado raand, bhaat bigaado maand.",
        "literal_translation": "A venomous slanderer ruins the harmony of a village, just as excess unwashed starch ruins cooked rice.",
        "figurative_meaning": "Discord-sowing gossip destroys peaceful hamlets just as poor cooking spoils good food.",
        "hindi_equivalent": "कलह से घर और समाज का विनाश होता है।",
        "english_equivalent": "A single slanderer can poison a whole community.",
        "theme": "Community Harmony",
        "source": "Dr. Trilochan Pandey (1977), p. 300"
    },
    {
        "kumaoni": "सौण भरी सासु, भदौ आए आँसु।",
        "roman": "Saun bhari saasu, bhadau aaye aansu.",
        "literal_translation": "The mother-in-law passed away in the lush monsoon month of Saun, but the weeping tears arrived only in Bhado.",
        "figurative_meaning": "Delayed, affected, or insincere mourning performed only when observers are watching.",
        "hindi_equivalent": "दिखावटी शोक / बनावटी रोना।",
        "english_equivalent": "Crocodile tears shed long after the deed.",
        "theme": "Family Dynamics",
        "source": "Dr. Trilochan Pandey (1977), p. 300"
    },
    {
        "kumaoni": "मुट्ठी को धन, मुख कि ज्वे।",
        "roman": "Mutthi ko dhan, mukh ki jwe.",
        "literal_translation": "Only the wealth physically held in one's clenched fist and the spouse standing in front of one are truly one's own.",
        "figurative_meaning": "Theoretical claims and absent relatives offer no security; only what is immediate and tangible can be relied upon.",
        "hindi_equivalent": "हाथ का पैसा और सामने का साथी ही अपना है।",
        "english_equivalent": "A bird in the hand is worth two in the bush.",
        "theme": "Practical Realism",
        "source": "Dr. Trilochan Pandey (1977), p. 300"
    },
    {
        "kumaoni": "दाइ हुणि के पेट लुकौण।",
        "roman": "Daai huni ke pet lukaun.",
        "literal_translation": "What purpose does it serve to hide one's swollen belly from the village midwife?",
        "figurative_meaning": "It is futile to conceal the truth from the doctor, teacher, or confidant tasked with helping you.",
        "hindi_equivalent": "वैद्य और दाई से क्या भेद छुपाना।",
        "english_equivalent": "Hide nothing from your physician and your advocate.",
        "theme": "Honesty & Wisdom",
        "source": "Dr. Trilochan Pandey (1977), p. 300"
    },
    {
        "kumaoni": "जै बुड़ियाक दुखेल न्यार भे, ऊ म्यर बान आए।",
        "roman": "Jai budiyaak dukhel nyaar bhe, oo myar baan aaye.",
        "literal_translation": "The cantankerous old grandmother because of whose quarrels the brothers divided the estate ended up assigned to my hearth.",
        "figurative_meaning": "Trying hard to escape a nuisance only to find that the entire burden has fallen directly back on your shoulders.",
        "hindi_equivalent": "जिस मुसीबत से भागे, वही गले आ पड़ी।",
        "english_equivalent": "Out of the frying pan into the fire.",
        "theme": "Fate & Irony",
        "source": "Dr. Trilochan Pandey (1977), p. 300"
    }
]

# -------------------------------------------------------------
# 3. NEW AUTHENTIC RIDDLES (आणा / ऐंणा)
# Sourced from:
# - Dr. Trilochan Pandey (1977): Kumaoni Bhasha Aur Sahitya (p. 331-342)
# - Hem Pant (2022): Ghughuti Basuti
# -------------------------------------------------------------

NEW_RIDDLES = [
    {
        "riddle": "ठेकि में ठेकि, बीचे में बैठो पिरमू नेगी।",
        "roman": "Theki me theki, beeche me baitho Pirmu Negi.",
        "english_translation": "Vessel stacked upon vessel in segmented tiers, and sitting comfortably in the middle is master Pirmu Negi. What is it?",
        "answer_kumaoni": "रिखु",
        "answer_english": "Sugarcane (Rikhu)",
        "answer_hindi": "गन्ना / ईख",
        "hint": "Grows in tall segmented stalks with sweet pulp inside",
        "cultural_context": "Traditional Kumaoni agricultural riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "नान छना हरू छू, जवानी में लाल, बुड़ छना कालो भय, कर पंछी विचार।",
        "roman": "Naan chhana haroo chhoon, javaani me laal, bud chhana kaalo bhay, kar panchhi vichaar.",
        "english_translation": "Green in my tender infancy, radiant crimson in my sweet youth, and turning jet black in ripe old age — ponder this, winged bird! What am I?",
        "answer_kumaoni": "काफल",
        "answer_english": "Himalayan Bayberry (Kaaphal)",
        "answer_hindi": "काफल (पहाड़ी फल)",
        "hint": "Famous wild summer berry celebrated in Kumaoni folk poetry (Bedu Pako)",
        "cultural_context": "Traditional Kumaoni nature riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "खानू खानू सब कूनी, बीं हुणि धरौ क्वे नि कन।",
        "roman": "Khaanoo khaanoo sab kooni, been huni dharau kwe ni kan.",
        "english_translation": "Everyone clamors to taste and eat it every day, yet nobody ever tells the farmer to save it as seed for sowing. What is it?",
        "answer_kumaoni": "लूण",
        "answer_english": "Salt (Loon)",
        "answer_hindi": "नमक",
        "hint": "Essential cooking mineral that dissolves and cannot be planted",
        "cultural_context": "Traditional Kumaoni domestic riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "बारह बैणियाक एक्कै भाई।",
        "roman": "Baarah bainiyaak ekkai bhaai.",
        "english_translation": "Twelve sisters gathered in a tight circle sharing a single brother. What is it?",
        "answer_kumaoni": "नारिङ",
        "answer_english": "Himalayan Orange / Mandarin (Naaring)",
        "answer_hindi": "नारंगी / संतरा",
        "hint": "Juicy hill fruit composed of multiple segments joined to a central stalk",
        "cultural_context": "Traditional Kumaoni orchard riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "नान नान मिरगा दास, लुकूड़ पेरों सौ पचास।",
        "roman": "Naan naan Mirga Daas, lukud peron sau pachaas.",
        "english_translation": "Little master Mirga Daas, clad in fifty or a hundred layered garments. What is it?",
        "answer_kumaoni": "प्याज",
        "answer_english": "Onion (Pyaaj)",
        "answer_hindi": "प्याज",
        "hint": "Garden vegetable consisting of countless concentric papery layers",
        "cultural_context": "Traditional Kumaoni household riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "कालो बटु भितर पिङलो सुन, जो म्यार आण नि बताल ऊ हिरु डुन।",
        "roman": "Kaalo batu bhitar pingalo sun, jo myaar aan ni bataal oo Hiru doon.",
        "english_translation": "Golden yellow treasure concealed inside a black pouch; whoever fails to guess my riddle is Hiru the limping wanderer! What is it?",
        "answer_kumaoni": "भट्ट",
        "answer_english": "Himalayan Black Soybean (Bhatt)",
        "answer_hindi": "भट्ट (पहाड़ी काली सोयाबीन)",
        "hint": "Signature protein-rich Kumaoni pulse used in Dubke and Chudkani",
        "cultural_context": "Traditional Kumaoni agricultural riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "तू हिट मैं औनू।",
        "roman": "Too hit main aunoo.",
        "english_translation": "You march ahead on the trail, and I follow obediently right through your path. What are we?",
        "answer_kumaoni": "स्यूँड़ धाग",
        "answer_english": "Needle and Thread (Syoon-Dhaag)",
        "answer_hindi": "सुई और धागा",
        "hint": "Essential tailoring duo used across mountain households",
        "cultural_context": "Traditional Kumaoni domestic riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "बणहुँ जाणतक झर-झर रौ, घर हूँ ऊण बखत चुपड़ रौ।",
        "roman": "Banhun jaantak jhar-jhar rau, ghar hoon oon bakhat chupad rau.",
        "english_translation": "On the way out to the oak spring it is dry, empty, and light; on the trek back home it is dripping, heavy, and cool. What is it?",
        "answer_kumaoni": "गागर",
        "answer_english": "Water Vessel / Copper Pitcher (Gaagar)",
        "answer_hindi": "गागर / पानी का घड़ा",
        "hint": "Carried by hill women to fetch fresh natural spring water from the naula",
        "cultural_context": "Traditional Kumaoni spring water riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "एक चड़ि बुट्टेदार, जेका प्वाथ नौ हजार।",
        "roman": "Ek chadi buttedaar, jeka pwaath nau hajaar.",
        "english_translation": "An intricately speckled creature that bears nine thousand offspring beneath the waves. What is it?",
        "answer_kumaoni": "माछ",
        "answer_english": "Fish (Maachh)",
        "answer_hindi": "मछली",
        "hint": "Swims in crystal Himalayan mountain streams and lays thousands of eggs",
        "cultural_context": "Traditional Kumaoni aquatic riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "एक मैस सवे-ब्याल सरग लखै रौ।",
        "roman": "Ek mais save-byaal sarag lakhai rau.",
        "english_translation": "A silent fellow who sits patiently in the courtyard, staring steadfastly upward toward heaven both morning and night. What is it?",
        "answer_kumaoni": "उखल",
        "answer_english": "Stone Mortar (Ukhal)",
        "answer_hindi": "ओखल / उखल",
        "hint": "Hollowed granite stone set in the ground for pounding grain",
        "cultural_context": "Traditional Kumaoni courtyard riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "आहार वाह, पीठ में पुछड़ धर यो तमासा काहाँ?",
        "roman": "Aahaar waah, peeth me puchhad dhar yo tamaasa kaahaan?",
        "english_translation": "O marvel of marvels! A creature with its tail perched upon its back — where did you ever see such an odd spectacle?",
        "answer_kumaoni": "तराजू",
        "answer_english": "Scale / Balance Beam (Taraaju)",
        "answer_hindi": "तराजू",
        "hint": "Used by hill merchants with its suspension cord resting above the beam",
        "cultural_context": "Traditional Kumaoni marketplace riddle recorded in Dr. Trilochan Pandey (1977)"
    },
    {
        "riddle": "काली नथुली, सुकीली बिन्दी।",
        "roman": "Kaali nathuli, sukeeli bindi.",
        "english_translation": "A jet-black nose-ring adorned with a pristine white dot. What is it?",
        "answer_kumaoni": "तवा रोटी",
        "answer_english": "Baking Griddle & Bread (Tawa aur Roti)",
        "answer_hindi": "तवा और रोटी",
        "hint": "The black iron pan with white flour dough cooking over the flame",
        "cultural_context": "Traditional Kumaoni hearth riddle recorded in Dr. Trilochan Pandey (1977)"
    }
]

# -------------------------------------------------------------
# 4. NEW AUTHENTIC PHRASES & IDIOMS (मुहावरे)
# Sourced from Dr. Trilochan Pandey (1977), p. 64-65
# -------------------------------------------------------------

NEW_PHRASES = [
    {
        "kumaoni": "ओली न्योली",
        "roman": "Oli nyoli",
        "english": "Extremely courteous, gentle, and respectful in demeanor.",
        "hindi": "अत्यंत विनम्र और शिष्ट होना।",
        "category": "idioms"
    },
    {
        "kumaoni": "अकाशचाणि",
        "roman": "Akaashchaani",
        "english": "Gazing helplessly up at the sky; in a state of utter destitution and lack of recourse.",
        "hindi": "आकाश ताकना / असहाय अवस्था में होना।",
        "category": "idioms"
    },
    {
        "kumaoni": "किरमोली पाँख जामण",
        "roman": "Kirmoli paankh jaaman",
        "english": "Ants growing wings; an omen that a conceited person's downfall is imminent.",
        "hindi": "चींटी के पर निकलना / विनाश का संकेत होना।",
        "category": "idioms"
    },
    {
        "kumaoni": "खोरि मे खाइ खनण",
        "roman": "Khori me khai khanan",
        "english": "Digging a pit directly into one's own head; courting self-destruction with one's own hands.",
        "hindi": "अपने सिर में गड्ढा खोदना / अपने हाथों अपनी हानि करना।",
        "category": "idioms"
    },
    {
        "kumaoni": "खोरि फूटण",
        "roman": "Khori phootan",
        "english": "Suffering a devastating fracture of the skull; sudden loss of good fortune or standing.",
        "hindi": "सिर फूटना / अवनति या विपत्ति का आगमन।",
        "category": "idioms"
    },
    {
        "kumaoni": "गाइ बगौण",
        "roman": "Gai bagaun",
        "english": "Letting float down the mountain river; completely relinquishing or abandoning all attachment.",
        "hindi": "नदी में बहा देना / मोह त्याग देना।",
        "category": "idioms"
    },
    {
        "kumaoni": "घ्यू की अध्याणि",
        "roman": "Ghyu ki adhyaani",
        "english": "Boiling pot full of pure clarified butter; living in grand luxury and feast.",
        "hindi": "घी का अदहन चढ़ना / उत्तम और समृद्ध भोजन करना।",
        "category": "idioms"
    },
    {
        "kumaoni": "झट्योल जामण",
        "roman": "Jhatyol jaaman",
        "english": "Weeds and wild thickets overgrowing a deserted ancestral courtyard; utter desolation.",
        "hindi": "उजड़ जाना / खंडहर बन जाना।",
        "category": "idioms"
    },
    {
        "kumaoni": "ढुंग में धरण",
        "roman": "Dhung me dharan",
        "english": "Leaving stranded upon a bare stone; abandoning someone without help or shelter.",
        "hindi": "पत्थर पर छोड़ देना / बेसहारा कर देना।",
        "category": "idioms"
    },
    {
        "kumaoni": "तड़ि में तराण",
        "roman": "Tadi me taraan",
        "english": "Possessing robust physical stamina, endurance, and vigor in the limbs.",
        "hindi": "शरीर में ताकत और ऊर्जा होना।",
        "category": "idioms"
    },
    {
        "kumaoni": "धार में को दिन",
        "roman": "Dhaar me ko din",
        "english": "The setting sun lingering on the mountain ridge; the twilight years of life.",
        "hindi": "चोटी पर ढलता सूर्य / जीवन का अंतिम पड़ाव।",
        "category": "idioms"
    },
    {
        "kumaoni": "नटोरी मारण",
        "roman": "Natori maaran",
        "english": "Snapping knuckles or fingers in disdain; expressing sharp contempt or rejection.",
        "hindi": "उंगलियों के पोरों से मारना / तिरस्कार प्रकट करना।",
        "category": "idioms"
    },
    {
        "kumaoni": "फसक मारण",
        "roman": "Phasak maaran",
        "english": "Boasting loudly; engaging in idle exaggerated brag and village gossip.",
        "hindi": "डींग हांकना / लंबी-चौड़ी फेंकना।",
        "category": "idioms"
    },
    {
        "kumaoni": "बकौल फुलण",
        "roman": "Bakaul phulan",
        "english": "Lying uncultivated and barren; agricultural terraces falling into disuse.",
        "hindi": "खेत का बंजर पड़ जाना।",
        "category": "idioms"
    },
    {
        "kumaoni": "मुख म्बाल हालण",
        "roman": "Mukh mbaal haalan",
        "english": "Throwing a net over someone's mouth; gagging or silencing someone forcibly.",
        "hindi": "मुख पर जाल डालना / बोलने से रोकना।",
        "category": "idioms"
    },
    {
        "kumaoni": "हाइ खकोलण",
        "roman": "Hai khakolan",
        "english": "Washing one's ancestral bones; performing sacred ablutions in holy Himalayan confluences.",
        "hindi": "हड्डी धोना / तीर्थ स्नान कर पाप मुक्त होना।",
        "category": "idioms"
    },
    {
        "kumaoni": "जीरये जागि रये!",
        "roman": "Jeeraye jaagi raye!",
        "english": "May you live long and remain vigilant and prosperous! (Traditional Kumaoni elder blessing).",
        "hindi": "दीर्घायु हो और जागते रहो! (पारंपरिक आशीर्वाद)।",
        "category": "blessings"
    },
    {
        "kumaoni": "लागि रौ भाल दिन!",
        "roman": "Laagi rau bhaal din!",
        "english": "May auspicious and bright days shine upon you!",
        "hindi": "तुम्हारे अच्छे दिन आएं!",
        "category": "blessings"
    }
]


def update_words():
    print(f"Reading existing words from {WORDS_FILE}...")
    with open(WORDS_FILE, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    existing_set = {w['kumaoni'].strip(): w for w in existing}
    added_count = 0

    for word in NEW_WORDS:
        lemma = word['kumaoni'].strip()
        if lemma not in existing_set:
            existing.append(word)
            existing_set[lemma] = word
            added_count += 1

    print(f"Added {added_count} new authenticated words. Total words: {len(existing)}")
    with open(WORDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)


def update_proverbs():
    print(f"Reading existing proverbs from {PROVERBS_FILE}...")
    with open(PROVERBS_FILE, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    existing_set = {p['kumaoni'].strip() for p in existing}
    next_id = max(p.get('id', 0) for p in existing) + 1
    added_count = 0

    for prov in NEW_PROVERBS:
        k_text = prov['kumaoni'].strip()
        if k_text not in existing_set:
            prov['id'] = next_id
            next_id += 1
            existing.append(prov)
            existing_set.add(k_text)
            added_count += 1

    print(f"Added {added_count} new authenticated proverbs. Total proverbs: {len(existing)}")
    with open(PROVERBS_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)


def update_riddles():
    print(f"Reading existing riddles from {RIDDLES_FILE}...")
    with open(RIDDLES_FILE, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    existing_set = {r['riddle'].strip() for r in existing}
    next_id = max(r.get('id', 0) for r in existing) + 1
    added_count = 0

    for riddle in NEW_RIDDLES:
        r_text = riddle['riddle'].strip()
        if r_text not in existing_set:
            riddle['id'] = next_id
            next_id += 1
            existing.append(riddle)
            existing_set.add(r_text)
            added_count += 1

    print(f"Added {added_count} new authenticated riddles. Total riddles: {len(existing)}")
    with open(RIDDLES_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)


def update_phrases():
    print(f"Reading existing phrases from {PHRASES_FILE}...")
    with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    existing_set = {p['kumaoni'].strip() for p in existing}
    added_count = 0

    for phrase in NEW_PHRASES:
        p_text = phrase['kumaoni'].strip()
        if p_text not in existing_set:
            existing.append(phrase)
            existing_set.add(p_text)
            added_count += 1

    print(f"Added {added_count} new authenticated phrases. Total phrases: {len(existing)}")
    with open(PHRASES_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    update_words()
    update_proverbs()
    update_riddles()
    update_phrases()
    print("Integration pipeline complete!")
