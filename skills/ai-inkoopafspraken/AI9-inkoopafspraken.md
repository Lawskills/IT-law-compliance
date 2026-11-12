# Kader AI9 — Afspraken bij inkoop van AI

Versie 0.3 · peildatum 2026-11-10

Doel: Controleren of afspraken bij de inkoop van AI de informatie, technische toegang en bijstand regelen die nodig zijn om aan de AI-verordening te voldoen (verplicht bij onderdelen van een hoogrisicosysteem), en de gebruikelijke waarborgen bevatten over documentatie, data, menselijk toezicht, kwaliteit, logging, incidenten, persoonsgegevens en audits.

Bronnen: AIVO-art12-lid1 (AI-verordening art. 12 lid 1); AIVO-art13-lid1 (AI-verordening art. 13 lid 1); AIVO-art14-lid1 (AI-verordening art. 14 lid 1); AIVO-art15-lid1 (AI-verordening art. 15 lid 1); AIVO-art25-lid4 (AI-verordening art. 25 lid 4); AIVO-art26-lid1 (AI-verordening art. 26 lid 1); AIVO-art26-lid6 (AI-verordening art. 26 lid 6); AIVO-art73-lid1 (AI-verordening art. 73 lid 1); AVG-art28-lid3 (AVG art. 28 lid 3); EC-MCC-AI (Europese modelcontractbepalingen voor de aanbesteding van AI (versies voor hoog risico en niet-hoog risico))

## Formulier (vragen aan de gebruiker)

- **supplier_name**: Welke leverancier levert de AI?
  - Label (voor de plek-om-in-te-vullen): naam van de leverancier
  - Type: text
- **buyer_name**: Wie neemt de AI af?
  - Label (voor de plek-om-in-te-vullen): naam van de afnemer
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **high_risk**: Gaat het om een hoogrisico-AI-systeem, of om een onderdeel daarvan?
  - Label (voor de plek-om-in-te-vullen): of het om een hoogrisicosysteem gaat
  - Type: boolean
- **buyer_is_provider**: Bouw je zelf een hoogrisicosysteem waarin je het onderdeel van de leverancier gebruikt (jij bent dan aanbieder)?
  - Label (voor de plek-om-in-te-vullen): of jij de aanbieder van het hoogrisicosysteem bent
  - Type: boolean · Alleen vragen als: `facts.high_risk != false`
- **free_open_source**: Is het onderdeel gratis en open source (niet als betaalde dienst geleverd)?
  - Label (voor de plek-om-in-te-vullen): of het gratis open source is
  - Type: boolean · Alleen vragen als: `facts.high_risk != false and facts.buyer_is_provider != false`
- **personal_data**: Verwerkt de leverancier persoonsgegevens voor jou (bijvoorbeeld invoer in het systeem)?
  - Label (voor de plek-om-in-te-vullen): of de leverancier persoonsgegevens verwerkt
  - Type: boolean
- **system_description**: Welk AI-systeem of onderdeel wordt geleverd, en voor welk doel?
  - Label (voor de plek-om-in-te-vullen): het systeem en het beoogde doel
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `systeem` (standaardkop: systeem)

#### AI9.1 — Welk systeem en welk doel
- Grondslag: goede praktijk; MCC-AI (goede praktijk)
- Toetspunt: De afspraken beschrijven het AI-systeem of onderdeel en het beoogde doel
- Tekstsoort: `append_section` · Nodig: system_description

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Systeem en doel
Leverancier levert {{facts.system_description}}. Afnemer gebruikt het alleen voor het beschreven doel.
````

### 2. Onderdeel `informatie` (standaardkop: informatie)

#### AI9.2 — Of de informatie voor naleving is afgesproken (hoog risico)
- Grondslag: art. 25 lid 4 AI-verordening
- Toetspunt: De aanbieder van een hoogrisicosysteem en de leverancier van een instrument, dienst, component of proces leggen schriftelijk vast welke informatie, capaciteiten en andere bijstand de leverancier levert, zodat de aanbieder aan de verordening kan voldoen
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.high_risk != false and facts.buyer_is_provider != false and facts.free_open_source != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Informatie en bijstand
Leverancier verstrekt Afnemer de informatie, documentatie en bijstand die Afnemer als aanbieder nodig heeft om aan de AI-verordening te voldoen, waaronder een beschrijving van de werking, de bekende beperkingen, de gebruikte data en de testresultaten van het geleverde onderdeel.
````

#### AI9.4 — Of de gebruiksaanwijzing wordt geleverd (hoog risico)
- Grondslag: art. 13 en 26 lid 1 AI-verordening
- Toetspunt: Bij een hoogrisicosysteem levert de leverancier een gebruiksaanwijzing met de informatie die de gebruiker nodig heeft (doel, nauwkeurigheid, beperkingen, menselijk toezicht, logs)
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.high_risk != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Leverancier levert een gebruiksaanwijzing met ten minste het beoogde doel, de nauwkeurigheid, de bekende beperkingen, de maatregelen voor menselijk toezicht en de manier waarop logs worden bewaard.
````

### 3. Onderdeel `toegang` (standaardkop: toegang)

#### AI9.3 — Of technische toegang is afgesproken (hoog risico)
- Grondslag: art. 25 lid 4 AI-verordening
- Toetspunt: De schriftelijke afspraken regelen ook de technische toegang die nodig is voor naleving
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.high_risk != false and facts.buyer_is_provider != false and facts.free_open_source != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Technische toegang
Leverancier geeft Afnemer de technische toegang die nodig is om het onderdeel te testen en de conformiteitsbeoordeling van het hoogrisicosysteem uit te voeren.
````

### 4. Onderdeel `data` (standaardkop: data)

#### AI9.5 — Of data zijn geregeld
- Grondslag: goede praktijk; MCC-AI (goede praktijk)
- Toetspunt: De afspraken regelen welke data de leverancier gebruikt en of invoer van de afnemer voor training mag worden gebruikt
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Data
Leverancier gebruikt gegevens die Afnemer invoert niet voor het trainen of verbeteren van modellen, tenzij Afnemer daar schriftelijk toestemming voor geeft.
````

### 5. Onderdeel `toezicht` (standaardkop: toezicht)

#### AI9.6 — Of menselijk toezicht mogelijk is
- Grondslag: goede praktijk; art. 14 AI-verordening (hoog risico); MCC-AI
- Toetspunt: Het systeem maakt menselijk toezicht mogelijk (uitkomsten begrijpen, negeren, stoppen)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Menselijk toezicht
Het systeem stelt Afnemer in staat de uitkomsten te begrijpen, te negeren of te corrigeren en het gebruik te stoppen.
````

### 6. Onderdeel `kwaliteit` (standaardkop: kwaliteit)

#### AI9.7 — Of kwaliteit en nauwkeurigheid zijn afgesproken
- Grondslag: goede praktijk; art. 15 AI-verordening (hoog risico); MCC-AI
- Toetspunt: De afspraken regelen nauwkeurigheid, robuustheid en beveiliging, en hoe die worden gemeten
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Kwaliteit
Leverancier waarborgt de nauwkeurigheid, robuustheid en beveiliging die in de documentatie zijn opgegeven en meldt wezenlijke afwijkingen.
````

### 7. Onderdeel `logging` (standaardkop: logging)

#### AI9.8 — Of logging is afgesproken
- Grondslag: goede praktijk; art. 12 en 26 lid 6 AI-verordening (hoog risico)
- Toetspunt: Het systeem legt gebeurtenissen vast en de afnemer krijgt toegang tot de logs
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Logs
Het systeem legt gebeurtenissen automatisch vast. Afnemer heeft toegang tot de logs en Leverancier bewaart ze ten minste zes maanden.
````

### 8. Onderdeel `incidenten` (standaardkop: incidenten)

#### AI9.9 — Of incidenten worden gemeld
- Grondslag: goede praktijk; art. 73 AI-verordening (hoog risico); MCC-AI
- Toetspunt: De leverancier meldt ernstige incidenten en wezenlijke wijzigingen aan de afnemer
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Incidenten en wijzigingen
Leverancier meldt Afnemer zonder onnodige vertraging ernstige incidenten en wezenlijke wijzigingen van het systeem.
````

### 9. Onderdeel `privacy` (standaardkop: privacy)

#### AI9.10 — Of er een verwerkersovereenkomst is
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Verwerkt de leverancier persoonsgegevens voor de afnemer, dan regelt of verwijst de overeenkomst naar een verwerkersovereenkomst volgens art. 28 lid 3 AVG
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.personal_data != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Persoonsgegevens
Voor de verwerking van persoonsgegevens door Leverancier sluiten partijen een verwerkersovereenkomst die voldoet aan artikel 28 lid 3 AVG.
````

### 10. Onderdeel `audit` (standaardkop: Informatie en audits)

#### AI9.11 — Of audits mogelijk zijn
- Grondslag: goede praktijk; MCC-AI (goede praktijk)
- Toetspunt: De afnemer kan de naleving van de afspraken laten controleren
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Controle
Leverancier verstrekt op verzoek de informatie die nodig is om de naleving van deze bijlage te controleren en werkt mee aan een audit.
````

## Toetspunten (voor de eindcontrole)

### AI9.1 — Welk systeem en welk doel
- Grondslag: goede praktijk; MCC-AI (goede praktijk)
- Toetspunt: De afspraken beschrijven het AI-systeem of onderdeel en het beoogde doel
- Bronnen: EC-MCC-AI (Europese modelcontractbepalingen voor de aanbesteding van AI (versies voor hoog risico en niet-hoog risico))
- Wat de tekst moet bereiken: Beschrijf welk AI-systeem wordt geleverd en voor welk doel.

### AI9.2 — Of de informatie voor naleving is afgesproken (hoog risico)
- Grondslag: art. 25 lid 4 AI-verordening
- Toetspunt: De aanbieder van een hoogrisicosysteem en de leverancier van een instrument, dienst, component of proces leggen schriftelijk vast welke informatie, capaciteiten en andere bijstand de leverancier levert, zodat de aanbieder aan de verordening kan voldoen
- Alleen als: `facts.high_risk != false and facts.buyer_is_provider != false and facts.free_open_source != true`
- Bronnen: AIVO-art25-lid4 (AI-verordening art. 25 lid 4)
- Wat de tekst moet bereiken: Leg schriftelijk vast welke informatie en bijstand de leverancier levert om aan de AI-verordening te voldoen.

### AI9.3 — Of technische toegang is afgesproken (hoog risico)
- Grondslag: art. 25 lid 4 AI-verordening
- Toetspunt: De schriftelijke afspraken regelen ook de technische toegang die nodig is voor naleving
- Alleen als: `facts.high_risk != false and facts.buyer_is_provider != false and facts.free_open_source != true`
- Bronnen: AIVO-art25-lid4 (AI-verordening art. 25 lid 4)
- Wat de tekst moet bereiken: Leg vast welke technische toegang de leverancier geeft, bijvoorbeeld voor tests en de conformiteitsbeoordeling.

### AI9.4 — Of de gebruiksaanwijzing wordt geleverd (hoog risico)
- Grondslag: art. 13 en 26 lid 1 AI-verordening
- Toetspunt: Bij een hoogrisicosysteem levert de leverancier een gebruiksaanwijzing met de informatie die de gebruiker nodig heeft (doel, nauwkeurigheid, beperkingen, menselijk toezicht, logs)
- Alleen als: `facts.high_risk != false`
- Bronnen: AIVO-art13-lid1 (AI-verordening art. 13 lid 1); AIVO-art26-lid1 (AI-verordening art. 26 lid 1)
- Wat de tekst moet bereiken: Spreek af dat de leverancier een volledige gebruiksaanwijzing levert.

### AI9.5 — Of data zijn geregeld
- Grondslag: goede praktijk; MCC-AI (goede praktijk)
- Toetspunt: De afspraken regelen welke data de leverancier gebruikt en of invoer van de afnemer voor training mag worden gebruikt
- Bronnen: EC-MCC-AI (Europese modelcontractbepalingen voor de aanbesteding van AI (versies voor hoog risico en niet-hoog risico))
- Wat de tekst moet bereiken: Leg vast dat invoer van de afnemer niet zonder toestemming voor training wordt gebruikt.

### AI9.6 — Of menselijk toezicht mogelijk is
- Grondslag: goede praktijk; art. 14 AI-verordening (hoog risico); MCC-AI
- Toetspunt: Het systeem maakt menselijk toezicht mogelijk (uitkomsten begrijpen, negeren, stoppen)
- Bronnen: AIVO-art14-lid1 (AI-verordening art. 14 lid 1); EC-MCC-AI (Europese modelcontractbepalingen voor de aanbesteding van AI (versies voor hoog risico en niet-hoog risico))
- Wat de tekst moet bereiken: Spreek af dat het systeem menselijk toezicht mogelijk maakt.

### AI9.7 — Of kwaliteit en nauwkeurigheid zijn afgesproken
- Grondslag: goede praktijk; art. 15 AI-verordening (hoog risico); MCC-AI
- Toetspunt: De afspraken regelen nauwkeurigheid, robuustheid en beveiliging, en hoe die worden gemeten
- Bronnen: AIVO-art15-lid1 (AI-verordening art. 15 lid 1); EC-MCC-AI (Europese modelcontractbepalingen voor de aanbesteding van AI (versies voor hoog risico en niet-hoog risico))
- Wat de tekst moet bereiken: Leg nauwkeurigheid, robuustheid en beveiliging vast, met meetmethode.

### AI9.8 — Of logging is afgesproken
- Grondslag: goede praktijk; art. 12 en 26 lid 6 AI-verordening (hoog risico)
- Toetspunt: Het systeem legt gebeurtenissen vast en de afnemer krijgt toegang tot de logs
- Bronnen: AIVO-art12-lid1 (AI-verordening art. 12 lid 1); AIVO-art26-lid6 (AI-verordening art. 26 lid 6)
- Wat de tekst moet bereiken: Spreek af dat het systeem logs bijhoudt en dat je er toegang toe hebt.

### AI9.9 — Of incidenten worden gemeld
- Grondslag: goede praktijk; art. 73 AI-verordening (hoog risico); MCC-AI
- Toetspunt: De leverancier meldt ernstige incidenten en wezenlijke wijzigingen aan de afnemer
- Bronnen: AIVO-art73-lid1 (AI-verordening art. 73 lid 1); EC-MCC-AI (Europese modelcontractbepalingen voor de aanbesteding van AI (versies voor hoog risico en niet-hoog risico))
- Wat de tekst moet bereiken: Spreek af dat de leverancier incidenten en wezenlijke wijzigingen direct meldt.

### AI9.10 — Of er een verwerkersovereenkomst is
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Verwerkt de leverancier persoonsgegevens voor de afnemer, dan regelt of verwijst de overeenkomst naar een verwerkersovereenkomst volgens art. 28 lid 3 AVG
- Alleen als: `facts.personal_data != false`
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3)
- Wat de tekst moet bereiken: Sluit een verwerkersovereenkomst met de leverancier.

### AI9.11 — Of audits mogelijk zijn
- Grondslag: goede praktijk; MCC-AI (goede praktijk)
- Toetspunt: De afnemer kan de naleving van de afspraken laten controleren
- Bronnen: EC-MCC-AI (Europese modelcontractbepalingen voor de aanbesteding van AI (versies voor hoog risico en niet-hoog risico))
- Wat de tekst moet bereiken: Spreek af dat je de naleving kunt laten controleren.
