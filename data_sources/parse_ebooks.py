import urllib.request, ssl, re, sys, html
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()
url = 'https://www.kumauni.in/p/e-books-relating-to-kumauni-language.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
    raw_html = resp.read().decode('utf-8', errors='ignore')

# Unescape html entities
unescaped = html.unescape(raw_html)

# Find all links
matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', unescaped, re.DOTALL)
print(f'Total links on e-books page: {len(matches)}')
for href, text in matches:
    clean_text = re.sub(r'<[^>]+>', ' ', text).strip()
    clean_text = ' '.join(clean_text.split())
    if any(k in href.lower() for k in ['drive.google', 'archive.org', 'pdf', 'docs.google']) or len(clean_text) > 5:
        print(f'{clean_text} --> {href}')
