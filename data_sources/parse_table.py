import urllib.request, ssl, re, sys
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()
url = 'https://www.kumauni.in/p/blog-page_87.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

for m in re.finditer(r'https://drive\.google\.com/file/d/([a-zA-Z0-9_-]+)/view', html):
    link = m.group(0)
    file_id = m.group(1)
    start = max(0, m.start() - 300)
    end = min(len(html), m.end() + 200)
    snippet = html[start:end]
    clean = re.sub(r'<[^>]+>', ' | ', snippet)
    clean = ' '.join(clean.split())
    print(f'FILE_ID: {file_id}')
    print(f'CONTEXT: {clean}')
    print('-' * 60)
