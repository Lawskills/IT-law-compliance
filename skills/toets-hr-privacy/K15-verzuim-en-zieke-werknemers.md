# Kader K15 — Verzuim en zieke werknemers

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een werkgever bij ziekte en verzuim alleen de gegevens verwerkt die hij mag verwerken: geen diagnose, aard of oorzaak van de ziekte; alleen wat nodig is voor loondoorbetaling, verzuimbegeleiding en re-integratie; medische gegevens alleen bij de bedrijfsarts of arbodienst.

Bronnen: AVG-art9-lid1 (AVG art. 9 lid 1); AVG-art9-lid2-b (AVG art. 9 lid 2 sub b); UAVG-art30-lid1-b (UAVG art. 30 lid 1 sub b); UAVG-art30-lid3 (UAVG art. 30 lid 3); AP-zieke-werknemer (Autoriteit Persoonsgegevens, informatie over de zieke werknemer (wat een werkgever mag vragen en vastleggen))

## Formulier (vragen aan de gebruiker)

- **records_diagnosis**: Vraag of noteer je (of een leidinggevende) wat een zieke medewerker mankeert: de diagnose, het soort ziekte of de oorzaak?
  - Label (voor de plek-om-in-te-vullen): of je vraagt of vastlegt wat een zieke medewerker mankeert
  - Hulp: Ook als de medewerker het uit zichzelf vertelt, mag je het niet vastleggen. Dat is aan de bedrijfsarts. Denk ook aan notities in e-mails, appjes of het HR-systeem.
  - Type: boolean
- **recorded_sick_data**: Welke gegevens leg je vast als een medewerker zich ziek meldt, en tijdens het verzuim?
  - Label (voor de plek-om-in-te-vullen): welke gegevens je bij een ziekmelding vastlegt
  - Hulp: Bijvoorbeeld: bereikbaarheid, verwachte duur, lopende afspraken, of er een derde aansprakelijk is, en de adviezen van de bedrijfsarts over wat de medewerker wel en niet kan.
  - Type: text
- **medical_data_only_by_doctor**: Komen medische gegevens alleen bij de bedrijfsarts of arbodienst terecht, en krijg je van hen alleen adviezen over werkhervatting en wat de medewerker wel en niet kan?
  - Label (voor de plek-om-in-te-vullen): of medische gegevens alleen bij de bedrijfsarts of arbodienst terechtkomen
  - Hulp: Kies nee als je bijvoorbeeld medische verklaringen, rapporten van specialisten of de volledige verslagen van de bedrijfsarts ontvangt of bewaart.
  - Type: boolean
- **absence_file_secured**: Is het verzuimdossier beveiligd, bijvoorbeeld in een afgeschermd systeem of een afgesloten kast?
  - Label (voor de plek-om-in-te-vullen): of het verzuimdossier beveiligd is
  - Type: boolean
- **absence_file_access_limited**: Kunnen alleen de mensen die het voor hun werk nodig hebben het verzuimdossier inzien, zoals HR en de direct leidinggevende?
  - Label (voor de plek-om-in-te-vullen): of alleen wie het nodig heeft het verzuimdossier kan inzien
  - Type: boolean
- **absence_retention**: Hoe lang bewaar je verzuimgegevens nadat het verzuim is afgelopen, of nadat de medewerker uit dienst is gegaan?
  - Label (voor de plek-om-in-te-vullen): hoe lang je verzuimgegevens bewaart
  - Hulp: Weet je het niet of is er geen vaste termijn, schrijf dat dan op.
  - Type: text

## Toetspunten

### K15.1 — Je vraagt of noteert niet wat een zieke medewerker mankeert
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Registreert of vraagt de werkgever de diagnose, aard of oorzaak van de ziekte? Niet toegestaan; dat is aan de bedrijfsarts, ook als de werknemer het uit zichzelf vertelt. Harde grens.
- Grondslag: art. 9 lid 1 AVG; art. 30 lid 1 sub b en lid 3 UAVG
- Beoordeeld op: de antwoorden
- Nodig: records_diagnosis
- Beoordeling:
  - Harde grens: geen afweging mogelijk.
  - present (in orde) als records_diagnosis onwaar is; absent (overtreding) als records_diagnosis waar is; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Ook als de werknemer de diagnose uit zichzelf vertelt, mag de werkgever die niet vastleggen: records_diagnosis waar blijft absent.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vraag en noteer nooit wat een zieke medewerker mankeert. Verwijder zulke notities uit dossiers, e-mails en systemen, en laat medische vragen over aan de bedrijfsarts.
- Bronnen: AVG-art9-lid1 (AVG art. 9 lid 1); UAVG-art30-lid1-b (UAVG art. 30 lid 1 sub b); UAVG-art30-lid3 (UAVG art. 30 lid 3); AP-zieke-werknemer (Autoriteit Persoonsgegevens, informatie over de zieke werknemer (wat een werkgever mag vragen en vastleggen))

### K15.2 — Je legt alleen vast wat nodig is voor loon, begeleiding en re-integratie
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Beperkt de werkgever zich tot wat nodig is voor loondoorbetaling, verzuimbegeleiding en re-integratie (bijvoorbeeld bereikbaarheid, verwachte duur, lopende afspraken, vangnetregeling, aansprakelijke derde, en functionele beperkingen en mogelijkheden zoals de bedrijfsarts die doorgeeft)?
- Grondslag: art. 5 lid 1 sub c AVG; art. 30 lid 1 sub b UAVG
- Beoordeeld op: de antwoorden
- Nodig: recorded_sick_data, records_diagnosis
- Beoordeling:
  - Art. 30 lid 1 UAVG is geen vrijbrief: de verwerking moet noodzakelijk zijn voor re-integratie of begeleiding.
  - Duidelijk compliant: recorded_sick_data noemt alleen gegevens uit de voorbeeldlijst (bereikbaarheid, verwachte duur, lopende afspraken, of de werknemer onder een vangnetregeling valt, of er een derde aansprakelijk is, functionele beperkingen en mogelijkheden zoals de bedrijfsarts die doorgeeft) of vergelijkbare administratieve gegevens (datum ziekmelding en herstelmelding).
  - Duidelijk non_compliant: recorded_sick_data noemt medische gegevens, zoals diagnose, klachten, medicijngebruik, behandelingen of medische verslagen, of records_diagnosis is waar.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is elk vastgelegd gegeven noodzakelijk voor loondoorbetaling, verzuimbegeleiding of re-integratie?
- Advies bij ❌ of ⚠️: Leg bij verzuim alleen vast wat je nodig hebt voor loondoorbetaling, begeleiding en re-integratie, zoals bereikbaarheid, verwachte duur, afspraken en de adviezen van de bedrijfsarts over wat de medewerker wel en niet kan.
- Bronnen: AVG-art5-lid1-c (AVG art. 5 lid 1 sub c); UAVG-art30-lid1-b (UAVG art. 30 lid 1 sub b); AP-zieke-werknemer (Autoriteit Persoonsgegevens, informatie over de zieke werknemer (wat een werkgever mag vragen en vastleggen))

### K15.3 — Medische gegevens blijven bij de bedrijfsarts of arbodienst
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Medische gegevens alleen door de bedrijfsarts of arbodienst verwerkt; de werkgever krijgt alleen de adviezen over werkhervatting
- Grondslag: art. 9 lid 1 AVG; art. 30 lid 3 UAVG
- Beoordeeld op: de antwoorden
- Nodig: medical_data_only_by_doctor
- Beoordeling:
  - present als medical_data_only_by_doctor waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Laat medische gegevens alleen verwerken door de bedrijfsarts of arbodienst. Vraag alleen de adviezen over werkhervatting en wat de medewerker wel en niet kan, en stuur medische stukken die je toch ontvangt terug of verwijder ze.
- Bronnen: AVG-art9-lid1 (AVG art. 9 lid 1); UAVG-art30-lid3 (UAVG art. 30 lid 3); AP-zieke-werknemer (Autoriteit Persoonsgegevens, informatie over de zieke werknemer (wat een werkgever mag vragen en vastleggen))

### K15.4 — Het verzuimdossier is beveiligd en alleen toegankelijk voor wie het nodig heeft
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Verzuimdossier beveiligd en alleen toegankelijk voor wie het nodig heeft (→ K11)
- Grondslag: art. 5 lid 1 sub f en art. 32 lid 1 AVG
- Beoordeeld op: de antwoorden
- Nodig: absence_file_secured, absence_file_access_limited
- Beoordeling:
  - present als absence_file_secured en absence_file_access_limited allebei waar zijn.
  - absent als een van beide onwaar is.
  - Ontbrekend of 'weet ik niet' bij een van beide (en de andere niet onwaar): ⚠️ (noem welk antwoord ontbreekt).
  - De beveiligingsmaatregelen zelf worden getoetst in K11.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Bewaar het verzuimdossier in een afgeschermd systeem of een afgesloten kast, en geef alleen HR en de direct leidinggevende toegang voor zover zij het nodig hebben.
- Bronnen: AVG-art5-lid1-f (AVG art. 5 lid 1 sub f); AVG-art32-lid1 (AVG art. 32 lid 1)

### K15.5 — Verzuimgegevens worden niet langer bewaard dan nodig
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bewaartermijn verzuimgegevens passend? (→ K4)
- Grondslag: art. 5 lid 1 sub e AVG
- Beoordeeld op: de antwoorden
- Nodig: absence_retention
- Beoordeling:
  - Duidelijk non_compliant: absence_retention zegt dat er geen termijn is of dat gegevens onbeperkt of 'voor altijd' worden bewaard.
  - absence_retention 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - De inhoudelijke beoordeling van de termijn gebeurt in K4; noem een concrete termijn met onderbouwing hooguit compliant als die termijn duidelijk kort is gekoppeld aan het einde van het verzuim of het dienstverband. Verzin geen termijn.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de bewaartermijn van de verzuimgegevens onderbouwd en niet langer dan nodig (zie K4)?
- Advies bij ❌ of ⚠️: Stel een vaste bewaartermijn vast voor verzuimgegevens, gekoppeld aan het einde van het verzuim of het dienstverband, en verwijder de gegevens daarna.
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); AP-zieke-werknemer (Autoriteit Persoonsgegevens, informatie over de zieke werknemer (wat een werkgever mag vragen en vastleggen))

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): recorded_sick_data. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 1 is een harde grens: de werkgever registreert of vraagt de diagnose, aard of oorzaak van de ziekte → non_compliant, ook als de werknemer het uit zichzelf vertelt. Geen afweging.
- Art. 30 lid 1 UAVG is geen vrijbrief: de verwerking moet noodzakelijk zijn voor re-integratie of begeleiding.
- Stap 4 → K11 (beveiliging); stap 5 → K4 (bewaartermijnen).

## Samenhang met andere kaders

- Kader K11 (/toets-beveiliging) — als `facts.absence_file_secured != true or facts.absence_file_access_limited != true`: Het verzuimdossier bevat gevoelige gegevens en moet goed beveiligd zijn.
- Kader K4 (/toets-beginselen) — als `true`: De bewaartermijn van verzuimgegevens wordt getoetst bij de beginselen en bewaartermijnen.
