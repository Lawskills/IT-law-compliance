---
name: compliance-overzicht
description: "Toont je compliance-dashboard als widgets in de chat: voortgang per domein, trendlijn per maand, open risico's, taken, recente activiteit en volgende stappen, berekend uit jouw eigen register. Gebruik bij \"compliance-overzicht\", \"compliance-dashboard\", \"hoe staan we ervoor met compliance\" of \"registreer: ...\" om het register bij te werken."
---

# /compliance-overzicht — Dashboard uit je eigen register

Toont de stand van je compliance als **widgets** in de chat, in deze volgorde: kop met totaalvoortgang → kaarten per domein (Privacy, Informatiebeveiliging, AI & cyber, Contracten) → **trendlijn per maand** → risicoverdeling → volgende stappen → open taken → recente activiteit. Elk getal wordt berekend uit `compliance-register.md`; er zijn geen vaste waarden of voorbeeldcijfers. Wat niet in het register staat, bestaat voor het overzicht niet, en een leeg onderdeel toont een lege staat.

> **Voortgangsmaat, geen oordeel.** De voortgang is het aandeel verplichtingen in jouw register met status `klaar`. Ze zegt niets over de kwaliteit van de documenten en is geen juridisch advies; zeg dat bij het overzicht.

## Werkwijze

1. **Register zoeken.** Zoek `compliance-register.md` in de bijlagen, de projectbestanden of de werkmap. Is er geen register, zeg dat in één zin en verwijs naar `/compliance-onboarding`; toon geen dashboard met verzonnen cijfers. Is er een register maar het is leeg (alleen profiel), toon dan de lege staat (`register.py html` doet dat zelf).
2. **Valideren.** Draai `python3 register.py validate compliance-register.md` (script in deze map). Meld fouten (onbekende status, ongeldige datum) en laat de gebruiker kiezen: eerst corrigeren, of tonen met de waarschuwingen die het overzicht zelf vermeldt.
3. **Berekenen.** Draai `python3 register.py metrics compliance-register.md` voor de cijfers (JSON) en `python3 register.py html compliance-register.md` voor de widgets. De datum van vandaag wordt vanzelf gebruikt; geef bij twijfel `--today JJJJ-MM-DD` mee. Is Python niet beschikbaar, reken dan met de regels uit `register-sjabloon.md` (in deze map; samengevat onderaan) en toon bij elk percentage "x van y".
4. **Tonen.** Kies de eerste route die beschikbaar is (zie `widgets.md`):
   1. een visualisatietool voor widgets in de chat (bijvoorbeeld `show_widget`; roep eerst zijn `read_me` aan als dat vereist is) met de uitvoer van `register.py html`;
   2. een HTML-artifact (schrijf de uitvoer naar een `.html`-bestand en publiceer die als de omgeving dat toestaat);
   3. de diagramtool voor een lijngrafiek (`chart_display_v0`, serie uit `trend` in de JSON) plus het tekstoverzicht van `register.py text`;
   4. alleen het tekstoverzicht.
   Wijzig de cijfers niet bij het tonen en voeg geen waarden toe.
5. **Toelichting in de reply.** Maximaal vijf regels naast de widgets: de grootste beweging sinds vorige maand (uit `trend`), het belangrijkste open punt, en wat in de waarschuwingen staat (bijvoorbeeld "klaar zonder afrondingsdatum": die verplichtingen tellen mee in de score maar niet in de trend). Eindig met de eerste volgende stap en de skill die erbij hoort.
6. **Bijwerken.** Zegt de gebruiker "registreer: …" of "registreer dit", pas dan het register aan (zie hieronder), toon de wijziging in één regel per aanpassing en lever het bijgewerkte bestand af. Toon daarna alleen een nieuw overzicht als de gebruiker dat vraagt.
7. **Documenten uit deze chat.** Zijn in dit gesprek skills uit deze set gebruikt (een document opgesteld, een toets uitgevoerd) en staat dat nog niet in het register, bied dan één keer aan het te registreren: verplichting op `klaar` met `Afgerond op` = vandaag en een activiteitsregel. Registreer niets zonder ja.

## Bijwerken van het register

- Gebruik `python3 register.py add|set compliance-register.md <sectie> …` (zie `python3 register.py --help`) of pas de tabellen rechtstreeks aan met dezelfde kolommen.
- Ontbreekt er iets bij een "registreer"-opdracht (status, datum, niveau, prioriteit, domein), vraag het met `AskUserQuestion` als aanklikbare velden (opties uit de toegestane waarden, hooguit vier vragen per aanroep); een niet-beantwoorde vraag blijft leeg of onbekend, nooit zelf aannemen.
- Alleen wat de gebruiker zegt. Geen status `klaar` zonder dat de gebruiker bevestigt dat het document klaar is; geen risiconiveau of deadline die de gebruiker niet noemde (vraag erom).
- Een toets met ⚠️ of ❌ levert een taak of risico op alleen met bevestiging van de gebruiker; stel het voor met de bron (welk toetspunt).
- Nieuwe verplichting? Controleer dat `Domein` exact `Privacy`, `Informatiebeveiliging`, `AI & cyber` of `Contracten` is en dat `Skill` een bestaande skill uit de set is.
- Lever het hele bijgewerkte bestand af en herinner eraan dat het bestand in het Project (of in de chat) moet worden vervangen; Claude onthoudt een bijlage niet vanzelf.

## Rekenregels (als `register.py` niet draait)

- **Voortgang domein** = verplichtingen `klaar` ÷ toepasselijke verplichtingen (alles behalve `n.v.t.`), afgerond op een geheel getal; zonder toepasselijke verplichtingen: `—`.
- **Totaal** = zelfde berekening over alles. Alle verplichtingen wegen even zwaar.
- **Trend** = per maandeinde: verplichtingen met `Afgerond op` ≤ maandeinde ÷ verplichtingen met `Toepasselijk sinds` ≤ maandeinde; de huidige maand gebruikt de huidige stand. Minder dan twee maanden data: toon een enkel punt en zeg dat de lijn vanaf de tweede maand verschijnt.
- **Risico's** = status `open`, per niveau. **Taken** = status `open`, op deadline; te laat = deadline vóór vandaag.
- **Volgende stappen** = te late taken, open hoge risico's, verlopen reviews, deadlines binnen 30 dagen, open verplichtingen, lopende verplichtingen.

## Harde regels

- **Alles uit het register.** Geen vaste voorbeeldwaarden, geen geschatte cijfers, geen trend die niet uit datums in het register volgt. Ontbreekt data, toon een lege staat en zeg wat er nodig is.
- **Methode vermelden.** De voetnoot over wat de voortgang wel en niet is, blijft in elk overzicht staan.
- **Geen oordeel.** Een hoge voortgang betekent niet dat de organisatie voldoet; een lage niet dat ze niet voldoet. Zeg dat als de gebruiker het getal als nalevingsscore gebruikt.
- **Geen persoonsgegevens** in het register of in het overzicht.
- **Bronnen.** Wil de gebruiker weten waarop een verplichting rust, verwijs naar `/compliance-chat`.

## Referenties

- `register.py` — berekent de cijfers en rendert de widgets (`metrics`, `html`, `text`, `validate`, `add`, `set`).
- `widgets.md` — welke weergaveroute je kiest en wat elk widget toont.
