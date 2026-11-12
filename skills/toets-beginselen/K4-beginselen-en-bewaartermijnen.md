# Kader K4 — Beginselen en bewaartermijnen

Versie 1.2 · peildatum 2026-11-10

Doel: Toetsen aan de beginselen van art. 5 AVG: doelbinding, minimale gegevensverwerking, juistheid, opslagbeperking (bewaartermijnen en verwijderen), en de verwijzing naar rechtmatigheid, transparantie en beveiliging in andere kaders.

Bronnen: AVG-art5 (AVG art. 5); AVG-art6-lid4 (AVG art. 6 lid 4); AWR-art52-lid4 (Algemene wet inzake rijksbelastingen art. 52 lid 4 (fiscale bewaarplicht 7 jaar)); BW-art2-10-lid3 (Burgerlijk Wetboek art. 2:10 lid 3 (bewaarplicht administratie 7 jaar)); HvJEU-C-77-21 (HvJEU 20 oktober 2022, C-77/21, Digi)

## Formulier (vragen aan de gebruiker)

- **purposes_description**: Voor welke doelen gebruik je persoonsgegevens? Noem elk doel apart, zo concreet mogelijk.
  - Label (voor de plek-om-in-te-vullen): de doelen waarvoor je gegevens gebruikt
  - Hulp: Bijvoorbeeld: 'bestellingen bezorgen', 'salaris betalen', 'nieuwsbrief sturen'. Een algemene omschrijving als 'bedrijfsvoering' is niet genoeg.
  - Type: text
- **data_per_purpose**: Welke gegevens verzamel je per doel? Noem de velden, bijvoorbeeld van je formulieren.
  - Label (voor de plek-om-in-te-vullen): welke gegevens je per doel verzamelt
  - Type: text
- **collects_unneeded_data**: Vraag of bewaar je gegevens die je voor je doelen eigenlijk niet nodig hebt, bijvoorbeeld omdat ze 'handig om te hebben' zijn?
  - Label (voor de plek-om-in-te-vullen): of je gegevens verzamelt die je eigenlijk niet nodig hebt
  - Type: boolean
- **can_correct_data**: Kun je gegevens van mensen corrigeren of bijwerken als ze niet (meer) kloppen?
  - Label (voor de plek-om-in-te-vullen): of je gegevens kunt corrigeren of bijwerken
  - Type: boolean
- **retention_defined**: Heb je per doel vastgelegd hoe lang je de gegevens bewaart, als termijn of als duidelijk criterium?
  - Label (voor de plek-om-in-te-vullen): of je per doel een bewaartermijn hebt vastgelegd
  - Hulp: Een criterium is bijvoorbeeld 'tot twee jaar na de laatste bestelling' of 'tot de sollicitatieprocedure is afgerond plus vier weken'.
  - Type: boolean
- **retention_periods**: Welke bewaartermijn of welk criterium geldt per doel?
  - Label (voor de plek-om-in-te-vullen): de bewaartermijn per doel
  - Type: text · Alleen vragen als: `facts.retention_defined == true`
- **retention_rationale**: Waarom heb je voor deze termijnen gekozen? Noem een wet als die de termijn voorschrijft.
  - Label (voor de plek-om-in-te-vullen): waarom je voor die bewaartermijnen hebt gekozen
  - Type: text · Alleen vragen als: `facts.retention_defined == true`
- **has_deletion_procedure**: Heb je een werkende manier om gegevens na afloop van de bewaartermijn te verwijderen of anoniem te maken?
  - Label (voor de plek-om-in-te-vullen): of je gegevens na afloop van de termijn verwijdert
  - Type: boolean
- **deletion_covers_backups**: Verdwijnen de gegevens dan ook uit je back-ups?
  - Label (voor de plek-om-in-te-vullen): of dat ook in back-ups gebeurt
  - Hulp: Bijvoorbeeld doordat back-ups na een vaste periode worden overschreven of verwijderd.
  - Type: boolean · Alleen vragen als: `facts.has_deletion_procedure == true`
- **uses_personal_data_in_test**: Gebruik je echte gegevens van klanten of medewerkers in een test- of ontwikkelomgeving?
  - Label (voor de plek-om-in-te-vullen): of je echte gegevens van mensen gebruikt om software te testen
  - Type: boolean
- **deletion_covers_test**: Worden die gegevens ook in de test- of ontwikkelomgeving verwijderd of anoniem gemaakt als de bewaartermijn voorbij is?
  - Label (voor de plek-om-in-te-vullen): of die gegevens ook uit de testomgeving worden verwijderd
  - Type: boolean · Alleen vragen als: `facts.uses_personal_data_in_test == true`

## Toetspunten

### K4.1 — Of je duidelijk hebt omschreven waarvoor je gegevens gebruikt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Doelbinding: elk doel vooraf, welbepaald en uitdrukkelijk omschreven
- Grondslag: art. 5 lid 1 sub b AVG
- Beoordeeld op: de antwoorden
- Nodig: purposes_description
- Beoordeling:
  - Duidelijk non_compliant: 'bedrijfsvoering' of 'verbetering van diensten' (of een vergelijkbaar algemene term) is de enige omschrijving van een doel.
  - Duidelijk compliant: elk genoemd doel is concreet genoeg dat een buitenstaander begrijpt wat er met de gegevens gebeurt.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn alle doelen welbepaald en uitdrukkelijk omschreven?
- Advies bij ❌ of ⚠️: Omschrijf elk doel concreet, zodat iemand begrijpt wat je met de gegevens doet, bijvoorbeeld 'bestellingen bezorgen' in plaats van 'bedrijfsvoering'.
- Bronnen: AVG-art5-lid1-b (AVG art. 5 lid 1 sub b); AVG-art6-lid4 (AVG art. 6 lid 4); HvJEU-C-77-21 (HvJEU 20 oktober 2022, C-77/21, Digi)

### K4.2 — Of je niet meer gegevens verzamelt dan nodig
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Minimale gegevensverwerking: toereikend, ter zake dienend en beperkt tot wat nodig is, per veld nagaan
- Grondslag: art. 5 lid 1 sub c AVG
- Beoordeeld op: de antwoorden
- Nodig: purposes_description, data_per_purpose, collects_unneeded_data
- Beoordeling:
  - Loop per veld in data_per_purpose na of het nodig is voor een doel in purposes_description.
  - Duidelijk non_compliant: collects_unneeded_data is waar, of data_per_purpose noemt een veld dat voor geen enkel genoemd doel nodig is.
  - Duidelijk compliant: collects_unneeded_data is onwaar en elk veld hoort aantoonbaar bij een genoemd doel.
  - In alle andere gevallen geen duidelijk geval (ook als collects_unneeded_data onbekend is).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Welke velden zijn niet nodig voor de genoemde doelen?
- Advies bij ❌ of ⚠️: Loop je formulieren en systemen na en schrap de gegevens die je voor geen van je doelen nodig hebt.
- Bronnen: AVG-art5-lid1-c (AVG art. 5 lid 1 sub c)

### K4.3 — Of je gegevens kunt corrigeren en bijwerken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Juistheid: er is een manier om gegevens te corrigeren of bij te werken
- Grondslag: art. 5 lid 1 sub d AVG
- Beoordeeld op: de antwoorden
- Nodig: can_correct_data
- Beoordeling:
  - present als can_correct_data waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zorg dat je gegevens in al je systemen kunt corrigeren en bijwerken als ze niet (meer) kloppen.
- Bronnen: AVG-art5-lid1-d (AVG art. 5 lid 1 sub d)

### K4.4 — Of je per doel een bewaartermijn hebt vastgelegd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Opslagbeperking: per doel een termijn of een criterium benoemd
- Grondslag: art. 5 lid 1 sub e AVG
- Beoordeeld op: de antwoorden
- Nodig: retention_defined, retention_periods
- Beoordeling:
  - present als retention_defined waar is en retention_periods voor elk doel uit purposes_description een termijn of een criterium noemt.
  - absent als retention_defined onwaar is.
  - absent als voor een of meer doelen geen termijn of criterium in retention_periods staat.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is voor elk doel een termijn of criterium vastgelegd?
- Advies bij ❌ of ⚠️: Leg per doel vast hoe lang je de gegevens bewaart, als termijn of als duidelijk criterium.
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e)

### K4.5 — Of je bewaartermijnen passend zijn
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bewaartermijn passend: wettelijke termijn volgen; anders eigen, onderbouwde afweging; 'zo lang als nodig' zonder criterium is onvoldoende
- Grondslag: art. 5 lid 1 sub e AVG; art. 52 lid 4 AWR; art. 2:10 lid 3 BW
- Alleen als: `facts.retention_defined == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: retention_periods, retention_rationale
- Beoordeling:
  - Duidelijk non_compliant: een termijn luidt 'zo lang als nodig' (of vergelijkbaar) zonder criterium.
  - Wettelijke termijn: die volgen. Voorbeeld: basisadministratie en boekhouding 7 jaar (art. 52 lid 4 AWR, art. 2:10 lid 3 BW). Pas andere wettelijke termijnen alleen toe als ze in de bronnendatabase staan, niet uit het hoofd.
  - Geen wettelijke termijn: eigen, onderbouwde afweging. Duidelijk compliant alleen als retention_rationale per termijn een onderbouwing geeft, of een wettelijke termijn noemt die in de bronnendatabase staat.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de termijnen onderbouwd, en kloppen de genoemde wettelijke termijnen?
- Advies bij ❌ of ⚠️: Volg de wettelijke bewaartermijn waar die bestaat (bijvoorbeeld 7 jaar voor de boekhouding). Leg voor de andere gegevens vast waarom je voor een termijn kiest.
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); AWR-art52-lid4 (Algemene wet inzake rijksbelastingen art. 52 lid 4 (fiscale bewaarplicht 7 jaar)); BW-art2-10-lid3 (Burgerlijk Wetboek art. 2:10 lid 3 (bewaarplicht administratie 7 jaar))

### K4.6 — Of je gegevens na afloop ook echt verwijdert, ook uit back-ups en testomgevingen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Werkende procedure om na afloop te verwijderen of te anonimiseren, ook in back-ups en testomgevingen
- Grondslag: art. 5 lid 1 sub e AVG
- Beoordeeld op: de antwoorden
- Nodig: has_deletion_procedure, deletion_covers_backups, uses_personal_data_in_test, deletion_covers_test
- Beoordeling:
  - present als has_deletion_procedure waar is, deletion_covers_backups waar is, en uses_personal_data_in_test onwaar is of deletion_covers_test waar is.
  - absent als has_deletion_procedure onwaar is.
  - absent als deletion_covers_backups onwaar is, of als uses_personal_data_in_test waar is en deletion_covers_test onwaar is (C-77/21: testdatabase met klantgegevens).
  - Ontbrekend of 'weet ik niet' bij een van deze feiten: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Richt een vaste procedure in om gegevens na afloop van de termijn te verwijderen of anoniem te maken, ook in back-ups en in test- en ontwikkelomgevingen.
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); HvJEU-C-77-21 (HvJEU 20 oktober 2022, C-77/21, Digi)

### K4.7 — Of je gegevens rechtmatig, behoorlijk en transparant gebruikt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Rechtmatigheid, behoorlijkheid en transparantie; getoetst via K2 en K5
- Grondslag: art. 5 lid 1 sub a AVG
- Beoordeeld op: de antwoorden
- Beoordeling:
  - Signalerende stap: dit beginsel wordt getoetst via K2 (grondslag) en K5 (informatieplicht). De stap beoordeelt niets zelf.
  - Uitkomst altijd review met verwijzing naar K2 en K5.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de grondslag- en informatieplichttoets uitgevoerd?
- Advies bij ❌ of ⚠️: Laat ook je grondslagen en je privacyverklaring toetsen.
- Bronnen: AVG-art5-lid1-a (AVG art. 5 lid 1 sub a)

### K4.8 — Of je gegevens goed beveiligt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Integriteit en vertrouwelijkheid; getoetst via K11
- Grondslag: art. 5 lid 1 sub f AVG
- Beoordeeld op: de antwoorden
- Beoordeling:
  - Signalerende stap: dit beginsel wordt getoetst via K11 (beveiliging). De stap beoordeelt niets zelf.
  - Uitkomst altijd review met verwijzing naar K11.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Is de beveiligingstoets uitgevoerd?
- Advies bij ❌ of ⚠️: Laat ook je beveiliging toetsen.
- Bronnen: AVG-art5-lid1-f (AVG art. 5 lid 1 sub f)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): purposes_description, data_per_purpose, retention_periods. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 1: 'bedrijfsvoering' of 'verbetering van diensten' als enige omschrijving → duidelijk geval → non_compliant.
- Stap 4: geen termijn of criterium per doel → non_compliant.
- Stap 5: wettelijke termijn → die volgen; geen wettelijke termijn → eigen, onderbouwde afweging; 'zo lang als nodig' zonder criterium → non_compliant.
- Stap 5: andere wettelijke termijnen dan de 7 jaar van art. 52 lid 4 AWR en art. 2:10 lid 3 BW per wet in de bronnendatabase vastleggen, niet uit het hoofd toepassen.
- Stap 6: verwijderen moet ook in back-ups en testomgevingen werken (C-77/21).

## Samenhang met andere kaders

- Kader K2 (/toets-grondslag) — als `true`: Rechtmatigheid (art. 5 lid 1 sub a) wordt getoetst via de grondslag.
- Kader K5 (/privacyverklaring) — als `true`: Behoorlijkheid en transparantie (art. 5 lid 1 sub a) worden getoetst via de informatieplicht.
- Kader K11 (/toets-beveiliging) — als `true`: Integriteit en vertrouwelijkheid (art. 5 lid 1 sub f) worden getoetst via beveiliging.

## Open punten en voorbehouden

- Stap 3 (juistheid) toetst alleen of corrigeren mogelijk is, niet of gegevens daadwerkelijk juist zijn.
