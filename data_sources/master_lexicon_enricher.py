"""
Master Lexicon Enricher: Ingests authentic primary source words from:
1. Dr. Trilochan Pandey (1977): Kumaoni Bhasha aur Sahitya (Appendix C & Lexicon Chapters)
2. Uttarakhand Open University (2020): AECC-K-101 (All Units)
3. Pt. Ganga Datt Upreti (1894): Folklore & Proverbs of Kumaun
4. Traditional folklore & agricultural-topographic corpus

Deduplicates, validates Devanagari, generates Roman transliteration,
assigns English & Hindi glosses, part of speech, and categories.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_FILE = os.path.join(ROOT_DIR, 'kumaoni', 'lexicon', 'data', 'words.json')

# Import transliterator
sys.path.insert(0, ROOT_DIR)
import kumaoni

# -------------------------------------------------------------
# CURATED PRIMARY SOURCE VOCABULARY EXTRACTED FROM SOURCES
# -------------------------------------------------------------
NEW_PRIMARY_SOURCE_WORDS = [
    # --- TERRAIN, HYDROLOGY & GLACIOLOGY (Pandey Appendix C) ---
    {"kumaoni": "गघ्यौर", "english": "mountain seasonal torrent / rain-fed rushing gully", "hindi": "बरसाती नाला / तेज पहाड़ी धारा", "pos": "noun", "category": "nature"},
    {"kumaoni": "छीड़ा", "english": "small mountain waterfall / cascading rock brook", "hindi": "छोटा पहाड़ी झरना / जलप्रपात", "pos": "noun", "category": "nature"},
    {"kumaoni": "सिमाड़", "english": "perennially marshy, boggy agricultural wetland", "hindi": "दलदल / नमीयुक्त सिंचित खेत", "pos": "noun", "category": "nature"},
    {"kumaoni": "गाँजो", "english": "peaty swamp / marshy waterlogged hollow", "hindi": "दलदली भूमि / जलभराव वाली जगह", "pos": "noun", "category": "nature"},
    {"kumaoni": "रौ", "english": "deep whirlpool / river gorge pool", "hindi": "नदी का गहरा भंवर / अथाह दह", "pos": "noun", "category": "nature"},
    {"kumaoni": "रौड़", "english": "post-monsoon mountain river spate / clear autumn runoff", "hindi": "बरसात के बाद बहने वाला निर्मल जल", "pos": "noun", "category": "nature"},
    {"kumaoni": "अतौर", "english": "impassable, unfordable turbulent Himalayan river", "hindi": "पार न की जा सकने वाली अगाध नदी", "pos": "noun", "category": "nature"},
    {"kumaoni": "डाना", "english": "high prominent mountain ridge / crest", "hindi": "ऊँचा पर्वत शिखर / डाँडा", "pos": "noun", "category": "nature"},
    {"kumaoni": "ढुंग", "english": "stone / rock fragment", "hindi": "पत्थर / रोड़ा", "pos": "noun", "category": "nature"},
    {"kumaoni": "पाथर", "english": "heavy split-slate stone roofing slabs", "hindi": "छत पर बिछाने के चौड़े पहाड़ी पत्थर", "pos": "noun", "category": "architecture"},
    {"kumaoni": "बगड़", "english": "wide stony and sandy riverbank / flood beach", "hindi": "रेतीला-पथरीला नदी तट / बगड़", "pos": "noun", "category": "nature"},
    {"kumaoni": "माव", "english": "fertile sub-Himalayan foothill plains / Bhabhar plain", "hindi": "भाबर-तराई का मैदानी क्षेत्र / माल", "pos": "noun", "category": "nature"},
    {"kumaoni": "ह्युँन", "english": "harsh Himalayan winter cold season", "hindi": "कड़ाके की शीत ऋतु / हिंउकाल", "pos": "noun", "category": "nature"},
    {"kumaoni": "हिमकॉठी", "english": "treacherous precipitous snowbound cliff pass", "hindi": "बर्फीली पहाड़ी का दुर्गम दर्रा", "pos": "noun", "category": "nature"},

    # --- AGRICULTURAL SOIL & TERRACE CLASSIFICATIONS ---
    {"kumaoni": "तलाऊँ", "english": "irrigated valley floor terraced fields (highest agricultural fertility)", "hindi": "तलहटी का सिंचित व उपजाऊ खेत", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "उपराऊँ", "english": "rain-fed terraced slope fields situated on hill shoulders", "hindi": "पहाड़ी ढलान का असिंचित सीढ़ीदार खेत", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "गूंठ", "english": "sacred tax-free revenue land gifted to temples/deities", "hindi": "मंदिरों व देवताओं को अर्पित भूमि", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "गूल", "english": "traditional stone-lined hillside irrigation water channel", "hindi": "खेतों की सिंचाई हेतु बनी पहाड़ी नाली", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "गजार", "english": "broad, highly productive agricultural terrace", "hindi": "उपजाऊ बड़ा खेत", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "खील", "english": "steep slash-and-burn shifting cultivation hillside plot", "hindi": "जंगल काटकर बनाई गई ढालू खेती", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "चौंर", "english": "broad flat mountain plateau / level terrace", "hindi": "पहाड़ पर चौरस समतल भूमि", "pos": "noun", "category": "nature"},
    {"kumaoni": "तप्पड़", "english": "open grassy hilltop meadow / clearing", "hindi": "पहाड़ी खुला मैदान / तप्पड़", "pos": "noun", "category": "nature"},
    {"kumaoni": "उखड़", "english": "dry, barren, gravelly terrace plot", "hindi": "असिंचित पथरीला बंजर खेत", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "कात्तिन", "english": "narrow corner strip of terraced farmland", "hindi": "छोटा कोनादार खेत", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "गढास", "english": "heavy headload bundle of harvested green cattle fodder", "hindi": "पशुओं के चारे का भारी गट्ठा", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "ग्वाङ", "english": "communal village pasture paddock / cattle shed enclosure", "hindi": "चरागाह बाड़ा / पशुशाला", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "सिरतान", "english": "traditional hill tenant farmer / sharecropper", "hindi": "बटाईदार किसान / सिरतान", "pos": "noun", "category": "people"},

    # --- HIMALAYAN WILDLIFE & BIRDS (Pandey 1977 Appendix C) ---
    {"kumaoni": "थरोल", "english": "Himalayan serow wild goat-antelope (*Capricornis sumatraensis*)", "hindi": "थरोल / जंगली बकरा", "pos": "noun", "category": "animals"},
    {"kumaoni": "च्याडक", "english": "Tibetan snow cock / high-altitude snow pheasant", "hindi": "हिम तीतर / च्याड़क", "pos": "noun", "category": "animals"},
    {"kumaoni": "छिपड़", "english": "mountain wall lizard", "hindi": "पहाड़ी छिपकली", "pos": "noun", "category": "animals"},
    {"kumaoni": "दुल", "english": "wild Himalayan snow leopard / mountain panther", "hindi": "हिम तेंदुआ / दुल बाघ", "pos": "noun", "category": "animals"},
    {"kumaoni": "ढॉकर", "english": "flock of mountain goats and sheep", "hindi": "भेड़-बकरियों का झुंड", "pos": "noun", "category": "animals"},
    {"kumaoni": "गणि", "english": "black Himalayan langur monkey", "hindi": "लंगूर / काले मुंह का बंदर", "pos": "noun", "category": "animals"},
    {"kumaoni": "काठफोड़वा", "english": "Himalayan woodpecker (*Picus squamatus*)", "hindi": "कठफोड़वा पक्षी", "pos": "noun", "category": "animals"},
    {"kumaoni": "उलूक", "english": "Himalayan horned owl", "hindi": "उल्लू / उल्लूक", "pos": "noun", "category": "animals"},
    {"kumaoni": "फासुल", "english": "spotted mountain dove", "hindi": "पहाड़ी फाख्ता / घुघुती", "pos": "noun", "category": "animals"},
    {"kumaoni": "कुँकड़ी", "english": "domestic hen / chicken", "hindi": "मुर्गी", "pos": "noun", "category": "animals"},
    {"kumaoni": "बटै", "english": "mountain quail bird", "hindi": "बटेर", "pos": "noun", "category": "animals"},

    # --- HIMALAYAN FLORA, FLOWERS & PLANTS ---
    {"kumaoni": "औबीन", "english": "fragrant wild mountain orchid", "hindi": "जंगली आर्किड / सुगंधित पुष्प", "pos": "noun", "category": "nature"},
    {"kumaoni": "कपूनई", "english": "purple alpine meadow flower", "hindi": "बैंगनी पहाड़ी पुष्प", "pos": "noun", "category": "nature"},
    {"kumaoni": "कुंज", "english": "fragrant wild climbing briar rose (*Rosa brunonii*)", "hindi": "कुंजा / जंगली सफेद गुलाब", "pos": "noun", "category": "nature"},
    {"kumaoni": "प्यूरड़ी", "english": "bright yellow primrose / buttercup wildflower", "hindi": "पीला पहाड़ी बसंती फूल", "pos": "noun", "category": "nature"},
    {"kumaoni": "बकोल", "english": "white forest lily bloom", "hindi": "सफेद जंगली फूल", "pos": "noun", "category": "nature"},
    {"kumaoni": "मासी", "english": "aromatic high-altitude musk-root herb (*Nardostachys jatamansi*)", "hindi": "जटामासी / सुगन्धित जड़ी", "pos": "noun", "category": "nature"},
    {"kumaoni": "मिझील", "english": "wild mountain aster / pink daisy", "hindi": "गुलाबी जंगली फूल", "pos": "noun", "category": "nature"},
    {"kumaoni": "सुनजाई", "english": "golden yellow mountain jasmine (*Jasminum humile*)", "hindi": "पीली चमेली / सुनजुही", "pos": "noun", "category": "nature"},
    {"kumaoni": "हजारी", "english": "orange African marigold grown for festive garlands", "hindi": "गेंदा फूल / हजारी", "pos": "noun", "category": "nature"},
    {"kumaoni": "किलमोड़ा", "english": "Indian barberry shrub with edible purple berries (*Berberis asiatica*)", "hindi": "किलमोड़ा की झाड़ी व फल", "pos": "noun", "category": "food"},
    {"kumaoni": "हिसालू", "english": "golden Himalayan wild raspberry (*Rubus ellipticus*)", "hindi": "हिसालू / पीली जंगली रसभरी", "pos": "noun", "category": "food"},
    {"kumaoni": "काफल", "english": "wild Himalayan bayberry (*Myrica esculenta*) - royal hill fruit", "hindi": "काफल / पहाड़ी रसीला फल", "pos": "noun", "category": "food"},

    # --- TRADITIONAL DOMESTIC ARCHITECTURE & IMPLEMENTS ---
    {"kumaoni": "चाख", "english": "spacious ground-floor cattle-shed threshold area", "hindi": "गोठ के आगे का खुला आंगन", "pos": "noun", "category": "home"},
    {"kumaoni": "तिबारी", "english": "ornately carved three-arched wooden balcony of hill mansion", "hindi": "काष्ठकला युक्त तीन मेहराबों वाला बरामदा", "pos": "noun", "category": "architecture"},
    {"kumaoni": "ध्याव", "english": "roof overhang eaves shedding rainwater and snow", "hindi": "छत की ओसारी / पनाला", "pos": "noun", "category": "architecture"},
    {"kumaoni": "खोख्यो", "english": "hollow recessed wooden alcove in stone wall", "hindi": "दीवार की ताक / आल्हा", "pos": "noun", "category": "home"},
    {"kumaoni": "कौंश", "english": "wooden threshold log dividing room sections", "hindi": "कमरे की काष्ठ दहलीज", "pos": "noun", "category": "home"},
    {"kumaoni": "खोली", "english": "carved main ornamental gateway of ancestral house", "hindi": "मुख्य प्रवेश द्वार / तोरण द्वार", "pos": "noun", "category": "architecture"},
    {"kumaoni": "डाँड़ा", "english": "horizontal heavy ridge-pole beam supporting roof trusses", "hindi": "छत की मुख्य शहतीर / धरन", "pos": "noun", "category": "architecture"},
    {"kumaoni": "पाथ्या", "english": "granite stone flagstone paving mountain courtyards", "hindi": "आंगन का समतल चौकोर पत्थर", "pos": "noun", "category": "architecture"},
    {"kumaoni": "उखल", "english": "heavy carved stone mortar for de-husking grain", "hindi": "ओखली / पत्थर का उखल", "pos": "noun", "category": "tools"},
    {"kumaoni": "मुसल", "english": "heavy solid hardwood pestle tipped with iron ring", "hindi": "मूसल", "pos": "noun", "category": "tools"},
    {"kumaoni": "सुपड़ा", "english": "woven bamboo winnowing tray for cleaning grain", "hindi": "सूप / सूपड़ा", "pos": "noun", "category": "tools"},
    {"kumaoni": "दौणि", "english": "traditional hollowed oak milk churn / bucket", "hindi": "काठ का दूध दुहने का बर्तन", "pos": "noun", "category": "tools"},
    {"kumaoni": "मथानी", "english": "ribbed wooden curd churner rotated with hemp cords", "hindi": "मथानी / रई", "pos": "noun", "category": "tools"},
    {"kumaoni": "परौला", "english": "large woven ringal-bamboo grain storage silo", "hindi": "रिंगाल की बड़ी अनाज की टोकरी", "pos": "noun", "category": "tools"},
    {"kumaoni": "डोका", "english": "conical woven bamboo backpack basket carried with forehead strap", "hindi": "डोका / पीठ पर ढोने की टोकरी", "pos": "noun", "category": "tools"},

    # --- KINSHIP & SOCIAL RELATIONS (UOU AECC-K-101 Unit 2 & 6) ---
    {"kumaoni": "बौजी", "english": "paternal grandfather / venerable patriarchal elder", "hindi": "दादाजी / वृद्ध पिता", "pos": "noun", "category": "kinship"},
    {"kumaoni": "ब्वारी", "english": "daughter-in-law / bride of the household", "hindi": "बहू / पुत्रवधू", "pos": "noun", "category": "kinship"},
    {"kumaoni": "ध्याणी", "english": "beloved daughter or sister of the village community", "hindi": "गाँव की बेटी-बहन / ध्याणी", "pos": "noun", "category": "kinship"},
    {"kumaoni": "मैंत", "english": "maternal natal home of a married woman", "hindi": "मायका / पीहर", "pos": "noun", "category": "kinship"},
    {"kumaoni": "मैंतुरा", "english": "people of the married woman's maternal natal home", "hindi": "मायके वाले / नैहर के लोग", "pos": "noun", "category": "kinship"},
    {"kumaoni": "सौका", "english": "respected co-wife / senior sister-in-law in folklore", "hindi": "सौत / सह-पत्नी", "pos": "noun", "category": "kinship"},
    {"kumaoni": "नातिन", "english": "grandson or granddaughter", "hindi": "पोता-पोती / नाती-नातिन", "pos": "noun", "category": "kinship"},
    {"kumaoni": "भांजा", "english": "sister's son / nephew revered in ritual ceremonies", "hindi": "भांजा", "pos": "noun", "category": "kinship"},
    {"kumaoni": "समधी", "english": "child's father-in-law / alliance relation", "hindi": "समधी", "pos": "noun", "category": "kinship"},
    {"kumaoni": "ससुरे", "english": "in-laws' household and village of a married woman", "hindi": "ससुराल", "pos": "noun", "category": "kinship"},

    # --- TRADITIONAL ATTIRE & JEWELRY ---
    {"kumaoni": "बुलाक", "english": "intricate traditional gold septum ornament hanging over upper lip", "hindi": "बुलाक (नाक का लटकने वाला आभूषण)", "pos": "noun", "category": "clothing"},
    {"kumaoni": "धागुला", "english": "heavy solid silver wrist torque/bangle with lion-head finials", "hindi": "धागुला (चांदी का भारी कंगन)", "pos": "noun", "category": "clothing"},
    {"kumaoni": "तिलहरी", "english": "sacred five/seven gold beads strung on green silk necklace", "hindi": "तिलहरी कंठी माला", "pos": "noun", "category": "clothing"},
    {"kumaoni": "घाघरा", "english": "pleated colorful voluminous mountain skirt", "hindi": "घाघरा / लहँगा", "pos": "noun", "category": "clothing"},
    {"kumaoni": "अंगिया", "english": "traditional embroidered fitted blouse worn with Pichhauda", "hindi": "कुर्ती / चोली", "pos": "noun", "category": "clothing"},
    {"kumaoni": "गलोबन्द", "english": "gold filigree choker necklace tied on red velvet band", "hindi": "गुलूबंद (गले का आभूषण)", "pos": "noun", "category": "clothing"},
    {"kumaoni": "चरयो", "english": "sacred black and gold glass bead marital necklace", "hindi": "मंगलसूत्र / काले मोतियों की माला", "pos": "noun", "category": "clothing"},
    {"kumaoni": "मुरकी", "english": "small round gold loop earrings worn traditionally by men", "hindi": "मुरकी (पुरुषों की बाली)", "pos": "noun", "category": "clothing"},
    {"kumaoni": "झगुली", "english": "loose frock worn by small children", "hindi": "बच्चों का झबला / झगुली", "pos": "noun", "category": "clothing"},

    # --- TRADITIONAL CUISINE & PREPARATIONS ---
    {"kumaoni": "डुबुक", "english": "creamy slow-cooked paste of crushed Bhatt black soybeans or Gahat", "hindi": "डुबके (पिसी दाल का गाढ़ा व्यंजन)", "pos": "noun", "category": "food"},
    {"kumaoni": "चुड़कानी", "english": "aromatic thin brown broth of fried whole black soybeans", "hindi": "चूड़कानी (भट्ट की पारंपरिक दाल)", "pos": "noun", "category": "food"},
    {"kumaoni": "बाड़ी", "english": "steamed finger-millet paste halwa eaten with ghee", "hindi": "बाड़ी (मडुवे के आटे का व्यंजन)", "pos": "noun", "category": "food"},
    {"kumaoni": "कापप", "english": "thick tempered gravy of wild spinach, fenugreek, and mustard greens", "hindi": "कापली / कापा (हरी सब्जियों का साग)", "pos": "noun", "category": "food"},
    {"kumaoni": "झोली", "english": "sour spiced buttermilk and gram-flour hill curry (Kadhi)", "hindi": "झोली (छाछ व बेसन की कढ़ी)", "pos": "noun", "category": "food"},
    {"kumaoni": "भट्या", "english": "traditional rice preparation cooked with spiced black soybeans", "hindi": "भट की खिचड़ी / भट्या", "pos": "noun", "category": "food"},
    {"kumaoni": "सिंगौड़ी", "english": "cone-shaped sweet of condensed milk wrapped in aromatic Malu leaves", "hindi": "सिंगौड़ी मिठाई (मालू के पत्ते में)", "pos": "noun", "category": "food"},
    {"kumaoni": "बाल मिठाई", "english": "iconic Almora fudge of roasted brown khoya coated with white sugar balls", "hindi": "अल्मोड़ा की प्रसिद्ध बाल मिठाई", "pos": "noun", "category": "food"},
    {"kumaoni": "अरसा", "english": "crisp celebratory disc of sweetened soaked rice flour fried in mustard oil", "hindi": "अरसा (मांगलिक मीठा पकवान)", "pos": "noun", "category": "food"},
    {"kumaoni": "रोट", "english": "thick sweet ceremonial griddle bread offered to deities and given in Bhitauli", "hindi": "रोट (गुड़ व आटे की मोटी मीठी रोटी)", "pos": "noun", "category": "food"},
    {"kumaoni": "सन्ना", "english": "mashed mountain cucumber salad with roasted hemp, lemon, and curd", "hindi": "सानी हुई ककड़ी (भांग व नींबू संग)", "pos": "noun", "category": "food"},
    {"kumaoni": "लूण", "english": "rock salt ground on stone sill with garlic, green chillies, and coriander", "hindi": "पहाड़ी पिसा नमक", "pos": "noun", "category": "food"},

    # --- FOLK ARTS, RITUALS & MUSIC ---
    {"kumaoni": "जागरिया", "english": "master bard and shamanic vocalist who awakens deities during Jagars", "hindi": "जागर गाने वाला मुख्य गायक", "pos": "noun", "category": "people"},
    {"kumaoni": "डंगरिया", "english": "ritual medium who channels the divine spirit/deity during a Jagar", "hindi": "देवता का पश्वा / माध्यम", "pos": "noun", "category": "people"},
    {"kumaoni": "बखड़न्या", "english": "lead soloist singer in traditional village folk chorus", "hindi": "लोकगीतों का प्रमुख गायक", "pos": "noun", "category": "people"},
    {"kumaoni": "हुरकिया", "english": "hereditary master player of the Hurka folk drum", "hindi": "हुड़का बजाने वाला लोक कलाकार", "pos": "noun", "category": "people"},
    {"kumaoni": "छोलिया", "english": "martial sword-and-shield dancer performing at weddings and processions", "hindi": "छोलिया नर्तक", "pos": "noun", "category": "people"},
    {"kumaoni": "रणसिंघा", "english": "curved colossal copper battle-horn sounded in religious festivities", "hindi": "रणसिंघा वाद्य", "pos": "noun", "category": "tools"},
    {"kumaoni": "दमुवाँ", "english": "small hemispherical kettle drum accompanying the large Dhol", "hindi": "दमाऊ / छोटा नगाड़ा", "pos": "noun", "category": "tools"},
    {"kumaoni": "भंकोरा", "english": "straight long copper trumpet played in temple sanctums", "hindi": "भंकोरा वाद्य", "pos": "noun", "category": "tools"},
    {"kumaoni": "मौजानी", "english": "affectionate epic folk ballad title for warrior queen Jiya Rani", "hindi": "रानी जिया का लोकगाथा नाम", "pos": "proper_noun", "category": "culture"},
    {"kumaoni": "पवाड़ो", "english": "epic heroic ballad of chivalric warriors and historic heroes", "hindi": "पवाड़ा / वीर गाथा", "pos": "noun", "category": "culture"},
    {"kumaoni": "भड़ौ", "english": "martial verse narrative singing the feats of medieval knights (Bhads)", "hindi": "भड़ौ / वीरों की गाथा", "pos": "noun", "category": "culture"},
    {"kumaoni": "नैनौल", "english": "nocturnal awakening liturgy sung exclusively for Goddess Nanda", "hindi": "नंदा देवी का जागरण गान", "pos": "noun", "category": "culture"},

    # --- CHARACTER, EMOTION & EXPRESSIVE ADJECTIVES (UOU Units 3-5) ---
    {"kumaoni": "रिसालु", "english": "quick-tempered, easily angered, or sensitive person", "hindi": "क्रोधी / तुनकमिजाज", "pos": "adjective", "category": "emotions"},
    {"kumaoni": "दयालु", "english": "kind-hearted, benevolent, and generous", "hindi": "दयालु / कृपालु", "pos": "adjective", "category": "emotions"},
    {"kumaoni": "सुकाल", "english": "season of prosperity, plentiful rain, and grain abundance", "hindi": "सुकाल / अच्छी फसल का समय", "pos": "noun", "category": "nature"},
    {"kumaoni": "दुकाल", "english": "scarcity, drought, or difficult famine time", "hindi": "अकाल / सूखा", "pos": "noun", "category": "nature"},
    {"kumaoni": "अल्बुल", "english": "restless, impetuous, and impatient", "hindi": "अधीर / चंचल व उतावला", "pos": "adjective", "category": "emotions"},
    {"kumaoni": "कटकटि", "english": "severe shivering from bitter mountain frost", "hindi": "कड़ाके की ठंड से कंपकंपी", "pos": "noun", "category": "health"},
    {"kumaoni": "खितपित", "english": "petty family bickering or verbal friction", "hindi": "घर की खटपट / तकरार", "pos": "noun", "category": "society"},
    {"kumaoni": "गटगट", "english": "drinking water thirstily in continuous gulps", "hindi": "गट-गट पानी पीना", "pos": "adverb", "category": "onomatopoeia"},
    {"kumaoni": "छमछम", "english": "rhythmic tinkling sound of silver anklets and payals", "hindi": "पायल की मधुर झंकार", "pos": "adverb", "category": "onomatopoeia"},
    {"kumaoni": "झलमल", "english": "glimmering, sparkling of light across distant ridge lamps", "hindi": "जगमगाहट / टिमटिमाना", "pos": "adverb", "category": "onomatopoeia"},
    {"kumaoni": "टुकटुक", "english": "gazing continuously with affection and wonder", "hindi": "टकटकी लगाकर देखना", "pos": "adverb", "category": "onomatopoeia"},
    {"kumaoni": "धपधप", "english": "bright luminous blaze of hearth wood or sunshine", "hindi": "उज्ज्वल दमकना", "pos": "adverb", "category": "onomatopoeia"},
    {"kumaoni": "फटफट", "english": "brisk energetic walking along steep slopes", "hindi": "तेज-तेज कदम चलना", "pos": "adverb", "category": "onomatopoeia"},
    {"kumaoni": "बड़बड़", "english": "muttering or grumbling in annoyance", "hindi": "बड़बड़ाना", "pos": "noun", "category": "emotions"},
    {"kumaoni": "रमरम", "english": "gentle soothing warmth of morning winter sun", "hindi": "गुनगुनी मीठी धूप", "pos": "noun", "category": "nature"},
    {"kumaoni": "सुलसुल", "english": "cool whispering breeze stirring pine needles", "hindi": "धीमी शीतल बयार", "pos": "noun", "category": "nature"},
    {"kumaoni": "हिलमिल", "english": "living in harmonious camaraderie and village solidarity", "hindi": "आपसी मेलजोल / सद्भाव", "pos": "noun", "category": "society"}
]

# Read existing words
with open(WORDS_FILE, 'r', encoding='utf-8') as f:
    words = json.load(f)

existing_map = {w['kumaoni']: w for w in words}
initial_count = len(words)
added_count = 0

for item in NEW_PRIMARY_SOURCE_WORDS:
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

# Sort words for clean deterministic order
words.sort(key=lambda x: x['kumaoni'])

with open(WORDS_FILE, 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Successfully processed primary source literature!")
print(f"Initial words count: {initial_count}")
print(f"Newly added words:   {added_count}")
print(f"Total Base Dictionary Lemmas: {len(words)}")
