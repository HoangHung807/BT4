import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SITE_FILES = {
    'index': BASE / 'index.html',
    'article': BASE / 'article.html',
    'faq': BASE / 'faq.html'
}

# Very small heuristic: match keywords to page
PAGE_KEYWORDS = {
    'sinh viên': 'article',
    'sinh vien': 'article',
    'dưới 10': 'faq',
    'duoi 10': 'faq',
    'iPhone': 'faq',
    'Samsung': 'faq',
    'game': 'article',
    'chụp': 'article',
    'chup': 'article',
    'pin': 'article',
    'camera': 'article',
    '5.000': 'article',
}


def choose_page(query):
    q = query.lower()
    for k, p in PAGE_KEYWORDS.items():
        if k.lower() in q:
            return p
    # fallback
    if 'iphone' in q or 'samsung' in q:
        return 'faq'
    return 'article'


def extract_snippet(page_key):
    path = SITE_FILES.get(page_key)
    if not path or not path.exists():
        return ''
    text = path.read_text(encoding='utf-8')
    # crude: take first 300 chars of body
    body_start = text.find('<main')
    if body_start == -1:
        return text[:300]
    snippet = text[body_start:body_start+600]
    return ' '.join(snippet.split())[:600]


def run_demo():
    queries = []
    with open(BASE / 'data' / 'ai-queries.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            queries.append(r['Query'])

    results = []
    for q in queries:
        page = choose_page(q)
        snippet = extract_snippet(page)
        url = f"https://HoangHung807.github.io/BT4/{page}.html"
        answer = f"Demo answer for: {q} -- Source: {url}\n\nSnippet:\n{snippet}" 
        results.append({'query': q, 'answer': answer, 'source': url})

    out = BASE / 'tools' / 'ai_demo_results.json'
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Wrote demo results to: {out}")


if __name__ == '__main__':
    run_demo()
