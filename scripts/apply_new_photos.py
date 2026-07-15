# -*- coding: utf-8 -*-
"""Place the new photos (July 2026 batch) across all 11 languages:
  - Bibich route page: car-at-Bibich photo as hero, winery entrance photo in
    the intro (hub-intro becomes a hub-prose section with the image).
  - Testament route page: vineyard photo as hero.
  - Airport-transfers hub: new Split Airport terminal photo as the content
    image (hero image untouched).
  - Vodice town page: waterfront photo as the content image.
Idempotent."""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")
LANGS = ["en", "hr", "de", "pl", "cs", "it", "fr", "nl", "sl", "hu", "sk"]

ALT = {
 "en": dict(bib_hero="TAXI Antonio's Škoda Superb in front of Bibich Winery in Plastovo",
            bib_ent="Entrance to the Bibich Winery tasting room in Plastovo near Skradin",
            test_hero="TAXI Antonio's Škoda Superb beside the vineyards on the way to Testament Winery near Šibenik",
            split="Split Airport terminal, where Antonio meets arriving passengers",
            vodice="TAXI Antonio's Škoda Superb on the Vodice seafront next to the marina"),
 "hr": dict(bib_hero="Škoda Superb TAXI Antonio ispred vinarije Bibich u Plastovu",
            bib_ent="Ulaz u kušaonicu vinarije Bibich u Plastovu kraj Skradina",
            test_hero="Škoda Superb TAXI Antonio uz vinograde na putu prema vinariji Testament kraj Šibenika",
            split="Terminal Zračne luke Split, gdje Antonio dočekuje putnike u dolasku",
            vodice="Škoda Superb TAXI Antonio na rivi u Vodicama uz marinu"),
 "de": dict(bib_hero="Škoda Superb von TAXI Antonio vor dem Weingut Bibich in Plastovo",
            bib_ent="Eingang zum Verkostungsraum des Weinguts Bibich in Plastovo bei Skradin",
            test_hero="Škoda Superb von TAXI Antonio an den Weinbergen auf dem Weg zum Weingut Testament bei Šibenik",
            split="Terminal des Flughafens Split, wo Antonio ankommende Passagiere empfängt",
            vodice="Škoda Superb von TAXI Antonio an der Uferpromenade von Vodice neben der Marina"),
 "pl": dict(bib_hero="Škoda Superb TAXI Antonio przed winnicą Bibich w Plastovie",
            bib_ent="Wejście do sali degustacyjnej winnicy Bibich w Plastovie koło Skradina",
            test_hero="Škoda Superb TAXI Antonio przy winnicach w drodze do winnicy Testament koło Šibenika",
            split="Terminal lotniska Split, gdzie Antonio wita przylatujących pasażerów",
            vodice="Škoda Superb TAXI Antonio na nabrzeżu w Vodicach obok mariny"),
 "cs": dict(bib_hero="Škoda Superb TAXI Antonio před vinařstvím Bibich v Plastovu",
            bib_ent="Vstup do degustační místnosti vinařství Bibich v Plastovu u Skradinu",
            test_hero="Škoda Superb TAXI Antonio u vinic na cestě k vinařství Testament u Šibeniku",
            split="Terminál letiště Split, kde Antonio vítá přilétající cestující",
            vodice="Škoda Superb TAXI Antonio na nábřeží ve Vodicích u maríny"),
 "it": dict(bib_hero="La Škoda Superb di TAXI Antonio davanti alla cantina Bibich a Plastovo",
            bib_ent="Ingresso della sala degustazione della cantina Bibich a Plastovo vicino a Skradin",
            test_hero="La Škoda Superb di TAXI Antonio lungo i vigneti verso la cantina Testament vicino a Šibenik",
            split="Terminal dell'aeroporto di Split, dove Antonio accoglie i passeggeri in arrivo",
            vodice="La Škoda Superb di TAXI Antonio sul lungomare di Vodice accanto alla marina"),
 "fr": dict(bib_hero="La Škoda Superb de TAXI Antonio devant le domaine viticole Bibich à Plastovo",
            bib_ent="Entrée de la salle de dégustation du domaine Bibich à Plastovo près de Skradin",
            test_hero="La Škoda Superb de TAXI Antonio le long des vignes en route vers le domaine Testament près de Šibenik",
            split="Terminal de l'aéroport de Split, où Antonio accueille les passagers à l'arrivée",
            vodice="La Škoda Superb de TAXI Antonio sur le front de mer de Vodice près de la marina"),
 "nl": dict(bib_hero="De Škoda Superb van TAXI Antonio voor wijnhuis Bibich in Plastovo",
            bib_ent="Ingang van de proeverij van wijnhuis Bibich in Plastovo bij Skradin",
            test_hero="De Škoda Superb van TAXI Antonio langs de wijngaarden op weg naar wijnhuis Testament bij Šibenik",
            split="Terminal van de luchthaven van Split, waar Antonio aankomende passagiers opwacht",
            vodice="De Škoda Superb van TAXI Antonio aan de boulevard van Vodice naast de jachthaven"),
 "sl": dict(bib_hero="Škoda Superb TAXI Antonio pred vinarijo Bibich v Plastovem",
            bib_ent="Vhod v degustacijsko sobo vinarije Bibich v Plastovem pri Skradinu",
            test_hero="Škoda Superb TAXI Antonio ob vinogradih na poti do vinarije Testament pri Šibeniku",
            split="Terminal letališča Split, kjer Antonio pričaka prispele potnike",
            vodice="Škoda Superb TAXI Antonio na obali v Vodicah ob marini"),
 "hu": dict(bib_hero="A TAXI Antonio Škoda Superbje a Bibich pincészet előtt Plastovóban",
            bib_ent="A Bibich pincészet kóstolótermének bejárata Plastovóban, Skradin közelében",
            test_hero="A TAXI Antonio Škoda Superbje a szőlők mellett a Testament pincészet felé Šibenik közelében",
            split="A spliti repülőtér terminálja, ahol Antonio az érkező utasokat várja",
            vodice="A TAXI Antonio Škoda Superbje a vodicei tengerparti sétányon a kikötő mellett"),
 "sk": dict(bib_hero="Škoda Superb TAXI Antonio pred vinárstvom Bibich v Plastove",
            bib_ent="Vstup do degustačnej miestnosti vinárstva Bibich v Plastove pri Skradine",
            test_hero="Škoda Superb TAXI Antonio pri viniciach na ceste k vinárstvu Testament pri Šibeniku",
            split="Terminál letiska Split, kde Antonio víta prilietajúcich cestujúcich",
            vodice="Škoda Superb TAXI Antonio na nábreží vo Vodiciach pri maríne"),
}

HUB_INTRO_RE = re.compile(
    r'<section class="hub-intro">\s*<div class="container">\s*'
    r'<span class="eyebrow center">(.*?)</span>\s*'
    r'<h2 class="section-title">(.*?)</h2>\s*'
    r'<p class="section-subtitle">(.*?)</p>\s*'
    r'</div>\s*</section>', re.S)


def swap_hero(html, new_src, new_alt, extra_class):
    html = html.replace('class="hero daytrip-hero"',
                        'class="hero daytrip-hero %s"' % extra_class, 1)
    html = re.sub(r'<img src="/assets/img/hero-transfers\.webp" alt="[^"]*" loading="eager">',
                  '<img src="/assets/img/%s" alt="%s" loading="eager">' % (new_src, new_alt),
                  html, count=1)
    return html


def prose_block(eyebrow, h2, p, img, alt):
    return ('''<section class="hub-prose-section hub-prose-white">
    <div class="container hub-prose-inner">
      <div class="hub-prose-image">
        <img src="/assets/img/%s" alt="%s" loading="lazy">
      </div>
      <div class="hub-prose-text">
        <span class="eyebrow">%s</span>
        <h2>%s</h2>
        <p>%s</p>
      </div>
    </div>
  </section>''' % (img, alt, eyebrow, h2, p))


def set_og(page_id, lang, img):
    mp = os.path.join(PAGES, page_id, lang, "meta.json")
    meta = json.load(open(mp, encoding="utf-8"))
    meta["og_image"] = "https://taxisibenik.hr/assets/img/" + img
    json.dump(meta, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


for lang in LANGS:
    a = ALT[lang]

    # --- Bibich: hero + entrance photo in the intro ---
    p = os.path.join(PAGES, "taxi-sibenik-to-bibich-winery", lang, "content.html")
    s = open(p, encoding="utf-8").read()
    if "taxi-antonio-bibich-winery.webp" not in s:
        s = swap_hero(s, "taxi-antonio-bibich-winery.webp", a["bib_hero"], "hero-photo-bibich")
        m = HUB_INTRO_RE.search(s)
        if m:
            s = s[:m.start()] + prose_block(m.group(1), m.group(2), m.group(3),
                                            "bibich-winery-entrance.webp", a["bib_ent"]) + s[m.end():]
        else:
            print("  no hub-intro match (bibich)", lang)
        open(p, "w", encoding="utf-8").write(s)
        set_og("taxi-sibenik-to-bibich-winery", lang, "taxi-antonio-bibich-winery.webp")
        print("bibich:", lang)

    # --- Testament: vineyard hero ---
    p = os.path.join(PAGES, "taxi-sibenik-to-testament-winery", lang, "content.html")
    s = open(p, encoding="utf-8").read()
    if "taxi-transfer-sibenik-winery.webp" not in s:
        s = swap_hero(s, "taxi-transfer-sibenik-winery.webp", a["test_hero"], "hero-photo-vineyard")
        open(p, "w", encoding="utf-8").write(s)
        set_og("taxi-sibenik-to-testament-winery", lang, "taxi-transfer-sibenik-winery.webp")
        print("testament:", lang)

    # --- Airport hub: content image only (hero untouched) ---
    p = os.path.join(PAGES, "airport-transfers", lang, "content.html")
    s = open(p, encoding="utf-8").read()
    if "taxi-antonio-split-airport.webp" not in s:
        s2 = re.sub(r'<img src="/assets/img/airport-terminal\.webp" alt="[^"]*"',
                    '<img src="/assets/img/taxi-antonio-split-airport.webp" alt="%s"' % a["split"], s, count=1)
        if s2 == s:
            print("  no airport-terminal img", lang)
        open(p, "w", encoding="utf-8").write(s2)
        print("airport hub:", lang)

    # --- Vodice town page: waterfront photo as the content image ---
    p = os.path.join(PAGES, "taxi-vodice", lang, "content.html")
    s = open(p, encoding="utf-8").read()
    if "taxi-antonio-vodice.webp" not in s:
        s2 = re.sub(r'<img src="/assets/img/hero-airport\.webp" alt="[^"]*"',
                    '<img src="/assets/img/taxi-antonio-vodice.webp" alt="%s"' % a["vodice"], s, count=1)
        if s2 == s:
            print("  no hero-airport img (vodice)", lang)
        open(p, "w", encoding="utf-8").write(s2)
        print("vodice:", lang)

print("done")
