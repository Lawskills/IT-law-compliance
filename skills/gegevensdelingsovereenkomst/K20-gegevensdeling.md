# Kader K20 — Gegevensdelingsovereenkomst (zelfstandige verantwoordelijken)

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of afspraken over het delen van persoonsgegevens tussen zelfstandige verwerkingsverantwoordelijken de rollen, het doel, de gegevens, de grondslag, het informeren van betrokkenen, de beveiliging en de onderlinge samenwerking regelen.

Bronnen: AVG-art12-lid3 (AVG art. 12 lid 3); AVG-art13-lid1 (AVG art. 13 lid 1); AVG-art14-lid1 (AVG art. 14 lid 1); AVG-art19 (AVG art. 19); AVG-art26-lid1 (AVG art. 26 lid 1); AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art33-lid1 (AVG art. 33 lid 1); AVG-art4-7 (AVG art. 4 punt 7); AVG-art44 (AVG art. 44); AVG-art46-lid1 (AVG art. 46 lid 1); AVG-art5-lid1-b (AVG art. 5 lid 1 sub b); AVG-art5-lid1-c (AVG art. 5 lid 1 sub c); AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); AVG-art6-lid1 (AVG art. 6 lid 1); AVG-art82-lid1 (AVG art. 82 lid 1); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)

## Formulier (vragen aan de gebruiker)

- **provider_name**: Wie verstrekt de gegevens?
  - Label (voor de plek-om-in-te-vullen): naam van de verstrekker
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **recipient_name**: Wie ontvangt de gegevens?
  - Label (voor de plek-om-in-te-vullen): naam van de ontvanger
  - Type: text
- **decide_together**: Bepalen jullie samen waarvoor en hoe de gegevens worden verwerkt (in plaats van ieder voor zijn eigen doel)?
  - Label (voor de plek-om-in-te-vullen): of jullie samen doel en middelen bepalen
  - Type: boolean
- **outside_eea**: Gaan de gegevens naar een organisatie of server buiten de Europese Economische Ruimte?
  - Label (voor de plek-om-in-te-vullen): of gegevens buiten de EER gaan
  - Type: boolean
- **sharing_purpose**: Waarvoor worden de gegevens gedeeld, en welke gegevens van wie?
  - Label (voor de plek-om-in-te-vullen): het doel van het delen
  - Type: text
- **legal_basis_text**: Op welke grondslag verstrekt de verstrekker en verwerkt de ontvanger de gegevens?
  - Label (voor de plek-om-in-te-vullen): de grondslag
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `doel` (standaardkop: doel)

#### K20.2 — Of doel en gegevens zijn omschreven
- Grondslag: art. 5 lid 1 sub b en c AVG
- Toetspunt: De afspraken omschrijven voor welk doel welke persoonsgegevens van welke betrokkenen worden verstrekt
- Tekstsoort: `append_section` · Nodig: sharing_purpose

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Doel en gegevens
Verstrekker verstrekt aan Ontvanger persoonsgegevens voor: {{facts.sharing_purpose}}. Ontvanger gebruikt de gegevens niet voor doelen die daarmee onverenigbaar zijn.
````

### 2. Onderdeel `grondslag` (standaardkop: Op welke grond gebruiken wij deze gegevens)

#### K20.3 — Of de grondslag is benoemd
- Grondslag: art. 6 lid 1 AVG
- Toetspunt: De afspraken noemen de grondslag waarop de verstrekker verstrekt en de ontvanger verwerkt
- Tekstsoort: `append_section` · Nodig: legal_basis_text

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Grondslag
Partijen verwerken de gegevens op de volgende grondslag: {{facts.legal_basis_text}}. Elke partij is zelf verantwoordelijk voor de rechtmatigheid van haar verwerking.
````

### 3. Onderdeel `informeren` (standaardkop: informeren)

#### K20.4 — Wie de betrokkenen informeert
- Grondslag: art. 13 en 14 AVG
- Toetspunt: De afspraken regelen hoe de betrokkenen worden geïnformeerd over de verstrekking en over de verwerking door de ontvanger
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Informeren van betrokkenen
Verstrekker vermeldt de verstrekking aan Ontvanger in zijn privacyverklaring. Ontvanger informeert de betrokkenen volgens artikel 14 AVG binnen een redelijke termijn na ontvangst, tenzij een uitzondering geldt.
````

### 4. Onderdeel `beveiliging` (standaardkop: Beveiliging)

#### K20.5 — Of de overdracht beveiligd is
- Grondslag: art. 32 AVG
- Toetspunt: De afspraken regelen passende beveiliging van de overdracht en van de gegevens bij de ontvanger
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Beveiliging
Partijen dragen de gegevens over via een beveiligde verbinding en nemen elk passende technische en organisatorische maatregelen volgens artikel 32 AVG.
````

### 5. Onderdeel `datalekken` (standaardkop: datalekken)

#### K20.6 — Of datalekken onderling worden gemeld
- Grondslag: goede praktijk; art. 33 AVG als achtergrond
- Toetspunt: De afspraken regelen dat partijen elkaar informeren over een datalek dat de gedeelde gegevens raakt
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Datalekken
Partijen informeren elkaar zonder onredelijke vertraging over een inbreuk die de gedeelde gegevens raakt. Elke partij beslist zelf over een melding aan de Autoriteit Persoonsgegevens en aan betrokkenen.
````

### 6. Onderdeel `rechten` (standaardkop: Je rechten)

#### K20.7 — Of verzoeken van betrokkenen worden doorgegeven
- Grondslag: goede praktijk; art. 12 en 19 AVG als achtergrond
- Toetspunt: De afspraken regelen dat partijen elkaar helpen of verzoeken doorsturen als een betrokkene zijn rechten uitoefent
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Rechten van betrokkenen
Partijen sturen een verzoek van een betrokkene dat de andere partij betreft onverwijld door, en informeren elkaar over rectificatie of wissing van gedeelde gegevens (artikel 19 AVG).
````

### 7. Onderdeel `bewaren` (standaardkop: Hoe lang bewaren wij je gegevens)

#### K20.8 — Hoe lang de ontvanger bewaart
- Grondslag: goede praktijk; art. 5 lid 1 sub e AVG als achtergrond
- Toetspunt: De afspraken regelen hoe lang de ontvanger de gegevens bewaart of hoe die termijn wordt bepaald
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Bewaren
Ontvanger bewaart de gegevens niet langer dan nodig voor het doel en verwijdert ze daarna.
````

### 8. Onderdeel `doorgifte` (standaardkop: doorgifte)

#### K20.9 — Of doorgifte buiten de EER is geregeld
- Grondslag: art. 44-46 AVG
- Toetspunt: Gaan gegevens buiten de EER, dan noemen de afspraken de doorgiftegrond (adequaatheidsbesluit of passende waarborgen)
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.outside_eea != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Doorgifte
Gegevens worden alleen buiten de EER doorgegeven op grond van een adequaatheidsbesluit of passende waarborgen, zoals de standaardcontractbepalingen van de Europese Commissie.
````

### 9. Onderdeel `aansprakelijkheid` (standaardkop: aansprakelijkheid)

#### K20.10 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 82 AVG als achtergrond
- Toetspunt: De afspraken regelen de aansprakelijkheid tussen partijen
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Aansprakelijkheid
Elke partij is aansprakelijk voor haar eigen verwerking en vrijwaart de andere partij voor schade door haar eigen niet-nakoming van de AVG.
````

## Toetspunten (voor de eindcontrole)

### K20.1 — Of jullie echt zelfstandig verantwoordelijk zijn
- Grondslag: art. 4 punt 7 en art. 26 AVG; EDPB-richtsnoeren 07/2020
- Toetspunt: De afspraken bevestigen dat elke partij voor eigen doelen en met eigen middelen verwerkt; bepalen de partijen samen doel en middelen, dan zijn zij gezamenlijk verantwoordelijk en geldt art. 26 AVG
- Bronnen: AVG-art4-7 (AVG art. 4 punt 7); AVG-art26-lid1 (AVG art. 26 lid 1); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat elke partij voor eigen doelen verwerkt; bepalen jullie samen doel en middelen, maak dan een regeling volgens art. 26 AVG.

### K20.2 — Of doel en gegevens zijn omschreven
- Grondslag: art. 5 lid 1 sub b en c AVG
- Toetspunt: De afspraken omschrijven voor welk doel welke persoonsgegevens van welke betrokkenen worden verstrekt
- Bronnen: AVG-art5-lid1-b (AVG art. 5 lid 1 sub b); AVG-art5-lid1-c (AVG art. 5 lid 1 sub c)
- Wat de tekst moet bereiken: Omschrijf waarvoor welke gegevens van wie worden gedeeld.

### K20.3 — Of de grondslag is benoemd
- Grondslag: art. 6 lid 1 AVG
- Toetspunt: De afspraken noemen de grondslag waarop de verstrekker verstrekt en de ontvanger verwerkt
- Bronnen: AVG-art6-lid1 (AVG art. 6 lid 1)
- Wat de tekst moet bereiken: Noem op welke grondslag de gegevens worden verstrekt en verwerkt.

### K20.4 — Wie de betrokkenen informeert
- Grondslag: art. 13 en 14 AVG
- Toetspunt: De afspraken regelen hoe de betrokkenen worden geïnformeerd over de verstrekking en over de verwerking door de ontvanger
- Bronnen: AVG-art13-lid1 (AVG art. 13 lid 1); AVG-art14-lid1 (AVG art. 14 lid 1)
- Wat de tekst moet bereiken: Leg vast wie de betrokkenen informeert over de verstrekking en het gebruik door de ontvanger.

### K20.5 — Of de overdracht beveiligd is
- Grondslag: art. 32 AVG
- Toetspunt: De afspraken regelen passende beveiliging van de overdracht en van de gegevens bij de ontvanger
- Bronnen: AVG-art32-lid1 (AVG art. 32 lid 1)
- Wat de tekst moet bereiken: Leg vast hoe de gegevens beveiligd worden overgedragen en bewaard.

### K20.6 — Of datalekken onderling worden gemeld
- Grondslag: goede praktijk; art. 33 AVG als achtergrond
- Toetspunt: De afspraken regelen dat partijen elkaar informeren over een datalek dat de gedeelde gegevens raakt
- Bronnen: AVG-art33-lid1 (AVG art. 33 lid 1)
- Wat de tekst moet bereiken: Spreek af dat jullie elkaar direct informeren over een datalek met de gedeelde gegevens.

### K20.7 — Of verzoeken van betrokkenen worden doorgegeven
- Grondslag: goede praktijk; art. 12 en 19 AVG als achtergrond
- Toetspunt: De afspraken regelen dat partijen elkaar helpen of verzoeken doorsturen als een betrokkene zijn rechten uitoefent
- Bronnen: AVG-art12-lid3 (AVG art. 12 lid 3); AVG-art19 (AVG art. 19)
- Wat de tekst moet bereiken: Spreek af hoe jullie verzoeken van betrokkenen doorgeven en elkaar informeren over correcties en verwijderingen.

### K20.8 — Hoe lang de ontvanger bewaart
- Grondslag: goede praktijk; art. 5 lid 1 sub e AVG als achtergrond
- Toetspunt: De afspraken regelen hoe lang de ontvanger de gegevens bewaart of hoe die termijn wordt bepaald
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e)
- Wat de tekst moet bereiken: Leg vast hoe lang de ontvanger de gegevens bewaart.

### K20.9 — Of doorgifte buiten de EER is geregeld
- Grondslag: art. 44-46 AVG
- Toetspunt: Gaan gegevens buiten de EER, dan noemen de afspraken de doorgiftegrond (adequaatheidsbesluit of passende waarborgen)
- Alleen als: `facts.outside_eea != false`
- Bronnen: AVG-art44 (AVG art. 44); AVG-art46-lid1 (AVG art. 46 lid 1)
- Wat de tekst moet bereiken: Noem de doorgiftegrond, bijvoorbeeld standaardcontractbepalingen.

### K20.10 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 82 AVG als achtergrond
- Toetspunt: De afspraken regelen de aansprakelijkheid tussen partijen
- Bronnen: AVG-art82-lid1 (AVG art. 82 lid 1)
- Wat de tekst moet bereiken: Leg de onderlinge aansprakelijkheid vast.
