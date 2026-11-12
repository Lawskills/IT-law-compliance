# Kader K1 — Rolbepaling

Versie 1.3 · peildatum 2026-11-10

Doel: Vaststellen of de klant bij een bepaalde samenwerking verwerkingsverantwoordelijke, verwerker of gezamenlijk verwerkingsverantwoordelijke is, op basis van de feiten en niet op basis van de benaming in het contract.

Geldt alleen als: `facts.only_legal_entity_data != true and facts.only_deceased_persons != true` — geen gegevens over levende personen, dan geldt de AVG niet en is er geen rol te bepalen (regel van kader K0)

Vervalt als kader K0 n.v.t. is (de AVG geldt niet).

Bronnen: AVG-art4-7 (AVG art. 4 punt 7); AVG-art4-8 (AVG art. 4 punt 8); AVG-art26 (AVG art. 26); AVG-art28-lid10 (AVG art. 28 lid 10); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG); HvJEU-C-210-16 (HvJEU, C-210/16, Wirtschaftsakademie Schleswig-Holstein (Facebook-fanpagina)); HvJEU-C-25-17 (HvJEU, C-25/17, Jehovan todistajat); HvJEU-C-40-17 (HvJEU, C-40/17, Fashion ID); HvJEU-C-683-21 (HvJEU, C-683/21, Nacionalinis visuomenės sveikatos centras)

## Formulier (vragen aan de gebruiker)

- **party_description**: Om welke andere partij gaat het, en wat doet die partij met de gegevens?
  - Label (voor de plek-om-in-te-vullen): de andere partij en wat die met de gegevens doet
  - Hulp: Bijvoorbeeld: 'ons boekhoudpakket in de cloud, waarin wij facturen en klantgegevens bijhouden' of 'een partnerbedrijf waarmee wij samen een actie organiseren'.
  - Type: text
- **data_flow**: Welke omschrijving past het best bij de samenwerking?
  - Label (voor de plek-om-in-te-vullen): hoe de gegevens tussen jou en de andere partij lopen
  - Type: enum (party_processes_for_us / we_process_for_party / shared_or_exchanged)
- **who_determines_purpose**: Wie bepaalt waarvoor de gegevens worden gebruikt?
  - Label (voor de plek-om-in-te-vullen): wie bepaalt waarvoor de gegevens worden gebruikt
  - Hulp: Het gaat om het waarom: met welk doel worden de gegevens verzameld en gebruikt?
  - Type: enum (client / other_party / jointly / each_separately)
- **who_determines_essential_means**: Wie bepaalt welke gegevens worden gebruikt, hoe lang ze worden bewaard, wie er toegang toe heeft en over welke mensen het gaat?
  - Label (voor de plek-om-in-te-vullen): wie bepaalt welke gegevens, hoe lang, wie toegang heeft en over welke mensen
  - Hulp: Welke software of beveiligingstechniek wordt gebruikt, telt hier niet mee. Dat mag een dienstverlener zelf kiezen.
  - Type: enum (client / other_party / jointly / each_separately)
- **processing_party_own_purposes**: Gebruikt de partij die als dienstverlener werkt (de andere partij, of jij zelf) de gegevens ook voor eigen doelen, of doet zij er meer mee dan is afgesproken?
  - Label (voor de plek-om-in-te-vullen): of de dienstverlener de gegevens ook voor eigen doelen gebruikt
  - Hulp: Bijvoorbeeld een softwareleverancier die klantgegevens ook gebruikt voor eigen marketing, eigen analyses of om eigen producten te verbeteren.
  - Type: boolean · Alleen vragen als: `facts.data_flow != "shared_or_exchanged"`
- **party_statutory_role**: Heeft de andere partij voor deze gegevens een eigen wettelijke taak of beroepsplicht?
  - Label (voor de plek-om-in-te-vullen): of de andere partij een eigen wettelijke taak of beroepsplicht heeft
  - Hulp: Bijvoorbeeld een accountant met een wettelijke controletaak, een bank of een arbodienst.
  - Type: boolean
- **contract_role_label**: Welke rollen staan in het contract met de andere partij?
  - Label (voor de plek-om-in-te-vullen): welke rollen het contract noemt
  - Type: enum (client_controller_party_processor / client_processor_party_controller / joint_controllers / independent_controllers / no_role_in_contract)

## Toetspunten

### K1.1 — Wie bepaalt waarvoor de gegevens worden gebruikt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Wie het doel van de verwerking bepaalt, is (mede)verantwoordelijke
- Grondslag: art. 4 lid 7 AVG
- Beoordeeld op: de antwoorden
- Nodig: party_description, who_determines_purpose
- Beoordeling:
  - De partij die het doel ('waarom') bepaalt, is (mede)verantwoordelijke. Wie een toepassing laat ontwikkelen of een dienst laat uitvoeren voor eigen doelen, kan verantwoordelijke zijn (C-683/21).
  - Duidelijk compliant: who_determines_purpose is client, other_party of each_separately en party_description sluit daarop aan.
  - who_determines_purpose jointly: duidelijk geval voor compliant als party_description een gezamenlijk doel beschrijft; zie stap 5.
  - party_description spreekt het antwoord tegen (bijvoorbeeld 'wij' terwijl de beschrijving laat zien dat de andere partij zelf beslist waarvoor de gegevens dienen): geen duidelijk geval.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Wie bepaalt feitelijk het doel van deze verwerking, en klopt dat met wat de klant aangeeft?
- Advies bij ❌ of ⚠️: Leg per samenwerking vast wie bepaalt waarvoor de gegevens worden gebruikt. Die partij is verantwoordelijk voor de verwerking.
- Bronnen: AVG-art4-7 (AVG art. 4 punt 7); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG); HvJEU-C-683-21 (HvJEU, C-683/21, Nacionalinis visuomenės sveikatos centras)

### K1.2 — Wie bepaalt hoe de gegevens worden gebruikt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Wie de wezenlijke middelen bepaalt (welke gegevens, hoe lang, wie toegang, welke betrokkenen); niet-wezenlijke, technische middelen mogen bij een verwerker liggen
- Grondslag: art. 4 lid 7 en lid 8 AVG
- Beoordeeld op: de antwoorden
- Nodig: who_determines_purpose, who_determines_essential_means
- Beoordeling:
  - Wezenlijke middelen: welke gegevens, hoe lang, wie toegang heeft, over welke betrokkenen. Niet-wezenlijke middelen (keuze van software, beveiligingsdetails) mogen bij een verwerker liggen zonder dat die verantwoordelijke wordt.
  - Duidelijk compliant: who_determines_essential_means is gelijk aan who_determines_purpose.
  - Doel door de ene partij, wezenlijke middelen door de andere: geen duidelijk geval (mogelijk zelfstandige of gezamenlijke verantwoordelijkheid van de andere partij).
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Bepaalt de dienstverlener alleen technische middelen, of beslist hij ook over welke gegevens, bewaartermijnen, toegang of betrokkenen?
- Advies bij ❌ of ⚠️: Leg vast wie beslist welke gegevens worden gebruikt, hoe lang ze worden bewaard en wie er toegang toe heeft. Laat een dienstverlener alleen de technische uitvoering kiezen als je hem als verwerker wilt inzetten.
- Bronnen: AVG-art4-7 (AVG art. 4 punt 7); AVG-art4-8 (AVG art. 4 punt 8); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)

### K1.3 — Of de dienstverlener de gegevens ook voor eigen doelen gebruikt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Een partij die gegevens voor eigen doelen gebruikt of buiten de instructies gaat, is voor dat deel verantwoordelijke, geen verwerker
- Grondslag: art. 28 lid 10 AVG
- Alleen als: `facts.data_flow != "shared_or_exchanged"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: processing_party_own_purposes
- Beoordeling:
  - present als processing_party_own_purposes onwaar is.
  - absent als processing_party_own_purposes waar is: de dienstverlener is voor dat deel verantwoordelijke (art. 28 lid 10) → review met uitleg dat de feiten beslissen, niet de benaming.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Voor welk deel van de verwerking is de dienstverlener zelf verantwoordelijk, en is dat geregeld?
- Advies bij ❌ of ⚠️: Spreek af dat een dienstverlener de gegevens alleen voor jouw doelen gebruikt. Gebruikt hij ze ook voor eigen doelen, dan is hij voor dat deel zelf verantwoordelijk en moet dat apart geregeld worden.
- Bronnen: AVG-art28-lid10 (AVG art. 28 lid 10); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)

### K1.4 — Of de andere partij een eigen wettelijke taak of beroepsplicht heeft
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Een partij met een eigen wettelijke taak of beroepsplicht die de verwerking bepaalt, is meestal zelfstandig verantwoordelijke
- Grondslag: art. 4 lid 7 AVG
- Beoordeeld op: de antwoorden
- Nodig: party_statutory_role, contract_role_label
- Beoordeling:
  - Duidelijk compliant: party_statutory_role onwaar.
  - Duidelijk compliant: party_statutory_role waar en contract_role_label independent_controllers.
  - party_statutory_role waar en de andere partij wordt als verwerker behandeld (contract_role_label client_controller_party_processor, of data_flow party_processes_for_us): geen duidelijk geval; meestal is zo'n partij (accountant met wettelijke controletaak, bank, arbodienst) zelfstandig verantwoordelijke.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Bepaalt de wettelijke taak of beroepsplicht van de andere partij de verwerking, zodat zij zelfstandig verantwoordelijke is?
- Advies bij ❌ of ⚠️: Een partij met een eigen wettelijke taak of beroepsplicht, zoals een accountant bij de wettelijke controle, een bank of een arbodienst, is meestal zelf verantwoordelijk. Een verwerkersovereenkomst past dan meestal niet.
- Bronnen: AVG-art4-7 (AVG art. 4 punt 7); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)

### K1.5 — Of je samen met de andere partij verantwoordelijk bent
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Twee partijen bepalen per verwerkingshandeling samen doel en middelen → gezamenlijke verantwoordelijkheid → K18
- Grondslag: art. 26 AVG
- Alleen als: `facts.who_determines_purpose == "jointly" or facts.who_determines_essential_means == "jointly" or facts.who_determines_purpose == null or facts.who_determines_essential_means == null` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: party_description, who_determines_purpose, who_determines_essential_means
- Beoordeling:
  - Gezamenlijke verantwoordelijkheid geldt alleen voor de verwerkingshandelingen waarvan doel en middelen samen worden bepaald (C-40/17), en vereist niet dat beide partijen toegang tot de gegevens hebben (C-25/17).
  - Een beheerder van een pagina op een platform kan samen met het platform verantwoordelijk zijn (C-210/16).
  - Gezamenlijke verantwoordelijkheid ontstaat door de feiten, ook zonder regeling (C-683/21); de regeling zelf toetst K18.
  - Deze stap signaleert en verwijst: uitkomst hooguit review.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Voor welke verwerkingshandelingen bepalen de partijen samen doel en middelen, en is daarvoor een regeling (art. 26) nodig?
- Advies bij ❌ of ⚠️: Je bepaalt samen met de andere partij waarvoor en hoe gegevens worden gebruikt. Leg in een regeling vast wie wat doet, vooral wie vragen en verzoeken van mensen afhandelt.
- Bronnen: AVG-art26 (AVG art. 26); HvJEU-C-210-16 (HvJEU, C-210/16, Wirtschaftsakademie Schleswig-Holstein (Facebook-fanpagina)); HvJEU-C-25-17 (HvJEU, C-25/17, Jehovan todistajat); HvJEU-C-40-17 (HvJEU, C-40/17, Fashion ID); HvJEU-C-683-21 (HvJEU, C-683/21, Nacionalinis visuomenės sveikatos centras)

### K1.6 — Of de rollen in het contract kloppen met wat er werkelijk gebeurt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Wie betaalt of wie het contract opstelt is niet doorslaggevend; de feitelijke rol gaat boven de benaming in het contract
- Grondslag: art. 4 lid 7 en lid 8 en art. 28 lid 10 AVG
- Beoordeeld op: de antwoorden
- Nodig: contract_role_label, who_determines_purpose, data_flow
- Beoordeling:
  - present als de benaming in het contract past bij de feiten: client_controller_party_processor bij data_flow party_processes_for_us, who_determines_purpose client en geen eigen doelen van de dienstverlener; client_processor_party_controller bij data_flow we_process_for_party, who_determines_purpose other_party en geen eigen doelen; joint_controllers bij who_determines_purpose jointly; independent_controllers bij who_determines_purpose each_separately.
  - no_role_in_contract: de feiten beslissen; present als de feiten uit stap 1-3 eenduidig zijn, anders twijfel (⚠️).
  - absent als de benaming niet past bij de feiten, bijvoorbeeld een partij die 'verwerker' heet maar eigen doelen heeft (processing_party_own_purposes waar) of zelf het doel bepaalt → review met uitleg dat de feiten beslissen.
  - Wie betaalt of wie het contract heeft opgesteld, telt niet mee.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Welke rol heeft elke partij feitelijk, en moet het contract daarop worden aangepast?
- Advies bij ❌ of ⚠️: Pas de rollen in het contract aan zodat ze kloppen met wat er werkelijk gebeurt. Niet de benaming, maar de feiten bepalen wie verantwoordelijk is.
- Bronnen: AVG-art4-7 (AVG art. 4 punt 7); AVG-art4-8 (AVG art. 4 punt 8); AVG-art28-lid10 (AVG art. 28 lid 10); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): party_description. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Rol duidelijk → vastleggen en door: verwerker → K7 (klant is verantwoordelijke) of K7b (klant is verwerker); gezamenlijk → K18.
- Tegenstrijdige feiten of een partij met een gemengde rol → review.
- Contract noemt een partij 'verwerker' terwijl zij eigen doelen heeft → review met uitleg dat de feiten beslissen.

## Samenhang met andere kaders

- Kader K7 (/verwerkersovereenkomst) — als `facts.data_flow == "party_processes_for_us"`: Werkt de andere partij in je opdracht als verwerker, dan is een verwerkersovereenkomst nodig.
- Kader K7b (/verwerkersovereenkomst) — als `facts.data_flow == "we_process_for_party"`: Werk je zelf in opdracht van de andere partij, dan toets je de verwerkersovereenkomst vanuit de verwerker.
- Kader K18 (/samenwerkingsafspraken) — als `facts.who_determines_purpose == "jointly" or facts.who_determines_essential_means == "jointly"`: Bij gezamenlijke verantwoordelijkheid is een eigen regeling verplicht.
