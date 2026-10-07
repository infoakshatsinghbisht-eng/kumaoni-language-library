"""
Ingest final curated heritage lemmas from Pt. Ganga Datt Upreti (1894),
traditional weaving, woolens, crafts, and mountain proverbs.
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_FILE = os.path.join(ROOT_DIR, 'kumaoni', 'lexicon', 'data', 'words.json')

sys.path.insert(0, ROOT_DIR)
import kumaoni

UPRETI_HERITAGE_WORDS = [
    # --- WEAVING, TEXTILES & CRAFTS OF MUNSYARI & JOHAR ---
    {"kumaoni": "थुलमा", "english": "thick, hand-woven brushed woolen blanket of Johar and Munsyari", "hindi": "थुलमा (हाथ से बुना रोएंदार ऊनी कंबल)", "pos": "noun", "category": "clothing"},
    {"kumaoni": "चुटका", "english": "heavy coarse-wool fleece rug used as winter mattress in high valleys", "hindi": "चुटका (भारी ऊनी नमदा / कालीन)", "pos": "noun", "category": "home"},
    {"kumaoni": "दन", "english": "intricately hand-knotted pile wool carpet featuring dragon and lotus motifs", "hindi": "दन (मुनस्यारी का हाथ से बुना ऊनी कालीन)", "pos": "noun", "category": "home"},
    {"kumaoni": "पश्मीना", "english": "luxurious, gossamer-fine cashmere wool combed from high-altitude Himalayan goats", "hindi": "पश्मीना ऊन", "pos": "noun", "category": "clothing"},
    {"kumaoni": "पट्टू", "english": "dense handloom woolen tweed fabric tailored into coats and capes", "hindi": "पट्टू (पहाड़ी मोटा ऊनी कपड़ा)", "pos": "noun", "category": "clothing"},
    {"kumaoni": "कमली", "english": "traditional dark sheep-wool blanket draped over shoulders", "hindi": "काली कमली / ऊनी चादर", "pos": "noun", "category": "clothing"},

    # --- TOOLS & IMPLEMENTS ---
    {"kumaoni": "दाँतुली", "english": "serrated curved hand-sickle for cutting grass and harvesting grain", "hindi": "दाँतीदार छोटी दरांती", "pos": "noun", "category": "tools"},
    {"kumaoni": "कुदालि", "english": "sturdy narrow mattock for weeding stony mountain terraces", "hindi": "कुदाल / कुदालि", "pos": "noun", "category": "tools"},
    {"kumaoni": "गैंत", "english": "heavy two-pointed pickaxe for excavating mountain rock and boulders", "hindi": "गैंती / पाषाण तोड़ने का औजार", "pos": "noun", "category": "tools"},

    # --- ANIMALS & FAUNA (Upreti 1894) ---
    {"kumaoni": "बाछी", "english": "young female heifer calf", "hindi": "बछिया / मादा गोवत्स", "pos": "noun", "category": "animals"},
    {"kumaoni": "बाछो", "english": "young male bull calf", "hindi": "बछड़ा / नर गोवत्स", "pos": "noun", "category": "animals"},
    {"kumaoni": "बानर", "english": "playful rhesus macaque monkey of hill orchards", "hindi": "बंदर / वानर", "pos": "noun", "category": "animals"},
    {"kumaoni": "स्याल", "english": "wily mountain golden jackal howling across ravines at dusk", "hindi": "सियार / गीदड़", "pos": "noun", "category": "animals"},
    {"kumaoni": "कस्तूरा", "english": "sacred alpine musk deer (*Moschus leucogaster*) - state animal", "hindi": "कस्तूरी मृग", "pos": "noun", "category": "animals"},
    {"kumaoni": "डाँफी", "english": "vernacular name for iridescent Himalayan monal pheasant", "hindi": "डाँफे / मोनाल पक्षी", "pos": "noun", "category": "animals"},
    {"kumaoni": "म्वार", "english": "peacock displaying iridescent plumage", "hindi": "मोर / मयूर", "pos": "noun", "category": "animals"},

    # --- CROPS, GRAINS & FOOD ---
    {"kumaoni": "ग्यूँ", "english": "golden wheat grain harvested in Baisakh", "hindi": "गेहूँ का अनाज", "pos": "noun", "category": "food"},
    {"kumaoni": "जौं", "english": "sacred barley grain sprouted for Harela blessings", "hindi": "जौ", "pos": "noun", "category": "food"},
    {"kumaoni": "घ्यू-खिचड़ी", "english": "festive preparation of rice and lentils drowned in pure cow ghee for Uttarayani", "hindi": "घी-खिचड़ी (उत्तरायणी का पारंपरिक भोजन)", "pos": "noun", "category": "food"},

    # --- SOCIAL INSTITUTIONS & VILLAGE LIFE ---
    {"kumaoni": "रैबार", "english": "verbal message, oral greeting, or news brought from afar", "hindi": "संदेश / समाचार / कुशल-क्षेम", "pos": "noun", "category": "society"},
    {"kumaoni": "रैबारी", "english": "trusted traveler or village messenger carrying news across valleys", "hindi": "संदेशवाहक / डाकिया", "pos": "noun", "category": "people"},
    {"kumaoni": "चौपाल", "english": "shaded flagstone platform where village elders gather to confer", "hindi": "चौपाल / ग्राम सभा स्थल", "pos": "noun", "category": "society"},
    {"kumaoni": "पंचैत", "english": "council of five village elders dispensing customary arbitration", "hindi": "पंचायत / ग्राम सभा", "pos": "noun", "category": "society"},
    {"kumaoni": "बरात", "english": "joyous wedding procession walking across hills with flags and trumpets", "hindi": "बारात / विवाह यात्रा", "pos": "noun", "category": "society"},
    {"kumaoni": "बाजा-गाजा", "english": "traditional folk musical ensemble of Dhol, Damau, and Ransingha", "hindi": "गाजे-बाजे / पारंपरिक वाद्यवृंद", "pos": "noun", "category": "culture"},

    # --- SPIRITUAL & HERMIT LIFE ---
    {"kumaoni": "धूणी", "english": "perpetual sacred smoldering fire tended by mountain ascetics and yogis", "hindi": "साधु की पवित्र धूनी / अलाव", "pos": "noun", "category": "culture"},
    {"kumaoni": "भभूत", "english": "sacred sanctified ash applied to forehead for divine protection", "hindi": "भभूत / भस्म / विभूति", "pos": "noun", "category": "culture"},
    {"kumaoni": "चिमटा", "english": "fire-tongs carried by Nath yogis and Jagar shamans", "hindi": "लोहे का चिमटा", "pos": "noun", "category": "tools"},
    {"kumaoni": "कमंडल", "english": "carved brass or wooden water vessel of wandering mendicants", "hindi": "कमंडल", "pos": "noun", "category": "tools"},
    {"kumaoni": "कुण्डल", "english": "large round bronze or gold earrings worn by Gorakhnath yogis", "hindi": "कुंडल (कान का आभूषण)", "pos": "noun", "category": "clothing"},
    {"kumaoni": "कंठी", "english": "rosary necklace of carved sacred basil or Rudraksha beads", "hindi": "कंठी माला", "pos": "noun", "category": "clothing"},
    {"kumaoni": "पीतांबर", "english": "sacred yellow silk vestment draped during religious festivities", "hindi": "पीतांबर (पीला रेशमी वस्त्र)", "pos": "noun", "category": "clothing"},

    # --- EMOTIONS, MORALS & INTERPERSONAL DYNAMICS ---
    {"kumaoni": "मखौल", "english": "good-natured teasing / playful banter among friends", "hindi": "हँसी-मजाक / मखौल", "pos": "noun", "category": "society"},
    {"kumaoni": "ठिठोली", "english": "lighthearted humorous jesting at fairs and festivals", "hindi": "दिल्लगी / ठिठोली", "pos": "noun", "category": "society"},
    {"kumaoni": "अणकौल", "english": "rare, extraordinary, and unexpected happening", "hindi": "अनोखा / अप्रत्याशित", "pos": "adjective", "category": "general"},
    {"kumaoni": "साँच", "english": "unvarnished truth / absolute veracity", "hindi": "सत्य / सच", "pos": "noun", "category": "society"},
    {"kumaoni": "झूठ", "english": "untruth / deception / fabrication", "hindi": "असत्य / झूठ", "pos": "noun", "category": "society"},
    {"kumaoni": "धरम", "english": "righteous duty / cosmic moral law / virtue", "hindi": "धर्म / कर्तव्य / पुण्य", "pos": "noun", "category": "society"},
    {"kumaoni": "करम", "english": "actions, deeds, and moral karma shaping life's path", "hindi": "कर्म / भाग्य / करनी", "pos": "noun", "category": "society"},
    {"kumaoni": "ल्वाठ", "english": "simple-hearted, guileless, and unsuspecting villager", "hindi": "सीधा-सादा, भोला-भाला व्यक्ति", "pos": "noun", "category": "people"},
    {"kumaoni": "च्याव", "english": "restless, eager excitement / enthusiastic anticipation", "hindi": "उमंग / उत्साह / चाव", "pos": "noun", "category": "emotions"},
    {"kumaoni": "धीरज", "english": "unwavering patience, forbearance, and quiet fortitude", "hindi": "धैर्य / सब्र / धीरज", "pos": "noun", "category": "emotions"},
    {"kumaoni": "हौंस", "english": "earnest aspiration / deep-seated heart's desire", "hindi": "अभिलाषा / तमन्ना / उमंग", "pos": "noun", "category": "emotions"},
    {"kumaoni": "परतीत", "english": "deep abiding faith / trustworthy conviction", "hindi": "विश्वास / भरोसा / प्रतीति", "pos": "noun", "category": "emotions"},
    {"kumaoni": "हियाव", "english": "inner pluck / daring courage to confront peril", "hindi": "हियाव / साहस / हिम्मत", "pos": "noun", "category": "emotions"},
    {"kumaoni": "चित्त", "english": "inner soul consciousness / tender mind", "hindi": "चित्त / अंतःकरण / मन", "pos": "noun", "category": "emotions"},
    {"kumaoni": "सुबुद्ध", "english": "intelligent, prudent, and thoughtful character", "hindi": "सुबुद्धि / समझदार", "pos": "adjective", "category": "people"},
    {"kumaoni": "कुबुद्ध", "english": "foolish, misguided, or perverse disposition", "hindi": "कुबुद्धि / मूर्ख", "pos": "adjective", "category": "people"},
    {"kumaoni": "सुखिया", "english": "contented, happy, and prosperous person", "hindi": "सुखी / प्रसन्नचित्त", "pos": "adjective", "category": "people"},
    {"kumaoni": "दुखिया", "english": "afflicted, distressed, or grieving person", "hindi": "दुखी / पीड़ित", "pos": "adjective", "category": "people"},
    {"kumaoni": "सतवंती", "english": "virtuous, faithful, and morally upright woman", "hindi": "सती / पतिव्रता व गुणवती स्त्री", "pos": "noun", "category": "people"},
    {"kumaoni": "दानपुन", "english": "charity, benevolent giving, and spiritual merit", "hindi": "दान-पुण्य / परोपकार", "pos": "noun", "category": "society"},
    {"kumaoni": "नेह", "english": "tender affection, warm love, and gentle attachment", "hindi": "स्नेह / प्रीति / प्यार", "pos": "noun", "category": "emotions"},
    {"kumaoni": "आशीस", "english": "benediction / elder's auspicious blessing ('Ji raya, jagi raya')", "hindi": "आशीर्वाद / आशीष", "pos": "noun", "category": "culture"},
    {"kumaoni": "जै-जयकार", "english": "triumphant chorus praising deities or celebrating victory", "hindi": "जय-जयकार / विजयघोष", "pos": "noun", "category": "culture"}
]

with open(WORDS_FILE, 'r', encoding='utf-8') as f:
    words = json.load(f)

existing_map = {w['kumaoni']: w for w in words}
initial_count = len(words)
added_count = 0

for item in UPRETI_HERITAGE_WORDS:
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

print(f"Heritage Ingestion Complete!")
print(f"Initial: {initial_count} words")
print(f"Added:   {added_count} words")
print(f"Total Base Dictionary Lemmas: {len(words)}")
