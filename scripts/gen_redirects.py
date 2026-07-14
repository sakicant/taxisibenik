# -*- coding: utf-8 -*-
"""Audit the old WordPress sitemap against the current site and generate 301s.

The old sitemap groups each concept's language versions together (en, then hr,
de, pl). We use the English URL of each group to identify the concept (current
page-id), then map every old language URL to the current slug for that concept
in that language. Old EN route slugs lack the '-to-' the current ones use, so we
match by collapsing '-to-'. Hubs/renamed pages use an explicit concept map.
Anything unresolved falls back to the most relevant current hub."""
import os, re, json, glob
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = r"C:\Users\sakic\Desktop\XML Sitemap - TAXI Šibenik.xml"

# --- current pages: {page_id: {lang: slug}} ---
current = {}
for mp in glob.glob(os.path.join(ROOT, "src", "pages", "*", "*", "meta.json")):
    parts = mp.split(os.sep)
    page_id, lang = parts[-3], parts[-2]
    slug = json.load(open(mp, encoding="utf-8")).get("slug", "")
    current.setdefault(page_id, {})[lang] = slug

def cur_path(page_id, lang):
    """Current root-relative path for a concept in a language, or None."""
    if page_id not in current or lang not in current[page_id]:
        return None
    slug = current[page_id][lang]
    if lang == "en":
        return "/%s/" % slug if slug else "/"
    return "/%s/%s/" % (lang, slug) if slug else "/%s/" % lang

# en slug -> page_id (exact + collapsed '-to-')
en_slug_to_id = {v["en"]: pid for pid, v in current.items() if "en" in v}
collapse_to_id = {s.replace("-to-", "-"): pid for s, pid in en_slug_to_id.items()}

# explicit concept map for renamed hubs / dropped pages (old en slug -> page_id)
CONCEPT = {
    "airport-transfers": "airport-transfers",
    "city-to-city-transfers": "sibenik-transfers",
    "transfers": "sibenik-transfers",
    "vodice-transfers": "taxi-vodice",
    "tisno-transfers": "sibenik-transfers",   # no dedicated Tisno page
    "marina-transfers": "sibenik-transfers",  # no aggregate marina hub now
    "day-trip-sibenik-from-zadar": "daytrips",
    "day-trip-sibenik-from-split": "daytrips",
}

def lang_of(path):
    seg = path.strip("/").split("/")
    return seg[0] if seg and seg[0] in ("hr", "de", "pl") else "en"

def en_slug_of(path, lang):
    p = path.strip("/")
    if lang != "en":
        p = p[len(lang) + 1:]  # strip "xx/"
    return p  # '' for home

def resolve_pageid(en_path):
    """page_id for a group, from its English URL path."""
    slug = en_slug_of(en_path, "en")
    if slug in en_slug_to_id:      # unchanged en slug
        return en_slug_to_id[slug]
    if slug in collapse_to_id:     # route: old lacks '-to-'
        return collapse_to_id[slug]
    if slug in CONCEPT:
        return CONCEPT[slug]
    return None

def fallback(path, lang):
    s = path.lower()
    if re.search(r"airport|aerodrom|flughafen|lotnisko|zracna-luka|zum-flughafen", s):
        return cur_path("airport-transfers", lang)
    if re.search(r"day-?trip|izlet|tagesausflug|wycieczka|dnevni", s):
        return cur_path("daytrips", lang)
    if re.search(r"taxi|taksi|taksowka|transfer", s):
        return cur_path("sibenik-transfers", lang)
    return "/%s/" % lang if lang != "en" else "/"

# --- parse old sitemap, in order, and group by en-start ---
old = open(OLD, encoding="utf-8").read()
oldpaths = [urlparse(u).path for u in re.findall(r"<loc>\s*(.*?)\s*</loc>", old)]
cur_all = set()
for pid in current:
    for lg in current[pid]:
        cur_all.add(cur_path(pid, lg))

groups = []
for p in oldpaths:
    if lang_of(p) == "en":
        groups.append([p])
    else:
        if groups:
            groups[-1].append(p)
        else:
            groups.append([p])

SKRADIN_HOME = {"en": "https://taxiskradin.hr/", "hr": "https://taxiskradin.hr/hr/",
                "de": "https://taxiskradin.hr/de/", "pl": "https://taxiskradin.hr/pl/"}

redirects = []   # (old_path, target, is_external)
fallbacks = []
bad_targets = []
for g in groups:
    pid = resolve_pageid(g[0])
    for p in g:
        if p in cur_all:
            continue  # still exists, no redirect
        lang = lang_of(p)
        # Skradin taxi pages -> sister site
        if re.search(r"(^|/)(taxi|taksi|taksowka)-skradin/?$", p):
            redirects.append((p, SKRADIN_HOME[lang], True)); continue
        target = cur_path(pid, lang) if pid else None
        if not target:
            target = fallback(p, lang)
            fallbacks.append((p, target))
        if target and target != p:
            if not target.startswith("http") and target not in cur_all:
                bad_targets.append((p, target))
            redirects.append((p, target, target.startswith("http")))

print("groups:", len(groups), "| redirects:", len(redirects),
      "| fallbacks:", len(fallbacks), "| BAD TARGETS:", len(bad_targets))
print("\n=== FALLBACKS ===")
for p, t in fallbacks:
    print("  %-55s -> %s" % (p, t))
if bad_targets:
    print("\n=== BAD TARGETS (do not exist!) ===")
    for p, t in bad_targets:
        print("  %-55s -> %s" % (p, t))

# emit the full redirect block for .htaccess
lines = []
lines.append("  # ===== 301 redirects (regenerated from the old sitemap audit) =====")
lines.append("  # Aliases not present in the old sitemap")
lines.append("  RewriteRule ^taxi-sibenik/?$ / [R=301,L]")
lines.append("  RewriteRule ^transfers-2/?$ /sibenik-transfers/ [R=301,L]")
lines.append("  RewriteRule ^airport-zadar-transfer/?$ /airport-transfers-from-sibenik/ [R=301,L]")
lines.append("")
lines.append("  # Skradin content -> sister site taxiskradin.hr")
lines.append("  RewriteRule ^(aci-marina-skradin-transfers)/?$ https://taxiskradin.hr/$1/ [R=301,L]")
lines.append("  RewriteRule ^([a-z]{2}/aci-marina-skradin-[a-z]+)/?$ https://taxiskradin.hr/$1/ [R=301,L]")
ext = [r for r in redirects if r[2]]
intr = [r for r in redirects if not r[2]]
for p, t, _ in sorted(ext):
    lines.append("  RewriteRule ^%s/?$ %s [R=301,L]" % (p.strip("/"), t))
lines.append("")
lines.append("  # Old sitemap URLs whose slug changed -> current page (same language)")
for p, t, _ in sorted(intr):
    lines.append("  RewriteRule ^%s/?$ %s [R=301,L]" % (p.strip("/"), t))

out = os.path.join(ROOT, "scripts", "_redirects_block.txt")
open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\nwrote", out, "(%d internal + %d external + 5 manual)" % (len(intr), len(ext)))
