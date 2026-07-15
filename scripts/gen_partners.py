# -*- coding: utf-8 -*-
"""Generate the /partners/ page in all 11 languages, add the footer
"Become a partner" link, and add a "Partnership proposal" topic option to the
contact + home forms. Idempotent: safe to run more than once.
"""
import os, json, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")
PARTIALS = os.path.join(ROOT, "src", "partials")

LANGS = ["en", "hr", "de", "pl", "cs", "it", "fr", "nl", "sl", "hu", "sk"]

SLUG = {"en": "partners", "hr": "partneri", "de": "partner", "pl": "partnerzy",
        "cs": "partneri", "it": "partner", "fr": "partenaires", "nl": "partners",
        "sl": "partnerji", "hu": "partnerek", "sk": "partneri"}
CONTACT = {"en": "contact", "hr": "kontakt", "de": "kontakt", "pl": "kontakt",
           "cs": "kontakt", "it": "contatti", "fr": "contact", "nl": "contact",
           "sl": "kontakt", "hu": "kapcsolat", "sk": "kontakt"}
BECOME = {"en": "Become a partner", "hr": "Postanite partner", "de": "Partner werden",
          "pl": "Zostań partnerem", "cs": "Staňte se partnerem", "it": "Diventa partner",
          "fr": "Devenir partenaire", "nl": "Word partner", "sl": "Postanite partner",
          "hu": "Legyen partnerünk", "sk": "Staňte sa partnerom"}
TOPIC = {"en": "Partnership proposal", "hr": "Prijedlog za suradnju",
         "de": "Partnerschaftsanfrage", "pl": "Propozycja współpracy",
         "cs": "Návrh spolupráce", "it": "Proposta di collaborazione",
         "fr": "Proposition de partenariat", "nl": "Samenwerkingsvoorstel",
         "sl": "Predlog za sodelovanje", "hu": "Együttműködési ajánlat",
         "sk": "Návrh spolupráce"}


def page_url(lang, slug):
    return "/%s/" % slug if lang == "en" else "/%s/%s/" % (lang, slug)


# ---------------------------------------------------------------- translations
L = {}

L["en"] = dict(
    hero_eyebrow="Partnerships", hero_h1="Become a Partner",
    hero_sub="A reliable local driver for your guests, clients and travellers on the Šibenik coast.",
    intro_h2="One Driver You Can Count On",
    intro_p1="I am Antonio, a local taxi and transfer driver based between Šibenik and Skradin. If you send people to this part of Dalmatia, you need someone on the ground who shows up on time, answers the phone, and treats your guests the way you would. That is what I do, every trip, personally.",
    intro_p2="I work with three kinds of partners. If you are one of them, I would like to hear from you.",
    who_eyebrow="Who I Work With", who_h2="Three Kinds of Partners",
    t1_h3="Travel Agents",
    t1_p="Foreign or local, if you book transfers and day trips for your clients, I am your driver on the Šibenik coast. Fixed prices, clear confirmations, and one person who answers you directly. No call centre in between.",
    t2_h3="Apartment &amp; Villa Owners",
    t2_p="Renting to guests and want their arrival to go smoothly? I collect them from the airport, get them to your door, and take them back at the end. Your guests start and end their stay relaxed, and you look after them from the very first minute.",
    t3_h3="Agencies",
    t3_p="Local and foreign agencies that need a dependable transport provider on this coast: I cover airport transfers, city-to-city runs and day trips, with one point of contact from the first message to the drop-off.",
    villa1_eyebrow="For Apartment &amp; Villa Owners",
    villa1_h2="Your Guests, Looked After Door to Door",
    villa1_p1="When a family lands after a long flight, the last thing they want is to hunt for a ride. Give them my details, or send me their arrival, and I meet them with a name sign, load the luggage, and drive them straight to your property.",
    villa1_p2="At the end of the stay I take them back to the airport in good time. It is one less thing for you to arrange, and it makes your place the one they recommend to friends.",
    villa1_alt="Holiday villa with a garden near Šibenik, the kind of property whose owners partner with TAXI Antonio for guest transfers",
    car_eyebrow="A Clean, Comfortable Car", car_h2="A Professional Ride, Every Time",
    car_p1="Your guests travel in a clean, air-conditioned Škoda Superb with room for up to four passengers and their luggage, plus free Wi-Fi on board. For larger groups I arrange a van through a trusted colleague and stay your single point of contact throughout.",
    car_p2="I have driven professionally for over ten years, along this coast and on winter airport transfers in Austria. Your guests are in experienced hands.",
    villa2_alt="Comfortable bedroom in a holiday villa near Šibenik served by TAXI Antonio guest transfers",
    why_eyebrow="Why Partner With Me", why_h2="What You Get",
    b1_h3="One Point of Contact", b1_p="You deal with me, not a rota of strangers. I answer messages personally, confirm directly, and take responsibility if anything comes up.",
    b2_h3="Fixed, Honest Prices", b2_p="Clear prices agreed up front, so you and your clients always know the cost. No surprises at the end of the ride.",
    b3_h3="On Time, Every Time", b3_p="I monitor flights, plan around ferries and buses, and build in the time to get your people where they need to be without a rush.",
    b4_h3="A Trusted Network", b4_p="When I am already booked or you need a bigger vehicle, I bring in hand-picked colleagues I know personally, and I always tell you who and why.",
    b5_h3="Local Knowledge", b5_p="I was born here and know these roads, towns and marinas inside out, from Zadar to Split and everywhere between.",
    b6_h3="Guests Treated Like Friends", b6_p="Your reputation rides with every guest. I look after them the way you would, so they come back to you.",
    note_h2="A Note for Fellow Drivers",
    note_p="I am not currently looking for partnerships with other taxi and transfer providers. I still hand-pick the colleagues I work with personally, one by one, and that network is settled for now. If that changes, I will say so here.",
    talk_h2="Let's Talk",
    talk_pre="If you are a travel agent, an apartment or villa owner, or an agency and you would like to work together, send me an email. Tell me who you are and what you need, and choose ",
    talk_suf=" as the topic so I know to reply quickly.",
    email_word="Email", cta_btn="Contact Me",
    meta_title="Become a Partner | TAXI Antonio Šibenik",
    meta_description="Travel agents, apartment and villa owners, and agencies: partner with a reliable local Šibenik driver for airport transfers, day trips and guest transport.",
    meta_keywords="sibenik taxi partner, transfer partner sibenik, villa guest transfers, travel agent transport dalmatia",
)

L["hr"] = dict(
    hero_eyebrow="Suradnja", hero_h1="Postanite partner",
    hero_sub="Pouzdan lokalni vozač za vaše goste, klijente i putnike na šibenskoj obali.",
    intro_h2="Jedan vozač na kojeg se možete osloniti",
    intro_p1="Ja sam Antonio, lokalni taksist i vozač transfera između Šibenika i Skradina. Ako šaljete ljude u ovaj dio Dalmacije, treba vam netko na terenu tko dolazi na vrijeme, javlja se na telefon i prema vašim gostima se ponaša kao što biste i vi. Upravo to radim, na svakoj vožnji, osobno.",
    intro_p2="Surađujem s tri vrste partnera. Ako ste jedan od njih, javite mi se.",
    who_eyebrow="S kim surađujem", who_h2="Tri vrste partnera",
    t1_h3="Putničke agencije",
    t1_p="Strane ili domaće, ako rezervirate transfere i izlete za svoje klijente, ja sam vaš vozač na šibenskoj obali. Fiksne cijene, jasne potvrde i jedna osoba koja vam odgovara izravno. Bez pozivnog centra u sredini.",
    t2_h3="Vlasnici apartmana i vila",
    t2_p="Iznajmljujete gostima i želite da im dolazak prođe glatko? Dočekam ih u zračnoj luci, dovezem do vaših vrata i vratim na kraju boravka. Vaši gosti počinju i završavaju odmor opušteno, a vi brinete o njima od prve minute.",
    t3_h3="Agencije",
    t3_p="Domaće i strane agencije kojima treba pouzdan prijevoznik na ovoj obali: pokrivam transfere do zračnih luka, međugradske vožnje i izlete, uz jednu kontakt osobu od prve poruke do dolaska.",
    villa1_eyebrow="Za vlasnike apartmana i vila",
    villa1_h2="Vaši gosti, zbrinuti od vrata do vrata",
    villa1_p1="Kad obitelj sleti nakon dugog leta, zadnje što žele je tražiti prijevoz. Dajte im moje podatke ili mi javite njihov dolazak, dočekam ih s natpisom s imenom, utovarim prtljagu i odvezem ih ravno do vašeg objekta.",
    villa1_p2="Na kraju boravka vratim ih u zračnu luku na vrijeme. To je jedna briga manje za vas, a vaš smještaj postaje onaj koji preporučuju prijateljima.",
    villa1_alt="Vila s vrtom u blizini Šibenika, primjer objekta čiji vlasnici surađuju s TAXI Antonio za transfere gostiju",
    car_eyebrow="Čist i udoban automobil", car_h2="Profesionalna vožnja, svaki put",
    car_p1="Vaši gosti putuju u čistom, klimatiziranom Škoda Superb automobilu s mjestom za do četiri putnika i njihovu prtljagu, uz besplatan Wi-Fi. Za veće grupe organiziram kombi preko provjerenog kolege i ostajem vaša jedina kontakt osoba.",
    car_p2="Profesionalno vozim više od deset godina, na ovoj obali i na zimskim transferima u Austriji. Vaši su gosti u iskusnim rukama.",
    villa2_alt="Udobna spavaća soba u vili blizu Šibenika koju TAXI Antonio poslužuje transferima gostiju",
    why_eyebrow="Zašto surađivati sa mnom", why_h2="Što dobivate",
    b1_h3="Jedna kontakt osoba", b1_p="Komunicirate sa mnom, a ne s nizom nepoznatih vozača. Osobno odgovaram na poruke, izravno potvrđujem i preuzimam odgovornost ako nešto iskrsne.",
    b2_h3="Fiksne, poštene cijene", b2_p="Jasne cijene dogovorene unaprijed, tako da vi i vaši klijenti uvijek znate trošak. Bez iznenađenja na kraju vožnje.",
    b3_h3="Uvijek na vrijeme", b3_p="Pratim letove, planiram oko trajekata i autobusa i uračunam vrijeme da vaši ljudi stignu kamo trebaju bez žurbe.",
    b4_h3="Provjerena mreža", b4_p="Kad sam već zauzet ili trebate veće vozilo, uključujem pažljivo odabrane kolege koje osobno poznajem i uvijek vam kažem tko i zašto.",
    b5_h3="Poznavanje kraja", b5_p="Rođen sam ovdje i poznajem ove ceste, gradove i marine u dušu, od Zadra do Splita i svugdje između.",
    b6_h3="Gosti tretirani kao prijatelji", b6_p="Vaš ugled putuje sa svakim gostom. Brinem o njima kao što biste i vi, da se vraćaju k vama.",
    note_h2="Napomena kolegama vozačima",
    note_p="Trenutačno ne tražim suradnju s drugim taksistima i prijevoznicima. I dalje osobno biram kolege s kojima radim, jednog po jednog, i ta je mreža za sada popunjena. Ako se to promijeni, ovdje ću to objaviti.",
    talk_h2="Javite se",
    talk_pre="Ako ste putnička agencija, vlasnik apartmana ili vile, ili agencija i želite surađivati, pošaljite mi e-mail. Recite tko ste i što trebate te odaberite temu ",
    talk_suf=" kako bih znao brzo odgovoriti.",
    email_word="E-mail", cta_btn="Kontaktirajte me",
    meta_title="Postanite partner | TAXI Antonio Šibenik",
    meta_description="Putničke agencije, vlasnici apartmana i vila te agencije: surađujte s pouzdanim lokalnim vozačem u Šibeniku za transfere, izlete i prijevoz gostiju.",
    meta_keywords="taxi šibenik partner, prijevoznik partner šibenik, transferi gostiju vila, agencija prijevoz dalmacija",
)

L["de"] = dict(
    hero_eyebrow="Partnerschaft", hero_h1="Partner werden",
    hero_sub="Ein zuverlässiger lokaler Fahrer für Ihre Gäste, Kunden und Reisenden an der Küste von Šibenik.",
    intro_h2="Ein Fahrer, auf den Sie zählen können",
    intro_p1="Ich bin Antonio, ein lokaler Taxi- und Transferfahrer zwischen Šibenik und Skradin. Wenn Sie Menschen in diesen Teil Dalmatiens schicken, brauchen Sie jemanden vor Ort, der pünktlich kommt, ans Telefon geht und Ihre Gäste so behandelt, wie Sie es tun würden. Genau das mache ich, bei jeder Fahrt, persönlich.",
    intro_p2="Ich arbeite mit drei Arten von Partnern. Wenn Sie einer davon sind, würde ich gern von Ihnen hören.",
    who_eyebrow="Mit wem ich arbeite", who_h2="Drei Arten von Partnern",
    t1_h3="Reisebüros",
    t1_p="Ob im Ausland oder vor Ort: Wenn Sie Transfers und Tagesausflüge für Ihre Kunden buchen, bin ich Ihr Fahrer an der Küste von Šibenik. Feste Preise, klare Bestätigungen und eine Person, die Ihnen direkt antwortet. Kein Callcenter dazwischen.",
    t2_h3="Apartment- &amp; Villenbesitzer",
    t2_p="Sie vermieten an Gäste und möchten, dass ihre Ankunft reibungslos verläuft? Ich hole sie am Flughafen ab, bringe sie an Ihre Tür und am Ende wieder zurück. Ihre Gäste beginnen und beenden ihren Urlaub entspannt, und Sie kümmern sich von der ersten Minute an um sie.",
    t3_h3="Agenturen",
    t3_p="Lokale und ausländische Agenturen, die einen zuverlässigen Transportanbieter an dieser Küste brauchen: Ich übernehme Flughafentransfers, Städtefahrten und Tagesausflüge, mit einem Ansprechpartner von der ersten Nachricht bis zur Ankunft.",
    villa1_eyebrow="Für Apartment- &amp; Villenbesitzer",
    villa1_h2="Ihre Gäste, von Tür zu Tür betreut",
    villa1_p1="Wenn eine Familie nach einem langen Flug landet, will sie nicht nach einer Fahrgelegenheit suchen. Geben Sie ihr meine Daten oder senden Sie mir die Ankunft, ich empfange sie mit einem Namensschild, lade das Gepäck ein und bringe sie direkt zu Ihrer Unterkunft.",
    villa1_p2="Am Ende des Aufenthalts bringe ich sie rechtzeitig zum Flughafen. Das ist eine Sorge weniger für Sie, und Ihre Unterkunft wird die, die man Freunden empfiehlt.",
    villa1_alt="Ferienvilla mit Garten bei Šibenik, deren Eigentümer mit TAXI Antonio für Gästetransfers zusammenarbeiten",
    car_eyebrow="Ein sauberes, bequemes Auto", car_h2="Eine professionelle Fahrt, jedes Mal",
    car_p1="Ihre Gäste reisen in einem sauberen, klimatisierten Škoda Superb mit Platz für bis zu vier Passagiere und ihr Gepäck, dazu kostenloses WLAN. Für größere Gruppen organisiere ich über einen vertrauten Kollegen einen Van und bleibe durchgehend Ihr einziger Ansprechpartner.",
    car_p2="Ich fahre seit über zehn Jahren professionell, an dieser Küste und bei Winter-Flughafentransfers in Österreich. Ihre Gäste sind in erfahrenen Händen.",
    villa2_alt="Gemütliches Schlafzimmer in einer Ferienvilla bei Šibenik, die von TAXI Antonio mit Gästetransfers bedient wird",
    why_eyebrow="Warum mit mir zusammenarbeiten", why_h2="Was Sie bekommen",
    b1_h3="Ein Ansprechpartner", b1_p="Sie haben es mit mir zu tun, nicht mit einer Schicht wechselnder Fahrer. Ich beantworte Nachrichten persönlich, bestätige direkt und übernehme Verantwortung, wenn etwas ist.",
    b2_h3="Feste, ehrliche Preise", b2_p="Klare, im Voraus vereinbarte Preise, damit Sie und Ihre Kunden die Kosten immer kennen. Keine Überraschungen am Ende der Fahrt.",
    b3_h3="Immer pünktlich", b3_p="Ich verfolge Flüge, plane um Fähren und Busse herum und rechne die Zeit ein, damit Ihre Leute ohne Hektik ankommen.",
    b4_h3="Ein vertrautes Netzwerk", b4_p="Wenn ich schon gebucht bin oder Sie ein größeres Fahrzeug brauchen, hole ich handverlesene Kollegen dazu, die ich persönlich kenne, und sage Ihnen immer, wer und warum.",
    b5_h3="Ortskenntnis", b5_p="Ich bin hier geboren und kenne diese Straßen, Städte und Marinas in- und auswendig, von Zadar bis Split und überall dazwischen.",
    b6_h3="Gäste wie Freunde behandelt", b6_p="Ihr Ruf fährt mit jedem Gast mit. Ich kümmere mich um sie, wie Sie es tun würden, damit sie zu Ihnen zurückkommen.",
    note_h2="Ein Hinweis für Fahrerkollegen",
    note_p="Ich suche derzeit keine Partnerschaften mit anderen Taxi- und Transferanbietern. Ich wähle die Kollegen, mit denen ich arbeite, weiterhin persönlich aus, einen nach dem anderen, und dieses Netzwerk ist vorerst vollständig. Sollte sich das ändern, sage ich es hier.",
    talk_h2="Sprechen wir",
    talk_pre="Wenn Sie ein Reisebüro, ein Apartment- oder Villenbesitzer oder eine Agentur sind und zusammenarbeiten möchten, schreiben Sie mir eine E-Mail. Sagen Sie mir, wer Sie sind und was Sie brauchen, und wählen Sie als Thema ",
    talk_suf=", damit ich schnell antworte.",
    email_word="E-Mail", cta_btn="Kontakt aufnehmen",
    meta_title="Partner werden | TAXI Antonio Šibenik",
    meta_description="Reisebüros, Apartment- und Villenbesitzer und Agenturen: Arbeiten Sie mit einem zuverlässigen lokalen Fahrer in Šibenik für Flughafentransfers, Ausflüge und Gästetransport zusammen.",
    meta_keywords="taxi šibenik partner, transfer partner šibenik, gästetransfer villa, reisebüro transport dalmatien",
)

L["pl"] = dict(
    hero_eyebrow="Współpraca", hero_h1="Zostań partnerem",
    hero_sub="Niezawodny lokalny kierowca dla Twoich gości, klientów i podróżnych na wybrzeżu Šibenika.",
    intro_h2="Jeden kierowca, na którym możesz polegać",
    intro_p1="Jestem Antonio, lokalny kierowca taksówki i transferów między Šibenikiem a Skradinem. Jeśli wysyłasz ludzi w tę część Dalmacji, potrzebujesz kogoś na miejscu, kto przyjeżdża punktualnie, odbiera telefon i traktuje Twoich gości tak, jak Ty byś to robił. Właśnie to robię, przy każdym kursie, osobiście.",
    intro_p2="Współpracuję z trzema rodzajami partnerów. Jeśli jesteś jednym z nich, odezwij się.",
    who_eyebrow="Z kim współpracuję", who_h2="Trzy rodzaje partnerów",
    t1_h3="Biura podróży",
    t1_p="Zagraniczne czy lokalne, jeśli rezerwujesz transfery i wycieczki dla swoich klientów, jestem Twoim kierowcą na wybrzeżu Šibenika. Stałe ceny, jasne potwierdzenia i jedna osoba, która odpowiada Ci bezpośrednio. Bez call center pośrodku.",
    t2_h3="Właściciele apartamentów i willi",
    t2_p="Wynajmujesz gościom i chcesz, aby ich przyjazd przebiegł bez problemów? Odbieram ich z lotniska, dowożę pod Twoje drzwi i odwożę na koniec pobytu. Twoi goście zaczynają i kończą urlop w spokoju, a Ty dbasz o nich od pierwszej minuty.",
    t3_h3="Agencje",
    t3_p="Lokalne i zagraniczne agencje, które potrzebują niezawodnego przewoźnika na tym wybrzeżu: obsługuję transfery lotniskowe, przejazdy między miastami i wycieczki, z jedną osobą kontaktową od pierwszej wiadomości do przyjazdu.",
    villa1_eyebrow="Dla właścicieli apartamentów i willi",
    villa1_h2="Twoi goście, zaopiekowani od drzwi do drzwi",
    villa1_p1="Gdy rodzina ląduje po długim locie, ostatnią rzeczą, jakiej chce, jest szukanie transportu. Daj im moje dane lub prześlij mi godzinę przylotu, a przywitam ich z tabliczką z nazwiskiem, załaduję bagaż i zawiozę prosto do Twojego obiektu.",
    villa1_p2="Na koniec pobytu odwożę ich na lotnisko na czas. To o jedno zmartwienie mniej dla Ciebie, a Twój obiekt staje się tym, który poleca się znajomym.",
    villa1_alt="Willa wakacyjna z ogrodem koło Šibenika, której właściciele współpracują z TAXI Antonio przy transferach gości",
    car_eyebrow="Czysty, wygodny samochód", car_h2="Profesjonalny przejazd, za każdym razem",
    car_p1="Twoi goście podróżują czystym, klimatyzowanym Škoda Superb z miejscem dla maksymalnie czterech pasażerów i ich bagażu oraz darmowym Wi-Fi. Dla większych grup organizuję busa przez zaufanego kolegę i pozostaję Twoją jedyną osobą kontaktową.",
    car_p2="Jeżdżę zawodowo od ponad dziesięciu lat, na tym wybrzeżu i przy zimowych transferach lotniskowych w Austrii. Twoi goście są w doświadczonych rękach.",
    villa2_alt="Wygodna sypialnia w willi wakacyjnej koło Šibenika obsługiwanej przez transfery gości TAXI Antonio",
    why_eyebrow="Dlaczego warto ze mną współpracować", why_h2="Co zyskujesz",
    b1_h3="Jedna osoba kontaktowa", b1_p="Masz do czynienia ze mną, a nie ze zmieniającymi się kierowcami. Osobiście odpowiadam na wiadomości, potwierdzam bezpośrednio i biorę odpowiedzialność, jeśli coś się pojawi.",
    b2_h3="Stałe, uczciwe ceny", b2_p="Jasne ceny ustalone z góry, aby Ty i Twoi klienci zawsze znali koszt. Bez niespodzianek na koniec kursu.",
    b3_h3="Zawsze na czas", b3_p="Śledzę loty, planuję wokół promów i autobusów i wliczam czas, aby Twoi ludzie dotarli tam, gdzie trzeba, bez pośpiechu.",
    b4_h3="Zaufana sieć", b4_p="Gdy jestem już zajęty lub potrzebujesz większego pojazdu, angażuję starannie dobranych kolegów, których znam osobiście, i zawsze mówię Ci kogo i dlaczego.",
    b5_h3="Znajomość okolicy", b5_p="Urodziłem się tutaj i znam te drogi, miasta i mariny na wylot, od Zadaru po Split i wszędzie pomiędzy.",
    b6_h3="Goście traktowani jak przyjaciele", b6_p="Twoja reputacja jedzie z każdym gościem. Dbam o nich tak, jak Ty byś to robił, aby wracali do Ciebie.",
    note_h2="Uwaga dla kolegów kierowców",
    note_p="Obecnie nie szukam współpracy z innymi taksówkarzami i przewoźnikami. Nadal osobiście dobieram kolegów, z którymi pracuję, jednego po drugim, i ta sieć jest na razie kompletna. Jeśli to się zmieni, napiszę o tym tutaj.",
    talk_h2="Porozmawiajmy",
    talk_pre="Jeśli jesteś biurem podróży, właścicielem apartamentu lub willi albo agencją i chcesz współpracować, napisz do mnie e-mail. Napisz, kim jesteś i czego potrzebujesz, i wybierz temat ",
    talk_suf=", abym wiedział, że mam odpowiedzieć szybko.",
    email_word="E-mail", cta_btn="Skontaktuj się ze mną",
    meta_title="Zostań partnerem | TAXI Antonio Šibenik",
    meta_description="Biura podróży, właściciele apartamentów i willi oraz agencje: współpracuj z niezawodnym lokalnym kierowcą w Šibeniku przy transferach lotniskowych, wycieczkach i transporcie gości.",
    meta_keywords="taxi šibenik partner, transfer partner šibenik, transfery gości willa, biuro podróży transport dalmacja",
)

L["cs"] = dict(
    hero_eyebrow="Spolupráce", hero_h1="Staňte se partnerem",
    hero_sub="Spolehlivý místní řidič pro vaše hosty, klienty a cestující na pobřeží Šibeniku.",
    intro_h2="Jeden řidič, na kterého se můžete spolehnout",
    intro_p1="Jsem Antonio, místní taxikář a řidič transferů mezi Šibenikem a Skradinem. Pokud posíláte lidi do této části Dalmácie, potřebujete někoho na místě, kdo přijede včas, zvedne telefon a chová se k vašim hostům tak, jak byste to udělali vy. Přesně to dělám, na každé jízdě, osobně.",
    intro_p2="Spolupracuji se třemi druhy partnerů. Pokud jste jedním z nich, ozvěte se mi.",
    who_eyebrow="S kým spolupracuji", who_h2="Tři druhy partnerů",
    t1_h3="Cestovní kanceláře",
    t1_p="Zahraniční i místní: pokud rezervujete transfery a výlety pro své klienty, jsem váš řidič na pobřeží Šibeniku. Pevné ceny, jasná potvrzení a jedna osoba, která vám odpovídá přímo. Bez call centra mezi vámi a mnou.",
    t2_h3="Majitelé apartmánů a vil",
    t2_p="Pronajímáte hostům a chcete, aby jejich příjezd proběhl hladce? Vyzvednu je na letišti, dovezu k vašim dveřím a na konci pobytu je odvezu zpět. Vaši hosté začínají i končí dovolenou v klidu a vy o ně pečujete od první minuty.",
    t3_h3="Agentury",
    t3_p="Místní i zahraniční agentury, které potřebují spolehlivého dopravce na tomto pobřeží: zajišťuji letištní transfery, jízdy mezi městy a výlety, s jednou kontaktní osobou od první zprávy až po příjezd.",
    villa1_eyebrow="Pro majitele apartmánů a vil",
    villa1_h2="O vaše hosty postaráno ode dveří ke dveřím",
    villa1_p1="Když rodina přistane po dlouhém letu, poslední, co chce, je hledat odvoz. Dejte jim mé kontakty nebo mi pošlete čas příletu, přivítám je s cedulkou se jménem, naložím zavazadla a odvezu je přímo k vašemu objektu.",
    villa1_p2="Na konci pobytu je včas odvezu na letiště. Pro vás je to jedna starost méně a váš objekt se stává tím, který doporučují přátelům.",
    villa1_alt="Prázdninová vila se zahradou u Šibeniku, jejíž majitelé spolupracují s TAXI Antonio na transferech hostů",
    car_eyebrow="Čisté, pohodlné auto", car_h2="Profesionální jízda, pokaždé",
    car_p1="Vaši hosté cestují v čistém, klimatizovaném voze Škoda Superb s místem až pro čtyři cestující a jejich zavazadla a s Wi-Fi zdarma. Pro větší skupiny zajistím dodávku přes prověřeného kolegu a zůstávám vaší jedinou kontaktní osobou.",
    car_p2="Řídím profesionálně přes deset let, na tomto pobřeží i na zimních letištních transferech v Rakousku. Vaši hosté jsou ve zkušených rukou.",
    villa2_alt="Pohodlná ložnice v prázdninové vile u Šibeniku, kterou obsluhuje TAXI Antonio transfery hostů",
    why_eyebrow="Proč spolupracovat se mnou", why_h2="Co získáte",
    b1_h3="Jedna kontaktní osoba", b1_p="Jednáte se mnou, ne se střídajícími se řidiči. Na zprávy odpovídám osobně, potvrzuji přímo a přebírám odpovědnost, pokud něco nastane.",
    b2_h3="Pevné, poctivé ceny", b2_p="Jasné ceny dohodnuté předem, takže vy i vaši klienti vždy znáte cenu. Žádná překvapení na konci jízdy.",
    b3_h3="Vždy včas", b3_p="Sleduji lety, plánuji kolem trajektů a autobusů a počítám s časem, aby se vaši lidé dostali tam, kam potřebují, bez spěchu.",
    b4_h3="Prověřená síť", b4_p="Když už jsem zamluvený nebo potřebujete větší vozidlo, přiberu pečlivě vybrané kolegy, které osobně znám, a vždy vám řeknu koho a proč.",
    b5_h3="Znalost kraje", b5_p="Narodil jsem se zde a znám tyto silnice, města a maríny dokonale, od Zadaru po Split a všude mezi tím.",
    b6_h3="S hosty jako s přáteli", b6_p="Vaše pověst cestuje s každým hostem. Starám se o ně tak, jak byste to dělali vy, aby se k vám vraceli.",
    note_h2="Poznámka pro kolegy řidiče",
    note_p="V současné době nehledám spolupráci s dalšími taxikáři a dopravci. Kolegy, se kterými pracuji, si stále vybírám osobně, jednoho po druhém, a tato síť je zatím naplněná. Pokud se to změní, napíšu to sem.",
    talk_h2="Pojďme to probrat",
    talk_pre="Pokud jste cestovní kancelář, majitel apartmánu nebo vily, nebo agentura a chcete spolupracovat, napište mi e-mail. Napište, kdo jste a co potřebujete, a jako téma zvolte ",
    talk_suf=", ať vím, že mám odpovědět rychle.",
    email_word="E-mail", cta_btn="Kontaktujte mě",
    meta_title="Staňte se partnerem | TAXI Antonio Šibenik",
    meta_description="Cestovní kanceláře, majitelé apartmánů a vil a agentury: spolupracujte se spolehlivým místním řidičem v Šibeniku na letištních transferech, výletech a dopravě hostů.",
    meta_keywords="taxi šibenik partner, transfer partner šibenik, transfery hostů vila, cestovní kancelář doprava dalmácie",
)

L["it"] = dict(
    hero_eyebrow="Collaborazione", hero_h1="Diventa partner",
    hero_sub="Un autista locale affidabile per i tuoi ospiti, clienti e viaggiatori sulla costa di Šibenik.",
    intro_h2="Un autista su cui puoi contare",
    intro_p1="Sono Antonio, autista di taxi e transfer locale tra Šibenik e Skradin. Se mandi persone in questa parte della Dalmazia, ti serve qualcuno sul posto che arrivi puntuale, risponda al telefono e tratti i tuoi ospiti come faresti tu. È esattamente ciò che faccio, a ogni corsa, di persona.",
    intro_p2="Lavoro con tre tipi di partner. Se sei uno di loro, mi piacerebbe sentirti.",
    who_eyebrow="Con chi lavoro", who_h2="Tre tipi di partner",
    t1_h3="Agenzie di viaggio",
    t1_p="Straniere o locali: se prenoti transfer e gite per i tuoi clienti, sono io il tuo autista sulla costa di Šibenik. Prezzi fissi, conferme chiare e una sola persona che ti risponde direttamente. Nessun call center di mezzo.",
    t2_h3="Proprietari di appartamenti e ville",
    t2_p="Affitti agli ospiti e vuoi che il loro arrivo fili liscio? Li prendo in aeroporto, li porto alla tua porta e li riaccompagno alla fine del soggiorno. I tuoi ospiti iniziano e finiscono la vacanza rilassati e tu ti prendi cura di loro dal primo minuto.",
    t3_h3="Agenzie",
    t3_p="Agenzie locali e straniere che cercano un fornitore di trasporti affidabile su questa costa: mi occupo di transfer aeroportuali, tratte tra città e gite, con un unico referente dal primo messaggio all'arrivo.",
    villa1_eyebrow="Per proprietari di appartamenti e ville",
    villa1_h2="I tuoi ospiti, seguiti porta a porta",
    villa1_p1="Quando una famiglia atterra dopo un lungo volo, l'ultima cosa che vuole è cercare un passaggio. Dai loro i miei contatti o inviami il loro arrivo: li accolgo con un cartello col nome, carico i bagagli e li porto direttamente alla tua struttura.",
    villa1_p2="Alla fine del soggiorno li riporto in aeroporto in tempo. È un pensiero in meno per te, e la tua struttura diventa quella che consigliano agli amici.",
    villa1_alt="Villa vacanze con giardino vicino a Šibenik, i cui proprietari collaborano con TAXI Antonio per i transfer degli ospiti",
    car_eyebrow="Un'auto pulita e comoda", car_h2="Un viaggio professionale, ogni volta",
    car_p1="I tuoi ospiti viaggiano su una Škoda Superb pulita e climatizzata, con spazio fino a quattro passeggeri e i loro bagagli, e Wi-Fi gratuito a bordo. Per gruppi più numerosi organizzo un van tramite un collega fidato e resto il tuo unico referente.",
    car_p2="Guido professionalmente da oltre dieci anni, su questa costa e nei transfer aeroportuali invernali in Austria. I tuoi ospiti sono in mani esperte.",
    villa2_alt="Camera da letto accogliente in una villa vacanze vicino a Šibenik servita dai transfer per ospiti di TAXI Antonio",
    why_eyebrow="Perché collaborare con me", why_h2="Cosa ottieni",
    b1_h3="Un unico referente", b1_p="Tratti con me, non con una schiera di autisti diversi. Rispondo ai messaggi di persona, confermo direttamente e mi assumo la responsabilità se succede qualcosa.",
    b2_h3="Prezzi fissi e onesti", b2_p="Prezzi chiari concordati in anticipo, così tu e i tuoi clienti conoscete sempre il costo. Nessuna sorpresa a fine corsa.",
    b3_h3="Sempre puntuale", b3_p="Monitoro i voli, pianifico intorno a traghetti e autobus e calcolo il tempo per portare le tue persone dove devono, senza fretta.",
    b4_h3="Una rete fidata", b4_p="Quando sono già impegnato o ti serve un veicolo più grande, coinvolgo colleghi selezionati che conosco di persona, e ti dico sempre chi e perché.",
    b5_h3="Conoscenza del territorio", b5_p="Sono nato qui e conosco a fondo queste strade, città e marine, da Zadar a Split e tutto ciò che sta in mezzo.",
    b6_h3="Ospiti trattati come amici", b6_p="La tua reputazione viaggia con ogni ospite. Mi prendo cura di loro come faresti tu, così tornano da te.",
    note_h2="Una nota per i colleghi autisti",
    note_p="Al momento non cerco collaborazioni con altri autisti di taxi e transfer. Continuo a scegliere personalmente i colleghi con cui lavoro, uno per uno, e quella rete per ora è al completo. Se cambierà, lo scriverò qui.",
    talk_h2="Parliamone",
    talk_pre="Se sei un'agenzia di viaggio, un proprietario di appartamento o villa, o un'agenzia e vuoi collaborare, scrivimi un'email. Dimmi chi sei e cosa ti serve, e scegli ",
    talk_suf=" come argomento, così so di risponderti in fretta.",
    email_word="Email", cta_btn="Contattami",
    meta_title="Diventa partner | TAXI Antonio Šibenik",
    meta_description="Agenzie di viaggio, proprietari di appartamenti e ville e agenzie: collabora con un autista locale affidabile a Šibenik per transfer aeroportuali, gite e trasporto ospiti.",
    meta_keywords="taxi šibenik partner, transfer partner šibenik, transfer ospiti villa, agenzia viaggi trasporto dalmazia",
)

L["fr"] = dict(
    hero_eyebrow="Partenariat", hero_h1="Devenir partenaire",
    hero_sub="Un chauffeur local fiable pour vos hôtes, clients et voyageurs sur la côte de Šibenik.",
    intro_h2="Un chauffeur sur qui compter",
    intro_p1="Je suis Antonio, chauffeur de taxi et de transferts local entre Šibenik et Skradin. Si vous envoyez des gens dans cette partie de la Dalmatie, il vous faut quelqu'un sur place qui arrive à l'heure, répond au téléphone et traite vos hôtes comme vous le feriez. C'est exactement ce que je fais, à chaque course, en personne.",
    intro_p2="Je travaille avec trois types de partenaires. Si vous en êtes un, contactez-moi.",
    who_eyebrow="Avec qui je travaille", who_h2="Trois types de partenaires",
    t1_h3="Agences de voyage",
    t1_p="Étrangères ou locales : si vous réservez des transferts et des excursions pour vos clients, je suis votre chauffeur sur la côte de Šibenik. Prix fixes, confirmations claires et une seule personne qui vous répond directement. Aucun centre d'appels entre nous.",
    t2_h3="Propriétaires d'appartements et de villas",
    t2_p="Vous louez à des hôtes et voulez que leur arrivée se passe sans accroc ? Je vais les chercher à l'aéroport, je les amène à votre porte et je les ramène à la fin du séjour. Vos hôtes commencent et terminent leurs vacances détendus, et vous prenez soin d'eux dès la première minute.",
    t3_h3="Agences",
    t3_p="Agences locales et étrangères en quête d'un transporteur fiable sur cette côte : je m'occupe des transferts aéroport, des trajets entre villes et des excursions, avec un seul interlocuteur du premier message à l'arrivée.",
    villa1_eyebrow="Pour les propriétaires d'appartements et de villas",
    villa1_h2="Vos hôtes, pris en charge de porte à porte",
    villa1_p1="Quand une famille atterrit après un long vol, la dernière chose qu'elle veut, c'est chercher un transport. Donnez-leur mes coordonnées ou envoyez-moi leur arrivée : je les accueille avec une pancarte à leur nom, je charge les bagages et je les conduis directement à votre logement.",
    villa1_p2="À la fin du séjour, je les ramène à l'aéroport à temps. C'est un souci de moins pour vous, et votre logement devient celui que l'on recommande à ses amis.",
    villa1_alt="Villa de vacances avec jardin près de Šibenik, dont les propriétaires collaborent avec TAXI Antonio pour les transferts des hôtes",
    car_eyebrow="Une voiture propre et confortable", car_h2="Un trajet professionnel, à chaque fois",
    car_p1="Vos hôtes voyagent dans une Škoda Superb propre et climatisée, avec de la place pour jusqu'à quatre passagers et leurs bagages, et le Wi-Fi gratuit à bord. Pour les groupes plus nombreux, j'organise un van via un collègue de confiance et je reste votre unique interlocuteur.",
    car_p2="Je conduis professionnellement depuis plus de dix ans, sur cette côte et lors de transferts aéroport hivernaux en Autriche. Vos hôtes sont entre des mains expérimentées.",
    villa2_alt="Chambre confortable dans une villa de vacances près de Šibenik desservie par les transferts d'hôtes de TAXI Antonio",
    why_eyebrow="Pourquoi travailler avec moi", why_h2="Ce que vous obtenez",
    b1_h3="Un seul interlocuteur", b1_p="Vous avez affaire à moi, pas à une rotation de chauffeurs inconnus. Je réponds aux messages en personne, je confirme directement et j'assume si quelque chose survient.",
    b2_h3="Des prix fixes et honnêtes", b2_p="Des prix clairs convenus à l'avance, pour que vous et vos clients connaissiez toujours le coût. Aucune surprise en fin de course.",
    b3_h3="Toujours à l'heure", b3_p="Je surveille les vols, je planifie autour des ferries et des bus et je prévois le temps nécessaire pour amener vos voyageurs à destination sans précipitation.",
    b4_h3="Un réseau de confiance", b4_p="Quand je suis déjà réservé ou qu'il vous faut un véhicule plus grand, je fais appel à des collègues triés sur le volet que je connais personnellement, et je vous dis toujours qui et pourquoi.",
    b5_h3="Connaissance du terrain", b5_p="Je suis né ici et je connais ces routes, ces villes et ces marinas sur le bout des doigts, de Zadar à Split et partout entre les deux.",
    b6_h3="Des hôtes traités en amis", b6_p="Votre réputation voyage avec chaque hôte. J'en prends soin comme vous le feriez, pour qu'ils reviennent vers vous.",
    note_h2="Un mot pour les chauffeurs confrères",
    note_p="Je ne cherche pas de partenariats avec d'autres chauffeurs de taxi et de transfert pour le moment. Je choisis toujours personnellement les collègues avec qui je travaille, un par un, et ce réseau est complet pour l'instant. Si cela change, je l'indiquerai ici.",
    talk_h2="Discutons-en",
    talk_pre="Si vous êtes une agence de voyage, un propriétaire d'appartement ou de villa, ou une agence et que vous souhaitez collaborer, envoyez-moi un e-mail. Dites-moi qui vous êtes et ce qu'il vous faut, et choisissez ",
    talk_suf=" comme sujet pour que je sache répondre vite.",
    email_word="E-mail", cta_btn="Contactez-moi",
    meta_title="Devenir partenaire | TAXI Antonio Šibenik",
    meta_description="Agences de voyage, propriétaires d'appartements et de villas et agences : collaborez avec un chauffeur local fiable à Šibenik pour les transferts aéroport, les excursions et le transport des hôtes.",
    meta_keywords="taxi šibenik partenaire, transfert partenaire šibenik, transfert hôtes villa, agence voyage transport dalmatie",
)

L["nl"] = dict(
    hero_eyebrow="Samenwerking", hero_h1="Word partner",
    hero_sub="Een betrouwbare lokale chauffeur voor uw gasten, klanten en reizigers aan de kust van Šibenik.",
    intro_h2="Eén chauffeur op wie u kunt rekenen",
    intro_p1="Ik ben Antonio, een lokale taxi- en transferchauffeur tussen Šibenik en Skradin. Als u mensen naar dit deel van Dalmatië stuurt, hebt u iemand ter plaatse nodig die op tijd komt, de telefoon opneemt en uw gasten behandelt zoals u dat zou doen. Dat is precies wat ik doe, bij elke rit, persoonlijk.",
    intro_p2="Ik werk met drie soorten partners. Bent u er een van, dan hoor ik graag van u.",
    who_eyebrow="Met wie ik samenwerk", who_h2="Drie soorten partners",
    t1_h3="Reisbureaus",
    t1_p="Buitenlands of lokaal: als u transfers en excursies voor uw klanten boekt, ben ik uw chauffeur aan de kust van Šibenik. Vaste prijzen, duidelijke bevestigingen en één persoon die u rechtstreeks antwoordt. Geen callcenter ertussen.",
    t2_h3="Eigenaren van appartementen en villa's",
    t2_p="Verhuurt u aan gasten en wilt u dat hun aankomst vlot verloopt? Ik haal ze op van de luchthaven, breng ze tot aan uw deur en breng ze aan het einde weer terug. Uw gasten beginnen en eindigen hun vakantie ontspannen, en u zorgt vanaf de eerste minuut voor ze.",
    t3_h3="Bureaus",
    t3_p="Lokale en buitenlandse bureaus die een betrouwbare vervoerder aan deze kust zoeken: ik verzorg luchthaventransfers, ritten tussen steden en excursies, met één aanspreekpunt van het eerste bericht tot de aankomst.",
    villa1_eyebrow="Voor eigenaren van appartementen en villa's",
    villa1_h2="Uw gasten, van deur tot deur verzorgd",
    villa1_p1="Als een gezin na een lange vlucht landt, wil het niet op zoek naar vervoer. Geef ze mijn gegevens of stuur mij hun aankomst: ik verwelkom ze met een naambordje, laad de bagage in en breng ze rechtstreeks naar uw accommodatie.",
    villa1_p2="Aan het einde van het verblijf breng ik ze op tijd terug naar de luchthaven. Voor u is dat één zorg minder, en uw accommodatie wordt degene die men aan vrienden aanbeveelt.",
    villa1_alt="Vakantievilla met tuin bij Šibenik, waarvan de eigenaren met TAXI Antonio samenwerken voor gasttransfers",
    car_eyebrow="Een schone, comfortabele auto", car_h2="Een professionele rit, elke keer",
    car_p1="Uw gasten reizen in een schone, airconditioned Škoda Superb met plaats voor maximaal vier passagiers en hun bagage, en gratis wifi aan boord. Voor grotere groepen regel ik een busje via een vertrouwde collega en blijf ik uw enige aanspreekpunt.",
    car_p2="Ik rijd al meer dan tien jaar professioneel, aan deze kust en op winterse luchthaventransfers in Oostenrijk. Uw gasten zijn in ervaren handen.",
    villa2_alt="Comfortabele slaapkamer in een vakantievilla bij Šibenik die door de gasttransfers van TAXI Antonio wordt bediend",
    why_eyebrow="Waarom met mij samenwerken", why_h2="Wat u krijgt",
    b1_h3="Eén aanspreekpunt", b1_p="U hebt met mij te maken, niet met een wisselend team van onbekenden. Ik beantwoord berichten persoonlijk, bevestig rechtstreeks en neem verantwoordelijkheid als er iets is.",
    b2_h3="Vaste, eerlijke prijzen", b2_p="Duidelijke prijzen die vooraf zijn afgesproken, zodat u en uw klanten altijd de kosten kennen. Geen verrassingen aan het einde van de rit.",
    b3_h3="Altijd op tijd", b3_p="Ik volg vluchten, plan rond veerboten en bussen en reken de tijd in om uw mensen zonder haast op hun bestemming te krijgen.",
    b4_h3="Een vertrouwd netwerk", b4_p="Als ik al geboekt ben of u een groter voertuig nodig hebt, schakel ik zorgvuldig gekozen collega's in die ik persoonlijk ken, en ik zeg u altijd wie en waarom.",
    b5_h3="Lokale kennis", b5_p="Ik ben hier geboren en ken deze wegen, steden en jachthavens door en door, van Zadar tot Split en overal daartussen.",
    b6_h3="Gasten als vrienden behandeld", b6_p="Uw reputatie reist met elke gast mee. Ik zorg voor ze zoals u dat zou doen, zodat ze bij u terugkomen.",
    note_h2="Een noot voor collega-chauffeurs",
    note_p="Ik zoek momenteel geen samenwerking met andere taxi- en transferaanbieders. Ik kies de collega's met wie ik werk nog steeds persoonlijk uit, een voor een, en dat netwerk is voorlopig compleet. Verandert dat, dan meld ik het hier.",
    talk_h2="Laten we praten",
    talk_pre="Bent u een reisbureau, eigenaar van een appartement of villa, of een bureau en wilt u samenwerken, stuur mij dan een e-mail. Vertel me wie u bent en wat u nodig hebt, en kies ",
    talk_suf=" als onderwerp, zodat ik weet dat ik snel moet reageren.",
    email_word="E-mail", cta_btn="Neem contact op",
    meta_title="Word partner | TAXI Antonio Šibenik",
    meta_description="Reisbureaus, eigenaren van appartementen en villa's en bureaus: werk samen met een betrouwbare lokale chauffeur in Šibenik voor luchthaventransfers, excursies en gastenvervoer.",
    meta_keywords="taxi šibenik partner, transfer partner šibenik, gasttransfers villa, reisbureau vervoer dalmatië",
)

L["sl"] = dict(
    hero_eyebrow="Sodelovanje", hero_h1="Postanite partner",
    hero_sub="Zanesljiv lokalni voznik za vaše goste, stranke in popotnike na obali Šibenika.",
    intro_h2="Voznik, na katerega se lahko zanesete",
    intro_p1="Sem Antonio, lokalni taksist in voznik transferjev med Šibenikom in Skradinom. Če pošiljate ljudi v ta del Dalmacije, potrebujete nekoga na terenu, ki pride pravočasno, se oglasi na telefon in z vašimi gosti ravna tako, kot bi vi. Prav to počnem, na vsaki vožnji, osebno.",
    intro_p2="Sodelujem s tremi vrstami partnerjev. Če ste eden od njih, se mi oglasite.",
    who_eyebrow="S kom sodelujem", who_h2="Tri vrste partnerjev",
    t1_h3="Potovalne agencije",
    t1_p="Tuje ali domače: če za svoje stranke rezervirate transferje in izlete, sem jaz vaš voznik na obali Šibenika. Fiksne cene, jasne potrditve in ena oseba, ki vam odgovarja neposredno. Brez klicnega centra vmes.",
    t2_h3="Lastniki apartmajev in vil",
    t2_p="Oddajate gostom in želite, da njihov prihod poteče gladko? Poberem jih na letališču, pripeljem do vaših vrat in ob koncu bivanja odpeljem nazaj. Vaši gosti začnejo in končajo počitnice sproščeno, vi pa zanje skrbite od prve minute.",
    t3_h3="Agencije",
    t3_p="Domače in tuje agencije, ki potrebujejo zanesljivega prevoznika na tej obali: opravljam letališke transferje, medmestne vožnje in izlete, z eno kontaktno osebo od prvega sporočila do prihoda.",
    villa1_eyebrow="Za lastnike apartmajev in vil",
    villa1_h2="Za vaše goste poskrbljeno od vrat do vrat",
    villa1_p1="Ko družina pristane po dolgem letu, je zadnje, kar želi, iskanje prevoza. Dajte jim moje podatke ali mi sporočite njihov prihod: pričakam jih z napisom z imenom, naložim prtljago in jih odpeljem naravnost do vašega objekta.",
    villa1_p2="Ob koncu bivanja jih pravočasno odpeljem na letališče. Za vas je to ena skrb manj, vaš objekt pa postane tisti, ki ga priporočajo prijateljem.",
    villa1_alt="Počitniška vila z vrtom blizu Šibenika, katere lastniki sodelujejo s TAXI Antonio pri prevozih gostov",
    car_eyebrow="Čist, udoben avtomobil", car_h2="Profesionalna vožnja, vsakič",
    car_p1="Vaši gosti se peljejo v čistem, klimatiziranem vozilu Škoda Superb s prostorom za do štiri potnike in njihovo prtljago ter brezplačnim Wi-Fi. Za večje skupine organiziram kombi prek zaupanja vrednega kolega in ostanem vaša edina kontaktna oseba.",
    car_p2="Profesionalno vozim več kot deset let, na tej obali in na zimskih letaliških transferjih v Avstriji. Vaši gosti so v izkušenih rokah.",
    villa2_alt="Udobna spalnica v počitniški vili blizu Šibenika, ki jo streže TAXI Antonio s prevozi gostov",
    why_eyebrow="Zakaj sodelovati z mano", why_h2="Kaj dobite",
    b1_h3="Ena kontaktna oseba", b1_p="Poslujete z mano, ne z izmeno neznanih voznikov. Na sporočila odgovarjam osebno, potrjujem neposredno in prevzamem odgovornost, če kaj nastane.",
    b2_h3="Fiksne, poštene cene", b2_p="Jasne cene, dogovorjene vnaprej, tako da vi in vaše stranke vedno poznate ceno. Brez presenečenj ob koncu vožnje.",
    b3_h3="Vedno pravočasno", b3_p="Spremljam lete, načrtujem okoli trajektov in avtobusov ter predvidim čas, da vaše ljudi brez naglice pripeljem tja, kamor morajo.",
    b4_h3="Zaupanja vredna mreža", b4_p="Ko sem že zaseden ali potrebujete večje vozilo, vključim skrbno izbrane kolege, ki jih osebno poznam, in vam vedno povem, kdo in zakaj.",
    b5_h3="Poznavanje kraja", b5_p="Rojen sem tukaj in te ceste, mesta in marine poznam do potankosti, od Zadra do Splita in povsod vmes.",
    b6_h3="Gostje, obravnavani kot prijatelji", b6_p="Vaš ugled potuje z vsakim gostom. Zanje poskrbim tako, kot bi vi, da se vračajo k vam.",
    note_h2="Beseda kolegom voznikom",
    note_p="Trenutno ne iščem sodelovanja z drugimi taksisti in prevozniki. Kolege, s katerimi delam, še vedno izbiram osebno, enega za drugim, in ta mreža je za zdaj polna. Če se to spremeni, bom zapisal tukaj.",
    talk_h2="Pogovorimo se",
    talk_pre="Če ste potovalna agencija, lastnik apartmaja ali vile ali agencija in želite sodelovati, mi pošljite e-pošto. Povejte mi, kdo ste in kaj potrebujete, ter izberite ",
    talk_suf=" kot temo, da bom vedel hitro odgovoriti.",
    email_word="E-pošta", cta_btn="Kontaktirajte me",
    meta_title="Postanite partner | TAXI Antonio Šibenik",
    meta_description="Potovalne agencije, lastniki apartmajev in vil ter agencije: sodelujte z zanesljivim lokalnim voznikom v Šibeniku za letališke transferje, izlete in prevoz gostov.",
    meta_keywords="taxi šibenik partner, transfer partner šibenik, prevoz gostov vila, potovalna agencija prevoz dalmacija",
)

L["hu"] = dict(
    hero_eyebrow="Együttműködés", hero_h1="Legyen partnerünk",
    hero_sub="Megbízható helyi sofőr az Ön vendégei, ügyfelei és utasai számára a šibeniki tengerparton.",
    intro_h2="Egy sofőr, akire számíthat",
    intro_p1="Antonio vagyok, helyi taxi- és transzfersofőr Šibenik és Skradin között. Ha ide, Dalmácia e részébe küld embereket, olyasvalakire van szüksége a helyszínen, aki időben érkezik, felveszi a telefont, és úgy bánik a vendégeivel, ahogy Ön tenné. Pontosan ezt teszem, minden úton, személyesen.",
    intro_p2="Háromféle partnerrel dolgozom. Ha Ön is közéjük tartozik, keressen meg.",
    who_eyebrow="Kikkel dolgozom", who_h2="Háromféle partner",
    t1_h3="Utazási irodák",
    t1_p="Külföldi vagy helyi: ha transzfereket és kirándulásokat foglal ügyfeleinek, én vagyok az Ön sofőrje a šibeniki parton. Fix árak, egyértelmű visszaigazolások és egyetlen személy, aki közvetlenül válaszol Önnek. Nincs köztünk telefonos központ.",
    t2_h3="Apartman- és villatulajdonosok",
    t2_p="Vendégeknek ad ki szállást, és szeretné, hogy zökkenőmentes legyen az érkezésük? Elhozom őket a repülőtérről, az ajtajához viszem, a végén pedig visszaviszem. Vendégei nyugodtan kezdik és fejezik be a nyaralást, Ön pedig az első perctől gondoskodik róluk.",
    t3_h3="Ügynökségek",
    t3_p="Helyi és külföldi ügynökségek, amelyeknek megbízható fuvarozóra van szükségük ezen a parton: repülőtéri transzfereket, városközi utakat és kirándulásokat vállalok, egyetlen kapcsolattartóval az első üzenettől az érkezésig.",
    villa1_eyebrow="Apartman- és villatulajdonosoknak",
    villa1_h2="Vendégeiről ajtótól ajtóig gondoskodom",
    villa1_p1="Amikor egy család egy hosszú repülőút után landol, a legkevésbé sem akar fuvar után kutatni. Adja meg nekik az elérhetőségemet, vagy küldje el az érkezésüket: névtáblával várom őket, berakom a csomagokat, és egyenesen a szálláshelyére viszem őket.",
    villa1_p2="A tartózkodás végén időben visszaviszem őket a repülőtérre. Ez Önnek eggyel kevesebb gond, a szállása pedig az lesz, amit a barátoknak ajánlanak.",
    villa1_alt="Nyaralóvilla kerttel Šibenik közelében, amelynek tulajdonosai a TAXI Antonióval működnek együtt a vendégtranszferekben",
    car_eyebrow="Tiszta, kényelmes autó", car_h2="Profi utazás, minden alkalommal",
    car_p1="Vendégei tiszta, légkondicionált Škoda Superbben utaznak, amelyben legfeljebb négy utas és a csomagjaik férnek el, a fedélzeten pedig ingyenes Wi-Fi van. Nagyobb csoportoknak megbízható kollégán keresztül szervezek kisbuszt, és végig én maradok az egyetlen kapcsolattartó.",
    car_p2="Több mint tíz éve vezetek hivatásszerűen, ezen a parton és téli ausztriai repülőtéri transzfereken is. Vendégei tapasztalt kezekben vannak.",
    villa2_alt="Kényelmes hálószoba egy Šibenik közeli nyaralóvillában, amelyet a TAXI Antonio vendégtranszferei szolgálnak ki",
    why_eyebrow="Miért velem dolgozzon", why_h2="Amit kap",
    b1_h3="Egyetlen kapcsolattartó", b1_p="Velem van dolga, nem váltakozó, ismeretlen sofőrökkel. Az üzenetekre személyesen válaszolok, közvetlenül visszaigazolok, és felelősséget vállalok, ha valami adódik.",
    b2_h3="Fix, tisztességes árak", b2_p="Előre megbeszélt, egyértelmű árak, hogy Ön és ügyfelei mindig tudják a költséget. Nincs meglepetés az út végén.",
    b3_h3="Mindig időben", b3_p="Figyelem a járatokat, a kompokhoz és buszokhoz igazítok, és beleszámítom az időt, hogy utasai kapkodás nélkül érjenek célba.",
    b4_h3="Megbízható hálózat", b4_p="Ha már foglalt vagyok, vagy nagyobb járműre van szüksége, gondosan kiválasztott, személyesen ismert kollégákat vonok be, és mindig megmondom, kit és miért.",
    b5_h3="Helyismeret", b5_p="Itt születtem, és tökéletesen ismerem ezeket az utakat, városokat és kikötőket, Zadartól Splitig és mindenütt közöttük.",
    b6_h3="Vendégek barátként kezelve", b6_p="Az Ön hírneve minden vendéggel utazik. Úgy gondoskodom róluk, ahogy Ön tenné, hogy visszatérjenek Önhöz.",
    note_h2="Néhány szó sofőrtársaknak",
    note_p="Jelenleg nem keresek együttműködést más taxi- és transzferszolgáltatókkal. A kollégákat, akikkel dolgozom, továbbra is személyesen, egyenként választom ki, és ez a hálózat egyelőre teljes. Ha ez változik, itt jelzem.",
    talk_h2="Beszéljünk",
    talk_pre="Ha utazási iroda, apartman- vagy villatulajdonos, vagy ügynökség, és szeretne együttműködni, írjon egy e-mailt. Írja meg, ki Ön és mire van szüksége, és válassza a ",
    talk_suf=" témát, hogy tudjam, gyorsan kell válaszolnom.",
    email_word="E-mail", cta_btn="Írjon nekem",
    meta_title="Legyen partnerünk | TAXI Antonio Šibenik",
    meta_description="Utazási irodák, apartman- és villatulajdonosok és ügynökségek: működjön együtt egy megbízható helyi sofőrrel Šibenikben repülőtéri transzferekhez, kirándulásokhoz és vendégszállításhoz.",
    meta_keywords="taxi šibenik partner, transzfer partner šibenik, vendégtranszfer villa, utazási iroda szállítás dalmácia",
)

L["sk"] = dict(
    hero_eyebrow="Spolupráca", hero_h1="Staňte sa partnerom",
    hero_sub="Spoľahlivý miestny vodič pre vašich hostí, klientov a cestujúcich na pobreží Šibeniku.",
    intro_h2="Vodič, na ktorého sa môžete spoľahnúť",
    intro_p1="Som Antonio, miestny taxikár a vodič transferov medzi Šibenikom a Skradinom. Ak posielate ľudí do tejto časti Dalmácie, potrebujete niekoho na mieste, kto príde načas, zdvihne telefón a k vašim hosťom sa správa tak, ako by ste to urobili vy. Presne to robím, na každej jazde, osobne.",
    intro_p2="Spolupracujem s tromi druhmi partnerov. Ak ste jedným z nich, ozvite sa mi.",
    who_eyebrow="S kým spolupracujem", who_h2="Tri druhy partnerov",
    t1_h3="Cestovné kancelárie",
    t1_p="Zahraničné aj miestne: ak rezervujete transfery a výlety pre svojich klientov, som váš vodič na pobreží Šibeniku. Pevné ceny, jasné potvrdenia a jedna osoba, ktorá vám odpovedá priamo. Bez call centra medzi nami.",
    t2_h3="Majitelia apartmánov a víl",
    t2_p="Prenajímate hosťom a chcete, aby ich príchod prebehol hladko? Vyzdvihnem ich na letisku, doveziem k vašim dverám a na konci pobytu odveziem späť. Vaši hostia začínajú aj končia dovolenku v pokoji a vy sa o nich staráte od prvej minúty.",
    t3_h3="Agentúry",
    t3_p="Miestne a zahraničné agentúry, ktoré potrebujú spoľahlivého dopravcu na tomto pobreží: zabezpečujem letiskové transfery, medzimestské jazdy a výlety, s jednou kontaktnou osobou od prvej správy až po príchod.",
    villa1_eyebrow="Pre majiteľov apartmánov a víl",
    villa1_h2="O vašich hostí postarané od dverí k dverám",
    villa1_p1="Keď rodina pristane po dlhom lete, posledné, čo chce, je hľadať odvoz. Dajte im moje kontakty alebo mi pošlite čas príletu: privítam ich s menovkou, naložím batožinu a odveziem ich priamo k vášmu objektu.",
    villa1_p2="Na konci pobytu ich načas odveziem na letisko. Pre vás je to o starosť menej a váš objekt sa stane tým, ktorý odporúčajú priateľom.",
    villa1_alt="Prázdninová vila so záhradou pri Šibeniku, ktorej majitelia spolupracujú s TAXI Antonio na transferoch hostí",
    car_eyebrow="Čisté, pohodlné auto", car_h2="Profesionálna jazda, zakaždým",
    car_p1="Vaši hostia cestujú v čistom, klimatizovanom vozidle Škoda Superb s miestom až pre štyroch cestujúcich a ich batožinu a s Wi-Fi zadarmo. Pre väčšie skupiny zabezpečím dodávku cez prevereného kolegu a zostávam vašou jedinou kontaktnou osobou.",
    car_p2="Jazdím profesionálne viac ako desať rokov, na tomto pobreží aj na zimných letiskových transferoch v Rakúsku. Vaši hostia sú v skúsených rukách.",
    villa2_alt="Pohodlná spálňa v prázdninovej vile pri Šibeniku, ktorú obsluhuje TAXI Antonio transfermi hostí",
    why_eyebrow="Prečo spolupracovať so mnou", why_h2="Čo získate",
    b1_h3="Jedna kontaktná osoba", b1_p="Jednáte so mnou, nie so striedajúcimi sa vodičmi. Na správy odpovedám osobne, potvrdzujem priamo a preberám zodpovednosť, ak niečo nastane.",
    b2_h3="Pevné, čestné ceny", b2_p="Jasné ceny dohodnuté vopred, aby ste vy aj vaši klienti vždy poznali cenu. Žiadne prekvapenia na konci jazdy.",
    b3_h3="Vždy načas", b3_p="Sledujem lety, plánujem okolo trajektov a autobusov a počítam s časom, aby sa vaši ľudia dostali tam, kam potrebujú, bez zhonu.",
    b4_h3="Preverená sieť", b4_p="Keď som už obsadený alebo potrebujete väčšie vozidlo, priberiem starostlivo vybraných kolegov, ktorých osobne poznám, a vždy vám poviem koho a prečo.",
    b5_h3="Znalosť kraja", b5_p="Narodil som sa tu a tieto cesty, mestá a maríny poznám dokonale, od Zadaru po Split a všade medzi tým.",
    b6_h3="Hostia ako priatelia", b6_p="Vaša povesť cestuje s každým hosťom. Starám sa o nich tak, ako by ste to robili vy, aby sa k vám vracali.",
    note_h2="Slovo pre kolegov vodičov",
    note_p="Momentálne nehľadám spoluprácu s inými taxikármi a dopravcami. Kolegov, s ktorými pracujem, si stále vyberám osobne, jedného po druhom, a táto sieť je zatiaľ naplnená. Ak sa to zmení, napíšem to sem.",
    talk_h2="Poďme sa porozprávať",
    talk_pre="Ak ste cestovná kancelária, majiteľ apartmánu alebo vily, alebo agentúra a chcete spolupracovať, napíšte mi e-mail. Napíšte, kto ste a čo potrebujete, a ako tému zvoľte ",
    talk_suf=", aby som vedel, že mám odpovedať rýchlo.",
    email_word="E-mail", cta_btn="Kontaktujte ma",
    meta_title="Staňte sa partnerom | TAXI Antonio Šibenik",
    meta_description="Cestovné kancelárie, majitelia apartmánov a víl a agentúry: spolupracujte so spoľahlivým miestnym vodičom v Šibeniku na letiskových transferoch, výletoch a doprave hostí.",
    meta_keywords="taxi šibenik partner, transfer partner šibenik, transfery hostí vila, cestovná kancelária doprava dalmácia",
)


# ---------------------------------------------------------------- page template
def build_content(lang):
    d = L[lang]
    contact_url = page_url(lang, CONTACT[lang])
    subj = urllib.parse.quote(TOPIC[lang])
    mailto = "mailto:info@taxisibenik.hr?subject=%s" % subj
    talk_full = d["talk_pre"] + '"' + TOPIC[lang] + '"' + d["talk_suf"]
    return """  <section class="page-hero">
    <div class="container">
      <span class="eyebrow">{hero_eyebrow}</span>
      <h1>{hero_h1}</h1>
      <p class="page-hero-sub">{hero_sub}</p>
    </div>
  </section>

  <section class="page-content">
    <div class="container prose">
      <h2>{intro_h2}</h2>
      <p>{intro_p1}</p>
      <p>{intro_p2}</p>
    </div>
  </section>

  <section class="why-book">
    <div class="container">
      <span class="eyebrow center">{who_eyebrow}</span>
      <h2 class="section-title">{who_h2}</h2>
      <div class="why-book-grid">
        <div class="why-book-item">
          <h3>{t1_h3}</h3>
          <p>{t1_p}</p>
        </div>
        <div class="why-book-item">
          <h3>{t2_h3}</h3>
          <p>{t2_p}</p>
        </div>
        <div class="why-book-item">
          <h3>{t3_h3}</h3>
          <p>{t3_p}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="hub-prose-section hub-prose-white">
    <div class="container hub-prose-inner">
      <div class="hub-prose-image">
        <img src="/assets/img/partners-villa-garden.webp" alt="{villa1_alt}" loading="lazy">
      </div>
      <div class="hub-prose-text">
        <span class="eyebrow">{villa1_eyebrow}</span>
        <h2>{villa1_h2}</h2>
        <p>{villa1_p1}</p>
        <p>{villa1_p2}</p>
      </div>
    </div>
  </section>

  <section class="hub-prose-section">
    <div class="container hub-prose-inner">
      <div class="hub-prose-text">
        <span class="eyebrow">{car_eyebrow}</span>
        <h2>{car_h2}</h2>
        <p>{car_p1}</p>
        <p>{car_p2}</p>
      </div>
      <div class="hub-prose-image">
        <img src="/assets/img/partners-villa-bedroom.webp" alt="{villa2_alt}" loading="lazy">
      </div>
    </div>
  </section>

  <section class="why-book">
    <div class="container">
      <span class="eyebrow center">{why_eyebrow}</span>
      <h2 class="section-title">{why_h2}</h2>
      <div class="why-book-grid">
        <div class="why-book-item"><h3>{b1_h3}</h3><p>{b1_p}</p></div>
        <div class="why-book-item"><h3>{b2_h3}</h3><p>{b2_p}</p></div>
        <div class="why-book-item"><h3>{b3_h3}</h3><p>{b3_p}</p></div>
        <div class="why-book-item"><h3>{b4_h3}</h3><p>{b4_p}</p></div>
        <div class="why-book-item"><h3>{b5_h3}</h3><p>{b5_p}</p></div>
        <div class="why-book-item"><h3>{b6_h3}</h3><p>{b6_p}</p></div>
      </div>
    </div>
  </section>

  <section class="page-content">
    <div class="container prose">
      <h2>{note_h2}</h2>
      <p>{note_p}</p>

      <h2>{talk_h2}</h2>
      <p>{talk_full}</p>
      <p>{email_word}: <a href="{mailto}">info@taxisibenik.hr</a></p>
      <a href="{contact_url}" class="btn btn-primary">{cta_btn}</a>
    </div>
  </section>
""".format(talk_full=talk_full, mailto=mailto, contact_url=contact_url, **d)


def write_pages():
    for lang in LANGS:
        d = L[lang]
        out_dir = os.path.join(PAGES, "partners", lang)
        os.makedirs(out_dir, exist_ok=True)
        meta = {
            "slug": SLUG[lang],
            "title": d["meta_title"],
            "description": d["meta_description"],
            "keywords": d["meta_keywords"],
            "og_image": "https://taxisibenik.hr/assets/img/partners-villa-garden.webp",
            "schema": None,
        }
        with open(os.path.join(out_dir, "meta.json"), "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
        with open(os.path.join(out_dir, "content.html"), "w", encoding="utf-8") as f:
            f.write(build_content(lang))
        print("page:", lang, SLUG[lang])


def add_footer_link():
    for lang in LANGS:
        fname = "footer.html" if lang == "en" else "footer.%s.html" % lang
        path = os.path.join(PARTIALS, fname)
        with open(path, encoding="utf-8") as f:
            html = f.read()
        url = page_url(lang, SLUG[lang])
        if url in html:
            print("footer already has link:", lang)
            continue
        li = '        <li><a href="%s">%s</a></li>\n' % (url, BECOME[lang])
        # second <ul class="footer-links"> is the Support list
        first = html.index('<ul class="footer-links">')
        second = html.index('<ul class="footer-links">', first + 1)
        close = html.index('</ul>', second)
        # insert before the line that holds the closing </ul>
        line_start = html.rfind('\n', 0, close) + 1
        html = html[:line_start] + li + html[line_start:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("footer link added:", lang)


def add_topic_option():
    targets = []
    for lang in LANGS:
        targets.append(os.path.join(PAGES, "contact", lang, "content.html"))
        targets.append(os.path.join(PAGES, "home", lang, "content.html"))
    for path in targets:
        if not os.path.exists(path):
            continue
        lang = path.split(os.sep)[-2]
        with open(path, encoding="utf-8") as f:
            html = f.read()
        if 'value="Partnership proposal"' in html:
            print("topic already present:", path)
            continue
        anchor = '<option value="Complaint">'
        idx = html.find(anchor)
        if idx == -1:
            print("NO Complaint anchor:", path)
            continue
        line_start = html.rfind('\n', 0, idx) + 1
        indent = html[line_start:idx]
        opt = '%s<option value="Partnership proposal">%s</option>\n' % (indent, TOPIC[lang])
        html = html[:line_start] + opt + html[line_start:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("topic added:", lang, os.sep.join(path.split(os.sep)[-3:]))


if __name__ == "__main__":
    write_pages()
    add_footer_link()
    add_topic_option()
    print("done")
