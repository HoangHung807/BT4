import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
pages = [ROOT / 'index.html', ROOT / 'article.html', ROOT / 'faq.html']

def read_html(p):
    return p.read_text(encoding='utf-8')

def extract_jsonld_blocks(html):
    # find <script type="application/ld+json"> ... </script>
    pattern = re.compile(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S|re.I)
    blocks = pattern.findall(html)
    objs = []
    for b in blocks:
        try:
            objs.append(json.loads(b.strip()))
        except Exception:
            # try to fix common trailing commas
            try:
                cleaned = re.sub(r',\s*}', '}', b)
                cleaned = re.sub(r',\s*]', ']', cleaned)
                objs.append(json.loads(cleaned))
            except Exception:
                pass
    return objs

def has_meta_description(html):
    return bool(re.search(r'<meta[^>]*name=["\']description["\'][^>]*>', html, re.I))

def has_canonical(html):
    return bool(re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*>', html, re.I))

def main():
    report = {'pages':{}}
    for p in pages:
        name = p.name
        html = read_html(p)
        desc = has_meta_description(html)
        canonical = has_canonical(html)
        jsonlds = extract_jsonld_blocks(html)
        types = []
        faq_count = 0
        for j in jsonlds:
            if isinstance(j, dict):
                t = j.get('@type')
                if t:
                    types.append(t)
                if j.get('@type') == 'FAQPage':
                    me = j.get('mainEntity')
                    if isinstance(me, list):
                        faq_count = len(me)
        report['pages'][name] = {
            'meta_description': desc,
            'canonical': canonical,
            'jsonld_types': types,
            'faq_count': faq_count
        }

    out = ROOT / 'tools' / 'validation_report.json'
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print('Validation complete. Report:', out)

if __name__ == '__main__':
    main()
