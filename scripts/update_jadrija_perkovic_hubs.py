# -*- coding: utf-8 -*-
"""After the new route pages exist:
  - Jadrija hub: turn the linkless "Arriving by plane?" note into a linked one
    (reverse airport->Jadrija pages now exist).
  - Perkovic hub: add "Route details" links to the Sibenik/Vodice/Skradin fare
    rows (forward pages) and add a "both ways" note linking the reverse pages.
Idempotent."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import add_arrivals_note as A

PAGES = A.PAGES
LANGS = A.LANGS


def page_url(page_id, lang):
    meta = os.path.join(PAGES, page_id, lang, "meta.json")
    if not os.path.exists(meta):
        return None
    slug = json.load(open(meta, encoding="utf-8"))["slug"]
    return "/%s/" % slug if lang == "en" else "/%s/%s/" % (lang, slug)


# ---------------------------------------------------------------- Jadrija note
def fix_jadrija():
    for lang in LANGS:
        path = os.path.join(PAGES, "taxi-jadrija", lang, "content.html")
        html = open(path, encoding="utf-8").read()
        fields = {"TOWN": "Jadrija"}
        ok = True
        for keyk, label in A.AIRPORTS:
            url = A.reverse_url("jadrija", keyk, lang)
            ph = {"split": "SPLIT", "zadar": "ZADAR", "zagreb": "ZAGREB", "dubrovnik": "DUBR"}[keyk]
            if url:
                fields[ph] = '<a href="%s">%s</a>' % (url, label)
            else:
                fields[ph] = label; ok = False
        note = '<p class="hub-note hub-note-arrival">' + A.NOTES[lang].format(**fields) + '</p>'
        lines = html.split("\n")
        done = False
        for i, ln in enumerate(lines):
            if "hub-note-arrival" in ln:
                indent = ln[:len(ln) - len(ln.lstrip())]
                lines[i] = indent + note
                done = True
                break
        if done:
            open(path, "w", encoding="utf-8").write("\n".join(lines))
            print("jadrija note linked:", lang, "(all 4 linked)" if ok else "(some missing)")
        else:
            print("jadrija: no arrival note found", lang)


# ---------------------------------------------------------------- Perkovic hub
# fare-row anchor tokens (language-invariant book hrefs) -> forward page id
FWD = [
    ("%C5%A0ibenik%20-%20center", "taxi-perkovic-to-sibenik"),
    ("Skradin%20-%20center", "taxi-perkovic-to-skradin"),
    ("Vodice&price=70", "taxi-perkovic-to-vodice"),
]
REV = [("Šibenik", "taxi-sibenik-to-perkovic"), ("Vodice", "taxi-vodice-to-perkovic"),
       ("Skradin", "taxi-skradin-to-perkovic")]

BOTH = {
    "en": "<strong>These routes run both ways.</strong> I drive Perković to Šibenik, Vodice and Skradin and back, at the same fixed price each way. See the return direction: {SIB}, {VOD}, {SKR}.",
    "hr": "<strong>Ove rute vozim u oba smjera.</strong> Perković do Šibenika, Vodica i Skradina i natrag, po istoj fiksnoj cijeni u svakom smjeru. Pogledajte suprotni smjer: {SIB}, {VOD}, {SKR}.",
    "de": "<strong>Diese Strecken fahre ich in beide Richtungen.</strong> Perković nach Šibenik, Vodice und Skradin und zurück, zum selben Festpreis je Richtung. Gegenrichtung ansehen: {SIB}, {VOD}, {SKR}.",
    "pl": "<strong>Te trasy obsługuję w obie strony.</strong> Perković do Šibenika, Vodic i Skradina i z powrotem, w tej samej stałej cenie w każdą stronę. Zobacz kierunek powrotny: {SIB}, {VOD}, {SKR}.",
    "cs": "<strong>Tyto trasy jezdím oběma směry.</strong> Perković do Šibeniku, Vodic a Skradinu a zpět, za stejnou pevnou cenu každým směrem. Podívejte se na opačný směr: {SIB}, {VOD}, {SKR}.",
    "it": "<strong>Faccio queste tratte in entrambe le direzioni.</strong> Perković verso Šibenik, Vodice e Skradin e ritorno, allo stesso prezzo fisso per direzione. Guarda il senso opposto: {SIB}, {VOD}, {SKR}.",
    "fr": "<strong>Je fais ces trajets dans les deux sens.</strong> Perković vers Šibenik, Vodice et Skradin et retour, au même prix fixe par sens. Voir le sens inverse : {SIB}, {VOD}, {SKR}.",
    "nl": "<strong>Deze routes rijd ik beide kanten op.</strong> Perković naar Šibenik, Vodice en Skradin en terug, voor dezelfde vaste prijs per richting. Bekijk de andere richting: {SIB}, {VOD}, {SKR}.",
    "sl": "<strong>Te poti vozim v obe smeri.</strong> Perković do Šibenika, Vodic in Skradina in nazaj, po isti fiksni ceni v vsako smer. Poglejte obratno smer: {SIB}, {VOD}, {SKR}.",
    "hu": "<strong>Ezeket az útvonalakat mindkét irányban vállalom.</strong> Perković–Šibenik, Vodice és Skradin, oda-vissza, irányonként ugyanazon a fix áron. Ellenkező irány: {SIB}, {VOD}, {SKR}.",
    "sk": "<strong>Tieto trasy jazdím oboma smermi.</strong> Perković do Šibeniku, Vodíc a Skradinu a späť, za rovnakú pevnú cenu každým smerom. Pozrite si opačný smer: {SIB}, {VOD}, {SKR}.",
}
RD = {"en": "Route details", "hr": "Detalji rute", "de": "Streckendetails", "pl": "Szczegóły trasy",
      "cs": "Detaily trasy", "it": "Dettagli tratta", "fr": "Détails du trajet", "nl": "Routedetails",
      "sl": "Podrobnosti poti", "hu": "Útvonal részletei", "sk": "Podrobnosti trasy"}


def fix_perkovic():
    for lang in LANGS:
        path = os.path.join(PAGES, "taxi-perkovic", lang, "content.html")
        html = open(path, encoding="utf-8").read()

        # A) add ar-details to the three forward fare rows (book path is
        #    localized per language, so anchor on the &to= token instead)
        for token, fwd_id in FWD:
            url = page_url(fwd_id, lang)
            if not url:
                print("  missing fwd page", fwd_id, lang); continue
            if ('ar-details" href="%s"' % url) in html:
                continue  # already added
            core = '&to=' + token
            idx = html.find(core)
            if idx == -1:
                print("  row anchor missing", token, lang); continue
            a_start = html.rfind('<a class="ar-book"', 0, idx)
            link = '<a class="ar-details" href="%s">%s</a>' % (url, RD[lang])
            html = html[:a_start] + link + html[a_start:]

        # B) add the "both ways" note before the airport arrivals note
        rev_urls = {ph: page_url(pid, lang) for ph, (_, pid) in zip(["SIB", "VOD", "SKR"], REV)}
        if all(rev_urls.values()) and ('href="%s"' % rev_urls["SIB"]) not in html:
            fields = {}
            for ph, (place, _pid) in zip(["SIB", "VOD", "SKR"], REV):
                fields[ph] = '<a href="%s">%s &rarr; Perković</a>' % (rev_urls[ph], place)
            note = '<p class="hub-note hub-note-arrival">' + BOTH[lang].format(**fields) + '</p>'
            lines = html.split("\n")
            for i, ln in enumerate(lines):
                if "hub-note-arrival" in ln:
                    indent = ln[:len(ln) - len(ln.lstrip())]
                    lines.insert(i, indent + note)
                    break
            html = "\n".join(lines)

        open(path, "w", encoding="utf-8").write(html)
        print("perkovic updated:", lang)


if __name__ == "__main__":
    fix_jadrija()
    fix_perkovic()
    print("done")
