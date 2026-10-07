"""
Parse and curate vocabulary from Dr. Trilochan Pandey (1977) Appendix C and UOU AECC-K-101.
"""
import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_TEXT_PATH = os.path.join(ROOT_DIR, 'data_sources', 'raw_texts', 'pandey_kumaoni_bhasha_1977.txt')
WORDS_PATH = os.path.join(ROOT_DIR, 'kumaoni', 'lexicon', 'data', 'words.json')

with open(RAW_TEXT_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('३६० कुमाउंनी भाषा और उसका साहित्य')
pos_end = text.find('(घ)', pos_start)
subtext = text[pos_start:pos_end]

cat_map = [
    ('पहाड', 'nature'),
    ('नदी नाले', 'nature'),
    ('फल', 'food'),
    ('फूल', 'nature'),
    ('पशु', 'animals'),
    ('पक्षी', 'animals'),
    ('जीव', 'animals'),
    ('कीट', 'animals'),
    ('वृक्ष', 'nature'),
    ('घास', 'nature'),
    ('झाडी', 'nature'),
    ('अनाज', 'food'),
    ('भूमि', 'agriculture'),
    ('उपकरण', 'tools'),
    ('माप', 'tools'),
    ('गणना', 'number'),
    ('घर', 'home'),
    ('परिवार', 'kinship'),
    ('भोज्य', 'food'),
    ('बर्तन', 'tools'),
    ('अंग', 'anatomy'),
    ('विकार', 'health'),
    ('वस्त्र', 'clothing'),
    ('आभूषण', 'clothing'),
    ('अन्धविश्वास', 'culture'),
    ('रीति', 'culture'),
    ('पर्व', 'culture'),
    ('पूजा', 'culture'),
    ('वाद्य', 'culture'),
    ('भाव', 'emotions'),
    ('अनुकरण', 'onomatopoeia'),
    ('सामासिक', 'general'),
    ('अन्य', 'general')
]

current_cat = 'nature'
extracted = []

for line in subtext.splitlines():
    l_str = line.strip()
    if not l_str:
        continue
    for kw, cat in cat_map:
        if kw in l_str and any(h in l_str for h in ['सम्बन्धी', 'संबंधी', 'के नाम', 'बोली']):
            current_cat = cat
            break
    for sep in ['=', '==', '—', '–']:
        if sep in l_str:
            parts = l_str.split(sep, 1)
            left = parts[0].strip()
            right = parts[1].strip()
            left_clean = re.sub(r'[\(\[（].*?[\)\]）]', '', left).strip()
            left_clean = re.sub(r'[•\*\.\:\;\"\'\’\‘]', '', left_clean).strip()
            if re.search(r'[\u0900-\u097F]', left_clean) and re.search(r'[\u0900-\u097F]', right):
                words = [w.strip() for w in re.split(r'[,/]', left_clean) if len(w.strip()) >= 2]
                for w in words:
                    w_clean = re.sub(r'[\s_]+', ' ', w).strip()
                    if 2 <= len(w_clean) <= 25 and not any(ch in w_clean for ch in '0123456789०१२३४५६७८९'):
                        extracted.append((w_clean, right, current_cat))
            break

print(f"Extracted {len(extracted)} candidate word entries from Pandey Appendix C.")
with open(os.path.join(ROOT_DIR, 'data_sources', 'pandey_candidates.json'), 'w', encoding='utf-8') as f:
    json.dump([{"kumaoni": w, "hindi": r, "category": c} for w, r, c in extracted], f, ensure_ascii=False, indent=2)
