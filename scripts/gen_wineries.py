# -*- coding: utf-8 -*-
"""Winery transfers (transport only, not a tour):
  - Build the "Visit Local Wineries" index page in all 11 languages.
  - Inject a transport-only disclaimer note into the 5 winery route pages.
  - Add the menu item to the Transfers dropdown in every header partial.
Run after gen_routes*.py, before build.py. Idempotent."""
import os, json
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")
PART = os.path.join(ROOT, "src", "partials")
LANGS = ["en", "hr", "de", "pl", "cs", "it", "fr", "nl", "sl", "hu", "sk"]

# name, route page-id, one-way, return, area
WINES = [
    ("Testament Winery", "taxi-sibenik-to-testament-winery", 30, 60, "Šibenik"),
    ("Rak Winery", "taxi-sibenik-to-rak-winery", 25, 50, "Dubrava"),
    ("Baraka Winery", "taxi-sibenik-to-baraka-winery", 30, 60, "Šibenik &ndash; Vodice"),
    ("Sladić Winery", "taxi-sibenik-to-sladic-winery", 60, 120, "Plastovo"),
    ("Bibich Winery", "taxi-sibenik-to-bibich-winery", 60, 120, "Plastovo"),
]

SLUG = {"en": "winery-transfers-from-sibenik", "hr": "transferi-do-vinarija",
        "de": "weingut-transfers-sibenik", "pl": "transfery-do-winnic",
        "cs": "transfery-do-vinarstvi", "it": "transfer-per-le-cantine",
        "fr": "transferts-vers-les-vignobles", "nl": "wijnhuis-transfers",
        "sl": "prevozi-do-vinarij", "hu": "pinceszet-transzferek",
        "sk": "transfery-do-vinarstiev"}
MENU = {"en": "Visit Local Wineries", "hr": "Posjetite lokalne vinarije",
        "de": "Lokale Weingüter besuchen", "pl": "Odwiedź lokalne winnice",
        "cs": "Navštivte místní vinařství", "it": "Visita le cantine locali",
        "fr": "Visiter les vignobles locaux", "nl": "Lokale wijnhuizen bezoeken",
        "sl": "Obiščite lokalne vinarije", "hu": "Helyi pincészetek",
        "sk": "Navštívte miestne vinárstva"}
CONTACT = {"en": "contact", "hr": "kontakt", "de": "kontakt", "pl": "kontakt",
           "cs": "kontakt", "it": "contatti", "fr": "contact", "nl": "contact",
           "sl": "kontakt", "hu": "kapcsolat", "sk": "kontakt"}


def url(lang, slug):
    return "/%s/" % slug if lang == "en" else "/%s/%s/" % (lang, slug)


def route_url(page_id, lang):
    meta = os.path.join(PAGES, page_id, lang, "meta.json")
    slug = json.load(open(meta, encoding="utf-8"))["slug"]
    return url(lang, slug)


L = {
 "en": dict(eyebrow="Winery Transfers", h1="Visit Local Wineries",
   sub="Fixed-price taxi transfers to the wineries around Šibenik and Skradin. I drive, you taste.",
   intro_h2="Transport to the Wineries, Nothing More",
   intro_p1="Fancy an afternoon at the local wineries but do not want to worry about driving? I take you there and bring you back at a fixed price, so everyone in the car can taste freely.",
   disclaimer="To be clear, I sell the transport only. I am glad to point you to good wineries and help you plan the day, but I am a driver, not a tour agency, and I never charge for advice or tastings. You arrange your own visits; I get you there and home safely.",
   grid_h2="Wineries and Fixed Fares from Šibenik", grid_sub="Price per car, up to 4 passengers, luggage included. One way, and the full round trip.",
   ow="one way", rt="return", details="View route &amp; book",
   other="Staying somewhere other than Šibenik? I can pick you up from most local towns too, at a fixed price. Just message me for the fare.",
   cta_h2="Plan Your Winery Trip", cta_sub="Tell me the winery, the day and how many of you, and I will confirm a fixed price.",
   wa="Message me on WhatsApp", contact="Contact me",
   mtitle="Winery Transfers from Šibenik | Fixed Prices | TAXI Antonio",
   mdesc="Fixed-price taxi transfers from Šibenik to local wineries (Testament, Rak, Baraka, Sladić, Bibich). Transport only, one way or return. Book direct.",
   mkw="winery transfer sibenik, taxi to winery sibenik, bibich winery taxi, testament winery transfer",
   note="Transport only: I drive you to the winery and back at a fixed price. Glad to share local tips, but I am a driver, not a tour agency, and I never charge for advice or tastings."),
 "hr": dict(eyebrow="Transferi do vinarija", h1="Posjetite lokalne vinarije",
   sub="Transferi po fiksnoj cijeni do vinarija oko Šibenika i Skradina. Ja vozim, vi kušate.",
   intro_h2="Prijevoz do vinarija, ništa više",
   intro_p1="Želite popodne u lokalnim vinarijama, ali ne želite brinuti o vožnji? Odvezem vas i vratim po fiksnoj cijeni, tako da svi u autu mogu slobodno kušati.",
   disclaimer="Da bude jasno, prodajem isključivo prijevoz. Rado ću vam preporučiti dobre vinarije i pomoći isplanirati dan, ali ja sam vozač, a ne turistička agencija, i nikada ne naplaćujem savjete ni kušanja. Posjete dogovarate sami; ja vas sigurno odvezem i vratim.",
   grid_h2="Vinarije i fiksne cijene iz Šibenika", grid_sub="Cijena po vozilu, do 4 putnika, prtljaga uključena. U jednom smjeru i povratno.",
   ow="u jednom smjeru", rt="povratno", details="Pogledaj rutu i rezerviraj",
   other="Odsjedate izvan Šibenika? Mogu vas pokupiti i iz većine lokalnih mjesta, po fiksnoj cijeni. Samo mi javite za cijenu.",
   cta_h2="Isplanirajte posjet vinarijama", cta_sub="Recite mi vinariju, dan i koliko vas je, i potvrdit ću fiksnu cijenu.",
   wa="Pošaljite poruku na WhatsApp", contact="Kontaktirajte me",
   mtitle="Transferi do vinarija iz Šibenika | Fiksne cijene | TAXI Antonio",
   mdesc="Transferi po fiksnoj cijeni iz Šibenika do lokalnih vinarija (Testament, Rak, Baraka, Sladić, Bibich). Samo prijevoz, u jednom smjeru ili povratno.",
   mkw="transfer vinarija šibenik, taxi do vinarije šibenik, bibich vinarija taxi",
   note="Samo prijevoz: odvezem vas do vinarije i natrag po fiksnoj cijeni. Rado dijelim lokalne savjete, ali ja sam vozač, a ne turistička agencija, i nikada ne naplaćujem savjete ni kušanja."),
 "de": dict(eyebrow="Weingut-Transfers", h1="Lokale Weingüter besuchen",
   sub="Taxitransfers zum Festpreis zu den Weingütern rund um Šibenik und Skradin. Ich fahre, Sie genießen.",
   intro_h2="Nur der Transport zu den Weingütern",
   intro_p1="Lust auf einen Nachmittag bei den lokalen Weingütern, aber keine Lust aufs Fahren? Ich bringe Sie zum Festpreis hin und zurück, damit alle im Auto in Ruhe probieren können.",
   disclaimer="Um es klar zu sagen: Ich verkaufe ausschließlich den Transport. Gern empfehle ich Ihnen gute Weingüter und helfe bei der Planung, aber ich bin Fahrer, kein Reiseveranstalter, und berechne nie etwas für Tipps oder Verkostungen. Die Besuche organisieren Sie selbst; ich bringe Sie sicher hin und zurück.",
   grid_h2="Weingüter und Festpreise ab Šibenik", grid_sub="Preis pro Fahrzeug, bis zu 4 Personen, Gepäck inklusive. Einfach und hin und zurück.",
   ow="einfach", rt="hin &amp; zurück", details="Strecke ansehen &amp; buchen",
   other="Sie wohnen nicht in Šibenik? Ich hole Sie auch aus den meisten Orten der Umgebung ab, zum Festpreis. Fragen Sie einfach nach dem Preis.",
   cta_h2="Planen Sie Ihre Weingut-Tour", cta_sub="Nennen Sie mir das Weingut, den Tag und die Personenzahl, und ich bestätige einen Festpreis.",
   wa="Auf WhatsApp schreiben", contact="Kontakt aufnehmen",
   mtitle="Weingut-Transfers ab Šibenik | Festpreise | TAXI Antonio",
   mdesc="Taxitransfers zum Festpreis von Šibenik zu lokalen Weingütern (Testament, Rak, Baraka, Sladić, Bibich). Nur Transport, einfach oder hin und zurück.",
   mkw="weingut transfer šibenik, taxi weingut šibenik, bibich weingut taxi",
   note="Nur Transport: Ich fahre Sie zum Festpreis zum Weingut und zurück. Gern gebe ich lokale Tipps, aber ich bin Fahrer, kein Reiseveranstalter, und berechne nie etwas für Tipps oder Verkostungen."),
 "pl": dict(eyebrow="Transfery do winnic", h1="Odwiedź lokalne winnice",
   sub="Transfery taxi w stałej cenie do winnic wokół Šibenika i Skradina. Ja prowadzę, ty degustujesz.",
   intro_h2="Tylko transport do winnic",
   intro_p1="Masz ochotę na popołudnie w lokalnych winnicach, ale nie chcesz martwić się prowadzeniem? Zawiozę i przywiozę Cię w stałej cenie, żeby wszyscy w aucie mogli swobodnie degustować.",
   disclaimer="Dla jasności: sprzedaję wyłącznie transport. Chętnie polecę dobre winnice i pomogę zaplanować dzień, ale jestem kierowcą, a nie biurem podróży, i nigdy nie pobieram opłat za porady ani degustacje. Wizyty organizujesz samodzielnie; ja bezpiecznie Cię dowożę i odwożę.",
   grid_h2="Winnice i stałe ceny z Šibenika", grid_sub="Cena za samochód, do 4 osób, bagaż wliczony. W jedną stronę i w obie strony.",
   ow="w jedną stronę", rt="w obie strony", details="Zobacz trasę i zarezerwuj",
   other="Mieszkasz poza Šibenikiem? Mogę odebrać Cię również z większości okolicznych miejscowości, w stałej cenie. Napisz po wycenę.",
   cta_h2="Zaplanuj wizytę w winnicach", cta_sub="Podaj winnicę, dzień i liczbę osób, a potwierdzę stałą cenę.",
   wa="Napisz na WhatsApp", contact="Skontaktuj się ze mną",
   mtitle="Transfery do winnic z Šibenika | Stałe ceny | TAXI Antonio",
   mdesc="Transfery taxi w stałej cenie z Šibenika do lokalnych winnic (Testament, Rak, Baraka, Sladić, Bibich). Tylko transport, w jedną lub w obie strony.",
   mkw="transfer winnica šibenik, taxi do winnicy šibenik, bibich winnica taxi",
   note="Tylko transport: zawożę Cię do winnicy i z powrotem w stałej cenie. Chętnie podzielę się lokalnymi wskazówkami, ale jestem kierowcą, a nie biurem podróży, i nigdy nie pobieram opłat za porady ani degustacje."),
 "cs": dict(eyebrow="Transfery do vinařství", h1="Navštivte místní vinařství",
   sub="Taxi transfery za pevnou cenu do vinařství kolem Šibeniku a Skradinu. Já řídím, vy ochutnáváte.",
   intro_h2="Jen doprava do vinařství",
   intro_p1="Máte chuť na odpoledne v místních vinařstvích, ale nechcete řešit řízení? Odvezu vás tam i zpět za pevnou cenu, aby si všichni v autě mohli v klidu ochutnat.",
   disclaimer="Aby bylo jasno: prodávám pouze dopravu. Rád doporučím dobrá vinařství a pomůžu naplánovat den, ale jsem řidič, ne cestovní kancelář, a za rady ani degustace si nikdy neúčtuji. Návštěvy si domlouváte sami; já vás bezpečně odvezu a přivezu.",
   grid_h2="Vinařství a pevné ceny ze Šibeniku", grid_sub="Cena za vůz, až 4 osoby, zavazadla v ceně. Jednosměrně i tam a zpět.",
   ow="jednosměrně", rt="tam a zpět", details="Zobrazit trasu a rezervovat",
   other="Bydlíte jinde než v Šibeniku? Vyzvednu vás i ve většině okolních míst, za pevnou cenu. Napište si o cenu.",
   cta_h2="Naplánujte návštěvu vinařství", cta_sub="Řekněte mi vinařství, den a počet osob, a potvrdím pevnou cenu.",
   wa="Napište na WhatsApp", contact="Kontaktujte mě",
   mtitle="Transfery do vinařství ze Šibeniku | Pevné ceny | TAXI Antonio",
   mdesc="Taxi transfery za pevnou cenu ze Šibeniku do místních vinařství (Testament, Rak, Baraka, Sladić, Bibich). Jen doprava, jednosměrně nebo tam a zpět.",
   mkw="transfer vinařství šibenik, taxi do vinařství šibenik, bibich vinařství taxi",
   note="Jen doprava: odvezu vás do vinařství a zpět za pevnou cenu. Rád poradím, ale jsem řidič, ne cestovní kancelář, a za rady ani degustace si nikdy neúčtuji."),
 "it": dict(eyebrow="Transfer per le cantine", h1="Visita le cantine locali",
   sub="Transfer in taxi a prezzo fisso verso le cantine intorno a Šibenik e Skradin. Io guido, tu degusti.",
   intro_h2="Solo il trasporto alle cantine",
   intro_p1="Voglia di un pomeriggio nelle cantine locali senza pensare alla guida? Ti porto e ti riporto a prezzo fisso, così tutti in auto possono degustare in tranquillità.",
   disclaimer="Per chiarezza: vendo solo il trasporto. Volentieri ti indico buone cantine e ti aiuto a organizzare la giornata, ma sono un autista, non un'agenzia turistica, e non faccio mai pagare consigli o degustazioni. Le visite le organizzi tu; io ti porto e ti riporto in sicurezza.",
   grid_h2="Cantine e prezzi fissi da Šibenik", grid_sub="Prezzo per auto, fino a 4 passeggeri, bagagli inclusi. Solo andata e andata e ritorno.",
   ow="solo andata", rt="andata e ritorno", details="Vedi tratta e prenota",
   other="Alloggi fuori Šibenik? Posso venire a prenderti anche nella maggior parte dei paesi vicini, a prezzo fisso. Scrivimi per il prezzo.",
   cta_h2="Organizza la tua visita alle cantine", cta_sub="Dimmi la cantina, il giorno e in quanti siete, e ti confermo un prezzo fisso.",
   wa="Scrivimi su WhatsApp", contact="Contattami",
   mtitle="Transfer per le cantine da Šibenik | Prezzi fissi | TAXI Antonio",
   mdesc="Transfer in taxi a prezzo fisso da Šibenik alle cantine locali (Testament, Rak, Baraka, Sladić, Bibich). Solo trasporto, solo andata o andata e ritorno.",
   mkw="transfer cantina šibenik, taxi cantina šibenik, bibich cantina taxi",
   note="Solo trasporto: ti porto in cantina e ti riporto a prezzo fisso. Volentieri condivido consigli locali, ma sono un autista, non un'agenzia turistica, e non faccio mai pagare consigli o degustazioni."),
 "fr": dict(eyebrow="Transferts vignobles", h1="Visiter les vignobles locaux",
   sub="Transferts en taxi à prix fixe vers les vignobles autour de Šibenik et Skradin. Je conduis, vous dégustez.",
   intro_h2="Seulement le transport vers les vignobles",
   intro_p1="Envie d'un après-midi dans les vignobles locaux sans vous soucier de la conduite ? Je vous emmène et vous ramène à prix fixe, pour que tout le monde puisse déguster tranquillement.",
   disclaimer="Pour être clair : je vends uniquement le transport. Je vous conseille volontiers de bons vignobles et vous aide à planifier la journée, mais je suis chauffeur, pas agence de voyage, et je ne facture jamais les conseils ni les dégustations. Vous organisez vos visites ; je vous emmène et vous ramène en sécurité.",
   grid_h2="Vignobles et prix fixes depuis Šibenik", grid_sub="Prix par voiture, jusqu'à 4 passagers, bagages inclus. Aller simple et aller-retour.",
   ow="aller simple", rt="aller-retour", details="Voir le trajet et réserver",
   other="Vous logez hors de Šibenik ? Je peux aussi venir vous chercher dans la plupart des villages voisins, à prix fixe. Écrivez-moi pour le tarif.",
   cta_h2="Planifiez votre visite des vignobles", cta_sub="Dites-moi le vignoble, le jour et combien vous êtes, et je confirme un prix fixe.",
   wa="Écrivez-moi sur WhatsApp", contact="Contactez-moi",
   mtitle="Transferts vers les vignobles depuis Šibenik | Prix fixes | TAXI Antonio",
   mdesc="Transferts en taxi à prix fixe depuis Šibenik vers les vignobles locaux (Testament, Rak, Baraka, Sladić, Bibich). Transport uniquement, aller ou aller-retour.",
   mkw="transfert vignoble šibenik, taxi vignoble šibenik, bibich vignoble taxi",
   note="Transport uniquement : je vous conduis au vignoble et vous ramène à prix fixe. Je partage volontiers des conseils locaux, mais je suis chauffeur, pas agence de voyage, et je ne facture jamais les conseils ni les dégustations."),
 "nl": dict(eyebrow="Wijnhuis-transfers", h1="Lokale wijnhuizen bezoeken",
   sub="Taxitransfers tegen vaste prijs naar de wijnhuizen rond Šibenik en Skradin. Ik rijd, u proeft.",
   intro_h2="Alleen het vervoer naar de wijnhuizen",
   intro_p1="Zin in een middag bij de lokale wijnhuizen, maar geen zin om te rijden? Ik breng u er tegen een vaste prijs heen en weer, zodat iedereen in de auto rustig kan proeven.",
   disclaimer="Voor de duidelijkheid: ik verkoop alleen het vervoer. Ik wijs u graag goede wijnhuizen aan en help de dag plannen, maar ik ben chauffeur, geen reisbureau, en reken nooit iets voor advies of proeverijen. De bezoeken regelt u zelf; ik breng u veilig heen en terug.",
   grid_h2="Wijnhuizen en vaste prijzen vanaf Šibenik", grid_sub="Prijs per auto, tot 4 passagiers, bagage inbegrepen. Enkele reis en heen en terug.",
   ow="enkele reis", rt="heen en terug", details="Route bekijken en boeken",
   other="Verblijft u buiten Šibenik? Ik haal u ook op in de meeste plaatsen in de buurt, tegen een vaste prijs. Stuur me even een bericht voor de prijs.",
   cta_h2="Plan uw wijnhuisbezoek", cta_sub="Vertel me het wijnhuis, de dag en met hoeveel u bent, dan bevestig ik een vaste prijs.",
   wa="Stuur me een WhatsApp", contact="Neem contact op",
   mtitle="Wijnhuis-transfers vanaf Šibenik | Vaste prijzen | TAXI Antonio",
   mdesc="Taxitransfers tegen vaste prijs van Šibenik naar lokale wijnhuizen (Testament, Rak, Baraka, Sladić, Bibich). Alleen vervoer, enkele reis of heen en terug.",
   mkw="wijnhuis transfer šibenik, taxi wijnhuis šibenik, bibich wijnhuis taxi",
   note="Alleen vervoer: ik breng u tegen een vaste prijs naar het wijnhuis en terug. Ik deel graag lokale tips, maar ik ben chauffeur, geen reisbureau, en reken nooit iets voor advies of proeverijen."),
 "sl": dict(eyebrow="Prevozi do vinarij", h1="Obiščite lokalne vinarije",
   sub="Taksi prevozi po fiksni ceni do vinarij okoli Šibenika in Skradina. Jaz vozim, vi pokušate.",
   intro_h2="Samo prevoz do vinarij",
   intro_p1="Bi radi popoldne v lokalnih vinarijah, a se ne želite ukvarjati z vožnjo? Odpeljem vas tja in nazaj po fiksni ceni, da lahko vsi v avtu mirno pokušajo.",
   disclaimer="Da bo jasno: prodajam le prevoz. Z veseljem vam priporočim dobre vinarije in pomagam načrtovati dan, a sem voznik, ne turistična agencija, in nasvetov ali degustacij nikoli ne zaračunam. Obiske uredite sami; jaz vas varno odpeljem in pripeljem nazaj.",
   grid_h2="Vinarije in fiksne cene iz Šibenika", grid_sub="Cena na vozilo, do 4 potnike, prtljaga vključena. V eno smer in povratno.",
   ow="v eno smer", rt="povratno", details="Poglej pot in rezerviraj",
   other="Bivate izven Šibenika? Poberem vas lahko tudi v večini okoliških krajev, po fiksni ceni. Le pišite mi za ceno.",
   cta_h2="Načrtujte obisk vinarij", cta_sub="Povejte mi vinarijo, dan in koliko vas je, in potrdim fiksno ceno.",
   wa="Pišite mi na WhatsApp", contact="Kontaktirajte me",
   mtitle="Prevozi do vinarij iz Šibenika | Fiksne cene | TAXI Antonio",
   mdesc="Taksi prevozi po fiksni ceni iz Šibenika do lokalnih vinarij (Testament, Rak, Baraka, Sladić, Bibich). Samo prevoz, v eno smer ali povratno.",
   mkw="prevoz vinarija šibenik, taksi vinarija šibenik, bibich vinarija taksi",
   note="Samo prevoz: odpeljem vas do vinarije in nazaj po fiksni ceni. Z veseljem delim lokalne nasvete, a sem voznik, ne turistična agencija, in nasvetov ali degustacij nikoli ne zaračunam."),
 "hu": dict(eyebrow="Pincészet-transzferek", h1="Helyi pincészetek meglátogatása",
   sub="Fix áras taxitranszferek a Šibenik és Skradin környéki pincészetekhez. Én vezetek, Ön kóstol.",
   intro_h2="Csak a fuvar a pincészetekhez",
   intro_p1="Kedve van egy délutánhoz a helyi pincészetekben, de nem szeretne vezetni? Fix áron odaviszem és vissza is hozom, hogy az autóban mindenki nyugodtan kóstolhasson.",
   disclaimer="Hogy világos legyen: kizárólag a fuvart adom el. Szívesen ajánlok jó pincészeteket és segítek megtervezni a napot, de sofőr vagyok, nem utazási iroda, és a tanácsért vagy kóstolásért soha nem kérek pénzt. A látogatásokat Ön szervezi; én biztonságosan odaviszem és hazahozom.",
   grid_h2="Pincészetek és fix árak Šibenikből", grid_sub="Ár autónként, legfeljebb 4 utas, csomag beleértve. Egy útra és oda-vissza.",
   ow="egy út", rt="oda-vissza", details="Útvonal és foglalás",
   other="Nem Šibenikben lakik? A legtöbb környező településről is elhozom, fix áron. Csak írjon az árért.",
   cta_h2="Tervezze meg a pincészeti látogatást", cta_sub="Mondja meg a pincészetet, a napot és hányan vannak, és megerősítem a fix árat.",
   wa="Írjon WhatsAppon", contact="Írjon nekem",
   mtitle="Pincészet-transzferek Šibenikből | Fix árak | TAXI Antonio",
   mdesc="Fix áras taxitranszferek Šibenikből helyi pincészetekhez (Testament, Rak, Baraka, Sladić, Bibich). Csak fuvar, egy útra vagy oda-vissza.",
   mkw="pincészet transzfer šibenik, taxi pincészet šibenik, bibich pincészet taxi",
   note="Csak fuvar: fix áron odaviszem a pincészethez és vissza. Szívesen adok helyi tippeket, de sofőr vagyok, nem utazási iroda, és a tanácsért vagy kóstolásért soha nem kérek pénzt."),
 "sk": dict(eyebrow="Transfery do vinárstiev", h1="Navštívte miestne vinárstva",
   sub="Taxi transfery za pevnú cenu do vinárstiev okolo Šibeniku a Skradinu. Ja šoférujem, vy ochutnávate.",
   intro_h2="Len doprava do vinárstiev",
   intro_p1="Máte chuť na popoludnie v miestnych vinárstvach, ale nechcete riešiť šoférovanie? Odveziem vás tam aj späť za pevnú cenu, aby si všetci v aute mohli v pokoji ochutnať.",
   disclaimer="Aby bolo jasno: predávam len dopravu. Rád odporučím dobré vinárstva a pomôžem naplánovať deň, ale som vodič, nie cestovná kancelária, a za rady ani ochutnávky si nikdy neúčtujem. Návštevy si dohodnete sami; ja vás bezpečne odveziem a priveziem.",
   grid_h2="Vinárstva a pevné ceny zo Šibeniku", grid_sub="Cena za vozidlo, až 4 osoby, batožina v cene. Jednosmerne aj tam a späť.",
   ow="jednosmerne", rt="tam a späť", details="Zobraziť trasu a rezervovať",
   other="Bývate mimo Šibeniku? Vyzdvihnem vás aj vo väčšine okolitých obcí, za pevnú cenu. Napíšte si o cenu.",
   cta_h2="Naplánujte návštevu vinárstiev", cta_sub="Povedzte mi vinárstvo, deň a koľko vás je, a potvrdím pevnú cenu.",
   wa="Napíšte na WhatsApp", contact="Kontaktujte ma",
   mtitle="Transfery do vinárstiev zo Šibeniku | Pevné ceny | TAXI Antonio",
   mdesc="Taxi transfery za pevnú cenu zo Šibeniku do miestnych vinárstiev (Testament, Rak, Baraka, Sladić, Bibich). Len doprava, jednosmerne alebo tam a späť.",
   mkw="transfer vinárstvo šibenik, taxi vinárstvo šibenik, bibich vinárstvo taxi",
   note="Len doprava: odveziem vás do vinárstva a späť za pevnú cenu. Rád poradím, ale som vodič, nie cestovná kancelária, a za rady ani ochutnávky si nikdy neúčtujem."),
}


def rows_html(lang, d):
    out = []
    for name, pid, ow, rt, area in WINES:
        u = route_url(pid, lang)
        out.append(
            '        <div class="airport-route">\n'
            '          <div class="ar-info"><span class="ar-name">%s &middot; %s</span>'
            '<span class="ar-price">&euro;%d <small>%s</small> &middot; &euro;%d <small>%s</small></span></div>\n'
            '          <div class="ar-actions"><a class="ar-details" href="%s">%s</a></div>\n'
            '        </div>' % (name, area, ow, d["ow"], rt, d["rt"], u, d["details"]))
    return "\n".join(out)


def build_index():
    for lang in LANGS:
        d = L[lang]
        wa = "https://wa.me/385994471013?text=" + quote(
            "Hi Antonio, I would like a taxi to a local winery. My details:\n- Winery: \n- Pickup date: \n- Pickup time: \n- Passengers: \n- Pickup address: \n- My name: ")
        content = '''  <section class="page-hero">
    <div class="container">
      <span class="eyebrow">%s</span>
      <h1>%s</h1>
      <p class="page-hero-sub">%s</p>
    </div>
  </section>

  <section class="page-content">
    <div class="container prose">
      <h2>%s</h2>
      <p>%s</p>
      <p>%s</p>
    </div>
  </section>

  <section class="hub-routes">
    <div class="container">
      <h2 class="section-title">%s</h2>
      <p class="section-subtitle">%s</p>
      <div class="airport-route-grid">
%s
      </div>
      <p class="hub-note hub-note-arrival">%s</p>
    </div>
  </section>

  <section class="daytrip-cta">
    <div class="container">
      <h2 class="section-title">%s</h2>
      <p class="section-subtitle">%s</p>
      <div class="hero-actions">
        <a href="%s" target="_blank" rel="noopener" class="btn btn-primary">%s</a>
        <a href="%s" class="btn btn-secondary">%s</a>
      </div>
    </div>
  </section>
''' % (d["eyebrow"], d["h1"], d["sub"], d["intro_h2"], d["intro_p1"], d["disclaimer"],
       d["grid_h2"], d["grid_sub"], rows_html(lang, d), d["other"],
       d["cta_h2"], d["cta_sub"], wa, d["wa"], url(lang, CONTACT[lang]), d["contact"])

        outdir = os.path.join(PAGES, "winery-transfers", lang)
        os.makedirs(outdir, exist_ok=True)
        meta = {"slug": SLUG[lang], "title": d["mtitle"], "description": d["mdesc"],
                "keywords": d["mkw"],
                "og_image": "https://taxisibenik.hr/assets/img/hero-transfers.webp", "schema": None}
        json.dump(meta, open(os.path.join(outdir, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(os.path.join(outdir, "content.html"), "w", encoding="utf-8").write(content)
        print("index:", lang, SLUG[lang])


def inject_disclaimer():
    for name, pid, ow, rt, area in WINES:
        for lang in LANGS:
            p = os.path.join(PAGES, pid, lang, "content.html")
            html = open(p, encoding="utf-8").read()
            if "winery-disclaimer" in html:
                continue
            anchor = '<p class="hub-note">'
            i = html.find(anchor)
            if i == -1:
                print("  no anchor", pid, lang); continue
            ls = html.rfind("\n", 0, i) + 1
            indent = html[ls:i]
            note = '%s<p class="hub-note hub-note-arrival winery-disclaimer">%s</p>\n' % (indent, L[lang]["note"])
            html = html[:ls] + note + html[ls:]
            open(p, "w", encoding="utf-8").write(html)
    print("disclaimer injected into route pages")


def add_menu():
    for lang in LANGS:
        fname = "header.html" if lang == "en" else "header.%s.html" % lang
        path = os.path.join(PART, fname)
        html = open(path, encoding="utf-8").read()
        u = url(lang, SLUG[lang])
        if u in html:
            print("menu already:", lang); continue
        # insert after the Marina Zaton transfers link (last item in Transfers menu)
        marker = "marina-zaton-transfers"
        mi = html.find(marker)
        if mi == -1:
            print("  no marina-zaton anchor:", lang); continue
        line_end = html.find("\n", mi)
        indent = "          "
        link = '\n%s<a href="%s">%s</a>' % (indent, u, MENU[lang])
        html = html[:line_end] + link + html[line_end:]
        open(path, "w", encoding="utf-8").write(html)
        print("menu added:", lang)


if __name__ == "__main__":
    build_index()
    inject_disclaimer()
    add_menu()
    print("done")
