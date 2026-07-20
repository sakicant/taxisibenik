# -*- coding: utf-8 -*-
"""Generate the 8 NEW-language route pages for taxisibenik.hr
(es, sv, sr, no, zh, ko, fi, ja) using the shared engine in route_loc.py.

The existing 10 languages keep their own gen_routes_<lang>.py scripts. Run this
after those, before build.py.
"""
import os, re, json, hashlib, sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import route_loc as R

NEW_LANGS = ["es", "sv", "sr", "no", "zh", "ko", "fi", "ja"]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")

src = open(os.path.join(ROOT, "script.js"), encoding="utf-8").read()
i = src.index("const PRICES = {"); j = src.index("{", i); d = 0
for k in range(j, len(src)):
    if src[k] == "{": d += 1
    elif src[k] == "}":
        d -= 1
        if d == 0: end = k + 1; break
PRICES = json.loads(src[j:end])

def price(a, b):
    if a in PRICES and PRICES[a].get(b) is not None: return PRICES[a][b]
    if b in PRICES and PRICES[b].get(a) is not None: return PRICES[b][a]
    return None

DIST = json.load(open(os.path.join(ROOT, "docs", "route-distances.json"), encoding="utf-8"))
def fmt_time(sec):
    m = int(round(sec / 60 / 5.0) * 5)
    if m >= 90:
        h, mm = m // 60, m % 60
        return "%d h" % h if mm == 0 else "%d h %d min" % (h, mm)
    return "%d min" % m

MAPK = {'Šibenik':'Šibenik - center','Brodarica':'Brodarica - Šibenik','Skradin':'Skradin - center',
        'Split Airport':'Split Airport (SPU)','Zadar Airport':'Zadar Airport (ZAD)',
        'Zagreb Airport':'Zagreb Airport (ZAG)','Dubrovnik Airport':'Dubrovnik Airport (DBV)'}
key = lambda n: MAPK.get(n, n)

BIG_CITIES = {'Split','Zadar','Dubrovnik','Zagreb','Trogir'}
AIRPORT_CITY = {'Split Airport':'Split','Zadar Airport':'Zadar','Zagreb Airport':'Zagreb','Dubrovnik Airport':'Dubrovnik'}
MARINAS = {'ACI Marina Trogir','Marina Trogir (SCT)','Marina Baotić','Marina Agana','Marina Pakoštane','D-Marin Dalmacija','Marina Frapa',
           'Marina Kremik','ACI Marina Vodice','Marina Tribunj','Marina Hramina','Marina Betina','ACI Marina Jezera'}

PROVIDER = {
    "@type": "LocalBusiness", "name": "Taxi Antonio",
    "telephone": "+385994471013", "email": "info@taxisibenik.hr",
    "address": {"@type": "PostalAddress", "addressLocality": "Šibenik", "addressCountry": "HR"},
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "152"},
}
TI_HERO = "3d034c475d3887585236cfe8dbc"
TI_REVIEWS = "4aa50a27517a87560776ec90a85"

def vhash(slug, n):
    return int(hashlib.md5(slug.encode()).hexdigest(), 16) % n

rows = []
for line in open(os.path.join(ROOT, "docs", "route-pages.md"), encoding="utf-8"):
    m = re.match(r'\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*`(.+?)`\s*\|\s*(.+?)\s*\|', line)
    if not m: continue
    frm, to, slug, doc = m.groups()
    if frm == "From": continue
    rows.append((frm, to, slug))
slug_of = {(f, t): s for f, t, s in rows}

def bkey(name): return quote(key(name))

def route_type(frm, to):
    if to in AIRPORT_CITY: return "to_airport"
    if frm in AIRPORT_CITY: return "from_airport"
    if frm in MARINAS or to in MARINAS: return "marina"
    if frm in BIG_CITIES or to in BIG_CITIES: return "city"
    return "local"

def build_lang(lang, frm, to, en_slug):
    p = price(key(frm), key(to))
    rp = p * 2
    typ = route_type(frm, to)
    frm_loc, to_loc = R.name_for(lang, frm), R.name_for(lang, to)
    rel = "%s - %s" % (frm_loc, to_loc)
    loc_slug = R.slug_for(lang, en_slug)
    hero_html = ('<img src="/assets/img/hero-transfers.webp" alt="%s" loading="eager">'
                 % R.TR[lang]["hero_alt"].format(rel=rel))

    rev = slug_of.get((to, frm))
    if rev:
        revlink = '<a href="/%s/%s/">%s - %s</a>' % (lang, R.slug_for(lang, rev), to_loc, frm_loc)
    else:
        revlink = "%s - %s" % (to_loc, frm_loc)

    book_link = "/%s/%s/?from=%s&to=%s&price=%s&trip=oneway&pax=1&lug=1" % (
        lang, R.TR[lang]["book_slug"], bkey(frm), bkey(to), p)

    dd = DIST.get("%s|%s" % (frm, to))
    ctx = {
        "frm": frm, "to": to, "rel": rel, "rel_from": frm_loc, "rel_to": to_loc,
        "city": AIRPORT_CITY.get(frm) or AIRPORT_CITY.get(to) or "",
        "p": p, "rp": rp, "typ": typ, "v": vhash(en_slug, 2),
        "dd": bool(dd), "km": dd["km"] if dd else None, "t": fmt_time(dd["sec"]) if dd else None,
        "hero_html": hero_html, "book_link": book_link, "revlink_html": revlink,
        "slug": loc_slug, "page_url": "https://taxisibenik.hr/%s/%s/" % (lang, loc_slug),
        "provider": PROVIDER, "og_image": "https://taxisibenik.hr/assets/img/hero-transfers.webp",
        "ti_hero": TI_HERO, "ti_reviews": TI_REVIEWS,
    }
    content, meta = R.build_page(lang, ctx)
    outdir = os.path.join(PAGES, en_slug, lang)
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, "content.html"), "w", encoding="utf-8").write(content)
    json.dump(meta, open(os.path.join(outdir, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return typ

made = 0
langs = [l for l in NEW_LANGS if l in R.TR]
for lang in langs:
    for frm, to, en_slug in rows:
        if price(key(frm), key(to)) is None:
            continue
        build_lang(lang, frm, to, en_slug)
        made += 1
print("generated sibenik new-lang:", made, "langs:", langs)
