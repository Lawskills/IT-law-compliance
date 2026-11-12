# Kader K3 — Bijzondere persoonsgegevens, strafrechtelijke gegevens en BSN

Versie 1.2 · peildatum 2026-11-10

Doel: Toetsen of de extra zware regels voor bijzondere persoonsgegevens (art. 9 AVG en art. 22 t/m 30 UAVG), strafrechtelijke gegevens (art. 10 AVG en art. 31 t/m 33 UAVG) en het burgerservicenummer (art. 87 AVG en art. 46 UAVG) worden nageleefd.

Bronnen: AVG-art9 (AVG art. 9); AVG-art10 (AVG art. 10); AVG-art87 (AVG art. 87); UAVG-art22 (UAVG art. 22); UAVG-art29 (UAVG art. 29); UAVG-art30-lid1 (UAVG art. 30 lid 1); UAVG-art32 (UAVG art. 32); UAVG-art33 (UAVG art. 33); UAVG-art46 (UAVG art. 46); Wabb (Wet algemene bepalingen burgerservicenummer); HvJEU-C-184-20 (HvJEU 1 augustus 2022, C-184/20, OT/Vyriausioji tarnybinės etikos komisija); HvJEU-C-21-23 (HvJEU 4 oktober 2024, C-21/23, Lindenapotheke); AP-boete-vingerafdrukken-2020 (Autoriteit Persoonsgegevens, boete van € 725.000 voor het gebruik van vingerafdrukscanners bij personeel (2020))

## Formulier (vragen aan de gebruiker)

- **data_description**: Welke gegevens over mensen gebruik je, en waarvoor? Beschrijf het in gewone woorden.
  - Label (voor de plek-om-in-te-vullen): welke gegevens je over mensen gebruikt en waarvoor
  - Hulp: Denk ook aan gegevens waaruit iets gevoeligs kan worden afgeleid, zoals een dieetwens, een pasfoto, een ziekmelding of een bestelling van medicijnen.
  - Type: text
- **processes_health_data**: Gebruik je gegevens over de gezondheid van mensen?
  - Label (voor de plek-om-in-te-vullen): of je gegevens over gezondheid gebruikt
  - Hulp: Bijvoorbeeld ziekmeldingen, allergieën, een beperking, zwangerschap, of bestellingen van geneesmiddelen die alleen bij een apotheek verkrijgbaar zijn.
  - Type: boolean
- **processes_biometric_data**: Gebruik je vingerafdrukken, gezichtsherkenning of andere lichaamskenmerken om mensen te herkennen?
  - Label (voor de plek-om-in-te-vullen): of je biometrische gegevens gebruikt om mensen te herkennen
  - Hulp: Bijvoorbeeld een vingerafdrukscanner voor de tijdregistratie of voor een deur. Een gewone foto op een personeelspas telt hier niet mee zolang die niet wordt gebruikt om mensen automatisch te herkennen.
  - Type: boolean
- **processes_other_special_data**: Gebruik je gegevens over ras of etnische afkomst, politieke opvattingen, religie of levensovertuiging, vakbondslidmaatschap, erfelijke (genetische) eigenschappen, of seksueel gedrag of seksuele gerichtheid?
  - Label (voor de plek-om-in-te-vullen): of je andere gevoelige gegevens gebruikt
  - Hulp: Ook als je dit niet direct vraagt, maar het wel uit andere gegevens blijkt. Een dieetwens kan bijvoorbeeld iets zeggen over iemands geloof.
  - Type: boolean
- **processes_criminal_data**: Gebruik je gegevens over strafbare feiten of veroordelingen van mensen, of over een verdenking daarvan?
  - Label (voor de plek-om-in-te-vullen): of je gegevens over strafbare feiten gebruikt
  - Hulp: Bijvoorbeeld een registratie van winkeldieven, een zwarte lijst van fraudeurs, of gegevens over een strafblad van een sollicitant of werknemer.
  - Type: boolean
- **processes_bsn**: Gebruik of bewaar je burgerservicenummers (BSN), ook op kopieën van paspoorten of identiteitskaarten?
  - Label (voor de plek-om-in-te-vullen): of je burgerservicenummers gebruikt
  - Type: boolean
- **special_data_exception**: Op welke grond gebruik je de gevoelige gegevens (gezondheid, biometrie of de andere categorieën)?
  - Label (voor de plek-om-in-te-vullen): de wettelijke uitzondering waarop je je beroept voor gevoelige gegevens
  - Hulp: Voor deze gegevens geldt een verbod, tenzij een wettelijke uitzondering van toepassing is.
  - Type: enum (explicit_consent / employment_obligation / biometric_security / made_public_by_person / other / none) · Alleen vragen als: `facts.processes_health_data != false or facts.processes_biometric_data != false or facts.processes_other_special_data != false`
- **special_data_exception_explanation**: Licht kort toe waarom je deze gegevens nodig hebt en waarom de gekozen reden van toepassing is.
  - Label (voor de plek-om-in-te-vullen): je toelichting op de uitzondering
  - Type: text · Alleen vragen als: `facts.processes_health_data != false or facts.processes_biometric_data != false or facts.processes_other_special_data != false`
- **consent_from_employees**: Vraag je deze toestemming (ook) aan je eigen werknemers?
  - Label (voor de plek-om-in-te-vullen): of de toestemming van je eigen werknemers komt
  - Hulp: In een arbeidsrelatie is toestemming zelden echt vrij, omdat een werknemer afhankelijk is van de werkgever.
  - Type: boolean · Alleen vragen als: `facts.special_data_exception == "explicit_consent"`
- **biometric_purpose**: Waarvoor gebruik je de vingerafdruk, gezichtsherkenning of het andere lichaamskenmerk?
  - Label (voor de plek-om-in-te-vullen): waarvoor je biometrie gebruikt
  - Type: enum (security_necessary / time_or_convenience / other) · Alleen vragen als: `facts.processes_biometric_data != false`
- **bsn_use_basis**: Waarom gebruik je het BSN?
  - Label (voor de plek-om-in-te-vullen): waarom je het BSN gebruikt
  - Type: enum (payroll / healthcare / other_law / no_law) · Alleen vragen als: `facts.processes_bsn == true`
- **bsn_law_name**: Welke wet schrijft je voor het BSN te gebruiken?
  - Label (voor de plek-om-in-te-vullen): de wet die het BSN-gebruik voorschrijft
  - Type: text · Alleen vragen als: `facts.bsn_use_basis == "other_law"`
- **bsn_only_for_legal_purpose**: Gebruik je het BSN alleen voor dat wettelijke doel, en niet ook voor andere dingen (zoals een klant- of personeelsnummer)?
  - Label (voor de plek-om-in-te-vullen): of je het BSN alleen gebruikt voor het doel dat de wet noemt
  - Type: boolean · Alleen vragen als: `facts.processes_bsn == true`
- **id_copy_bsn_visible**: Bewaar je kopieën van paspoorten of identiteitskaarten waarop het BSN zichtbaar is?
  - Label (voor de plek-om-in-te-vullen): of je kopieën van identiteitsbewijzen bewaart waarop het BSN zichtbaar is
  - Hulp: Kies je 'nee' als je geen kopieën bewaart, of als het BSN op de kopie is afgeschermd.
  - Type: boolean · Alleen vragen als: `facts.processes_bsn == true`
- **criminal_data_basis**: Op welke grond gebruik je de gegevens over strafbare feiten?
  - Label (voor de plek-om-in-te-vullen): de wettelijke grond voor het gebruik van strafrechtelijke gegevens
  - Type: enum (explicit_consent / made_public_by_person / legal_claim / assessing_request / protection_against_offences / other / none) · Alleen vragen als: `facts.processes_criminal_data == true`
- **criminal_data_about_employees**: Gaat het (ook) om gegevens over je eigen werknemers?
  - Label (voor de plek-om-in-te-vullen): of het gaat om strafrechtelijke gegevens over je eigen personeel
  - Type: boolean · Alleen vragen als: `facts.processes_criminal_data == true`
- **works_council_rules**: Heb je regels voor het gebruik van deze gegevens over werknemers vastgesteld volgens de procedure met de ondernemingsraad?
  - Label (voor de plek-om-in-te-vullen): of er met de ondernemingsraad vastgestelde regels zijn
  - Hulp: Het gaat om regels die de ondernemingsraad heeft goedgekeurd of waarover die heeft meegepraat zoals de Wet op de ondernemingsraden voorschrijft.
  - Type: boolean · Alleen vragen als: `facts.criminal_data_about_employees == true`
- **extra_safeguards**: Heb je voor deze gevoelige gegevens extra maatregelen genomen, zoals beperkte toegang, vastleggen wie de gegevens inziet en versleuteling?
  - Label (voor de plek-om-in-te-vullen): of je extra beveiliging hebt voor deze gegevens
  - Type: boolean
- **large_scale**: Gebruik je deze gevoelige gegevens op grote schaal, bijvoorbeeld van heel veel mensen of als kern van je dienstverlening?
  - Label (voor de plek-om-in-te-vullen): of het om veel mensen of veel gegevens gaat
  - Type: boolean

## Toetspunten

### K3.1 — Welke gevoelige gegevens je gebruikt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Welke bijzondere categorie, strafrechtelijk gegeven of het BSN wordt verwerkt; ruime uitleg: ook gegevens waaruit een bijzonder gegeven kan worden afgeleid
- Grondslag: art. 9 lid 1, art. 10 en art. 87 AVG; art. 46 UAVG
- Beoordeeld op: de antwoorden
- Nodig: data_description, processes_health_data, processes_biometric_data, processes_other_special_data, processes_criminal_data, processes_bsn
- Beoordeling:
  - Deze stap stelt vast welke categorieën worden verwerkt; hij levert nooit non_compliant op.
  - Uitleg ruim: ook gegevens waaruit een bijzonder gegeven kan worden afgeleid tellen mee (C-184/20), zoals een dieetwens die op religie wijst of een online bestelling van een apotheekplichtig geneesmiddel, ook zonder recept (C-21/23).
  - Duidelijk compliant: alle categorievragen zijn met ja of nee beantwoord en data_description bevat niets waaruit een niet-aangevinkte categorie kan worden afgeleid.
  - geen duidelijk geval als een categorievraag met 'weet ik niet' is beantwoord, of als data_description gegevens noemt waaruit een categorie kan worden afgeleid die met nee is beantwoord. Noem die categorie in de toelichting.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Worden er gegevens verwerkt waaruit een bijzondere categorie kan worden afgeleid die de klant niet heeft aangegeven?
- Advies bij ❌ of ⚠️: Loop na welke gegevens je gebruikt en of daaruit iets over gezondheid, geloof, afkomst of andere gevoelige kenmerken kan worden afgeleid. Voor die gegevens gelden extra regels.
- Bronnen: AVG-art9-lid1 (AVG art. 9 lid 1); AVG-art10 (AVG art. 10); AVG-art87 (AVG art. 87); UAVG-art46 (UAVG art. 46); HvJEU-C-184-20 (HvJEU 1 augustus 2022, C-184/20, OT/Vyriausioji tarnybinės etikos komisija); HvJEU-C-21-23 (HvJEU 4 oktober 2024, C-21/23, Lindenapotheke)

### K3.2 — Of je een wettelijke uitzondering hebt voor gevoelige gegevens
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Naast een grondslag uit art. 6 (K2) een uitzondering uit art. 9 lid 2 AVG of art. 22 t/m 30 UAVG
- Grondslag: art. 9 lid 2 AVG; art. 22 t/m 30 UAVG
- Alleen als: `facts.processes_health_data != false or facts.processes_biometric_data != false or facts.processes_other_special_data != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: special_data_exception, special_data_exception_explanation, consent_from_employees, biometric_purpose
- Beoordeling:
  - absent als special_data_exception none is: zonder uitzondering geldt het verbod van art. 9 lid 1.
  - absent als processes_biometric_data waar is en biometric_purpose time_or_convenience is: biometrie voor unieke identificatie is alleen toegestaan als dit noodzakelijk is voor authenticatie of beveiliging (art. 29 UAVG); vingerafdruk voor tijdregistratie of een kantoordeur zonder bijzonder beveiligingsbelang is een duidelijk geval (AP-boete 2020).
  - present als special_data_exception explicit_consent is en consent_from_employees onwaar is.
  - twijfel (⚠️) als special_data_exception explicit_consent is en consent_from_employees waar is: in een werkgeversrelatie is toestemming zelden vrij.
  - present als special_data_exception employment_obligation is en het gaat om gezondheidsgegevens van werknemers (art. 9 lid 2 sub b AVG, art. 30 lid 1 UAVG); de uitwerking wordt getoetst in K15. Bij andere categorieën dan gezondheid: twijfel (⚠️).
  - Bij biometric_security of biometric_purpose security_necessary: present alleen als special_data_exception_explanation een concreet beveiligingsbelang noemt waarvoor biometrie noodzakelijk is; anders twijfel (⚠️).
  - twijfel (⚠️) als special_data_exception made_public_by_person is: deze uitzondering wordt strikt uitgelegd, bij twijfel review.
  - twijfel (⚠️) als special_data_exception other is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de genoemde uitzondering in deze situatie werkelijk van toepassing (vrije toestemming, noodzaak van biometrie, kennelijk openbaar gemaakt)?
- Advies bij ❌ of ⚠️: Stel vast op welke wettelijke uitzondering je je beroept voor deze gevoelige gegevens. Is er geen uitzondering, stop dan met het gebruik of kies een alternatief zonder deze gegevens (bijvoorbeeld een pas of pincode in plaats van een vingerafdruk).
- Bronnen: AVG-art9-lid2 (AVG art. 9 lid 2); AVG-art9-lid2-a (AVG art. 9 lid 2 sub a); AVG-art9-lid2-b (AVG art. 9 lid 2 sub b); AVG-art9-lid2-e (AVG art. 9 lid 2 sub e); UAVG-art22 (UAVG art. 22); UAVG-art29 (UAVG art. 29); UAVG-art30-lid1 (UAVG art. 30 lid 1); AP-boete-vingerafdrukken-2020 (Autoriteit Persoonsgegevens, boete van € 725.000 voor het gebruik van vingerafdrukscanners bij personeel (2020))

### K3.3 — Of je het BSN alleen gebruikt waar een wet dat voorschrijft
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het BSN wordt alleen gebruikt ter uitvoering van de wet of voor doeleinden die bij wet zijn bepaald, en binnen dat doel
- Grondslag: art. 87 AVG; art. 46 UAVG; Wet algemene bepalingen burgerservicenummer
- Alleen als: `facts.processes_bsn == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: bsn_use_basis, bsn_only_for_legal_purpose, id_copy_bsn_visible
- Beoordeling:
  - present als bsn_use_basis payroll of healthcare is (typisch: loonadministratie door de werkgever, zorgaanbieder), bsn_only_for_legal_purpose waar is en id_copy_bsn_visible onwaar is.
  - present als bsn_use_basis other_law is, bsn_law_name een wet noemt, bsn_only_for_legal_purpose waar is en id_copy_bsn_visible onwaar is. Noemt bsn_law_name geen herkenbare wet: twijfel (⚠️).
  - absent als bsn_use_basis no_law is (typisch: BSN als klantnummer, of BSN opvragen 'ter identificatie' zonder wettelijke basis).
  - absent als bsn_only_for_legal_purpose onwaar is: het gebruik gaat buiten het wettelijke doel.
  - absent als id_copy_bsn_visible waar is en er geen wettelijke basis voor het BSN-gebruik is (bsn_use_basis no_law): BSN niet afgeschermd op een ID-kopie.
  - twijfel (⚠️) als id_copy_bsn_visible waar is en er wel een wettelijke basis is: de reviewer beoordeelt of die wet ook het bewaren van de kopie met zichtbaar BSN dekt.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Schrijft een wet het gebruik van het BSN in deze situatie voor, en blijft het gebruik (inclusief bewaarde ID-kopieën) binnen dat doel?
- Advies bij ❌ of ⚠️: Gebruik het BSN alleen waar een wet dat voorschrijft, en alleen voor dat doel. Gebruik een eigen klant- of personeelsnummer in plaats van het BSN en scherm het BSN af op kopieën van identiteitsbewijzen die je niet op grond van een wet met BSN moet bewaren.
- Bronnen: AVG-art87 (AVG art. 87); UAVG-art46 (UAVG art. 46); Wabb (Wet algemene bepalingen burgerservicenummer)

### K3.4 — Of je een wettelijke grond hebt voor gegevens over strafbare feiten
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Grondslag in art. 10 AVG jo. art. 31 t/m 33 UAVG; voor gegevens over eigen personeel regels vastgesteld volgens de procedure van de Wet op de ondernemingsraden (art. 33 lid 3 UAVG)
- Grondslag: art. 10 AVG; art. 31 t/m 33 UAVG
- Alleen als: `facts.processes_criminal_data == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: criminal_data_basis, criminal_data_about_employees, works_council_rules
- Beoordeling:
  - absent als criminal_data_basis none is.
  - absent als criminal_data_about_employees waar is en works_council_rules onwaar is: gegevens over eigen personeel alleen volgens regels die zijn vastgesteld met de procedure van de Wet op de ondernemingsraden (art. 33 lid 3 UAVG).
  - present als criminal_data_basis explicit_consent, made_public_by_person of legal_claim is (algemene uitzonderingen art. 32 UAVG), of assessing_request of protection_against_offences (art. 33 lid 2 UAVG), en het niet om eigen personeel gaat of works_council_rules waar is.
  - twijfel (⚠️) als criminal_data_basis other is.
  - twijfel (⚠️) als het om eigen personeel gaat en de organisatie geen ondernemingsraad of personeelsvertegenwoordiging heeft: hoe art. 33 lid 3 UAVG dan wordt nageleefd, moet een juridisch adviseur beoordelen.
  - twijfel (⚠️) als made_public_by_person is gekozen en uit de feiten niet blijkt dat de persoon de gegevens zelf openbaar heeft gemaakt.
  - Ontbrekend of 'weet ik niet' (ook works_council_rules als het om eigen personeel gaat): ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Valt het gebruik onder een uitzondering van art. 32 of 33 UAVG, en zijn voor eigen personeel regels vastgesteld volgens de WOR-procedure?
- Advies bij ❌ of ⚠️: Gebruik gegevens over strafbare feiten alleen als een van de wettelijke uitzonderingen van toepassing is. Voor gegevens over je eigen werknemers heb je regels nodig die zijn vastgesteld met de ondernemingsraad.
- Bronnen: AVG-art10 (AVG art. 10); UAVG-art31 (UAVG art. 31); UAVG-art32 (UAVG art. 32); UAVG-art33 (UAVG art. 33); UAVG-art33-lid2 (UAVG art. 33 lid 2); UAVG-art33-lid3 (UAVG art. 33 lid 3)

### K3.5 — Of je deze gegevens extra goed beveiligt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Extra waarborgen (toegang, logging, versleuteling) voor bijzondere, strafrechtelijke gegevens en BSN; doorverwijzing naar K11
- Grondslag: art. 9 en 10 AVG in samenhang met art. 32 AVG
- Alleen als: `facts.extra_safeguards != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: extra_safeguards
- Beoordeling:
  - Signalerende stap met doorverwijzing naar K11 (beveiliging). De stap toetst de maatregelen niet zelf.
  - Deze stap geldt alleen als extra_safeguards onwaar of onbekend is; uitkomst altijd review met verwijzing naar K11.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de maatregelen voor deze gevoelige gegevens passend? (Zie de beveiligingstoets.)
- Advies bij ❌ of ⚠️: Beperk wie bij deze gegevens kan, leg vast wie ze inziet en versleutel ze. Laat je beveiliging als geheel toetsen.
- Bronnen: AVG-art32 (AVG art. 32); AVG-art9 (AVG art. 9); AVG-art10 (AVG art. 10)

### K3.6 — Of je deze gegevens op grote schaal gebruikt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Grootschalige verwerking van bijzondere of strafrechtelijke gegevens; doorverwijzing naar K9 (DPIA) en K10 (FG)
- Grondslag: art. 35 lid 3 sub b en art. 37 lid 1 sub c AVG
- Alleen als: `facts.large_scale != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: large_scale
- Beoordeling:
  - Signalerende stap met doorverwijzing naar K9 (DPIA-toets) en K10 (FG-plicht). 'Grote schaal' is een open norm en wordt daar beoordeeld.
  - Deze stap geldt alleen als large_scale waar of onbekend is; uitkomst altijd review.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Is de verwerking grootschalig in de zin van art. 35 lid 3 sub b en art. 37 lid 1 sub c AVG?
- Advies bij ❌ of ⚠️: Laat beoordelen of voor deze verwerking een DPIA en een functionaris gegevensbescherming verplicht zijn.
- Bronnen: AVG-art35-lid3-b (AVG art. 35 lid 3 sub b); AVG-art37-lid1-c (AVG art. 37 lid 1 sub c)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): data_description. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 2: geen uitzondering uit art. 9 lid 2 AVG of art. 22 t/m 30 UAVG → non_compliant.
- Stap 2: toestemming in een werkgeversrelatie → review (zelden vrij). Kennelijk door de betrokkene openbaar gemaakt → strikt uitleggen, bij twijfel review.
- Stap 2: vingerafdruk of andere biometrie voor tijdregistratie of een kantoordeur zonder bijzonder beveiligingsbelang → non_compliant (art. 29 UAVG; AP-boete 2020).
- Stap 3: typisch compliant: loonadministratie (werkgever), zorgaanbieder. Typisch non_compliant: BSN als klantnummer, BSN opvragen 'ter identificatie' zonder wettelijke basis, BSN niet afgeschermd op een ID-kopie.
- Stap 4: geen grondslag → non_compliant; gegevens over eigen personeel zonder met de OR vastgestelde regels → non_compliant.
- Dit kader komt naast K2: ook bij een geldige uitzondering is een grondslag uit art. 6 nodig.

## Samenhang met andere kaders

- Kader K2 (/toets-grondslag) — als `facts.processes_health_data != false or facts.processes_biometric_data != false or facts.processes_other_special_data != false or facts.processes_criminal_data == true`: Naast een uitzondering voor bijzondere of strafrechtelijke gegevens is ook een gewone grondslag nodig.
- Kader K15 (/toets-hr-privacy) — als `facts.processes_health_data == true`: Voor gezondheidsgegevens van werknemers (verzuim) gelden eigen regels voor werkgevers.
- Kader K11 (/toets-beveiliging) — als `facts.extra_safeguards != true`: Voor deze gegevens zijn extra beveiligingsmaatregelen nodig.
- Kader K9 (/dpia) — als `facts.large_scale != false`: Grootschalige verwerking van bijzondere of strafrechtelijke gegevens vraagt om een DPIA-toets.
- Kader K10 (/toets-fg-plicht) — als `facts.large_scale != false`: Grootschalige verwerking van bijzondere of strafrechtelijke gegevens kan een functionaris gegevensbescherming verplicht maken.

## Open punten en voorbehouden

- Inhoud van de Wet algemene bepalingen burgerservicenummer en de sectorwetten die het BSN-gebruik voorschrijven, in de bronnendatabase vastleggen; niet uit het hoofd toepassen.
