"""
Master Update and Integration Script for Kumaoni Language Library v1.1.0
Integrates:
- UOU AECC-K-101 Textbooks: Idioms, Proverbs, Riddles, Vocabulary
- Master Bibliography (Excel Sheet + User's Comprehensive Working Bibliography)
- New Canonical Authors in literature.py
"""

import json
import os
import sys
import zipfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'kumaoni', 'lexicon', 'data')
CULTURE_DATA_DIR = os.path.join(ROOT_DIR, 'kumaoni', 'culture', 'data')
os.makedirs(CULTURE_DATA_DIR, exist_ok=True)

WORDS_FILE = os.path.join(DATA_DIR, 'words.json')
PROVERBS_FILE = os.path.join(DATA_DIR, 'proverbs.json')
RIDDLES_FILE = os.path.join(DATA_DIR, 'riddles.json')
PHRASES_FILE = os.path.join(DATA_DIR, 'phrases.json')
BIB_FILE = os.path.join(CULTURE_DATA_DIR, 'bibliography.json')

# ----------------------------------------------------------------------
# 1. NEW WORDS (UOU AECC-K-101 & Himalayan Cultural Terminology)
# ----------------------------------------------------------------------
UOU_WORDS = [
    {"kumaoni": "खाप", "roman": "khaap", "english": "mouth / oral cavity", "hindi": "मुँह", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "रीस", "roman": "rees", "english": "anger / wrath / fierce indignation", "hindi": "क्रोध / गुस्सा", "pos": "noun", "category": "emotions"},
    {"kumaoni": "कलिजो", "roman": "kalijo", "english": "liver / heart / soul / innermost seat of affection", "hindi": "कलेजा / अंतरात्मा", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "डज्या", "roman": "dajya", "english": "burnt / scorched / singed by flame", "hindi": "जला हुआ / झुलसा हुआ", "pos": "adjective", "category": "state"},
    {"kumaoni": "गोरू", "roman": "goru", "english": "cow / cattle / bovine livestock", "hindi": "गाय / मवेशी", "pos": "noun", "category": "animals"},
    {"kumaoni": "फसक", "roman": "phasak", "english": "idle gossip / cheerful mountain banter", "hindi": "गपशप / किस्सागोई", "pos": "noun", "category": "conversation"},
    {"kumaoni": "क्वीड़", "roman": "kweed", "english": "intimate group chatter among hill women", "hindi": "महिलाओं की आपसी बातचीत व गपशप", "pos": "noun", "category": "conversation"},
    {"kumaoni": "पलो", "roman": "palo", "english": "winter frost / rime ice coating mountain grasses", "hindi": "पाला / तुषार", "pos": "noun", "category": "weather"},
    {"kumaoni": "घाम", "roman": "ghaam", "english": "bright mountain sunshine / comforting winter warmth", "hindi": "धूप / सूर्यताप", "pos": "noun", "category": "weather"},
    {"kumaoni": "सिकड़", "roman": "sikad", "english": "slender flexible birch or willow rod / supple twig", "hindi": "लचीली पतली छड़ी", "pos": "noun", "category": "tools"},
    {"kumaoni": "पुड़ो", "roman": "pudo", "english": "paper or leaf packet of medicinal herbs or sweets", "hindi": "पुड़िया / छोटा पैकेट", "pos": "noun", "category": "household"},
    {"kumaoni": "कौन्", "roman": "kaun", "english": "foxtail millet / coarse high-altitude mountain grain", "hindi": "कौणी / छोटा पहाड़ी अनाज", "pos": "noun", "category": "food"},
    {"kumaoni": "कछरण", "roman": "kachharan", "english": "to tuck up garment folds / to withdraw / to concede", "hindi": "कपड़े समेटना / पीछे हटना / हार मानना", "pos": "verb", "category": "actions"},
    {"kumaoni": "खंजन", "roman": "khanchan", "english": "to undermine / inflict damage / damage irreparably", "hindi": "क्षति पहुँचाना / नुकसान करना", "pos": "verb", "category": "actions"},
    {"kumaoni": "बगंबर", "roman": "bagambar", "english": "tiger pelt / ascetic's animal hide meditation seat", "hindi": "बाघाम्बर / बाघ की खाल का आसन", "pos": "noun", "category": "culture"},
    {"kumaoni": "धेकून", "roman": "dhekoon", "english": "to intimidate / glare threateningly with wide eyes", "hindi": "आँखें तरेरना / धमकाना", "pos": "verb", "category": "actions"},
    {"kumaoni": "अलज्यून", "roman": "aljyoon", "english": "to entangle into matrimonial alliance or kinship ties", "hindi": "विवाह सूत्र में बाँधना / रिश्ते में उलझाना", "pos": "verb", "category": "culture"},
    {"kumaoni": "जागरिया", "roman": "jaagariya", "english": "master ritualist bard who chants spirit invocations (Jagar)", "hindi": "जागर का मुख्य गायक व अनुष्ठाता", "pos": "noun", "category": "culture"},
    {"kumaoni": "डंगरिया", "roman": "dangariya", "english": "spiritual medium or oracle possessed by the deity in Jagar", "hindi": "जागर में देवता का पश्वा / अवतारी माध्यम", "pos": "noun", "category": "culture"},
    {"kumaoni": "हुड़किया", "roman": "hudkiya", "english": "traditional bard and master player of the hourglass drum (Hurka)", "hindi": "हुड़का बजाने वाला लोक गायक", "pos": "noun", "category": "culture"},
    {"kumaoni": "हुड़का", "roman": "hudka", "english": "traditional two-headed hourglass hand-drum used in ballads and Jagar", "hindi": "पारंपरिक पहाड़ी वाद्य हुड़का", "pos": "noun", "category": "tools"},
    {"kumaoni": "थाई", "roman": "thaai", "english": "traditional brass or bell-metal circular dinner plate", "hindi": "कांसी या पीतल की थाली", "pos": "noun", "category": "household"}
]

with open(WORDS_FILE, 'r', encoding='utf-8') as f:
    existing_words = json.load(f)

existing_word_set = {w['kumaoni'] for w in existing_words}
added_words = 0
for w in UOU_WORDS:
    if w['kumaoni'] not in existing_word_set:
        existing_words.append(w)
        existing_word_set.add(w['kumaoni'])
        added_words += 1

with open(WORDS_FILE, 'w', encoding='utf-8') as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)
print(f"Words: Added {added_words} new words. Total now: {len(existing_words)}")

# ----------------------------------------------------------------------
# 2. NEW IDIOMS & PHRASES (UOU AECC-K-101 Unit 5)
# ----------------------------------------------------------------------
UOU_PHRASES = [
    {"kumaoni": "हात मलन", "roman": "haat malan", "english": "to wring one's hands in bitter regret", "hindi": "पछतावा करना / पश्चाताप में हाथ मलना", "category": "idioms"},
    {"kumaoni": "चुड़ा पैरन", "roman": "chuda pairan", "english": "to show cowardice / display unmanliness", "hindi": "कायरता दिखाना / चूड़ियाँ पहनना", "category": "idioms"},
    {"kumaoni": "कान भरन", "roman": "kaan bharan", "english": "to poison someone's ears with malicious gossip", "hindi": "चुगली करना / कान भरना", "category": "idioms"},
    {"kumaoni": "नाक राखन", "roman": "naak raakhan", "english": "to preserve prestige and family honour", "hindi": "मान-मर्यादा या प्रतिष्ठा बचाना", "category": "idioms"},
    {"kumaoni": "ख्वारा में चडूंन", "roman": "khwaara mein chadoon", "english": "to pamper excessively / spoil by overindulgence", "hindi": "सिर चढ़ाना / अत्यधिक लाड़-प्यार से बिगाड़ना", "category": "idioms"},
    {"kumaoni": "गांठा पाड़न", "roman": "gaantha paadan", "english": "to commit permanently to memory / knot in mind", "hindi": "गाँठ बाँधना / हमेशा याद रखना", "category": "idioms"},
    {"kumaoni": "खाप में जान भरीन", "roman": "khaap mein jaan bhareen", "english": "to drool in greed / covet with watering mouth", "hindi": "ललचाना / मुँह में पानी भर आना", "category": "idioms"},
    {"kumaoni": "टाङ कछरन", "roman": "taang kachharan", "english": "to concede defeat / throw in the towel", "hindi": "हार मानना / पराजित होकर पीछे हटना", "category": "idioms"},
    {"kumaoni": "रीस को पुलो", "roman": "rees ko pulo", "english": "bundle of fury / extremely hot-tempered person", "hindi": "अत्यधिक क्रोधी व्यक्ति", "category": "idioms"},
    {"kumaoni": "फसक उडूंन", "roman": "phasak udoon", "english": "to spread rumors / indulge in idle talk", "hindi": "अफवाह उड़ाना / गप हांकना", "category": "idioms"},
    {"kumaoni": "खाड़ खंजन", "roman": "khaad khanchan", "english": "to inflict damage / sabotage someone's work", "hindi": "क्षति पहुँचाना / काम में रोड़ा अटकाना", "category": "idioms"},
    {"kumaoni": "क्वीड़ करण", "roman": "kweed karan", "english": "women gathering together for intimate chat and gossip", "hindi": "महिलाओं की आपसी अंतरंग गपशप", "category": "idioms"},
    {"kumaoni": "खुटा पकड़न", "roman": "khuta pakadan", "english": "to plead humbly / flatter someone in desperation", "hindi": "खुशामद करना / पाँव पकड़ना", "category": "idioms"},
    {"kumaoni": "आंखा धेकून", "roman": "aankha dhekoon", "english": "to glare menacingly / intimidate with fierce eyes", "hindi": "धमकाना / आँखें तरेरना", "category": "idioms"},
    {"kumaoni": "गाड़ बगूण", "roman": "gaad bagoon", "english": "to wash away in a river / squander everything completely", "hindi": "नदी में बहा देना / सब कुछ बर्बाद करना", "category": "idioms"},
    {"kumaoni": "गोरख्याल हुण", "roman": "gorkhyaal hoon", "english": "to act tyrannical, ruthless, or oppressively cruel", "hindi": "गोरखों की भांति अत्याचारी या निर्दयी होना", "category": "idioms"},
    {"kumaoni": "बिख झाणण", "roman": "bikh jhaanan", "english": "to vent bitter venomous fury upon someone", "hindi": "विष झाड़ना / तीव्र क्रोध निकालना", "category": "idioms"},
    {"kumaoni": "पातल मुख पोछण", "roman": "paatal mukh pochhan", "english": "to wipe mouth with a leaf and pretend total innocence after wrongdoing", "hindi": "अपराध करके अनजान बन जाना", "category": "idioms"},
    {"kumaoni": "जागर लगूण", "roman": "jaagar lagoon", "english": "to create a huge uproar / invoke spirits / stir great commotion", "hindi": "बड़ी हलचल मचाना / आह्वान करना", "category": "idioms"},
    {"kumaoni": "अगासै चड़न", "roman": "agaasai chadan", "english": "to become inflated and conceited from false praise", "hindi": "झूठी प्रशंसा से आसमान पर चढ़ना", "category": "idioms"},
    {"kumaoni": "गैली बात", "roman": "gaili baat", "english": "a confidential inside secret / hidden truth", "hindi": "भेद की बात / गुप्त रहस्य", "category": "idioms"},
    {"kumaoni": "गांठ कोतरन", "roman": "gaanth kotaran", "english": "to pick pockets / secretly steal hidden savings", "hindi": "जेब काटना / गुप्त धन चुराना", "category": "idioms"},
    {"kumaoni": "पाताळै की खबर ल्यूंन", "roman": "paataalai ki khabar lyoon", "english": "to bring news from far and wide / exceptionally well-informed", "hindi": "दूर-दराज से समाचार लाना", "category": "idioms"},
    {"kumaoni": "पाणि का भौ", "roman": "paani ka bhau", "english": "dirt cheap / almost free of charge", "hindi": "पानी के मोल / बेहद सस्ता", "category": "idioms"},
    {"kumaoni": "भदौ मैना को राँगो", "roman": "bhadau maina ko raango", "english": "extremely plump and overfed (like a buffalo in monsoon)", "hindi": "अत्यधिक मोटा-ताजा व्यक्ति", "category": "idioms"}
]

with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
    existing_phrases = json.load(f)

existing_phr_set = {p['kumaoni'] for p in existing_phrases}
added_phrases = 0
for p in UOU_PHRASES:
    if p['kumaoni'] not in existing_phr_set:
        existing_phrases.append(p)
        existing_phr_set.add(p['kumaoni'])
        added_phrases += 1

with open(PHRASES_FILE, 'w', encoding='utf-8') as f:
    json.dump(existing_phrases, f, ensure_ascii=False, indent=2)
print(f"Phrases: Added {added_phrases} new phrases. Total now: {len(existing_phrases)}")

# ----------------------------------------------------------------------
# 3. NEW PROVERBS (UOU AECC-K-101 Unit 5)
# ----------------------------------------------------------------------
with open(PROVERBS_FILE, 'r', encoding='utf-8') as f:
    existing_proverbs = json.load(f)

current_prov_id = len(existing_proverbs)
UOU_PROVERBS = [
    {
        "id": current_prov_id + 1,
        "kumaoni": "मुसकि ऐ रै गाउ, बिराउक है री खेल।",
        "roman": "Musaki ai rai gaau, biraauk hai ree khel.",
        "literal_translation": "A dire crisis has befallen the mouse, while for the cat it is mere sport.",
        "figurative_meaning": "What is life and death tragedy for the helpless is casual amusement for the powerful.",
        "hindi_equivalent": "चूहे की जान पर बनी है और बिल्ली के लिए खेल हो रहा है।",
        "english_equivalent": "One man's sorrow is another man's sport.",
        "theme": "Social Irony & Power",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 2,
        "kumaoni": "जो गौं जाण नै, वीक बाट के पुछण।",
        "roman": "Jo gaun jaan nai, veek baat ke puchhan.",
        "literal_translation": "Why inquire about the road leading to a village you do not intend to visit?",
        "figurative_meaning": "Do not waste time or curiosity meddling with affairs that do not concern you.",
        "hindi_equivalent": "जिस गाँव जाना नहीं, उसका रास्ता पूछने से क्या लाभ।",
        "english_equivalent": "Do not cross bridges you never intend to walk / Mind your own business.",
        "theme": "Practical Prudence",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 3,
        "kumaoni": "भैंसक सींग भैंस कैं भारर कन हुन।",
        "roman": "Bhainsak seeng bhains kain bhaarar kan hoon.",
        "literal_translation": "A buffalo's heavy horns are never a burden to the buffalo itself.",
        "figurative_meaning": "Parents never consider their own children or family duties an oppressive burden.",
        "hindi_equivalent": "भैंस के सींग भैंस को भारी नहीं लगते (अपनी संतान कभी बोझ नहीं होती)।",
        "english_equivalent": "A mother never finds the weight of her children burdensome.",
        "theme": "Family & Kinship",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 4,
        "kumaoni": "आपण सुन ख्वट, परखनेर कै दोष दी।",
        "roman": "Aapan sun khwat, parakhner kai dosh dee.",
        "literal_translation": "When one's own gold is debased alloy, why cast blame upon the assayer?",
        "figurative_meaning": "When one's own people or actions are fundamentally deficient, do not blame the impartial judge.",
        "hindi_equivalent": "अपना सोना खोटा हो तो परखने वाले जौहरी को क्या दोष देना।",
        "english_equivalent": "Look to your own shortcomings before blaming the evaluator.",
        "theme": "Self-Accountability",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 5,
        "kumaoni": "द्याप्त देखण जागस्यर, म्याल देखण बागस्यर।",
        "roman": "Dyaapt dekhan Jaagasyar, myaal dekhan Baagasyar.",
        "literal_translation": "To see deities visit Jageshwar; to behold the grand festival visit Bageshwar.",
        "figurative_meaning": "Every sacred Himalayan center possesses its own distinctive cultural virtue and renown.",
        "hindi_equivalent": "देवता दर्शन जागेश्वर धाम में और विशाल मेला दर्शन बागेश्वर में।",
        "english_equivalent": "To each sanctuary its distinct virtue; to each sacred place its true renown.",
        "theme": "Sacred Geography & Tradition",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 6,
        "kumaoni": "जॉ कुकड़ि कन हुन, वॉ के रात कन ब्यानी?",
        "roman": "Jau kukadi kan hoon, vau ke raat kan byaani?",
        "literal_translation": "In a place where no rooster crows, does the dawn fail to break?",
        "figurative_meaning": "Nature's course and society's wheels turn inexorably; no single person is indispensable.",
        "hindi_equivalent": "जहाँ मुर्गा नहीं बोलता, क्या वहाँ सवेरा नहीं होता?",
        "english_equivalent": "The dawn does not wait for any single rooster to crow.",
        "theme": "Humility & Inevitability",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 7,
        "kumaoni": "नानतिनाक जाड़ ढुंगा में।",
        "roman": "Naanatinaak jaad dhunga mein.",
        "literal_translation": "The winter cold of little children is absorbed harmlessly into mountain rocks.",
        "figurative_meaning": "Young children are naturally resilient, active, and impervious to the mountain chill.",
        "hindi_equivalent": "बच्चों की सर्दी पत्थर में समा जाती है (बच्चे जाड़े से नहीं डरते)।",
        "english_equivalent": "Children are made of sturdy mountain grit.",
        "theme": "Childhood & Hardiness",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 8,
        "kumaoni": "अदपुरि विद्या जीवे काल।",
        "roman": "Adapoori vidya jeeve kaal.",
        "literal_translation": "Half-acquired knowledge becomes the very death of life.",
        "figurative_meaning": "Superficial understanding causes far more disaster and harm than honest ignorance.",
        "hindi_equivalent": "अधूरी विद्या जान की दुश्मन बन जाती है (नीम हकीम खतरा-ए-जान)।",
        "english_equivalent": "A little learning is a dangerous thing.",
        "theme": "Wisdom & Knowledge",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 9,
        "kumaoni": "जैक बकड़-बकड़ आस, उइले दे कौन् को गास।",
        "roman": "Jaik bakad-bakad aas, uile de kaun ko gaas.",
        "literal_translation": "From whom huge hopes were cherished, he offered merely a tiny bite of coarse millet.",
        "figurative_meaning": "Grand expectations from self-important patrons frequently result in meager disappointment.",
        "hindi_equivalent": "जिससे बड़ी-बड़ी आशाएँ थीं, उसने बहुत मामूली सहारा दिया।",
        "english_equivalent": "Great promises often yield very small fruits.",
        "theme": "Expectations & Human Nature",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    },
    {
        "id": current_prov_id + 10,
        "kumaoni": "ढको द्वार, हिटो हरिद्वार।",
        "roman": "Dhako dwaar, hito Haridwaar.",
        "literal_translation": "Shut the home's doors and set off on the pilgrimage to Haridwar.",
        "figurative_meaning": "When all worldly ties and domestic disputes become overwhelming, renounce and seek solace.",
        "hindi_equivalent": "घर का दरवाजा बंद करो और हरिद्वार की राह पकड़ो (सब छोड़ कर निकल पड़ना)।",
        "english_equivalent": "Cut your losses and seek spiritual peace.",
        "theme": "Renunciation & Peace",
        "source": "Uttarakhand Open University AECC-K-101 Unit 5"
    }
]

existing_prov_texts = {p['kumaoni'] for p in existing_proverbs}
added_proverbs = 0
for p in UOU_PROVERBS:
    if p['kumaoni'] not in existing_prov_texts:
        existing_proverbs.append(p)
        existing_prov_texts.add(p['kumaoni'])
        added_proverbs += 1

with open(PROVERBS_FILE, 'w', encoding='utf-8') as f:
    json.dump(existing_proverbs, f, ensure_ascii=False, indent=2)
print(f"Proverbs: Added {added_proverbs} new proverbs. Total now: {len(existing_proverbs)}")

# ----------------------------------------------------------------------
# 4. NEW RIDDLES (UOU AECC-K-101 Unit 5)
# ----------------------------------------------------------------------
with open(RIDDLES_FILE, 'r', encoding='utf-8') as f:
    existing_riddles = json.load(f)

current_rid_id = len(existing_riddles)
UOU_RIDDLES = [
    {
        "id": current_rid_id + 1,
        "riddle": "थाई में डबल गिण कन सक, चपकन सिकड़ टोड कन सक।",
        "roman": "Thaai mein dabal gin kan sak, chapkan sikad tod kan sak.",
        "english_translation": "Silver coins piled high in a platter cannot be counted; a slender supple rod cannot be broken.",
        "answer_kumaoni": "आकाशक तारा और साँप",
        "answer_english": "Stars in the night sky and a mountain snake",
        "answer_hindi": "आकाश के तारे व सांप",
        "hint": "Gaze upward upon starry nights, and look along terrace stone boundaries.",
        "cultural_context": "Traditional Aan recited beside the winter hearth (bhiner) across Kumaon."
    },
    {
        "id": current_rid_id + 2,
        "riddle": "सफेद घ्वड़ पाणि पीहूँ जाणौ, लाल घ्वड़ पाणि पी बेर ऊणौ।",
        "roman": "Safed ghwad paani peehoon jaanau, laal ghwad paani pee ber oonau.",
        "english_translation": "A white horse gallops down to drink water; a red horse returns having drunk.",
        "answer_kumaoni": "पूरी तलिण",
        "answer_english": "Frying wheat dough pooris in a cauldron of boiling ghee/oil",
        "answer_hindi": "कड़ाही में पूरी तलना",
        "hint": "Festive culinary preparation during mountain marriages and pujas.",
        "cultural_context": "Pahari riddle contrasting white rolled dough immersed in hot oil and emerging golden-red."
    },
    {
        "id": current_rid_id + 3,
        "riddle": "ठेकक मैं ठेकक बीचम भै गो पिरमू नेगी।",
        "roman": "Thekak main thekak beecham bhai go Pirmu Negi.",
        "english_translation": "Container balanced atop container, and Pirmu Negi sits comfortably in between.",
        "answer_kumaoni": "रिखु / गन्ना",
        "answer_english": "Sugarcane stalk with its segmented wooden nodes",
        "answer_hindi": "गन्ना (ईख की पोरियाँ)",
        "hint": "Tall sweet segmented crop harvested in Himalayan foothills.",
        "cultural_context": "Agricultural harvest riddle celebrating winter sugarcane crushing in valley flats."
    },
    {
        "id": current_rid_id + 4,
        "riddle": "आलङ गड़ा दोष, पालङ गड़ा ओस, तेरर ईजा ऊंन तक मैं नहांकथन होस।",
        "roman": "Aalang gada dosh, paalang gada os, terar eeja oon tak main nahaankathan hos.",
        "english_translation": "Frost upon this mountain ridge, dew upon the far ridge; until your mother arrives, I have no vitality.",
        "answer_kumaoni": "घाम / धूप",
        "answer_english": "Winter sunshine dispelling the morning frost",
        "answer_hindi": "पहाड़ की गुनगुनी धूप",
        "hint": "The cherished golden warmth awaited each winter morning on hill slopes.",
        "cultural_context": "High-altitude winter riddle celebrating the sun melting valley rime frost (palo)."
    },
    {
        "id": current_rid_id + 5,
        "riddle": "खुटा काटि कभिङ धरर जांछ, अफ रुख जांछ।",
        "roman": "Khuta kaati kabhing dharar jaanchh, af rukh jaanchh.",
        "english_translation": "Its feet are separated and set against the stone wall; yet it halts right there.",
        "answer_kumaoni": "पुल्या / जूता",
        "answer_english": "Traditional mountain shoes / footwear",
        "answer_hindi": "जूता / खड़ाऊँ",
        "hint": "Left outside the threshold (dehali) of a Pahari home.",
        "cultural_context": "Traditional domestic etiquette of never entering the home or kitchen wearing outdoor shoes."
    },
    {
        "id": current_rid_id + 6,
        "riddle": "काठकक कठघोड़ी लुवाकक लगाम, बै में बैठ्यो कलुवा पधान।",
        "roman": "Kaathakak kathaghodi luwaakak lagaam, bai mein baithyo Kaluwa padhaan.",
        "english_translation": "A wooden mare with iron reins; upon her back sits Kaluwa the village headman.",
        "answer_kumaoni": "हुक्का-चिलम",
        "answer_english": "Traditional wooden hookah with earthen chilam",
        "answer_hindi": "हुक्का-चिलम",
        "hint": "Enjoyed during village panchayats on the paved courtyard (khalo).",
        "cultural_context": "Symbol of village communion where elders gathered to discuss agricultural seasons."
    }
]

existing_rid_texts = {r['riddle'] for r in existing_riddles}
added_riddles = 0
for r in UOU_RIDDLES:
    if r['riddle'] not in existing_rid_texts:
        existing_riddles.append(r)
        existing_rid_texts.add(r['riddle'])
        added_riddles += 1

with open(RIDDLES_FILE, 'w', encoding='utf-8') as f:
    json.dump(existing_riddles, f, ensure_ascii=False, indent=2)
print(f"Riddles: Added {added_riddles} new riddles. Total now: {len(existing_riddles)}")

# ----------------------------------------------------------------------
# 5. MASTER BIBLIOGRAPHY INTEGRATION (Excel Sheet + Full User Corpus)
# ----------------------------------------------------------------------
xlsx_path = r'C:\Users\digit_lgfi273\Downloads\Kumaoni_Master_Bibliography_Verified_v1.xlsx'
ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def parse_sheet(z, sheet_name):
    tree = ET.fromstring(z.read(sheet_name))
    rows = []
    for r in tree.findall('.//m:row', ns):
        row_vals = []
        for c in r.findall('m:c', ns):
            t = c.attrib.get('t')
            if t == 'inlineStr':
                is_elem = c.find('m:is', ns)
                if is_elem is not None:
                    t_elem = is_elem.find('m:t', ns)
                    row_vals.append(t_elem.text if t_elem is not None else '')
                else:
                    row_vals.append('')
            else:
                v_elem = c.find('m:v', ns)
                row_vals.append(v_elem.text if v_elem is not None else '')
        if row_vals:
            rows.append(row_vals)
    return rows

with zipfile.ZipFile(xlsx_path, 'r') as z:
    raw_rows = parse_sheet(z, 'xl/worksheets/sheet1.xml')

header = [h.strip() for h in raw_rows[0]]
bib_entries = []
seen_titles = set()

for r in raw_rows[1:]:
    while len(r) < len(header):
        r.append('')
    d = {header[i]: r[i].strip() for i in range(len(header))}
    title = d.get('Title', '')
    if not title:
        continue
    
    genre = d.get('Genre', '')
    lang_status = d.get('Language / Status', '')
    
    # Categorize properly
    if any(k in title for k in ['ब्याकरण', 'व्याकरण', 'शब्द संपदा', 'प्यौलिपिटार', 'क्रियापदों की पड़ताल', 'शब्दकोश']) or 'शब्दकोश' in genre:
        cat = "grammar_and_linguistics"
        cat_lbl = "Kumaoni Grammar, Lexicography & Linguistics"
    elif any(k in title for k in ['उद्भव विकास', 'भाषा और उसका साहित्य', 'का लोक साहित्य', 'लोक-साहित्य की पृष्ठभूमि', 'लोक संस्कृति के विविध आयाम', 'जन-जीवन', 'अध्ययन']) or any(k in genre for k in ['शोध', 'लोकसाहित्य/शोध', 'लोकगीत/शोध', 'भाषा/साहित्य']) or 'शोध' in lang_status:
        cat = "works_about_kumaoni"
        cat_lbl = "Works About Kumaoni (Criticism, History & Folk Studies)"
    else:
        cat = "works_in_kumaoni"
        cat_lbl = "Works Written In Kumaoni (Literature & Texts)"

    entry = {
        "id": int(d.get('No.', len(bib_entries) + 1)),
        "title": title,
        "author": d.get('Author / Editor', ''),
        "year": d.get('Year', ''),
        "genre": genre,
        "category": cat,
        "category_label": cat_lbl,
        "language_status": lang_status,
        "evidence": d.get('Evidence', ''),
        "publisher": d.get('Publisher', ''),
        "pages": d.get('Pages', ''),
        "isbn": d.get('ISBN', ''),
        "source_url": d.get('Source URL / Search Key', ''),
        "confidence": d.get('Confidence', '')
    }
    bib_entries.append(entry)
    seen_titles.add(title.strip())

# Now append any missing titles from the user's verified working bibliography!
ADDITIONAL_BIB_CORPUS = [
    # 1. Classical / Early Kumaoni
    {"title": "गंगाशतक", "author": "गुमानी पंत", "genre": "काव्य/धार्मिक", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Classical Kumaoni literature; Kumauni.in digital archives", "confidence": "A — directly catalogued/official"},
    {"title": "गुमानी वाणी", "author": "गुमानी पंत", "genre": "काव्य-संग्रह", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Classical Kumaoni literature; Kumauni.in digital archives", "confidence": "A — directly catalogued/official"},
    {"title": "कुमाऊँ के सम्राट, भाग 1", "author": "चिंतामणि पालीवाल", "genre": "ऐतिहासिक/काव्य", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Kumauni.in digital collection", "confidence": "A — directly catalogued/official"},
    {"title": "कुमाऊँ के सम्राट, भाग 4", "author": "चिंतामणि पालीवाल", "genre": "ऐतिहासिक/काव्य", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Kumauni.in digital collection", "confidence": "A — directly catalogued/official"},
    {"title": "शैलानी — दिल्ली की सैल, पहाड़ की सैल", "author": "चिंतामणि पालीवाल", "genre": "काव्य/यात्रा-संस्मरण", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Kumauni.in digital collection", "confidence": "A — directly catalogued/official"},
    {"title": "मन्खौं पड़्यौव मैं", "author": "हीरा सिंह राणा", "genre": "काव्य-संग्रह", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "pages": "80", "evidence": "Kumauni.in digital collection / CamScanner PDF", "confidence": "A — directly catalogued/official"},
    {"title": "उघड़ी आँखोंक स्वींण", "author": "नवीन जोशी", "genre": "काव्य-संग्रह", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Kumaoni modern poetry collection", "confidence": "A — directly catalogued/official"},
    {"title": "स्यौ सार", "author": "गौरी दत्त पांडे 'गौर्दा'", "genre": "काव्य-संग्रह", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Kumaoni patriotic and social poetry", "confidence": "A — directly catalogued/official"},
    {"title": "गौर्दा वाणी", "author": "गौरी दत्त पांडे 'गौर्दा'", "genre": "काव्य-संग्रह", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Kumaoni patriotic and social poetry", "confidence": "A — directly catalogued/official"},

    # 2. Puran Chandra Kandpal works
    {"title": "कुमाउँनम में हामनखी", "author": "पूरन चन्द्र कांडपाल", "genre": "गद्य/कविता", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Puran Chandra Kandpal Kumaoni corpus; Dr Pawanesh bibliography", "confidence": "A — directly catalogued/official"},
    {"title": "उज्याव", "author": "पूरन चन्द्र कांडपाल", "genre": "ज्ञान/सामान्य ज्ञान", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Kumaoni general knowledge treatise; Mera Pahad Forum", "confidence": "A — directly catalogued/official"},
    {"title": "हमरि भाषा हमरि पछ्याण", "author": "पूरन चन्द्र कांडपाल", "genre": "भाषा/संस्कृति", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Puran Chandra Kandpal Kumaoni corpus", "confidence": "A — directly catalogued/official"},

    # 3. Sher Singh Bisht 'Anpadh' works
    {"title": "दीदि-बैंणि", "author": "शेर सिंह बिष्ट 'अनपढ़'", "genre": "काव्य/व्यंग्य", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "evidence": "Kumauni literary source 2019/12; modern satire", "confidence": "A — directly catalogued/official"},
    {"title": "कुमाऊनी", "author": "शेर सिंह बिष्ट 'अनपढ़'", "genre": "काव्य/साहित्य", "category": "works_in_kumaoni", "category_label": "Works Written In Kumaoni (Literature & Texts)", "pages": "256", "evidence": "Sahitya Akademi catalogue AR-2023-24", "confidence": "A — directly catalogued/official"},

    # 4. Landmark Story Collections & Children's Literature
    {
        "title": "कौ सुआ काथ कौथ",
        "author": "विविध लेखक (संपादक मंडल)",
        "genre": "कहानी-संग्रह (100 कहानियाँ)",
        "category": "works_in_kumaoni",
        "category_label": "Works Written In Kumaoni (Literature & Texts)",
        "pages": "456",
        "evidence": "Landmark 456-page compilation spanning 80 years with 30+ Kumaoni authors; Jagran / Amazon",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाऊँनी बालसाहित्य पाठमाला (धगुलि, हंसुली, छुबकि, पैजनि, झुमकि)",
        "author": "उत्तराखंड विद्यालयी शिक्षा परिषद",
        "genre": "बालसाहित्य / पाठ्यपुस्तक",
        "category": "works_in_kumaoni",
        "category_label": "Works Written In Kumaoni (Literature & Texts)",
        "evidence": "Primary school Kumaoni curriculum (Class 1 to 5) listed in Dainik Jagran",
        "confidence": "A — directly catalogued/official"
    },

    # 5. Grammar & Linguistics
    {
        "title": "कुमाउनी भाषाक ब्याकरण",
        "author": "पूरन चन्द्र कांडपाल",
        "genre": "व्याकरण",
        "category": "grammar_and_linguistics",
        "category_label": "Kumaoni Grammar, Lexicography & Linguistics",
        "evidence": "Authoritative grammatical treatise in Kumaoni",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाउनी क्रियापदों की पड़ताल",
        "author": "सुरेश पंत",
        "genre": "भाषाविज्ञान/व्याकरण",
        "category": "grammar_and_linguistics",
        "category_label": "Kumaoni Grammar, Lexicography & Linguistics",
        "evidence": "Linguistic analysis of Kumaoni verbal system",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाउनी शब्द संपदा",
        "author": "डॉ. नागेश कुमार शाह",
        "genre": "शब्दकोश (कुमाउनी-हिन्दी-अंग्रेजी)",
        "category": "grammar_and_linguistics",
        "category_label": "Kumaoni Grammar, Lexicography & Linguistics",
        "evidence": "Trilingual Kumaoni-Hindi-English lexicon; Kumauni Bhasha research",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाऊँनी की अस्कोटी बोली का व्याकरण",
        "author": "डॉ. जगत सिंह बिष्ट",
        "genre": "व्याकरण/बोली-अध्ययन",
        "category": "grammar_and_linguistics",
        "category_label": "Kumaoni Grammar, Lexicography & Linguistics",
        "evidence": "Dialectal grammar study of Askoti Kumaoni",
        "confidence": "A — directly catalogued/official"
    },

    # 6. Books ABOUT Kumaoni
    {
        "title": "कुमाउनी भाषा और उसका साहित्य",
        "author": "डॉ. त्रिलोचन पाण्डे",
        "genre": "साहित्येतिहास/शोध",
        "category": "works_about_kumaoni",
        "category_label": "Works About Kumaoni (Criticism, History & Folk Studies)",
        "publisher": "श्री अल्मोड़ा बुक डिपो, अल्मोड़ा",
        "evidence": "UOU AECC-K-101 Reference & Internet Archive (nucr-kumaoni-bhasha-aur-sahitya)",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाउनी भाषा और साहित्य का उद्भव विकास",
        "author": "प्रो. शेर सिंह बिष्ट",
        "genre": "साहित्येतिहास/शोध",
        "category": "works_about_kumaoni",
        "category_label": "Works About Kumaoni (Criticism, History & Folk Studies)",
        "publisher": "अंकित प्रकाशन, हल्द्वानी",
        "evidence": "UOU AECC-K-101 Reference Syllabus",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाउनी लोक साहित्य एवं कुमाउनी साहित्य",
        "author": "देवसिंह पोखरिया",
        "genre": "साहित्येतिहास/शोध",
        "category": "works_about_kumaoni",
        "category_label": "Works About Kumaoni (Criticism, History & Folk Studies)",
        "publisher": "श्री अल्मोड़ा बुक डिपो, अल्मोड़ा",
        "evidence": "UOU AECC-K-101 Reference Syllabus",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाउनी का लोक साहित्य",
        "author": "डॉ. त्रिलोचन पाण्डे",
        "genre": "लोकसाहित्य/शोध",
        "category": "works_about_kumaoni",
        "category_label": "Works About Kumaoni (Criticism, History & Folk Studies)",
        "evidence": "UOU AECC-K-101 Reference Syllabus",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाउनी लोक-साहित्य की पृष्ठभूमि",
        "author": "डॉ. त्रिलोचन पाण्डे",
        "genre": "लोकसाहित्य/शोध",
        "category": "works_about_kumaoni",
        "category_label": "Works About Kumaoni (Criticism, History & Folk Studies)",
        "evidence": "UOU AECC-K-101 Reference Syllabus",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "कुमाऊँनी लोक संस्कृति के विविध आयाम",
        "author": "अनिल कार्की",
        "genre": "लोकसंस्कृति/शोध",
        "category": "works_about_kumaoni",
        "category_label": "Works About Kumaoni (Criticism, History & Folk Studies)",
        "publisher": "समय साक्ष्य प्रकाशन, देहरादून",
        "evidence": "UOU AECC-K-101 Reference Syllabus",
        "confidence": "A — directly catalogued/official"
    },
    {
        "title": "उत्तराखण्ड का लोक साहित्य और जन-जीवन",
        "author": "डॉ. सरला चंदोला",
        "genre": "लोकसाहित्य/शोध",
        "category": "works_about_kumaoni",
        "category_label": "Works About Kumaoni (Criticism, History & Folk Studies)",
        "publisher": "तक्षशीला प्रकाशन, नई दिल्ली",
        "evidence": "UOU AECC-K-101 Reference Syllabus",
        "confidence": "A — directly catalogued/official"
    }
]

for item in ADDITIONAL_BIB_CORPUS:
    # Check if title already present
    t = item['title'].strip()
    if not any(t in existing_t or existing_t in t for existing_t in seen_titles):
        new_entry = {
            "id": len(bib_entries) + 1,
            "title": t,
            "author": item.get('author', ''),
            "year": item.get('year', ''),
            "genre": item.get('genre', ''),
            "category": item.get('category', 'works_in_kumaoni'),
            "category_label": item.get('category_label', 'Works Written In Kumaoni (Literature & Texts)'),
            "language_status": item.get('language_status', 'कुमाऊँनी'),
            "evidence": item.get('evidence', ''),
            "publisher": item.get('publisher', ''),
            "pages": item.get('pages', ''),
            "isbn": item.get('isbn', ''),
            "source_url": item.get('source_url', ''),
            "confidence": item.get('confidence', 'A — directly catalogued/official')
        }
        bib_entries.append(new_entry)
        seen_titles.add(t)

with open(BIB_FILE, 'w', encoding='utf-8') as f:
    json.dump(bib_entries, f, ensure_ascii=False, indent=2)

print(f"Bibliography: Total catalogued works now: {len(bib_entries)}")
from collections import Counter
cat_counts = Counter(e['category'] for e in bib_entries)
for cat, cnt in cat_counts.items():
    print(f"  {cat}: {cnt}")
