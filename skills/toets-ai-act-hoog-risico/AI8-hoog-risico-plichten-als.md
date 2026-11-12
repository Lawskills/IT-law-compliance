# Kader AI8 — Hoog risico: plichten als importeur of distributeur (art. 23 en 24)

Versie 0.4 · peildatum 2026-11-10

Doel: Controleren of een importeur (brengt een systeem van een aanbieder buiten de EU op de EU-markt) of distributeur (levert een systeem door zonder aanbieder of importeur te zijn) vóór het leveren de vereiste controles doet, niet-conforme systemen tegenhoudt, de juiste gegevens vermeldt, documentatie bewaart en bij risico's meldt.

Van toepassing vanaf: 2027-12-02 als `facts.high_risk_basis == "annex3"`; 2028-08-02 als `facts.high_risk_basis == "annex1"` — art. 113, derde alinea, onder c, zoals gewijzigd bij Verordening (EU) 2026/1744

Bronnen: AIVO-art3-6 (AI-verordening art. 3 punt 6); AIVO-art3-7 (AI-verordening art. 3 punt 7); AIVO-art23-lid1 (AI-verordening art. 23 lid 1); AIVO-art23-lid2 (AI-verordening art. 23 lid 2); AIVO-art23-lid3 (AI-verordening art. 23 lid 3); AIVO-art23-lid4 (AI-verordening art. 23 lid 4); AIVO-art23-lid5 (AI-verordening art. 23 lid 5); AIVO-art24-lid1 (AI-verordening art. 24 lid 1); AIVO-art24-lid2 (AI-verordening art. 24 lid 2); AIVO-art24-lid3 (AI-verordening art. 24 lid 3); AIVO-art24-lid4 (AI-verordening art. 24 lid 4); AIVO-art25-lid1 (AI-verordening art. 25 lid 1); AIVO-art113 (AI-verordening art. 113); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI)); AIVO-art111-lid2 (AI-verordening art. 111 lid 2)

## Formulier (vragen aan de gebruiker)

- **system_name**: Om welk AI-systeem gaat het, en wie is de aanbieder?
  - Label (voor de plek-om-in-te-vullen): welk systeem het is
  - Type: text
- **operator_role**: Welke rol heb je bij dit systeem?
  - Label (voor de plek-om-in-te-vullen): of je importeur of distributeur bent
  - Type: enum (importer / distributor)
- **high_risk_basis**: Waarom is dit systeem hoog risico?
  - Label (voor de plek-om-in-te-vullen): waarom het systeem hoog risico is
  - Type: enum (annex3 / annex1)
- **own_name_on_system**: Zet je je eigen naam of merk op het systeem?
  - Label (voor de plek-om-in-te-vullen): of je je eigen naam of merk op het systeem zet
  - Type: boolean
- **checked_conformity_assessment**: Heb je vóór het leveren gecontroleerd dat de aanbieder de conformiteitsbeoordeling heeft gedaan?
  - Label (voor de plek-om-in-te-vullen): of je hebt gecontroleerd dat de aanbieder de conformiteitsbeoordeling heeft gedaan
  - Type: boolean · Alleen vragen als: `facts.operator_role != "distributor"`
- **checked_technical_documentation**: Heb je gecontroleerd dat de aanbieder de technische documentatie heeft opgesteld?
  - Label (voor de plek-om-in-te-vullen): of je hebt gecontroleerd dat de technische documentatie er is
  - Type: boolean · Alleen vragen als: `facts.operator_role != "distributor"`
- **checked_authorised_rep**: Heb je gecontroleerd dat de aanbieder een gemachtigde in de EU heeft aangewezen?
  - Label (voor de plek-om-in-te-vullen): of je hebt gecontroleerd dat de aanbieder een gemachtigde in de EU heeft
  - Type: boolean · Alleen vragen als: `facts.operator_role != "distributor"`
- **checked_ce_declaration_instructions**: Heb je gecontroleerd dat het systeem de CE-markering heeft en dat de EU-conformiteitsverklaring en de gebruiksaanwijzing erbij zitten?
  - Label (voor de plek-om-in-te-vullen): of je CE-markering, conformiteitsverklaring en gebruiksaanwijzing hebt gecontroleerd
  - Type: boolean
- **checked_upstream_obligations**: Heb je gecontroleerd dat de aanbieder en (als die er is) de importeur hun naam en contactgegevens vermelden en een kwaliteitsbeheersysteem hebben?
  - Label (voor de plek-om-in-te-vullen): of je hebt gecontroleerd dat aanbieder en importeur hun plichten nakomen
  - Type: boolean · Alleen vragen als: `facts.operator_role != "importer"`
- **nonconformity_procedure**: Is vastgelegd dat je een systeem dat niet voldoet niet levert, en dat je bij een risico de aanbieder (en bij import ook de gemachtigde en de toezichthouder) informeert?
  - Label (voor de plek-om-in-te-vullen): of je een procedure hebt voor systemen die niet voldoen
  - Type: boolean
- **importer_details_on_system**: Staan je naam, handelsnaam of merk en je contactadres als importeur op het systeem, de verpakking of de documentatie?
  - Label (voor de plek-om-in-te-vullen): of je naam en contactadres als importeur op het systeem staan
  - Type: boolean · Alleen vragen als: `facts.operator_role != "distributor"`
- **storage_transport_ok**: Zorg je dat opslag of vervoer (bijvoorbeeld van hardware of installatiebestanden) niets aan het systeem verandert?
  - Label (voor de plek-om-in-te-vullen): of opslag en vervoer de naleving niet in gevaar brengen
  - Type: boolean
- **importer_keeps_documents**: Bewaar je kopieën van het certificaat van de aangemelde instantie (als dat er is), de gebruiksaanwijzing en de EU-conformiteitsverklaring tien jaar?
  - Label (voor de plek-om-in-te-vullen): of je als importeur de documenten tien jaar bewaart
  - Type: boolean · Alleen vragen als: `facts.operator_role != "distributor"`
- **distributor_corrective_actions**: Is vastgelegd dat je een al geleverd systeem dat niet voldoet laat corrigeren, uit de handel neemt of terugroept, en bij een risico de aanbieder of importeur en de toezichthouder direct informeert?
  - Label (voor de plek-om-in-te-vullen): of je als distributeur corrigerende maatregelen neemt bij een systeem dat al geleverd is
  - Type: boolean · Alleen vragen als: `facts.operator_role != "importer"`

## Toetspunten

### AI8.1 — Of je zelf aanbieder wordt door je eigen naam op het systeem
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Een importeur of distributeur die zijn naam of merk op een hoogrisicosysteem zet, wordt aanbieder
- Grondslag: art. 25 lid 1 sub a AI-verordening
- Alleen als: `facts.own_name_on_system != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: own_name_on_system
- Beoordeling:
  - Altijd review. Vermeld dat dan de plichten van de aanbieder gelden (kader AI7).
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Geldt de importeur of distributeur door zijn naam of merk als aanbieder (art. 25 lid 1 sub a)?
- Advies bij ❌ of ⚠️: Zet je je eigen naam of merk op het systeem, dan ben je aanbieder. Doe dan de check 'Hoog risico: plichten als aanbieder' en maak afspraken met de oorspronkelijke aanbieder.
- Bronnen: AIVO-art25-lid1 (AI-verordening art. 25 lid 1)

### AI8.2 — Of je als importeur vóór het leveren alles hebt gecontroleerd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Vóór het in de handel brengen controleert de importeur dat (a) de aanbieder de conformiteitsbeoordeling heeft uitgevoerd, (b) de technische documentatie is opgesteld, (c) het systeem de CE-markering heeft en vergezeld gaat van de EU-conformiteitsverklaring en gebruiksaanwijzing, en (d) de aanbieder een gemachtigde heeft aangewezen
- Grondslag: art. 23 lid 1 AI-verordening
- Alleen als: `facts.operator_role != "distributor"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: operator_role, checked_conformity_assessment, checked_technical_documentation, checked_ce_declaration_instructions, checked_authorised_rep
- Beoordeling:
  - present als checked_conformity_assessment, checked_technical_documentation, checked_ce_declaration_instructions en checked_authorised_rep alle vier true zijn.
  - absent als een ervan false is; noem welke controle ontbreekt.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Controleer vóór je het systeem op de markt brengt: is de conformiteitsbeoordeling gedaan, is er technische documentatie, staat de CE-markering erop met verklaring en gebruiksaanwijzing, en is er een gemachtigde in de EU? Leg de controle vast.
- Bronnen: AIVO-art23-lid1 (AI-verordening art. 23 lid 1)

### AI8.3 — Of je als distributeur vóór het leveren alles hebt gecontroleerd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Vóór het op de markt aanbieden controleert de distributeur of het systeem de CE-markering heeft, vergezeld gaat van de EU-conformiteitsverklaring en gebruiksaanwijzing, en of de aanbieder en de importeur hun plichten (art. 16 sub b en c, art. 23 lid 3) zijn nagekomen
- Grondslag: art. 24 lid 1 AI-verordening
- Alleen als: `facts.operator_role != "importer"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: operator_role, checked_ce_declaration_instructions, checked_upstream_obligations
- Beoordeling:
  - present als checked_ce_declaration_instructions en checked_upstream_obligations beide true zijn.
  - absent als een van beide false is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Controleer vóór levering de CE-markering, de EU-conformiteitsverklaring en de gebruiksaanwijzing, en of aanbieder en importeur hun naam en contactgegevens vermelden en kwaliteitsbeheer hebben. Leg de controle vast.
- Bronnen: AIVO-art24-lid1 (AI-verordening art. 24 lid 1)

### AI8.4 — Of je systemen die niet voldoen tegenhoudt en risico's meldt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Heeft de importeur of distributeur reden om aan te nemen dat het systeem niet voldoet, dan brengt hij het niet in de handel of op de markt tot het in overeenstemming is; bij een risico (art. 79 lid 1) informeert de importeur de aanbieder, de gemachtigde en de markttoezichtautoriteiten, en de distributeur de aanbieder of importeur
- Grondslag: art. 23 lid 2 en art. 24 lid 2 AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: nonconformity_procedure
- Beoordeling:
  - present als nonconformity_procedure true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg vast dat je een systeem dat niet voldoet niet levert tot het is gecorrigeerd, en wie je bij een risico informeert.
- Bronnen: AIVO-art23-lid2 (AI-verordening art. 23 lid 2); AIVO-art24-lid2 (AI-verordening art. 24 lid 2)

### AI8.5 — Of je gegevens als importeur op het systeem staan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De importeur vermeldt zijn naam, geregistreerde handelsnaam of merk en contactadres op het systeem en op de verpakking of in de documentatie
- Grondslag: art. 23 lid 3 AI-verordening
- Alleen als: `facts.operator_role != "distributor"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: importer_details_on_system
- Beoordeling:
  - present als importer_details_on_system true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zet je naam of merk en je contactadres als importeur op het systeem en in de verpakking of documentatie.
- Bronnen: AIVO-art23-lid3 (AI-verordening art. 23 lid 3)

### AI8.6 — Of opslag en vervoer het systeem niet aantasten
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Zolang het systeem onder zijn verantwoordelijkheid valt, zorgt de importeur of distributeur dat opslag- of vervoersomstandigheden de naleving van de eisen niet in gevaar brengen
- Grondslag: art. 23 lid 4 en art. 24 lid 3 AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: storage_transport_ok
- Beoordeling:
  - present als storage_transport_ok true is; absent als false.
  - Voor puur digitale levering is deze plicht beperkt; daarom niet verplicht in deze toets: ontbreken geeft review.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Advies bij ❌ of ⚠️: Zorg dat opslag en vervoer van hardware of installatiebestanden niets aan het systeem veranderen, bijvoorbeeld met controlegetallen bij downloads.
- Bronnen: AIVO-art23-lid4 (AI-verordening art. 23 lid 4); AIVO-art24-lid3 (AI-verordening art. 24 lid 3)

### AI8.7 — Of je als importeur de documenten tien jaar bewaart
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De importeur bewaart tien jaar na het in de handel brengen een kopie van het certificaat van de aangemelde instantie (waar van toepassing), de gebruiksaanwijzing en de EU-conformiteitsverklaring
- Grondslag: art. 23 lid 5 AI-verordening
- Alleen als: `facts.operator_role != "distributor"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: importer_keeps_documents
- Beoordeling:
  - present als importer_keeps_documents true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Bewaar tien jaar een kopie van de gebruiksaanwijzing, de EU-conformiteitsverklaring en (als die er is) het certificaat van de aangemelde instantie.
- Bronnen: AIVO-art23-lid5 (AI-verordening art. 23 lid 5)

### AI8.8 — Of je als distributeur ingrijpt bij een systeem dat al geleverd is
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Een distributeur die reden heeft om aan te nemen dat een door hem geleverd systeem niet voldoet, neemt corrigerende maatregelen, neemt het uit de handel of roept het terug (of zorgt dat de aanbieder, importeur of een betrokken operator dat doet), en informeert bij een risico onmiddellijk de aanbieder of importeur en de bevoegde autoriteiten
- Grondslag: art. 24 lid 4 AI-verordening
- Alleen als: `facts.operator_role != "importer"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: distributor_corrective_actions
- Beoordeling:
  - present als distributor_corrective_actions true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg vast wat je doet als een geleverd systeem niet voldoet: laten corrigeren, uit de handel nemen of terugroepen, en wie je bij een risico direct informeert.
- Bronnen: AIVO-art24-lid4 (AI-verordening art. 24 lid 4)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): system_name. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.


## Regels van dit kader

- Wanneer dit geldt: de plichten van dit kader (hoofdstuk III, afdeling 1 tot en met 3) gelden vanaf 2 december 2027 voor hoogrisicosystemen uit bijlage III en vanaf 2 augustus 2028 voor systemen uit bijlage I (art. 113 zoals gewijzigd bij Verordening (EU) 2026/1744). Tot die datum is een ❌ een voorbereidingspunt: de rekenhulp maakt er een ⚠️ met de datum van ('Van toepassing vanaf'). Een systeem dat vóór die datum in de handel of in gebruik is, valt er alleen onder als het ontwerp daarna ingrijpend verandert; een systeem dat bedoeld is voor overheidsinstanties moet uiterlijk 2 augustus 2030 voldoen (art. 111 lid 2). Noem dit in het rapport als het systeem al vóór de datum in gebruik is.

## Samenhang met andere kaders

- Kader AI7 (/toets-ai-act-hoog-risico) — als `facts.own_name_on_system == true`: Wie zijn eigen naam of merk op een hoogrisicosysteem zet, wordt zelf aanbieder (art. 25 lid 1 sub a).

## Open punten en voorbehouden

- Art. 23 lid 6-7 en art. 24 lid 5-6 (informatie op verzoek, samenwerking met autoriteiten) niet als stap opgenomen.
- Officiële tekst na de Omnibus nalezen.
