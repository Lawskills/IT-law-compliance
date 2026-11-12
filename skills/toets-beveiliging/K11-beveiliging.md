# Kader K11 — Beveiliging

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of de organisatie passende technische en organisatorische maatregelen heeft genomen om persoonsgegevens te beveiligen, afgestemd op het risico (art. 32 AVG).

Bronnen: AVG-art32 (AVG art. 32); AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art32-lid2 (AVG art. 32 lid 2); AVG-art32-lid4 (AVG art. 32 lid 4); HvJEU-C-340-21 (HvJEU 14 december 2023, C-340/21, Natsionalna agentsia za prihodite); AP-boete-HagaZiekenhuis-2019 (Autoriteit Persoonsgegevens, boetebesluit HagaZiekenhuis (logging en toegang tot patiëntendossiers)); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

## Formulier (vragen aan de gebruiker)

- **data_description**: Welke persoonsgegevens gebruik je, van wie, en ongeveer van hoeveel mensen?
  - Label (voor de plek-om-in-te-vullen): welke persoonsgegevens je gebruikt en van hoeveel mensen
  - Hulp: Bijvoorbeeld: 'Naam, adres en bestellingen van ongeveer 5.000 klanten, en personeelsdossiers van 20 medewerkers.'
  - Type: text
- **special_categories**: Gebruik je gegevens over gezondheid, geloof, ras of etnische afkomst, politieke voorkeur, vakbondslidmaatschap, seksuele leven of geaardheid, of biometrische of genetische gegevens?
  - Label (voor de plek-om-in-te-vullen): of je gevoelige gegevens gebruikt
  - Hulp: Ook ziekmeldingen van medewerkers of medische informatie van klanten tellen mee.
  - Type: boolean
- **risk_assessed**: Heb je ingeschat wat er mis kan gaan met de gegevens (uitlekken, verlies, onbevoegde wijziging), hoe groot die kans is en hoe ernstig de gevolgen voor de mensen zijn?
  - Label (voor de plek-om-in-te-vullen): of je het beveiligingsrisico hebt ingeschat
  - Hulp: Een korte, vastgelegde inschatting is genoeg. Hij hoort ook rekening te houden met wat technisch gangbaar is en wat maatregelen kosten.
  - Type: boolean
- **risk_assessment_description**: Beschrijf kort hoe je het risico hebt ingeschat en wat daaruit kwam.
  - Label (voor de plek-om-in-te-vullen): hoe je het risico hebt ingeschat
  - Type: text · Alleen vragen als: `facts.risk_assessed == true`
- **risk_level**: Hoe ernstig zijn de gevolgen voor de mensen als deze gegevens uitlekken of verloren gaan?
  - Label (voor de plek-om-in-te-vullen): hoe ernstig de gevolgen voor mensen zijn als het misgaat
  - Type: enum (low / medium / high)
- **access_need_to_know**: Kunnen medewerkers alleen bij de gegevens die ze voor hun werk nodig hebben?
  - Label (voor de plek-om-in-te-vullen): of medewerkers alleen toegang hebben tot de gegevens die ze nodig hebben
  - Hulp: Bijvoorbeeld: alleen HR kan personeelsdossiers openen, en de klantenservice ziet geen betaalgegevens.
  - Type: boolean
- **strong_authentication**: Is voor inloggen van buiten kantoor en voor beheerdersaccounts meer nodig dan alleen een wachtwoord?
  - Label (voor de plek-om-in-te-vullen): of er sterke inlogbeveiliging is voor toegang op afstand en beheeraccounts
  - Hulp: Bijvoorbeeld een code via een app of sms, of een beveiligingssleutel (tweestapsverificatie).
  - Type: boolean
- **encryption_devices**: Zijn laptops, telefoons, USB-sticks en andere apparaten waarop persoonsgegevens staan versleuteld?
  - Label (voor de plek-om-in-te-vullen): of laptops, telefoons en andere gegevensdragers versleuteld zijn
  - Hulp: Bijvoorbeeld met BitLocker (Windows) of FileVault (Mac). Staat er op apparaten nooit iets opgeslagen, kies dan ja.
  - Type: boolean
- **encryption_connections**: Gaan gegevens altijd via een versleutelde verbinding, bijvoorbeeld https op je website en een beveiligde verbinding voor e-mail en thuiswerken?
  - Label (voor de plek-om-in-te-vullen): of verbindingen versleuteld zijn
  - Type: boolean
- **backups_restorable**: Maak je regelmatig back-ups, en kun je daarmee de gegevens op tijd terugzetten als er iets misgaat?
  - Label (voor de plek-om-in-te-vullen): of je back-ups maakt waarmee je gegevens kunt terugzetten
  - Type: boolean
- **access_logging**: Wordt bijgehouden wie welke gevoelige gegevens heeft bekeken of gewijzigd?
  - Label (voor de plek-om-in-te-vullen): of wordt vastgelegd wie gevoelige gegevens bekijkt
  - Hulp: Bijvoorbeeld een logboek in je HR-, patiënten- of klantensysteem.
  - Type: boolean
- **patch_policy**: Worden updates voor besturingssystemen, programma's en apparaten op tijd geïnstalleerd?
  - Label (voor de plek-om-in-te-vullen): of software op tijd wordt bijgewerkt
  - Hulp: Bijvoorbeeld automatische updates, of een vaste afspraak wie updates controleert en installeert.
  - Type: boolean
- **staff_confidentiality**: Hebben medewerkers die met persoonsgegevens werken een geheimhoudingsplicht, en krijgen zij instructies over veilig werken met gegevens?
  - Label (voor de plek-om-in-te-vullen): of medewerkers geheimhouding en instructies hebben
  - Hulp: Bijvoorbeeld een geheimhoudingsclausule in het arbeidscontract en een jaarlijkse korte training over phishing en veilig werken.
  - Type: boolean
- **measures_tested**: Controleer je regelmatig of de beveiligingsmaatregelen werken, bijvoorbeeld door een test, een audit of een jaarlijkse evaluatie?
  - Label (voor de plek-om-in-te-vullen): of je de maatregelen regelmatig test en evalueert
  - Type: boolean
- **security_description**: Welke andere beveiligingsmaatregelen heb je, of wil je nog iets toelichten?
  - Label (voor de plek-om-in-te-vullen): welke beveiligingsmaatregelen je verder hebt
  - Type: text
- **cbw_applies**: Valt je organisatie onder de Cyberbeveiligingswet?
  - Label (voor de plek-om-in-te-vullen): of je organisatie onder de Cyberbeveiligingswet valt
  - Hulp: Deze wet geldt voor middelgrote en grote organisaties in bepaalde sectoren, zoals energie, vervoer, zorg, digitale diensten en afvalbeheer.
  - Type: boolean

## Toetspunten

### K11.1 — Je hebt het beveiligingsrisico ingeschat
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Risico ingeschat: stand van de techniek, uitvoeringskosten, aard, omvang, context en doel van de verwerking, kans en ernst van de risico's
- Grondslag: art. 32 lid 1 (aanhef) en lid 2 AVG
- Beoordeeld op: de antwoorden
- Nodig: risk_assessed, risk_assessment_description, risk_level, data_description
- Beoordeling:
  - Duidelijk non_compliant: risk_assessed onwaar.
  - Duidelijk compliant: risk_assessed waar én risk_assessment_description laat zien dat kans en ernst van de risico's voor de betrokkenen zijn afgewogen, passend bij data_description.
  - risk_assessed 'weet ik niet' of risk_level 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het risico voor de betrokkenen realistisch ingeschat, gezien de aard, omvang en context van de verwerking?
- Advies bij ❌ of ⚠️: Leg kort vast wat er met de gegevens mis kan gaan, hoe waarschijnlijk dat is en hoe ernstig de gevolgen voor de mensen zijn. Kies op basis daarvan je maatregelen.
- Bronnen: AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art32-lid2 (AVG art. 32 lid 2); HvJEU-C-340-21 (HvJEU 14 december 2023, C-340/21, Natsionalna agentsia za prihodite)

### K11.2a — Medewerkers kunnen alleen bij de gegevens die ze nodig hebben
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Basismaatregel (keuze van dit kader, geen wettelijke lijst): toegang op basis van noodzaak (wie mag wat)
- Grondslag: art. 32 lid 1 sub b AVG (vertrouwelijkheid)
- Beoordeeld op: de antwoorden
- Nodig: access_need_to_know
- Beoordeling:
  - Deze maatregel komt uit een minimumset die in dit kader is gekozen; het is geen wettelijke lijst.
  - present als access_need_to_know waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Beslisregel bij absent: risk_level high, special_categories waar, of risk_level of special_categories 'weet ik niet' → non_compliant (❌). risk_level low of medium én special_categories onwaar → review (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het ontbreken van toegangsbeperking bij dit risico een tekort dat direct hersteld moet worden?
- Advies bij ❌ of ⚠️: Richt de toegang zo in dat medewerkers alleen bij de gegevens kunnen die ze voor hun werk nodig hebben, en controleer de rechten regelmatig.
- Bronnen: AVG-art32-lid1-b (AVG art. 32 lid 1 sub b); AVG-art32-lid2 (AVG art. 32 lid 2)

### K11.2b — Inloggen op afstand en met beheeraccounts is extra beveiligd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Basismaatregel (keuze van dit kader, geen wettelijke lijst): sterke authenticatie, minstens voor toegang op afstand en beheeraccounts
- Grondslag: art. 32 lid 1 sub b AVG (vertrouwelijkheid)
- Beoordeeld op: de antwoorden
- Nodig: strong_authentication
- Beoordeling:
  - Deze maatregel komt uit een minimumset die in dit kader is gekozen; het is geen wettelijke lijst.
  - present als strong_authentication waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Beslisregel bij absent: risk_level high, special_categories waar, of risk_level of special_categories 'weet ik niet' → non_compliant (❌). risk_level low of medium én special_categories onwaar → review (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het ontbreken van sterke authenticatie bij dit risico een tekort dat direct hersteld moet worden?
- Advies bij ❌ of ⚠️: Zet tweestapsverificatie aan voor inloggen van buiten kantoor en voor alle beheerdersaccounts.
- Bronnen: AVG-art32-lid1-b (AVG art. 32 lid 1 sub b); AVG-art32-lid2 (AVG art. 32 lid 2)

### K11.2c — Apparaten en verbindingen zijn versleuteld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Basismaatregel (keuze van dit kader, geen wettelijke lijst): versleuteling van gegevensdragers en verbindingen; art. 32 lid 1 sub a noemt versleuteling en pseudonimisering expliciet
- Grondslag: art. 32 lid 1 sub a AVG
- Beoordeeld op: de antwoorden
- Nodig: encryption_devices, encryption_connections
- Beoordeling:
  - Deze maatregel komt uit een minimumset die in dit kader is gekozen; het is geen wettelijke lijst. Art. 32 lid 1 sub a noemt versleuteling wel uitdrukkelijk als voorbeeld.
  - present als encryption_devices én encryption_connections waar zijn; absent als een van beide onwaar is; anders bij ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Beslisregel bij absent: risk_level high, special_categories waar, of risk_level of special_categories 'weet ik niet' → non_compliant (❌). risk_level low of medium én special_categories onwaar → review (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het ontbreken van versleuteling bij dit risico een tekort dat direct hersteld moet worden?
- Advies bij ❌ of ⚠️: Versleutel laptops, telefoons en andere gegevensdragers, en gebruik alleen versleutelde verbindingen (https, beveiligde e-mail en VPN of vergelijkbaar voor thuiswerken).
- Bronnen: AVG-art32-lid1-a (AVG art. 32 lid 1 sub a); AVG-art32-lid2 (AVG art. 32 lid 2)

### K11.2d — Er zijn back-ups waarmee je gegevens kunt terugzetten
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Basismaatregel (keuze van dit kader, geen wettelijke lijst): back-ups en herstelmogelijkheid
- Grondslag: art. 32 lid 1 sub c AVG
- Beoordeeld op: de antwoorden
- Nodig: backups_restorable
- Beoordeling:
  - Deze maatregel komt uit een minimumset die in dit kader is gekozen; het is geen wettelijke lijst. Art. 32 lid 1 sub c noemt het tijdig herstellen van de beschikbaarheid wel uitdrukkelijk.
  - present als backups_restorable waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Beslisregel bij absent: risk_level high, special_categories waar, of risk_level of special_categories 'weet ik niet' → non_compliant (❌). risk_level low of medium én special_categories onwaar → review (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het ontbreken van herstelbare back-ups bij dit risico een tekort dat direct hersteld moet worden?
- Advies bij ❌ of ⚠️: Maak regelmatig back-ups, bewaar er een kopie van los van je systemen, en probeer af en toe of terugzetten lukt.
- Bronnen: AVG-art32-lid1-c (AVG art. 32 lid 1 sub c); AVG-art32-lid2 (AVG art. 32 lid 2)

### K11.2e — Er wordt bijgehouden wie gevoelige gegevens bekijkt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Basismaatregel (keuze van dit kader, geen wettelijke lijst): logging van toegang tot gevoelige gegevens
- Grondslag: art. 32 lid 1 sub b AVG (vertrouwelijkheid en integriteit)
- Beoordeeld op: de antwoorden
- Nodig: access_logging
- Beoordeling:
  - Deze maatregel komt uit een minimumset die in dit kader is gekozen; het is geen wettelijke lijst.
  - present als access_logging waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Beslisregel bij absent: risk_level high, special_categories waar, of risk_level of special_categories 'weet ik niet' → non_compliant (❌). risk_level low of medium én special_categories onwaar → review (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het ontbreken van logging bij dit risico een tekort dat direct hersteld moet worden?
- Advies bij ❌ of ⚠️: Zet logging aan in systemen met gevoelige gegevens, zodat je kunt zien wie welke gegevens heeft bekeken of gewijzigd, en controleer die logs regelmatig.
- Bronnen: AVG-art32-lid1-b (AVG art. 32 lid 1 sub b); AVG-art32-lid2 (AVG art. 32 lid 2); AP-boete-HagaZiekenhuis-2019 (Autoriteit Persoonsgegevens, boetebesluit HagaZiekenhuis (logging en toegang tot patiëntendossiers))

### K11.2f — Software wordt op tijd bijgewerkt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Basismaatregel (keuze van dit kader, geen wettelijke lijst): updates en patchbeleid
- Grondslag: art. 32 lid 1 sub b AVG (vertrouwelijkheid, integriteit, beschikbaarheid en veerkracht)
- Beoordeeld op: de antwoorden
- Nodig: patch_policy
- Beoordeling:
  - Deze maatregel komt uit een minimumset die in dit kader is gekozen; het is geen wettelijke lijst.
  - present als patch_policy waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Beslisregel bij absent: risk_level high, special_categories waar, of risk_level of special_categories 'weet ik niet' → non_compliant (❌). risk_level low of medium én special_categories onwaar → review (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het ontbreken van een updatebeleid bij dit risico een tekort dat direct hersteld moet worden?
- Advies bij ❌ of ⚠️: Zet automatische updates aan waar dat kan, en spreek af wie de overige updates controleert en op tijd installeert.
- Bronnen: AVG-art32-lid1-b (AVG art. 32 lid 1 sub b); AVG-art32-lid2 (AVG art. 32 lid 2)

### K11.2g — Medewerkers hebben geheimhouding en weten hoe ze veilig werken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Basismaatregel (keuze van dit kader, geen wettelijke lijst): geheimhouding, instructie en bewustzijn bij medewerkers
- Grondslag: art. 32 lid 4 AVG
- Beoordeeld op: de antwoorden
- Nodig: staff_confidentiality
- Beoordeling:
  - Deze maatregel komt uit een minimumset die in dit kader is gekozen; het is geen wettelijke lijst. Art. 32 lid 4 eist wel dat medewerkers gegevens alleen op instructie verwerken.
  - present als staff_confidentiality waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Beslisregel bij absent: risk_level high, special_categories waar, of risk_level of special_categories 'weet ik niet' → non_compliant (❌). risk_level low of medium én special_categories onwaar → review (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het ontbreken van geheimhouding en instructie bij dit risico een tekort dat direct hersteld moet worden?
- Advies bij ❌ of ⚠️: Neem een geheimhoudingsplicht op in arbeidscontracten, geef medewerkers duidelijke instructies over het werken met persoonsgegevens, en herhaal dat regelmatig.
- Bronnen: AVG-art32-lid4 (AVG art. 32 lid 4); AVG-art32-lid2 (AVG art. 32 lid 2)

### K11.3 — Je test en evalueert de maatregelen regelmatig
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Procedure voor het regelmatig testen, beoordelen en evalueren van de doeltreffendheid van de maatregelen
- Grondslag: art. 32 lid 1 sub d AVG
- Beoordeeld op: de antwoorden
- Nodig: measures_tested
- Beoordeling:
  - present als measures_tested waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Plan een vaste controle van je beveiliging, bijvoorbeeld een jaarlijkse evaluatie of test, en leg de uitkomsten en verbeterpunten vast.
- Bronnen: AVG-art32-lid1-d (AVG art. 32 lid 1 sub d)

### K11.4 — De maatregelen passen bij het risico
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Passen de maatregelen bij het risico? Bijzondere gegevens → strenger
- Grondslag: art. 32 lid 1 en 2 AVG
- Beoordeeld op: de antwoorden
- Nodig: risk_level, special_categories, data_description, security_description, access_need_to_know, strong_authentication, encryption_devices, encryption_connections, backups_restorable, access_logging, patch_policy, staff_confidentiality
- Beoordeling:
  - Bij bijzondere gegevens (special_categories waar) of risk_level high gelden strengere eisen.
  - Duidelijk non_compliant: special_categories waar of risk_level high, en twee of meer basismaatregelen (stap 2a-2g) ontbreken.
  - Duidelijk compliant: alle basismaatregelen aanwezig, risk_level low of medium en special_categories onwaar, en security_description of data_description wijst niet op een verhoogd risico.
  - Het enkele feit dat er een datalek is geweest, betekent niet dat de maatregelen onvoldoende waren (C-340/21); de organisatie moet wel kunnen aantonen dat ze passend waren.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de maatregelen samen passend voor dit risico, gezien de aard van de gegevens en de stand van de techniek? (Door een beveiligingsdeskundige te beoordelen.)
- Advies bij ❌ of ⚠️: Stem je maatregelen af op de gevoeligheid van de gegevens: hoe ernstiger de gevolgen voor mensen, hoe strenger de beveiliging. Leg vast waarom je je maatregelen passend vindt.
- Bronnen: AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art32-lid2 (AVG art. 32 lid 2); AVG-art9-lid1 (AVG art. 9 lid 1); HvJEU-C-340-21 (HvJEU 14 december 2023, C-340/21, Natsionalna agentsia za prihodite)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): data_description. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- De lijst in stap 2 (2a-2g) is een minimumset die in dit kader is gekozen, NIET een wettelijke lijst. Het rapport vermeldt dit bij elke basismaatregel.
- Ontbreken van een basismaatregel (2a-2g) → ⚠️ of ❌ afhankelijk van het risico uit stap 1: ❌ (non_compliant) bij risk_level high, bij bijzondere gegevens of als het risico onbekend is; ⚠️ (review) bij risk_level low of medium zonder bijzondere gegevens.
- Een datalek betekent niet automatisch dat de maatregelen onvoldoende waren; de bewijslast dat ze passend waren ligt bij de verantwoordelijke (C-340/21).

## Samenhang met andere kaders

- Kader CB1 (/toets-cyberbeveiligingswet) — als `facts.cbw_applies == true`: Je organisatie valt onder de Cyberbeveiligingswet; daarnaast gelden de zorgplicht en meldplicht uit die wet.

## Open punten en voorbehouden

- De basislijst van stap 2 is een eigen keuze van deze skill, geen wettelijke lijst; de keuze en de risicogrens voor ⚠️/❌ moeten door een deskundige worden bevestigd.
- Keuze bij de beslisregel van stap 2: een onbekend risico (risk_level of special_categories 'weet ik niet') wordt als hoog behandeld (voorzichtigste lezing). Te verifiëren.
