# Kader K18 — Gezamenlijke verwerkingsverantwoordelijkheid

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of er bij gezamenlijke verwerkingsverantwoordelijkheid een regeling is die aan art. 26 AVG voldoet: wie welke verplichting nakomt, passend bij de feitelijke rollen, beschikbaar voor betrokkenen, en zonder beperking van hun rechten tegenover elk van de partijen.

Bronnen: AVG-art26 (AVG art. 26); AVG-art26-lid1 (AVG art. 26 lid 1); AVG-art26-lid2 (AVG art. 26 lid 2); AVG-art26-lid3 (AVG art. 26 lid 3); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG); HvJEU-C-210-16 (HvJEU, C-210/16, Wirtschaftsakademie Schleswig-Holstein (Facebook-fanpagina)); HvJEU-C-25-17 (HvJEU, C-25/17, Jehovan todistajat); HvJEU-C-40-17 (HvJEU, C-40/17, Fashion ID); HvJEU-C-683-21 (HvJEU, C-683/21, Nacionalinis visuomenės sveikatos centras)

## Formulier (vragen aan de gebruiker)

- **partner_names**: Met welke organisatie of organisaties beslis je samen over het gebruik van de gegevens?
  - Label (voor de plek-om-in-te-vullen): met wie je samen verantwoordelijk bent
  - Type: text
- **joint_operations_description**: Beschrijf welke onderdelen van de verwerking je samen met de andere partij bepaalt (waarvoor en hoe), en welke onderdelen elke partij zelf regelt.
  - Label (voor de plek-om-in-te-vullen): waarover je samen beslist
  - Hulp: Bijvoorbeeld: 'Samen: de inschrijving voor het gezamenlijke evenement en de deelnemerslijst. Zelf: ieder gebruikt de lijst niet voor eigen nieuwsbrieven.' Of: 'Wij plaatsen een like-knop; de gegevens die daarmee naar het socialemediabedrijf gaan, zijn het gezamenlijke deel.'
  - Type: text
- **operations_delineated**: Heb je met de andere partij vastgesteld voor welke onderdelen van de verwerking je samen verantwoordelijk bent?
  - Label (voor de plek-om-in-te-vullen): of je hebt afgesproken welke onderdelen gezamenlijk zijn
  - Type: boolean
- **responsibilities_set_by_law**: Staat in een wet (Europees of Nederlands) al precies vastgelegd wie van jullie welke privacyverplichting nakomt?
  - Label (voor de plek-om-in-te-vullen): of de verdeling van de verantwoordelijkheden al in de wet staat
  - Hulp: Dat komt vooral voor bij samenwerking die een wet voorschrijft, bijvoorbeeld tussen overheidsorganisaties. Is maar een deel wettelijk geregeld, kies dan 'nee'. Voor de meeste bedrijven is het antwoord nee.
  - Type: boolean
- **law_description**: Welke wet regelt de verdeling van de verantwoordelijkheden?
  - Label (voor de plek-om-in-te-vullen): welke wet de verdeling regelt
  - Type: text · Alleen vragen als: `facts.responsibilities_set_by_law == true`
- **has_arrangement**: Heb je met de andere partij afspraken vastgelegd over wie welke privacyverplichting nakomt?
  - Label (voor de plek-om-in-te-vullen): of je een regeling met de andere partij hebt
  - Hulp: Bijvoorbeeld een samenwerkingsovereenkomst met een privacyparagraaf, of de voorwaarden die een socialemediabedrijf hiervoor aanbiedt.
  - Type: boolean
- **arrangement_allocates_obligations**: Staat in de afspraken duidelijk wie verzoeken van mensen afhandelt (zoals inzage of verwijdering) en wie mensen informeert over het gebruik van hun gegevens?
  - Label (voor de plek-om-in-te-vullen): of de regeling vastlegt wie wat doet
  - Type: boolean · Alleen vragen als: `facts.has_arrangement == true`
- **arrangement_matches_practice**: Klopt wat in de afspraken staat met hoe jij en de andere partij in de praktijk samenwerken?
  - Label (voor de plek-om-in-te-vullen): of de regeling past bij hoe je echt samenwerkt
  - Hulp: Bijvoorbeeld: de afspraken zeggen dat de andere partij alle vragen afhandelt, maar in de praktijk komen ze allemaal bij jou terecht.
  - Type: boolean · Alleen vragen als: `facts.has_arrangement == true`
- **arrangement_essence_available**: Kunnen mensen van wie je gegevens verwerkt de kern van de afspraken lezen, bijvoorbeeld in je privacyverklaring?
  - Label (voor de plek-om-in-te-vullen): of mensen de kern van de regeling kunnen lezen
  - Type: boolean · Alleen vragen als: `facts.has_arrangement == true`
- **contact_point**: Is er één vast contactpunt aangewezen waar mensen met privacyvragen terechtkunnen?
  - Label (voor de plek-om-in-te-vullen): of er een contactpunt voor mensen is
  - Hulp: Dit is niet verplicht.
  - Type: boolean
- **rights_at_each_party**: Weten jij en de andere partij dat mensen hun privacyrechten bij elk van jullie kunnen uitoefenen, en behandel je zo'n verzoek ook als het over het deel van de ander gaat?
  - Label (voor de plek-om-in-te-vullen): of mensen bij elke partij terechtkunnen
  - Type: boolean
- **arrangement_limits_to_one_party**: Staat in de afspraken dat mensen zich alleen tot één van de partijen mogen wenden?
  - Label (voor de plek-om-in-te-vullen): of de regeling mensen naar één partij verwijst
  - Type: boolean · Alleen vragen als: `facts.has_arrangement == true`

## Toetspunten (voor de eindcontrole)

### K18.1 — Voor welke onderdelen je samen verantwoordelijk bent
- Grondslag: art. 26 lid 1 en art. 4 punt 7 AVG
- Toetspunt: Voor welke verwerkingshandelingen bestaat gezamenlijke verantwoordelijkheid? Alleen voor handelingen waarvan doel en middelen samen worden bepaald; voor de rest is ieder zelfstandig verantwoordelijk
- Bronnen: AVG-art26-lid1 (AVG art. 26 lid 1); AVG-art4-7 (AVG art. 4 punt 7); HvJEU-C-40-17 (HvJEU, C-40/17, Fashion ID); HvJEU-C-210-16 (HvJEU, C-210/16, Wirtschaftsakademie Schleswig-Holstein (Facebook-fanpagina)); HvJEU-C-25-17 (HvJEU, C-25/17, Jehovan todistajat); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Stel samen met de andere partij vast voor welke onderdelen van de verwerking je samen beslist over doel en middelen. Voor de andere onderdelen is ieder zelf verantwoordelijk.

### K18.2 — Er is een regeling met de andere partij
- Grondslag: art. 26 lid 1 AVG
- Toetspunt: De gezamenlijk verantwoordelijken stellen in een onderlinge regeling op transparante wijze hun verantwoordelijkheden vast, tenzij deze bij Unierecht of lidstaatrecht zijn vastgesteld
- Alleen als: `facts.responsibilities_set_by_law != true`
- Bronnen: AVG-art26-lid1 (AVG art. 26 lid 1); HvJEU-C-683-21 (HvJEU, C-683/21, Nacionalinis visuomenės sveikatos centras); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg met de andere partij schriftelijk vast wie van jullie welke privacyverplichting nakomt. Zonder die afspraken blijven jullie samen verantwoordelijk.

### K18.3 — De regeling legt vast wie wat doet
- Grondslag: art. 26 lid 1 AVG
- Toetspunt: De regeling stelt op transparante wijze vast wie welke verplichtingen nakomt, met name wat betreft de rechten van betrokkenen en de informatieplicht (art. 13 en 14)
- Alleen als: `facts.has_arrangement != false`
- Bronnen: AVG-art26-lid1 (AVG art. 26 lid 1); AVG-art13 (AVG art. 13); AVG-art14 (AVG art. 14); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg in de regeling vast wie verzoeken van betrokkenen afhandelt en wie hen informeert over het gebruik van hun gegevens.

### K18.4 — De regeling past bij hoe je echt samenwerkt
- Grondslag: art. 26 lid 2 AVG
- Toetspunt: De regeling weerspiegelt de respectieve rollen en verhoudingen van de gezamenlijk verantwoordelijken ten opzichte van de betrokkenen
- Alleen als: `facts.has_arrangement != false`
- Bronnen: AVG-art26-lid2 (AVG art. 26 lid 2); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Pas de regeling aan zodat die beschrijft hoe jij en de andere partij in de praktijk samenwerken, of pas de praktijk aan de afspraken aan.

### K18.5 — Mensen kunnen de kern van de regeling lezen
- Grondslag: art. 26 lid 2 AVG
- Toetspunt: De wezenlijke inhoud van de regeling wordt aan de betrokkene beschikbaar gesteld
- Alleen als: `facts.has_arrangement != false`
- Bronnen: AVG-art26-lid2 (AVG art. 26 lid 2)
- Wat de tekst moet bereiken: Neem de kern van de afspraken op in je privacyverklaring: met wie je samenwerkt, wie welke verplichting nakomt en waar mensen terechtkunnen.

### K18.6 — Mensen kunnen bij elke partij terecht
- Grondslag: art. 26 lid 1 laatste zin en lid 3 AVG
- Toetspunt: Betrokkenen kunnen hun rechten uitoefenen met betrekking tot en tegen elk van de verwerkingsverantwoordelijken, ongeacht de regeling; (optioneel) een contactpunt
- Bronnen: AVG-art26-lid3 (AVG art. 26 lid 3); AVG-art26-lid1 (AVG art. 26 lid 1)
- Wat de tekst moet bereiken: Zorg dat jij en de andere partij elk verzoek van een betrokkene behandelen, ook als het over het deel van de ander gaat, en haal uit de afspraken elke bepaling die mensen naar één partij verwijst. Een vast contactpunt kan helpen.
