# Kader AI4 — Transparantie (art. 50)

Versie 0.4 · peildatum 2026-11-10

Doel: Controleren of mensen worden geïnformeerd wanneer art. 50 AI-verordening dat vereist: bij systemen die rechtstreeks met mensen communiceren, bij synthetische inhoud, bij emotieherkenning en biometrische categorisering, bij deepfakes en bij AI-tekst over zaken van algemeen belang. Van toepassing sinds 2 augustus 2026.

Geldt alleen als: `facts.system_infers != false` · poortstap AI0.1 — vervalt als de toepassing duidelijk geen AI-systeem is (regel van kader AI0)

Bronnen: AIVO-art3-3 (AI-verordening art. 3 punt 3); AIVO-art3-4 (AI-verordening art. 3 punt 4); AIVO-art3-60 (AI-verordening art. 3 punt 60); AIVO-art50-lid1 (AI-verordening art. 50 lid 1); AIVO-art50-lid2 (AI-verordening art. 50 lid 2); AIVO-art50-lid3 (AI-verordening art. 50 lid 3); AIVO-art50-lid4 (AI-verordening art. 50 lid 4); AIVO-art50-lid5 (AI-verordening art. 50 lid 5); AIVO-art99-lid4-g (AI-verordening art. 99 lid 4 sub g); AIVO-art111-lid4 (AI-verordening art. 111 lid 4); AIVO-overw132 (AI-verordening overweging 132); AIVO-overw133 (AI-verordening overweging 133); AIVO-overw134 (AI-verordening overweging 134); EC-richtsnoeren-art50-2026 (Richtsnoeren van de Commissie over transparantieverplichtingen voor aanbieders en gebruiksverantwoordelijken van bepaalde AI-systemen (art. 50 AI-verordening)); EC-gedragscode-labelen-2026 (Gedragscode over het markeren en labelen van door AI gegenereerde inhoud (Code of Practice on marking and labelling of AI-generated content)); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

## Formulier (vragen aan de gebruiker)

- **app_purpose**: Waarvoor gebruik je de toepassing, wat maakt of doet zij, en wie krijgt de uitkomst te zien?
  - Label (voor de plek-om-in-te-vullen): waarvoor en bij wie je de toepassing gebruikt
  - Hulp: Overgenomen uit de eerste vragen over deze toepassing. Vul aan: bijvoorbeeld 'beelden voor onze social media', 'nieuwsberichten op onze website' of 'stemanalyse van bellers'.
  - Type: text
- **ai_role**: Ben je aanbieder van deze toepassing, of gebruik je een toepassing van een ander?
  - Label (voor de plek-om-in-te-vullen): je rol bij deze toepassing
  - Hulp: Overgenomen uit de vragen over de rol. Aanbieder ben je als je de toepassing zelf hebt gebouwd of laten bouwen (ook op een AI-model van een ander) en onder je eigen naam gebruikt of aanbiedt.
  - Type: enum (provider / deployer)
- **interacts_with_people**: Communiceert de toepassing rechtstreeks met mensen, zoals een chatbot, spraakassistent of AI-agent die namens jou berichten stuurt of gesprekken voert?
  - Label (voor de plek-om-in-te-vullen): of de toepassing rechtstreeks met mensen communiceert
  - Hulp: Het gaat om contact met klanten, bezoekers, sollicitanten of andere mensen. Een tool die alleen je eigen medewerkers helpen teksten te schrijven, communiceert niet zelf met anderen.
  - Type: boolean
- **interaction_disclosed**: Krijgen mensen uiterlijk bij het eerste contact duidelijk te zien of te horen dat ze met AI communiceren, en bij een AI-agent ook namens wie hij handelt?
  - Label (voor de plek-om-in-te-vullen): of mensen horen of zien dat ze met AI communiceren
  - Hulp: Bijvoorbeeld 'Je chat met onze digitale assistent (AI)' boven in het chatvenster. Alleen een vermelding in de algemene voorwaarden of de privacyverklaring is niet genoeg.
  - Type: boolean · Alleen vragen als: `facts.interacts_with_people != false`
- **interaction_context**: Hoe komen mensen met de toepassing in contact, en wat zien of horen zij daarbij?
  - Label (voor de plek-om-in-te-vullen): hoe het contact met de toepassing verloopt
  - Hulp: Bijvoorbeeld: 'Chatvenster rechtsonder op de website met de naam Sanne en een foto' of 'Robotstem die de telefoon opneemt'.
  - Type: text · Alleen vragen als: `facts.interacts_with_people != false`
- **generates_synthetic_content**: Maakt de toepassing zelf tekst, beelden, geluid of video?
  - Label (voor de plek-om-in-te-vullen): of de toepassing tekst, beeld, geluid of video maakt
  - Type: boolean
- **output_marked**: Krijgt de inhoud die de toepassing maakt een technische markering (bijvoorbeeld een watermerk of metadata) waaraan software kan zien dat het door AI is gemaakt?
  - Label (voor de plek-om-in-te-vullen): of de gemaakte inhoud machineleesbaar als AI-inhoud is gemarkeerd
  - Hulp: Dit is een plicht voor de aanbieder van de toepassing, ook voor tekst (bijvoorbeeld de antwoorden van een eigen chatbot). Heb je de toepassing zelf gebouwd op een AI-model van een ander, dan moet je nagaan of dat model of jouw eigen toepassing deze markering toevoegt.
  - Type: boolean · Alleen vragen als: `facts.generates_synthetic_content != false and facts.ai_role != "deployer"`
- **assistive_editing_only**: Doet de toepassing alleen gewone bewerkingen van inhoud die mensen zelf aanleveren (zoals spelling verbeteren of een foto bijsnijden), zonder de inhoud of betekenis wezenlijk te veranderen?
  - Label (voor de plek-om-in-te-vullen): of de toepassing alleen bestaande inhoud licht bewerkt
  - Type: boolean · Alleen vragen als: `facts.generates_synthetic_content != false and facts.ai_role != "deployer"`
- **on_market_before_aug2026**: Was de toepassing al vóór 2 augustus 2026 op de markt of in gebruik?
  - Label (voor de plek-om-in-te-vullen): of de toepassing al vóór 2 augustus 2026 in de handel of in gebruik was
  - Type: boolean · Alleen vragen als: `facts.generates_synthetic_content != false and facts.ai_role != "deployer"`
- **uses_emotion_or_biocat**: Gebruik je de toepassing om emoties van mensen te herkennen aan hun gezicht, stem of lichaam, of om mensen op basis van lichaamskenmerken in te delen?
  - Label (voor de plek-om-in-te-vullen): of je emotieherkenning of biometrische categorisering gebruikt
  - Hulp: Bijvoorbeeld stemanalyse die de stemming van bellers meet, of een camera die bezoekers naar leeftijd of geslacht indeelt. Analyse van alleen geschreven tekst telt hier niet.
  - Type: boolean
- **emotion_notice**: Worden de mensen bij wie je dit gebruikt vooraf geïnformeerd dat het systeem werkt?
  - Label (voor de plek-om-in-te-vullen): of mensen worden geïnformeerd over de emotieherkenning of indeling
  - Type: boolean · Alleen vragen als: `facts.uses_emotion_or_biocat != false`
- **makes_deepfakes**: Maak of bewerk je met deze toepassing beelden, geluid of video die lijken op echte personen, voorwerpen, plaatsen of gebeurtenissen en die voor echt kunnen worden aangezien?
  - Label (voor de plek-om-in-te-vullen): of je met AI realistische beelden, geluid of video maakt van bestaande personen, plaatsen of gebeurtenissen
  - Hulp: Bijvoorbeeld een video waarin je directeur met een AI-stem iets zegt wat hij niet echt heeft ingesproken, of een realistische foto van een gebeurtenis die niet heeft plaatsgevonden. Een duidelijk getekende of fantasievolle afbeelding telt niet. Verspreid je alleen materiaal dat een ander heeft gemaakt, dan geldt deze plicht niet voor jou.
  - Type: boolean
- **deepfake_disclosed**: Vermeld je bij deze inhoud dat die met AI is gemaakt of bewerkt?
  - Label (voor de plek-om-in-te-vullen): of je vermeldt dat de inhoud met AI is gemaakt of bewerkt
  - Type: boolean · Alleen vragen als: `facts.makes_deepfakes != false`
- **deepfake_artistic**: Is de inhoud duidelijk artistiek, creatief, satirisch of fictief, zodat iedereen begrijpt dat het niet echt is bedoeld?
  - Label (voor de plek-om-in-te-vullen): of het gaat om duidelijk artistiek, satirisch of fictief werk
  - Type: boolean · Alleen vragen als: `facts.makes_deepfakes != false`
- **publishes_ai_text_public_interest**: Publiceer je met AI gemaakte of bewerkte tekst om het publiek te informeren over zaken van algemeen belang, zoals nieuws, politiek, gezondheid of maatschappelijke onderwerpen?
  - Label (voor de plek-om-in-te-vullen): of je met AI gemaakte tekst publiceert over zaken van algemeen belang
  - Hulp: Productteksten, marketing of een blog over je eigen diensten tellen meestal niet. Een nieuwsbericht of een artikel over een maatschappelijk onderwerp wel.
  - Type: boolean
- **text_disclosed**: Vermeld je bij die tekst dat die met AI is gemaakt of bewerkt?
  - Label (voor de plek-om-in-te-vullen): of je bij die tekst vermeldt dat AI is gebruikt
  - Type: boolean · Alleen vragen als: `facts.publishes_ai_text_public_interest != false`
- **text_human_editorial**: Wordt de tekst vóór publicatie door een mens gecontroleerd of geredigeerd, én is een persoon of je organisatie redactioneel verantwoordelijk voor de publicatie?
  - Label (voor de plek-om-in-te-vullen): of een mens de tekst controleert en iemand er redactioneel verantwoordelijk voor is
  - Type: boolean · Alleen vragen als: `facts.publishes_ai_text_public_interest != false`
- **disclosure_description**: Hoe en wanneer laat je mensen weten dat AI is gebruikt? Beschrijf de tekst en de plek van de melding.
  - Label (voor de plek-om-in-te-vullen): hoe en wanneer je de melding geeft
  - Hulp: Bijvoorbeeld: 'In het chatvenster staat vóór het eerste bericht: Je praat met een AI-assistent' of 'Onder elke video staat: Deze video is gemaakt met AI'.
  - Type: text · Alleen vragen als: `facts.interaction_disclosed == true or facts.emotion_notice == true or facts.deepfake_disclosed == true or facts.text_disclosed == true`

## Toetspunten

### AI4.1 — Of mensen weten dat ze met AI praten (je bent aanbieder)
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De aanbieder zorgt dat een AI-systeem dat rechtstreeks met mensen communiceert zo is ontworpen dat zij weten dat zij met een AI-systeem communiceren, tenzij dat evident is
- Grondslag: art. 50 lid 1 AI-verordening
- Alleen als: `facts.interacts_with_people != false and facts.ai_role != "deployer"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: ai_role, interacts_with_people, interaction_disclosed
- Beoordeling:
  - present als interaction_disclosed true is en interaction_context of disclosure_description dit bevestigt of niet tegenspreekt.
  - absent als interaction_disclosed false is en interaction_context niet laat zien dat het voor een normaal geïnformeerde, oplettende en omzichtige persoon evident is dat het om AI gaat (een menselijke naam of foto maakt het juist niet evident).
  - twijfel (⚠️) als interaction_disclosed false is maar de organisatie stelt dat het evident is; of als de melding alleen in algemene voorwaarden of een privacyverklaring staat; of bij een AI-agent als niet wordt vermeld namens wie hij handelt (richtsnoeren art. 50).
  - ai_role onbekend of interaction_disclosed ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het voor een normaal geïnformeerde, oplettende en omzichtige persoon evident dat hij met een AI-systeem communiceert, of wordt dit duidelijk gemeld?
- Advies bij ❌ of ⚠️: Laat bij het eerste contact duidelijk zien of horen dat mensen met AI communiceren, bijvoorbeeld 'Je chat met onze AI-assistent'. Gebruik je een AI-agent die namens jou berichten stuurt, vermeld dan ook namens wie hij handelt.
- Bronnen: AIVO-art50-lid1 (AI-verordening art. 50 lid 1); AIVO-art3-3 (AI-verordening art. 3 punt 3); AIVO-overw132 (AI-verordening overweging 132); EC-richtsnoeren-art50-2026 (Richtsnoeren van de Commissie over transparantieverplichtingen voor aanbieders en gebruiksverantwoordelijken van bepaalde AI-systemen (art. 50 AI-verordening))

### AI4.2 — Of de chatbot of agent van je leverancier meldt dat het AI is
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Bij een systeem van een leverancier dat rechtstreeks met mensen communiceert: het systeem meldt dat het AI is (de plicht van art. 50 lid 1 ligt bij de aanbieder)
- Grondslag: art. 50 lid 1 jo. art. 3 punt 4 AI-verordening
- Alleen als: `facts.interacts_with_people != false and facts.ai_role != "provider"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: ai_role, interacts_with_people, interaction_disclosed
- Beoordeling:
  - present als interaction_disclosed true is.
  - absent als interaction_disclosed false is: de wettelijke plicht ligt bij de aanbieder, dus geen non_compliant voor de gebruiksverantwoordelijke, maar review: spreek de leverancier aan en controleer of de organisatie door eigen instellingen of een eigen naam zelf aanbieder is geworden (AI0 stap 3).
  - ai_role onbekend (rol niet vastgesteld) of interaction_disclosed ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Meldt het systeem van de leverancier dat mensen met AI communiceren, en is de organisatie door configuratie of eigen naam mogelijk zelf aanbieder?
- Advies bij ❌ of ⚠️: Vraag je leverancier om de chatbot of agent bij het eerste contact te laten melden dat het AI is, of zet die melding zelf in het venster. Controleer of je door eigen instellingen of een eigen naam niet zelf aanbieder bent.
- Bronnen: AIVO-art50-lid1 (AI-verordening art. 50 lid 1); AIVO-art3-4 (AI-verordening art. 3 punt 4); EC-richtsnoeren-art50-2026 (Richtsnoeren van de Commissie over transparantieverplichtingen voor aanbieders en gebruiksverantwoordelijken van bepaalde AI-systemen (art. 50 AI-verordening))

### AI4.3 — Of AI-inhoud technisch als AI-inhoud herkenbaar is (je bent aanbieder)
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De aanbieder van een AI-systeem dat synthetische audio, beelden, video of tekst genereert, zorgt dat de output machineleesbaar is gemarkeerd en als kunstmatig gegenereerd of bewerkt detecteerbaar is (niet bij alleen ondersteunende standaardbewerking)
- Grondslag: art. 50 lid 2 en art. 111 lid 4 AI-verordening (zoals gewijzigd bij Verordening (EU) 2026/1744)
- Geldt vanaf: 2026-12-02 als `facts.on_market_before_aug2026 == true`; 2026-08-02 — art. 111 lid 4 (overgangstermijn voor systemen die vóór 2 augustus 2026 in de handel waren) en art. 113
- Alleen als: `facts.generates_synthetic_content != false and facts.ai_role != "deployer"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: ai_role, generates_synthetic_content, output_marked, app_purpose
- Beoordeling:
  - Dit geldt ook voor een organisatie die een eigen chatbot of tool op een AI-model van een ander heeft gebouwd: zij is aanbieder van het AI-systeem. Voegt het onderliggende model al een markering toe die behouden blijft, dan kan dat volstaan.
  - present als output_marked true is.
  - present als assistive_editing_only true is en de omschrijving bevestigt dat alleen standaardbewerkingen worden gedaan zonder wezenlijke wijziging van de inhoud of de betekenis (uitzondering lid 2).
  - absent als output_marked false en assistive_editing_only false is. Was het systeem vóór 2 augustus 2026 in de handel (on_market_before_aug2026 true), dan geldt de plicht pas vanaf 2 december 2026 en wordt een ❌ tot die datum een ⚠️ met de datum; is dat onbekend, dan ook ⚠️ (zie 'Geldt vanaf').
  - Er is geen uitzondering voor chatantwoorden of andere tekst. Wel hoeven de technische oplossingen alleen te werken voor zover dat technisch haalbaar is, rekening houdend met de beperkingen van het soort inhoud (lid 2, tweede zin); de vrijwillige gedragscode zondert korte teksten (minder dan ongeveer 200 tokens) uit van watermerken, maar geeft geen vermoeden van conformiteit. Daarom: twijfel (⚠️) als output_marked false is en app_purpose laat zien dat de output (vrijwel) alleen uit korte tekstantwoorden bestaat (bijvoorbeeld een chatbot); een juridisch adviseur beoordeelt het beroep op technische haalbaarheid.
  - ai_role onbekend of output_marked ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt). output_marked false en assistive_editing_only ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de output machineleesbaar gemarkeerd, geldt de uitzondering voor ondersteunende bewerking, of loopt de overgangstermijn tot 2 december 2026 nog?
- Advies bij ❌ of ⚠️: Zorg dat tekst, beeld, geluid of video uit je toepassing een machineleesbare markering krijgt (bijvoorbeeld metadata of een watermerk). Ga na of het AI-model dat je gebruikt dit al doet en of de markering behouden blijft. De gedragscode van de Commissie over markeren en labelen geeft praktische voorbeelden.
- Bronnen: AIVO-art50-lid2 (AI-verordening art. 50 lid 2); AIVO-art111-lid4 (AI-verordening art. 111 lid 4); AIVO-overw133 (AI-verordening overweging 133); EC-gedragscode-labelen-2026 (Gedragscode over het markeren en labelen van door AI gegenereerde inhoud (Code of Practice on marking and labelling of AI-generated content)); EC-richtsnoeren-art50-2026 (Richtsnoeren van de Commissie over transparantieverplichtingen voor aanbieders en gebruiksverantwoordelijken van bepaalde AI-systemen (art. 50 AI-verordening)); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI4.4 — Of mensen weten dat hun emoties worden herkend of dat ze worden ingedeeld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De gebruiksverantwoordelijke van een emotieherkenningssysteem of een systeem voor biometrische categorisering informeert de natuurlijke personen die eraan worden blootgesteld over de werking van het systeem
- Grondslag: art. 50 lid 3 AI-verordening
- Alleen als: `facts.uses_emotion_or_biocat != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: uses_emotion_or_biocat, emotion_notice
- Beoordeling:
  - present als emotion_notice true is.
  - absent als emotion_notice false is.
  - Deze stap beoordeelt alleen de meldplicht. Of het gebruik zelf is toegestaan, toetst AI1 (verboden op het werk en in het onderwijs) en AI2 (hoog risico); de verwerking van biometrische gegevens toetst K3.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Informeer de mensen bij wie je emotieherkenning of biometrische indeling gebruikt, vóórdat het systeem hen analyseert, bijvoorbeeld met een duidelijke melding aan het begin van het gesprek of bij de ingang.
- Bronnen: AIVO-art50-lid3 (AI-verordening art. 50 lid 3); AIVO-overw132 (AI-verordening overweging 132); EC-richtsnoeren-art50-2026 (Richtsnoeren van de Commissie over transparantieverplichtingen voor aanbieders en gebruiksverantwoordelijken van bepaalde AI-systemen (art. 50 AI-verordening))

### AI4.5 — Of je vermeldt dat realistische beelden, geluid of video met AI zijn gemaakt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De gebruiksverantwoordelijke van een AI-systeem dat deepfakes genereert of bewerkt, maakt bekend dat de inhoud kunstmatig is gegenereerd of bewerkt; bij evident artistiek, creatief, satirisch of fictief werk volstaat een passende vermelding die de weergave niet hindert
- Grondslag: art. 50 lid 4, eerste alinea, jo. art. 3 punt 60 AI-verordening
- Alleen als: `facts.makes_deepfakes != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: makes_deepfakes, deepfake_disclosed, app_purpose
- Beoordeling:
  - Een deepfake is door AI gegenereerd of bewerkt beeld-, audio- of videomateriaal dat lijkt op bestaande personen, voorwerpen, plaatsen, entiteiten of gebeurtenissen en ten onrechte echt of waarheidsgetrouw zou lijken (art. 3 punt 60). Tekst valt hier niet onder (zie stap 6). Wie alleen verspreidt wat een ander heeft gemaakt, valt niet onder deze plicht.
  - present als deepfake_disclosed true is.
  - present als deepfake_artistic true is en disclosure_description een passende vermelding beschrijft die de weergave niet hindert.
  - absent als deepfake_disclosed false is en deepfake_artistic false is.
  - twijfel (⚠️) als deepfake_disclosed false is en deepfake_artistic true of onbekend is (ook bij evident artistiek werk is een vermelding nodig, maar een lichtere); of als twijfelachtig is of het publiek de inhoud voor echt zou houden.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de inhoud een deepfake in de zin van art. 3 punt 60, en is de vermelding passend (ook bij evident artistiek, satirisch of fictief werk)?
- Advies bij ❌ of ⚠️: Vermeld duidelijk bij de beelden, het geluid of de video dat die met AI zijn gemaakt of bewerkt, bijvoorbeeld 'Deze video is gemaakt met AI'. Bij duidelijk artistiek of satirisch werk volstaat een vermelding die het werk niet verstoort, zoals in de aftiteling.
- Bronnen: AIVO-art50-lid4 (AI-verordening art. 50 lid 4); AIVO-art3-60 (AI-verordening art. 3 punt 60); AIVO-overw134 (AI-verordening overweging 134); EC-richtsnoeren-art50-2026 (Richtsnoeren van de Commissie over transparantieverplichtingen voor aanbieders en gebruiksverantwoordelijken van bepaalde AI-systemen (art. 50 AI-verordening)); EC-gedragscode-labelen-2026 (Gedragscode over het markeren en labelen van door AI gegenereerde inhoud (Code of Practice on marking and labelling of AI-generated content))

### AI4.6 — Of je vermeldt dat een tekst over een maatschappelijk onderwerp met AI is gemaakt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De gebruiksverantwoordelijke van een AI-systeem dat tekst genereert of bewerkt die wordt gepubliceerd om het publiek te informeren over aangelegenheden van algemeen belang, maakt bekend dat de tekst kunstmatig is gegenereerd of bewerkt, tenzij de tekst menselijke controle of redactie heeft ondergaan én een natuurlijke of rechtspersoon de redactionele verantwoordelijkheid draagt
- Grondslag: art. 50 lid 4, tweede alinea, AI-verordening
- Alleen als: `facts.publishes_ai_text_public_interest != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: publishes_ai_text_public_interest, app_purpose
- Beoordeling:
  - present als text_disclosed true is.
  - present als text_human_editorial true is: menselijke controle of redactie én redactionele verantwoordelijkheid (beide voorwaarden zijn nodig; de vraag dekt beide).
  - absent als text_disclosed false en text_human_editorial false is.
  - twijfel (⚠️) als twijfelachtig is of de tekst over een zaak van algemeen belang gaat (bijvoorbeeld een blog van een bedrijf over een maatschappelijk thema), of als de menselijke controle alleen vluchtig is.
  - Ontbrekend of 'weet ik niet' bij text_disclosed of text_human_editorial terwijl de ander niet true is: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Gaat de tekst over een aangelegenheid van algemeen belang, en is er menselijke controle of redactie én redactionele verantwoordelijkheid?
- Advies bij ❌ of ⚠️: Vermeld bij de tekst dat die met AI is gemaakt of bewerkt, of laat elke tekst vóór publicatie door een redacteur controleren en wijs iemand aan die redactioneel verantwoordelijk is.
- Bronnen: AIVO-art50-lid4 (AI-verordening art. 50 lid 4); AIVO-overw134 (AI-verordening overweging 134); EC-richtsnoeren-art50-2026 (Richtsnoeren van de Commissie over transparantieverplichtingen voor aanbieders en gebruiksverantwoordelijken van bepaalde AI-systemen (art. 50 AI-verordening)); EC-gedragscode-labelen-2026 (Gedragscode over het markeren en labelen van door AI gegenereerde inhoud (Code of Practice on marking and labelling of AI-generated content))

### AI4.7 — Of de melding duidelijk is en op tijd komt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De informatie wordt op duidelijke en herkenbare wijze verstrekt, uiterlijk bij de eerste interactie of blootstelling, en voldoet aan de toegankelijkheidseisen
- Grondslag: art. 50 lid 5 AI-verordening
- Alleen als: `facts.interaction_disclosed == true or facts.emotion_notice == true or facts.deepfake_disclosed == true or facts.text_disclosed == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: disclosure_description
- Beoordeling:
  - present als disclosure_description een melding beschrijft die zichtbaar of hoorbaar is vóór of bij het eerste contact of de eerste blootstelling, in begrijpelijke taal, op de plek zelf (in het chatvenster, bij het beeld, aan het begin van het gesprek).
  - absent als de melding alleen in algemene voorwaarden, een privacyverklaring of op een aparte pagina staat, of pas na het contact of de blootstelling komt.
  - twijfel (⚠️) in andere gevallen, onder meer als de toegankelijkheid onduidelijk is (bijvoorbeeld alleen een visuele melding bij een telefoonassistent) of bij een vermelding pas in de aftiteling van een evident artistiek werk.
  - Ontbrekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de melding duidelijk, herkenbaar, tijdig (uiterlijk bij de eerste interactie of blootstelling) en toegankelijk?
- Advies bij ❌ of ⚠️: Geef de melding op de plek zelf en vóór of bij het eerste contact, in gewone taal, en zo dat ook mensen met een beperking haar kunnen waarnemen (bijvoorbeeld tekst én gesproken melding bij een telefoonassistent).
- Bronnen: AIVO-art50-lid5 (AI-verordening art. 50 lid 5); EC-richtsnoeren-art50-2026 (Richtsnoeren van de Commissie over transparantieverplichtingen voor aanbieders en gebruiksverantwoordelijken van bepaalde AI-systemen (art. 50 AI-verordening))

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): app_purpose, disclosure_description. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 2 is niet verplicht: bij een systeem van een leverancier ligt de plicht bij de aanbieder → review, geen non_compliant.
- Rol onbekend (ai_role onbekend) → stap 1, 2 en 3 gelden en eindigen in review.
- Overgangstermijn art. 50 lid 2 nog lopend (vóór 2-12-2026, systeem vóór 2-8-2026 in de handel) → stap 3 review met datum. De rekenhulp past dit toe via 'Geldt vanaf' en stopt er vanzelf mee na 2-12-2026.
- Stap 7 is een F-stap: een melding die alleen in voorwaarden of een privacyverklaring staat, of te laat komt, is non_compliant en werkt door in de kaderuitkomst.

## Samenhang met andere kaders

- Kader AI1 (/toets-ai-act-basis) — als `facts.uses_emotion_or_biocat != false`: Emotieherkenning op het werk of in het onderwijs en biometrische categorisering naar gevoelige kenmerken zijn verboden.
- Kader K3 (/toets-grondslag) — als `facts.uses_emotion_or_biocat != false`: Biometrische gegevens zijn bijzondere persoonsgegevens (art. 9 AVG, art. 29 UAVG).
- Kader K5 (/privacyverklaring) — als `facts.interacts_with_people == true`: Verwerkt de chatbot of agent persoonsgegevens, dan moet ook de privacyverklaring dit gebruik noemen.

## Open punten en voorbehouden

- Na 2-12-2026 heeft de vraag on_market_before_aug2026 geen gevolg meer voor stap 3; bij de eerstvolgende inhoudelijke herziening kan zij vervallen.
- Gedragscode markeren en labelen (10-6-2026) is vrijwillig en geeft na de wijziging van art. 50 lid 7 geen vermoeden van conformiteit; alleen als praktijkvoorbeeld gebruiken.
- Rolafleiding: bij een eigen assistent binnen een leveranciersplatform (AI0 stap 3 review) blijft ai_role onbekend; overwegen om beide rollen te toetsen.
