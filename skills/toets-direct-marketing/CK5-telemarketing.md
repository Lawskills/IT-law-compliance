# Kader CK5 — Telemarketing

Versie 0.3 · peildatum 2026-11-10

Doel: Controleren of een organisatie die natuurlijke personen belt voor marketing dat alleen doet met voorafgaande toestemming of binnen de uitzondering voor eigen klanten, bij elk gesprek op het recht van verzet wijst en dat verwerkt, een herkenbaar nummer gebruikt en de toestemming kan aantonen.

Bronnen: ACM-telemarketing (Uitleg van de Autoriteit Consument & Markt over telemarketing (opt-in sinds 1 juli 2021)); AVG-art21-lid3 (AVG art. 21 lid 3); AVG-art28-lid3 (AVG art. 28 lid 3); AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid1 (AVG art. 7 lid 1); TW-art11.7-lid2 (Telecommunicatiewet art. 11.7 lid 2); TW-art11.7-lid4 (Telecommunicatiewet art. 11.7 lid 4); TW-art11.7-lid5 (Telecommunicatiewet art. 11.7 lid 5); TW-art11.7-lid8 (Telecommunicatiewet art. 11.7 lid 8)

## Formulier (vragen aan de gebruiker)

- **calls_for_marketing**: Bel je (of een callcenter in je opdracht) mensen om producten, diensten of goede doelen aan te bieden?
  - Label (voor de plek-om-in-te-vullen): of je belt voor marketing
  - Type: boolean
- **calls_natural_persons**: Bel je consumenten of eenmanszaken (natuurlijke personen), en niet alleen bedrijven met rechtspersoonlijkheid?
  - Label (voor de plek-om-in-te-vullen): of je natuurlijke personen belt
  - Type: boolean · Alleen vragen als: `facts.calls_for_marketing != false`
- **basis**: Op welke grond bel je deze mensen?
  - Label (voor de plek-om-in-te-vullen): op welke grond je belt
  - Type: enum (consent / customer / none) · Alleen vragen als: `facts.calls_for_marketing != false and facts.calls_natural_persons != false`
- **consent_recorded**: Kun je per persoon aantonen wanneer en hoe hij toestemming gaf?
  - Label (voor de plek-om-in-te-vullen): of je de toestemming kunt aantonen
  - Type: boolean · Alleen vragen als: `facts.calls_for_marketing != false and facts.calls_natural_persons != false and facts.basis != "customer" and facts.basis != "none"`
- **customer_conditions**: Kreeg je het nummer bij een verkoop, bel je alleen voor eigen vergelijkbare producten of diensten, kon de klant bij het verkrijgen al bezwaar maken, en bel je binnen de termijn die de ACM noemt?
  - Label (voor de plek-om-in-te-vullen): of je binnen de klantuitzondering blijft
  - Type: boolean · Alleen vragen als: `facts.calls_for_marketing != false and facts.calls_natural_persons != false and facts.basis != "consent" and facts.basis != "none"`
- **objection_each_call**: Vertel je bij elk gesprek dat iemand kan aangeven niet meer gebeld te willen worden, en verwerk je dat direct?
  - Label (voor de plek-om-in-te-vullen): of je bij elk gesprek op het recht van verzet wijst
  - Type: boolean · Alleen vragen als: `facts.calls_for_marketing != false`
- **number_shown**: Bel je met zichtbaar nummer, waarop mensen ook kunnen terugbellen?
  - Label (voor de plek-om-in-te-vullen): of je met een herkenbaar nummer belt
  - Type: boolean · Alleen vragen als: `facts.calls_for_marketing != false`
- **callcenter_instructed**: Als een callcenter voor je belt: heb je vastgelegd dat het alleen belt wie toestemming gaf of klant is, en dat bezwaren direct bij jou terechtkomen?
  - Label (voor de plek-om-in-te-vullen): of afspraken met een callcenter zijn vastgelegd
  - Type: boolean · Alleen vragen als: `facts.calls_for_marketing != false`

## Toetspunten

### CK5.1 — Of je natuurlijke personen mag bellen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Telefonische marketing aan natuurlijke personen gebeurt alleen met hun voorafgaande toestemming of binnen de uitzondering voor eigen klanten; koude acquisitie en gekochte bestanden zonder toestemming zijn niet toegestaan
- Grondslag: art. 11.7 lid 2 en lid 4 Telecommunicatiewet
- Alleen als: `facts.calls_for_marketing != false and facts.calls_natural_persons != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: basis
- Beoordeling:
  - Duidelijk geval non_compliant: basis none.
  - Duidelijk geval compliant: basis consent of customer (de voorwaarden toetsen stap 2 en 3).
  - Ontbrekend of "weet ik niet": ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Rust het bellen op toestemming of de klantuitzondering?
- Advies bij ❌ of ⚠️: Bel consumenten en eenmanszaken alleen met hun voorafgaande toestemming, of als eigen klant voor vergelijkbare producten of diensten.
- Bronnen: TW-art11.7-lid2 (Telecommunicatiewet art. 11.7 lid 2); TW-art11.7-lid4 (Telecommunicatiewet art. 11.7 lid 4); ACM-telemarketing (Uitleg van de Autoriteit Consument & Markt over telemarketing (opt-in sinds 1 juli 2021))

### CK5.2 — Of je de toestemming kunt aantonen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De toestemming voldoet aan de AVG (vrij, specifiek, geïnformeerd, ondubbelzinnig) en de organisatie kan aantonen dat zij is gegeven
- Grondslag: art. 11.7 lid 2 Telecommunicatiewet; art. 4 punt 11 en art. 7 lid 1 AVG
- Alleen als: `facts.calls_for_marketing != false and facts.calls_natural_persons != false and facts.basis != "customer" and facts.basis != "none"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: consent_recorded
- Beoordeling:
  - present als consent_recorded true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg per persoon vast wanneer en hoe hij toestemming gaf om gebeld te worden.
- Bronnen: TW-art11.7-lid2 (Telecommunicatiewet art. 11.7 lid 2); AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid1 (AVG art. 7 lid 1)

### CK5.3 — Of je binnen de uitzondering voor klanten blijft
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Bij eigen klanten: het nummer is verkregen bij een verkoop, er wordt gebeld voor eigen gelijksoortige producten of diensten, de klant kon bij het verkrijgen kosteloos bezwaar maken, en er wordt gebeld binnen de termijn die de ACM in haar uitleg noemt
- Grondslag: art. 11.7 lid 4 Telecommunicatiewet; uitleg ACM
- Alleen als: `facts.calls_for_marketing != false and facts.calls_natural_persons != false and facts.basis != "consent" and facts.basis != "none"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: customer_conditions
- Beoordeling:
  - present als customer_conditions true is; absent als false.
  - De termijn is uitleg van de ACM; noem dat in de onderbouwing.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Bel klanten alleen voor eigen vergelijkbare producten of diensten, alleen als ze bij de verkoop bezwaar konden maken, en binnen de termijn die de ACM noemt.
- Bronnen: TW-art11.7-lid4 (Telecommunicatiewet art. 11.7 lid 4); ACM-telemarketing (Uitleg van de Autoriteit Consument & Markt over telemarketing (opt-in sinds 1 juli 2021))

### CK5.4 — Of je bij elk gesprek op het recht van verzet wijst
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Bij elk gesprek wordt de gebelde gewezen op de mogelijkheid kosteloos bezwaar te maken, en een bezwaar wordt direct verwerkt
- Grondslag: art. 11.7 lid 5 Telecommunicatiewet; art. 21 lid 3 AVG
- Alleen als: `facts.calls_for_marketing != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: objection_each_call
- Beoordeling:
  - present als objection_each_call true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zeg bij elk gesprek dat iemand kan aangeven niet meer gebeld te willen worden, en verwerk dat direct.
- Bronnen: TW-art11.7-lid5 (Telecommunicatiewet art. 11.7 lid 5); AVG-art21-lid3 (AVG art. 21 lid 3)

### CK5.5 — Of je met een herkenbaar nummer belt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Bij telefonische marketing wordt de nummerweergave niet geblokkeerd
- Grondslag: art. 11.7 lid 8 Telecommunicatiewet
- Alleen als: `facts.calls_for_marketing != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: number_shown
- Beoordeling:
  - present als number_shown true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Bel met een zichtbaar nummer waarop mensen kunnen terugbellen.
- Bronnen: TW-art11.7-lid8 (Telecommunicatiewet art. 11.7 lid 8)

### CK5.6 — Of afspraken met een callcenter zijn vastgelegd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Belt een callcenter in opdracht, dan zijn de regels en het doorgeven van bezwaren vastgelegd; de opdrachtgever blijft verantwoordelijk
- Grondslag: goede praktijk; art. 11.7 Telecommunicatiewet; art. 28 AVG als achtergrond
- Alleen als: `facts.calls_for_marketing != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: callcenter_instructed
- Beoordeling:
  - present als callcenter_instructed true is; absent als false.
  - Geen callcenter: deze stap mag review geven; niet verplicht.
  - Goede praktijk, geen wettelijke eis: ontbreken geeft review, nooit non_compliant.
- Is het vereiste afwezig (*absent*): ⚠️
- Advies bij ❌ of ⚠️: Leg met het callcenter vast wie het mag bellen en dat bezwaren direct bij jou terechtkomen, en sluit een verwerkersovereenkomst.
- Bronnen: TW-art11.7-lid2 (Telecommunicatiewet art. 11.7 lid 2); AVG-art28-lid3 (AVG art. 28 lid 3)

## Regels van dit kader

- Belt de organisatie niet voor marketing → alle stappen n.v.t.
- Een verplichte F-stap absent → non_compliant.
- Bellen van rechtspersonen valt buiten de opt-in; dan gelden alleen recht van verzet en nummerweergave (te controleren).

## Samenhang met andere kaders

- Kader CK4 (/toets-direct-marketing) — als `facts.calls_for_marketing != false`: Voor e-mail en sms gelden vergelijkbare regels (art. 11.7 Tw).

## Open punten en voorbehouden

- Art. 11.7 lid 2-8 Tw (versie sinds 1 juli 2021) letterlijk nalezen, vooral de uitzondering voor klanten en wie onder "natuurlijke persoon" valt (eenmanszaak).
- De ACM-uitleg over de termijn voor het bellen van klanten nalezen en de vindplaats vastleggen.
