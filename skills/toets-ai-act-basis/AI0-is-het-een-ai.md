# Kader AI0 — Is het een AI-systeem, en welke rol heb je?

Versie 0.4 · peildatum 2026-11-10

Doel: Vaststellen of de AI-verordening op een toepassing van toepassing is (is het een AI-systeem, geldt er een uitzondering) en of de organisatie aanbieder of gebruiksverantwoordelijke is. Zonder deze basis zijn de verboden (AI1), het hoog-risicosignaal (AI2) en de transparantieplichten (AI4) niet te toetsen.

Bronnen: AIVO-art2-lid3 (AI-verordening art. 2 lid 3); AIVO-art2-lid6 (AI-verordening art. 2 lid 6); AIVO-art2-lid8 (AI-verordening art. 2 lid 8); AIVO-art2-lid12 (AI-verordening art. 2 lid 12); AIVO-art3-1 (AI-verordening art. 3 punt 1); AIVO-art3-3 (AI-verordening art. 3 punt 3); AIVO-art3-4 (AI-verordening art. 3 punt 4); AIVO-art3-6 (AI-verordening art. 3 punt 6); AIVO-art3-7 (AI-verordening art. 3 punt 7); AIVO-art3-11 (AI-verordening art. 3 punt 11); AIVO-art3-63 (AI-verordening art. 3 punt 63); AIVO-art3-68 (AI-verordening art. 3 punt 68); AIVO-art25-lid1 (AI-verordening art. 25 lid 1); AIVO-art53 (AI-verordening art. 53); AIVO-overw12 (AI-verordening overweging 12); EC-C-2025-924 (Richtsnoeren van de Commissie over de definitie van een AI-systeem, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

## Formulier (vragen aan de gebruiker)

- **app_name**: Hoe heet de toepassing?
  - Label (voor de plek-om-in-te-vullen): naam van de AI-toepassing
  - Hulp: Bijvoorbeeld ChatGPT, Microsoft Copilot, de chatbot op je website of de naam van je HR-tool.
  - Type: text
- **app_vendor**: Van welke leverancier is de toepassing? Heb je hem zelf gebouwd, vul dan je eigen organisatie in.
  - Label (voor de plek-om-in-te-vullen): leverancier van de toepassing
  - Type: text
- **app_purpose**: Waarvoor gebruik je de toepassing, en bij of over wie?
  - Label (voor de plek-om-in-te-vullen): waarvoor en bij wie je de toepassing gebruikt
  - Hulp: Bijvoorbeeld: 'Klantvragen beantwoorden op onze website', 'cv's van sollicitanten sorteren', 'teksten voor onze nieuwsbrief schrijven'.
  - Type: text
- **app_description**: Hoe werkt de toepassing, in gewone woorden?
  - Label (voor de plek-om-in-te-vullen): hoe de toepassing werkt
  - Hulp: Wat stop je erin, wat komt eruit, en wie bepaalt hoe het systeem van het een naar het ander komt? Bijvoorbeeld: 'Wij typen een vraag, het systeem schrijft zelf een antwoord' of 'Het systeem volgt een vaste beslisboom die wij hebben ingesteld'.
  - Type: text
- **system_infers**: Maakt de toepassing zelf voorspellingen, teksten, beelden, aanbevelingen of beslissingen op basis van wat zij uit gegevens heeft geleerd of afleidt?
  - Label (voor de plek-om-in-te-vullen): of de toepassing zelf voorspellingen, teksten, aanbevelingen of beslissingen afleidt
  - Hulp: Ja bij bijvoorbeeld chatbots op een taalmodel, beeldgeneratoren, spraakherkenning, scoringsmodellen en de meeste 'slimme' functies. Nee als de software alleen vaste regels uitvoert die een mens heeft bedacht (zoals 'als het bedrag hoger is dan 500 euro, dan...') of alleen rekent.
  - Type: boolean
- **art2_exception**: Gebruik je de toepassing uitsluitend voor een van deze doelen?
  - Label (voor de plek-om-in-te-vullen): of een uitzondering van de AI-verordening geldt
  - Hulp: Deze uitzonderingen zijn smal. Voor bijna alle organisaties is het antwoord 'Geen van deze'.
  - Type: enum (none / military_defence_security / scientific_research_only / pre_market_testing)
- **development_mode**: Welke omschrijving past het best?
  - Label (voor de plek-om-in-te-vullen): hoe je aan de toepassing komt
  - Type: enum (vendor_system / configured_on_platform / built_own / modified_system / finetuned_model / resell)
- **own_name**: Breng je het systeem onder je eigen naam of merk in gebruik of op de markt, ook als je het alleen intern gebruikt?
  - Label (voor de plek-om-in-te-vullen): of je het systeem onder je eigen naam of merk gebruikt of aanbiedt
  - Hulp: Bijvoorbeeld een chatbot op je website die als 'jouw' assistent wordt gepresenteerd, of een tool die je onder je merknaam aan klanten levert.
  - Type: boolean · Alleen vragen als: `facts.development_mode == "built_own" or facts.development_mode == "configured_on_platform" or facts.development_mode == "modified_system"`
- **processes_personal_data**: Komen er gegevens over personen in of uit de toepassing?
  - Label (voor de plek-om-in-te-vullen): of de toepassing persoonsgegevens verwerkt
  - Hulp: Bijvoorbeeld namen, e-mails, klantgesprekken, cv's, camerabeelden of stemopnames. Ook als je ze alleen in een vraag aan een chatbot plakt.
  - Type: boolean
- **affects_individuals**: Gebruik je de toepassing om beslissingen over individuele personen te nemen of voor te bereiden?
  - Label (voor de plek-om-in-te-vullen): of je de toepassing gebruikt voor beslissingen over personen
  - Hulp: Bijvoorbeeld welke sollicitant wordt uitgenodigd, welke klant krediet krijgt of welke prijs iemand betaalt.
  - Type: boolean

## Toetspunten

### AI0.1 — Of je toepassing een AI-systeem is
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De toepassing is een AI-systeem: een machinaal systeem dat met enige autonomie werkt en uit de invoer afleidt hoe het output genereert, zoals voorspellingen, inhoud, aanbevelingen of beslissingen
- Grondslag: art. 3 punt 1 AI-verordening; overweging 12
- Beoordeeld op: de antwoorden
- Nodig: system_infers, app_description
- Beoordeling:
  - Dit is een kwalificatiestap: 'compliant' betekent dat de kwalificatie (wel of geen AI-systeem) duidelijk vaststaat. Een duidelijk non_compliant geval bestaat bij deze stap niet.
  - Duidelijk geval (compliant): system_infers is true en app_description beschrijft een systeem dat zelf tekst, beeld, geluid, voorspellingen, scores, aanbevelingen of beslissingen genereert (bijvoorbeeld een taalmodel, beeldgenerator, spraak- of gezichtsherkenning, machine learning-model).
  - Duidelijk geval (compliant, kwalificatie: geen AI-systeem): system_infers is false en app_description beschrijft uitsluitend regels die door mensen zijn vastgesteld, eenvoudige berekeningen, sortering of databeheer, zonder dat het systeem zelf afleidt hoe het output genereert (overweging 12; richtsnoeren C(2025) 924).
  - system_infers false terwijl app_description wijst op een taalmodel, 'slimme' functie, scoring, herkenning of generatie: geen duidelijk geval.
  - system_infers true terwijl app_description alleen vaste regels of rekenwerk beschrijft: geen duidelijk geval.
  - In alle andere gevallen geen duidelijk geval.
  - Kwalificatie 'geen AI-systeem': de overige stappen van AI0 en de kaders AI1, AI2 en AI4 zijn voor deze toepassing niet van toepassing; AI3 blijft gelden als de organisatie andere AI-systemen gebruikt.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Leidt het systeem zelf af hoe het zijn output genereert, of voert het uitsluitend door mensen vastgestelde regels uit?
- Advies bij ❌ of ⚠️: Stel vast of de toepassing zelf output afleidt (bijvoorbeeld een taalmodel of scoringsmodel) of alleen vaste regels uitvoert. Vraag zo nodig de leverancier om uitleg over hoe het systeem werkt.
- Bronnen: AIVO-art3-1 (AI-verordening art. 3 punt 1); AIVO-overw12 (AI-verordening overweging 12); EC-C-2025-924 (Richtsnoeren van de Commissie over de definitie van een AI-systeem, vastgesteld bij Verordening (EU) 2024/1689 (AI-verordening))

### AI0.2 — Of een uitzondering van de AI-verordening geldt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Geen uitzondering van art. 2: niet uitsluitend militair, defensie of nationale veiligheid (lid 3), niet uitsluitend wetenschappelijk onderzoek en ontwikkeling (lid 6), geen onderzoek of test vóór het in de handel brengen of in gebruik stellen (lid 8)
- Grondslag: art. 2 lid 3, 6, 8 en 12 AI-verordening
- Alleen als: `facts.system_infers != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: art2_exception
- Beoordeling:
  - Kwalificatiestap: 'compliant' betekent dat duidelijk vaststaat dat er geen uitzondering geldt en de verordening dus van toepassing is.
  - Duidelijk geval (compliant): art2_exception is none.
  - Elk beroep op een uitzondering: geen duidelijk geval. De uitzonderingen zijn smal: lid 3 alleen bij uitsluitend militaire doeleinden, defensie of nationale veiligheid; lid 6 alleen bij uitsluitend wetenschappelijk onderzoek en ontwikkeling; lid 8 geldt niet voor testen onder reële omstandigheden en niet meer zodra het systeem in gebruik is.
  - Vrije en opensource-licenties (lid 12) zijn geen uitzondering voor verboden praktijken, transparantieplichten (art. 50) en hoog-risicosystemen; een beroep daarop verandert de uitkomst van AI1, AI2 en AI4 niet.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Wordt de toepassing echt uitsluitend gebruikt voor het genoemde doel, zodat de uitzondering van art. 2 geldt?
- Advies bij ❌ of ⚠️: Ga ervan uit dat de AI-verordening geldt, tenzij een juridisch adviseur bevestigt dat een van de smalle uitzonderingen van toepassing is.
- Bronnen: AIVO-art2-lid3 (AI-verordening art. 2 lid 3); AIVO-art2-lid6 (AI-verordening art. 2 lid 6); AIVO-art2-lid8 (AI-verordening art. 2 lid 8); AIVO-art2-lid12 (AI-verordening art. 2 lid 12)

### AI0.3 — Of je aanbieder of gebruiker bent
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De rol van de organisatie staat vast: aanbieder (ontwikkelt of laat ontwikkelen en brengt onder eigen naam in de handel of in gebruik) of gebruiksverantwoordelijke (gebruikt een systeem onder eigen verantwoordelijkheid)
- Grondslag: art. 3 punt 3, 4, 11 en 68 AI-verordening
- Alleen als: `facts.system_infers != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: development_mode
- Beoordeling:
  - Kwalificatiestap: 'compliant' betekent dat de rol duidelijk vaststaat. Een duidelijk non_compliant geval bestaat bij deze stap niet.
  - Duidelijk geval gebruiksverantwoordelijke (compliant): development_mode is vendor_system en app_description of app_vendor bevestigt dat een andere partij het systeem aanbiedt.
  - Duidelijk geval aanbieder (compliant): development_mode is built_own en own_name is true. Dit geldt ook als het systeem draait op een AI-model van een ander via een API (aanbieder van het AI-systeem, art. 3 punt 3 en 68) en ook bij uitsluitend eigen gebruik (in gebruik stellen, art. 3 punt 11).
  - development_mode configured_on_platform (eigen assistent of bot ingesteld binnen het platform van een leverancier): grijs gebied, geen duidelijk geval.
  - development_mode built_own met own_name false of onbekend: geen duidelijk geval.
  - development_mode modified_system, finetuned_model of resell: geen duidelijk geval; stap 4 beoordeelt dit verder.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Brengt de organisatie het systeem onder eigen naam of merk in de handel of in gebruik (aanbieder), of gebruikt zij een systeem van een ander (gebruiksverantwoordelijke)?
- Advies bij ❌ of ⚠️: Stel vast of je het systeem alleen gebruikt (gebruiksverantwoordelijke) of het zelf hebt gebouwd of laten bouwen en onder je eigen naam gebruikt of aanbiedt (aanbieder). Van die rol hangt af welke plichten voor jou gelden.
- Bronnen: AIVO-art3-3 (AI-verordening art. 3 punt 3); AIVO-art3-4 (AI-verordening art. 3 punt 4); AIVO-art3-11 (AI-verordening art. 3 punt 11); AIVO-art3-68 (AI-verordening art. 3 punt 68)

### AI0.4 — Of je door aanpassen of doorverkopen extra plichten krijgt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bij een aangepast systeem, een verder getraind model of doorverkoop: de rol en plichten zijn vastgesteld (art. 25 lid 1 alleen bij hoog risico; importeur of distributeur; aanbieder van een AI-model voor algemene doeleinden)
- Grondslag: art. 25 lid 1, art. 3 punt 6, 7 en 63 en art. 53 AI-verordening
- Alleen als: `facts.system_infers != false and (facts.development_mode == "modified_system" or facts.development_mode == "finetuned_model" or facts.development_mode == "resell" or facts.development_mode == null)` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: development_mode, app_description
- Beoordeling:
  - Deze stap geeft altijd review: de gevolgen hangen af van feiten die een juridisch adviseur moet beoordelen.
  - modified_system: art. 25 lid 1 maakt een distributeur, importeur, gebruiksverantwoordelijke of andere derde alleen bij een hoog-risicosysteem tot aanbieder: eigen naam of merk op een hoog-risicosysteem, een substantiële wijziging die het hoog risico laat, of een ander beoogd doel waardoor een systeem hoog risico wordt. Bij andere systemen volgt de rol uit art. 3 punt 3. Noem in de onderbouwing of er een bijlage III-signaal is (zie AI2).
  - finetuned_model: wie een AI-model voor algemene doeleinden van een ander wezenlijk verder traint en aanbiedt, kan zelf aanbieder van een AI-model worden (art. 3 punt 63, art. 53), met plichten sinds 2 augustus 2025.
  - resell: de organisatie is importeur (systeem van een aanbieder buiten de EU) of distributeur (art. 3 punt 6 en 7); de eigen plichten gelden vooral bij hoog-risicosystemen.
  - development_mode onbekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Wordt de organisatie door de aanpassing, het verder trainen of de doorverkoop aanbieder (art. 25 lid 1 bij hoog risico; art. 53 bij een AI-model voor algemene doeleinden), importeur of distributeur?
- Advies bij ❌ of ⚠️: Laat een juridisch adviseur beoordelen of je door de aanpassing, het verder trainen of het doorverkopen zelf aanbieder, importeur of distributeur bent, en welke plichten daarbij horen.
- Bronnen: AIVO-art25-lid1 (AI-verordening art. 25 lid 1); AIVO-art3-6 (AI-verordening art. 3 punt 6); AIVO-art3-7 (AI-verordening art. 3 punt 7); AIVO-art3-63 (AI-verordening art. 3 punt 63); AIVO-art53 (AI-verordening art. 53)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): app_name, app_purpose, app_description. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- AI0 geeft nooit non_compliant: het kwalificeert. 'compliant' = de kwalificatie staat vast.
- system_infers false → stap 2-4 not_applicable. AI1, AI2 en AI4 worden voor deze toepassing alleen not_applicable als stap 1 compliant is (duidelijk geen AI-systeem). Geeft stap 1 review (bijvoorbeeld 'nee' terwijl de beschrijving op een taalmodel wijst), dan blijven AI1, AI2 en AI4 in de route.
- Zo werkt dat in de rekenhulp: AI1, AI2 en AI4 hebben de poortregel `facts.system_infers != false` met poortstap AI0.1. Bij system_infers false vervallen hun vragen; wordt AI0.1 daarna niet ✅, dan meldt `kader.py uitkomst` dat die kaders niet zijn uitgesloten. Spreekt app_description het antwoord op system_infers tegen, vraag dat dan eerst één keer na; blijft de tegenspraak, zet system_infers op 'weet ik niet'. AI3 blijft op organisatieniveau gelden als er andere AI-systemen zijn.
- Rol onduidelijk of 'weet ik niet' → review.
- De rol uit stap 3 (ai_role) wordt doorgegeven aan AI4; bij review in stap 3 krijgt AI4 ai_role = null en eindigt de rolafhankelijke stap in review.

## Samenhang met andere kaders

- Kader K0 (/toets-toepasselijkheid-rol) — als `facts.processes_personal_data != false`: De toepassing verwerkt (mogelijk) persoonsgegevens; dan geldt ook de AVG.
- Kader K9 (/dpia) — als `facts.processes_personal_data != false and facts.system_infers != false`: Een AI-toepassing telt als innovatieve technologie bij de vraag of een DPIA verplicht is.
- Kader K16 (/toets-geautomatiseerde-besluiten) — als `facts.affects_individuals == true`: De toepassing wordt gebruikt voor beslissingen over personen; dan gelden mogelijk de regels voor geautomatiseerde besluiten.

## Open punten en voorbehouden

- Eigen assistent binnen een leveranciersplatform (bijvoorbeeld een eigen GPT): de rolverdeling is niet door de Commissie verduidelijkt; na nieuwe richtsnoeren de criteria van stap 3 aanscherpen.
