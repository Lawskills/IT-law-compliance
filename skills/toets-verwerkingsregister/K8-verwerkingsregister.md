# Kader K8 — Verwerkingsregister

Versie 1.2 · peildatum 2026-11-10

Doel: Toetsen of de organisatie een register van verwerkingsactiviteiten moet bijhouden (art. 30 lid 5 AVG), of dat register bestaat, en of het de verplichte inhoud van art. 30 lid 1 (verantwoordelijke) en art. 30 lid 2 (verwerker) bevat, actueel is en aan de AP kan worden verstrekt.

Bronnen: AVG-art30 (AVG art. 30); AVG-art30-lid1 (AVG art. 30 lid 1); AVG-art30-lid2 (AVG art. 30 lid 2); AVG-art30-lid3 (AVG art. 30 lid 3); AVG-art30-lid4 (AVG art. 30 lid 4); AVG-art30-lid5 (AVG art. 30 lid 5); WP29-PP-art30-5 (Artikel 29-werkgroep, position paper over de uitzonderingen op de plicht tot het bijhouden van een register van verwerkingsactiviteiten (art. 30 lid 5 AVG), bekrachtigd door de EDPB)

## Formulier (vragen aan de gebruiker)

- **role**: Gebruik je persoonsgegevens voor je eigen doelen, in opdracht van klanten, of allebei?
  - Label (voor de plek-om-in-te-vullen): je rol bij het gebruik van persoonsgegevens
  - Type: enum (controller / processor / both) · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **employee_count**: Hoeveel werknemers heeft je organisatie?
  - Label (voor de plek-om-in-te-vullen): het aantal werknemers
  - Type: number · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **has_staff_or_customer_records**: Houd je een personeelsadministratie, een klantenbestand of een ledenadministratie bij?
  - Label (voor de plek-om-in-te-vullen): of je een personeels- of klantenadministratie hebt
  - Hulp: Ook een eenvoudige lijst in een spreadsheet of boekhoudprogramma telt mee.
  - Type: boolean
- **processing_only_occasional**: Gebruik je persoonsgegevens alleen af en toe, bij uitzondering, en niet als vast onderdeel van je werk?
  - Label (voor de plek-om-in-te-vullen): of je persoonsgegevens alleen af en toe gebruikt
  - Hulp: Een personeelsadministratie, klantenbestand of nieuwsbrief is een vast onderdeel en dus niet 'af en toe'.
  - Type: boolean
- **processing_risk_likely**: Kan jouw gebruik van persoonsgegevens waarschijnlijk nadelige gevolgen hebben voor de mensen om wie het gaat?
  - Label (voor de plek-om-in-te-vullen): of jouw gebruik van gegevens waarschijnlijk risico's voor mensen meebrengt
  - Hulp: Bijvoorbeeld omdat je gegevens combineert, mensen volgt of beoordeelt, of gegevens gebruikt waarmee misbruik kan worden gemaakt.
  - Type: boolean
- **processes_special_or_criminal**: Gebruik je gegevens over gezondheid, afkomst, religie, politieke opvattingen, vakbondslidmaatschap, seksuele gerichtheid, genetische of biometrische gegevens, of gegevens over strafbare feiten?
  - Label (voor de plek-om-in-te-vullen): of je gevoelige of strafrechtelijke gegevens gebruikt
  - Type: boolean
- **transfers_outside_eea**: Worden gegevens opgeslagen of bekeken buiten de Europese Unie, Noorwegen, IJsland en Liechtenstein?
  - Label (voor de plek-om-in-te-vullen): of gegevens buiten de EU/EER terechtkomen
  - Hulp: Denk aan Amerikaanse diensten voor e-mail, nieuwsbrieven, CRM, cloudopslag of AI, en aan support vanuit een land buiten Europa.
  - Type: boolean
- **transfer_details**: Naar welke landen en via welke diensten gaan de gegevens, en op welke basis?
  - Label (voor de plek-om-in-te-vullen): landen en de basis per doorgifte
  - Type: text · Alleen vragen als: `facts.transfers_outside_eea == true`
- **register_exists**: Heb je een overzicht (register) van alle manieren waarop je persoonsgegevens voor je eigen doelen gebruikt, op papier of digitaal?
  - Label (voor de plek-om-in-te-vullen): of je een verwerkingsregister hebt
  - Type: boolean · Alleen vragen als: `facts.role != "processor"`
- **reg_has_controller_details**: Staan in het register de naam en contactgegevens van je organisatie, en (als die er zijn) van een organisatie waarmee je samen verantwoordelijk bent, van je vertegenwoordiger in de EU en van je functionaris gegevensbescherming?
  - Label (voor de plek-om-in-te-vullen): of je naam en contactgegevens in het register staan
  - Type: boolean · Alleen vragen als: `facts.register_exists == true`
- **reg_has_purposes**: Staat in het register waarvoor je de gegevens gebruikt, per verwerking?
  - Label (voor de plek-om-in-te-vullen): of de doelen in het register staan
  - Type: boolean · Alleen vragen als: `facts.register_exists == true`
- **reg_has_categories**: Staat in het register over welke groepen mensen het gaat (bijvoorbeeld klanten, werknemers) en welke soorten gegevens je van hen gebruikt?
  - Label (voor de plek-om-in-te-vullen): of de soorten mensen en gegevens in het register staan
  - Type: boolean · Alleen vragen als: `facts.register_exists == true`
- **reg_has_recipients**: Staat in het register met welke soorten partijen je gegevens deelt, ook als die buiten Europa zitten?
  - Label (voor de plek-om-in-te-vullen): of de ontvangers in het register staan
  - Type: boolean · Alleen vragen als: `facts.register_exists == true`
- **reg_has_transfers**: Staat in het register naar welke landen buiten Europa gegevens gaan?
  - Label (voor de plek-om-in-te-vullen): of de doorgiften buiten de EER in het register staan
  - Type: boolean · Alleen vragen als: `facts.register_exists == true and facts.transfers_outside_eea == true`
- **reg_has_retention**: Staat in het register hoe lang je de gegevens bewaart?
  - Label (voor de plek-om-in-te-vullen): of de bewaartermijnen in het register staan
  - Type: enum (included / not_included / not_possible) · Alleen vragen als: `facts.register_exists == true`
- **reg_has_security**: Staat in het register in grote lijnen hoe je de gegevens beveiligt?
  - Label (voor de plek-om-in-te-vullen): of een beschrijving van de beveiliging in het register staat
  - Type: enum (included / not_included / not_possible) · Alleen vragen als: `facts.register_exists == true`
- **processor_register_exists**: Heb je een overzicht (register) van alle soorten werkzaamheden die je met persoonsgegevens in opdracht van klanten uitvoert?
  - Label (voor de plek-om-in-te-vullen): of je een register hebt van wat je in opdracht van klanten doet
  - Type: boolean · Alleen vragen als: `facts.role != "controller"`
- **preg_has_controllers**: Staan in dat register de naam en contactgegevens van elke klant voor wie je werkt, van jezelf, en (als die er zijn) van vertegenwoordigers en functionarissen gegevensbescherming?
  - Label (voor de plek-om-in-te-vullen): of per klant de naam en contactgegevens in dat register staan
  - Type: boolean · Alleen vragen als: `facts.processor_register_exists == true`
- **preg_has_categories**: Staat in dat register per klant welke soorten werkzaamheden je met de gegevens uitvoert?
  - Label (voor de plek-om-in-te-vullen): of per klant de soorten werkzaamheden in dat register staan
  - Type: boolean · Alleen vragen als: `facts.processor_register_exists == true`
- **preg_has_transfers**: Staat in dat register naar welke landen buiten Europa gegevens gaan?
  - Label (voor de plek-om-in-te-vullen): of de doorgiften buiten de EER in dat register staan
  - Type: boolean · Alleen vragen als: `facts.processor_register_exists == true and facts.transfers_outside_eea == true`
- **preg_has_security**: Staat in dat register in grote lijnen hoe je de gegevens beveiligt?
  - Label (voor de plek-om-in-te-vullen): of een beschrijving van de beveiliging in dat register staat
  - Type: enum (included / not_included / not_possible) · Alleen vragen als: `facts.processor_register_exists == true`
- **register_up_to_date**: Klopt het register met wat je nu werkelijk doet? Staan nieuwe systemen, diensten en werkwijzen er ook in?
  - Label (voor de plek-om-in-te-vullen): of het register actueel is
  - Type: boolean · Alleen vragen als: `facts.register_exists == true or facts.processor_register_exists == true`
- **register_available_to_ap**: Kun je het register direct aan de Autoriteit Persoonsgegevens geven als die erom vraagt?
  - Label (voor de plek-om-in-te-vullen): of je het register aan de toezichthouder kunt geven
  - Type: boolean · Alleen vragen als: `facts.register_exists == true or facts.processor_register_exists == true`

## Toetspunten

### K8.1 — Of je een verwerkingsregister moet bijhouden
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Geldt de uitzondering van art. 30 lid 5? Alleen als alle voorwaarden kloppen: minder dan 250 werknemers én geen waarschijnlijk risico én incidenteel én geen bijzondere of strafrechtelijke gegevens
- Grondslag: art. 30 lid 5 AVG
- Beoordeeld op: de antwoorden
- Nodig: employee_count, has_staff_or_customer_records, processing_only_occasional, processing_risk_likely, processes_special_or_criminal
- Beoordeling:
  - De uitzondering geldt alleen als alle voorwaarden kloppen: employee_count kleiner dan 250 én processing_risk_likely onwaar én processing_only_occasional waar én processes_special_or_criminal onwaar.
  - Structurele verwerkingen zoals personeels- en klantadministratie zijn niet incidenteel (position paper): has_staff_or_customer_records waar betekent dat de uitzondering niet geldt, ook bij een klein bedrijf.
  - Deze stap stelt de plicht vast; ontbreken van het register wordt in stap 2 getoetst. De stap levert nooit non_compliant op.
  - Duidelijk compliant: de plicht is duidelijk vastgesteld (een van de voorwaarden is duidelijk niet vervuld), of de uitzondering geldt duidelijk (alle voorwaarden bevestigd en has_staff_or_customer_records onwaar).
  - Twijfel (een of meer voorwaarden 'weet ik niet' en geen voorwaarde duidelijk niet vervuld) → geen duidelijk geval, met het advies toch een register bij te houden.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Geldt de uitzondering van art. 30 lid 5 werkelijk (alle voorwaarden, en de verwerking is incidenteel)?
- Advies bij ❌ of ⚠️: Houd een verwerkingsregister bij. Bij twijfel over de uitzondering is een register de veilige keuze; een personeels- of klantenadministratie valt nooit onder de uitzondering.
- Bronnen: AVG-art30-lid5 (AVG art. 30 lid 5); WP29-PP-art30-5 (Artikel 29-werkgroep, position paper over de uitzonderingen op de plicht tot het bijhouden van een register van verwerkingsactiviteiten (art. 30 lid 5 AVG), bekrachtigd door de EDPB)

### K8.2 — Er is een verwerkingsregister
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het register bestaat, schriftelijk of elektronisch
- Grondslag: art. 30 lid 1 en lid 3 AVG
- Alleen als: `facts.role != "processor" and facts.employee_count >= 250 or facts.role != "processor" and facts.has_staff_or_customer_records != false or facts.role != "processor" and facts.processing_only_occasional != true or facts.role != "processor" and facts.processing_risk_likely != false or facts.role != "processor" and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: register_exists, has_staff_or_customer_records, processing_only_occasional, processing_risk_likely, processes_special_or_criminal
- Beoordeling:
  - present als register_exists waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Een register op papier of digitaal (bijvoorbeeld een spreadsheet) volstaat.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Maak een verwerkingsregister: een overzicht van elke verwerking met de verplichte gegevens. Een spreadsheet volstaat.
- Bronnen: AVG-art30-lid1 (AVG art. 30 lid 1); AVG-art30-lid3 (AVG art. 30 lid 3)

### K8.3 — Je naam en contactgegevens staan in het register
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Naam en contactgegevens van de verantwoordelijke, eventuele gezamenlijke verantwoordelijke, vertegenwoordiger en FG
- Grondslag: art. 30 lid 1 sub a AVG
- Alleen als: `facts.register_exists == true and facts.role != "processor" and facts.employee_count >= 250 or facts.register_exists == true and facts.role != "processor" and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.role != "processor" and facts.processing_only_occasional != true or facts.register_exists == true and facts.role != "processor" and facts.processing_risk_likely != false or facts.register_exists == true and facts.role != "processor" and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reg_has_controller_details
- Beoordeling:
  - present als reg_has_controller_details waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zet de naam en contactgegevens van je organisatie in het register, en als die er zijn ook die van een gezamenlijke verantwoordelijke, je vertegenwoordiger en je functionaris gegevensbescherming.
- Bronnen: AVG-art30-lid1-a (AVG art. 30 lid 1 sub a)

### K8.4 — De doelen staan in het register
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Verwerkingsdoeleinden
- Grondslag: art. 30 lid 1 sub b AVG
- Alleen als: `facts.register_exists == true and facts.role != "processor" and facts.employee_count >= 250 or facts.register_exists == true and facts.role != "processor" and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.role != "processor" and facts.processing_only_occasional != true or facts.register_exists == true and facts.role != "processor" and facts.processing_risk_likely != false or facts.register_exists == true and facts.role != "processor" and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reg_has_purposes
- Beoordeling:
  - present als reg_has_purposes waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vermeld per verwerking in het register waarvoor je de gegevens gebruikt.
- Bronnen: AVG-art30-lid1-b (AVG art. 30 lid 1 sub b)

### K8.5 — De soorten mensen en gegevens staan in het register
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Categorieën betrokkenen en categorieën persoonsgegevens
- Grondslag: art. 30 lid 1 sub c AVG
- Alleen als: `facts.register_exists == true and facts.role != "processor" and facts.employee_count >= 250 or facts.register_exists == true and facts.role != "processor" and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.role != "processor" and facts.processing_only_occasional != true or facts.register_exists == true and facts.role != "processor" and facts.processing_risk_likely != false or facts.register_exists == true and facts.role != "processor" and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reg_has_categories
- Beoordeling:
  - present als reg_has_categories waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vermeld per verwerking over welke groepen mensen het gaat en welke soorten gegevens je gebruikt.
- Bronnen: AVG-art30-lid1-c (AVG art. 30 lid 1 sub c)

### K8.6 — De ontvangers staan in het register
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Categorieën ontvangers, ook ontvangers buiten de EER
- Grondslag: art. 30 lid 1 sub d AVG
- Alleen als: `facts.register_exists == true and facts.role != "processor" and facts.employee_count >= 250 or facts.register_exists == true and facts.role != "processor" and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.role != "processor" and facts.processing_only_occasional != true or facts.register_exists == true and facts.role != "processor" and facts.processing_risk_likely != false or facts.register_exists == true and facts.role != "processor" and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reg_has_recipients
- Beoordeling:
  - present als reg_has_recipients waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vermeld per verwerking met welke soorten partijen je gegevens deelt, ook partijen buiten Europa.
- Bronnen: AVG-art30-lid1-d (AVG art. 30 lid 1 sub d)

### K8.7 — Doorgiften buiten Europa staan in het register
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Doorgiften naar een derde land of internationale organisatie en, bij doorgifte op grond van art. 49 lid 1 tweede alinea, de documenten inzake de passende waarborgen
- Grondslag: art. 30 lid 1 sub e AVG
- Alleen als: `facts.register_exists == true and facts.role != "processor" and facts.transfers_outside_eea == true and facts.employee_count >= 250 or facts.register_exists == true and facts.role != "processor" and facts.transfers_outside_eea == true and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.role != "processor" and facts.transfers_outside_eea == true and facts.processing_only_occasional != true or facts.register_exists == true and facts.role != "processor" and facts.transfers_outside_eea == true and facts.processing_risk_likely != false or facts.register_exists == true and facts.role != "processor" and facts.transfers_outside_eea == true and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reg_has_transfers, transfer_details
- Beoordeling:
  - present als reg_has_transfers waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Blijkt uit transfer_details een beroep op art. 49 lid 1 tweede alinea (dwingende gerechtvaardigde belangen), dan moeten ook de waarborgen in het register staan; is dat uit de feiten niet vast te stellen: twijfel (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Staan de waarborgen in het register bij een doorgifte op grond van art. 49 lid 1 tweede alinea?
- Advies bij ❌ of ⚠️: Vermeld in het register naar welke landen buiten Europa gegevens gaan.
- Bronnen: AVG-art30-lid1-e (AVG art. 30 lid 1 sub e); AVG-art49-lid1 (AVG art. 49 lid 1)

### K8.8 — De bewaartermijnen staan in het register
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Indien mogelijk: de beoogde termijnen voor het wissen van de verschillende gegevenscategorieën
- Grondslag: art. 30 lid 1 sub f AVG
- Alleen als: `facts.register_exists == true and facts.role != "processor" and facts.employee_count >= 250 or facts.register_exists == true and facts.role != "processor" and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.role != "processor" and facts.processing_only_occasional != true or facts.register_exists == true and facts.role != "processor" and facts.processing_risk_likely != false or facts.register_exists == true and facts.role != "processor" and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reg_has_retention
- Beoordeling:
  - present als reg_has_retention included is; absent als not_included.
  - twijfel (⚠️) als not_possible: de wet eist dit 'indien mogelijk'; de reviewer beoordeelt of vaststellen echt niet mogelijk is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het werkelijk niet mogelijk een bewaartermijn te noemen?
- Advies bij ❌ of ⚠️: Vermeld per soort gegevens hoe lang je die bewaart.
- Bronnen: AVG-art30-lid1-f (AVG art. 30 lid 1 sub f)

### K8.9 — Een beschrijving van de beveiliging staat in het register
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Indien mogelijk: een algemene beschrijving van de technische en organisatorische beveiligingsmaatregelen
- Grondslag: art. 30 lid 1 sub g AVG
- Alleen als: `facts.register_exists == true and facts.role != "processor" and facts.employee_count >= 250 or facts.register_exists == true and facts.role != "processor" and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.role != "processor" and facts.processing_only_occasional != true or facts.register_exists == true and facts.role != "processor" and facts.processing_risk_likely != false or facts.register_exists == true and facts.role != "processor" and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reg_has_security
- Beoordeling:
  - present als reg_has_security included is; absent als not_included.
  - twijfel (⚠️) als not_possible: de wet eist dit 'indien mogelijk'.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het werkelijk niet mogelijk de beveiliging in grote lijnen te beschrijven?
- Advies bij ❌ of ⚠️: Neem in het register een korte beschrijving op van de belangrijkste beveiligingsmaatregelen.
- Bronnen: AVG-art30-lid1-g (AVG art. 30 lid 1 sub g); AVG-art32-lid1 (AVG art. 32 lid 1)

### K8.10 — Er is een register van wat je in opdracht van klanten doet
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Register van de verwerker: per verantwoordelijke namen en contactgegevens, categorieën verwerkingen, doorgiften en beveiliging
- Grondslag: art. 30 lid 2 AVG
- Alleen als: `facts.role != "controller" and facts.employee_count >= 250 or facts.role != "controller" and facts.has_staff_or_customer_records != false or facts.role != "controller" and facts.processing_only_occasional != true or facts.role != "controller" and facts.processing_risk_likely != false or facts.role != "controller" and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: processor_register_exists, preg_has_controllers, preg_has_categories, preg_has_transfers, preg_has_security
- Beoordeling:
  - absent als processor_register_exists onwaar is.
  - absent als preg_has_controllers of preg_has_categories onwaar is, of als transfers_outside_eea waar is en preg_has_transfers onwaar is, of als preg_has_security not_included is.
  - present als processor_register_exists, preg_has_controllers en preg_has_categories waar zijn, preg_has_transfers waar is (als er doorgiften zijn) en preg_has_security included is.
  - twijfel (⚠️) als preg_has_security not_possible is ('indien mogelijk').
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Houd als verwerker een apart register bij met per klant: namen en contactgegevens, de soorten werkzaamheden, doorgiften buiten Europa en een beschrijving van de beveiliging.
- Bronnen: AVG-art30-lid2 (AVG art. 30 lid 2); AVG-art30-lid2-a (AVG art. 30 lid 2 sub a); AVG-art30-lid2-b (AVG art. 30 lid 2 sub b); AVG-art30-lid2-c (AVG art. 30 lid 2 sub c); AVG-art30-lid2-d (AVG art. 30 lid 2 sub d)

### K8.11 — Het register is actueel en klopt met de praktijk
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Actueel en in lijn met de praktijk; geen logboek van elke handeling, wel een overzicht van elke verwerking
- Grondslag: art. 30 lid 1 en 2 AVG
- Alleen als: `facts.register_exists == true and facts.employee_count >= 250 or facts.register_exists == true and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.processing_only_occasional != true or facts.register_exists == true and facts.processing_risk_likely != false or facts.register_exists == true and facts.processes_special_or_criminal != false or facts.processor_register_exists == true and facts.employee_count >= 250 or facts.processor_register_exists == true and facts.has_staff_or_customer_records != false or facts.processor_register_exists == true and facts.processing_only_occasional != true or facts.processor_register_exists == true and facts.processing_risk_likely != false or facts.processor_register_exists == true and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: register_up_to_date
- Beoordeling:
  - Het register hoeft geen logboek van elke handeling te zijn; het moet wel elke verwerking bevatten.
  - Duidelijk non_compliant: register_up_to_date is onwaar.
  - Duidelijk compliant: register_up_to_date is waar en geen ander antwoord wijst op een verwerking die ontbreekt.
  - In alle andere gevallen geen duidelijk geval (ook bij 'weet ik niet').
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Ontbreken er verwerkingen in het register?
- Advies bij ❌ of ⚠️: Werk het register bij zodra je een nieuw systeem, een nieuwe dienst of een nieuwe werkwijze met persoonsgegevens gaat gebruiken, en loop het regelmatig na.
- Bronnen: AVG-art30-lid1 (AVG art. 30 lid 1); AVG-art30-lid2 (AVG art. 30 lid 2)

### K8.12 — Je kunt het register aan de toezichthouder geven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het register kan op verzoek aan de toezichthoudende autoriteit ter beschikking worden gesteld
- Grondslag: art. 30 lid 4 AVG
- Alleen als: `facts.register_exists == true and facts.employee_count >= 250 or facts.register_exists == true and facts.has_staff_or_customer_records != false or facts.register_exists == true and facts.processing_only_occasional != true or facts.register_exists == true and facts.processing_risk_likely != false or facts.register_exists == true and facts.processes_special_or_criminal != false or facts.processor_register_exists == true and facts.employee_count >= 250 or facts.processor_register_exists == true and facts.has_staff_or_customer_records != false or facts.processor_register_exists == true and facts.processing_only_occasional != true or facts.processor_register_exists == true and facts.processing_risk_likely != false or facts.processor_register_exists == true and facts.processes_special_or_criminal != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: register_available_to_ap
- Beoordeling:
  - present als register_available_to_ap waar is; absent als onwaar; ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zorg dat je het register direct kunt opvragen en aan de Autoriteit Persoonsgegevens kunt geven.
- Bronnen: AVG-art30-lid4 (AVG art. 30 lid 4)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): role, employee_count. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 1: de uitzondering van art. 30 lid 5 geldt alleen als alle voorwaarden kloppen: minder dan 250 werknemers én geen waarschijnlijk risico én incidenteel én geen bijzondere of strafrechtelijke gegevens. Personeels- en klantadministratie zijn niet incidenteel (position paper). Twijfel → register aanbevelen, uitkomst review.
- Stap 2-12 gelden alleen als de registerplicht duidelijk vaststaat; bij twijfel zijn ze not_applicable en geeft stap 1 review.
- Stap 3-9 (verplichte inhoud art. 30 lid 1, allemaal F): één onderdeel ontbreekt → non_compliant. Bij stap 8 en 9 ('indien mogelijk') geeft 'niet mogelijk' review.
- Stap 10: verwerker (ook als hij daarnaast verantwoordelijke is) → ook het register van art. 30 lid 2.
- Lopende wetgeving (Omnibus IV) wordt niet als geldend recht toegepast; Deze toets toetst aan de huidige tekst van art. 30 lid 5.

## Samenhang met andere kaders

- Kader K13 (/toets-doorgifte) — als `facts.transfers_outside_eea == true`: Doorgifte buiten de EER moet in het register staan en is alleen toegestaan met een adequaatheidsbesluit of passende waarborgen.
- Kader K3 (/toets-grondslag) — als `facts.processes_special_or_criminal != false`: Voor bijzondere en strafrechtelijke gegevens gelden extra regels.

## Open punten en voorbehouden

- Lopende wetswijziging — altijd vermelden: het Omnibus IV-pakket breidt verlichtingen voor het mkb uit naar een nieuwe categorie 'small mid-caps'. Raad en Parlement bereikten op 9 juni 2026 een voorlopig akkoord; volgens het persbericht van de Raad gaat het om ondernemingen met minder dan 1.000 werknemers en een jaaromzet tot € 200 miljoen of een balanstotaal tot € 172 miljoen. Het Commissievoorstel (mei 2025) wijzigde art. 30 lid 5 AVG zo dat het register alleen nog verplicht is bij verwerkingen die waarschijnlijk een hoog risico inhouden. Het persbericht noemt de AVG niet; of en in welke vorm de wijziging van art. 30 lid 5 in het akkoord staat, is nog niet bevestigd. Het akkoord moet nog formeel worden aangenomen; de definitieve AVG-tekst en ingangsdatum controleren vóór livegang. Tot die tijd toetst deze skill aan de huidige tekst.
- Stap 11 wordt alleen op een zelfverklaring (register_up_to_date) getoetst; een vergelijking met de werkelijke verwerkingen vergt het register zelf.
