# Kader K11b — Informatiebeveiligingsbeleid (document)

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een informatiebeveiligingsbeleid de risicoafweging, de maatregelen van art. 32 lid 1 sub a-d, de instructie van medewerkers, de datalekprocedure en de verantwoordelijkheid en evaluatie regelt.

Bronnen: AVG-art24-lid1 (AVG art. 24 lid 1); AVG-art24-lid2 (AVG art. 24 lid 2); AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art32-lid1-a (AVG art. 32 lid 1 sub a); AVG-art32-lid1-b (AVG art. 32 lid 1 sub b); AVG-art32-lid1-c (AVG art. 32 lid 1 sub c); AVG-art32-lid1-d (AVG art. 32 lid 1 sub d); AVG-art32-lid2 (AVG art. 32 lid 2); AVG-art32-lid4 (AVG art. 32 lid 4); AVG-art33-lid1 (AVG art. 33 lid 1); AVG-art33-lid5 (AVG art. 33 lid 5)

## Formulier (vragen aan de gebruiker)

- **organisation_name**: Wat is de naam van je organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van de organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **policy_owner**: Wie is eigenaar van het beveiligingsbeleid (functie)?
  - Label (voor de plek-om-in-te-vullen): wie eigenaar is van het beleid
  - Type: text
- **review_interval**: Hoe vaak evalueer je het beleid?
  - Label (voor de plek-om-in-te-vullen): hoe vaak het beleid wordt geëvalueerd
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `risico` (standaardkop: risico)

#### K11b.1 — Waarop het beleid is gebaseerd
- Grondslag: art. 32 lid 1 (aanhef) en lid 2 AVG
- Toetspunt: Het beleid gaat uit van een beoordeling van de risico's voor de rechten en vrijheden van personen (waarschijnlijkheid en ernst), zoals verlies, wijziging, ongeoorloofde verstrekking of toegang
- Tekstsoort: `append_section` · Nodig: organisation_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Risicobeoordeling
{{facts.organisation_name}} bepaalt de beveiligingsmaatregelen op basis van een beoordeling van de risico's voor de betrokkenen, met name het risico op vernietiging, verlies, wijziging, ongeoorloofde verstrekking van of toegang tot persoonsgegevens. De beoordeling wordt herhaald bij wezenlijke wijzigingen.
````

### 2. Onderdeel `maatregelen` (standaardkop: maatregelen)

#### K11b.2 — Of versleuteling en pseudonimisering zijn geregeld
- Grondslag: art. 32 lid 1 sub a AVG
- Toetspunt: Het beleid regelt waar passend pseudonimisering en versleuteling van persoonsgegevens
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Versleuteling
Persoonsgegevens worden versleuteld bij verzending over openbare netwerken en bij opslag op draagbare apparaten en in de cloud. Waar mogelijk worden gegevens gepseudonimiseerd.
````

### 3. Onderdeel `toegang` (standaardkop: toegang)

#### K11b.3 — Of vertrouwelijkheid, integriteit en beschikbaarheid zijn geregeld
- Grondslag: art. 32 lid 1 sub b AVG
- Toetspunt: Het beleid regelt maatregelen om de vertrouwelijkheid, integriteit, beschikbaarheid en veerkracht van systemen en diensten te waarborgen, zoals toegangsbeheer
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Toegang en beschikbaarheid
Medewerkers hebben alleen toegang tot de persoonsgegevens die zij voor hun werk nodig hebben. Toegang tot systemen met persoonsgegevens vereist tweestapsverificatie. Systemen worden bijgewerkt met beveiligingsupdates.
````

### 4. Onderdeel `herstel` (standaardkop: herstel)

#### K11b.4 — Of herstel na een incident is geregeld
- Grondslag: art. 32 lid 1 sub c AVG
- Toetspunt: Het beleid regelt het vermogen om bij een incident de beschikbaarheid van en toegang tot persoonsgegevens tijdig te herstellen, zoals back-ups
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Back-ups en herstel
Van systemen met persoonsgegevens worden regelmatig back-ups gemaakt, gescheiden van de productieomgeving. Het herstel wordt periodiek getest.
````

### 5. Onderdeel `testen` (standaardkop: testen)

#### K11b.5 — Of maatregelen regelmatig worden getest
- Grondslag: art. 32 lid 1 sub d AVG
- Toetspunt: Het beleid regelt een procedure om de doeltreffendheid van de maatregelen regelmatig te testen, beoordelen en evalueren
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Testen en evalueren
De doeltreffendheid van de maatregelen wordt regelmatig getest en beoordeeld, onder meer met een jaarlijkse controle van toegangsrechten en kwetsbaarheidsscans.
````

### 6. Onderdeel `medewerkers` (standaardkop: medewerkers)

#### K11b.6 — Of medewerkers alleen op instructie verwerken
- Grondslag: art. 32 lid 4 AVG
- Toetspunt: Het beleid regelt dat wie onder gezag van de organisatie toegang heeft tot persoonsgegevens, die alleen op instructie verwerkt
- Tekstsoort: `append_section` · Nodig: organisation_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Medewerkers
Medewerkers en ingehuurde krachten verwerken persoonsgegevens alleen volgens de instructies van {{facts.organisation_name}}, zijn tot geheimhouding verplicht en krijgen bij indiensttreding en periodiek uitleg over beveiliging.
````

### 7. Onderdeel `datalekken` (standaardkop: datalekken)

#### K11b.7 — Of het beleid verwijst naar de datalekprocedure
- Grondslag: art. 33 AVG
- Toetspunt: Het beleid verwijst naar de procedure voor het melden en vastleggen van inbreuken in verband met persoonsgegevens
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Datalekken
Iedere medewerker meldt een (mogelijk) datalek direct volgens de datalekprocedure. Alle datalekken worden vastgelegd; melding aan de Autoriteit Persoonsgegevens gebeurt waar nodig binnen 72 uur.
````

### 8. Onderdeel `eigenaar` (standaardkop: eigenaar)

#### K11b.8 — Wie eigenaar is en hoe vaak het beleid wordt geëvalueerd
- Grondslag: goede praktijk; art. 24 lid 1 en 2 AVG als achtergrond
- Toetspunt: Het beleid noemt een eigenaar en een evaluatiecyclus
- Tekstsoort: `append_section` · Nodig: policy_owner, review_interval

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Eigenaar en evaluatie
Eigenaar van dit beleid is {{facts.policy_owner}}. Het beleid wordt geëvalueerd: {{facts.review_interval}}.
````

## Toetspunten (voor de eindcontrole)

### K11b.1 — Waarop het beleid is gebaseerd
- Grondslag: art. 32 lid 1 (aanhef) en lid 2 AVG
- Toetspunt: Het beleid gaat uit van een beoordeling van de risico's voor de rechten en vrijheden van personen (waarschijnlijkheid en ernst), zoals verlies, wijziging, ongeoorloofde verstrekking of toegang
- Bronnen: AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art32-lid2 (AVG art. 32 lid 2)
- Wat de tekst moet bereiken: Neem op dat de maatregelen volgen uit een risicobeoordeling, en hoe die wordt gedaan.

### K11b.2 — Of versleuteling en pseudonimisering zijn geregeld
- Grondslag: art. 32 lid 1 sub a AVG
- Toetspunt: Het beleid regelt waar passend pseudonimisering en versleuteling van persoonsgegevens
- Bronnen: AVG-art32-lid1-a (AVG art. 32 lid 1 sub a)
- Wat de tekst moet bereiken: Leg vast wanneer gegevens worden versleuteld of gepseudonimiseerd.

### K11b.3 — Of vertrouwelijkheid, integriteit en beschikbaarheid zijn geregeld
- Grondslag: art. 32 lid 1 sub b AVG
- Toetspunt: Het beleid regelt maatregelen om de vertrouwelijkheid, integriteit, beschikbaarheid en veerkracht van systemen en diensten te waarborgen, zoals toegangsbeheer
- Bronnen: AVG-art32-lid1-b (AVG art. 32 lid 1 sub b)
- Wat de tekst moet bereiken: Regel toegangsbeheer (wie mag wat), sterke authenticatie en maatregelen voor beschikbaarheid.

### K11b.4 — Of herstel na een incident is geregeld
- Grondslag: art. 32 lid 1 sub c AVG
- Toetspunt: Het beleid regelt het vermogen om bij een incident de beschikbaarheid van en toegang tot persoonsgegevens tijdig te herstellen, zoals back-ups
- Bronnen: AVG-art32-lid1-c (AVG art. 32 lid 1 sub c)
- Wat de tekst moet bereiken: Regel back-ups en hoe snel je na een incident herstelt.

### K11b.5 — Of maatregelen regelmatig worden getest
- Grondslag: art. 32 lid 1 sub d AVG
- Toetspunt: Het beleid regelt een procedure om de doeltreffendheid van de maatregelen regelmatig te testen, beoordelen en evalueren
- Bronnen: AVG-art32-lid1-d (AVG art. 32 lid 1 sub d)
- Wat de tekst moet bereiken: Leg vast hoe en hoe vaak je de maatregelen test.

### K11b.6 — Of medewerkers alleen op instructie verwerken
- Grondslag: art. 32 lid 4 AVG
- Toetspunt: Het beleid regelt dat wie onder gezag van de organisatie toegang heeft tot persoonsgegevens, die alleen op instructie verwerkt
- Bronnen: AVG-art32-lid4 (AVG art. 32 lid 4)
- Wat de tekst moet bereiken: Leg vast dat medewerkers persoonsgegevens alleen volgens instructie verwerken, en hoe ze daarover worden geïnstrueerd.

### K11b.7 — Of het beleid verwijst naar de datalekprocedure
- Grondslag: art. 33 AVG
- Toetspunt: Het beleid verwijst naar de procedure voor het melden en vastleggen van inbreuken in verband met persoonsgegevens
- Bronnen: AVG-art33-lid1 (AVG art. 33 lid 1); AVG-art33-lid5 (AVG art. 33 lid 5)
- Wat de tekst moet bereiken: Verwijs naar je datalekprocedure.

### K11b.8 — Wie eigenaar is en hoe vaak het beleid wordt geëvalueerd
- Grondslag: goede praktijk; art. 24 lid 1 en 2 AVG als achtergrond
- Toetspunt: Het beleid noemt een eigenaar en een evaluatiecyclus
- Bronnen: AVG-art24-lid1 (AVG art. 24 lid 1); AVG-art24-lid2 (AVG art. 24 lid 2)
- Wat de tekst moet bereiken: Noem wie eigenaar is van het beleid en hoe vaak het wordt geëvalueerd.
