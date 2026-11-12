---
name: toets-ai-act-hoog-risico
description: "Toetst de plichten bij een hoogrisico-AI-systeem, afhankelijk van je rol: gebruiksverantwoordelijke (art. 26), grondrechtentoets (art. 27), aanbieder (art. 16) of importeur en distributeur (art. 23 en 24). Gebruik bij \"hoogrisico AI\", \"grondrechtentoets\" of \"plichten als aanbieder van AI\"."
---

# /toets-ai-act-hoog-risico — AI-verordening: hoogrisicosystemen

Toetst de **plichten bij een hoogrisico-AI-systeem**, per rol: gebruiksverantwoordelijke (AI5), grondrechtentoets (AI6), aanbieder (AI7), importeur en distributeur (AI8).

> **Eerste beoordeling, geen juridisch advies.** Deze toets beoordeelt alleen wat de gebruiker aangeeft of aanlevert; ze kan niet nagaan of de antwoorden kloppen. De kaders rusten op de wettekst en officiële bronnen met peildatum 2026-11-10; wetgeving verandert, dus controleer bij twijfel de actuele tekst.

## Kaders in deze skill

- **AI5 — Hoog risico: plichten als gebruiker (art. 26)** (`./AI5-hoog-risico-plichten-als.md`): Controleren of een organisatie die een hoogrisico-AI-systeem onder haar verantwoordelijkheid gebruikt (gebruiksverantwoordelijke) de plichten van art. 26 AI-verordening naleeft, of zij door eigen handelen zelf aanbieder wordt (art. 25 lid 1), en of zij betrokkenen kan informeren en uitleg kan geven (art. 26 lid 11, art. 86).
- **AI6 — Hoog risico: grondrechtentoets (art. 27)** (`./AI6-hoog-risico-grondrechtentoets-art.md`): Controleren of een gebruiksverantwoordelijke die daartoe verplicht is, vóór het eerste gebruik van een hoogrisico-AI-systeem een beoordeling van de gevolgen voor de grondrechten uitvoert met de inhoud van art. 27 lid 1, die actueel houdt, de markttoezichtautoriteit op de hoogte brengt en laat aansluiten op de DPIA.
- **AI7 — Hoog risico: plichten als aanbieder (art. 16)** (`./AI7-hoog-risico-plichten-als.md`): Controleren of een aanbieder van een hoogrisico-AI-systeem de plichten van art. 16 AI-verordening heeft ingericht: de eisen aan het systeem (art. 9-15), kwaliteitsbeheer, documentatie en logs, conformiteitsbeoordeling, verklaring, CE-markering, registratie, corrigerende maatregelen, monitoring na het in de handel brengen en het melden van ernstige incidenten.
- **AI8 — Hoog risico: plichten als importeur of distributeur (art. 23 en 24)** (`./AI8-hoog-risico-plichten-als.md`): Controleren of een importeur (brengt een systeem van een aanbieder buiten de EU op de EU-markt) of distributeur (levert een systeem door zonder aanbieder of importeur te zijn) vóór het leveren de vereiste controles doet, niet-conforme systemen tegenhoudt, de juiste gegevens vermeldt, documentatie bewaart en bij risico's meldt.

Gebruik eerst de uitkomst van `/toets-ai-act-basis` (rol en signaal hoog risico); is die er niet, vraag de rol en doe AI0 uit de basistoets kort mee. Welk kader geldt hangt af van de rol; kies niet voor de gebruiker maar vraag, en geef daarna de kaders van die rol in één keer mee: gebruiksverantwoordelijke → AI5 en AI6 (de grondrechtentoets vervalt vanzelf als zij niet geldt), aanbieder → AI7, importeur of distributeur → AI8. Een vraag die in meer kaders staat, wordt dan één keer gesteld. **Datums:** de plichten in deze skill gelden pas vanaf 2 december 2027 (bijlage III) of 2 augustus 2028 (bijlage I); de kaders noemen dat bij "Van toepassing vanaf", en tot die datum is een ❌ een voorbereidingspunt (⚠️ met de datum). Is het systeem al vóór die datum in gebruik, noem dan art. 111 lid 2 (zie de regels van het kader).

## Werkwijze

`kader.py` (in de map van deze skill) rekent de vaste logica uit: welke vragen nu nodig zijn, welke toetspunten gelden en wat de kaderuitkomst is. Gebruik het als Python beschikbaar is; jij beoordeelt alleen de inhoud van de toetspunten. Zonder Python volg je dezelfde regels met de hand (zie "Uitkomsten en regels").

1. **Beginstand.** Zoek `compliance-register.md` (Project, bijlage of werkmap) en lees een aangeleverd document of eerdere antwoorden in dit gesprek. Zeg in één zin wat je gaat toetsen en kies het kader (of de kaders) uit de lijst hierboven; past geen kader duidelijk, geef dan alle kaders mee die in aanmerking komen (poortregels laten wat niet geldt vanzelf vervallen) in plaats van eerst te vragen welk kader past. Toetst het kader **per verwerking, toepassing, doel of leverancier**, neem dan "waarvoor is de toets?" als eerste vraag van het formulier mee (via `--extra`) en herhaal het formulier per stuk, met een eigen `antwoorden.json` per stuk; noemt de gebruiker meer stukken, zet ze dan als groepen in hetzelfde formulier en de organisatievragen één keer.
2. **Eén formulier met alle vragen.** Hieronder staat `<kaders>` voor het kaderbestand, of voor alle kaders die je toetst. Toets je meer kaders van deze skill, geef ze dan **in één keer** mee: `alle` (alle kaders van deze skill, in de volgorde van "Kaders in deze skill") of de bestanden die je kiest. Dan geldt één `antwoorden.json` en één `oordelen.json` voor alle kaders, wordt een vraag die in meer kaders staat één keer gesteld, en vervalt een kader dat volgens een eerder antwoord niet geldt (poortregel).
   - Is er een register: `python3 kader.py voorstel <kaders> --register compliance-register.md > voorstel.json` geeft antwoorden uit het profiel; die komen voorgevuld in het formulier (`--voorgesteld voorstel.json`). Doe hetzelfde met antwoorden uit een aangeleverd stuk (zet ze in `voorstel.json` als `{"sleutel": waarde}`).
   - `python3 kader.py formulier <kaders> …` maakt het ene formulier met alle vragen (route 1, 2 of 3 uit "Vragen stellen"); zet het antwoord in `antwoorden.json` (sleutel: antwoord; "weet ik niet" letterlijk). Controleer daarna met `python3 kader.py vragen <kaders> --antwoorden antwoorden.json` dat `klaar` waar is; staat er toch iets open, vraag dat dan in één bericht na.
   - **"Weet ik niet" mag, maar telt als niet ingevuld:** een toetspunt dat dat antwoord nodig heeft, voldoet niet tot het is ingevuld (bij een aanbeveling: in te vullen). Bij de kwalificatievragen van het kader is "weet ik niet" geen optie; zeg dat het antwoord eerst nodig is. Vraag niet om persoonsgegevens van individuele mensen.
3. **Toetsen.** `python3 kader.py stappen <kaders> --antwoorden antwoorden.json` zegt per toetspunt of het geldt, n.v.t. is of onzeker, welke antwoorden ontbreken en of een plicht pas vanaf een latere datum geldt. Beoordeel elk toetspunt dat geldt of onzeker is met de criteria van dat toetspunt en de "Regels van dit kader".
4. **Uitkomst.** Zet je oordelen in `oordelen.json` (`{"K2.1": "voldoet", …}`; een n.v.t. op grond van een kaderregel als `{"uitkomst": "n.v.t.", "reden": "…"}`) en draai `python3 kader.py uitkomst <kaders> --antwoorden antwoorden.json --oordelen oordelen.json`. Het script past de plafonds, poortregels en datums toe en berekent de kaderuitkomst per kader; neem die over zonder ze te veranderen en noem de opmerkingen die het geeft. Meldt het dat een kader "niet is uitgesloten", stel dan de vragen van dat kader alsnog.
5. **Rapport.** Lever:
   - de **kaderuitkomst** (bij meer kaders: per kader) met de kaderversie en de datum van vandaag;
   - een **tabel**: toetspunt · grondslag · uitkomst (✅ voldoet · ❌ voldoet niet · ⚠️ in te vullen · n.v.t.) · waarom, in één zin op basis van het antwoord;
   - per ⚠️ of ❌ **wat te doen** (het advies uit het referentiebestand, in gewone taal) en, bij ⚠️, de vraag voor de beoordelaar; bij een voorbereidingspunt de datum waarop de plicht gaat gelden;
   - **wat nog ontbreekt** (niet ingevulde antwoorden, ontbrekend document), met de toetspunten die daardoor niet voldoen;
   - **voorbehouden en open punten** van het kader (zie het referentiebestand), kort.
6. **Vervolg.** `python3 kader.py samenhang <kaders> --antwoorden antwoorden.json` geeft de vervolgkaders en skills die volgens de antwoorden in beeld komen (zeker of mogelijk); noem ze met de reden. Bied aan het rapport als bestand af te leveren en, als er een `compliance-register.md` is, de uitkomst te registreren via `/compliance-overzicht` ("registreer dit").

## Vragen stellen (aanklikbare velden)

**Eén formulier, geen rondes.** Alle vragen gaan in één keer naar de gebruiker, als één formulier met één Verstuur-knop. Vragen die door een antwoord niet meer nodig zijn, verdwijnen live uit het formulier (waar de route dat kan); wat overblijft telt `kader.py` zelf: antwoorden op vragen die niet gelden worden genegeerd en wat leeg blijft is onbekend. Je stelt dus nooit een vervolgronde; draai `kader.py vragen` na het formulier alleen om te controleren of `klaar` waar is.

Maak het formulier met `python3 kader.py formulier <kaders> [--antwoorden …] [--voorgesteld voorstel.json] [--extra extra.json]`. `--voorgesteld` vult antwoorden uit het register of een aangeleverd stuk voor. `--extra` voegt een groep vooraan toe met alles wat de skill buiten het kaderformulier vraagt: een keuze vooraf (rol, soort verzoek, voor welk doel of welke verwerking je toetst), de huisstijl-vraag als er geen huisstijl is en de "extra" vragen bij standaardbepalingen (namen, adres, KvK-nummer, termijnen, rechter): `[{"titel": "Voor we beginnen", "vragen": [{"sleutel": …, "vraag": …, "type": "enum", "opties": […], "verplicht": true}]}]`. Zo komt er na het formulier niets meer te vragen.

Kies de eerste route die kan:

1. **Widget in de chat** (bijvoorbeeld `show_widget`; roep eerst zijn `read_me` aan als dat vereist is): `python3 kader.py formulier <kaders> --html`, de uitvoer **ongewijzigd** als widgetcode. De antwoorden komen terug als bericht van de gebruiker met JSON `{sleutel: waarde}`; geef dat door als `--antwoorden`.
2. **Lokale pagina** (Claude Code op de computer van de gebruiker, zonder widgettool): `python3 kader.py formulier <kaders> --serve antwoorden.json`, op de achtergrond gestart. Het zet het formulier op `127.0.0.1`, opent de browser en schrijft de antwoorden naar `antwoorden.json` zodra de gebruiker verstuurt; wacht tot dat bestand er is (het commando eindigt dan) en lees het. Zeg erbij dat het formulier in de browser staat. Lukt de browser niet (externe of cloudsessie), neem dan route 3.
3. **Eén genummerde lijst in één bericht**: `python3 kader.py formulier <kaders> --tekst`, de uitvoer als bericht. De gebruiker antwoordt met "1: ja, 2: nee, …"; zet dat om naar `antwoorden.json` met de sleutels uit `python3 kader.py formulier <kaders>` (JSON, zelfde volgorde). Bij een keuzevraag staan de Nederlandse labels in `opties_nl`, in dezelfde volgorde als de codes in `opties`: de gebruiker kiest een label, jij zet de **code** in `antwoorden.json`. Overgeslagen = "weet ik niet". Is er een andere vraagtool, gebruik die dan niet voor losse rondes: zet alle vragen in één aanroep of in dit ene bericht.

Overige regels:

- **Labels en codes.** Toon de gebruiker altijd de Nederlandse labels (`opties_nl`) en nooit de Engelse codes; in `antwoorden.json` komt altijd de code. Het formulier doet dit zelf; kies je zelf een vraagtool (de golven), neem dan de labels over en vertaal het antwoord terug.
- **Niet beantwoord = onbekend.** Neem nooit zelf een antwoord aan; zet het op "weet ik niet" (`[IN TE VULLEN]` of ⚠️). Zeg in de samenvatting welke vragen onbeantwoord bleven. Een eigen tekst of opmerking van de gebruiker gaat voor op de opties en wordt gevolgd.
- **Controleer op tegenstrijdigheid** tussen antwoorden (bijvoorbeeld 2–9 medewerkers met een omzet boven € 10 miljoen) en vraag dat één keer na voordat je het gebruikt.
- Zet geen persoonsgegevens in een voorstel of voorgevulde waarde en verzin geen feiten over de organisatie.

## Uitkomsten en regels

Toon uitkomsten altijd met deze Nederlandse labels, nooit met de interne sleutels (*compliant*, *review*, *non_compliant*, *not_applicable*).

- **✅ voldoet**: op basis van de antwoorden voldoet het toetspunt, en je kunt de grondslag uit het referentiebestand noemen. Zonder noembare grondslag wordt het ⚠️.
- **❌ voldoet niet**: het vereiste ontbreekt, **of een antwoord dat nodig is, is niet ingevuld** ("weet ik niet" telt als niet ingevuld). Zeg dan welk antwoord ontbreekt; zodra het is ingevuld, toets je opnieuw.
- **⚠️ in te vullen**: een aanbeveling (een stap die niet meetelt) zonder antwoord, een afweging die een mens moet maken, of een plicht die pas later geldt.
- **n.v.t.** (*not_applicable*) ontstaat op drie manieren, en alleen zo: (1) de voorwaarde `Alleen als` (of de poortregel van het kader) is onwaar; (2) een regel van dit kader zegt het (noem de regel); (3) een kwalificatiestap met "Is het vereiste afwezig: n.v.t." waarbij het vereiste duidelijk afwezig is. In geval (3) gelden de regels van het kader niet: de kaderuitkomst is n.v.t. (bijvoorbeeld "de AVG is niet van toepassing").
- **Voorwaarden met drie waarden** (ja / nee / onbekend). In een voorwaarde is `facts.sleutel` het antwoord op de vraag met die sleutel. Een vergelijking met een onbekend antwoord is onbekend; `== null` is waar als het antwoord onbekend is. `and` is onwaar als een deel onwaar is, anders onbekend als een deel onbekend is; `or` is waar als een deel waar is, anders onbekend als een deel onbekend is. Een antwoord op een vraag die zelf niet gesteld hoefde te worden, maakt elke vergelijking ermee onwaar.
  - Een **vraag** stel je als haar voorwaarde waar of onbekend is.
  - Een **toetspunt** geldt bij waar, is n.v.t. bij onwaar, en geldt bij onbekend; het antwoord dat ontbreekt, maakt het ❌ voldoet niet (bij een stap die niet meetelt ⚠️ in te vullen).
- **Ontbreekt een antwoord** dat een toetspunt bij "Nodig" noemt, dan is dat toetspunt ❌ voldoet niet; bij een stap die niet meetelt is het ⚠️ in te vullen. Deze regel gaat voor wat een toetspunt zelf over ontbrekende antwoorden of "weet ik niet" zegt. Een vraag die door een eerder antwoord is vervallen, ontbreekt niet: die is n.v.t.
- In de criteria betekent *present* dat het vereiste aanwezig is, *absent* dat het ontbreekt of niet klopt. *Duidelijk geval* betekent dat de antwoorden geen redelijke twijfel laten; *geen duidelijk geval* betekent ⚠️.
- **Formele stap (F):** toets aan de criteria; ontbreekt het vereiste duidelijk, dan geldt de uitkomst bij "Is het vereiste afwezig". Een harde eis is een harde eis: maak van een duidelijk ❌ geen ⚠️ uit voorzichtigheid.
- **Afwegingsstap (A):** ✅ of ❌ alleen bij een duidelijk geval volgens de criteria; anders ⚠️. Een open norm (bijvoorbeeld "grote schaal") is zelden een duidelijk geval.
- **Hoogste uitkomst ⚠️:** een stap met die aanduiding (of een signalerende stap, of een stap die "altijd review" geeft) wordt nooit ✅. Ontbreekt bij zo'n stap een nodig antwoord en telt hij mee, dan is hij ❌.
- **Poortregel** (bovenaan een kader: "Geldt alleen als …"): onwaar → het hele kader is n.v.t. (een regel van het eerdere kader; de vragen ervan vervallen). Is de genoemde poortstap van het eerdere kader niet ✅, dan is het kader niet uitgesloten: stel de vragen alsnog en beoordeel het. Onbekend → het kader geldt. "Vervalt als kader X n.v.t. is": is X n.v.t., dan dit kader ook.
- **Datum** ("Van toepassing vanaf" bovenaan een kader, of "Geldt vanaf" bij een toetspunt): is die datum nog niet bereikt, dan wordt een ❌ een ⚠️, een **voorbereidingspunt** met de datum erbij. Hangt de datum af van een onbekend antwoord en kan hij al zijn verstreken, dan ook ⚠️. Een ✅ blijft ✅.
- **Kaderuitkomst:** is de poortregel onwaar of een kwalificatiestap n.v.t. volgens (3), dan is het kader n.v.t. Anders: is een stap die meetelt ❌, dan is het kader ❌. Anders, is een stap ⚠️ (of een stap die niet meetelt ❌), dan is het kader ⚠️. Anders is het kader ✅. Zijn alle stappen n.v.t., dan is het kader n.v.t. Een stap die niet meetelt, signaleert alleen.

## Harde regels

- **Verzin niets.** Geen feiten, bedragen, termijnen, wetsartikelen of rechtspraak die niet in het referentiebestand, in de antwoorden of in een aangeleverd stuk staan. Een artikel dat je noemt, staat in het referentiebestand bij "Grondslag".
- **Alleen wat de gebruiker zegt.** Je beoordeelt de antwoorden en aangeleverde stukken; je kunt niet controleren of ze kloppen. Zeg dat in het rapport.
- **De rekenregels winnen.** De kaderuitkomst volgt uit de regels hierboven (of uit `kader.py uitkomst`), niet uit een totaalindruk.
- **Nooit "je voldoet aan alles".** Een ✅ geldt voor dat toetspunt op basis van de antwoorden, niet voor de organisatie als geheel.
- **Niet ingevuld wat nodig is = ❌ voldoet niet.** Zeg welk antwoord ontbreekt. Raad niet en rond niet naar boven af.
- **Eerlijk over de status.** Noem in je afsluiting welke punten op een afweging of aanname rusten en dat dit een eerste beoordeling is op basis van de gegeven antwoorden.
- **Geen document zonder reden.** Lever een rapport, geen contract of verklaring, tenzij de gebruiker daarom vraagt en er een skill voor bestaat.
- **Sporen.** Noem aan het eind de kaderversie(s) en de peildatum waarop de beoordeling rustte.

## Referenties

- `./AI5-hoog-risico-plichten-als.md` — kader AI5 (Hoog risico: plichten als gebruiker (art. 26)) met alle vragen en toetspunten.
- `./AI6-hoog-risico-grondrechtentoets-art.md` — kader AI6 (Hoog risico: grondrechtentoets (art. 27)) met alle vragen en toetspunten.
- `./AI7-hoog-risico-plichten-als.md` — kader AI7 (Hoog risico: plichten als aanbieder (art. 16)) met alle vragen en toetspunten.
- `./AI8-hoog-risico-plichten-als.md` — kader AI8 (Hoog risico: plichten als importeur of distributeur (art. 23 en 24)) met alle vragen en toetspunten.
- `kader.py` — rekenhulp (Python, geen packages): `voorstel`, `vragen`, `stappen`, `uitkomst`, `samenhang` en `document` volgens de vaste regels van de kaders.
