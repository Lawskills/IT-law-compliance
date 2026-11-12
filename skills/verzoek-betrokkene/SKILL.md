---
name: verzoek-betrokkene
description: "Stelt het antwoord op aan iemand die zijn privacyrechten uitoefent (inzage, correctie, verwijdering, beperking, bezwaar, overdraagbaarheid), of een brief om de termijn te verlengen of het verzoek te weigeren (art. 12 t/m 22 AVG). Gebruik bij \"verzoek van betrokkene\", \"inzageverzoek\", \"verwijderverzoek\" of \"AVG-verzoek beantwoorden\"."
---

# /verzoek-betrokkene — Antwoord op een privacyverzoek

Stelt het **antwoord aan een betrokkene** op die zijn rechten uitoefent. Kaders: K6 (`K6-rechten-betrokkenen.md`) en voor enkele standaardzinnen K5 (`K5-privacyverklaring.md`).

> **Hulpmiddel, geen juridisch advies.** Dit document is opgesteld op basis van jouw antwoorden, de wettekst en gangbare marktpraktijk (peildatum 2026-11-10). Controleer feiten, bedragen en keuzes voordat je het gebruikt; voor een bijzondere situatie raadpleeg je een gespecialiseerd adviseur.

**Persoonsgegevens van de verzoeker.** Vraag niet naar de naam of gegevens van de verzoeker. In de aanhef komt `[IN TE VULLEN: naam van de betrokkene, vul je zelf in]`; de gebruiker vult dat zelf in, buiten dit gesprek. Een inzagekopie stelt de gebruiker zelf samen uit zijn systemen; jij schrijft de begeleidende brief.

## Eerst: welk verzoek en welk antwoord?

Stel dit als eerste aanroep van de eerste golf (stap 2, samen met de huisstijl-vraag); wat daarna nog nodig is (de vragen onder "Vragen per soort antwoord" en de kadervragen) komt samen in één tweede golf:

1. **Soort verzoek:** inzage · correctie · verwijdering · beperking · bezwaar · overdraagbaarheid.
2. **Soort antwoord:** antwoord (verzoek uitgevoerd) · verlenging van de termijn · weigering.
3. **Ontvangen op** (datum) en **kenmerk** (optioneel).

**Termijn.** Reageer zonder onredelijke vertraging en uiterlijk binnen één maand na ontvangst; verlenging met hooguit twee maanden kan bij complexe of veel verzoeken, mits je dat binnen de eerste maand meldt met de reden (art. 12 lid 3 AVG). Reken uit tot wanneer, en zeg het. Is de termijn al verstreken, zeg dat dan ronduit: dat is een open punt.

## Werkwijze

1. **Doel vaststellen.** Zeg in één zin welk document je gaat opstellen en voor wie. Is er al een document of situatie aangeleverd? Lees die eerst en vul daaruit alvast antwoorden in; vraag alleen naar wat er ontbreekt.
2. **Formulier: één intake.** Neem de vragen uit het kader (zie "Formulier" in het referentiebestand), of, als deze skill zelf een lijst "Vragen" noemt, die lijst. Is Python beschikbaar, gebruik dan `kader.py` (in de map van deze skill): `python3 kader.py voorstel <kader>.md --register compliance-register.md > voorstel.json` voor antwoorden uit het profiel (als er een register is) en `python3 kader.py vragen <kader>.md --antwoorden antwoorden.json --voorgesteld voorstel.json` voor de hele eerste golf; stel die **in één blok** (zie "Vragen stellen" hieronder) en neem in de eerste aanroep ook mee wat deze skill buiten het kaderformulier vraagt (een keuze vooraf, de huisstijl-vraag van stap 3 en de "extra" vragen bij de standaardbepalingen, zoals namen, adres, KvK-nummer, termijnen en rechter), zodat er na het formulier niets meer wordt nagevraagd. Draai `vragen` daarna opnieuw voor de vervolgvragen (tweede golf) tot `klaar` waar is. Regels:
   - Sla een vraag over als de voorwaarde (`Alleen vragen als`) onwaar is; is de voorwaarde onbekend, stel de vraag wel.
   - **"Weet ik niet" is altijd een geldig antwoord**; dan komt er een `[IN TE VULLEN: …]` in het document.
   - Vul antwoorden voor, als ze al uit het register, eerdere antwoorden of aangeleverde stukken volgen, en laat de gebruiker die in één keer bevestigen (`--voorgesteld`).
   - Vraag niet om persoonsgegevens van individuele mensen (zoals een verzoeker of een betrokkene); die vult de gebruiker zelf in.
3. **Huisstijl en eigen clausules.** Kijk **vóór stap 2** of de gebruiker een huisstijl of eigen standaardclausules heeft: een bijgevoegd bestand `huisstijl.md`, een skill `mijn-huisstijl`, een eerder contract of een document in het Project. Is dat er, gebruik het (zie `/huisstijl-en-standaardclausules`). Is het er niet, dan gaat de vraag of de gebruiker er een heeft als één vraag mee in het formulier van stap 2 (`--extra`) (*Nee, gebruik de standaard* · *Ja, ik lever ze aan*); stel haar niet apart en ga bij geen antwoord door met de standaard. Volgorde van voorrang: (1) wat de wet eist (kadertekst), (2) eigen clausules van de gebruiker, (3) de bibliotheek in `bepalingen.md`.
4. **Samenvatting.** Toon vóór het schrijven kort wat je gaat opstellen, welke standaardkeuzes uit `bepalingen.md` je neemt en welke antwoorden ontbreken. Ga door als de gebruiker niets corrigeert.
5. **Opstellen.** Heeft het kader een "Opbouw van het document", zet dan eerst de kaderteksten klaar met `python3 kader.py document <kader>.md --antwoorden antwoorden.json --tekst`: dat levert de teksten in de juiste volgorde, laat weg wat volgens de voorwaarden niet geldt en zet `[IN TE VULLEN: …]` waar een antwoord ontbreekt. Volg de volgorde en de teksten uit het referentiebestand; vul keuzes rond de kadertekst met de bepalingen uit `bepalingen.md` (eigen woorden, marktpositie, bronnen erin) en pas ze aan de antwoorden aan. Vul `{{facts.x}}` met het antwoord. Gebruik de vragen per soort antwoord hieronder, niet het volledige kaderformulier.
6. **Eindcontrole.** Loop de toetspunten uit het referentiebestand langs en toon een tabel: toetspunt · grondslag · gedekt (ja / deels / nee) · wat nog moet. Een onderdeel met een `[IN TE VULLEN]` is nooit "ja".
7. **Aflevering.** Lever het document als Markdown in de chat of als bestand. Wil de gebruiker Word of PDF, maak dat dan van dezelfde tekst. Sluit af met de lijst van openstaande `[IN TE VULLEN]`-punten.

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

## Vragen per soort antwoord

**Verlenging van de termijn**
- **new_deadline** — Wanneer krijgt de persoon uiterlijk antwoord? (Hooguit twee maanden na de eerste termijn van een maand; stel de uiterste datum zelf voor op basis van de ontvangstdatum.)
- **reason** — Waarom heb je meer tijd nodig? (Alleen vanwege de complexiteit van het verzoek of het aantal verzoeken, art. 12 lid 3 AVG.)
- **contact** — Via welk e-mailadres of telefoonnummer kan de persoon je bereiken?

**Weigering**
- **reason** — Waarom geef je (deels) geen gevolg aan het verzoek? (Bijvoorbeeld een wettelijke uitzondering, of het verzoek is kennelijk ongegrond of buitensporig, art. 12 lid 5 AVG. Bezwaar tegen direct marketing weiger je nooit, art. 21 lid 3 AVG: wijs de gebruiker hierop.)
- **contact**

**Inzage — antwoord**
- **purposes** — waarvoor gebruik je de gegevens van deze persoon?
- **categories** — welke soorten gegevens heb je van deze persoon?
- **recipients** — aan welke organisaties heb je de gegevens gegeven of geef je ze (bij naam, ook buiten de EER; HvJEU C-154/21)?
- **retention** — hoe lang bewaar je de gegevens, of volgens welke criteria?
- **source** — van wie kreeg je gegevens, als dat niet de persoon zelf was? (Alles van de persoon zelf: "van de persoon zelf".)
- **automated** — neem je automatisch besluiten over deze persoon? Zo ja: hoe werkt dat en wat zijn de gevolgen?
- **contact**

**Correctie, verwijdering, beperking, bezwaar, overdraagbaarheid — antwoord**
- **done** — wat heb je precies gedaan, en wanneer?
- **recipients_informed** — (bij correctie, verwijdering, beperking) welke organisaties die de gegevens kregen heb je ingelicht, of waarom was dat niet mogelijk? (art. 19 AVG)
- **contact**

## Opbouw per soort antwoord

Altijd: **Aanhef** — "Op [ontvangstdatum] ontvingen wij je verzoek (kenmerk …) om [inzage in / correctie van / verwijdering van / beperking van het gebruik van / bezwaar tegen / overdracht van] je persoonsgegevens."

- **Verlenging:** Aanhef → *Verlenging van de termijn* (uiterste datum + reden; K6.2) → Afsluiting.
- **Weigering:** Aanhef → *Waarom wij geen gevolg geven aan je verzoek* (reden; K6.9) → *Klacht en beroep* (klacht bij de Autoriteit Persoonsgegevens, www.autoriteitpersoonsgegevens.nl, en naar de rechter stappen; K6.9) → Afsluiting.
- **Inzage:** Aanhef → *Kopie van je gegevens* (bijlage; gegevens over andere mensen onleesbaar gemaakt; K6.5) → *Waarvoor wij je gegevens gebruiken* → *Welke soorten gegevens* → *Aan wie wij je gegevens geven* → *Hoe lang wij je gegevens bewaren* → *Je andere rechten* (uit K5.8) → *Klacht indienen* (uit K5.10) → *Waar wij je gegevens vandaan hebben* → *Automatische besluiten* → Afsluiting.
- **Overige verzoeken:** Aanhef → *Wat wij hebben gedaan* (K6.6 verwijdering, K6.7 bezwaar, K6.8 overig) → bij correctie/verwijdering/beperking *Organisaties die je gegevens kregen* (K6.8) → *Klacht indienen* → Afsluiting.
- **Afsluiting:** "Heb je vragen? Neem contact met ons op via [contact]. Met vriendelijke groet, [organisatie]".

Het antwoord is in de je-vorm en in gewone taal.

## Bepalingen en huisstijl

- `bepalingen.md` bevat de standaardkeuzes en gangbare formuleringen (marktpositie, met bronnen en peildatum) voor de onderdelen rond de kadertekst. Waar elders in deze skill staat dat iets een keuze van de gebruiker is: vraag het eerst; antwoordt de gebruiker niet of "weet ik niet", neem dan de standaardkeuze uit `bepalingen.md` en noem die in je afsluiting. Staat er in `bepalingen.md` geen standaardkeuze (bijvoorbeeld een beschikbaarheidspercentage, een bedrag of een naam), dan blijft het een `[IN TE VULLEN: …]`.
- Heeft de gebruiker een eigen huisstijl of eigen standaardclausules (zie `/huisstijl-en-standaardclausules`)? Dan gaan die voor de bibliotheek, maar nooit voor wat de wet eist.

## Harde regels

- **Verzin niets.** Geen feiten, bedragen, termijnen, wetsartikelen of rechtspraak die niet in het referentiebestand, in de antwoorden of in een aangeleverd stuk staan. Een artikel dat je noemt, staat in het referentiebestand bij "Grondslag".
- **Kadertekst blijft staan.** Wat de wet of het toetspunt eist (de teksten uit het referentiebestand) laat je niet weg en zwak je niet af. Je mag verbindende zinnen toevoegen (partijen, ondertekening, datum), geen nieuwe verplichtingen of beperkingen.
- **Onzeker of onbekend = zichtbaar.** Schrijf `[IN TE VULLEN: wat er nodig is]`, en raad niet.
- **Eerlijk over keuzes.** Noem in je afsluiting welke onderdelen op een standaardkeuze uit `bepalingen.md` of op een aanname rusten, en welke `[IN TE VULLEN]`-punten openstaan.
- **Huisstijl en eigen clausules gaan voor, de wet gaat voor alles.** Een eigen clausule van de gebruiker vervangt de bibliotheekbepaling op dezelfde plek, maar nooit de kadertekst (wat de wet eist). Strijdt een eigen clausule met het kader, zeg dat en stel een aangepaste formulering voor.
- **Aanspreekvorm.** Volg `huisstijl.md` als die er is; anders schrijf je verklaringen voor het publiek en brieven in de je-vorm, en contracten in de derde persoon met de gedefinieerde termen. Pas de aanspreekvorm van een kadertekst daarop aan; dat is geen inhoudelijke wijziging.
- **Datum.** Gebruik de datum van vandaag alleen waar een datum nodig is (opgesteld op); verzin geen ingangsdata of termijnen.
- **Sporen.** Noem aan het eind de kaderversie en de peildatum (zie referentiebestand) zodat later te zien is waarop het document rustte.

## Referentie

- `K6-rechten-betrokkenen.md` — kader K6 (rechten van betrokkenen).
- `K5-privacyverklaring.md` — kader K5 (voor de zinnen over rechten en klachten, K5.8 en K5.10).
- `bepalingen.md` — standaardkeuzes en gangbare formuleringen met bronnen en peildatum.
- `kader.py` — rekenhulp (Python, geen packages): `voorstel`, `vragen`, `stappen`, `uitkomst`, `samenhang` en `document` volgens de vaste regels van de kaders.
