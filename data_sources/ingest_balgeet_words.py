"""
Ingest authentic terms from Hem Pant's Ghughuti Basuti (Kumaoni Balgeet & Nursery Rhymes).
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_FILE = os.path.join(ROOT_DIR, 'kumaoni', 'lexicon', 'data', 'words.json')

sys.path.insert(0, ROOT_DIR)
import kumaoni

BALGEET_WORDS = [
    {"kumaoni": "पालड़ी", "english": "mountain slope meadow where green grass fodder is cut", "hindi": "घास काटने का ढालू मैदान / चारागाह", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "तौलि", "english": "traditional small bronze bowl or plate for serving food to children", "hindi": "काँसे या पीतल की छोटी तसली / कटोरा", "pos": "noun", "category": "tools"},
    {"kumaoni": "गुदड़ी", "english": "quilted patchwork cotton mattress for babies", "hindi": "शिशु का गुदड़ा / बिछौना", "pos": "noun", "category": "home"},
    {"kumaoni": "हल्लोरी", "english": "rhythmic hill lullaby sung while swaying the baby's cradle", "hindi": "पालना झुलाने की पहाड़ी लोरी", "pos": "noun", "category": "culture"},
    {"kumaoni": "जाँठी", "english": "sturdy mountain walking staff adorned with bells", "hindi": "घुंघरू वाली पहाड़ी लाठी / छड़ी", "pos": "noun", "category": "tools"},
    {"kumaoni": "गिचलू", "english": "chubby, endearing little face of a baby", "hindi": "प्यारा गोल-मटोल मुखड़ा / गाल", "pos": "noun", "category": "people"},
    {"kumaoni": "बिरळी", "english": "playful hill domestic cat", "hindi": "बिल्ली / मार्जारी", "pos": "noun", "category": "animals"},
    {"kumaoni": "खुट्टी", "english": "foot / leg of a child or person", "hindi": "पैर / पाँव / टांग", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "डाला", "english": "bough or branch of a high Himalayan oak or pine tree", "hindi": "पेड़ की डाल / टहनी", "pos": "noun", "category": "nature"},
    {"kumaoni": "भव्वा", "english": "Himalayan black bear mentioned in affectionate cautionary bedtime tales", "hindi": "भालू / हौवा (बच्चों को सुलाने की पुकार)", "pos": "noun", "category": "animals"},
    {"kumaoni": "पिन्ना", "english": "crushed mustard-seed or sesame oilcake pounded in stone mortars", "hindi": "खली / पिन्ना (तिल या सरसों का अवशेष)", "pos": "noun", "category": "agriculture"},
    {"kumaoni": "आमा", "english": "paternal grandmother / elder matriarch of the household", "hindi": "दादी / आमा", "pos": "noun", "category": "kinship"},
    {"kumaoni": "गिच्चि", "english": "mouth or tiny chin of an infant", "hindi": "मुँह / नन्ही ठुड्डी", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "चुप्पा", "english": "sweet affectionate kiss given to a child", "hindi": "प्यार का चुंबन / पप्पी", "pos": "noun", "category": "actions"},
    {"kumaoni": "थुपलु", "english": "plump, cuddly little child wrapped warmly", "hindi": "गुदगुदा, प्यारा नन्हा बालक", "pos": "noun", "category": "people"},
    {"kumaoni": "चुंचलू", "english": "sprightly, energetic little toddler", "hindi": "चंचल, फुर्तीला नन्हा बालक", "pos": "noun", "category": "people"}
]

with open(WORDS_FILE, 'r', encoding='utf-8') as f:
    words = json.load(f)

existing_map = {w['kumaoni']: w for w in words}
initial_count = len(words)
added_count = 0

for item in BALGEET_WORDS:
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

print(f"Balgeet Ingestion Complete!")
print(f"Initial words: {initial_count}")
print(f"Added words:   {added_count}")
print(f"Total Base Dictionary Lemmas: {len(words)}")
