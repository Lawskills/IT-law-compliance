---
name: huisstijl-en-standaardclausules
description: "Legt je eigen huisstijl en standaardclausules vast (naam, toon, opmaak, gedefinieerde termen, eigen clausules per onderwerp) in één bestand dat alle opstel-skills gebruiken, uit een bestaand contract of via een korte vragenlijst. Gebruik bij \"huisstijl instellen\", \"eigen standaardclausules\" of \"gebruik mijn eigen voorwaarden\"."
---

# /huisstijl-en-standaardclausules — Eigen huisstijl en clausules vastleggen

Maakt één bestand, `huisstijl.md`, met hoe jouw organisatie documenten opstelt en welke eigen standaardclausules ze gebruikt. Elke opstel-skill (verwerkersovereenkomst, algemene voorwaarden, NDA, SLA, beleidsstukken, enzovoort) leest dat bestand en past het toe, zonder dat wat de wet eist verloren gaat.

> **Hulpmiddel, geen juridisch advies.** Eigen clausules worden overgenomen zoals je ze aanlevert; deze skill beoordeelt ze alleen op strijd met de kadertekst van de skill waarin ze worden gebruikt.

## Werkwijze

1. **Route kiezen zonder vraag.** Is er een document bijgevoegd of in het Project (eigen contract, algemene voorwaarden, beleid), neem dan route (a) en stel in dezelfde golf alleen de vragen uit de vragenlijst die het document niet beantwoordt; is er geen document, neem dan route (b) en stel de hele vragenlijst. Vraag niet eerst welke route de gebruiker wil: een mix gebeurt vanzelf.
2. **Uit een document (a).** Lees het document en haal eruit: naam en rechtsvorm van de organisatie, aanspreekvorm en toon, gedefinieerde termen (bijv. Opdrachtgever/Opdrachtnemer of Klant/Leverancier), nummering en kopstijl, en per onderwerp de **eigen clausules, letterlijk**. Zet elke clausule onder het onderwerp dat in `bepalingen.md` van de betreffende skill voorkomt (bijv. "Aansprakelijkheid", "Duur", "Subverwerkers"). Toon wat je hebt gevonden en laat de gebruiker corrigeren.
3. **Vragenlijst (b).** Gebruik `huisstijl-sjabloon.md`: stel de vragen als aanklikbare velden, alle twaalf in één golf van drie aanroepen in één blok (zie "Vragen stellen" hieronder). "Weet ik niet" of "geen voorkeur" is een geldig antwoord: laat dat onderdeel dan leeg, zodat de bibliotheek geldt.
4. **Samenstellen.** Maak `huisstijl.md` volgens `huisstijl-sjabloon.md`. Neem eigen clausules **letterlijk** over en vul niets aan. Noem geen namen van klanten of andere vertrouwelijke gegevens in het bestand.
5. **Opslaan en gebruiken.** Lever het bestand af en leg uit hoe het wordt hergebruikt; Claude onthoudt een bijlage niet vanzelf:
   - **Project:** zet `huisstijl.md` in de projectbestanden van een Project; elke chat in dat Project heeft het dan bij de hand (aanbevolen).
   - **Eigen skill:** maak er een skill `mijn-huisstijl` van (een map met `SKILL.md`, naam en beschrijving, met de inhoud van `huisstijl.md`) en upload die via Instellingen → Skills; dan is het in elke chat beschikbaar. Bied aan de `SKILL.md` klaar te zetten.
   - **Per chat:** voeg het bestand toe aan het gesprek waarin je een document opstelt.
6. **Bij gebruik door een opstel-skill.** De skill leest `huisstijl.md`, past opmaak, termen en toon toe en vervangt de bibliotheekbepaling door de eigen clausule. Bij strijd met de kadertekst meldt de skill dat en stelt een aangepaste formulering voor; de kadertekst blijft staan.

## Vragen stellen (aanklikbare velden)

Stel **alle** vragen als aanklikbare velden met `AskUserQuestion`, ook de open vragen, zodat de gebruiker snel klaar is. Is die tool er niet, stel dan dezelfde vragen als genummerde lijst, elk met voorgestelde antwoorden.

**Eén blok per golf.** Doe alle aanroepen van een golf in hetzelfde blok, dus zonder tussendoor tekst te schrijven of een script te draaien, en ga pas verder als de hele golf is beantwoord. Toont de omgeving ze één voor één of weigert ze gelijktijdig, stel ze dan direct na elkaar, nog steeds zonder tussenstappen.
- **Per aanroep hooguit vier vragen**, gegroepeerd per onderwerp, en zo weinig aanroepen als mogelijk. Maak elke vraag zelfstandig leesbaar; zet in de beschrijving van een optie een korte uitleg of voorbeeld (uit de `Hulp` bij de vraag in het kader).
- **Ja/nee** → opties *Ja*, *Nee* en, waar dat mag, *Weet ik niet*. **Keuzevraag** → de keuzes uit het kader in gewone taal (meer dan vier: groepeer of splits in twee vragen). **"Welke …?" of meerdere mogelijk** → `multiSelect`. **Aantal of omvang** → bereiken.
- **Open vraag** (omschrijving, doel, maatregel, naam) → twee tot vier **antwoordsuggesties** die uit het kader, de voorbeelden bij de vraag, eerdere antwoorden of een aangeleverd stuk komen; de gebruiker typt een eigen antwoord via "Other". Is er geen zinvolle suggestie (bijvoorbeeld een naam), bied dan twee opties die de situatie indelen en laat de tekst typen. Een suggestie is pas een antwoord als de gebruiker erop klikt. Verzin geen feiten over de organisatie en zet geen persoonsgegevens in een optie.
- **Voorgevulde antwoorden** (uit een aangeleverd stuk of eerdere antwoorden) leg je in dezelfde ronde voor ter bevestiging, met "(voorgesteld)" bij de eerste optie.
- **Niet beantwoord = onbekend.** Neem nooit zelf een antwoord aan; vraag hooguit één keer opnieuw en zet het anders op "weet ik niet" (`[IN TE VULLEN]` of ⚠️). Zeg in de samenvatting welke vragen onbeantwoord bleven. Een eigen tekst of opmerking van de gebruiker gaat voor op de opties en wordt gevolgd, ook als die om iets anders vraagt.
- **Controleer op tegenstrijdigheid** tussen antwoorden (bijvoorbeeld 2–9 medewerkers met een omzet boven € 10 miljoen) en vraag dat één keer na voordat je het gebruikt.

## Harde regels

- **Verzin geen clausules.** Alleen wat de gebruiker aanlevert of kiest komt in `huisstijl.md`.
- **Letterlijk overnemen.** Pas eigen clausules niet stilzwijgend aan; stel wijzigingen voor en laat de gebruiker beslissen.
- **Voorrang.** Wet (kadertekst) > eigen clausules > bibliotheek. Zeg het als een eigen clausule onder het wettelijk minimum valt (bijvoorbeeld een datalekmeldtermijn die langer is dan de wet toestaat).
- **Eigen materiaal.** Neem geen clausules uit andermans contract over zonder dat de gebruiker de rechten daarop heeft; vraag bij twijfel naar de herkomst.
- **Geen persoonsgegevens of vertrouwelijke klantinformatie** in het huisstijlbestand.

## Referenties

- `huisstijl-sjabloon.md` — de structuur van `huisstijl.md` en de vragenlijst.
