---
name: compliance-onboarding
description: "Eerste inrichting van je compliance-set: stelt alle relevante vragen over je organisatie, bepaalt welke verplichtingen gelden, legt je huisstijl vast en maakt het register waarop /compliance-overzicht draait. Gebruik bij \"compliance-onboarding\", \"aan de slag met compliance\", \"waar begin ik met compliance\" of \"stel mijn compliance-profiel en huisstijl in\"."
---

# /compliance-onboarding — Profiel, huisstijl en register inrichten

Brengt je organisatie in kaart en richt de set in: **(1)** een profiel, **(2)** de lijst met verplichtingen die voor jou gelden, **(3)** je huisstijl en eigen clausules, **(4)** het register waarop `/compliance-overzicht` zijn cijfers baseert. Daarna weet elke andere skill in deze set wie je bent en hoe je documenten eruit moeten zien.

> **Hulpmiddel, geen juridisch advies.** De uitkomst rust op de antwoorden van de gebruiker; ze kan niet nagaan of die kloppen. Bij elke verplichting beslist de bijbehorende toets-skill of ze echt geldt.

## Werkwijze

1. **Beginstand.** Zoek eerst `compliance-register.md` en `huisstijl.md` (Project, bijlage of werkmap). Bestaan ze, vraag dan of de gebruiker wil **bijwerken** (alleen wat veranderd is, via hetzelfde formulier met het register voorgevuld) of **opnieuw beginnen** (bestaand register niet overschrijven zonder ja). Bestaan ze niet, begin bij stap 2. Zeg in één zin wat je oplevert (profiel, verplichtingen, register, huisstijl) en dat het één formulier van ongeveer drie minuten is. De vraag "bijwerken of opnieuw beginnen" is de enige vraag die vóór het formulier mag komen, en alleen als er al een register is.
2. **Eén formulier.** Alle vragen staan in `onboarding-formulier.json` (in deze map; zes groepen, vragen die van een eerder antwoord afhangen verdwijnen vanzelf). Maak het formulier met `python3 kader.py formulier --extra onboarding-formulier.json` (met `--voorgesteld voorstel.json` als je antwoorden uit een aangeleverd document of het register kunt voorvullen) en toon het volgens "Vragen stellen" hieronder. Is er al een document aangeleverd (privacyverklaring, contract, beleid), lees dat eerst en vul antwoorden voor; de gebruiker controleert ze in het formulier. **"Weet ik niet" en niet-beantwoord blijven "onbekend"**; het wordt nooit "nee" en je neemt nooit zelf een antwoord aan. Zet de antwoorden om naar de profielsleutels zoals bovenaan `onboarding-vragen.md` staat.
3. **Toepasselijkheid.** Pas `toepasselijkheid.md` toe op de antwoorden. Toon de gebruiker één tabel: onderwerp · skill · **waarom** (het antwoord waarop het rust) · voorgestelde status (`open` / `n.v.t.`). Laat corrigeren. Beslis niet zelf over drempels en uitzonderingen: die horen bij de toets-skill (zie de regels bovenaan `toepasselijkheid.md`).
4. **Bestaande documenten** (groep 5 van het formulier). Zet een document dat al bestaat op `klaar` met `Afgerond op` (de datum die de gebruiker noemt; een bij benadering genoemde datum krijgt de opmerking "datum bij benadering") en, als de gebruiker dat wil, een `Volgende review`. Geef zelf geen reviewtermijn op; stel hooguit voor "elk jaar" en laat de gebruiker kiezen. Kent de gebruiker de datum niet, geef `"afgerond op="` (leeg) mee aan `register.py add`, want zonder die waarde vult het script vandaag in; laat `Afgerond op` dus leeg: het overzicht telt het document dan wel mee, maar niet in de trendlijn, en zegt dat.
5. **Huisstijl** (groep 6 van het formulier). Heeft de gebruiker een bestaand document, lees daar de huisstijl uit en laat bevestigen; anders de vier vragen uit `onboarding-vragen.md`. Standaardkeuzes en eigen clausules komen later via `huisstijl-en-standaardclausules`. Maak `huisstijl.md` volgens `../huisstijl-en-standaardclausules/huisstijl-sjabloon.md`; neem eigen clausules **letterlijk** over en verzin niets. Is die skill niet beschikbaar, gebruik dan de vragen H1–H4 en dezelfde structuur (Organisatie, Taal en toon, Opmaak, Standaardkeuzes, Nooit opnemen, Eigen clausules).
6. **Register bouwen.** Maak `compliance-register.md`:
   - Is Python beschikbaar, gebruik `register.py` (in deze map): `python3 register.py init compliance-register.md --org "<naam>"`, daarna per profielantwoord, verplichting en taak `python3 register.py add compliance-register.md <sectie> kolom=waarde …` (secties: profiel, verplichtingen, taken, risicos, activiteit; zie `register-sjabloon.md` voor de kolommen). Draai daarna `python3 register.py validate compliance-register.md` en herstel fouten.
   - Is Python niet beschikbaar, schrijf het bestand met dezelfde tabellen volgens `register-sjabloon.md`.
   - **Profiel:** elke vraagsleutel uit `onboarding-vragen.md` met het antwoord (`onbekend` als het onbekend is), plus `Organisatie` en `Register aangemaakt` (datum van vandaag).
   - **Verplichtingen:** één regel per gekozen onderwerp uit stap 3 met `Toepasselijk sinds` = datum van vandaag, tenzij de gebruiker een andere datum noemt.
   - **Taken:** maximaal drie startpunten uit de open verplichtingen, in de volgorde: (1) wat volgens de antwoorden het grootste gat is (bijvoorbeeld geen datalekprocedure, geen verwerkersovereenkomsten met leveranciers), (2) wat de toets-skills als eerste beslissen, (3) wat de gebruiker zelf noemde. Geef geen deadlines tenzij de gebruiker ze noemt of er een wettelijke datum uit de kaders bij hoort (noem dan de bron).
   - **Risico's:** alleen wat de gebruiker benoemt of wat rechtstreeks uit een antwoord volgt (bijvoorbeeld "geen tweestapsverificatie" bij beheerders); niveau schat de gebruiker, of laat het `middel` met de opmerking dat het een eerste inschatting is.
   - **Activiteit:** één regel "Onboarding doorlopen" met de datum.
7. **Opslaan.** Lever `compliance-register.md` en `huisstijl.md` als bestanden af en leg uit hoe ze worden hergebruikt (Claude onthoudt een bijlage niet vanzelf):
   - **Project (aanbevolen):** zet beide bestanden in de projectbestanden van een Project; elke chat in dat Project heeft ze bij de hand. Na elke wijziging het bijgewerkte bestand opnieuw uploaden of vervangen.
   - **Per chat:** voeg ze toe aan het gesprek waarin je `/compliance-overzicht` of een opstel-skill gebruikt.
   - **Werkmap (Claude Code):** laat ze in de map van het project staan; de skills lezen ze daar.
   - **Eigen skill:** `huisstijl.md` kan ook als skill `mijn-huisstijl` worden geüpload (Instellingen → Skills), zoals beschreven in `huisstijl-en-standaardclausules`. Het register hoort niet in een skill, omdat het verandert.
8. **Afsluiten.** Vat in vijf regels samen: aantal verplichtingen per domein, wat onbekend bleef, de eerste drie stappen met de skill erbij (`/privacyverklaring`, `/toets-grondslag`, enzovoort), en dat `/compliance-overzicht` nu het dashboard toont. Zeg eerlijk wat nog open is (onbekende antwoorden, toetsen die nog moeten beslissen).

## Vragen stellen (formulier)

Alle vragen gaan in **één formulier** met één Verstuur-knop. Kies de eerste route die kan:

1. **Widget in de chat** (bijvoorbeeld `show_widget`; roep eerst zijn `read_me` aan als dat vereist is): `python3 kader.py formulier --extra onboarding-formulier.json --html`, de uitvoer **ongewijzigd** als widgetcode. De antwoorden komen terug als JSON `{sleutel: waarde}` in een bericht van de gebruiker.
2. **Lokale pagina** (Claude Code op de computer van de gebruiker): `python3 kader.py formulier --extra onboarding-formulier.json --serve antwoorden.json` op de achtergrond; het opent de browser en schrijft de antwoorden naar `antwoorden.json` zodra de gebruiker verstuurt. Lukt dat niet, neem route 3.
3. **Eén genummerde lijst in één bericht**: `python3 kader.py formulier --extra onboarding-formulier.json --tekst`; de gebruiker antwoordt met "1: ja, 2: nee, …".

- **Niet beantwoord = onbekend.** Neem nooit zelf een antwoord aan; zet het op "weet ik niet" (`[IN TE VULLEN]` of ⚠️). Zeg in de samenvatting welke vragen onbeantwoord bleven. Een eigen tekst of opmerking van de gebruiker gaat voor op de opties en wordt gevolgd.
- **Controleer op tegenstrijdigheid** tussen antwoorden (bijvoorbeeld 2–9 medewerkers met een omzet boven € 10 miljoen) en vraag dat één keer na voordat je het gebruikt.

## Harde regels

- **Alles uit de antwoorden.** Geen aannames over de organisatie, geen invulling van wat niet is gezegd. Onbekend blijft onbekend en wordt een toets of vraag, geen "nee".
- **Geen cijfers verzinnen.** Het register bevat alleen wat de gebruiker heeft gezegd of wat uit de kaders volgt; er worden geen scores, risiconiveaus of deadlines "bij wijze van voorbeeld" ingevuld.
- **Toepasselijk is niet hetzelfde als verplicht.** De lijst zegt waar de gebruiker mee te maken kan hebben; de toets-skill beslist. Zeg dat bij de samenvatting.
- **Geen persoonsgegevens, geen geheimen.** Vraag niet naar namen van individuele personen, wachtwoorden, sleutels, BSN of bankgegevens; neem ze niet op in het register of de huisstijl. Namen van klanten of leveranciers zijn niet nodig; gebruik soorten ("cloudleverancier", "salarisadministratie").
- **Niet overschrijven.** Een bestaand register of huisstijlbestand wordt alleen vervangen na een uitdrukkelijk ja; anders werk je bij.
- **Voorrang** in documenten: wet (kadertekst) > eigen clausules uit `huisstijl.md` > bibliotheek.

## Referenties

- `onboarding-vragen.md` — de zes groepen, de afvinkregels en de sleutels van het profiel.
- `toepasselijkheid.md` — welk antwoord leidt tot welke verplichting en skill.
- `register-sjabloon.md` — kolommen, statuswaarden en voorbeeldregels van het register (zonder cijfers).
- `register.py` — maakt en onderhoudt het register en berekent het overzicht.
