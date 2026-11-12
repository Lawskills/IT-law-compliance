# Kader AI1 — Verboden praktijken (art. 5)

Versie 0.4 · peildatum 2026-11-10

Doel: Controleren of een AI-toepassing onder een van de verboden van art. 5 AI-verordening valt. De verboden gelden sinds 2 februari 2025 voor aanbieders én gebruiksverantwoordelijken (in de handel brengen, in gebruik stellen of gebruiken).

Geldt alleen als: `facts.system_infers != false` · poortstap AI0.1 — vervalt als de toepassing duidelijk geen AI-systeem is (regel van kader AI0)

Bronnen: AIVO-art3-34 (AI-verordening art. 3 punt 34); AIVO-art3-39 (AI-verordening art. 3 punt 39); AIVO-art3-40 (AI-verordening art. 3 punt 40); AIVO-art3-44 (AI-verordening art. 3 punt 44); AIVO-art5-lid1-a (AI-verordening art. 5 lid 1 sub a); AIVO-art5-lid1-b (AI-verordening art. 5 lid 1 sub b); AIVO-art5-lid1-ba (AI-verordening art. 5 lid 1 sub ba); AIVO-art5-lid1-bb (AI-verordening art. 5 lid 1 sub bb); AIVO-art5-lid1-c (AI-verordening art. 5 lid 1 sub c); AIVO-art5-lid1-d (AI-verordening art. 5 lid 1 sub d); AIVO-art5-lid1-e (AI-verordening art. 5 lid 1 sub e); AIVO-art5-lid1-f (AI-verordening art. 5 lid 1 sub f); AIVO-art5-lid1-g (AI-verordening art. 5 lid 1 sub g); AIVO-art5-lid1-h (AI-verordening art. 5 lid 1 sub h); AIVO-art5-lid1a (AI-verordening art. 5 lid 1a); AIVO-art5-lid1b (AI-verordening art. 5 lid 1b); AIVO-art99-lid3 (AI-verordening art. 99 lid 3); AIVO-art99-lid6 (AI-verordening art. 99 lid 6); AIVO-art113 (AI-verordening art. 113); AIVO-overw18 (AI-verordening overweging 18); AIVO-overw29 (AI-verordening overweging 29); AIVO-overw31 (AI-verordening overweging 31); AIVO-overw44 (AI-verordening overweging 44); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening)); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

## Formulier (vragen aan de gebruiker)

- **app_purpose**: Waarvoor gebruik je de toepassing, en bij of over wie?
  - Label (voor de plek-om-in-te-vullen): waarvoor en bij wie je de toepassing gebruikt
  - Hulp: Overgenomen uit de eerste vragen over deze toepassing. Vul aan als dat nodig is.
  - Type: text
- **manipulative_techniques**: Is de toepassing bedoeld of geschikt om mensen ongemerkt, manipulatief of misleidend te beïnvloeden, zodat zij een keuze maken die zij anders niet hadden gemaakt en die hen kan schaden?
  - Label (voor de plek-om-in-te-vullen): of de toepassing mensen ongemerkt of misleidend beïnvloedt
  - Hulp: Bijvoorbeeld verborgen prikkels, of een systeem dat bewust misleidt om iemand tot een dure aankoop of een schadelijk besluit te brengen. Gewone, eerlijke reclame of een aanbeveling valt hier niet onder.
  - Type: boolean
- **exploits_vulnerability**: Speelt de toepassing in op de kwetsbaarheid van mensen door hun leeftijd, een handicap of hun sociale of economische situatie, op een manier die hun gedrag wezenlijk verandert en hen kan schaden?
  - Label (voor de plek-om-in-te-vullen): of de toepassing inspeelt op kwetsbaarheden van mensen
  - Hulp: Bijvoorbeeld een systeem dat mensen met schulden gericht leningen aanprijst op hun zwakste momenten, of kinderen aanzet tot riskant gedrag.
  - Type: boolean
- **social_scoring**: Beoordeelt of rangschikt de toepassing mensen over een periode op basis van hun gedrag of (afgeleide) persoonlijke eigenschappen, met een score die leidt tot een nadelige behandeling?
  - Label (voor de plek-om-in-te-vullen): of de toepassing mensen een score geeft op basis van hun gedrag of kenmerken
  - Hulp: Het gaat om een score die wordt gebruikt in een andere situatie dan waarin de gegevens zijn verzameld (bijvoorbeeld gedrag op sociale media dat bepaalt of iemand een woning krijgt), of die onevenredig zwaar uitpakt. Een gewone kredietcheck of klantwaardering is iets anders; die komt bij het hoog-risicosignaal aan bod.
  - Type: boolean
- **social_scoring_description**: Waarop is de score gebaseerd, waarvoor wordt hij gebruikt, en wat zijn de gevolgen voor iemand met een lage score?
  - Label (voor de plek-om-in-te-vullen): hoe de score wordt gebruikt
  - Type: text · Alleen vragen als: `facts.social_scoring != false`
- **crime_prediction**: Voorspelt de toepassing het risico dat iemand een strafbaar feit pleegt, uitsluitend op basis van een profiel of persoonlijke eigenschappen?
  - Label (voor de plek-om-in-te-vullen): of de toepassing voorspelt of iemand een strafbaar feit zal plegen
  - Hulp: Bijvoorbeeld 'deze klant heeft een hoog risico op diefstal' op basis van leeftijd, woonplaats of persoonlijkheid. Een systeem dat een medewerker helpt bij een beoordeling die al op concrete, controleerbare feiten berust, valt hier niet onder.
  - Type: boolean
- **face_scraping**: Bouwt of vult de toepassing een databank voor gezichtsherkenning door zonder onderscheid gezichtsfoto's van internet of camerabeelden te verzamelen?
  - Label (voor de plek-om-in-te-vullen): of de toepassing ongericht gezichtsfoto's verzamelt voor gezichtsherkenning
  - Type: boolean
- **emotion_inference**: Leidt de toepassing emoties of intenties van mensen af, zoals boosheid, stress, tevredenheid, verveling of of iemand liegt?
  - Label (voor de plek-om-in-te-vullen): of de toepassing emoties of intenties van mensen afleidt
  - Hulp: Ook als het maar een onderdeel is, zoals 'sentimentscore' of 'stemmingsanalyse' in een klantenservice- of HR-tool.
  - Type: boolean
- **emotion_data_basis**: Waaruit leidt de toepassing de emoties af?
  - Label (voor de plek-om-in-te-vullen): waaruit de toepassing de emoties afleidt
  - Type: enum (biometric / text_only) · Alleen vragen als: `facts.emotion_inference != false`
- **emotion_subjects**: Van wie leidt de toepassing de emoties af?
  - Label (voor de plek-om-in-te-vullen): bij wie de toepassing emoties afleidt
  - Type: enum (employees / job_applicants / students / customers_and_employees / customers_or_public) · Alleen vragen als: `facts.emotion_inference != false`
- **emotion_medical_or_safety**: Wordt de emotieherkenning uitsluitend gebruikt om medische redenen of voor de veiligheid van mensen?
  - Label (voor de plek-om-in-te-vullen): of de emotieherkenning uitsluitend om medische of veiligheidsredenen wordt gebruikt
  - Hulp: Bijvoorbeeld een medisch hulpmiddel, of het bewaken van de aandacht van iemand in een beroep met levensgevaar. Algemene stress-, burn-out- of welzijnsmonitoring valt hier niet onder.
  - Type: boolean · Alleen vragen als: `facts.emotion_inference != false and facts.emotion_data_basis != "text_only" and facts.emotion_subjects != "customers_or_public"`
- **biometric_categorisation**: Deelt de toepassing mensen in op basis van gezicht, stem of andere lichaamskenmerken om hun ras, politieke opvattingen, vakbondslidmaatschap, geloof of levensovertuiging, seksleven of seksuele gerichtheid af te leiden?
  - Label (voor de plek-om-in-te-vullen): of de toepassing mensen indeelt naar gevoelige kenmerken op basis van lichaamskenmerken
  - Type: boolean
- **realtime_rbi_law_enforcement**: Wordt de toepassing gebruikt om voor politie of justitie live mensen op afstand te herkennen in openbaar toegankelijke ruimten, zoals straten, winkels of stations?
  - Label (voor de plek-om-in-te-vullen): of de toepassing voor politie of justitie live personen herkent in openbaar toegankelijke ruimten
  - Hulp: Alleen relevant voor politie, justitie of wie in hun opdracht werkt. Voor bijna alle organisaties is het antwoord nee.
  - Type: boolean
- **generates_intimate_content**: Is de toepassing bedoeld of gebruikt om realistische naakt- of seksuele beelden, video's of geluid van echte, herkenbare personen te maken of te bewerken, of kan zij dat zonder moeite omdat beveiligingen ontbreken?
  - Label (voor de plek-om-in-te-vullen): of de toepassing naakt- of seksuele beelden van echte personen kan maken
  - Hulp: Een gewone beeldgenerator met goede beveiligingen tegen dit soort gebruik valt hier niet onder.
  - Type: boolean

## Toetspunten

### AI1.1 — Of de toepassing mensen manipuleert of misleidt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen subliminale, doelbewust manipulatieve of misleidende technieken die het gedrag wezenlijk verstoren, waardoor iemand een besluit neemt dat hij anders niet had genomen, met (waarschijnlijk) aanzienlijke schade
- Grondslag: art. 5 lid 1 sub a AI-verordening; overweging 29
- Beoordeeld op: de antwoorden
- Nodig: manipulative_techniques, app_purpose
- Beoordeling:
  - present als manipulative_techniques false is en app_purpose geen manipulatief of misleidend gebruik beschrijft.
  - absent als manipulative_techniques true is en app_purpose een doelbewust misleidende of subliminale techniek beschrijft die mensen tot een schadelijk besluit brengt (bijvoorbeeld verborgen prikkels, of doelbewust misleiden om tot een aankoop of besluit met aanzienlijke financiële of lichamelijke schade te komen).
  - twijfel (⚠️) bij elk grensgeval: gepersonaliseerde verkoopdruk, 'dark patterns' of overtuigingstechnieken waarbij niet duidelijk is of het gedrag wezenlijk wordt verstoord of de schade aanzienlijk is; of als manipulative_techniques true is zonder duidelijke beschrijving.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Verstoort de techniek het gedrag wezenlijk, en veroorzaakt of dreigt zij aanzienlijke schade (art. 5 lid 1 sub a)?
- Advies bij ❌ of ⚠️: Stop met deze toepassing en schakel een juridisch adviseur in. Verboden AI-praktijken kunnen leiden tot boetes van tot 35 miljoen euro of 7% van de wereldwijde jaaromzet (voor het mkb het laagste van beide).
- Bronnen: AIVO-art5-lid1-a (AI-verordening art. 5 lid 1 sub a); AIVO-overw29 (AI-verordening overweging 29); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI1.2 — Of de toepassing inspeelt op kwetsbare mensen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen uitbuiting van kwetsbaarheden door leeftijd, handicap of een specifieke sociale of economische situatie, met een wezenlijke verstoring van gedrag en (waarschijnlijk) aanzienlijke schade
- Grondslag: art. 5 lid 1 sub b AI-verordening; overweging 29
- Beoordeeld op: de antwoorden
- Nodig: exploits_vulnerability, app_purpose
- Beoordeling:
  - present als exploits_vulnerability false is en app_purpose geen gericht gebruik op kwetsbare groepen beschrijft.
  - absent als exploits_vulnerability true is en app_purpose beschrijft dat het systeem doelbewust inspeelt op de leeftijd, handicap of sociale of economische situatie van mensen om hun gedrag te sturen, met aanzienlijke schade als gevolg.
  - twijfel (⚠️) als de doelgroep kwetsbaar is (bijvoorbeeld kinderen of mensen met schulden) maar niet duidelijk is of het gedrag wezenlijk wordt verstoord of de schade aanzienlijk is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Buit de toepassing een kwetsbaarheid uit door leeftijd, handicap of sociale of economische situatie, met aanzienlijke schade (art. 5 lid 1 sub b)?
- Advies bij ❌ of ⚠️: Stop met deze toepassing en schakel een juridisch adviseur in. Het uitbuiten van kwetsbaarheden met AI is verboden.
- Bronnen: AIVO-art5-lid1-b (AI-verordening art. 5 lid 1 sub b); AIVO-overw29 (AI-verordening overweging 29); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI1.3 — Of de toepassing mensen een sociale score geeft
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen beoordeling of indeling van personen over een periode op basis van sociaal gedrag of bekende, afgeleide of voorspelde persoonlijke kenmerken, met een nadelige behandeling in een niet-verwante context of een ongerechtvaardigde of onevenredige nadelige behandeling
- Grondslag: art. 5 lid 1 sub c AI-verordening; overweging 31
- Beoordeeld op: de antwoorden
- Nodig: social_scoring, app_purpose
- Beoordeling:
  - present als social_scoring false is en app_purpose geen scoring van personen op gedrag of kenmerken beschrijft.
  - absent als social_scoring true is en social_scoring_description laat zien dat de score (i) leidt tot nadelige behandeling in een sociale context die geen verband houdt met de context waarin de gegevens zijn verzameld, of (ii) leidt tot een nadelige behandeling die ongerechtvaardigd of onevenredig is ten opzichte van het gedrag of de ernst daarvan.
  - twijfel (⚠️) als social_scoring true is maar de beschrijving ontbreekt of niet duidelijk maakt of de behandeling in een niet-verwante context plaatsvindt of onevenredig is; ook bij klantscores of 'trust scores' die meerdere diensten raken.
  - Een gebruikelijke kredietwaardigheidsbeoordeling die binnen haar eigen context blijft, is geen social scoring (maar wel een hoog-risicosignaal, AI2): dan present, mits social_scoring false is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Leidt de score tot een nadelige behandeling in een niet-verwante context, of tot een behandeling die onevenredig is ten opzichte van het gedrag (art. 5 lid 1 sub c)?
- Advies bij ❌ of ⚠️: Stop met het gebruik van de score voor nadelige beslissingen en schakel een juridisch adviseur in. Social scoring met AI is verboden.
- Bronnen: AIVO-art5-lid1-c (AI-verordening art. 5 lid 1 sub c); AIVO-overw31 (AI-verordening overweging 31); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI1.4 — Of de toepassing voorspelt wie een strafbaar feit gaat plegen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen risicobeoordeling van het plegen van strafbare feiten uitsluitend op basis van profilering of persoonlijkheidskenmerken (uitgezonderd: ondersteuning van een menselijke beoordeling die al op objectieve, verifieerbare feiten berust)
- Grondslag: art. 5 lid 1 sub d AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: crime_prediction, app_purpose
- Beoordeling:
  - present als crime_prediction false is.
  - absent als crime_prediction true is en app_purpose bevestigt dat de voorspelling uitsluitend op een profiel of persoonlijkheidskenmerken berust (zoals leeftijd, nationaliteit, woonplaats, persoonlijkheid).
  - twijfel (⚠️) als het systeem ook concrete feiten gebruikt, als een medewerker de beoordeling doet, of bij fraudedetectie over personen: de uitzondering voor ondersteuning van een menselijke beoordeling op objectieve, verifieerbare feiten moet een juridisch adviseur beoordelen.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Berust de risicobeoordeling uitsluitend op profilering of persoonlijkheidskenmerken, of ondersteunt zij een menselijke beoordeling op objectieve, verifieerbare feiten (art. 5 lid 1 sub d)?
- Advies bij ❌ of ⚠️: Stop met risicovoorspellingen over strafbare feiten die alleen op een profiel berusten en schakel een juridisch adviseur in.
- Bronnen: AIVO-art5-lid1-d (AI-verordening art. 5 lid 1 sub d); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI1.5 — Of de toepassing ongericht gezichtsfoto's verzamelt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen aanleg of uitbreiding van databanken voor gezichtsherkenning door ongerichte scraping van gezichtsbeelden van internet of camerabeelden
- Grondslag: art. 5 lid 1 sub e AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: face_scraping
- Beoordeling:
  - present als face_scraping false is.
  - absent als face_scraping true is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Stop met het verzamelen van gezichtsbeelden voor deze databank en verwijder de verzamelde beelden in overleg met een juridisch adviseur.
- Bronnen: AIVO-art5-lid1-e (AI-verordening art. 5 lid 1 sub e); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI1.6 — Of de toepassing emoties herkent op het werk of in het onderwijs
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen systemen die emoties of intenties afleiden uit biometrische gegevens van natuurlijke personen op de werkplek of in onderwijsinstellingen, behalve om medische of veiligheidsredenen
- Grondslag: art. 5 lid 1 sub f jo. art. 3 punt 39 AI-verordening; overwegingen 18 en 44
- Alleen als: `facts.emotion_inference != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: emotion_inference, emotion_data_basis, emotion_subjects
- Beoordeling:
  - Het verbod geldt alleen voor systemen die emoties of intenties afleiden uit biometrische gegevens (art. 3 punt 39). Emoties afleiden uit geschreven tekst valt buiten het verbod (richtsnoeren C(2025) 884). Fysieke toestanden als pijn of vermoeidheid zijn geen emoties (overweging 18).
  - absent (verboden) als emotion_data_basis biometric is, emotion_subjects employees, job_applicants of students is, en emotion_medical_or_safety false is. Sollicitatieprocedures vallen onder de werkplek (richtsnoeren).
  - emotion_subjects customers_and_employees met biometric en emotion_medical_or_safety false: absent, tenzij app_purpose laat zien dat de analyse van medewerkers technisch is uitgesloten (dan twijfel (⚠️)); de richtsnoeren vereisen dat geen medewerkers worden gevolgd.
  - twijfel (⚠️) als emotion_data_basis biometric is, emotion_subjects employees, job_applicants of students is, en emotion_medical_or_safety true is: de uitzondering is smal (algemene stress-, burn-out- of welzijnsmonitoring valt er niet onder) en moet door een juridisch adviseur worden beoordeeld.
  - twijfel (⚠️) als emotion_medical_or_safety onbekend is bij biometrische emotieherkenning van medewerkers, sollicitanten of leerlingen: ⚠️ (noem welk antwoord ontbreekt).
  - present als emotion_data_basis text_only is: buiten dit verbod. Ook art. 50 lid 3 en bijlage III punt 1 sub c gelden alleen voor systemen op basis van biometrische gegevens; de AVG blijft wel gelden.
  - present als emotion_subjects customers_or_public is én app_purpose niet laat zien dat ook medewerkers worden geanalyseerd (bijvoorbeeld stemanalyse van alleen de klant in een callcenter). Zie AI2 (bijlage III punt 1 sub c) en AI4 stap 4. Blijkt uit app_purpose dat ook medewerkers worden geanalyseerd, of is dat onduidelijk: twijfel (⚠️).
  - emotion_data_basis of emotion_subjects ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Leidt het systeem emoties af uit biometrische gegevens van medewerkers, sollicitanten of leerlingen, en valt het gebruik echt onder de smalle uitzondering voor medische of veiligheidsredenen (art. 5 lid 1 sub f)?
- Advies bij ❌ of ⚠️: Stop met emotieherkenning bij medewerkers, sollicitanten of leerlingen en schakel een juridisch adviseur in. Dit is een verboden AI-praktijk sinds 2 februari 2025, tenzij het uitsluitend om medische of veiligheidsredenen gebeurt.
- Bronnen: AIVO-art5-lid1-f (AI-verordening art. 5 lid 1 sub f); AIVO-art3-39 (AI-verordening art. 3 punt 39); AIVO-art3-34 (AI-verordening art. 3 punt 34); AIVO-overw18 (AI-verordening overweging 18); AIVO-overw44 (AI-verordening overweging 44); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI1.7 — Of de toepassing mensen indeelt naar ras, geloof of andere gevoelige kenmerken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen biometrische categorisering om ras, politieke opvattingen, vakbondslidmaatschap, religieuze of levensbeschouwelijke overtuigingen, seksleven of seksuele gerichtheid af te leiden (uitgezonderd: labelen of filteren van rechtmatig verkregen biometrische datasets en categorisering bij rechtshandhaving)
- Grondslag: art. 5 lid 1 sub g jo. art. 3 punt 40 AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: biometric_categorisation, app_purpose
- Beoordeling:
  - present als biometric_categorisation false is. Indelen naar andere kenmerken (bijvoorbeeld leeftijd of haarkleur voor een filter) valt niet onder dit verbod, maar kan wel een hoog-risicosignaal zijn (AI2).
  - absent als biometric_categorisation true is en app_purpose geen van de uitzonderingen beschrijft.
  - twijfel (⚠️) als app_purpose wijst op het labelen of filteren van rechtmatig verkregen biometrische datasets, of op rechtshandhaving.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Worden personen op basis van biometrische gegevens ingedeeld om een van de limitatief genoemde gevoelige kenmerken af te leiden, en geldt een uitzondering (art. 5 lid 1 sub g)?
- Advies bij ❌ of ⚠️: Stop met het indelen van mensen naar deze gevoelige kenmerken en schakel een juridisch adviseur in.
- Bronnen: AIVO-art5-lid1-g (AI-verordening art. 5 lid 1 sub g); AIVO-art3-40 (AI-verordening art. 3 punt 40); AIVO-art3-34 (AI-verordening art. 3 punt 34); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI1.8 — Of de toepassing voor politie of justitie live mensen herkent op straat
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen biometrische systemen voor realtime identificatie op afstand in openbaar toegankelijke ruimten met het oog op rechtshandhaving, buiten de strikt omschreven uitzonderingen
- Grondslag: art. 5 lid 1 sub h jo. art. 3 punt 44 AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: realtime_rbi_law_enforcement
- Beoordeling:
  - present als realtime_rbi_law_enforcement false is. Gezichtsherkenning buiten rechtshandhaving valt niet onder dit verbod (wel onder art. 9 AVG, art. 29 UAVG en mogelijk bijlage III punt 1, zie AI2).
  - twijfel (⚠️) als realtime_rbi_law_enforcement true is: de uitzonderingen (slachtoffers zoeken, dreiging afwenden, verdachten van zware misdrijven) vereisen een wettelijke basis en voorafgaande toestemming; altijd een juridisch adviseur.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is er een wettelijke basis en voorafgaande toestemming, en valt het gebruik onder een van de uitzonderingen van art. 5 lid 1 sub h?
- Advies bij ❌ of ⚠️: Laat een juridisch adviseur beoordelen of een van de strikte uitzonderingen geldt, met de vereiste wettelijke basis en toestemming vooraf.
- Bronnen: AIVO-art5-lid1-h (AI-verordening art. 5 lid 1 sub h); AIVO-art3-44 (AI-verordening art. 3 punt 44); EC-C-2025-884 (Richtsnoeren van de Commissie over verboden praktijken op het gebied van artificiële intelligentie, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI1.9 — Of de toepassing naakt- of seksuele beelden van echte personen kan maken (verbod vanaf 2 december 2026)
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen AI-systemen die zonder toestemming realistische intieme beelden van herkenbare personen genereren of bewerken, of kindermisbruikmateriaal genereren (verbod vanaf 2 december 2026)
- Grondslag: art. 5 lid 1 sub ba en bb, lid 1a en 1b AI-verordening (ingevoegd bij Verordening (EU) 2026/1744); art. 113
- Geldt vanaf: 2026-12-02 — art. 113, derde alinea, onder a, zoals gewijzigd bij Verordening (EU) 2026/1744
- Alleen als: `facts.generates_intimate_content != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: generates_intimate_content, app_purpose
- Beoordeling:
  - Deze verboden zijn pas van toepassing vanaf 2 december 2026 (zie 'Geldt vanaf'). Tot die datum wordt een ❌ een ⚠️ (voorbereidingspunt); vermeld de datum in de onderbouwing.
  - Voor de aanbieder geldt het verbod als het genereren van zulk materiaal het beoogde doel is, of een redelijkerwijs voorzienbare en reproduceerbare uitkomst zonder adequate waarborgen (lid 1a). Voor de gebruiksverantwoordelijke geldt het bij het daadwerkelijk genereren of bewerken.
  - Het maken en verspreiden van zulk materiaal is nu al strafbaar naar Nederlands strafrecht (art. 139h Sr: seksueel beeldmateriaal van een persoon zonder toestemming, ook deepfakes; art. 252 Sr: afbeeldingen van seksuele handelingen met kinderen): verwijs altijd direct naar een juridisch adviseur.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Is het genereren van intieme beelden zonder toestemming of van kindermisbruikmateriaal het doel of een voorzienbare uitkomst zonder adequate waarborgen, en welk strafrecht is nu al van toepassing?
- Advies bij ❌ of ⚠️: Stop met dit gebruik en schakel direct een juridisch adviseur in. Vanaf 2 december 2026 is dit een verboden AI-praktijk; het maken en verspreiden van zulk materiaal is nu al strafbaar.
- Bronnen: AIVO-art5-lid1-ba (AI-verordening art. 5 lid 1 sub ba); AIVO-art5-lid1-bb (AI-verordening art. 5 lid 1 sub bb); AIVO-art5-lid1a (AI-verordening art. 5 lid 1a); AIVO-art5-lid1b (AI-verordening art. 5 lid 1b); AIVO-art113 (AI-verordening art. 113); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): app_purpose. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Duidelijk geen van de verboden → compliant voor deze toetspunten.
- Emotieherkenning uit tekst of alleen bij klanten → stap 6 compliant, maar route naar AI2 en AI4 (samenloop).

## Samenhang met andere kaders

- Kader K14 (/toets-cameratoezicht) — als `facts.emotion_inference == true and facts.emotion_data_basis == "biometric"`: Emotieherkenning met camera's of stemopnames raakt ook het cameratoezicht en de bijzondere persoonsgegevens (AVG).
- Kader K3 (/toets-grondslag) — als `facts.biometric_categorisation != false or facts.emotion_data_basis == "biometric"`: Biometrische gegevens zijn bijzondere persoonsgegevens (art. 9 AVG, art. 29 UAVG).
- Kader AI2 (/toets-ai-act-basis) — als `facts.emotion_inference == true and facts.emotion_subjects == "customers_or_public"`: Emotieherkenning buiten werk en onderwijs is niet verboden, maar kan hoog risico zijn (bijlage III punt 1 sub c).
- Kader AI4 (/toets-ai-act-basis) — als `facts.emotion_inference == true or facts.biometric_categorisation == true`: Wie emotieherkenning of biometrische categorisering gebruikt, moet de betrokkenen informeren (art. 50 lid 3).

## Open punten en voorbehouden

- Nationale boetes en toezichthouders volgen uit de Uitvoeringswet AI-verordening (wetsvoorstel, nog niet in werking).
