# -*- coding: utf-8 -*-
"""STEP 1 of the Skradin migration: copy the 88 Skradin-related route pages
(both directions) from taxisibenik-code into taxiskradin-code, with:
  - live-site slug reconciliation for the 19 pages that exist live (hr/de/pl),
  - reverse-link (revlink) rewrite to the reverse page's FINAL slug,
  - domain swap in meta schema url + og_image (taxisibenik.hr -> taxiskradin.hr).
Does NOT delete from taxisibenik (step 2 does that after verification).
Writes the final slug map to scratch for the hub-link-fix step."""
import os, re, json, shutil

SIB = r"C:\Users\sakic\taxisibenik-code\src\pages"
SKR = r"C:\Users\sakic\taxiskradin-code\src\pages"
OVERRIDES = json.load(open(r"C:\Users\sakic\taxiskradin-code\docs\live-slug-overrides.json", encoding="utf-8"))
LANGS = ["en", "hr", "de", "pl", "cs", "it", "fr", "nl", "sl", "hu", "sk"]

moving = sorted([d for d in os.listdir(SIB)
                 if re.search(r'^taxi-skradin-to-|-to-skradin$', d) and os.path.isdir(os.path.join(SIB, d))])
assert len(moving) == 88, len(moving)


def reverse(pid):
    body = pid[len("taxi-"):]
    a, b = body.split("-to-", 1)
    return "taxi-%s-to-%s" % (b, a)


# read all current slugs first (before any change)
cur = {}
for pid in moving:
    for lang in LANGS:
        mp = os.path.join(SIB, pid, lang, "meta.json")
        cur[(pid, lang)] = json.load(open(mp, encoding="utf-8"))["slug"]


def final_slug(pid, lang):
    if pid in OVERRIDES and lang in OVERRIDES[pid]:
        return OVERRIDES[pid][lang]
    return cur[(pid, lang)]


def lpath(lang, slug):
    return "/%s/" % slug if lang == "en" else "/%s/%s/" % (lang, slug)


copied = 0
revlink_fixes = 0
for pid in moving:
    rev = reverse(pid)
    for lang in LANGS:
        srcdir = os.path.join(SIB, pid, lang)
        dstdir = os.path.join(SKR, pid, lang)
        os.makedirs(dstdir, exist_ok=True)
        html = open(os.path.join(srcdir, "content.html"), encoding="utf-8").read()
        meta = json.load(open(os.path.join(srcdir, "meta.json"), encoding="utf-8"))

        # 1) reverse-link fix: point to reverse page's FINAL slug
        rev_cur = cur[(rev, lang)]
        rev_fin = final_slug(rev, lang)
        if rev_cur != rev_fin:
            old = 'href="%s"' % lpath(lang, rev_cur)
            new = 'href="%s"' % lpath(lang, rev_fin)
            if old in html:
                html = html.replace(old, new)
                revlink_fixes += 1

        # 2) meta: new own slug, domain swap in schema + og_image, schema url slug
        meta["slug"] = final_slug(pid, lang)
        if meta.get("og_image"):
            meta["og_image"] = meta["og_image"].replace("https://taxisibenik.hr", "https://taxiskradin.hr")
        sch = meta.get("schema")
        if sch:
            s = json.dumps(sch, ensure_ascii=False)
            s = s.replace("https://taxisibenik.hr", "https://taxiskradin.hr")
            meta["schema"] = json.loads(s)

        # 3) any stray absolute domain in content
        html = html.replace("https://taxisibenik.hr", "https://taxiskradin.hr")

        open(os.path.join(dstdir, "content.html"), "w", encoding="utf-8").write(html)
        json.dump(meta, open(os.path.join(dstdir, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        copied += 1

# save the final slug map (page-id -> lang -> slug) for the taxisibenik hub fix
fmap = {pid: {lang: final_slug(pid, lang) for lang in LANGS} for pid in moving}
scratch = r"C:\Users\sakic\AppData\Local\Temp\claude\C--Users-sakic-taxisibenik-code\cf536c1b-7545-406f-b294-a0de842b092e\scratchpad"
json.dump(fmap, open(os.path.join(scratch, "skradin_final_slugs.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print("pages moved:", len(moving), "| lang-files copied:", copied, "| revlink fixes:", revlink_fixes)
print("saved final slug map for", len(fmap), "pages")
