# -*- coding: utf-8 -*-
"""STEP 2: rewrite every taxisibenik link that points into a moved Skradin
route page so it points cross-domain to https://taxiskradin.hr/<final-slug>/.
Run before deleting the moved pages (reads their current slugs from taxisibenik).
"""
import os, re, json

SIB = r"C:\Users\sakic\taxisibenik-code\src\pages"
FINAL = json.load(open(r"C:\Users\sakic\AppData\Local\Temp\claude\C--Users-sakic-taxisibenik-code\cf536c1b-7545-406f-b294-a0de842b092e\scratchpad\skradin_final_slugs.json", encoding="utf-8"))
LANGS = ["en", "hr", "de", "pl", "cs", "it", "fr", "nl", "sl", "hu", "sk"]

moving = set(FINAL.keys())


def lpath(lang, slug):
    return "/%s/" % slug if lang == "en" else "/%s/%s/" % (lang, slug)


# replacement map: current local href -> cross-domain final href
repl = {}
for pid in moving:
    for lang in LANGS:
        cur = json.load(open(os.path.join(SIB, pid, lang, "meta.json"), encoding="utf-8"))["slug"]
        fin = FINAL[pid][lang]
        old = 'href="%s"' % lpath(lang, cur)
        new = 'href="https://taxiskradin.hr%s"' % lpath(lang, fin)
        repl[old] = new

changed_files = 0
changed_pages = set()
for pid in sorted(os.listdir(SIB)):
    if pid in moving:
        continue  # moved pages are handled separately / deleted
    pdir = os.path.join(SIB, pid)
    if not os.path.isdir(pdir):
        continue
    for lang in os.listdir(pdir):
        cpath = os.path.join(pdir, lang, "content.html")
        if not os.path.exists(cpath):
            continue
        html = open(cpath, encoding="utf-8").read()
        orig = html
        for old, new in repl.items():
            if old in html:
                html = html.replace(old, new)
        if html != orig:
            open(cpath, "w", encoding="utf-8").write(html)
            changed_files += 1
            changed_pages.add(pid)

print("rewrote cross-domain links in", changed_files, "files across", len(changed_pages), "page-ids")
for p in sorted(changed_pages):
    print("  ", p)
