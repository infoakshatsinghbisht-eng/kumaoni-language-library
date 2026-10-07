import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
urls = [
    'https://www.kumauni.in/p/e-books-relating-to-kumauni-language.html',
    'https://www.kumauni.in/p/blog-page_87.html',
    'https://www.kumauni.in/2019/12/blog-post_56.html'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f'Page {url}: {len(html)} chars')
            # Extract links and titles
            matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
            print(f'Found {len(matches)} anchor tags:')
            for href, text in matches:
                clean_text = re.sub(r'<[^>]+>', '', text).strip()
                if any(k in href.lower() for k in ['pdf', 'drive.google', 'archive.org', 'dropbox', 'mediafire']) or any(k in clean_text for k in ['डाउनलोड', 'किताब', 'पुस्तक', 'ई-बुक', 'pdf', 'PDF', 'पढ़ें', 'पढ़ें']):
                    print(f'  LINK: {clean_text[:50]} -> {href}')
    except Exception as e:
        print(f'Error fetching {url}: {e}')
