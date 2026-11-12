# Kader K21 — Privacy bij werving en selectie

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een organisatie bij werving en selectie een geldige grondslag heeft, sollicitanten informeert, niet meer gegevens vraagt dan nodig, zorgvuldig screent, niet te lang bewaart, geautomatiseerde selectie begrenst en de toegang beperkt.

Bronnen: AP-werving-selectie (Uitleg van de Autoriteit Persoonsgegevens over persoonsgegevens bij sollicitaties); AVG-art13-lid1 (AVG art. 13 lid 1); AVG-art13-lid2 (AVG art. 13 lid 2); AVG-art22-lid1 (AVG art. 22 lid 1); AVG-art22-lid3 (AVG art. 22 lid 3); AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art35-lid1 (AVG art. 35 lid 1); AVG-art5-lid1-a (AVG art. 5 lid 1 sub a); AVG-art5-lid1-c (AVG art. 5 lid 1 sub c); AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); AVG-art5-lid1-f (AVG art. 5 lid 1 sub f); AVG-art6-lid1 (AVG art. 6 lid 1); AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); AVG-art7-lid4 (AVG art. 7 lid 4); AVG-art9-lid1 (AVG art. 9 lid 1); AVG-overw43 (AVG overweging 43); NVP-sollicitatiecode (Sollicitatiecode van de Nederlandse Vereniging voor Personeelsmanagement & Organisatieontwikkeling (NVP)); UAVG-art46 (UAVG art. 46)

## Formulier (vragen aan de gebruiker)

- **basis_determined**: Heb je bepaald op welke grondslag je sollicitatiegegevens verwerkt (bijvoorbeeld de stappen voor een arbeidsovereenkomst of je gerechtvaardigd belang)?
  - Label (voor de plek-om-in-te-vullen): of je de grondslag hebt bepaald
  - Type: boolean
- **relies_on_consent**: Vraag je sollicitanten toestemming als grondslag voor de gewone procedure?
  - Label (voor de plek-om-in-te-vullen): of je toestemming als grondslag gebruikt
  - Type: boolean
- **applicants_informed**: Informeer je sollicitanten over wat je met hun gegevens doet (bijvoorbeeld in een privacyverklaring voor sollicitanten of in de vacature)?
  - Label (voor de plek-om-in-te-vullen): of je sollicitanten informeert
  - Type: boolean
- **asks_bsn_or_health**: Vraag je sollicitanten om hun BSN, een kopie van hun paspoort of gegevens over hun gezondheid?
  - Label (voor de plek-om-in-te-vullen): of je om BSN of gezondheidsgegevens vraagt
  - Type: boolean
- **online_screening**: Zoek je sollicitanten op internet of sociale media op, of bel je referenten?
  - Label (voor de plek-om-in-te-vullen): of je sollicitanten online screent of referenties natrekt
  - Type: boolean
- **screening_safeguards**: Doe je dat alleen als het nodig is voor de functie, informeer je de sollicitant vooraf en mag hij reageren op wat je vindt?
  - Label (voor de plek-om-in-te-vullen): of je dat zorgvuldig doet
  - Type: boolean · Alleen vragen als: `facts.online_screening != false`
- **retention**: Hoe lang bewaar je gegevens van afgewezen sollicitanten?
  - Label (voor de plek-om-in-te-vullen): hoe lang je gegevens van afgewezen sollicitanten bewaart
  - Type: enum (four_weeks / year_with_consent / longer)
- **automated_selection**: Selecteert of wijst software sollicitanten automatisch af, zonder dat een mens het besluit neemt?
  - Label (voor de plek-om-in-te-vullen): of software sollicitanten automatisch selecteert of afwijst
  - Type: boolean
- **human_review**: Kijkt een mens inhoudelijk naar elke afwijzing voordat die wordt verstuurd?
  - Label (voor de plek-om-in-te-vullen): of een mens het besluit neemt
  - Type: boolean · Alleen vragen als: `facts.automated_selection != false`
- **assessments**: Gebruik je persoonlijkheidstests, assessments of video-analyses?
  - Label (voor de plek-om-in-te-vullen): of je assessments of tests gebruikt
  - Type: boolean
- **access_limited**: Hebben alleen de mensen die bij de selectie betrokken zijn toegang tot de sollicitatiegegevens?
  - Label (voor de plek-om-in-te-vullen): of alleen betrokkenen toegang hebben
  - Type: boolean

## Toetspunten

### K21.1 — Of je een geldige grondslag hebt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De verwerking van sollicitatiegegevens rust op een grondslag van art. 6; toestemming is in een sollicitatieprocedure zelden vrij gegeven en dus meestal geen geschikte grondslag voor de gewone procedure
- Grondslag: art. 6 lid 1 en art. 7 lid 4 AVG
- Beoordeeld op: de antwoorden
- Nodig: basis_determined
- Beoordeling:
  - Duidelijk geval non_compliant: basis_determined false.
  - Duidelijk geval compliant: basis_determined true en relies_on_consent false.
  - relies_on_consent true: geen duidelijk geval (een juridisch adviseur beoordeelt of de toestemming vrij is gegeven).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is de gekozen grondslag geschikt?
- Advies bij ❌ of ⚠️: Gebruik voor de gewone procedure de stappen voor een arbeidsovereenkomst of je gerechtvaardigd belang, en vraag alleen toestemming voor iets extra's (zoals langer bewaren).
- Bronnen: AVG-art6-lid1 (AVG art. 6 lid 1); AVG-art7-lid4 (AVG art. 7 lid 4); AVG-overw43 (AVG overweging 43)

### K21.2 — Of je sollicitanten informeert
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Sollicitanten krijgen bij het verzamelen de informatie van art. 13 AVG (wie, waarvoor, grondslag, ontvangers, bewaartermijn, rechten)
- Grondslag: art. 13 AVG
- Beoordeeld op: de antwoorden
- Nodig: applicants_informed
- Beoordeling:
  - present als applicants_informed true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Maak een privacyverklaring voor sollicitanten en verwijs ernaar in de vacature en de sollicitatieomgeving.
- Bronnen: AVG-art13-lid1 (AVG art. 13 lid 1); AVG-art13-lid2 (AVG art. 13 lid 2)

### K21.3 — Of je niet meer vraagt dan nodig
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Er worden niet meer gegevens verwerkt dan nodig; het BSN wordt niet vóór indiensttreding gevraagd en gezondheidsgegevens worden niet gevraagd
- Grondslag: art. 5 lid 1 sub c en art. 9 AVG; art. 46 UAVG
- Beoordeeld op: de antwoorden
- Nodig: asks_bsn_or_health
- Beoordeling:
  - present als asks_bsn_or_health false is; absent als true.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vraag geen BSN, kopie identiteitsbewijs of gezondheidsgegevens tijdens de sollicitatie; het BSN pas bij indiensttreding.
- Bronnen: AVG-art5-lid1-c (AVG art. 5 lid 1 sub c); AVG-art9-lid1 (AVG art. 9 lid 1); UAVG-art46 (UAVG art. 46)

### K21.4 — Of online screening en referenties zorgvuldig gebeuren
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Online screening en het natrekken van referenties gebeuren alleen als dat nodig en evenredig is voor de functie, met vooraf informeren en de mogelijkheid om te reageren
- Grondslag: art. 6 lid 1 sub f en art. 5 lid 1 sub a en c AVG
- Alleen als: `facts.online_screening != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: screening_safeguards
- Beoordeling:
  - Duidelijk geval compliant: screening_safeguards true.
  - Duidelijk geval non_compliant: screening_safeguards false.
  - Ontbrekend of "weet ik niet": ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is de screening nodig en evenredig?
- Advies bij ❌ of ⚠️: Screen online en bel referenten alleen als het nodig is voor de functie; zeg het vooraf en laat de sollicitant reageren.
- Bronnen: AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); AVG-art5-lid1-a (AVG art. 5 lid 1 sub a); AP-werving-selectie (Uitleg van de Autoriteit Persoonsgegevens over persoonsgegevens bij sollicitaties)

### K21.5 — Of je gegevens van afgewezen sollicitanten niet te lang bewaart
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Gegevens van afgewezen sollicitanten worden niet langer bewaard dan nodig; volgens de uitleg van de AP en de NVP Sollicitatiecode tot vier weken na de procedure, of tot een jaar met toestemming
- Grondslag: art. 5 lid 1 sub e AVG; uitleg AP en NVP Sollicitatiecode
- Beoordeeld op: de antwoorden
- Nodig: retention
- Beoordeling:
  - present als retention four_weeks of year_with_consent is; absent als longer.
  - De termijn is uitleg, geen wettekst: ontbreken of overschrijden geeft review.
- Is het vereiste afwezig (*absent*): ⚠️
- Advies bij ❌ of ⚠️: Verwijder gegevens van afgewezen sollicitanten vier weken na de procedure, of bewaar ze tot een jaar alleen met hun toestemming.
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); NVP-sollicitatiecode (Sollicitatiecode van de Nederlandse Vereniging voor Personeelsmanagement & Organisatieontwikkeling (NVP)); AP-werving-selectie (Uitleg van de Autoriteit Persoonsgegevens over persoonsgegevens bij sollicitaties)

### K21.6 — Of een mens beslist over afwijzingen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Een sollicitant wordt niet onderworpen aan een besluit dat uitsluitend op geautomatiseerde verwerking berust en hem aanmerkelijk treft, tenzij een uitzondering geldt met passende maatregelen
- Grondslag: art. 22 AVG
- Alleen als: `facts.automated_selection != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: human_review
- Beoordeling:
  - Duidelijk geval compliant: human_review true.
  - human_review false: geen duidelijk geval (een juridisch adviseur beoordeelt of een uitzondering van art. 22 lid 2 geldt); meestal moet een mens beslissen.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is er sprake van een besluit uitsluitend op geautomatiseerde verwerking, en geldt een uitzondering?
- Advies bij ❌ of ⚠️: Laat een mens inhoudelijk naar elke afwijzing kijken voordat die wordt verstuurd.
- Bronnen: AVG-art22-lid1 (AVG art. 22 lid 1); AVG-art22-lid3 (AVG art. 22 lid 3)

### K21.7 — Of je bij assessments een DPIA overweegt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Bij persoonlijkheidstests, assessments of video-analyses beoordeelt de organisatie of een DPIA verplicht is
- Grondslag: art. 35 AVG
- Alleen als: `facts.assessments != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Beoordeling:
  - Deze stap verwijst naar K9; hij is altijd review.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Is een DPIA nodig voor de gebruikte tests of assessments?
- Advies bij ❌ of ⚠️: Beoordeel met de DPIA-check of een DPIA nodig is voor de tests of assessments.
- Bronnen: AVG-art35-lid1 (AVG art. 35 lid 1)

### K21.8 — Of alleen betrokkenen toegang hebben
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Alleen wie bij de selectie betrokken is, heeft toegang tot de sollicitatiegegevens
- Grondslag: art. 5 lid 1 sub f en art. 32 AVG
- Beoordeeld op: de antwoorden
- Nodig: access_limited
- Beoordeling:
  - present als access_limited true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Beperk de toegang tot sollicitatiegegevens tot de mensen die bij de selectie betrokken zijn.
- Bronnen: AVG-art5-lid1-f (AVG art. 5 lid 1 sub f); AVG-art32-lid1 (AVG art. 32 lid 1)

## Regels van dit kader

- Een verplichte F-stap absent → non_compliant.
- De bewaartermijn (stap 5) volgt uit uitleg van de AP en de NVP-code: ontbreken of overschrijden geeft review, niet non_compliant.

## Samenhang met andere kaders

- Kader AI2 (/toets-ai-act-basis) — als `facts.automated_selection != false`: AI voor werving en selectie kan een hoogrisicosysteem zijn (bijlage III punt 4 AI-verordening).
- Kader K16 (/toets-geautomatiseerde-besluiten) — als `facts.automated_selection != false`: Een afwijzing zonder menselijke tussenkomst valt onder art. 22 AVG.
- Kader K9 (/dpia) — als `facts.assessments != false`: Bij persoonlijkheidstests of assessments kan een DPIA nodig zijn.

## Open punten en voorbehouden

- De uitleg van de AP over sollicitaties (bewaartermijn, online screening, referenties) letterlijk nalezen en de vindplaats vastleggen.
- Art. 46 UAVG (BSN) en art. 9 AVG met art. 30 UAVG letterlijk nalezen.
