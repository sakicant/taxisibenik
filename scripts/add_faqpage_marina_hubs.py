# -*- coding: utf-8 -*-
"""Add a FAQPage schema block (built from each page's own visible FAQ items) to
the two marina hub pages that were missing it, in every language. Idempotent:
skips a page whose schema already contains a FAQPage."""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")
TARGETS = ["d-marin-mandalina-transfers", "marina-zaton-transfers"]

def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&euro;", "€").replace("&amp;", "&").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()

def faq_schema_from(content):
    items = re.findall(r'<div class="faq-item">\s*<h4>(.*?)</h4>\s*<p>(.*?)</p>\s*</div>', content, re.S)
    if not items:
        return None
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip_tags(q),
                            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in items]}

changed = 0
for pid in TARGETS:
    for lang in sorted(os.listdir(os.path.join(PAGES, pid))):
        d = os.path.join(PAGES, pid, lang)
        mp = os.path.join(d, "meta.json"); cp = os.path.join(d, "content.html")
        if not os.path.exists(mp):
            continue
        meta = json.load(open(mp, encoding="utf-8"))
        schema = meta.get("schema") or []
        if not isinstance(schema, list):
            schema = [schema]
        if any(isinstance(b, dict) and b.get("@type") == "FAQPage" for b in schema):
            continue
        fs = faq_schema_from(open(cp, encoding="utf-8").read())
        if not fs:
            print("  no FAQ items:", pid, lang); continue
        schema.append(fs)
        meta["schema"] = schema
        json.dump(meta, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        changed += 1
print("added FAQPage to", changed, "meta.json files")
