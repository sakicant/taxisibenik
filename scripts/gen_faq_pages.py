# -*- coding: utf-8 -*-
"""Build a dedicated FAQ page per language by reusing the already-translated
FAQ section from each home page. Content matches a freshly-built FAQPage schema
(built from the same visible Q&As), so the rich snippet is consistent."""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")

FAQ_SLUG = {
    "en": "frequently-asked-questions", "hr": "cesta-pitanja", "de": "haeufige-fragen",
    "it": "domande-frequenti", "pl": "czeste-pytania", "cs": "caste-otazky",
    "fr": "questions-frequentes", "nl": "veelgestelde-vragen", "sl": "pogosta-vprasanja",
    "hu": "gyakori-kerdesek", "sk": "caste-otazky",
}

def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&euro;", "€").replace("&amp;", "&").replace("&nbsp;", " ")
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

def build(lang):
    home = os.path.join(PAGES, "home", lang, "content.html")
    if not os.path.exists(home):
        return None
    content = open(home, encoding="utf-8").read()
    m = re.search(r'<section id="faq".*?</section>', content, re.S)
    if not m:
        return "no-faq-section"
    sec = m.group(0)
    eyebrow = (re.search(r'<span class="eyebrow[^"]*">(.*?)</span>', sec, re.S) or [None, "FAQ"])[1].strip()
    h2 = re.search(r'<h2[^>]*>(.*?)</h2>', sec, re.S).group(1).strip()
    subm = re.search(r'<p class="section-subtitle">(.*?)</p>', sec, re.S)
    subtitle = subm.group(1).strip() if subm else ""
    grid = re.search(r'<div class="faq-grid">.*?</div>\s*</div>\s*(?=<p class="faq-more"|</div>\s*</section>)', sec, re.S)
    # fall back: take everything from faq-grid up to the faq-more paragraph or section end
    if grid:
        grid_html = grid.group(0)
    else:
        g = re.search(r'(<div class="faq-grid">.*?</div>)\s*<p class="faq-more"', sec, re.S)
        grid_html = g.group(1) if g else re.search(r'<div class="faq-grid">.*</div>', sec, re.S).group(0)
    items = re.findall(r'<div class="faq-item">\s*<h4>(.*?)</h4>\s*<p>(.*?)</p>\s*</div>', sec, re.S)
    if not items:
        return "no-items"

    faq_schema = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": strip_tags(q),
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in items
        ],
    }

    page = '''  <section class="hub-intro">
    <div class="container">
      <span class="eyebrow center">%s</span>
      <h1 class="section-title">%s</h1>
      <p class="section-subtitle">%s</p>
    </div>
  </section>

  <section id="faq" class="faq">
    <div class="container">
      %s
    </div>
  </section>

{{RELATED_LINKS}}
''' % (eyebrow, h2, subtitle, grid_html.strip())

    slug = FAQ_SLUG[lang]
    title = "%s | TAXI Antonio" % strip_tags(h2)
    desc = strip_tags(subtitle) or strip_tags(h2)
    if len(desc) > 160:
        desc = desc[:157].rstrip() + "..."
    meta = {
        "slug": slug, "title": title, "description": desc,
        "keywords": strip_tags(h2).lower(),
        "og_image": "https://taxisibenik.hr/assets/og-image.png",
        "schema": [faq_schema],
    }
    outdir = os.path.join(PAGES, "faq", lang)
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, "content.html"), "w", encoding="utf-8").write(page)
    json.dump(meta, open(os.path.join(outdir, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return "ok (%d Q&A)" % len(items)

for lang in FAQ_SLUG:
    print("%-3s %s -> %s" % (lang, FAQ_SLUG[lang], build(lang)))
