# Kader AI7 — Hoog risico: plichten als aanbieder (art. 16)

Versie 0.4 · peildatum 2026-11-10

Doel: Controleren of een aanbieder van een hoogrisico-AI-systeem de plichten van art. 16 AI-verordening heeft ingericht: de eisen aan het systeem (art. 9-15), kwaliteitsbeheer, documentatie en logs, conformiteitsbeoordeling, verklaring, CE-markering, registratie, corrigerende maatregelen, monitoring na het in de handel brengen en het melden van ernstige incidenten.

Van toepassing vanaf: 2027-12-02 als `facts.high_risk_basis == "annex3"`; 2028-08-02 als `facts.high_risk_basis == "annex1"` — art. 113, derde alinea, onder c, zoals gewijzigd bij Verordening (EU) 2026/1744

Bronnen: AIVO-art3-3 (AI-verordening art. 3 punt 3); AIVO-art9-lid1 (AI-verordening art. 9 lid 1); AIVO-art9-lid2 (AI-verordening art. 9 lid 2); AIVO-art10-lid2 (AI-verordening art. 10 lid 2); AIVO-art10-lid3 (AI-verordening art. 10 lid 3); AIVO-art11-lid1 (AI-verordening art. 11 lid 1); AIVO-art12-lid1 (AI-verordening art. 12 lid 1); AIVO-art13-lid1 (AI-verordening art. 13 lid 1); AIVO-art13-lid3 (AI-verordening art. 13 lid 3); AIVO-art14-lid1 (AI-verordening art. 14 lid 1); AIVO-art15-lid1 (AI-verordening art. 15 lid 1); AIVO-art15-lid3 (AI-verordening art. 15 lid 3); AIVO-art16 (AI-verordening art. 16); AIVO-art17-lid1 (AI-verordening art. 17 lid 1); AIVO-art17-lid2 (AI-verordening art. 17 lid 2); AIVO-art18-lid1 (AI-verordening art. 18 lid 1); AIVO-art19-lid1 (AI-verordening art. 19 lid 1); AIVO-art20-lid1 (AI-verordening art. 20 lid 1); AIVO-art22-lid1 (AI-verordening art. 22 lid 1); AIVO-art43-lid1 (AI-verordening art. 43 lid 1); AIVO-art43-lid2 (AI-verordening art. 43 lid 2); AIVO-art47-lid1 (AI-verordening art. 47 lid 1); AIVO-art48-lid1 (AI-verordening art. 48 lid 1); AIVO-art49-lid1 (AI-verordening art. 49 lid 1); AIVO-art72-lid1 (AI-verordening art. 72 lid 1); AIVO-art73-lid1 (AI-verordening art. 73 lid 1); AIVO-art73-lid2 (AI-verordening art. 73 lid 2); AIVO-art73-lid3 (AI-verordening art. 73 lid 3); AIVO-art73-lid4 (AI-verordening art. 73 lid 4); AIVO-art4a (AI-verordening art. 4a); AIVO-bijlage4 (AI-verordening bijlage IV); AIVO-art113 (AI-verordening art. 113); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI)); AIVO-art111-lid2 (AI-verordening art. 111 lid 2)

## Formulier (vragen aan de gebruiker)

- **system_name**: Om welk AI-systeem gaat het, en waarvoor is het bedoeld?
  - Label (voor de plek-om-in-te-vullen): welk systeem het is
  - Type: text
- **high_risk_basis**: Waarom is dit systeem hoog risico?
  - Label (voor de plek-om-in-te-vullen): waarom het systeem hoog risico is
  - Type: enum (annex3 / annex1)
- **biometric_system**: Is het een systeem voor biometrie: mensen op afstand herkennen, indelen naar gevoelige kenmerken, of emoties herkennen?
  - Label (voor de plek-om-in-te-vullen): of het een biometrisch systeem is (bijlage III punt 1)
  - Type: boolean · Alleen vragen als: `facts.high_risk_basis != "annex1"`
- **harmonised_standards_applied**: Pas je voor alle eisen geharmoniseerde Europese normen of gemeenschappelijke specificaties toe?
  - Label (voor de plek-om-in-te-vullen): of je volledig geharmoniseerde normen of gemeenschappelijke specificaties toepast
  - Type: boolean · Alleen vragen als: `facts.biometric_system != false and facts.high_risk_basis != "annex1"`
- **established_in_eu**: Is je organisatie in de EU gevestigd?
  - Label (voor de plek-om-in-te-vullen): of je in de EU bent gevestigd
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **sme**: Heeft je organisatie minder dan 750 medewerkers?
  - Label (voor de plek-om-in-te-vullen): of je een kmo of small mid-cap bent
  - Hulp: Kleinere organisaties mogen technische documentatie en kwaliteitsbeheer in vereenvoudigde vorm opzetten. De precieze grenzen staan in de aanbeveling van de Commissie en de Omnibus; controleer of je eronder valt.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **risk_management**: Heb je een vastgelegd proces dat de risico's van het systeem vaststelt, beoordeelt en beperkt, met tests, en dat je de hele levensduur bijhoudt?
  - Label (voor de plek-om-in-te-vullen): of je een systeem voor risicobeheer hebt dat de hele levensduur loopt
  - Type: boolean
- **trains_with_data**: Wordt het model met data getraind, gevalideerd of getest?
  - Label (voor de plek-om-in-te-vullen): of het systeem met data wordt getraind
  - Type: boolean
- **data_governance**: Leg je vast waar de data vandaan komen, hoe je ze voorbereidt, of ze representatief en zo foutloos en volledig mogelijk zijn, en hoe je vooroordelen opspoort en beperkt?
  - Label (voor de plek-om-in-te-vullen): of je afspraken hebt over de kwaliteit van trainings-, validatie- en testdata
  - Type: boolean · Alleen vragen als: `facts.trains_with_data != false`
- **trains_with_personal_data**: Zitten er persoonsgegevens in die data?
  - Label (voor de plek-om-in-te-vullen): of in de data persoonsgegevens zitten
  - Type: boolean · Alleen vragen als: `facts.trains_with_data != false`
- **technical_documentation**: Heb je de technische documentatie opgesteld met de onderdelen die bijlage IV noemt, vóór het in de handel brengen, en houd je die bij?
  - Label (voor de plek-om-in-te-vullen): of de technische documentatie volgens bijlage IV klaar is
  - Type: boolean
- **automatic_logging**: Legt het systeem tijdens het gebruik automatisch gebeurtenissen vast (logs), zodat je de werking achteraf kunt nagaan?
  - Label (voor de plek-om-in-te-vullen): of het systeem automatisch gebeurtenissen vastlegt
  - Type: boolean
- **instructions_for_use**: Heb je een gebruiksaanwijzing voor gebruikers, met je contactgegevens, het doel, de nauwkeurigheid en bekende beperkingen, het menselijk toezicht en hoe logs worden bewaard?
  - Label (voor de plek-om-in-te-vullen): of er een gebruiksaanwijzing is met de verplichte inhoud
  - Type: boolean
- **human_oversight_design**: Is het systeem zo gebouwd dat een mens de uitkomsten kan begrijpen, kan negeren of terugdraaien, en het systeem kan stoppen?
  - Label (voor de plek-om-in-te-vullen): of het systeem is ontworpen voor menselijk toezicht
  - Type: boolean
- **accuracy_robustness_security**: Heb je nauwkeurigheid, bestendigheid tegen fouten en beveiliging (ook tegen manipulatie van data of model) getest, en staan de nauwkeurigheidscijfers in de gebruiksaanwijzing?
  - Label (voor de plek-om-in-te-vullen): of je nauwkeurigheid, robuustheid en beveiliging hebt getest en de nauwkeurigheid vermeldt
  - Type: boolean
- **quality_management**: Heb je een vastgelegd kwaliteitsbeheersysteem voor dit AI-systeem: beleid, procedures voor ontwerp, tests, data, risicobeheer, monitoring, incidenten en verantwoordelijkheden?
  - Label (voor de plek-om-in-te-vullen): of je een systeem voor kwaliteitsbeheer hebt
  - Type: boolean
- **documentation_retention**: Bewaar je de technische documentatie, het kwaliteitsbeheer, de conformiteitsverklaring en eventuele besluiten van de aangemelde instantie tien jaar na het in de handel brengen?
  - Label (voor de plek-om-in-te-vullen): of je de documentatie tien jaar bewaart
  - Type: boolean
- **logs_control**: Komen de automatisch gemaakte logs bij jou terecht (bijvoorbeeld omdat je het systeem als dienst levert)?
  - Label (voor de plek-om-in-te-vullen): of de logs onder jouw beheer staan
  - Type: boolean
- **logs_retention_months**: Hoeveel maanden bewaar je die logs?
  - Label (voor de plek-om-in-te-vullen): hoe lang je de logs bewaart (in maanden)
  - Type: number · Alleen vragen als: `facts.logs_control != false`
- **conformity_assessment**: Heb je de conformiteitsbeoordeling gedaan vóór het in de handel brengen of in gebruik stellen (zelf via interne controle, of met een aangemelde instantie waar dat moet)?
  - Label (voor de plek-om-in-te-vullen): of de conformiteitsbeoordeling is gedaan
  - Type: boolean
- **notified_body_used**: Heeft een aangemelde instantie de beoordeling gedaan?
  - Label (voor de plek-om-in-te-vullen): of een aangemelde instantie de beoordeling heeft gedaan
  - Type: boolean · Alleen vragen als: `facts.conformity_assessment != false`
- **eu_declaration**: Heb je een EU-conformiteitsverklaring opgesteld en ondertekend?
  - Label (voor de plek-om-in-te-vullen): of je een EU-conformiteitsverklaring hebt opgesteld
  - Type: boolean
- **ce_marking**: Staat de CE-markering op het systeem (of, bij een digitaal systeem, digitaal of op de verpakking of documentatie)?
  - Label (voor de plek-om-in-te-vullen): of de CE-markering is aangebracht
  - Type: boolean
- **name_on_system**: Staan je naam, handelsnaam of merk en je contactadres op het systeem, of anders op de verpakking of documentatie?
  - Label (voor de plek-om-in-te-vullen): of je naam en contactadres op het systeem staan
  - Type: boolean
- **eu_registration**: Heb je jezelf en het systeem geregistreerd in de EU-databank voordat het in de handel kwam?
  - Label (voor de plek-om-in-te-vullen): of het systeem in de EU-databank is geregistreerd
  - Type: boolean · Alleen vragen als: `facts.high_risk_basis != "annex1"`
- **corrective_actions_procedure**: Is vastgelegd wat je doet als het systeem niet (meer) voldoet: corrigeren, uit de handel nemen of terugroepen, en gebruikers en toezichthouders informeren?
  - Label (voor de plek-om-in-te-vullen): of je een procedure hebt voor corrigerende maatregelen
  - Type: boolean
- **post_market_monitoring**: Heb je een plan om na de levering actief gegevens te verzamelen over hoe het systeem presteert, en dat plan in de technische documentatie opgenomen?
  - Label (voor de plek-om-in-te-vullen): of je een plan hebt voor monitoring na het in de handel brengen
  - Type: boolean
- **incident_reporting**: Heb je een procedure om ernstige incidenten te melden aan de markttoezichtautoriteit, met de wettelijke termijnen (uiterlijk 15 dagen, 10 dagen bij overlijden, 2 dagen bij een wijdverbreide inbreuk of ernstige verstoring van kritieke infrastructuur)?
  - Label (voor de plek-om-in-te-vullen): of je een procedure hebt om ernstige incidenten op tijd te melden
  - Type: boolean
- **accessibility**: Voldoet het systeem aan de Europese toegankelijkheidseisen voor mensen met een beperking?
  - Label (voor de plek-om-in-te-vullen): of het systeem voldoet aan de toegankelijkheidseisen
  - Type: boolean
- **authorised_representative**: Heb je schriftelijk een gemachtigde in de EU aangewezen?
  - Label (voor de plek-om-in-te-vullen): of je een gemachtigde in de EU hebt aangewezen
  - Type: boolean · Alleen vragen als: `facts.established_in_eu != true`
- **interacts_with_persons**: Communiceert het systeem rechtstreeks met mensen, of maakt het tekst, beeld of geluid?
  - Label (voor de plek-om-in-te-vullen): of het systeem met mensen communiceert of inhoud maakt
  - Type: boolean

## Toetspunten

### AI7.1 — Of je de risico's beheerst gedurende de hele levensduur
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Er is een systeem voor risicobeheer vastgesteld, uitgevoerd, gedocumenteerd en in stand gehouden: een doorlopend, iteratief proces over de hele levensduur, met het vaststellen en beoordelen van risico's, maatregelen en tests
- Grondslag: art. 9 lid 1 en 2 AI-verordening; art. 16 sub a
- Beoordeeld op: de antwoorden
- Nodig: risk_management
- Beoordeling:
  - present als risk_management true is; absent als false. Deze skill beoordeelt niet of het risicobeheer inhoudelijk volstaat.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Richt een vastgelegd proces in om de risico's van het systeem vast te stellen, te beoordelen en te beperken, met tests vóór levering, en houd het bij zolang het systeem wordt gebruikt.
- Bronnen: AIVO-art9-lid1 (AI-verordening art. 9 lid 1); AIVO-art9-lid2 (AI-verordening art. 9 lid 2); AIVO-art16 (AI-verordening art. 16)

### AI7.2 — Of je de kwaliteit van je trainings- en testdata bewaakt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Trainings-, validatie- en testdata voldoen aan de kwaliteitscriteria van art. 10 lid 2-4: praktijken voor databeheer (herkomst, voorbereiding, aannames, beschikbaarheid), onderzoek naar en beperking van vooroordelen, en data die relevant, voldoende representatief en zoveel mogelijk foutloos en volledig zijn
- Grondslag: art. 10 lid 2 en 3 AI-verordening; art. 4a (sinds Vo. (EU) 2026/1744, voor bijzondere persoonsgegevens om vooroordelen op te sporen)
- Alleen als: `facts.trains_with_data != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: trains_with_data, data_governance
- Beoordeling:
  - present als data_governance true is; absent als false.
  - Gebruikt de aanbieder bijzondere persoonsgegevens om vooroordelen op te sporen: dat mag alleen onder de voorwaarden van art. 4a (vroeger art. 10 lid 5), waaronder dat het doel niet met andere, synthetische of geanonimiseerde data kan worden bereikt. Noem dat als trains_with_personal_data true is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg per dataset vast waar de data vandaan komen, hoe je ze hebt voorbereid, of ze passen bij de groep mensen waarop het systeem wordt toegepast, en hoe je vooroordelen opspoort en beperkt.
- Bronnen: AIVO-art10-lid2 (AI-verordening art. 10 lid 2); AIVO-art10-lid3 (AI-verordening art. 10 lid 3); AIVO-art4a (AI-verordening art. 4a); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI7.3 — Of de technische documentatie klaar is
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De technische documentatie is opgesteld vóór het in de handel brengen of in gebruik stellen, wordt actueel gehouden en bevat ten minste de elementen van bijlage IV; kmo's (en sinds de Omnibus small mid-caps) mogen een vereenvoudigde vorm gebruiken
- Grondslag: art. 11 lid 1 en bijlage IV AI-verordening; art. 16 sub a
- Beoordeeld op: de antwoorden
- Nodig: technical_documentation
- Beoordeling:
  - present als technical_documentation true is; absent als false.
  - Is sme true: vermeld dat een vereenvoudigde vorm met het model van de Commissie mag.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Stel de technische documentatie op met de onderdelen van bijlage IV: beschrijving van het systeem en het ontwerp, data, tests en prestaties, risicobeheer, menselijk toezicht en het monitoringsplan. Houd haar actueel.
- Bronnen: AIVO-art11-lid1 (AI-verordening art. 11 lid 1); AIVO-bijlage4 (AI-verordening bijlage IV); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI7.4 — Of het systeem automatisch logt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het systeem maakt het technisch mogelijk om gedurende de levensduur automatisch gebeurtenissen (logs) te registreren, passend bij het beoogde doel
- Grondslag: art. 12 lid 1 AI-verordening; art. 16 sub a
- Beoordeeld op: de antwoorden
- Nodig: automatic_logging
- Beoordeling:
  - present als automatic_logging true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Bouw automatische logging in: welke invoer, uitkomst en tijd bij elk gebruik, zodat risico's en ingrijpende wijzigingen achteraf zijn na te gaan.
- Bronnen: AIVO-art12-lid1 (AI-verordening art. 12 lid 1)

### AI7.5 — Of gebruikers een volledige gebruiksaanwijzing krijgen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het systeem is voldoende transparant voor gebruiksverantwoordelijken en gaat vergezeld van een gebruiksaanwijzing met beknopte, volledige, juiste en duidelijke informatie, waaronder identiteit en contactgegevens van de aanbieder, kenmerken, capaciteiten en beperkingen, nauwkeurigheid, menselijk toezicht en logbeheer
- Grondslag: art. 13 lid 1 en 3 AI-verordening; art. 16 sub a
- Beoordeeld op: de antwoorden
- Nodig: instructions_for_use
- Beoordeling:
  - present als instructions_for_use true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Maak een gebruiksaanwijzing met je contactgegevens, het doel, wat het systeem wel en niet kan, de nauwkeurigheid, bekende risico's, hoe het menselijk toezicht werkt, welke invoer het nodig heeft en hoe gebruikers de logs bewaren.
- Bronnen: AIVO-art13-lid1 (AI-verordening art. 13 lid 1); AIVO-art13-lid3 (AI-verordening art. 13 lid 3)

### AI7.6 — Of een mens het systeem kan begrijpen, corrigeren en stoppen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het systeem is zo ontworpen en ontwikkeld, met passende mens-machine-interfaces, dat natuurlijke personen er tijdens het gebruik doeltreffend toezicht op kunnen houden
- Grondslag: art. 14 lid 1 AI-verordening; art. 16 sub a
- Beoordeeld op: de antwoorden
- Nodig: human_oversight_design
- Beoordeling:
  - present als human_oversight_design true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zorg dat gebruikers de uitkomst kunnen begrijpen en uitleggen, dat ze een uitkomst kunnen negeren of terugdraaien, en dat er een stopknop is.
- Bronnen: AIVO-art14-lid1 (AI-verordening art. 14 lid 1)

### AI7.7 — Of het systeem nauwkeurig, robuust en veilig is getest
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het systeem bereikt een passend niveau van nauwkeurigheid, robuustheid en cyberbeveiliging gedurende de levensduur; de nauwkeurigheidsniveaus en relevante maatstaven staan in de gebruiksaanwijzing
- Grondslag: art. 15 lid 1 en 3 AI-verordening; art. 16 sub a
- Beoordeeld op: de antwoorden
- Nodig: accuracy_robustness_security
- Beoordeling:
  - present als accuracy_robustness_security true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Test nauwkeurigheid, bestendigheid tegen fouten en beveiliging tegen aanvallen zoals datavergiftiging en misleidende invoer, en zet de nauwkeurigheidscijfers in de gebruiksaanwijzing.
- Bronnen: AIVO-art15-lid1 (AI-verordening art. 15 lid 1); AIVO-art15-lid3 (AI-verordening art. 15 lid 3)

### AI7.8 — Of je kwaliteitsbeheer hebt ingericht
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De aanbieder heeft een systeem voor kwaliteitsbeheer dat de naleving waarborgt, systematisch en ordelijk gedocumenteerd in schriftelijk beleid, procedures en instructies (art. 17 lid 1 sub a-m), evenredig met de omvang van de organisatie
- Grondslag: art. 17 lid 1 en 2 AI-verordening (zoals gewijzigd bij Vo. (EU) 2026/1744); art. 16 sub c
- Beoordeeld op: de antwoorden
- Nodig: quality_management
- Beoordeling:
  - present als quality_management true is; absent als false.
  - Is sme true: vermeld dat kwaliteitsbeheer in vereenvoudigde vorm mag (na de Omnibus ook voor small mid-caps).
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg je kwaliteitsbeheer vast: strategie voor naleving, procedures voor ontwerp, ontwikkeling, tests en data, risicobeheer, monitoring na levering, incidentmeldingen, communicatie met toezichthouders, documentbeheer en wie waarvoor verantwoordelijk is.
- Bronnen: AIVO-art17-lid1 (AI-verordening art. 17 lid 1); AIVO-art17-lid2 (AI-verordening art. 17 lid 2); AIVO-art16 (AI-verordening art. 16); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI7.9 — Of je de documentatie tien jaar bewaart
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De aanbieder houdt gedurende tien jaar na het in de handel brengen of in gebruik stellen de technische documentatie, de documentatie over kwaliteitsbeheer, eventuele wijzigingen en besluiten van aangemelde instanties en de EU-conformiteitsverklaring ter beschikking van de bevoegde autoriteiten
- Grondslag: art. 18 lid 1 AI-verordening; art. 16 sub d
- Beoordeeld op: de antwoorden
- Nodig: documentation_retention
- Beoordeling:
  - present als documentation_retention true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Spreek af dat je de technische documentatie, het kwaliteitsbeheer, de conformiteitsverklaring en besluiten van de aangemelde instantie tien jaar bewaart, ook als het systeem eerder uit de handel gaat.
- Bronnen: AIVO-art18-lid1 (AI-verordening art. 18 lid 1); AIVO-art16 (AI-verordening art. 16)

### AI7.10 — Of je de logs minstens zes maanden bewaart
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Voor zover de automatisch gegenereerde logs onder zijn controle staan, bewaart de aanbieder ze gedurende een periode die past bij het beoogde doel, ten minste zes maanden, tenzij Unie- of nationaal recht anders bepaalt
- Grondslag: art. 19 lid 1 AI-verordening; art. 16 sub e
- Alleen als: `facts.logs_control != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: logs_control, logs_retention_months
- Beoordeling:
  - present als logs_retention_months 6 of meer is; absent als minder dan 6.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Bewaar de logs die bij jou binnenkomen minstens zes maanden, en niet langer dan nodig.
- Bronnen: AIVO-art19-lid1 (AI-verordening art. 19 lid 1); AIVO-art16 (AI-verordening art. 16)

### AI7.11 — Of de conformiteitsbeoordeling langs de juiste route is gedaan
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Het systeem ondergaat vóór het in de handel brengen of in gebruik stellen de toepasselijke conformiteitsbeoordeling: voor bijlage III punt 2-8 interne controle (bijlage VI); voor biometrie (punt 1) interne controle alleen als geharmoniseerde normen of gemeenschappelijke specificaties volledig zijn toegepast, anders met een aangemelde instantie (bijlage VII); voor bijlage I de procedure van de productwetgeving
- Grondslag: art. 43 lid 1 en 2 AI-verordening; art. 16 sub f
- Beoordeeld op: de antwoorden
- Nodig: conformity_assessment
- Beoordeling:
  - Duidelijk geval non_compliant: conformity_assessment false.
  - Duidelijk geval compliant: conformity_assessment true en (biometric_system false of high_risk_basis annex1, of biometric_system true en (harmonised_standards_applied true of notified_body_used true)).
  - biometric_system true, harmonised_standards_applied false en notified_body_used false: duidelijk non_compliant (bijlage VII is dan verplicht).
  - Bijlage I (high_risk_basis annex1): de procedure van de productwetgeving geldt; geen duidelijk geval tenzij conformity_assessment false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is de juiste conformiteitsbeoordelingsprocedure gevolgd (art. 43)?
- Advies bij ❌ of ⚠️: Doe de conformiteitsbeoordeling vóór levering. Voor de meeste systemen uit bijlage III is dat een interne controle volgens bijlage VI; voor biometrie zonder volledig toegepaste geharmoniseerde normen is een aangemelde instantie nodig.
- Bronnen: AIVO-art43-lid1 (AI-verordening art. 43 lid 1); AIVO-art43-lid2 (AI-verordening art. 43 lid 2); AIVO-art16 (AI-verordening art. 16)

### AI7.12 — Of de conformiteitsverklaring en de CE-markering er zijn
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De aanbieder stelt een schriftelijke, machineleesbare, ondertekende EU-conformiteitsverklaring op en brengt de CE-markering aan (bij digitaal geleverde systemen digitaal), of anders op de verpakking of documentatie
- Grondslag: art. 47 lid 1 en art. 48 lid 1 AI-verordening; art. 16 sub g en h
- Beoordeeld op: de antwoorden
- Nodig: eu_declaration, ce_marking
- Beoordeling:
  - present als eu_declaration en ce_marking beide true zijn; absent als een van beide false is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Stel na de conformiteitsbeoordeling de EU-conformiteitsverklaring op (inhoud volgens bijlage V) en breng de CE-markering aan, bij een digitaal systeem in de interface of de documentatie.
- Bronnen: AIVO-art47-lid1 (AI-verordening art. 47 lid 1); AIVO-art48-lid1 (AI-verordening art. 48 lid 1); AIVO-art16 (AI-verordening art. 16)

### AI7.13 — Of je naam en contactadres op het systeem staan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De aanbieder vermeldt op het systeem, of anders op de verpakking of in de documentatie, zijn naam, geregistreerde handelsnaam of merk en contactadres
- Grondslag: art. 16 sub b AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: name_on_system
- Beoordeling:
  - present als name_on_system true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zet je naam of merk en een contactadres in het systeem zelf, of anders in de verpakking of documentatie.
- Bronnen: AIVO-art16 (AI-verordening art. 16)

### AI7.14 — Of het systeem is geregistreerd in de EU-databank
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Vóór het in de handel brengen of in gebruik stellen van een systeem uit bijlage III registreert de aanbieder (of zijn gemachtigde) zichzelf en het systeem in de EU-databank; voor bijlage III punt 2 op nationaal niveau, voor punt 1, 6 en 7 in een beveiligd, niet-openbaar deel
- Grondslag: art. 49 lid 1 AI-verordening (met lid 4 en 5); art. 16 sub i
- Alleen als: `facts.high_risk_basis != "annex1"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: eu_registration
- Beoordeling:
  - present als eu_registration true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Registreer je organisatie en het systeem in de EU-databank voor hoogrisico-AI voordat je het levert.
- Bronnen: AIVO-art49-lid1 (AI-verordening art. 49 lid 1); AIVO-art16 (AI-verordening art. 16)

### AI7.15 — Of je weet wat je doet als het systeem niet meer voldoet
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Een aanbieder die van mening is of reden heeft om aan te nemen dat zijn systeem niet in overeenstemming is met de verordening, neemt onmiddellijk corrigerende maatregelen (in overeenstemming brengen, uit de handel nemen, buiten gebruik stellen of terugroepen) en informeert de distributeurs en, waar van toepassing, gebruiksverantwoordelijken, gemachtigde en importeurs
- Grondslag: art. 20 lid 1 AI-verordening; art. 16 sub j
- Beoordeeld op: de antwoorden
- Nodig: corrective_actions_procedure
- Beoordeling:
  - present als corrective_actions_procedure true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg vast wie beslist en wat je doet als het systeem niet voldoet: corrigeren, uit de handel nemen of terugroepen, en wie je informeert (distributeurs, gebruikers, importeurs, gemachtigde en bij een risico de toezichthouder).
- Bronnen: AIVO-art20-lid1 (AI-verordening art. 20 lid 1); AIVO-art16 (AI-verordening art. 16)

### AI7.16 — Of je na levering volgt hoe het systeem presteert
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De aanbieder heeft een systeem voor monitoring na het in de handel brengen, evenredig met de aard van de technologie en de risico's, dat actief en systematisch relevante gegevens verzamelt over de prestaties gedurende de levensduur, op basis van een monitoringsplan dat deel uitmaakt van de technische documentatie
- Grondslag: art. 72 lid 1 AI-verordening (richtsnoer Commissie uiterlijk 2 september 2027 volgens de Omnibus)
- Beoordeeld op: de antwoorden
- Nodig: post_market_monitoring
- Beoordeling:
  - present als post_market_monitoring true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Maak een monitoringsplan: welke gegevens je na levering verzamelt over prestaties en fouten (ook via gebruikers), hoe vaak je ze analyseert en wat je met de uitkomsten doet. Neem het op in de technische documentatie.
- Bronnen: AIVO-art72-lid1 (AI-verordening art. 72 lid 1); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI7.17 — Of je ernstige incidenten op tijd meldt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De aanbieder meldt ernstige incidenten aan de markttoezichtautoriteit van de lidstaat waar het incident plaatsvond, onmiddellijk na het vaststellen van het verband en uiterlijk 15 dagen nadat hij ervan op de hoogte is; uiterlijk 2 dagen bij een wijdverbreide inbreuk of een ernstige verstoring van kritieke infrastructuur, en uiterlijk 10 dagen bij overlijden
- Grondslag: art. 73 lid 1-4 AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: incident_reporting
- Beoordeling:
  - present als incident_reporting true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Maak een meldprocedure voor ernstige incidenten met de termijnen: uiterlijk 15 dagen, 10 dagen bij overlijden, 2 dagen bij een wijdverbreide inbreuk of ernstige verstoring van kritieke infrastructuur. Leg vast wie meldt en bij welke toezichthouder.
- Bronnen: AIVO-art73-lid1 (AI-verordening art. 73 lid 1); AIVO-art73-lid2 (AI-verordening art. 73 lid 2); AIVO-art73-lid3 (AI-verordening art. 73 lid 3); AIVO-art73-lid4 (AI-verordening art. 73 lid 4)

### AI7.18 — Of het systeem toegankelijk is voor mensen met een beperking
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: De aanbieder waarborgt dat het systeem voldoet aan de toegankelijkheidseisen van Richtlijn (EU) 2016/2102 en Richtlijn (EU) 2019/882
- Grondslag: art. 16 sub l AI-verordening
- Beoordeeld op: de antwoorden
- Nodig: accessibility
- Beoordeling:
  - present als accessibility true is; absent als false.
  - Welke eisen precies gelden hangt af van het product en de richtlijnen zelf; deze stap is daarom niet verplicht in deze toets en geeft bij ontbreken review.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Welke toegankelijkheidseisen gelden voor dit systeem, en voldoet het daaraan?
- Advies bij ❌ of ⚠️: Laat nagaan welke toegankelijkheidseisen (Europese toegankelijkheidsakte, richtlijn webtoegankelijkheid) voor het systeem gelden, en test de interface daarop.
- Bronnen: AIVO-art16 (AI-verordening art. 16)

### AI7.19 — Of je een gemachtigde in de EU hebt (aanbieder buiten de EU)
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Een aanbieder die buiten de Unie is gevestigd, wijst vóór het op de markt aanbieden schriftelijk een in de Unie gevestigde gemachtigde aan
- Grondslag: art. 22 lid 1 AI-verordening
- Alleen als: `facts.established_in_eu != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: established_in_eu, authorised_representative
- Beoordeling:
  - present als authorised_representative true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Wijs schriftelijk een gemachtigde in de EU aan voordat je het systeem in de EU aanbiedt, met een mandaat dat de taken van art. 22 lid 3 dekt.
- Bronnen: AIVO-art22-lid1 (AI-verordening art. 22 lid 1)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): system_name. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Wanneer dit geldt: de plichten van dit kader (hoofdstuk III, afdeling 1 tot en met 3) gelden vanaf 2 december 2027 voor hoogrisicosystemen uit bijlage III en vanaf 2 augustus 2028 voor systemen uit bijlage I (art. 113 zoals gewijzigd bij Verordening (EU) 2026/1744). Tot die datum is een ❌ een voorbereidingspunt: de rekenhulp maakt er een ⚠️ met de datum van ('Van toepassing vanaf'). Een systeem dat vóór die datum in de handel of in gebruik is, valt er alleen onder als het ontwerp daarna ingrijpend verandert; een systeem dat bedoeld is voor overheidsinstanties moet uiterlijk 2 augustus 2030 voldoen (art. 111 lid 2). Noem dit in het rapport als het systeem al vóór de datum in gebruik is.
- Stap 11 (A) geeft alleen compliant of non_compliant als duidelijk geval; biometrie zonder geharmoniseerde normen en zonder aangemelde instantie is een duidelijk non_compliant geval.
- Stap 18 is niet verplicht; ontbreken geeft review.
- Deze toets toetst of een plicht is ingericht, niet de technische inhoud; dat zegt elk rapport.

## Samenhang met andere kaders

- Kader AI4 (/toets-ai-act-basis) — als `facts.interacts_with_persons != false`: Systemen die met mensen communiceren of inhoud maken, hebben ook transparantieplichten (art. 50).
- Kader K9 (/dpia) — als `facts.trains_with_personal_data != false`: Trainen met persoonsgegevens vraagt een grondslag en vaak een DPIA; voor gevoelige gegevens om vooroordelen op te sporen gelden strenge voorwaarden (art. 4a AI-verordening, art. 9 AVG).

## Open punten en voorbehouden

- Officiële tekst van art. 4a, 10, 11, 17, 49, 72 en bijlage VIII zoals gewijzigd bij Vo. (EU) 2026/1744 nalezen; criteria nu op basis van de oorspronkelijke tekst en secundaire bronnen.
- Grenzen voor small mid-caps (Omnibus) en de vereenvoudigde vormen van technische documentatie en kwaliteitsbeheer laten bevestigen; de vraag 'minder dan 750 medewerkers' is een benadering.
- Art. 21 (samenwerking met autoriteiten), art. 16 sub k (aantonen op verzoek) en art. 111 lid 2 (bestaande systemen) niet als stap opgenomen.
- Importeurs (art. 23) en distributeurs (art. 24): eigen kader AI8.
