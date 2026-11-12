# Kader AI3 — AI-geletterdheid (art. 4)

Versie 0.3 · peildatum 2026-11-10

Doel: Controleren of de organisatie maatregelen neemt om de AI-geletterdheid te ondersteunen van haar personeel en van anderen die namens haar AI-systemen bedienen en gebruiken, afgestemd op hun kennis, ervaring, opleiding en de context waarin de systemen worden gebruikt (art. 4 AI-verordening).

Bronnen: AIVO-art3-56 (AI-verordening art. 3 punt 56); AIVO-art4 (AI-verordening art. 4); AIVO-overw20 (AI-verordening overweging 20); EC-QA-AI-geletterdheid (Vragen en antwoorden van de Europese Commissie over AI-geletterdheid (art. 4 AI-verordening)); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

## Formulier (vragen aan de gebruiker)

- **uses_ai_systems**: Gebruikt of ontwikkelt je organisatie AI-systemen, zoals ChatGPT, Copilot, een chatbot of AI in HR-, klantenservice- of boekhoudsoftware?
  - Label (voor de plek-om-in-te-vullen): of je organisatie AI-systemen gebruikt of ontwikkelt
  - Hulp: Ook als medewerkers het op eigen initiatief voor hun werk gebruiken.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **ai_inventory**: Heb je een overzicht van welke AI-systemen er in je organisatie worden gebruikt, door wie en waarvoor?
  - Label (voor de plek-om-in-te-vullen): of je een overzicht hebt van de AI-systemen in je organisatie
  - Hulp:
  - Type: boolean · Alleen vragen als: `facts.uses_ai_systems != false`
- **literacy_measures**: Heb je maatregelen genomen zodat mensen verstandig met AI kunnen werken?
  - Label (voor de plek-om-in-te-vullen): of je maatregelen voor AI-geletterdheid hebt genomen
  - Hulp: Bijvoorbeeld een instructie of training, gebruiksregels (wat mag wel en niet in een AI-tool), een aanspreekpunt voor vragen, of uitleg bij de invoering van een nieuwe tool. Een certificaat is niet verplicht.
  - Type: boolean · Alleen vragen als: `facts.uses_ai_systems != false`
- **literacy_measures_description**: Welke maatregelen heb je genomen, en voor wie? Heb je niets gedaan, schrijf dan 'geen'.
  - Label (voor de plek-om-in-te-vullen): welke maatregelen je hebt genomen
  - Hulp: Bijvoorbeeld: 'Alle medewerkers kregen in maart een workshop van twee uur; er zijn gebruiksregels op het intranet; HR kreeg een extra training over AI bij werving.' Ook een korte instructie of een afspraak over wat wel en niet mag telt mee.
  - Type: text · Alleen vragen als: `facts.uses_ai_systems != false`
- **high_impact_use**: Gebruiken medewerkers AI bij beslissingen of beoordelingen over mensen, zoals sollicitanten, medewerkers, klanten of leerlingen?
  - Label (voor de plek-om-in-te-vullen): of AI wordt gebruikt bij beslissingen over mensen
  - Type: boolean · Alleen vragen als: `facts.uses_ai_systems != false`
- **measures_differentiated**: Krijgen mensen die AI gebruiken voor belangrijkere taken (bijvoorbeeld beslissingen over mensen) meer of andere uitleg dan mensen die AI alleen voor eenvoudige taken gebruiken?
  - Label (voor de plek-om-in-te-vullen): of de maatregelen zijn afgestemd op wat mensen met AI doen
  - Type: boolean · Alleen vragen als: `facts.literacy_measures != false`
- **external_users**: Werken er ook mensen van buiten je organisatie namens jou met AI-systemen, zoals uitzendkrachten, freelancers of een ingehuurde dienstverlener?
  - Label (voor de plek-om-in-te-vullen): of externen namens jou met AI werken
  - Type: boolean · Alleen vragen als: `facts.uses_ai_systems != false`
- **externals_covered**: Gelden de maatregelen ook voor die externen, bijvoorbeeld doordat zij dezelfde instructie krijgen of doordat je dit met hun werkgever of opdrachtnemer hebt afgesproken?
  - Label (voor de plek-om-in-te-vullen): of de maatregelen ook voor externen gelden
  - Type: boolean · Alleen vragen als: `facts.external_users != false`
- **measures_documented**: Leg je vast welke maatregelen je hebt genomen, voor wie en wanneer?
  - Label (voor de plek-om-in-te-vullen): of je de maatregelen vastlegt
  - Hulp: Bijvoorbeeld een overzicht van gegeven trainingen en de datum van de gebruiksregels. De wet schrijft geen vorm voor, maar zonder vastlegging kun je niet aantonen wat je hebt gedaan.
  - Type: boolean · Alleen vragen als: `facts.uses_ai_systems != false`

## Toetspunten

### AI3.1 — Of je weet welke AI er in je organisatie wordt gebruikt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: De organisatie heeft een overzicht van de gebruikte AI-systemen (geen uitdrukkelijke wettelijke plicht, wel voorwaarde om art. 4 gericht in te vullen)
- Grondslag: art. 4 AI-verordening (afgeleid)
- Alleen als: `facts.uses_ai_systems != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: uses_ai_systems, ai_inventory
- Beoordeling:
  - present als ai_inventory true is; absent als ai_inventory false is. Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Deze stap is niet verplicht en kan niet leiden tot non_compliant: een ontbrekend overzicht geeft review.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Weet de organisatie welke AI-systemen worden gebruikt, zodat zij de maatregelen daarop kan afstemmen?
- Advies bij ❌ of ⚠️: Maak een overzicht van de AI-systemen die in je organisatie worden gebruikt, door wie en waarvoor.
- Bronnen: AIVO-art4 (AI-verordening art. 4); EC-QA-AI-geletterdheid (Vragen en antwoorden van de Europese Commissie over AI-geletterdheid (art. 4 AI-verordening))

### AI3.2 — Of je maatregelen hebt genomen zodat mensen verstandig met AI werken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De organisatie neemt maatregelen om de ontwikkeling van AI-geletterdheid van haar personeel en van anderen die namens haar AI-systemen bedienen en gebruiken te ondersteunen
- Grondslag: art. 4 AI-verordening (zoals gewijzigd bij Verordening (EU) 2026/1744); art. 3 punt 56
- Alleen als: `facts.uses_ai_systems != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: uses_ai_systems, literacy_measures
- Beoordeling:
  - present als literacy_measures true is en literacy_measures_description ten minste één concrete maatregel noemt (instructie, training, workshop, e-learning, gebruiksregels of beleid, een aanspreekpunt, uitleg bij invoering) en voor wie die geldt.
  - absent als literacy_measures false is en literacy_measures_description leeg is of 'geen' zegt: geen enkele maatregel.
  - twijfel (⚠️) als literacy_measures false is maar literacy_measures_description toch een maatregel beschrijft (bijvoorbeeld 'nee, geen certificaat, maar wel een workshop'): het antwoord berust mogelijk op een misverstand.
  - twijfel (⚠️) als literacy_measures true is maar de beschrijving ontbreekt of vaag is ('iedereen weet hoe het werkt', 'we letten erop'), of als de maatregel alleen voor een klein deel van de gebruikers geldt.
  - Een ontbrekend certificaat, examen of vastgesteld kennisniveau per medewerker maakt de stap nooit absent: art. 4 vereist niet dat een bepaald niveau van AI-geletterdheid per persoon wordt gegarandeerd.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de genoemde maatregelen concreet genoeg om de ontwikkeling van AI-geletterdheid van de gebruikers te ondersteunen?
- Advies bij ❌ of ⚠️: Neem maatregelen zodat medewerkers verstandig met AI werken: bijvoorbeeld een korte instructie, gebruiksregels over wat wel en niet in een AI-tool mag, en een aanspreekpunt voor vragen. Een certificaat is niet verplicht.
- Bronnen: AIVO-art4 (AI-verordening art. 4); AIVO-art3-56 (AI-verordening art. 3 punt 56); AIVO-overw20 (AI-verordening overweging 20); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI3.3 — Of de maatregelen passen bij wat mensen met AI doen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De maatregelen houden rekening met de technische kennis, ervaring, onderwijs en opleiding van de gebruikers, de context waarin de AI-systemen worden gebruikt, en de personen of groepen personen ten aanzien van wie de AI-systemen worden gebruikt
- Grondslag: art. 4 AI-verordening
- Alleen als: `facts.uses_ai_systems != false and facts.literacy_measures != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: literacy_measures, high_impact_use, measures_differentiated
- Beoordeling:
  - Duidelijk geval (compliant): high_impact_use false en literacy_measures_description beschrijft maatregelen die passen bij het gebruik; of high_impact_use true, measures_differentiated true en de beschrijving noemt extra aandacht voor wie AI bij beslissingen over mensen gebruikt (bijvoorbeeld risico's, fouten, vooroordelen, menselijke controle).
  - high_impact_use true en measures_differentiated false: geen duidelijk geval (een juridisch adviseur beoordeelt of algemene maatregelen hier volstaan). Art. 4 noemt uitdrukkelijk ook de personen of groepen personen ten aanzien van wie de AI-systemen worden gebruikt (bijvoorbeeld sollicitanten, cliënten, kinderen): maatregelen die daar geen enkele aandacht aan besteden terwijl AI bij beslissingen over hen wordt gebruikt, zijn geen duidelijk compliant geval.
  - Een duidelijk non_compliant geval bestaat bij deze stap alleen als er in de praktijk niets op het gebruik is afgestemd terwijl AI wordt ingezet bij belangrijke beslissingen over mensen en de beschrijving dat bevestigt; ook dan is terughoudendheid geboden, omdat art. 4 een inspanningsverplichting is.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Houden de maatregelen voldoende rekening met de kennis van de gebruikers en met de context, vooral waar AI wordt gebruikt bij beslissingen over mensen?
- Advies bij ❌ of ⚠️: Stem de maatregelen af op wat mensen met AI doen. Wie AI gebruikt bij beslissingen over sollicitanten, medewerkers of klanten, heeft meer uitleg nodig over risico's, fouten en vooroordelen en over het eigen oordeel dat de medewerker moet blijven vormen.
- Bronnen: AIVO-art4 (AI-verordening art. 4); AIVO-overw20 (AI-verordening overweging 20); EC-QA-AI-geletterdheid (Vragen en antwoorden van de Europese Commissie over AI-geletterdheid (art. 4 AI-verordening))

### AI3.4 — Of de maatregelen ook gelden voor externen die namens jou met AI werken
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De maatregelen omvatten ook andere personen die namens de organisatie AI-systemen bedienen en gebruiken (uitzendkrachten, freelancers, dienstverleners)
- Grondslag: art. 4 AI-verordening
- Alleen als: `facts.uses_ai_systems != false and facts.external_users != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: external_users, externals_covered
- Beoordeling:
  - Art. 4 noemt uitdrukkelijk 'andere personen die namens hen AI-systemen bedienen en gebruiken'. De vraag is niet óf zij eronder vallen, maar hoe de maatregelen hen bereiken (zelfde instructie, of afspraken met hun werkgever of opdrachtnemer).
  - Duidelijk geval (compliant): externals_covered true.
  - externals_covered false: geen duidelijk geval (review); art. 4 is een inspanningsverplichting en maatregelen via de werkgever van de externe kunnen volstaan, dat beoordeelt een juridisch adviseur.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Worden externen die namens de organisatie AI gebruiken voldoende bereikt door de maatregelen, direct of via afspraken met hun werkgever?
- Advies bij ❌ of ⚠️: Zorg dat ook uitzendkrachten, freelancers en dienstverleners die namens jou met AI werken de instructie en gebruiksregels krijgen, of maak daarover afspraken met hun werkgever of opdrachtnemer.
- Bronnen: AIVO-art4 (AI-verordening art. 4); EC-QA-AI-geletterdheid (Vragen en antwoorden van de Europese Commissie over AI-geletterdheid (art. 4 AI-verordening))

### AI3.5 — Of je vastlegt wat je hebt gedaan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: De organisatie legt vast welke maatregelen zijn genomen, voor wie en wanneer (geen wettelijke vormvereiste; nodig om naleving aan te tonen)
- Grondslag: art. 4 AI-verordening (afgeleid)
- Alleen als: `facts.uses_ai_systems != false and facts.literacy_measures != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: measures_documented
- Beoordeling:
  - present als measures_documented true is; absent als false. Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Deze stap is niet verplicht en kan niet leiden tot non_compliant: ontbrekende vastlegging geeft review.
- Is het vereiste afwezig (*absent*): ⚠️
- Advies bij ❌ of ⚠️: Leg vast welke trainingen en instructies je hebt gegeven, aan wie en wanneer, en bewaar de gebruiksregels met datum. Een eenvoudig overzicht volstaat.
- Bronnen: AIVO-art4 (AI-verordening art. 4); EC-QA-AI-geletterdheid (Vragen en antwoorden van de Europese Commissie over AI-geletterdheid (art. 4 AI-verordening))

## Regels van dit kader

- Stap 2 absent (geen enkele maatregel) → non_compliant → kader non_compliant.
- Een ontbrekend certificaat, toets of niveau per medewerker is nooit een reden voor non_compliant (art. 4 zoals gewijzigd).
- Stap 1 en 5 zijn niet verplicht; ontbreken geeft review.

## Open punten en voorbehouden

- Opgelost in v0.3 (officiële tekst gecontroleerd): 'toereikend niveau' is vervallen; 'de personen of groepen personen ten aanzien van wie de AI-systemen zullen worden gebruikt' staat er wel in en is in stap 3 opgenomen; de verplichting houdt uitdrukkelijk niet in dat een bepaald niveau moet worden gewaarborgd.
- Q&A van de Commissie over AI-geletterdheid (mei 2025) is opgesteld onder de oude tekst; alleen gebruiken waar verenigbaar met de nieuwe inspanningsverplichting.
- Art. 4 staat niet in de boetecategorieën van art. 99; handhaving via nationaal recht (Uitvoeringswet AI-verordening, wetsvoorstel).
