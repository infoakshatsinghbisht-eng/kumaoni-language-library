"""
Parse and process the Master Bibliography Excel file.
Outputs structured JSON and stats.
"""
import zipfile
import xml.etree.ElementTree as ET
import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')

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
    rows = parse_sheet(z, 'xl/worksheets/sheet1.xml')

header = [h.strip() for h in rows[0]]
print("Header:", header)

books = []
for r in rows[1:]:
    while len(r) < len(header):
        r.append('')
    d = {header[i]: r[i].strip() for i in range(len(header))}
    books.append(d)

print(f"Total entries in Sheet 1: {len(books)}")

# Categorize entries
# 1. works_in_kumaoni: Books written IN Kumaoni
# 2. grammar_and_linguistics: Grammar, dictionaries, linguistic analysis
# 3. works_about_kumaoni: Literary criticism, history, folk studies about Kumaoni

categorized = []
for b in books:
    title = b.get('Title', '')
    author = b.get('Author / Editor', '')
    genre = b.get('Genre', '')
    lang_status = b.get('Language / Status', '')
    
    # Check category
    if any(k in title for k in ['ब्याकरण', 'व्याकरण', 'शब्द संपदा', 'प्यौलिपिटार', 'क्रियापदों की पड़ताल', 'शब्दकोश']) or 'शब्दकोश' in genre:
        category = "grammar_and_linguistics"
        category_label = "Kumaoni Grammar, Lexicography & Linguistics"
    elif any(k in title for k in ['उद्भव विकास', 'भाषा और उसका साहित्य', 'का लोक साहित्य', 'लोक-साहित्य की पृष्ठभूमि', 'लोक संस्कृति के विविध आयाम', 'जन-जीवन', 'अध्ययन']) or any(k in genre for k in ['शोध', 'लोकसाहित्य/शोध', 'लोकगीत/शोध', 'भाषा/साहित्य']) or 'शोध' in lang_status:
        category = "works_about_kumaoni"
        category_label = "Works About Kumaoni (Criticism, History & Folk Studies)"
    else:
        category = "works_in_kumaoni"
        category_label = "Works Written In Kumaoni (Literature & Texts)"

    entry = {
        "id": int(b.get('No.', len(categorized) + 1)),
        "title": title,
        "author": author,
        "year": b.get('Year', ''),
        "genre": genre,
        "category": category,
        "category_label": category_label,
        "language_status": lang_status,
        "evidence": b.get('Evidence', ''),
        "publisher": b.get('Publisher', ''),
        "pages": b.get('Pages', ''),
        "isbn": b.get('ISBN', ''),
        "source_url": b.get('Source URL / Search Key', ''),
        "confidence": b.get('Confidence', '')
    }
    categorized.append(entry)

out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'kumaoni', 'culture', 'data')
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, 'bibliography.json')

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(categorized, f, ensure_ascii=False, indent=2)

print(f"Saved {len(categorized)} entries to {out_file}")

# Stats
from collections import Counter
cat_counts = Counter(e['category'] for e in categorized)
for cat, cnt in cat_counts.items():
    print(f"  {cat}: {cnt}")
