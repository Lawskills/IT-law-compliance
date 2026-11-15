# Kader AI10 — AI-gebruiksbeleid

Versie 0.3 · peildatum 2026-11-10

Doel: Controleren of een AI-gebruiksbeleid regelt welke tools en toepassingen zijn toegestaan, verboden praktijken uitsluit, persoonsgegevens en vertrouwelijke informatie beschermt, menselijke controle en transparantie vraagt, en training, een aanspreekpunt en incidenten regelt.

Bronnen: AIVO-art4 (AI-verordening art. 4); AIVO-art5-lid1-a (AI-verordening art. 5 lid 1 sub a); AIVO-art5-lid1-f (AI-verordening art. 5 lid 1 sub f); AIVO-art50-lid1 (AI-verordening art. 50 lid 1); AIVO-art50-lid4 (AI-verordening art. 50 lid 4); AVG-art22-lid1 (AVG art. 22 lid 1); AVG-art28-lid1 (AVG art. 28 lid 1); AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art33-lid1 (AVG art. 33 lid 1); AVG-art5-lid1-f (AVG art. 5 lid 1 sub f); AVG-art6-lid1 (AVG art. 6 lid 1); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

## Formulier (vragen aan de gebruiker)

- **organisation_name**: Wat is de naam van je organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van de organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **customer_facing_ai**: Gebruik je AI die rechtstreeks met klanten communiceert of inhoud voor hen maakt (chatbot, teksten, beelden)?
  - Label (voor de plek-om-in-te-vullen): of je AI gebruikt richting klanten
  - Type: boolean
- **allowed_tools**: Welke AI-tools mogen medewerkers gebruiken (bijvoorbeeld de zakelijke versie van een bepaalde chatbot)?
  - Label (voor de plek-om-in-te-vullen): welke tools zijn toegestaan
  - Type: text
- **ai_contact**: Wie is het aanspreekpunt voor vragen over AI?
  - Label (voor de plek-om-in-te-vullen): het aanspreekpunt
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `toepassing` (standaardkop: toepassing)

#### AI10.1 — Voor wie en waarvoor het beleid geldt
- Grondslag: goede praktijk; art. 4 AI-verordening als achtergrond
- Toetspunt: Het beleid noemt voor wie het geldt (ook externen die namens de organisatie AI gebruiken) en voor welk gebruik
- Tekstsoort: `append_section` · Nodig: organisation_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Voor wie dit beleid geldt
Dit beleid geldt voor alle medewerkers van {{facts.organisation_name}} en voor iedereen die namens {{facts.organisation_name}} AI-systemen gebruikt, zoals uitzendkrachten en freelancers.
````

### 2. Onderdeel `tools` (standaardkop: tools)

#### AI10.2 — Welke tools zijn toegestaan
- Grondslag: goede praktijk; goede praktijk; art. 28 en 32 AVG als achtergrond
- Toetspunt: Het beleid noemt welke AI-tools en toepassingen zijn toegestaan en hoe een nieuwe tool wordt goedgekeurd
- Tekstsoort: `append_section` · Nodig: allowed_tools

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Toegestane tools
Medewerkers gebruiken alleen deze AI-tools: {{facts.allowed_tools}}. Een nieuwe tool wordt eerst beoordeeld en goedgekeurd door het aanspreekpunt voor AI.
````

### 3. Onderdeel `verboden` (standaardkop: verboden)

#### AI10.3 — Of verboden toepassingen zijn uitgesloten
- Grondslag: art. 5 AI-verordening
- Toetspunt: Het beleid sluit de verboden AI-praktijken uit, zoals emotieherkenning op het werk en manipulatie
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Verboden toepassingen
AI wordt niet gebruikt voor toepassingen die de AI-verordening verbiedt, zoals het herkennen van emoties van medewerkers of het manipuleren van mensen.
````

### 4. Onderdeel `gegevens` (standaardkop: gegevens)

#### AI10.4 — Of persoonsgegevens en vertrouwelijke informatie zijn beschermd
- Grondslag: art. 5 lid 1, art. 6, art. 28 en art. 32 AVG
- Toetspunt: Het beleid regelt dat medewerkers geen persoonsgegevens of vertrouwelijke informatie in AI-tools invoeren, tenzij de tool daarvoor is goedgekeurd (grondslag, verwerkersovereenkomst, beveiliging)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Persoonsgegevens en vertrouwelijke informatie
Medewerkers voeren geen persoonsgegevens of vertrouwelijke informatie in AI-tools in, behalve in tools die daarvoor zijn goedgekeurd en waarvoor een verwerkersovereenkomst is gesloten.
````

### 5. Onderdeel `controle` (standaardkop: controle)

#### AI10.5 — Of uitkomsten door een mens worden gecontroleerd
- Grondslag: art. 4 en 26 lid 2 AI-verordening; art. 22 AVG als achtergrond
- Toetspunt: Het beleid regelt dat medewerkers uitkomsten van AI controleren voordat ze die gebruiken, vooral bij besluiten over mensen
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Controle van uitkomsten
Medewerkers controleren uitkomsten van AI op juistheid voordat ze die gebruiken. Besluiten over mensen worden altijd door een mens genomen.
````

### 6. Onderdeel `transparantie` (standaardkop: transparantie)

#### AI10.6 — Of transparantie naar klanten is geregeld
- Grondslag: art. 50 AI-verordening
- Toetspunt: Communiceert AI met klanten of maakt het inhoud voor hen, dan regelt het beleid dat klanten weten dat ze met AI te maken hebben en dat deepfakes worden gemarkeerd
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.customer_facing_ai != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Transparantie
Als klanten met een AI-systeem communiceren, wordt dat duidelijk gemaakt. Beeld, geluid of video dat met AI is gemaakt of bewerkt en echt lijkt, wordt als zodanig gemarkeerd.
````

### 7. Onderdeel `training` (standaardkop: training)

#### AI10.7 — Of training en uitleg zijn geregeld
- Grondslag: art. 4 AI-verordening (zoals gewijzigd bij Vo. (EU) 2026/1744)
- Toetspunt: Het beleid regelt maatregelen voor AI-geletterdheid: uitleg of training passend bij wat medewerkers met AI doen
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Training
Medewerkers krijgen uitleg over verstandig gebruik van AI, passend bij hun werk. Wie AI gebruikt bij beslissingen over mensen, krijgt aanvullende uitleg over risico's, fouten en vooroordelen.
````

### 8. Onderdeel `aanspreekpunt` (standaardkop: aanspreekpunt)

#### AI10.8 — Of er een aanspreekpunt is
- Grondslag: goede praktijk
- Toetspunt: Het beleid noemt een aanspreekpunt voor vragen en goedkeuring
- Tekstsoort: `append_section` · Nodig: ai_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Aanspreekpunt
Vragen over AI en verzoeken om een nieuwe tool gaan naar {{facts.ai_contact}}.
````

### 9. Onderdeel `registratie` (standaardkop: registratie)

#### AI10.9 — Of gebruikte tools worden geregistreerd
- Grondslag: goede praktijk; art. 4 AI-verordening als achtergrond
- Toetspunt: Het beleid regelt een overzicht van de gebruikte AI-systemen
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Overzicht
Het aanspreekpunt houdt een overzicht bij van de AI-systemen die worden gebruikt, door wie en waarvoor.
````

### 10. Onderdeel `incidenten` (standaardkop: incidenten)

#### AI10.10 — Of incidenten worden gemeld
- Grondslag: goede praktijk; art. 33 AVG als achtergrond
- Toetspunt: Het beleid regelt dat medewerkers fouten, misbruik of het lekken van gegevens via AI melden
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Incidenten
Medewerkers melden fouten, misbruik of het onbedoeld delen van persoonsgegevens via een AI-tool direct bij het aanspreekpunt. Een mogelijk datalek wordt behandeld volgens de datalekprocedure.
````

## Toetspunten (voor de eindcontrole)

### AI10.1 — Voor wie en waarvoor het beleid geldt
- Grondslag: goede praktijk; art. 4 AI-verordening als achtergrond
- Toetspunt: Het beleid noemt voor wie het geldt (ook externen die namens de organisatie AI gebruiken) en voor welk gebruik
- Bronnen: AIVO-art4 (AI-verordening art. 4)
- Wat de tekst moet bereiken: Beschrijf voor wie het beleid geldt, ook uitzendkrachten en freelancers.

### AI10.2 — Welke tools zijn toegestaan
- Grondslag: goede praktijk; goede praktijk; art. 28 en 32 AVG als achtergrond
- Toetspunt: Het beleid noemt welke AI-tools en toepassingen zijn toegestaan en hoe een nieuwe tool wordt goedgekeurd
- Bronnen: AVG-art28-lid1 (AVG art. 28 lid 1); AVG-art32-lid1 (AVG art. 32 lid 1)
- Wat de tekst moet bereiken: Noem welke tools zijn toegestaan en hoe een nieuwe tool wordt goedgekeurd.

### AI10.3 — Of verboden toepassingen zijn uitgesloten
- Grondslag: art. 5 AI-verordening
- Toetspunt: Het beleid sluit de verboden AI-praktijken uit, zoals emotieherkenning op het werk en manipulatie
- Bronnen: AIVO-art5-lid1-a (AI-verordening art. 5 lid 1 sub a); AIVO-art5-lid1-f (AI-verordening art. 5 lid 1 sub f)
- Wat de tekst moet bereiken: Sluit verboden AI-toepassingen uit, zoals emotieherkenning bij medewerkers.

### AI10.4 — Of persoonsgegevens en vertrouwelijke informatie zijn beschermd
- Grondslag: art. 5 lid 1, art. 6, art. 28 en art. 32 AVG
- Toetspunt: Het beleid regelt dat medewerkers geen persoonsgegevens of vertrouwelijke informatie in AI-tools invoeren, tenzij de tool daarvoor is goedgekeurd (grondslag, verwerkersovereenkomst, beveiliging)
- Bronnen: AVG-art5-lid1-f (AVG art. 5 lid 1 sub f); AVG-art6-lid1 (AVG art. 6 lid 1); AVG-art28-lid1 (AVG art. 28 lid 1); AVG-art32-lid1 (AVG art. 32 lid 1)
- Wat de tekst moet bereiken: Leg vast dat geen persoonsgegevens of vertrouwelijke informatie in AI-tools gaan, behalve in tools die daarvoor zijn goedgekeurd.

### AI10.5 — Of uitkomsten door een mens worden gecontroleerd
- Grondslag: art. 4 en 26 lid 2 AI-verordening; art. 22 AVG als achtergrond
- Toetspunt: Het beleid regelt dat medewerkers uitkomsten van AI controleren voordat ze die gebruiken, vooral bij besluiten over mensen
- Bronnen: AIVO-art4 (AI-verordening art. 4); AVG-art22-lid1 (AVG art. 22 lid 1)
- Wat de tekst moet bereiken: Leg vast dat medewerkers AI-uitkomsten altijd controleren, en dat een mens beslist over mensen.

### AI10.6 — Of transparantie naar klanten is geregeld
- Grondslag: art. 50 AI-verordening
- Toetspunt: Communiceert AI met klanten of maakt het inhoud voor hen, dan regelt het beleid dat klanten weten dat ze met AI te maken hebben en dat deepfakes worden gemarkeerd
- Alleen als: `facts.customer_facing_ai != false`
- Bronnen: AIVO-art50-lid1 (AI-verordening art. 50 lid 1); AIVO-art50-lid4 (AI-verordening art. 50 lid 4)
- Wat de tekst moet bereiken: Leg vast dat klanten weten wanneer ze met AI communiceren en dat AI-beelden en -video's worden gemarkeerd.

### AI10.7 — Of training en uitleg zijn geregeld
- Grondslag: art. 4 AI-verordening (zoals gewijzigd bij Vo. (EU) 2026/1744)
- Toetspunt: Het beleid regelt maatregelen voor AI-geletterdheid: uitleg of training passend bij wat medewerkers met AI doen
- Bronnen: AIVO-art4 (AI-verordening art. 4); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))
- Wat de tekst moet bereiken: Regel uitleg of training over verstandig AI-gebruik, met meer aandacht voor wie AI bij belangrijke taken gebruikt.

### AI10.8 — Of er een aanspreekpunt is
- Grondslag: goede praktijk
- Toetspunt: Het beleid noemt een aanspreekpunt voor vragen en goedkeuring
- Bronnen: AIVO-art4 (AI-verordening art. 4)
- Wat de tekst moet bereiken: Wijs een aanspreekpunt voor AI aan.

### AI10.9 — Of gebruikte tools worden geregistreerd
- Grondslag: goede praktijk; art. 4 AI-verordening als achtergrond
- Toetspunt: Het beleid regelt een overzicht van de gebruikte AI-systemen
- Bronnen: AIVO-art4 (AI-verordening art. 4)
- Wat de tekst moet bereiken: Houd een overzicht bij van de gebruikte AI-systemen.

### AI10.10 — Of incidenten worden gemeld
- Grondslag: goede praktijk; art. 33 AVG als achtergrond
- Toetspunt: Het beleid regelt dat medewerkers fouten, misbruik of het lekken van gegevens via AI melden
- Bronnen: AVG-art33-lid1 (AVG art. 33 lid 1)
- Wat de tekst moet bereiken: Leg vast dat medewerkers fouten en het lekken van gegevens via AI direct melden.
