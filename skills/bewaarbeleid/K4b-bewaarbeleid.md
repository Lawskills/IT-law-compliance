# Kader K4b — Bewaarbeleid (document)

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een bewaarbeleid per categorie persoonsgegevens een bewaartermijn of criteria noemt met onderbouwing, wettelijke bewaarplichten verwerkt, regelt wat er na afloop gebeurt, aansluit op het verwerkingsregister en de verantwoordelijkheid en controle regelt.

Bronnen: AVG-art13-lid2-a (AVG art. 13 lid 2 sub a); AVG-art30-lid1-f (AVG art. 30 lid 1 sub f); AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); AVG-art5-lid2 (AVG art. 5 lid 2); AVG-art6-lid1-c (AVG art. 6 lid 1 sub c); AWR-art52-lid4 (Algemene wet inzake rijksbelastingen art. 52 lid 4 (fiscale bewaarplicht 7 jaar))

## Formulier (vragen aan de gebruiker)

- **organisation_name**: Wat is de naam van je organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van de organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **has_register**: Heb je een verwerkingsregister?
  - Label (voor de plek-om-in-te-vullen): of je een verwerkingsregister hebt
  - Type: boolean
- **retention_table**: Welke bewaartermijnen gelden per soort gegevens (bijvoorbeeld "sollicitaties: 4 weken na de procedure")?
  - Label (voor de plek-om-in-te-vullen): de bewaartermijnen per categorie
  - Type: text
- **retention_owner**: Wie zorgt dat de termijnen worden nageleefd?
  - Label (voor de plek-om-in-te-vullen): wie verantwoordelijk is
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `termijnen` (standaardkop: termijnen)

#### K4b.1 — Of er per soort gegevens een termijn staat
- Grondslag: art. 5 lid 1 sub e en art. 13 lid 2 sub a AVG
- Toetspunt: Het beleid noemt per categorie persoonsgegevens een bewaartermijn of de criteria om die te bepalen
- Tekstsoort: `append_section` · Nodig: organisation_name, retention_table

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Bewaartermijnen
{{facts.organisation_name}} bewaart persoonsgegevens niet langer dan nodig voor het doel waarvoor ze zijn verzameld. Per categorie gelden deze termijnen:
{{facts.retention_table}}
````

### 2. Onderdeel `wettelijk` (standaardkop: wettelijk)

#### K4b.3 — Of wettelijke bewaarplichten zijn verwerkt
- Grondslag: art. 52 lid 4 AWR; art. 6 lid 1 sub c AVG
- Toetspunt: Het beleid verwerkt de wettelijke bewaarplichten die gelden, zoals de fiscale bewaarplicht van zeven jaar
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Wettelijke bewaarplichten
Gegevens die deel uitmaken van de administratie worden zeven jaar bewaard (artikel 52 lid 4 Algemene wet inzake rijksbelastingen). Andere wettelijke bewaarplichten gaan voor de termijnen in dit beleid.
````

### 3. Onderdeel `einde` (standaardkop: Einde van de verwerking)

#### K4b.4 — Wat er na afloop gebeurt
- Grondslag: art. 5 lid 1 sub e AVG
- Toetspunt: Het beleid regelt dat gegevens na afloop van de termijn worden vernietigd of geanonimiseerd, ook in back-ups en bij verwerkers
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Na afloop van de termijn
Na afloop van de termijn worden de gegevens vernietigd of zo geanonimiseerd dat ze niet meer tot personen te herleiden zijn. Dit geldt ook voor kopieën en voor gegevens bij verwerkers; back-ups worden binnen hun eigen cyclus overschreven.
````

### 4. Onderdeel `register` (standaardkop: register)

#### K4b.5 — Of het beleid aansluit op het verwerkingsregister
- Grondslag: art. 30 lid 1 sub f AVG
- Toetspunt: De termijnen in het beleid komen overeen met het verwerkingsregister, dat waar mogelijk de bewaartermijnen per categorie noemt
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.has_register != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Verwerkingsregister
De bewaartermijnen in dit beleid worden ook vastgelegd in het verwerkingsregister (artikel 30 lid 1 sub f AVG); bij een wijziging worden beide tegelijk bijgewerkt.
````

### 5. Onderdeel `controle` (standaardkop: controle)

#### K4b.6 — Wie verantwoordelijk is en hoe naleving wordt gecontroleerd
- Grondslag: goede praktijk; art. 5 lid 2 AVG (verantwoordingsplicht) als achtergrond
- Toetspunt: Het beleid noemt wie verantwoordelijk is voor de naleving en hoe dat wordt gecontroleerd
- Tekstsoort: `append_section` · Nodig: retention_owner

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Verantwoordelijkheid
{{facts.retention_owner}} zorgt dat de termijnen worden nageleefd en controleert dit ten minste jaarlijks.
````

## Toetspunten (voor de eindcontrole)

### K4b.1 — Of er per soort gegevens een termijn staat
- Grondslag: art. 5 lid 1 sub e en art. 13 lid 2 sub a AVG
- Toetspunt: Het beleid noemt per categorie persoonsgegevens een bewaartermijn of de criteria om die te bepalen
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); AVG-art13-lid2-a (AVG art. 13 lid 2 sub a)
- Wat de tekst moet bereiken: Noem per soort gegevens hoe lang je ze bewaart, of naar welk criterium.

### K4b.2 — Of de termijnen niet langer zijn dan nodig
- Grondslag: art. 5 lid 1 sub e en lid 2 AVG
- Toetspunt: De termijnen zijn onderbouwd met het doel of een wettelijke plicht en niet langer dan nodig
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); AVG-art5-lid2 (AVG art. 5 lid 2)
- Wat de tekst moet bereiken: Onderbouw elke termijn met het doel of de wettelijke plicht, en schrap onbeperkt bewaren.

### K4b.3 — Of wettelijke bewaarplichten zijn verwerkt
- Grondslag: art. 52 lid 4 AWR; art. 6 lid 1 sub c AVG
- Toetspunt: Het beleid verwerkt de wettelijke bewaarplichten die gelden, zoals de fiscale bewaarplicht van zeven jaar
- Bronnen: AWR-art52-lid4 (Algemene wet inzake rijksbelastingen art. 52 lid 4 (fiscale bewaarplicht 7 jaar)); AVG-art6-lid1-c (AVG art. 6 lid 1 sub c)
- Wat de tekst moet bereiken: Noem de wettelijke bewaarplichten, zoals zeven jaar voor de financiële administratie.

### K4b.4 — Wat er na afloop gebeurt
- Grondslag: art. 5 lid 1 sub e AVG
- Toetspunt: Het beleid regelt dat gegevens na afloop van de termijn worden vernietigd of geanonimiseerd, ook in back-ups en bij verwerkers
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e)
- Wat de tekst moet bereiken: Leg vast dat gegevens na afloop worden vernietigd of geanonimiseerd, ook bij leveranciers.

### K4b.5 — Of het beleid aansluit op het verwerkingsregister
- Grondslag: art. 30 lid 1 sub f AVG
- Toetspunt: De termijnen in het beleid komen overeen met het verwerkingsregister, dat waar mogelijk de bewaartermijnen per categorie noemt
- Alleen als: `facts.has_register != false`
- Bronnen: AVG-art30-lid1-f (AVG art. 30 lid 1 sub f)
- Wat de tekst moet bereiken: Laat de termijnen aansluiten op het verwerkingsregister.

### K4b.6 — Wie verantwoordelijk is en hoe naleving wordt gecontroleerd
- Grondslag: goede praktijk; art. 5 lid 2 AVG (verantwoordingsplicht) als achtergrond
- Toetspunt: Het beleid noemt wie verantwoordelijk is voor de naleving en hoe dat wordt gecontroleerd
- Bronnen: AVG-art5-lid2 (AVG art. 5 lid 2)
- Wat de tekst moet bereiken: Noem wie zorgt voor naleving en hoe vaak dat wordt gecontroleerd.
