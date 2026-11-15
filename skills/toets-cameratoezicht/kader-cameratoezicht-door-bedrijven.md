# Kader K14 — Cameratoezicht door bedrijven

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of cameratoezicht door een bedrijf een concreet doel heeft, noodzakelijk en beperkt is, kenbaar is gemaakt, en of beelden kort en beveiligd worden bewaard; met extra aandacht voor camera's op de werkvloer, slimme camera's en emotieherkenning.

Bronnen: AVG-art5 (AVG art. 5); AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); AVG-art13 (AVG art. 13); AVG-art35 (AVG art. 35); WOR-art27-lid1-l (Wet op de ondernemingsraden art. 27 lid 1 sub l (instemmingsrecht personeelsvolgsystemen)); Sr-art139f (Wetboek van Strafrecht art. 139f (heimelijk vervaardigen van afbeeldingen in een woning of andere niet voor het publiek toegankelijke plaats)); Sr-art441b (Wetboek van Strafrecht art. 441b (heimelijk vervaardigen van afbeeldingen op een voor het publiek toegankelijke plaats)); HvJEU-C-708-18 (HvJEU 11 december 2019, C-708/18, TK/Asociaţia de Proprietari bloc M5A-ScaraA); EHRM-LopezRibalda-2019 (EHRM (Grote Kamer) 17 oktober 2019, López Ribalda e.a./Spanje (heimelijke camera's op de werkvloer)); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur); AP-cameratoezicht (Autoriteit Persoonsgegevens, informatie over cameratoezicht door bedrijven); AIVO-art5-lid1-f (AI-verordening art. 5 lid 1 sub f)

## Formulier (vragen aan de gebruiker)

- **camera_purpose**: Waarom hangen de camera's er? Beschrijf het doel zo concreet mogelijk.
  - Label (voor de plek-om-in-te-vullen): waarvoor de camera's hangen
  - Hulp: Bijvoorbeeld: 'Inbraak en diefstal in het magazijn voorkomen en kunnen aantonen' of 'De veiligheid van medewerkers aan de kassa beschermen'.
  - Type: text
- **purpose_documented**: Heb je het doel van de camera's op papier gezet voordat je ermee begon te filmen?
  - Label (voor de plek-om-in-te-vullen): of het doel vooraf is vastgelegd
  - Type: boolean
- **incidents_or_risks**: Welke incidenten of concrete risico's waren de aanleiding voor de camera's?
  - Label (voor de plek-om-in-te-vullen): welke incidenten of risico's er waren
  - Hulp: Bijvoorbeeld: 'Drie inbraken in 2025' of 'Medewerkers zijn aan de kassa bedreigd'. Waren er geen, schrijf dat dan op.
  - Type: text
- **alternatives_considered**: Heb je eerst minder ingrijpende maatregelen overwogen of geprobeerd, zoals betere verlichting, sloten of toegangscontrole?
  - Label (voor de plek-om-in-te-vullen): of je eerst minder ingrijpende maatregelen hebt overwogen
  - Type: boolean
- **alternatives_description**: Welke maatregelen heb je overwogen of geprobeerd, en waarom waren die niet genoeg?
  - Label (voor de plek-om-in-te-vullen): welke andere maatregelen je hebt overwogen
  - Type: text · Alleen vragen als: `facts.alternatives_considered == true`
- **films_public_road**: Filmen de camera's (een deel van) de openbare weg, zoals de stoep of de straat?
  - Label (voor de plek-om-in-te-vullen): of de camera's de openbare weg filmen
  - Type: enum (none / narrow_strip / yes)
- **films_neighbours**: Filmen de camera's (een deel van) het terrein, de ingang of de ramen van buren?
  - Label (voor de plek-om-in-te-vullen): of de camera's buren filmen
  - Type: boolean
- **films_private_areas**: Filmen de camera's toiletten, kleedruimtes, pauzeruimtes of andere plekken waar mensen privacy mogen verwachten?
  - Label (voor de plek-om-in-te-vullen): of de camera's plekken filmen waar mensen privacy mogen verwachten
  - Type: boolean
- **signage**: Hangt er een bord of sticker, vóórdat mensen het gefilmde gebied binnengaan?
  - Label (voor de plek-om-in-te-vullen): of er een bord hangt vóór het gefilmde gebied
  - Type: enum (complete / incomplete / none)
- **privacy_statement_mentions_cameras**: Staat in je privacyverklaring dat je camera's gebruikt, waarom, en hoe lang je de beelden bewaart?
  - Label (voor de plek-om-in-te-vullen): of je privacyverklaring het cameratoezicht beschrijft
  - Type: boolean
- **retention**: Hoe lang bewaar je de camerabeelden normaal (dus als er niets is gebeurd)?
  - Label (voor de plek-om-in-te-vullen): hoe lang je camerabeelden bewaart
  - Type: enum (up_to_4_weeks / longer / no_fixed_period)
- **retention_reason**: Waarom bewaar je de beelden langer dan 4 weken?
  - Label (voor de plek-om-in-te-vullen): waarom je de beelden zo lang bewaart
  - Type: text · Alleen vragen als: `facts.retention == "longer"`
- **footage_access_limited**: Kunnen alleen daarvoor aangewezen personen de beelden bekijken?
  - Label (voor de plek-om-in-te-vullen): of alleen bevoegde personen de beelden kunnen bekijken
  - Type: boolean
- **footage_access_logged**: Wordt bijgehouden wie wanneer beelden heeft bekeken of gekopieerd?
  - Label (voor de plek-om-in-te-vullen): of wordt vastgelegd wie de beelden bekijkt
  - Type: boolean
- **workplace_cameras**: Komen je medewerkers tijdens hun werk in beeld?
  - Label (voor de plek-om-in-te-vullen): of medewerkers in beeld komen
  - Type: boolean
- **employees_informed**: Heb je je medewerkers verteld waar de camera's hangen, waarom, en wat er met de beelden gebeurt?
  - Label (voor de plek-om-in-te-vullen): of medewerkers over de camera's zijn geïnformeerd
  - Type: boolean · Alleen vragen als: `facts.workplace_cameras == true`
- **has_works_council**: Heeft je organisatie een ondernemingsraad?
  - Label (voor de plek-om-in-te-vullen): of er een ondernemingsraad is
  - Type: boolean · Alleen vragen als: `facts.workplace_cameras == true` · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **works_council_consent**: Heeft de ondernemingsraad ingestemd met het cameratoezicht?
  - Label (voor de plek-om-in-te-vullen): of de ondernemingsraad heeft ingestemd
  - Type: boolean · Alleen vragen als: `facts.workplace_cameras == true and facts.has_works_council == true`
- **covert_cameras**: Gebruik je (ook) verborgen camera's, waarvan de medewerkers niet weten dat ze er hangen?
  - Label (voor de plek-om-in-te-vullen): of er verborgen camera's zijn
  - Type: boolean · Alleen vragen als: `facts.workplace_cameras == true`
- **covert_justification**: Waarom gebruik je een verborgen camera, hoe lang, en welke andere maatregelen heb je eerst geprobeerd?
  - Label (voor de plek-om-in-te-vullen): waarom de verborgen camera nodig is
  - Type: text · Alleen vragen als: `facts.covert_cameras == true`
- **dpia_considered**: Heb je vooraf onderzocht of voor de camera's een privacy-risicoanalyse (DPIA) nodig is?
  - Label (voor de plek-om-in-te-vullen): of je hebt onderzocht of een DPIA nodig is
  - Type: boolean
- **biometric_cameras**: Herkennen de camera's (of de software erachter) gezichten of mensen aan hun lichaamskenmerken?
  - Label (voor de plek-om-in-te-vullen): of de camera's gezichtsherkenning of andere biometrie gebruiken
  - Hulp: Bijvoorbeeld gezichtsherkenning bij de ingang, of software die bezoekers herkent aan hun manier van lopen. Alleen beweging of personen detecteren zonder ze te herkennen telt niet.
  - Type: boolean
- **emotion_recognition**: Herkent of analyseert de camera (of de software erachter) emoties of stemmingen van medewerkers?
  - Label (voor de plek-om-in-te-vullen): of de camera's emoties van medewerkers herkennen
  - Hulp: Bijvoorbeeld software die meet of medewerkers gestrest, boos of vrolijk zijn.
  - Type: boolean
- **emotion_exception_claimed**: Gebruik je deze emotieherkenning uitsluitend om medische redenen of om veiligheidsredenen?
  - Label (voor de plek-om-in-te-vullen): of je emotieherkenning gebruikt om medische of veiligheidsredenen
  - Hulp: Bijvoorbeeld om vermoeidheid bij chauffeurs van zware voertuigen te detecteren. Klanttevredenheid, productiviteit of beoordeling van medewerkers zijn geen medische of veiligheidsredenen.
  - Type: boolean · Alleen vragen als: `facts.emotion_recognition == true`
- **emotion_exception_description**: Beschrijf de medische of veiligheidsreden en hoe het systeem wordt gebruikt.
  - Label (voor de plek-om-in-te-vullen): welke medische of veiligheidsreden je hebt
  - Type: text · Alleen vragen als: `facts.emotion_exception_claimed == true`

## Toetspunten

### K14.1 — Het doel van de camera's is concreet en vooraf vastgelegd
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Doel concreet (beveiliging van personen, goederen, pand) en vooraf vastgelegd; door naar K2c (gerechtvaardigd belang)
- Grondslag: art. 5 lid 1 sub b en art. 6 lid 1 sub f AVG
- Beoordeeld op: de antwoorden
- Nodig: camera_purpose, purpose_documented
- Beoordeling:
  - Duidelijk non_compliant: purpose_documented onwaar, of camera_purpose noemt geen herkenbaar doel (bijvoorbeeld 'voor de zekerheid' of 'om te kijken wat er gebeurt').
  - Duidelijk compliant: purpose_documented waar én camera_purpose noemt een concreet doel, zoals de beveiliging van personen, goederen of het pand.
  - Een doel dat vooral het controleren van medewerkers of hun prestaties betreft: geen duidelijk geval (zie stap 7).
  - purpose_documented 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - In alle andere gevallen geen duidelijk geval. De belangenafweging zelf wordt getoetst in K2c.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het doel concreet genoeg, en is het vooraf vastgelegd?
- Advies bij ❌ of ⚠️: Leg vast waarvoor de camera's dienen, zo concreet mogelijk (bijvoorbeeld: inbraak in het magazijn voorkomen), voordat je gaat filmen.
- Bronnen: AVG-art5-lid1-b (AVG art. 5 lid 1 sub b); AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur); HvJEU-C-708-18 (HvJEU 11 december 2019, C-708/18, TK/Asociaţia de Proprietari bloc M5A-ScaraA)

### K14.2 — Camera's zijn echt nodig
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Noodzakelijk: zijn minder ingrijpende maatregelen (verlichting, sloten, toegangscontrole) onvoldoende? Zijn er concrete incidenten of risico's?
- Grondslag: art. 5 lid 1 sub c en art. 6 lid 1 sub f AVG
- Beoordeeld op: de antwoorden
- Nodig: incidents_or_risks, alternatives_considered, alternatives_description
- Beoordeling:
  - Duidelijk non_compliant: incidents_or_risks noemt geen enkel incident of concreet risico én alternatives_considered is onwaar.
  - Duidelijk compliant: incidents_or_risks noemt concrete incidenten of risico's, én alternatives_considered is waar met een toelichting waaruit blijkt dat minder ingrijpende maatregelen onvoldoende waren.
  - alternatives_considered 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is cameratoezicht noodzakelijk, of had een minder ingrijpende maatregel volstaan?
- Advies bij ❌ of ⚠️: Leg vast welke incidenten of risico's er zijn, en waarom minder ingrijpende maatregelen zoals verlichting, sloten of toegangscontrole niet genoeg zijn.
- Bronnen: AVG-art5-lid1-c (AVG art. 5 lid 1 sub c); AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); HvJEU-C-708-18 (HvJEU 11 december 2019, C-708/18, TK/Asociaţia de Proprietari bloc M5A-ScaraA); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur)

### K14.3 — De camera's filmen niet meer dan nodig
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Beperkt tot wat nodig is: geen zicht op de openbare weg (hooguit een onvermijdelijke smalle strook), buren of plekken met een hoge privacyverwachting (toiletten, kleedruimtes, pauzeruimtes)
- Grondslag: art. 5 lid 1 sub c AVG
- Beoordeeld op: de antwoorden
- Nodig: films_public_road, films_neighbours, films_private_areas
- Beoordeling:
  - Duidelijk non_compliant: films_private_areas waar, of films_public_road yes, of films_neighbours waar.
  - Duidelijk compliant: films_public_road none of narrow_strip, films_neighbours onwaar en films_private_areas onwaar.
  - 'Weet ik niet' bij een van de drie, zonder een van de non_compliant-gronden: ⚠️ (noem welk antwoord ontbreekt).
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het gefilmde gebied beperkt tot wat voor het doel nodig is?
- Advies bij ❌ of ⚠️: Richt de camera's zo in dat ze alleen je eigen terrein filmen, hooguit met een smalle strook openbare weg die niet te vermijden is, en nooit toiletten, kleedruimtes of pauzeruimtes. Gebruik zo nodig privacymaskering.
- Bronnen: AVG-art5-lid1-c (AVG art. 5 lid 1 sub c); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur); AP-cameratoezicht (Autoriteit Persoonsgegevens, informatie over cameratoezicht door bedrijven)

### K14.4 — Mensen zien vóór het gefilmde gebied dat er camera's zijn
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Duidelijk kenbaar gemaakt vóór het betreden van het gefilmde gebied (bord met wie, waarom, en waar meer informatie); volledige informatie in de privacyverklaring (K5)
- Grondslag: art. 12 lid 1 en art. 13 AVG
- Beoordeeld op: de antwoorden
- Nodig: signage
- Beoordeling:
  - present als signage complete is; absent als signage incomplete of none is; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - De volledige informatie hoort daarnaast in de privacyverklaring (tweede laag); dat wordt getoetst in K5. Is privacy_statement_mentions_cameras niet true, noem dat in het rapport als vervolgpunt; het verandert de uitkomst van deze stap niet.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Hang vóór het gefilmde gebied een bord met wie er filmt, waarom, en waar mensen meer informatie vinden (bijvoorbeeld een link naar je privacyverklaring).
- Bronnen: AVG-art12-lid1 (AVG art. 12 lid 1); AVG-art13 (AVG art. 13); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur); AP-cameratoezicht (Autoriteit Persoonsgegevens, informatie over cameratoezicht door bedrijven)

### K14.5 — Beelden worden kort bewaard
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bewaartermijn kort en onderbouwd; de AP noemt in principe maximaal 4 weken, tenzij beelden nodig zijn voor de afhandeling van een incident
- Grondslag: art. 5 lid 1 sub e AVG
- Beoordeeld op: de antwoorden
- Nodig: retention, retention_reason
- Beoordeling:
  - Duidelijk compliant: retention up_to_4_weeks.
  - Duidelijk non_compliant: retention no_fixed_period.
  - retention longer: geen duidelijk geval; de AP noemt 4 weken als uitgangspunt 'in principe', dus een langere termijn vraagt een beoordeling van retention_reason.
  - Beelden van een concreet incident mogen langer worden bewaard zolang dat nodig is voor de afhandeling.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de bewaartermijn kort en onderbouwd?
- Advies bij ❌ of ⚠️: Stel een vaste, korte bewaartermijn in (de AP noemt in principe maximaal 4 weken) en laat de beelden daarna automatisch overschrijven. Bewaar beelden van een incident alleen zolang dat nodig is om het af te handelen.
- Bronnen: AVG-art5-lid1-e (AVG art. 5 lid 1 sub e); AP-cameratoezicht (Autoriteit Persoonsgegevens, informatie over cameratoezicht door bedrijven); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur)

### K14.6 — Alleen bevoegde personen kunnen de beelden zien, en dat wordt bijgehouden
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Toegang tot beelden beperkt tot bevoegde personen, en gelogd
- Grondslag: art. 5 lid 1 sub f en art. 32 lid 1 AVG
- Beoordeeld op: de antwoorden
- Nodig: footage_access_limited, footage_access_logged
- Beoordeling:
  - present als footage_access_limited en footage_access_logged allebei waar zijn.
  - absent als een van beide onwaar is.
  - Ontbrekend of 'weet ik niet' bij een van beide (en de andere niet onwaar): ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Wijs aan wie de beelden mag bekijken, beveilig de toegang met een eigen account, en houd bij wie wanneer beelden bekijkt of kopieert.
- Bronnen: AVG-art5-lid1-f (AVG art. 5 lid 1 sub f); AVG-art32-lid1 (AVG art. 32 lid 1); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur)

### K14.7 — Camera's op de werkvloer: medewerkers en ondernemingsraad
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Werknemers geïnformeerd; ondernemingsraad heeft instemmingsrecht (art. 27 lid 1 sub l WOR). Heimelijk alleen bij een concreet vermoeden, tijdelijk en als uiterste middel; heimelijk filmen kan strafbaar zijn (art. 139f en 441b Sr). Altijd ⚠️
- Grondslag: art. 13 AVG; art. 27 lid 1 sub l WOR; art. 139f en 441b Sr
- Alleen als: `facts.workplace_cameras == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: employees_informed, has_works_council, works_council_consent, covert_cameras, covert_justification
- Beoordeling:
  - Deze stap gaat altijd naar menselijke review (⚠️): nooit compliant.
  - Noem in de toelichting de concrete tekorten: medewerkers niet geïnformeerd (employees_informed onwaar); ondernemingsraad aanwezig maar geen instemming (works_council_consent onwaar); verborgen camera's (covert_cameras waar).
  - Verborgen camera's zijn alleen denkbaar bij een concreet vermoeden, tijdelijk en als uiterste middel (López Ribalda); vermeld dat heimelijk filmen strafbaar kan zijn (art. 139f en 441b Sr).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn medewerkers geïnformeerd, heeft de ondernemingsraad ingestemd, en is heimelijk filmen (indien van toepassing) gerechtvaardigd door een concreet vermoeden, tijdelijk en als uiterste middel?
- Advies bij ❌ of ⚠️: Informeer je medewerkers over de camera's, vraag instemming van de ondernemingsraad als je die hebt, en gebruik geen verborgen camera's zonder juridisch advies.
- Bronnen: AVG-art13 (AVG art. 13); WOR-art27-lid1-l (Wet op de ondernemingsraden art. 27 lid 1 sub l (instemmingsrecht personeelsvolgsystemen)); Sr-art139f (Wetboek van Strafrecht art. 139f (heimelijk vervaardigen van afbeeldingen in een woning of andere niet voor het publiek toegankelijke plaats)); Sr-art441b (Wetboek van Strafrecht art. 441b (heimelijk vervaardigen van afbeeldingen op een voor het publiek toegankelijke plaats)); EHRM-LopezRibalda-2019 (EHRM (Grote Kamer) 17 oktober 2019, López Ribalda e.a./Spanje (heimelijke camera's op de werkvloer)); AP-cameratoezicht (Autoriteit Persoonsgegevens, informatie over cameratoezicht door bedrijven)

### K14.8 — Of een DPIA nodig is
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: DPIA nodig? → K9
- Grondslag: art. 35 AVG
- Beoordeeld op: de antwoorden
- Nodig: dpia_considered
- Beoordeling:
  - Signalerende stap: de DPIA-plicht wordt getoetst in K9. Nooit compliant.
  - Vermeld in de toelichting of vooraf is onderzocht of een DPIA nodig is (dpia_considered), en verwijs naar K9.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Is voor dit cameratoezicht een DPIA verplicht (zie K9)?
- Advies bij ❌ of ⚠️: Ga na of voor je camera's een DPIA verplicht is, vooral bij camera's op de werkvloer, veel camera's of slimme camera's.
- Bronnen: AVG-art35 (AVG art. 35); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur)

### K14.9 — Slimme camera's met gezichtsherkenning of andere biometrie
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Slimme camera's met gezichtsherkenning of andere biometrie → K3 (art. 29 UAVG) en AI-kaders (AI0-AI2). Altijd ⚠️
- Grondslag: art. 9 lid 1 AVG; art. 29 UAVG
- Alleen als: `facts.biometric_cameras == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: biometric_cameras
- Beoordeling:
  - Deze stap gaat altijd naar menselijke review (⚠️): nooit compliant.
  - Verwijs naar K3 (art. 29 UAVG: biometrie alleen als noodzakelijk voor authenticatie of beveiliging) en naar de AI-kaders AI0-AI2.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Valt de biometrische verwerking onder een uitzondering van art. 9 lid 2 AVG of art. 29 UAVG, en welke eisen stelt de AI-verordening?
- Advies bij ❌ of ⚠️: Gebruik gezichtsherkenning of andere biometrie niet zonder juridisch advies: dit is alleen in uitzonderlijke gevallen toegestaan.
- Bronnen: AVG-art9-lid1 (AVG art. 9 lid 1); UAVG-art29 (UAVG art. 29); EDPB-RL-03-2019 (EDPB, Richtsnoeren 3/2019 inzake de verwerking van persoonsgegevens door middel van videoapparatuur)

### K14.10 — Er wordt geen emotieherkenning op medewerkers toegepast
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Emotieherkenning op de werkplek: verboden AI-praktijk sinds 2 februari 2025, tenzij om medische of veiligheidsredenen → ❌, verwijzen naar AI1. Beroep op de medische of veiligheidsuitzondering → ⚠️
- Grondslag: art. 5 lid 1 sub f AI-verordening
- Alleen als: `facts.emotion_recognition == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: emotion_recognition, emotion_exception_claimed, emotion_exception_description
- Beoordeling:
  - Deze stap geldt alleen als emotion_recognition waar is.
  - absent (verboden praktijk) als emotion_exception_claimed onwaar is → non_compliant (❌); verwijs naar AI1.
  - Beroept de klant zich op de medische of veiligheidsuitzondering (emotion_exception_claimed waar) → review (⚠️), nooit compliant; beoordeel emotion_exception_description in de toelichting.
  - emotion_exception_claimed ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Valt het gebruik echt onder de uitzondering voor medische of veiligheidsredenen van art. 5 lid 1 sub f AI-verordening?
- Advies bij ❌ of ⚠️: Stop met emotieherkenning op medewerkers. Dit is sinds 2 februari 2025 verboden, behalve om medische of veiligheidsredenen; laat een beroep op die uitzondering juridisch beoordelen.
- Bronnen: AIVO-art5-lid1-f (AI-verordening art. 5 lid 1 sub f)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): camera_purpose, incidents_or_risks, workplace_cameras, has_works_council, covert_cameras. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 1: doel concreet en vooraf vastgelegd → de belangenafweging (gerechtvaardigd belang) gaat door naar K2c.
- Stap 4: volledige informatie hoort in de privacyverklaring → K5.
- Stap 10: emotieherkenning op medewerkers → non_compliant (verboden AI-praktijk, art. 5 lid 1 sub f AI-verordening), verwijzen naar AI1; beroep op de medische of veiligheidsuitzondering → review.

## Samenhang met andere kaders

- Kader K2c (/toets-grondslag) — als `true`: Cameratoezicht door bedrijven steunt op gerechtvaardigd belang; de belangenafweging wordt daar getoetst.
- Kader K5 (/privacyverklaring) — als `facts.privacy_statement_mentions_cameras != true`: De volledige informatie over het cameratoezicht (doel, grondslag, bewaartermijn) hoort in de privacyverklaring; die vermeldt het cameratoezicht nog niet of dat is onbekend.
- Kader K9 (/dpia) — als `facts.dpia_considered != true`: Er is niet vooraf onderzocht of een DPIA nodig is.
- Kader K3 (/toets-grondslag) — als `facts.biometric_cameras == true`: Gezichtsherkenning of andere biometrie valt onder de bijzondere persoonsgegevens (art. 29 UAVG).
- Kader AI0 (/toets-ai-act-basis) — als `facts.biometric_cameras == true or facts.emotion_recognition == true`: Slimme camera's kunnen een AI-systeem zijn; de AI-verordening kan van toepassing zijn.
- Kader AI1 (/toets-ai-act-basis) — als `facts.biometric_cameras == true or facts.emotion_recognition == true`: Emotieherkenning op de werkplek is een verboden AI-praktijk; biometrische systemen kunnen verboden of hoog risico zijn.
- Kader AI2 (/toets-ai-act-basis) — als `facts.biometric_cameras == true`: Biometrische identificatie kan een AI-systeem met hoog risico zijn.
