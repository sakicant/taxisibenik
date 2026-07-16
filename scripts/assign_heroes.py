# -*- coding: utf-8 -*-
"""Assign per-category hero images (desktop <img> + mobile <picture> source)
across route pages and key hubs, and sync og:image to the desktop hero.
Ordered rules; first match wins. Pages matching no rule are left untouched
(preserves winery/marina custom heroes). Re-runnable/idempotent."""
import os, re, json
ROOT="src/pages"; A="/assets/img/"
LANGS=["en","hr","de","pl","cs","it","fr","nl","sl","hu","sk"]

def desktop_hero(pid):
    if pid.startswith("taxi-tisno-to-"): return "hero-tisno-land.webp"
    if "zagreb" in pid: return "hero-zagreb-land.webp"
    if "zadar" in pid and "zadar-airport" not in pid: return "hero-zadar-center-land.webp"
    return None
def mobile_hero(pid):
    if pid.endswith("-to-split-airport"): return "hero-split-dep-mobile.webp"
    if pid.startswith("taxi-split-airport-to-"): return "hero-split-arr-mobile.webp"
    if "zadar-airport" in pid: return "hero-zadar-airport-mobile.webp"
    if "dubrovnik" in pid: return "hero-dubrovnik-mobile.webp"
    return None

# special pages: (desktop or None -> keep current, mobile or None)
SPECIAL={
 "home":("hero-home-land.webp","hero-dresort-villa-mobile.webp"),
 "airport-transfers":(None,"hero-airport-hub-mobile.webp"),
 "daytrips":(None,"hero-daytrips-hub-mobile.webp"),
 "d-resort-transfers":(None,"hero-dresort-villa-mobile.webp"),
}
HERO=re.compile(r'(?:<picture>\s*<source[^>]*>\s*)?<img src="(/assets/img/[^"]*)"\s+alt="([^"]*)"\s+loading="eager">(?:\s*</picture>)?')

def apply(pid, dh, mh):
    changed=0
    for lang in LANGS:
        cp=os.path.join(ROOT,pid,lang,"content.html")
        if not os.path.exists(cp): continue
        html=open(cp,encoding="utf-8").read()
        m=HERO.search(html)
        if not m: continue
        cur,alt=m.group(1),m.group(2)
        desk = A+dh if dh else cur
        if mh:
            hero='<picture><source media="(max-width: 768px)" srcset="%s%s"><img src="%s" alt="%s" loading="eager"></picture>'%(A,mh,desk,alt)
        else:
            hero='<img src="%s" alt="%s" loading="eager">'%(desk,alt)
        new=html[:m.start()]+hero+html[m.end():]
        if new!=html:
            open(cp,"w",encoding="utf-8").write(new); changed+=1
        if dh:
            mp=os.path.join(ROOT,pid,lang,"meta.json")
            meta=json.load(open(mp,encoding="utf-8"))
            want="https://taxisibenik.hr"+A+dh
            if meta.get("og_image")!=want:
                meta["og_image"]=want; json.dump(meta,open(mp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    return changed

pids=sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT,d)))
tot=0; npages=0
for pid in pids:
    if pid in SPECIAL:
        dh,mh=SPECIAL[pid]
    elif pid.startswith("day-trip-krka"):
        dh,mh=None,"hero-krka-mobile.webp"
    elif pid.startswith("taxi-"):
        dh,mh=desktop_hero(pid),mobile_hero(pid)
        if not dh and not mh: continue
    else:
        continue
    c=apply(pid,dh,mh)
    if c: npages+=1; tot+=c
print("pages touched:",npages,"| lang-files changed:",tot)
