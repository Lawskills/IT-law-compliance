# Kader AI5 — Hoog risico: plichten als gebruiker (art. 26)

Versie 0.4 · peildatum 2026-11-10

Doel: Controleren of een organisatie die een hoogrisico-AI-systeem onder haar verantwoordelijkheid gebruikt (gebruiksverantwoordelijke) de plichten van art. 26 AI-verordening naleeft, of zij door eigen handelen zelf aanbieder wordt (art. 25 lid 1), en of zij betrokkenen kan informeren en uitleg kan geven (art. 26 lid 11, art. 86).

Van toepassing vanaf: 2027-12-02 als `facts.high_risk_basis == "annex3"`; 2028-08-02 als `facts.high_risk_basis == "annex1"` — art. 113, derde alinea, onder c, zoals gewijzigd bij Verordening (EU) 2026/1744

Bronnen: AIVO-art3-4 (AI-verordening art. 3 punt 4); AIVO-art6-lid2 (AI-verordening art. 6 lid 2); AIVO-art25-lid1 (AI-verordening art. 25 lid 1); AIVO-art26-lid1 (AI-verordening art. 26 lid 1); AIVO-art26-lid2 (AI-verordening art. 26 lid 2); AIVO-art26-lid3 (AI-verordening art. 26 lid 3); AIVO-art26-lid4 (AI-verordening art. 26 lid 4); AIVO-art26-lid5 (AI-verordening art. 26 lid 5); AIVO-art26-lid6 (AI-verordening art. 26 lid 6); AIVO-art26-lid7 (AI-verordening art. 26 lid 7); AIVO-art26-lid8 (AI-verordening art. 26 lid 8); AIVO-art26-lid9 (AI-verordening art. 26 lid 9); AIVO-art26-lid11 (AI-verordening art. 26 lid 11); AIVO-art49-lid3 (AI-verordening art. 49 lid 3); AIVO-art86-lid1 (AI-verordening art. 86 lid 1); AIVO-art113 (AI-verordening art. 113); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI)); AIVO-art111-lid2 (AI-verordening art. 111 lid 2)

## Formulier (vragen aan de gebruiker)

- **system_name**: Om welk AI-systeem gaat het, en van welke leverancier?
  - Label (voor de plek-om-in-te-vullen): welk systeem het is
  - Type: text
- **high_risk_basis**: Waarom is dit systeem hoog risico?
  - Label (voor de plek-om-in-te-vullen): waarom het systeem hoog risico is
  - Hulp: Gebruik de uitkomst van de check 'Signaal: mogelijk hoog risico' of wat de leverancier zegt.
  - Type: enum (annex3 / annex1)
- **high_risk_confirmed**: Heeft de leverancier of een andere deskundige bevestigd dat het systeem hoog risico is?
  - Label (voor de plek-om-in-te-vullen): of bevestigd is dat het systeem hoog risico is
  - Type: boolean
- **annex3_area**: In welk gebied gebruik je het systeem?
  - Label (voor de plek-om-in-te-vullen): in welk gevoelig gebied je het systeem gebruikt
  - Type: enum (none / employment / education / credit_scoring / life_health_insurance / biometric / critical_infrastructure / public_services / law_enforcement_migration_justice_elections)
- **deployer_type**: Wat voor organisatie ben je?
  - Label (voor de plek-om-in-te-vullen): wat voor organisatie je bent
  - Type: enum (public_body / private_public_service / other) · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **role_change_name**: Zet je je eigen naam of merk op het systeem, bijvoorbeeld omdat je het aan klanten aanbiedt als jouw product?
  - Label (voor de plek-om-in-te-vullen): of je je eigen naam of merk op het systeem zet
  - Type: boolean
- **role_change_modification**: Heb je het systeem zelf wezenlijk aangepast, op een manier die de leverancier niet had voorzien?
  - Label (voor de plek-om-in-te-vullen): of je het systeem wezenlijk wijzigt
  - Hulp: Bijvoorbeeld het model opnieuw trainen voor een ander soort beslissing. Gewone instellingen volgens de handleiding tellen niet.
  - Type: boolean
- **role_change_purpose**: Gebruik je het systeem voor een ander doel dan waarvoor de leverancier het levert, waardoor het pas hoog risico wordt?
  - Label (voor de plek-om-in-te-vullen): of je het systeem voor een ander doel gebruikt dan de leverancier bedoelt
  - Hulp: Bijvoorbeeld een algemene chatbot inzetten om sollicitanten te selecteren.
  - Type: boolean
- **instructions_available**: Heb je de gebruiksaanwijzing van de aanbieder ontvangen?
  - Label (voor de plek-om-in-te-vullen): of je de gebruiksaanwijzing van de aanbieder hebt
  - Type: boolean
- **use_per_instructions**: Heb je afspraken of technische instellingen die ervoor zorgen dat het systeem alleen wordt gebruikt zoals de gebruiksaanwijzing beschrijft?
  - Label (voor de plek-om-in-te-vullen): of je maatregelen hebt om het systeem volgens de gebruiksaanwijzing te gebruiken
  - Hulp: Bijvoorbeeld een werkinstructie, beperkte toegang, of instellingen die alleen het beoogde gebruik toelaten.
  - Type: boolean
- **oversight_assigned**: Heb je bij naam of functie vastgelegd wie toezicht houdt op het systeem?
  - Label (voor de plek-om-in-te-vullen): of het menselijk toezicht aan bepaalde personen is toegewezen
  - Type: boolean
- **oversight_competent**: Hebben die personen de kennis en opleiding om de uitkomsten te begrijpen, en mogen en kunnen ze ingrijpen of het systeem stoppen?
  - Label (voor de plek-om-in-te-vullen): of de toezichthouders de nodige kennis, opleiding, bevoegdheid en ondersteuning hebben
  - Type: boolean
- **input_data_control**: Bepaal je zelf welke gegevens in het systeem gaan (bijvoorbeeld welke cv's of klantgegevens)?
  - Label (voor de plek-om-in-te-vullen): of je zelf bepaalt welke gegevens het systeem krijgt
  - Type: boolean
- **input_data_checked**: Controleer je of die gegevens passen bij het doel en de groep mensen waarop het systeem wordt toegepast?
  - Label (voor de plek-om-in-te-vullen): of je controleert dat de invoergegevens relevant en representatief zijn
  - Type: boolean · Alleen vragen als: `facts.input_data_control != false`
- **monitoring_in_place**: Volg je de werking van het systeem zoals de gebruiksaanwijzing voorschrijft, bijvoorbeeld door uitkomsten steekproefsgewijs te controleren?
  - Label (voor de plek-om-in-te-vullen): of je de werking van het systeem volgt
  - Type: boolean
- **incident_procedure**: Is vastgelegd wat je doet bij een risico of een ernstig incident: het gebruik stoppen, en de aanbieder en de toezichthouder direct informeren?
  - Label (voor de plek-om-in-te-vullen): of je weet wanneer je de aanbieder en de toezichthouder moet informeren
  - Type: boolean
- **logs_control**: Bewaar jij de automatisch gemaakte logbestanden van het systeem (en niet alleen de leverancier)?
  - Label (voor de plek-om-in-te-vullen): of de logbestanden van het systeem onder jouw beheer staan
  - Type: boolean
- **logs_retention_months**: Hoeveel maanden bewaar je de logbestanden?
  - Label (voor de plek-om-in-te-vullen): hoe lang je de logbestanden bewaart (in maanden)
  - Type: number · Alleen vragen als: `facts.logs_control != false`
- **workplace_use**: Gebruik je het systeem op de werkvloer, of voor beslissingen over je eigen medewerkers?
  - Label (voor de plek-om-in-te-vullen): of je het systeem op de werkvloer gebruikt
  - Type: boolean
- **workers_informed**: Heb je de ondernemingsraad (of personeelsvertegenwoordiging) en de medewerkers die het raakt geïnformeerd voordat het systeem in gebruik ging?
  - Label (voor de plek-om-in-te-vullen): of je de werknemersvertegenwoordiging en de betrokken medewerkers vooraf hebt geïnformeerd
  - Type: boolean · Alleen vragen als: `facts.workplace_use != false`
- **registered_use**: Heb je het gebruik van het systeem geregistreerd in de EU-databank, en staat het systeem zelf daar ook in?
  - Label (voor de plek-om-in-te-vullen): of het gebruik is geregistreerd in de EU-databank
  - Type: boolean · Alleen vragen als: `facts.deployer_type != "other"`
- **personal_data**: Verwerkt het systeem persoonsgegevens?
  - Label (voor de plek-om-in-te-vullen): of het systeem persoonsgegevens verwerkt
  - Type: boolean
- **dpia_uses_provider_info**: Heb je een DPIA gedaan, en heb je daarbij de informatie uit de gebruiksaanwijzing van de aanbieder gebruikt?
  - Label (voor de plek-om-in-te-vullen): of je een DPIA hebt gedaan met de informatie van de aanbieder
  - Type: boolean · Alleen vragen als: `facts.personal_data != false`
- **decisions_about_persons**: Neemt het systeem besluiten over mensen, of helpt het bij zulke besluiten (bijvoorbeeld wie wordt uitgenodigd, wie krediet krijgt)?
  - Label (voor de plek-om-in-te-vullen): of het systeem besluiten over personen neemt of daarbij helpt
  - Type: boolean
- **persons_informed**: Vertel je de mensen over wie het gaat dat dit systeem bij hen wordt gebruikt?
  - Label (voor de plek-om-in-te-vullen): of je de betrokken personen vertelt dat het systeem wordt gebruikt
  - Type: boolean · Alleen vragen als: `facts.decisions_about_persons != false`
- **explanation_procedure**: Kun je iemand op verzoek duidelijk uitleggen welke rol het systeem had bij een besluit over hem, en wat de belangrijkste redenen voor het besluit waren?
  - Label (voor de plek-om-in-te-vullen): of je op verzoek kunt uitleggen welke rol het systeem bij een besluit had
  - Type: boolean · Alleen vragen als: `facts.decisions_about_persons != false`

## Toetspunten

### AI5.1 — Of vaststaat dat het systeem hoog risico is
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Het systeem is als hoogrisico-AI-systeem geclassificeerd (art. 6 lid 1 met bijlage I, of art. 6 lid 2 met bijlage III); zonder bevestiging gaat deze toets uit van hoog risico
- Grondslag: art. 6 lid 1 en 2 AI-verordening
- Alleen als: `facts.high_risk_confirmed != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: high_risk_confirmed, high_risk_basis
- Beoordeling:
  - Deze stap geeft altijd review: Deze toets classificeert niet definitief. Vermeld dat de rest van de toets ervan uitgaat dat het systeem hoog risico is, en dat de leverancier (aanbieder) moet kunnen zeggen of het een hoogrisicosysteem is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Is het systeem een hoogrisico-AI-systeem in de zin van art. 6 lid 1 of 2?
- Advies bij ❌ of ⚠️: Vraag de leverancier schriftelijk of het systeem een hoogrisicosysteem is, en zo ja, om de EU-conformiteitsverklaring en de gebruiksaanwijzing. Laat bij twijfel een juridisch adviseur classificeren.
- Bronnen: AIVO-art6-lid2 (AI-verordening art. 6 lid 2); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI5.2 — Of je zelf aanbieder wordt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De gebruiksverantwoordelijke wordt aanbieder als hij zijn naam of merk op het hoogrisicosysteem zet, het systeem substantieel wijzigt, of het beoogde doel wijzigt waardoor het een hoogrisicosysteem wordt
- Grondslag: art. 25 lid 1 sub a-c AI-verordening
- Alleen als: `facts.role_change_name != false or facts.role_change_modification != false or facts.role_change_purpose != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: role_change_name, role_change_modification, role_change_purpose
- Beoordeling:
  - Deze stap geeft altijd review: of een wijziging 'substantieel' is, is een afweging.
  - Is een van de drie feiten true: vermeld dat de organisatie dan als aanbieder geldt en de plichten van art. 16 heeft (kader AI7), en dat de oorspronkelijke aanbieder dan moet meewerken met informatie en technische toegang (art. 25 lid 2).
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Wordt de gebruiksverantwoordelijke door het genoemde handelen aanbieder in de zin van art. 25 lid 1?
- Advies bij ❌ of ⚠️: Laat een juridisch adviseur beoordelen of je door deze handeling zelf aanbieder wordt. Is dat zo, doe dan ook de check 'Hoog risico: plichten als aanbieder' en maak schriftelijke afspraken met de oorspronkelijke leverancier over informatie en technische toegang.
- Bronnen: AIVO-art25-lid1 (AI-verordening art. 25 lid 1)

### AI5.3 — Of je het systeem gebruikt volgens de gebruiksaanwijzing
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De gebruiksverantwoordelijke neemt passende technische en organisatorische maatregelen om het systeem te gebruiken overeenkomstig de gebruiksaanwijzing
- Grondslag: art. 26 lid 1 AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: instructions_available, use_per_instructions
- Beoordeling:
  - present als instructions_available true en use_per_instructions true is.
  - absent als instructions_available false is (zonder gebruiksaanwijzing kun je er niet naar handelen) of use_per_instructions false is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vraag de gebruiksaanwijzing op bij de leverancier en maak een korte werkinstructie: waarvoor het systeem wel en niet gebruikt mag worden, door wie, en met welke instellingen.
- Bronnen: AIVO-art26-lid1 (AI-verordening art. 26 lid 1)

### AI5.4 — Of iemand met de juiste kennis en bevoegdheid toezicht houdt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De gebruiksverantwoordelijke draagt het menselijk toezicht op aan natuurlijke personen die over de nodige bekwaamheid, opleiding en autoriteit beschikken en de nodige ondersteuning krijgen
- Grondslag: art. 26 lid 2 AI-verordening (lid 3: andere plichten en de vrijheid om toezicht te organiseren blijven onverlet)
- Beoordeeld op: de antwoorden
- Nodig: oversight_assigned, oversight_competent
- Beoordeling:
  - present als oversight_assigned true en oversight_competent true is.
  - absent als oversight_assigned false is of oversight_competent false is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Wijs per systeem bij naam of functie aan wie toezicht houdt. Zorg dat die personen weten hoe het systeem werkt en waar het fouten maakt, dat ze uitkomsten mogen negeren of het systeem mogen stoppen, en dat ze daar tijd voor hebben.
- Bronnen: AIVO-art26-lid2 (AI-verordening art. 26 lid 2); AIVO-art26-lid3 (AI-verordening art. 26 lid 3)

### AI5.5 — Of de gegevens die je invoert passen bij het doel
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Voor zover de gebruiksverantwoordelijke controle heeft over de inputdata, zorgt hij dat die relevant en voldoende representatief zijn voor het beoogde doel
- Grondslag: art. 26 lid 4 AI-verordening
- Alleen als: `facts.input_data_control != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: input_data_control, input_data_checked
- Beoordeling:
  - present als input_data_checked true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg vast welke gegevens in het systeem gaan en controleer periodiek of ze passen bij het doel en bij de groep mensen waarop het wordt toegepast, bijvoorbeeld of bepaalde groepen ondervertegenwoordigd zijn.
- Bronnen: AIVO-art26-lid4 (AI-verordening art. 26 lid 4)

### AI5.6 — Of je de werking volgt en weet wanneer je moet melden
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De gebruiksverantwoordelijke monitort de werking op basis van de gebruiksaanwijzing; bij reden om aan te nemen dat het systeem een risico vormt, informeert hij zonder onnodige vertraging de aanbieder of distributeur en de markttoezichtautoriteit en schort hij het gebruik op; bij een ernstig incident informeert hij onmiddellijk eerst de aanbieder en daarna de importeur of distributeur en de markttoezichtautoriteiten
- Grondslag: art. 26 lid 5 AI-verordening (met art. 79 lid 1 en art. 73)
- Beoordeeld op: de antwoorden
- Nodig: monitoring_in_place, incident_procedure
- Beoordeling:
  - present als monitoring_in_place true en incident_procedure true is.
  - absent als een van beide false is.
  - Voor financiële instellingen die onder interne governanceregels van het financiële recht vallen, geldt de monitoringplicht als vervuld door die regels na te leven (art. 26 lid 5, tweede alinea). Wijst system_name of het gebied daarop, vermeld dat.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Spreek af hoe vaak en hoe je uitkomsten controleert, en leg vast wat je doet bij een risico of ernstig incident: het gebruik stoppen en de leverancier en de toezichthouder direct informeren.
- Bronnen: AIVO-art26-lid5 (AI-verordening art. 26 lid 5)

### AI5.7 — Of je de logbestanden minstens zes maanden bewaart
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Voor zover de automatisch gegenereerde logs onder zijn controle staan, bewaart de gebruiksverantwoordelijke ze gedurende een periode die past bij het doel, ten minste zes maanden, tenzij Unie- of nationaal recht (met name over persoonsgegevens) anders bepaalt
- Grondslag: art. 26 lid 6 AI-verordening
- Alleen als: `facts.logs_control != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: logs_control, logs_retention_months
- Beoordeling:
  - present als logs_retention_months 6 of meer is; absent als het minder dan 6 is.
  - Een termijn van meer dan zes maanden is niet automatisch goed: de AVG vraagt dat persoonsgegevens niet langer worden bewaard dan nodig. Noem dat in de onderbouwing als logs_retention_months hoger is dan 24.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Bewaar de logbestanden van het systeem minstens zes maanden, en niet langer dan nodig is voor het doel. Leg de termijn vast in je bewaarbeleid.
- Bronnen: AIVO-art26-lid6 (AI-verordening art. 26 lid 6)

### AI5.8 — Of je medewerkers en hun vertegenwoordiging vooraf hebt geïnformeerd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Een gebruiksverantwoordelijke die werkgever is, informeert vóór de ingebruikname op de werkplek de werknemersvertegenwoordigers en de betrokken werknemers dat zij aan het systeem worden onderworpen
- Grondslag: art. 26 lid 7 AI-verordening
- Alleen als: `facts.workplace_use != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: workplace_use, workers_informed
- Beoordeling:
  - present als workers_informed true is; absent als false.
  - Naar Nederlands recht kan daarnaast instemming van de ondernemingsraad nodig zijn (art. 27 lid 1 sub l WOR, systemen voor waarneming van of controle op aanwezigheid, gedrag of prestaties). Dat is geen onderdeel van deze toets: noem het alleen in de onderbouwing.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Informeer de ondernemingsraad (of personeelsvertegenwoordiging) en de medewerkers die het raakt voordat het systeem in gebruik gaat. Volgt het systeem gedrag of prestaties van medewerkers, vraag dan ook instemming van de ondernemingsraad.
- Bronnen: AIVO-art26-lid7 (AI-verordening art. 26 lid 7)

### AI5.9 — Of het gebruik is geregistreerd (overheid)
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Gebruiksverantwoordelijken die overheidsinstanties of instellingen van de Unie zijn, registreren zich, kiezen het systeem en registreren het gebruik ervan in de EU-databank; een systeem dat niet in de databank staat, gebruiken zij niet en zij informeren de aanbieder of distributeur
- Grondslag: art. 26 lid 8 en art. 49 lid 3 AI-verordening
- Alleen als: `facts.deployer_type != "other" and facts.deployer_type != "private_public_service"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: deployer_type, registered_use
- Beoordeling:
  - present als registered_use true is; absent als false.
  - Voor systemen voor kritieke infrastructuur (bijlage III punt 2) geldt registratie op nationaal niveau (art. 49 lid 5); voor rechtshandhaving, migratie en grenscontrole een beveiligd, niet-openbaar deel (art. 49 lid 4). Vermeld dat als annex3_area daarop wijst.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Registreer je organisatie en het gebruik van dit systeem in de EU-databank voor hoogrisico-AI. Staat het systeem zelf er niet in, gebruik het dan niet en meld dat aan de leverancier.
- Bronnen: AIVO-art26-lid8 (AI-verordening art. 26 lid 8); AIVO-art49-lid3 (AI-verordening art. 49 lid 3)

### AI5.10 — Of je de informatie van de aanbieder gebruikt voor je DPIA
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Waar van toepassing gebruikt de gebruiksverantwoordelijke de informatie van art. 13 (gebruiksaanwijzing) om zijn plicht tot een gegevensbeschermingseffectbeoordeling (art. 35 AVG) na te komen
- Grondslag: art. 26 lid 9 AI-verordening; art. 35 AVG
- Alleen als: `facts.personal_data != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: personal_data, dpia_uses_provider_info
- Beoordeling:
  - present als dpia_uses_provider_info true is; absent als false.
  - Of een DPIA verplicht is, beoordeelt K9; deze stap kijkt alleen of de informatie van de aanbieder daarvoor is gebruikt. Daarom niet verplicht: ontbreken geeft review.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is een DPIA verplicht voor deze verwerking, en is de informatie van de aanbieder daarin verwerkt?
- Advies bij ❌ of ⚠️: Doe een DPIA en gebruik daarbij de gebruiksaanwijzing van de aanbieder: het doel, de bekende beperkingen, de nauwkeurigheid en de risico's die hij noemt.
- Bronnen: AIVO-art26-lid9 (AI-verordening art. 26 lid 9)

### AI5.11 — Of je mensen vertelt dat het systeem bij hen wordt gebruikt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Gebruiksverantwoordelijken van hoogrisicosystemen uit bijlage III die besluiten nemen of helpen nemen over natuurlijke personen, informeren die personen dat het systeem op hen wordt toegepast
- Grondslag: art. 26 lid 11 AI-verordening
- Alleen als: `facts.decisions_about_persons != false and facts.high_risk_basis != "annex1"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: decisions_about_persons, persons_informed
- Beoordeling:
  - present als persons_informed true is; absent als false.
  - Voor rechtshandhaving geldt art. 13 van Richtlijn (EU) 2016/680 (art. 26 lid 11, tweede zin). Vermeld dat als annex3_area daarop wijst.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vertel de mensen over wie het systeem besluit of adviseert dat je het gebruikt, bijvoorbeeld in de vacaturetekst, de aanvraagprocedure of je privacyverklaring.
- Bronnen: AIVO-art26-lid11 (AI-verordening art. 26 lid 11)

### AI5.12 — Of je een besluit op verzoek kunt uitleggen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Wie geraakt wordt door een besluit dat de gebruiksverantwoordelijke neemt op basis van de output van een hoogrisicosysteem uit bijlage III (behalve punt 2), met rechtsgevolgen of vergelijkbare aanzienlijke gevolgen, heeft recht op een duidelijke en zinvolle uitleg over de rol van het systeem in de besluitvorming en de belangrijkste elementen van het besluit
- Grondslag: art. 86 lid 1 AI-verordening
- Alleen als: `facts.decisions_about_persons != false and facts.high_risk_basis != "annex1" and facts.annex3_area != "critical_infrastructure"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: decisions_about_persons, explanation_procedure
- Beoordeling:
  - Art. 86 geeft een recht aan de betrokkene; een vaste procedure is niet voorgeschreven, maar zonder procedure kun je het verzoek niet beantwoorden. Daarom niet verplicht: ontbreken geeft review.
  - present als explanation_procedure true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Kan de organisatie op verzoek een duidelijke en zinvolle uitleg geven over de rol van het systeem en de belangrijkste elementen van het besluit (art. 86)?
- Advies bij ❌ of ⚠️: Leg vast hoe je een verzoek om uitleg beantwoordt: wie het oppakt, welke informatie over de rol van het systeem je geeft en wat de belangrijkste redenen voor het besluit waren. Vraag de leverancier welke informatie hij daarvoor levert.
- Bronnen: AIVO-art86-lid1 (AI-verordening art. 86 lid 1)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): system_name. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Wanneer dit geldt: de plichten van dit kader (hoofdstuk III, afdeling 1 tot en met 3) gelden vanaf 2 december 2027 voor hoogrisicosystemen uit bijlage III en vanaf 2 augustus 2028 voor systemen uit bijlage I (art. 113 zoals gewijzigd bij Verordening (EU) 2026/1744). Tot die datum is een ❌ een voorbereidingspunt: de rekenhulp maakt er een ⚠️ met de datum van ('Van toepassing vanaf'). Een systeem dat vóór die datum in de handel of in gebruik is, valt er alleen onder als het ontwerp daarna ingrijpend verandert; een systeem dat bedoeld is voor overheidsinstanties moet uiterlijk 2 augustus 2030 voldoen (art. 111 lid 2). Noem dit in het rapport als het systeem al vóór de datum in gebruik is.
- Stap 10 en 12 zijn niet verplicht; ontbreken geeft review.

## Samenhang met andere kaders

- Kader AI6 (/toets-ai-act-hoog-risico) — als `(facts.deployer_type != "other" and facts.annex3_area != "critical_infrastructure") or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance"`: Als overheid, als bedrijf dat een openbare dienst levert, of bij kredietscores en levens- en ziektekostenverzekeringen moet je vóór het eerste gebruik een grondrechtentoets doen (art. 27).
- Kader AI7 (/toets-ai-act-hoog-risico) — als `facts.role_change_name == true or facts.role_change_modification == true or facts.role_change_purpose == true`: Door je eigen naam op het systeem te zetten, het wezenlijk te wijzigen of het voor een ander doel te gebruiken, word je zelf aanbieder en gelden de aanbiedersplichten (art. 25 lid 1).
- Kader K9 (/dpia) — als `facts.personal_data != false`: Verwerkt het systeem persoonsgegevens, dan is een DPIA vrijwel altijd nodig; gebruik daarvoor de informatie van de aanbieder (art. 26 lid 9).
- Kader K16 (/toets-geautomatiseerde-besluiten) — als `facts.decisions_about_persons != false`: Besluiten over personen met hulp van het systeem kunnen ook onder de AVG-regels voor geautomatiseerde besluiten vallen (art. 22 AVG).

## Open punten en voorbehouden

- Officiële tekst van art. 25, 26, 49 en 86 zoals gewijzigd bij Vo. (EU) 2026/1744 nalezen; de huidige criteria volgen de oorspronkelijke tekst en drie secundaire bronnen die zeggen dat art. 26 en 27 inhoudelijk niet zijn gewijzigd.
- Art. 26 lid 10 (biometrische identificatie achteraf door rechtshandhaving) en lid 12 (samenwerking met autoriteiten) zijn niet opgenomen: buiten de doelgroep en niet als feit te toetsen.
- Art. 111 lid 2 (systemen die vóór de toepassingsdatum in de handel zijn gebracht) nog verwerken: bepaalt of de plichten gelden voor een bestaand systeem zonder ingrijpende wijziging. Datum na de Omnibus controleren.
- Welke markttoezichtautoriteit in Nederland bevoegd is, hangt af van de Uitvoeringswet AI-verordening; nog niet genoemd.
