# Bepalingen — sla

Peildatum 2026-11-10. Standaardkeuzes en gangbare formuleringen, afgeleid van professionele modellen en marktvoorwaarden (bronnen onderaan), in eigen woorden en afgestemd op Nederlands recht.

**Zo gebruik je dit bestand**
- De kadertekst (wat de wet eist) staat in het kader-bestand en blijft altijd staan; dit bestand vult de keuzes daaromheen.
- Een eigen clausule of huisstijl van de gebruiker gaat voor op een bibliotheekbepaling, nooit op de kadertekst.
- **Standaardkeuze** = neem op als de gebruiker niets kiest en meld dat in je afsluiting. **Marktpositie** en **marktrange** beschrijven wat gangbaar is; het is geen verplichting.
- Verzin geen getallen of bedragen die hier niet staan; vraag erom of schrijf `[IN TE VULLEN: …]`.
- De voorbeeldteksten zijn voorbeelden: pas ze aan op de partijtermen en de antwoorden.

## Bepalingen

Referentie: Common Paper Service Level Agreement v2.0 (CC BY 4.0), in eigen woorden en naar Nederlandse gebruiken aangepast. Alle percentages en termijnen zijn **keuzes**; de getallen hieronder zijn de gangbare marktposities, geen wettelijke eisen.

### 1. Beschikbaarheid meten
- **Marktpositie:** beschikbaarheid per kalendermaand = (beschikbare minuten − minuten downtime) ÷ beschikbare minuten. Gemeten door monitoring van de leverancier; de klant mag een eigen meting overleggen bij een betwisting.
- **Voorbeeldtekst:** "De Beschikbaarheid wordt per kalendermaand berekend als het aantal minuten in die maand waarin de Dienst beschikbaar was, gedeeld door het totaal aantal minuten in die maand, na aftrek van de Uitgesloten Downtime."
- **Doelwaarde:** vraag de gebruiker; vermeld in de afsluiting dat 99,5%, 99,9% en 99,95% per maand respectievelijk ongeveer 3,6 uur, 43 minuten en 22 minuten downtime toestaan (rekenkundig bij een maand van 30 dagen).

### 2. Uitgesloten downtime
- **Marktpositie:** geplande onderhoudsvensters (binnen het afgesproken venster of vooraf aangekondigd, bijv. ten minste 48 uur), overmacht, storingen in internet of apparatuur van derden buiten controle van de leverancier, gebruik in strijd met de voorwaarden, en storingen veroorzaakt door de klant.

### 3. Support en responstijden
- **Marktpositie:** responstijd = tijd tot een inhoudelijke bevestiging door een medewerker (een automatisch antwoord telt niet); categorieën naar ernst (kritiek, hoog, normaal, laag) met per categorie respons- en streeftijd voor herstel en de tijden waarbinnen support bereikbaar is (kantooruren of 24/7).
- **Standaardkeuze:** laat de gebruiker de uren en categorieën kiezen; neem geen tijden over die hij niet noemt.

### 4. Melden van storingen
- **Marktpositie:** de klant meldt via het afgesproken kanaal; de leverancier bevestigt, geeft updates tijdens kritieke storingen en levert na afloop een korte oorzaakanalyse.

### 5. Gevolgen bij het niet halen (servicecredits)
- **Marktpositie:** servicecredit = percentage van de maandvergoeding volgens een staffel; de klant claimt binnen **7 dagen** na afloop van de maand waarin de afspraak is gemist; credits alleen als korting op toekomstige facturen; **maximum 8%** van de vergoedingen (Common Paper).
- **Staffel (voorbeeld, naar keuze aanpassen):** hoe lager de beschikbaarheid, hoe hoger het credit, binnen het maximum; noem de gebruiker dat dit een voorbeeld is en geen marktnorm.

### 6. Chronisch falen
- **Marktpositie:** als de doelwaarde in **2 van 3** opeenvolgende maanden niet wordt gehaald, mag de klant met een opzegtermijn van 30 dagen opzeggen en krijgt hij het vooruitbetaalde deel naar rato terug.
- **Exclusieve remedie:** credits en opzegging vormen de enige vergoeding voor het niet halen van de SLA; het recht op schadevergoeding voor andere tekortkomingen blijft onverlet.

### 7. Back-ups, beveiliging en herstel
- **Marktpositie:** frequentie van back-ups, herstelpunt (RPO) en herstelduur (RTO) alleen noemen als de gebruiker ze kiest; geen getallen verzinnen. Verwijs voor beveiliging naar de verwerkersovereenkomst en het beveiligingsbeleid.

### 8. Rapportage en overleg
- **Marktpositie:** maandelijkse of kwartaalrapportage van beschikbaarheid en incidenten; jaarlijks evaluatiegesprek.

### 9. Exit
- **Marktpositie:** bij einde krijgt de klant zijn gegevens in een gangbaar formaat terug (zie `saas-overeenkomst` voor de overstapregels van de Data Act).

## Bronnen
- Common Paper, Service Level Agreement v2.0 (CC BY 4.0) — https://commonpaper.com/standards/service-level-agreement/
- NLdigital Voorwaarden 2025 (SLA en onderhoud).
