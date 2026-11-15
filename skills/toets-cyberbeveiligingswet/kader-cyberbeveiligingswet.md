# Kader CB1 — Cyberbeveiligingswet

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of een organisatie die onder de Cyberbeveiligingswet valt, is geregistreerd, de zorgplicht (passende en evenredige maatregelen, ten minste de onderwerpen van art. 21 lid 2 NIS2) invult, het bestuur zijn verantwoordelijkheid neemt en significante incidenten op tijd kan melden.

Bronnen: Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn)); NCSC-Cbw (Rijksoverheid, nieuwsbericht 15 augustus 2026 "Cyberbeveiligingswet en Wet weerbaarheid kritieke entiteiten vanaf vandaag van kracht"); NIS2-art2-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 2 lid 1); NIS2-art2-lid2 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 2 lid 2); NIS2-art20-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 20 lid 1); NIS2-art20-lid2 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 20 lid 2); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); NIS2-art21-lid2-a (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub a); NIS2-art21-lid2-b (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub b); NIS2-art21-lid2-c (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub c); NIS2-art21-lid2-d (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub d); NIS2-art21-lid2-e (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub e); NIS2-art21-lid2-f (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub f); NIS2-art21-lid2-g (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub g); NIS2-art21-lid2-h (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub h); NIS2-art21-lid2-i (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub i); NIS2-art21-lid2-j (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub j); NIS2-art23-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 23 lid 1); NIS2-art23-lid4 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 23 lid 4); NIS2-art3-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 3 lid 1); NIS2-art3-lid4 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 3 lid 4); NIS2-bijlage1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) bijlage 1); NIS2-bijlage2 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) bijlage 2)

## Formulier (vragen aan de gebruiker)

- **sector**: Ben je actief in een van deze sectoren?
  - Label (voor de plek-om-in-te-vullen): in welke sector je actief bent
  - Type: enum (annex1 / annex2 / none)
- **size**: Hoe groot is je organisatie?
  - Label (voor de plek-om-in-te-vullen): hoe groot je organisatie is
  - Type: enum (small / medium / large)
- **size_independent**: Lever je een dienst die ongeacht de omvang onder de wet valt, zoals DNS-diensten, een topleveldomeinregister, vertrouwensdiensten of openbare elektronische communicatie?
  - Label (voor de plek-om-in-te-vullen): of je een dienst levert die ongeacht omvang onder de wet valt
  - Type: boolean
- **in_scope**: Valt je organisatie volgens je eigen beoordeling (of die van je adviseur) onder de Cyberbeveiligingswet?
  - Label (voor de plek-om-in-te-vullen): of je volgens je eigen beoordeling onder de wet valt
  - Type: boolean
- **registered**: Heb je je organisatie geregistreerd bij het NCSC?
  - Label (voor de plek-om-in-te-vullen): of je bent geregistreerd
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **risk_policy**: Heb je een risicoanalyse en een beleid voor de beveiliging van je netwerk- en informatiesystemen?
  - Label (voor de plek-om-in-te-vullen): risicoanalyse en beveiligingsbeleid
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **incident_handling**: Heb je een procedure om incidenten te herkennen, af te handelen en op te volgen?
  - Label (voor de plek-om-in-te-vullen): incidentbehandeling
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **continuity**: Heb je regelingen voor bedrijfscontinuïteit, back-ups, herstel na een ramp en crisisbeheer?
  - Label (voor de plek-om-in-te-vullen): bedrijfscontinuïteit en back-ups
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **supply_chain**: Stel je beveiligingseisen aan je leveranciers en dienstverleners, en beoordeel je hun risico's?
  - Label (voor de plek-om-in-te-vullen): beveiliging van de toeleveringsketen
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **secure_development**: Let je bij aanschaf, ontwikkeling en onderhoud van systemen op beveiliging, inclusief het afhandelen en melden van kwetsbaarheden?
  - Label (voor de plek-om-in-te-vullen): beveiliging bij aanschaf, ontwikkeling en onderhoud
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **effectiveness**: Beoordeel je regelmatig of je maatregelen werken (bijvoorbeeld met audits of tests)?
  - Label (voor de plek-om-in-te-vullen): beoordeling van de effectiviteit
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **hygiene_training**: Pas je basismaatregelen voor cyberhygiëne toe (updates, wachtwoorden) en trainen je medewerkers in cyberbeveiliging?
  - Label (voor de plek-om-in-te-vullen): cyberhygiëne en training
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **cryptography**: Heb je beleid voor het gebruik van cryptografie en, waar passend, versleuteling?
  - Label (voor de plek-om-in-te-vullen): cryptografie en versleuteling
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **access_assets**: Heb je beleid voor de beveiliging van personeel, toegangsbeheer en een overzicht van je bedrijfsmiddelen (assets)?
  - Label (voor de plek-om-in-te-vullen): personeel, toegang en beheer van bedrijfsmiddelen
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **mfa**: Gebruik je waar passend meervoudige authenticatie en beveiligde communicatie (ook voor noodcommunicatie)?
  - Label (voor de plek-om-in-te-vullen): meervoudige authenticatie en beveiligde communicatie
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **board_approval**: Keurt het bestuur de beveiligingsmaatregelen goed, houdt het toezicht op de uitvoering en volgen de bestuurders een training?
  - Label (voor de plek-om-in-te-vullen): of het bestuur de maatregelen goedkeurt en volgt
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`
- **reporting_procedure**: Heb je een procedure om significante incidenten te melden: een vroegtijdige waarschuwing binnen 24 uur, een melding binnen 72 uur en een eindverslag binnen een maand?
  - Label (voor de plek-om-in-te-vullen): of je significante incidenten op tijd kunt melden
  - Type: boolean · Alleen vragen als: `facts.in_scope != false`

## Toetspunten

### CB1.1 — Of je onder de Cyberbeveiligingswet valt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De organisatie valt onder de wet als zij in een sector van bijlage I of II van NIS2 actief is en ten minste middelgroot is, of ongeacht omvang een dienst levert die de wet aanwijst; de organisatie bepaalt dat zelf
- Grondslag: art. 2 en 3 NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Beoordeeld op: de antwoorden
- Nodig: sector, size
- Beoordeling:
  - Altijd review. Vermeld de waarschijnlijke uitkomst: sector annex1 of annex2 en size medium of large, of size_independent true → waarschijnlijk wel; sector none en size_independent false → waarschijnlijk niet. Grote ondernemingen in bijlage I zijn doorgaans essentiële entiteiten, de overige belangrijke entiteiten.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Valt de organisatie onder de Cyberbeveiligingswet, en als essentiële of als belangrijke entiteit?
- Advies bij ❌ of ⚠️: Ga na of je onder de Cyberbeveiligingswet valt met de zelftest van de overheid of je adviseur.
- Bronnen: NIS2-art2-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 2 lid 1); NIS2-art2-lid2 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 2 lid 2); NIS2-art3-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 3 lid 1); NIS2-bijlage1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) bijlage 1); NIS2-bijlage2 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) bijlage 2); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn)); NCSC-Cbw (Rijksoverheid, nieuwsbericht 15 augustus 2026 "Cyberbeveiligingswet en Wet weerbaarheid kritieke entiteiten vanaf vandaag van kracht")

### CB1.2 — Of je geregistreerd bent
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De organisatie heeft zich geregistreerd in het register van het NCSC
- Grondslag: Cyberbeveiligingswet (registratieplicht); art. 3 lid 4 en art. 27 NIS2
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: registered
- Beoordeling:
  - present als registered true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Registreer je organisatie bij het NCSC.
- Bronnen: Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn)); NIS2-art3-lid4 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 3 lid 4); NCSC-Cbw (Rijksoverheid, nieuwsbericht 15 augustus 2026 "Cyberbeveiligingswet en Wet weerbaarheid kritieke entiteiten vanaf vandaag van kracht")

### CB1.3 — Of je een risicoanalyse en beveiligingsbeleid hebt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Beleid inzake risicoanalyse en beveiliging van informatiesystemen
- Grondslag: art. 21 lid 2 sub a NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: risk_policy
- Beoordeling:
  - present als risk_policy true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: beleid inzake risicoanalyse en beveiliging van informatiesystemen.
- Bronnen: NIS2-art21-lid2-a (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub a); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.4 — Of incidentbehandeling is geregeld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Incidentenbehandeling
- Grondslag: art. 21 lid 2 sub b NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: incident_handling
- Beoordeling:
  - present als incident_handling true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: incidentenbehandeling.
- Bronnen: NIS2-art21-lid2-b (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub b); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.5 — Of bedrijfscontinuïteit is geregeld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Bedrijfscontinuïteit, zoals back-upbeheer, noodherstel en crisisbeheer
- Grondslag: art. 21 lid 2 sub c NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: continuity
- Beoordeling:
  - present als continuity true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: bedrijfscontinuïteit, zoals back-upbeheer, noodherstel en crisisbeheer.
- Bronnen: NIS2-art21-lid2-c (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub c); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.6 — Of de toeleveringsketen is beveiligd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Beveiliging van de toeleveringsketen, met inbegrip van de relaties met rechtstreekse leveranciers en dienstverleners
- Grondslag: art. 21 lid 2 sub d NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: supply_chain
- Beoordeling:
  - present als supply_chain true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: beveiliging van de toeleveringsketen, met inbegrip van de relaties met rechtstreekse leveranciers en dienstverleners.
- Bronnen: NIS2-art21-lid2-d (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub d); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.7 — Of beveiliging bij aanschaf en ontwikkeling is geregeld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Beveiliging bij het verwerven, ontwikkelen en onderhouden van systemen, met inbegrip van de behandeling en bekendmaking van kwetsbaarheden
- Grondslag: art. 21 lid 2 sub e NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: secure_development
- Beoordeling:
  - present als secure_development true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: beveiliging bij het verwerven, ontwikkelen en onderhouden van systemen, met inbegrip van de behandeling en bekendmaking van kwetsbaarheden.
- Bronnen: NIS2-art21-lid2-e (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub e); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.8 — Of je de effectiviteit beoordeelt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Beleid en procedures om de effectiviteit van de beheersmaatregelen te beoordelen
- Grondslag: art. 21 lid 2 sub f NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: effectiveness
- Beoordeling:
  - present als effectiveness true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: beleid en procedures om de effectiviteit van de beheersmaatregelen te beoordelen.
- Bronnen: NIS2-art21-lid2-f (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub f); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.9 — Of cyberhygiëne en training zijn geregeld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Basispraktijken op het gebied van cyberhygiëne en opleiding op het gebied van cyberbeveiliging
- Grondslag: art. 21 lid 2 sub g NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: hygiene_training
- Beoordeling:
  - present als hygiene_training true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: basispraktijken op het gebied van cyberhygiëne en opleiding op het gebied van cyberbeveiliging.
- Bronnen: NIS2-art21-lid2-g (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub g); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.10 — Of cryptografie is geregeld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Beleid en procedures inzake het gebruik van cryptografie en, waar passend, versleuteling
- Grondslag: art. 21 lid 2 sub h NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: cryptography
- Beoordeling:
  - present als cryptography true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: beleid en procedures inzake het gebruik van cryptografie en, waar passend, versleuteling.
- Bronnen: NIS2-art21-lid2-h (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub h); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.11 — Of personeel, toegang en assets zijn geregeld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Beveiligingsaspecten ten aanzien van personeel, toegangsbeleid en beheer van activa
- Grondslag: art. 21 lid 2 sub i NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: access_assets
- Beoordeling:
  - present als access_assets true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: beveiligingsaspecten ten aanzien van personeel, toegangsbeleid en beheer van activa.
- Bronnen: NIS2-art21-lid2-i (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub i); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.12 — Of meervoudige authenticatie en beveiligde communicatie zijn geregeld
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Waar passend het gebruik van multifactorauthenticatie of continue authenticatie, beveiligde spraak-, video- en tekstcommunicatie en beveiligde noodcommunicatie
- Grondslag: art. 21 lid 2 sub j NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: mfa
- Beoordeling:
  - present als mfa true is; absent als false.
  - Of de maatregel passend en evenredig is, beoordeelt deze skill niet; deze stap toetst of het onderwerp is geregeld.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Regel: waar passend het gebruik van multifactorauthenticatie of continue authenticatie, beveiligde spraak-, video- en tekstcommunicatie en beveiligde noodcommunicatie.
- Bronnen: NIS2-art21-lid2-j (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub j); NIS2-art21-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 1); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

### CB1.13 — Of het bestuur zijn verantwoordelijkheid neemt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het bestuur keurt de maatregelen goed, houdt toezicht op de uitvoering en volgt een opleiding om risico's te kunnen beoordelen
- Grondslag: art. 20 lid 1 en 2 NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: board_approval
- Beoordeling:
  - present als board_approval true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Laat het bestuur de maatregelen goedkeuren, het toezicht op de uitvoering vastleggen en een training volgen.
- Bronnen: NIS2-art20-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 20 lid 1); NIS2-art20-lid2 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 20 lid 2); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn)); NCSC-Cbw (Rijksoverheid, nieuwsbericht 15 augustus 2026 "Cyberbeveiligingswet en Wet weerbaarheid kritieke entiteiten vanaf vandaag van kracht")

### CB1.14 — Of je significante incidenten op tijd kunt melden
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Significante incidenten worden gemeld: vroegtijdige waarschuwing binnen 24 uur, incidentmelding binnen 72 uur, eindverslag binnen een maand na de melding
- Grondslag: art. 23 lid 4 NIS2-richtlijn, omgezet in de Cyberbeveiligingswet
- Alleen als: `facts.in_scope != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reporting_procedure
- Beoordeling:
  - present als reporting_procedure true is; absent als false.
  - Controleer de termijnen zoals de Cbw ze overneemt (open punt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Maak een meldprocedure met de termijnen 24 uur, 72 uur en een maand, en leg vast wie meldt via het portaal van het NCSC.
- Bronnen: NIS2-art23-lid1 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 23 lid 1); NIS2-art23-lid4 (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 23 lid 4); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn)); NCSC-Cbw (Rijksoverheid, nieuwsbericht 15 augustus 2026 "Cyberbeveiligingswet en Wet weerbaarheid kritieke entiteiten vanaf vandaag van kracht")

## Regels van dit kader

- Stap 1 is altijd review: deze skill stelt niet definitief vast of de organisatie onder de wet valt.
- Valt de organisatie er volgens haar eigen beoordeling niet onder (in_scope false): stap 2-14 n.v.t.
- Een verplichte F-stap absent → non_compliant.

## Open punten en voorbehouden

- Cbw-artikelnummers vastleggen (Staatsblad 2026, 187) en de stappen daarnaar laten verwijzen; ook de uitvoeringsregels (Cyberbeveiligingsbesluit) en de meldtermijnen zoals de Cbw die overneemt.
- Sectorale toezichthouders en uitzonderingen ongeacht omvang (art. 2 lid 2 NIS2) per sector nalezen.
