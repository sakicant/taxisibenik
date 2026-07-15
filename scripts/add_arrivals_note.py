# -*- coding: utf-8 -*-
"""Add an "Arriving by plane?" note to every service-area (town) page in all
11 languages, making clear the airport routes run in reverse (arrivals), and
linking the reverse airport->town pages where they exist. Idempotent."""
import os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")
LANGS = ["en", "hr", "de", "pl", "cs", "it", "fr", "nl", "sl", "hu", "sk"]

# town slug -> display name (place names are the same across languages)
TOWNS = {
    "bilice": "Bilice", "brodarica": "Brodarica", "jadrija": "Jadrija",
    "zablace": "Zablaće", "zaboric": "Žaborić", "tromilja": "Tromilja",
    "srima": "Srima", "vodice": "Vodice", "lozovac": "Lozovac",
    "perkovic": "Perković", "grebastica": "Grebaštica", "bilo": "Bilo",
    "drnis": "Drniš", "knin": "Knin",
}
# these two have no reverse route pages -> note without links
NO_REVERSE = {"jadrija", "perkovic"}

AIRPORTS = [("split", "Split"), ("zadar", "Zadar"), ("zagreb", "Zagreb"), ("dubrovnik", "Dubrovnik")]

# {TOWN} {SPLIT} {ZADAR} {ZAGREB} {DUBR} placeholders
NOTES = {
    "en": "<strong>Arriving by plane?</strong> Every airport route runs in reverse too. I meet you in the arrivals hall with a name sign, track your flight and drive you straight to {TOWN} for the same fixed price. Book an arrival from {SPLIT}, {ZADAR}, {ZAGREB} or {DUBR} airport.",
    "hr": "<strong>Stižete avionom?</strong> Svaku rutu do zračne luke vozim i u obrnutom smjeru. Dočekam vas u dolascima s natpisom s imenom, pratim vaš let i odvezem vas ravno u {TOWN} po istoj fiksnoj cijeni. Rezervirajte dolazak iz zračne luke {SPLIT}, {ZADAR}, {ZAGREB} ili {DUBR}.",
    "de": "<strong>Sie kommen mit dem Flugzeug an?</strong> Jede Flughafenroute fahre ich auch in umgekehrter Richtung. Ich empfange Sie in der Ankunftshalle mit einem Namensschild, verfolge Ihren Flug und bringe Sie zum selben Festpreis direkt nach {TOWN}. Buchen Sie eine Ankunft ab dem Flughafen {SPLIT}, {ZADAR}, {ZAGREB} oder {DUBR}.",
    "pl": "<strong>Przylatujesz samolotem?</strong> Każdą trasę na lotnisko obsługuję też w drugą stronę. Witam Cię w hali przylotów z tabliczką z nazwiskiem, śledzę Twój lot i zawożę prosto do {TOWN} w tej samej stałej cenie. Zarezerwuj przyjazd z lotniska {SPLIT}, {ZADAR}, {ZAGREB} lub {DUBR}.",
    "cs": "<strong>Přilétáte letadlem?</strong> Každou trasu na letiště jezdím i opačným směrem. Přivítám vás v příletové hale s cedulkou se jménem, sleduji váš let a odvezu vás přímo do {TOWN} za stejnou pevnou cenu. Rezervujte si příjezd z letiště {SPLIT}, {ZADAR}, {ZAGREB} nebo {DUBR}.",
    "it": "<strong>Arrivi in aereo?</strong> Ogni tratta per l'aeroporto la faccio anche al contrario. Ti accolgo nell'area arrivi con un cartello col nome, monitoro il tuo volo e ti porto direttamente a {TOWN} allo stesso prezzo fisso. Prenota un arrivo dall'aeroporto di {SPLIT}, {ZADAR}, {ZAGREB} o {DUBR}.",
    "fr": "<strong>Vous arrivez en avion ?</strong> Chaque trajet vers l'aéroport se fait aussi en sens inverse. Je vous accueille dans le hall des arrivées avec une pancarte à votre nom, je suis votre vol et je vous conduis directement à {TOWN} au même prix fixe. Réservez une arrivée depuis l'aéroport de {SPLIT}, {ZADAR}, {ZAGREB} ou {DUBR}.",
    "nl": "<strong>Komt u met het vliegtuig aan?</strong> Elke luchthavenrit rijd ik ook andersom. Ik ontvang u in de aankomsthal met een naambordje, volg uw vlucht en breng u rechtstreeks naar {TOWN} voor dezelfde vaste prijs. Boek een aankomst vanaf de luchthaven van {SPLIT}, {ZADAR}, {ZAGREB} of {DUBR}.",
    "sl": "<strong>Prihajate z letalom?</strong> Vsako pot do letališča opravim tudi v obratni smeri. Pričakam vas v prihodni dvorani z napisom z imenom, spremljam vaš let in vas po isti fiksni ceni odpeljem naravnost v {TOWN}. Rezervirajte prihod z letališča {SPLIT}, {ZADAR}, {ZAGREB} ali {DUBR}.",
    "hu": "<strong>Repülővel érkezik?</strong> Minden reptéri útvonalat fordított irányban is vállalok. Névtáblával várom az érkezési csarnokban, figyelem a járatát, és ugyanazon a fix áron egyenesen {TOWN} településre viszem. Foglaljon érkezést {SPLIT}, {ZADAR}, {ZAGREB} vagy {DUBR} repülőteréről.",
    "sk": "<strong>Prilietate lietadlom?</strong> Každú trasu na letisko jazdím aj opačným smerom. Privítam vás v príletovej hale s menovkou, sledujem váš let a odveziem vás priamo do {TOWN} za rovnakú pevnú cenu. Rezervujte si príchod z letiska {SPLIT}, {ZADAR}, {ZAGREB} alebo {DUBR}.",
}

ANCHOR = '<p class="hub-note">'


def reverse_url(town, airport_key, lang):
    """Return localized URL for taxi-<airport>-airport-to-<town>, or None."""
    pid = "taxi-%s-airport-to-%s" % (airport_key, town)
    meta = os.path.join(PAGES, pid, lang, "meta.json")
    if not os.path.exists(meta):
        return None
    with open(meta, encoding="utf-8") as f:
        slug = json.load(f)["slug"]
    return "/%s/" % slug if lang == "en" else "/%s/%s/" % (lang, slug)


def build_note(town, lang):
    disp = TOWNS[town]
    fields = {"TOWN": disp}
    linked = town not in NO_REVERSE
    for key, label in AIRPORTS:
        ph = {"split": "SPLIT", "zadar": "ZADAR", "zagreb": "ZAGREB", "dubrovnik": "DUBR"}[key]
        url = reverse_url(town, key, lang) if linked else None
        fields[ph] = '<a href="%s">%s</a>' % (url, label) if url else label
    return '<p class="hub-note hub-note-arrival">' + NOTES[lang].format(**fields) + '</p>'


def run():
    changed = 0
    for town in TOWNS:
        for lang in LANGS:
            path = os.path.join(PAGES, "taxi-%s" % town, lang, "content.html")
            if not os.path.exists(path):
                print("MISSING page:", town, lang)
                continue
            with open(path, encoding="utf-8") as f:
                html = f.read()
            if "hub-note-arrival" in html:
                continue
            idx = html.find(ANCHOR)
            if idx == -1:
                print("NO anchor:", town, lang)
                continue
            line_start = html.rfind("\n", 0, idx) + 1
            indent = html[line_start:idx]
            note = build_note(town, lang)
            html = html[:line_start] + indent + note + "\n" + html[line_start:]
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            changed += 1
    print("inserted notes:", changed)


if __name__ == "__main__":
    run()
