# Kader K0 — Toepasselijkheid AVG

Versie 1.3 · peildatum 2026-11-10

Doel: Vaststellen of de AVG geldt voor wat de organisatie met gegevens doet: gaat het om persoonsgegevens, is er een verwerking, valt die binnen het materiële en territoriale toepassingsgebied, en geldt er geen uitzondering.

Bronnen: AVG-art2-lid1 (AVG art. 2 lid 1); AVG-art2-lid2 (AVG art. 2 lid 2); AVG-art3 (AVG art. 3); AVG-art4-1 (AVG art. 4 punt 1); AVG-art4-2 (AVG art. 4 punt 2); AVG-art4-5 (AVG art. 4 punt 5); AVG-overw26 (AVG overweging 26); AVG-overw27 (AVG overweging 27); UAVG-art4 (UAVG art. 4); HvJEU-C-582-14 (HvJEU 19 oktober 2016, C-582/14, Breyer (dynamische IP-adressen)); HvJEU-C-434-16 (HvJEU 20 december 2017, C-434/16, Nowak (ruime uitleg persoonsgegeven)); HvJEU-C-212-13 (HvJEU 11 december 2014, C-212/13, Ryneš (huishoudelijke uitzondering; camera die openbare ruimte filmt)); HvJEU-C-413-23P (HvJEU 4 september 2025, C-413/23 P, EDPS/Gemeenschappelijke Afwikkelingsraad (SRB))

## Formulier (vragen aan de gebruiker)

- **data_description**: Welke gegevens gebruik je, over wie gaan ze, en wat doe je ermee?
  - Label (voor de plek-om-in-te-vullen): welke gegevens je gebruikt, over wie, en wat je ermee doet
  - Hulp: Bijvoorbeeld: 'naam, adres en bestelgeschiedenis van klanten, voor bezorging en facturen' of 'bedrijfsnaam en KvK-nummer van leveranciers'. Zoals je het aan een collega zou uitleggen.
  - Type: text
- **only_legal_entity_data**: Gaat het uitsluitend om gegevens over bedrijven of organisaties, zonder gegevens over personen?
  - Label (voor de plek-om-in-te-vullen): of het alleen om gegevens over bedrijven en organisaties gaat
  - Hulp: Antwoord alleen 'ja' als er geen namen, e-mailadressen, telefoonnummers of andere gegevens van contactpersonen of medewerkers in zitten. Let op: gegevens over een eenmanszaak of vof zijn vaak ook gegevens over de ondernemer zelf; kies dan 'nee'.
  - Type: boolean
- **only_deceased_persons**: Gaat het uitsluitend om gegevens over mensen die zijn overleden?
  - Label (voor de plek-om-in-te-vullen): of het alleen om gegevens over overleden personen gaat
  - Hulp: Bijvoorbeeld een archief of stamboom met alleen overleden personen. Zitten er ook gegevens van levende familieleden of nabestaanden in, kies dan 'nee'.
  - Type: boolean
- **identifiability**: Welke omschrijving past het best bij de gegevens?
  - Label (voor de plek-om-in-te-vullen): hoe goed de gegevens naar een persoon te herleiden zijn
  - Hulp: Kies de omschrijving die het dichtst bij de meest herleidbare gegevens komt die je gebruikt.
  - Type: enum (directly_identifiable / indirectly_identifiable / pseudonymised_with_key / pseudonymised_without_key / anonymous) · Alleen vragen als: `facts.only_legal_entity_data != true and facts.only_deceased_persons != true`
- **anonymisation_basis**: Waarom kan niemand de gegevens meer naar een persoon herleiden, ook niet door ze te combineren met andere informatie?
  - Label (voor de plek-om-in-te-vullen): waarom je de gegevens als anoniem beschouwt
  - Hulp: Beschrijf hoe de gegevens anoniem zijn gemaakt (bijvoorbeeld alleen totalen per maand) en of iemand met redelijke middelen personen kan terugvinden.
  - Type: text · Alleen vragen als: `facts.identifiability == "anonymous"`
- **performs_processing**: Doe je iets met deze gegevens, zoals verzamelen, opslaan, bekijken, doorsturen, aanpassen of wissen?
  - Label (voor de plek-om-in-te-vullen): of je iets met de gegevens doet
  - Hulp: Vrijwel elke handeling telt, ook alleen bewaren of inzien.
  - Type: boolean
- **processing_means**: Hoe houd je de gegevens bij?
  - Label (voor de plek-om-in-te-vullen): hoe je de gegevens bijhoudt
  - Type: enum (automated / structured_paper / unstructured_paper)
- **purely_personal_use**: Gebruik je de gegevens uitsluitend voor jezelf of je huishouden, helemaal los van een bedrijf of beroep?
  - Label (voor de plek-om-in-te-vullen): of je de gegevens alleen privé gebruikt
  - Hulp: Bijvoorbeeld een privé-adresboek. Zodra het (ook) voor je onderneming of beroep is, is het antwoord 'nee'.
  - Type: boolean
- **established_in_eu**: Heeft je organisatie een vestiging in de Europese Unie?
  - Label (voor de plek-om-in-te-vullen): of je organisatie een vestiging in de EU heeft
  - Hulp: Voor bijna alle Nederlandse organisaties is het antwoord ja.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **targets_people_in_eu**: Bied je producten of diensten aan mensen in de EU aan, of volg je hun gedrag (bijvoorbeeld via tracking of profilering)?
  - Label (voor de plek-om-in-te-vullen): of je je richt op mensen in de EU
  - Type: boolean · Alleen vragen als: `facts.established_in_eu == false`
- **has_eu_representative**: Heb je schriftelijk een vertegenwoordiger in de EU aangewezen?
  - Label (voor de plek-om-in-te-vullen): of je een vertegenwoordiger in de EU hebt aangewezen
  - Type: boolean · Alleen vragen als: `facts.established_in_eu == false and facts.targets_people_in_eu == true`

## Toetspunten

### K0.1 — Of het om gegevens over levende personen gaat
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Informatie over een geïdentificeerde of identificeerbare, levende natuurlijke persoon (persoonsgegeven)
- Grondslag: art. 4 lid 1 en lid 5 AVG; overwegingen 26 en 27 AVG
- Alleen als: `facts.only_legal_entity_data != true and facts.only_deceased_persons != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: data_description, identifiability
- Beoordeling:
  - Het begrip persoonsgegeven wordt ruim uitgelegd (C-434/16). Namen, zakelijke e-mailadressen en telefoonnummers van contactpersonen bij bedrijven zijn persoonsgegevens; gegevens over een eenmanszaak of vof kunnen persoonsgegevens van de ondernemer zijn.
  - Duidelijk compliant (persoonsgegevens vastgesteld): identifiability directly_identifiable of pseudonymised_with_key (gepseudonimiseerde gegevens blijven persoonsgegevens voor wie de sleutel heeft of redelijkerwijs kan heridentificeren, art. 4 lid 5).
  - identifiability indirectly_identifiable (IP-adressen, klantnummers, foto's, apparaat-ID's): meestal persoonsgegevens (C-582/14 voor dynamische IP-adressen); duidelijk geval voor compliant tenzij data_description aanwijst dat niemand met redelijke middelen de persoon kan achterhalen.
  - identifiability pseudonymised_without_key: mogelijk geen persoonsgegeven voor deze ontvanger als die geen redelijke middelen tot heridentificatie heeft (C-413/23 P); bijna altijd geen duidelijk geval.
  - identifiability anonymous: echt anoniem (overweging 26) betekent dat de AVG niet geldt, maar een claim van anonimiteit zonder overtuigende onderbouwing in anonymisation_basis geeft geen duidelijk geval. Anonimiteit wordt nooit door het model zelf vastgesteld: geen duidelijk geval.
  - Gegevens over overleden personen vallen niet onder de AVG (overweging 27; Nederland heeft de AVG niet tot overledenen uitgebreid). Blijkt uit data_description dat het uitsluitend om overledenen gaat terwijl only_deceased_persons niet ja is: geen duidelijk geval.
  - Blijkt uit data_description dat er geen enkel gegeven over een natuurlijke persoon in zit: uitkomst not_applicable, nooit non_compliant.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): n.v.t.
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de gegevens voor deze organisatie met redelijke middelen herleidbaar tot een levende persoon, of is de claim van anonimiteit of pseudonimisering zonder sleutel voldoende onderbouwd?
- Advies bij ❌ of ⚠️: Ga ervan uit dat de AVG geldt zodra gegevens iets zeggen over een persoon die jij (of een ander) met redelijke middelen kunt herkennen. Beschouw je gegevens als anoniem of gepseudonimiseerd zonder sleutel, leg dan vast waarom niemand ze meer kan herleiden.
- Bronnen: AVG-art4-1 (AVG art. 4 punt 1); AVG-art4-5 (AVG art. 4 punt 5); AVG-overw26 (AVG overweging 26); AVG-overw27 (AVG overweging 27); HvJEU-C-582-14 (HvJEU 19 oktober 2016, C-582/14, Breyer (dynamische IP-adressen)); HvJEU-C-434-16 (HvJEU 20 december 2017, C-434/16, Nowak (ruime uitleg persoonsgegeven)); HvJEU-C-413-23P (HvJEU 4 september 2025, C-413/23 P, EDPS/Gemeenschappelijke Afwikkelingsraad (SRB))

### K0.2 — Of je iets met de gegevens doet
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Er is een verwerking: elke handeling, van verzamelen en raadplegen tot wissen en vernietigen
- Grondslag: art. 4 lid 2 AVG
- Alleen als: `facts.only_legal_entity_data != true and facts.only_deceased_persons != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: performs_processing
- Beoordeling:
  - present als performs_processing waar is. Elke handeling telt, ook alleen opslaan, raadplegen of wissen.
  - absent als performs_processing onwaar is; uitkomst dan not_applicable (geen verwerking = AVG geldt niet), nooit non_compliant.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): n.v.t.
- Advies bij ❌ of ⚠️: Ook alleen bewaren, inzien of doorsturen van gegevens is een verwerking. Behandel het daarom als een verwerking die onder de AVG valt.
- Bronnen: AVG-art4-2 (AVG art. 4 punt 2)

### K0.3 — Of je de gegevens digitaal of in een geordend bestand bijhoudt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geheel of gedeeltelijk geautomatiseerde verwerking, of niet-geautomatiseerde verwerking van gegevens die in een bestand zijn opgenomen of daarvoor bestemd zijn
- Grondslag: art. 2 lid 1 AVG
- Alleen als: `facts.only_legal_entity_data != true and facts.only_deceased_persons != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: processing_means
- Beoordeling:
  - present als processing_means automated of structured_paper is.
  - absent als processing_means unstructured_paper is; uitkomst dan not_applicable, nooit non_compliant.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): n.v.t.
- Advies bij ❌ of ⚠️: Digitale gegevens en papieren gegevens die je op een geordende manier bijhoudt (bijvoorbeeld dossiers op naam) vallen onder de AVG.
- Bronnen: AVG-art2-lid1 (AVG art. 2 lid 1)

### K0.4 — Of een wettelijke uitzondering geldt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen uitzondering van art. 2 lid 2 AVG; voor bedrijven is alleen de huishoudelijke uitzondering (sub c) denkbaar, en die geldt nooit voor een onderneming of beroepsactiviteit
- Grondslag: art. 2 lid 2 AVG
- Alleen als: `facts.only_legal_entity_data != true and facts.only_deceased_persons != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: purely_personal_use
- Beoordeling:
  - present (geen uitzondering) als purely_personal_use onwaar is.
  - present ook als purely_personal_use waar is maar data_description laat zien dat de verwerking (mede) voor een onderneming of beroep is: de huishoudelijke uitzondering geldt daar nooit.
  - De huishoudelijke uitzondering wordt strikt uitgelegd: een camera die (deels) de openbare ruimte filmt, valt er niet onder (C-212/13).
  - Opsporing en vervolging (sub d) valt onder de Wpg/Wjsg, niet onder de AVG; voor bedrijven niet van toepassing.
  - absent (uitzondering geldt) alleen als purely_personal_use waar is en niets in data_description wijst op een onderneming of beroep; uitkomst dan not_applicable.
- Is het vereiste afwezig (*absent*): n.v.t.
- Advies bij ❌ of ⚠️: Gebruik je gegevens voor je bedrijf of beroep, dan geldt de uitzondering voor privégebruik niet en val je onder de AVG.
- Bronnen: AVG-art2-lid2 (AVG art. 2 lid 2); HvJEU-C-212-13 (HvJEU 11 december 2014, C-212/13, Ryneš (huishoudelijke uitzondering; camera die openbare ruimte filmt))

### K0.5 — Of de AVG geldt op grond van waar je gevestigd bent of op wie je je richt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Territoriale werking: vestiging in de EU (art. 3 lid 1), of aanbieden van goederen of diensten aan / gedrag monitoren van personen in de EU (art. 3 lid 2); bij lid 2 zonder EU-vestiging een vertegenwoordiger (art. 27)
- Grondslag: art. 3 en art. 27 AVG; art. 4 UAVG
- Alleen als: `facts.only_legal_entity_data != true and facts.only_deceased_persons != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: established_in_eu
- Beoordeling:
  - present als established_in_eu waar is (art. 3 lid 1). Of daarnaast de UAVG geldt, volgt uit art. 4 UAVG.
  - present als established_in_eu onwaar is, targets_people_in_eu waar is en has_eu_representative waar is (art. 3 lid 2 en art. 27).
  - established_in_eu onwaar, targets_people_in_eu waar en has_eu_representative onwaar of onbekend: twijfel (⚠️). De AVG geldt, en de plicht om een vertegenwoordiger aan te wijzen (art. 27) wordt gesignaleerd; of de uitzondering van art. 27 lid 2 geldt, beoordeelt een juridisch adviseur.
  - absent als established_in_eu onwaar en targets_people_in_eu onwaar is; uitkomst dan not_applicable.
  - targets_people_in_eu onbekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): n.v.t.
- Bij ⚠️ stel je de gebruiker deze vraag: Geldt de AVG via art. 3 lid 2, en valt de organisatie onder de uitzondering van art. 27 lid 2, of moet zij een vertegenwoordiger aanwijzen?
- Advies bij ❌ of ⚠️: Is je organisatie buiten de EU gevestigd en richt je je op mensen in de EU, dan geldt de AVG en moet je in de regel schriftelijk een vertegenwoordiger in de EU aanwijzen.
- Bronnen: AVG-art3-lid1 (AVG art. 3 lid 1); AVG-art3-lid2 (AVG art. 3 lid 2); AVG-art27 (AVG art. 27); UAVG-art4 (UAVG art. 4)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): data_description, purely_personal_use, established_in_eu. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Alle stappen compliant en geen uitzondering → AVG van toepassing; door naar K1. Is dit kader n.v.t., dan is K1 dat ook (in de rekenhulp: 'Vervalt als kader K0 n.v.t. is' bij K1).
- Stap 1, 2, 3 of 5 not_applicable, of stap 4 uitzondering → AVG niet van toepassing; kader not_applicable. Geen persoonsgegevens → n.v.t., nooit non_compliant.
- Stap 1 onzeker → review, maar door met de overige kaders 'onder voorbehoud'.
- Dit kader geeft nooit non_compliant: het stelt vast óf de AVG geldt, niet of de klant haar naleeft.

## Samenhang met andere kaders

- Kader K1 (/toets-toepasselijkheid-rol) — als `facts.only_legal_entity_data != true and facts.only_deceased_persons != true`: Als de AVG geldt, is de volgende vraag welke rol je organisatie heeft.
