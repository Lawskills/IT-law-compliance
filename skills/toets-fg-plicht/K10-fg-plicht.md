# Kader K10 — FG-plicht

Versie 1.2 · peildatum 2026-11-10

Doel: Vaststellen of een functionaris gegevensbescherming (FG) verplicht is (art. 37 lid 1 AVG), en als er een FG is (verplicht of vrijwillig) of aan de eisen van art. 37 lid 7 en art. 38 wordt voldaan.

Bronnen: AVG-art37 (AVG art. 37); AVG-art37-lid1 (AVG art. 37 lid 1); AVG-art37-lid7 (AVG art. 37 lid 7); AVG-art38 (AVG art. 38); AVG-art39 (AVG art. 39); WP243-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake functionarissen voor gegevensbescherming (WP243 rev.01), bekrachtigd door de EDPB); HvJEU-C-453-21 (HvJEU 9 februari 2023, C-453/21, X-FAB Dresden)

## Formulier (vragen aan de gebruiker)

- **public_authority**: Is je organisatie een overheidsinstantie of overheidsorgaan?
  - Label (voor de plek-om-in-te-vullen): of je organisatie een overheidsinstantie is
  - Hulp: Bijvoorbeeld een gemeente, provincie, waterschap of een zelfstandig bestuursorgaan. Een gewoon bedrijf dat voor de overheid werkt, telt niet.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **court_judicial_capacity**: Is je organisatie een gerecht, en gaat het om de verwerking bij het rechtspreken?
  - Label (voor de plek-om-in-te-vullen): of het gaat om een gerecht in zijn rechtspraaktaak
  - Type: boolean · Alleen vragen als: `facts.public_authority == true` · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **core_activity_description**: Wat zijn de belangrijkste activiteiten van je organisatie, en welke rol spelen persoonsgegevens daarin?
  - Label (voor de plek-om-in-te-vullen): wat je belangrijkste activiteiten zijn
  - Hulp: Het gaat om je kernactiviteiten: waarmee je je doel bereikt of je geld verdient, niet om ondersteunende zaken als salarisadministratie of IT-beheer.
  - Type: text
- **core_activity_monitoring**: Bestaan je kernactiviteiten uit het regelmatig en stelselmatig volgen of observeren van mensen op grote schaal?
  - Label (voor de plek-om-in-te-vullen): of je kernactiviteiten bestaan uit het regelmatig en stelselmatig volgen van mensen op grote schaal
  - Hulp: Bijvoorbeeld een beveiligingsbedrijf dat camera's beheert, een bedrijf dat online gedrag volgt voor advertenties, of een verzekeraar die rijgedrag volgt.
  - Type: boolean
- **core_activity_special_data**: Bestaan je kernactiviteiten uit het op grote schaal verwerken van gevoelige gegevens (zoals gezondheid) of gegevens over strafbare feiten?
  - Label (voor de plek-om-in-te-vullen): of je kernactiviteiten bestaan uit grootschalige verwerking van gevoelige of strafrechtelijke gegevens
  - Hulp: Bijvoorbeeld een ziekenhuis, een arbodienst of een bedrijf dat antecedentenonderzoek doet.
  - Type: boolean
- **has_dpo**: Heb je een functionaris gegevensbescherming (FG) aangesteld, verplicht of vrijwillig?
  - Label (voor de plek-om-in-te-vullen): of je een functionaris gegevensbescherming hebt
  - Hulp: Een privacymedewerker zonder de officiële FG-rol telt niet mee.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **dpo_assessment_documented**: Heb je vastgelegd waarom je organisatie geen FG hoeft aan te stellen?
  - Label (voor de plek-om-in-te-vullen): of je hebt vastgelegd waarom je geen FG nodig hebt
  - Type: boolean · Alleen vragen als: `facts.has_dpo != true and facts.public_authority != true and facts.core_activity_monitoring != true and facts.core_activity_special_data != true`
- **dpo_contact_published**: Heb je de contactgegevens van je FG gepubliceerd, bijvoorbeeld in je privacyverklaring?
  - Label (voor de plek-om-in-te-vullen): of de contactgegevens van de FG openbaar zijn
  - Type: boolean · Alleen vragen als: `facts.has_dpo == true`
- **dpo_reported_to_ap**: Heb je je FG aangemeld bij de Autoriteit Persoonsgegevens?
  - Label (voor de plek-om-in-te-vullen): of de FG is aangemeld bij de Autoriteit Persoonsgegevens
  - Type: boolean · Alleen vragen als: `facts.has_dpo == true`
- **dpo_involved_timely**: Wordt je FG tijdig en goed betrokken bij alle zaken over persoonsgegevens, bijvoorbeeld voordat een nieuw systeem wordt gekozen?
  - Label (voor de plek-om-in-te-vullen): of de FG tijdig wordt betrokken
  - Type: boolean · Alleen vragen als: `facts.has_dpo == true`
- **dpo_sufficient_resources**: Heeft je FG voldoende tijd, budget en toegang tot informatie om zijn taken uit te voeren?
  - Label (voor de plek-om-in-te-vullen): of de FG voldoende tijd en middelen heeft
  - Type: boolean · Alleen vragen als: `facts.has_dpo == true`
- **dpo_independent**: Werkt je FG zonder instructies over de uitvoering van zijn taken, en is uitgesloten dat hij wordt ontslagen of gestraft voor het uitvoeren van die taken?
  - Label (voor de plek-om-in-te-vullen): of de FG onafhankelijk werkt
  - Type: boolean · Alleen vragen als: `facts.has_dpo == true`
- **dpo_other_roles**: Welke andere functies of taken heeft je FG binnen of buiten je organisatie?
  - Label (voor de plek-om-in-te-vullen): welke andere functies de FG heeft
  - Hulp: Bijvoorbeeld directeur, hoofd IT, HR-manager, of 'geen andere taken'.
  - Type: text · Alleen vragen als: `facts.has_dpo == true`
- **dpo_conflict_of_interest**: Beslist je FG in een andere functie zelf mee over waarvoor en hoe persoonsgegevens worden gebruikt?
  - Label (voor de plek-om-in-te-vullen): of de FG in een andere functie zelf beslist over het gebruik van persoonsgegevens
  - Type: boolean · Alleen vragen als: `facts.has_dpo == true`

## Toetspunten

### K10.1 — Of je als overheidsorganisatie een FG moet hebben
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Overheidsinstantie of -orgaan (behalve gerechten in hun rechterlijke taak)? → FG verplicht
- Grondslag: art. 37 lid 1 sub a AVG
- Beoordeeld op: de antwoorden
- Nodig: public_authority, court_judicial_capacity, has_dpo
- Beoordeling:
  - present als public_authority onwaar is, of als court_judicial_capacity waar is (geen verplichting op deze grond).
  - present als public_authority waar is, court_judicial_capacity onwaar is en has_dpo waar is.
  - absent als public_authority waar is, court_judicial_capacity onwaar is en has_dpo onwaar is.
  - Ontbrekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Stel een functionaris gegevensbescherming aan; voor overheidsorganisaties is dat verplicht.
- Bronnen: AVG-art37-lid1-a (AVG art. 37 lid 1 sub a)

### K10.2 — Of je een FG moet hebben omdat je mensen op grote schaal volgt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bestaan de kernactiviteiten uit verwerkingen die regelmatige en stelselmatige observatie op grote schaal vereisen? → FG verplicht
- Grondslag: art. 37 lid 1 sub b AVG
- Beoordeeld op: de antwoorden
- Nodig: core_activity_description, core_activity_monitoring, has_dpo
- Beoordeling:
  - 'Kernactiviteit' en 'grote schaal' zijn open normen: bij twijfel geen duidelijk geval.
  - Duidelijk compliant: has_dpo waar, of core_activity_monitoring onwaar en core_activity_description bevestigt dat het volgen van mensen geen kernactiviteit is.
  - Duidelijk non_compliant: core_activity_monitoring waar, core_activity_description bevestigt dat het volgen van mensen op grote schaal de kern van de activiteiten is, en has_dpo onwaar.
  - Een leverancier of klant die een FG eist, maakt het geen wettelijke plicht.
  - In alle andere gevallen geen duidelijk geval (ook bij 'weet ik niet').
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het regelmatig en stelselmatig observeren op grote schaal een kernactiviteit van deze organisatie?
- Advies bij ❌ of ⚠️: Bestaan je kernactiviteiten uit het op grote schaal volgen van mensen, stel dan een functionaris gegevensbescherming aan.
- Bronnen: AVG-art37-lid1-b (AVG art. 37 lid 1 sub b); WP243-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake functionarissen voor gegevensbescherming (WP243 rev.01), bekrachtigd door de EDPB)

### K10.3 — Of je een FG moet hebben omdat je op grote schaal gevoelige gegevens verwerkt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bestaan de kernactiviteiten uit grootschalige verwerking van bijzondere of strafrechtelijke gegevens? → FG verplicht
- Grondslag: art. 37 lid 1 sub c AVG
- Beoordeeld op: de antwoorden
- Nodig: core_activity_description, core_activity_special_data, has_dpo
- Beoordeling:
  - 'Kernactiviteit' en 'grote schaal' zijn open normen: bij twijfel geen duidelijk geval.
  - Duidelijk compliant: has_dpo waar, of core_activity_special_data onwaar en core_activity_description bevestigt dat de verwerking van bijzondere of strafrechtelijke gegevens geen kernactiviteit is (bijvoorbeeld alleen verzuimgegevens van eigen personeel).
  - Duidelijk non_compliant: core_activity_special_data waar, core_activity_description bevestigt dat grootschalige verwerking van deze gegevens de kern van de activiteiten is, en has_dpo onwaar.
  - In alle andere gevallen geen duidelijk geval (ook bij 'weet ik niet').
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is grootschalige verwerking van bijzondere of strafrechtelijke gegevens een kernactiviteit van deze organisatie?
- Advies bij ❌ of ⚠️: Bestaan je kernactiviteiten uit het op grote schaal verwerken van gevoelige of strafrechtelijke gegevens, stel dan een functionaris gegevensbescherming aan.
- Bronnen: AVG-art37-lid1-c (AVG art. 37 lid 1 sub c); WP243-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake functionarissen voor gegevensbescherming (WP243 rev.01), bekrachtigd door de EDPB)

### K10.4 — Of je hebt vastgelegd waarom je geen FG nodig hebt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Geen van drieën → niet verplicht; een leverancier of klant die een FG eist maakt het geen wettelijke plicht; het vastleggen van de afweging is aan te bevelen (WP243)
- Grondslag: art. 37 lid 1 AVG; WP243 rev.01
- Alleen als: `facts.has_dpo != true and facts.public_authority != true and facts.core_activity_monitoring != true and facts.core_activity_special_data != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: dpo_assessment_documented
- Beoordeling:
  - Het vastleggen van de afweging is een aanbeveling, geen wettelijke plicht: deze stap levert nooit non_compliant op.
  - Duidelijk compliant: dpo_assessment_documented waar.
  - dpo_assessment_documented onwaar of onbekend: geen duidelijk geval, met het advies de afweging vast te leggen.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is de afweging dat geen FG verplicht is, vastgelegd?
- Advies bij ❌ of ⚠️: Leg kort vast waarom je organisatie geen FG hoeft aan te stellen. Wil je wel iemand met privacytaken, noem die persoon dan geen 'FG'.
- Bronnen: AVG-art37-lid1 (AVG art. 37 lid 1); WP243-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake functionarissen voor gegevensbescherming (WP243 rev.01), bekrachtigd door de EDPB)

### K10.5 — Je FG voldoet aan de eisen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Als er een FG is, verplicht of vrijwillig: contactgegevens gepubliceerd en meegedeeld aan de AP, tijdig betrokken, voldoende middelen, geen instructies en geen ontslag of straf voor het uitvoeren van de taken, geen belangenconflict
- Grondslag: art. 37 lid 7 en art. 38 lid 1, 2, 3 en 6 AVG
- Alleen als: `facts.has_dpo == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: dpo_contact_published, dpo_reported_to_ap, dpo_involved_timely, dpo_sufficient_resources, dpo_independent, dpo_other_roles, dpo_conflict_of_interest
- Beoordeling:
  - Voor een vrijwillige FG gelden dezelfde regels als voor een verplichte (WP243).
  - absent als een van dpo_contact_published, dpo_reported_to_ap, dpo_involved_timely, dpo_sufficient_resources of dpo_independent onwaar is.
  - absent als dpo_conflict_of_interest waar is (art. 38 lid 6; C-453/21).
  - twijfel (⚠️) als dpo_conflict_of_interest onwaar is maar dpo_other_roles een functie noemt waarin de FG mogelijk zelf beslist over doelen en middelen van verwerkingen: een belangenconflict wordt per geval beoordeeld (C-453/21).
  - present als alle vijf waar zijn, dpo_conflict_of_interest onwaar is en dpo_other_roles geen functie noemt die tot een belangenconflict kan leiden.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Leidt een andere functie van de FG tot een belangenconflict?
- Advies bij ❌ of ⚠️: Zorg dat je FG bereikbaar is via gepubliceerde contactgegevens, is aangemeld bij de Autoriteit Persoonsgegevens, tijdig wordt betrokken, voldoende middelen heeft, onafhankelijk werkt en geen functie heeft waarin hij zelf beslist over het gebruik van persoonsgegevens.
- Bronnen: AVG-art37-lid7 (AVG art. 37 lid 7); AVG-art38-lid1 (AVG art. 38 lid 1); AVG-art38-lid2 (AVG art. 38 lid 2); AVG-art38-lid3 (AVG art. 38 lid 3); AVG-art38-lid6 (AVG art. 38 lid 6); WP243-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake functionarissen voor gegevensbescherming (WP243 rev.01), bekrachtigd door de EDPB); HvJEU-C-453-21 (HvJEU 9 februari 2023, C-453/21, X-FAB Dresden)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): public_authority, court_judicial_capacity, core_activity_description, has_dpo, dpo_other_roles. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 2 en 3 zijn open normen ('kernactiviteit', 'grote schaal') → bij twijfel review.
- Geen van stap 1-3 → FG niet verplicht. Een leverancier of klant die een FG eist, maakt het geen wettelijke plicht.
- Voor een vrijwillige FG gelden dezelfde regels als voor een verplichte FG (WP243).
- Wil de klant geen FG aanstellen maar wel iemand met privacytaken, dan die persoon niet 'FG' noemen.

## Samenhang met andere kaders

- Kader K3 (/toets-grondslag) — als `facts.core_activity_special_data != false`: Voor bijzondere en strafrechtelijke gegevens gelden extra regels.
