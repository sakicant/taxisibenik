# -*- coding: utf-8 -*-
"""Cross-link the Krka day-trip pages to the Skradin Krka hub.

taxisibenik.hr owns the "day trip to Krka from <town>" pages; taxiskradin.hr
owns the gateway content (Skradin sits at the park gate). Linking the two makes
them complementary rather than competing, and passes authority to the newer
site without moving any ranking page.

Inserts one short paragraph before the "why-book" section on each Krka
day-trip page, in every language. Idempotent: skips pages that already link.

Run with --write; without it, prints a dry run.
"""
import os, io, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")
WRITE = "--write" in sys.argv

DAYTRIPS = ["day-trip-krka-sibenik", "day-trip-krka-split", "day-trip-krka-zadar",
            "day-trip-krka-vodice", "day-trip-krka-primosten"]

# (lead sentence, link text) per language
T = {
 "en": ("Starting your day in Skradin instead?", "Taxi to Krka National Park from Skradin"),
 "hr": ("Krećete iz Skradina?", "Taksi do NP Krka iz Skradina"),
 "de": ("Starten Sie stattdessen in Skradin?", "Taxi zum Nationalpark Krka ab Skradin"),
 "pl": ("Zaczynasz dzień w Skradinie?", "Taxi do Parku Narodowego Krka ze Skradina"),
 "cs": ("Začínáte den ve Skradinu?", "Taxi do NP Krka ze Skradinu"),
 "it": ("Parte invece da Skradin?", "Taxi per il Parco Nazionale di Krka da Skradin"),
 "fr": ("Vous partez plutôt de Skradin ?", "Taxi vers le parc national de Krka depuis Skradin"),
 "nl": ("Vertrekt u liever vanuit Skradin?", "Taxi naar Nationaal Park Krka vanuit Skradin"),
 "sl": ("Začenjate dan v Skradinu?", "Taksi do NP Krka iz Skradina"),
 "hu": ("Inkább Skradinból indul?", "Taxi a Krka Nemzeti Parkba Skradinból"),
 "sk": ("Začínate deň v Skradine?", "Taxi do NP Krka zo Skradinu"),
 "es": ("¿Empieza el día en Skradin?", "Taxi al Parque Nacional de Krka desde Skradin"),
 "sv": ("Startar du dagen i Skradin i stället?", "Taxi till nationalparken Krka från Skradin"),
 "sr": ("Krećete iz Skradina?", "Taksi do NP Krka iz Skradina"),
 "no": ("Starter du dagen i Skradin i stedet?", "Taxi til Krka nasjonalpark fra Skradin"),
 "zh": ("从斯克拉丁出发？", "从 Skradin 前往 Krka 国家公园的出租车"),
 "ko": ("스크라딘에서 출발하시나요?", "Skradin에서 Krka 국립공원까지 택시"),
 "fi": ("Aloitatko päivän Skradinista?", "Taksi Krkan kansallispuistoon Skradinista"),
 "ja": ("スクラディンから出発されますか？", "Skradin からクルカ国立公園へのタクシー"),
}

# short explainer per language: Skradin is at the park gate, that runs on the sister site
WHY = {
 "en": "Skradin sits right at the park gate, so those transfers run on my sister site:",
 "hr": "Skradin je na samim vratima parka, pa te prijevoze vodim na sestrinskoj stranici:",
 "de": "Skradin liegt direkt am Parkeingang, daher laufen diese Transfers auf meiner Schwesterseite:",
 "pl": "Skradin leży tuż przy bramie parku, więc te transfery prowadzę na siostrzanej stronie:",
 "cs": "Skradin leží přímo u brány parku, proto tyto přejezdy vedu na sesterském webu:",
 "it": "Skradin si trova proprio all'ingresso del parco, quindi quei trasferimenti sono sul sito gemello:",
 "fr": "Skradin se trouve juste à l'entrée du parc, ces transferts sont donc sur mon site jumeau :",
 "nl": "Skradin ligt vlak bij de parkingang, dus die transfers staan op mijn zustersite:",
 "sl": "Skradin je tik ob vhodu v park, zato te prevoze vodim na sestrski strani:",
 "hu": "Skradin közvetlenül a park kapujánál fekszik, ezért ezek a transzferek a testvéroldalon futnak:",
 "sk": "Skradin leží priamo pri bráne parku, preto tieto prejazdy vediem na sesterskom webe:",
 "es": "Skradin está justo en la entrada del parque, así que esos traslados están en mi sitio hermano:",
 "sv": "Skradin ligger precis vid parkens entré, så de transfererna finns på min systersajt:",
 "sr": "Skradin je na samim vratima parka, pa te prevoze vodim na sestrinskom sajtu:",
 "no": "Skradin ligger rett ved parkporten, så de transportene ligger på søstersiden min:",
 "zh": "Skradin 就在公园入口旁，因此这些接送服务在我的姊妹网站上：",
 "ko": "Skradin은 공원 입구 바로 옆에 있어 해당 이동 서비스는 자매 사이트에서 운영합니다:",
 "fi": "Skradin sijaitsee aivan puiston portilla, joten ne kuljetukset ovat sisarsivustollani:",
 "ja": "Skradin は公園のゲートのすぐそばにあるため、これらの送迎は姉妹サイトでご案内しています:",
}

ANCHOR = '  <section class="why-book">'
added, skipped, missing = 0, 0, []

for pid in DAYTRIPS:
    pdir = os.path.join(PAGES, pid)
    if not os.path.isdir(pdir):
        continue
    for lang in sorted(os.listdir(pdir)):
        cp = os.path.join(pdir, lang, "content.html")
        if not os.path.isfile(cp) or lang not in T:
            continue
        html = io.open(cp, encoding="utf-8", errors="ignore").read()
        if "taxiskradin.hr/" in html and "krka-national-park-transfers" in html:
            skipped += 1
            continue
        if ANCHOR not in html:
            missing.append("%s/%s" % (pid, lang))
            continue
        prefix = "" if lang == "en" else lang + "/"
        block = (
            '  <section class="page-content">\n'
            '    <div class="container prose">\n'
            '      <p><strong>%s</strong> %s <a href="https://taxiskradin.hr/%skrka-national-park-transfers/" target="_blank" rel="noopener">%s</a>.</p>\n'
            '    </div>\n'
            '  </section>\n\n'
        ) % (T[lang][0], WHY[lang], prefix, T[lang][1])
        html = html.replace(ANCHOR, block + ANCHOR, 1)
        if WRITE:
            io.open(cp, "w", encoding="utf-8").write(html)
        added += 1

print("cross-links added:", added)
print("already linked (skipped):", skipped)
print("anchor not found:", len(missing), missing[:5])
if not WRITE:
    print("\n(dry run - nothing written. re-run with --write)")
