# Kader K13 — Doorgifte buiten de EER

Versie 1.2 · peildatum 2026-11-10

Doel: Toetsen of doorgifte van persoonsgegevens naar een land buiten de EER (vaak via clouddiensten) is toegestaan: op basis van een adequaatheidsbesluit (voor de VS: DPF-certificering), passende waarborgen met een doorgiftetoets, of bij uitzondering op grond van art. 49, en of de doorgifte in privacyverklaring en register staat.

Bronnen: AVG-art44 (AVG art. 44); AVG-art45 (AVG art. 45); AVG-art46 (AVG art. 46); AVG-art47 (AVG art. 47); AVG-art49 (AVG art. 49); HvJEU-C-311-18 (HvJEU 16 juli 2020, C-311/18, Data Protection Commissioner/Facebook Ireland en Schrems (Schrems II)); UB-2023-1795 (Uitvoeringsbesluit (EU) 2023/1795 van de Commissie over het passende beschermingsniveau in het kader van het EU-VS Data Privacy Framework); GerEU-T-553-23 (Gerecht EU 3 september 2025, T-553/23, Latombe/Commissie); UB-2021-914 (Uitvoeringsbesluit (EU) 2021/914 van de Commissie betreffende standaardcontractbepalingen voor de doorgifte van persoonsgegevens aan derde landen); EDPB-RL-05-2021 (EDPB, Richtsnoeren 05/2021 over de wisselwerking tussen de toepassing van artikel 3 en de bepalingen inzake internationale doorgiften van hoofdstuk V van de AVG); EDPB-AB-01-2020 (EDPB, Aanbevelingen 01/2020 over maatregelen ter aanvulling van doorgifte-instrumenten om te waarborgen dat het EU-niveau van bescherming van persoonsgegevens wordt nageleefd); AP-boete-Uber-2024 (Autoriteit Persoonsgegevens, boete aan Uber voor doorgifte van persoonsgegevens naar de Verenigde Staten (2024))

## Formulier (vragen aan de gebruiker)

- **data_stored_outside_eea**: Worden gegevens opgeslagen buiten de Europese Unie, Noorwegen, IJsland en Liechtenstein?
  - Label (voor de plek-om-in-te-vullen): of gegevens buiten de EU/EER worden opgeslagen
  - Hulp: Denk aan diensten voor e-mail, nieuwsbrieven, CRM, cloudopslag, boekhouding of AI. Kijk in de voorwaarden of het privacybeleid van de leverancier waar de gegevens staan.
  - Type: boolean
- **remote_access_outside_eea**: Kunnen mensen vanuit een land buiten de EU/EER bij de gegevens, bijvoorbeeld de helpdesk of technici van een leverancier of diens onderaannemers?
  - Label (voor de plek-om-in-te-vullen): of gegevens vanuit een land buiten de EU/EER bekeken kunnen worden
  - Hulp: Ook als de gegevens zelf in Europa staan, geldt toegang op afstand vanuit een ander land als doorgifte.
  - Type: boolean
- **us_provider_eu_hosting**: Gebruik je een Amerikaanse aanbieder die je gegevens in Europa opslaat?
  - Label (voor de plek-om-in-te-vullen): of je een Amerikaanse aanbieder gebruikt die de gegevens in Europa opslaat
  - Type: boolean
- **transfer_details**: Naar welke landen gaan de gegevens, via welke diensten of partijen, en op welke basis?
  - Label (voor de plek-om-in-te-vullen): landen, diensten en de basis per doorgifte
  - Hulp: Bijvoorbeeld: 'Verenigde Staten, nieuwsbriefdienst, EU-VS Data Privacy Framework' of 'India, helpdeskpartner, standaardcontractbepalingen'.
  - Type: text · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)`
- **basis_adequacy**: Gaan (een deel van de) gegevens naar een land waarvan de Europese Commissie heeft besloten dat de bescherming daar voldoende is?
  - Label (voor de plek-om-in-te-vullen): of gegevens naar een land gaan met een adequaatheidsbesluit
  - Hulp: Voor de Verenigde Staten beantwoord je de volgende vraag.
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)`
- **basis_dpf**: Gaan (een deel van de) gegevens naar een Amerikaanse ontvanger die gecertificeerd is onder het EU-VS Data Privacy Framework?
  - Label (voor de plek-om-in-te-vullen): of gegevens naar een Amerikaanse ontvanger met DPF-certificering gaan
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)`
- **dpf_listing_verified**: Heb je gecontroleerd dat die ontvanger nu op de officiële Data Privacy Framework-lijst staat, voor de dienst die je afneemt?
  - Label (voor de plek-om-in-te-vullen): of je hebt gecontroleerd dat de ontvanger actueel op de DPF-lijst staat
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.basis_dpf != false`
- **transfer_without_adequacy**: Gaan er ook gegevens naar landen of ontvangers waarvoor geen adequaatheidsbesluit en geen DPF-certificering geldt?
  - Label (voor de plek-om-in-te-vullen): of er doorgiften zijn zonder adequaatheidsbesluit of DPF
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)`
- **basis_safeguards**: Heb je voor die doorgiften standaardcontractbepalingen van de Europese Commissie afgesloten, of gelden bindende bedrijfsvoorschriften?
  - Label (voor de plek-om-in-te-vullen): of je standaardcontractbepalingen of bindende bedrijfsvoorschriften gebruikt
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false`
- **scc_module_correct**: Is de module van de standaardcontractbepalingen gebruikt die past bij jouw rol en die van de ontvanger (bijvoorbeeld verantwoordelijke naar verwerker)?
  - Label (voor de plek-om-in-te-vullen): of de juiste module van de standaardcontractbepalingen is gebruikt
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false and facts.basis_safeguards != false`
- **tia_done**: Heb je vastgelegd onderzocht of de wetgeving en praktijk in het land van ontvangst de bescherming ondermijnen, en welke aanvullende maatregelen (bijvoorbeeld versleuteling) nodig zijn?
  - Label (voor de plek-om-in-te-vullen): of je een doorgiftetoets hebt gedaan
  - Hulp: Dit heet een doorgiftetoets of transfer impact assessment.
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false and facts.basis_safeguards != false`
- **basis_art49**: Beroep je je voor een doorgifte op een uitzondering, zoals uitdrukkelijke toestemming van de persoon of de noodzaak voor een overeenkomst met die persoon?
  - Label (voor de plek-om-in-te-vullen): of je je op een uitzondering beroept
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false`
- **art49_occasional**: Gebeurt die doorgifte alleen af en toe, in een enkel geval, en niet structureel?
  - Label (voor de plek-om-in-te-vullen): of die doorgifte alleen incidenteel gebeurt
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false and facts.basis_art49 != false`
- **art49_ground**: Op welke uitzondering beroep je je, en waarom is die in dit geval van toepassing?
  - Label (voor de plek-om-in-te-vullen): op welke uitzondering je je beroept en waarom
  - Type: text · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false and facts.basis_art49 != false`
- **transfer_in_privacy_statement**: Staat in je privacyverklaring dat gegevens buiten Europa terechtkomen, en op welke basis?
  - Label (voor de plek-om-in-te-vullen): of de doorgifte in je privacyverklaring staat
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)`
- **transfer_in_register**: Staat de doorgifte in je verwerkingsregister?
  - Label (voor de plek-om-in-te-vullen): of de doorgifte in je verwerkingsregister staat
  - Type: boolean · Alleen vragen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)`

## Toetspunten

### K13.1 — Of gegevens buiten Europa terechtkomen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Worden gegevens buiten de EER opgeslagen, of zijn ze vanaf daar toegankelijk (ook toegang op afstand door support of subverwerkers)? Toegang op afstand geldt als doorgifte
- Grondslag: art. 44 AVG
- Beoordeeld op: de antwoorden
- Nodig: data_stored_outside_eea, remote_access_outside_eea, us_provider_eu_hosting
- Beoordeling:
  - Deze stap stelt vast of er een doorgifte is. present als data_stored_outside_eea en remote_access_outside_eea allebei bekend zijn (waar of onwaar).
  - Toegang op afstand vanuit een land buiten de EER geldt als doorgifte (EDPB 05/2021).
  - Ontbrekend of 'weet ik niet' bij een van beide: ⚠️ (noem welk antwoord ontbreekt) (de organisatie moet weten waar haar gegevens heen gaan).
  - EU-hosting bij een Amerikaanse aanbieder (us_provider_eu_hosting waar) zonder opslag of toegang buiten de EER is op zichzelf geen doorgifte, maar wel een punt van aandacht (toegang door buitenlandse autoriteiten): vermelden in de toelichting, geen absent.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is voldoende duidelijk of gegevens buiten de EER worden opgeslagen of daarvandaan toegankelijk zijn?
- Advies bij ❌ of ⚠️: Zoek per leverancier uit waar de gegevens staan en vanuit welke landen zij (of hun onderaannemers) erbij kunnen.
- Bronnen: AVG-art44 (AVG art. 44); EDPB-RL-05-2021 (EDPB, Richtsnoeren 05/2021 over de wisselwerking tussen de toepassing van artikel 3 en de bepalingen inzake internationale doorgiften van hoofdstuk V van de AVG)

### K13.2 — Of het land van ontvangst een passend beschermingsniveau heeft
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Adequaatheidsbesluit voor dat land? Voor de VS: is de ontvanger gecertificeerd onder het Data Privacy Framework (actueel op de DPF-lijst)?
- Grondslag: art. 45 AVG; Uitvoeringsbesluit (EU) 2023/1795
- Alleen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and (facts.basis_adequacy != false or facts.basis_dpf != false)` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: basis_adequacy, basis_dpf, dpf_listing_verified, transfer_details
- Beoordeling:
  - present als basis_adequacy waar is en transfer_details een land noemt waarvoor een adequaatheidsbesluit in de bronnendatabase staat.
  - present voor de VS als basis_dpf waar is en dpf_listing_verified waar is.
  - absent als basis_dpf waar is en dpf_listing_verified onwaar is, tenzij transfer_details voor dezelfde ontvanger ook standaardcontractbepalingen noemt (dan twijfel (⚠️)).
  - twijfel (⚠️) als basis_adequacy waar is maar het genoemde land niet als adequaat in de bronnendatabase staat.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Geldt voor elk genoemd land of elke Amerikaanse ontvanger een adequaatheidsbesluit of een actuele DPF-certificering?
- Advies bij ❌ of ⚠️: Controleer of het land een adequaatheidsbesluit heeft. Voor Amerikaanse ontvangers: controleer op de officiële DPF-lijst dat de ontvanger actueel gecertificeerd is voor de dienst die je afneemt.
- Bronnen: AVG-art45 (AVG art. 45); UB-2023-1795 (Uitvoeringsbesluit (EU) 2023/1795 van de Commissie over het passende beschermingsniveau in het kader van het EU-VS Data Privacy Framework); GerEU-T-553-23 (Gerecht EU 3 september 2025, T-553/23, Latombe/Commissie)

### K13.3 — Of er passende waarborgen zijn waar geen adequaatheidsbesluit geldt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Zo niet: passende waarborgen (standaardcontractbepalingen met de juiste module, bindende bedrijfsvoorschriften)?
- Grondslag: art. 46 en 47 AVG; Uitvoeringsbesluit (EU) 2021/914
- Alleen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: transfer_without_adequacy, basis_safeguards, scc_module_correct, basis_art49
- Beoordeling:
  - present als basis_safeguards waar is en scc_module_correct waar is (of transfer_details bindende bedrijfsvoorschriften noemt).
  - absent als basis_safeguards onwaar is en basis_art49 onwaar is: geen adequaatheid en geen waarborgen.
  - absent als scc_module_correct onwaar is: de standaardcontractbepalingen passen niet bij de rollen.
  - twijfel (⚠️) als basis_safeguards onwaar is en basis_art49 waar is: de uitzondering wordt in stap 5 getoetst.
  - Ontbrekend of 'weet ik niet' (ook transfer_without_adequacy): ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is voor elke doorgifte zonder adequaatheid een passende waarborg met de juiste module aanwezig?
- Advies bij ❌ of ⚠️: Sluit voor doorgiften zonder adequaatheidsbesluit de standaardcontractbepalingen van de Europese Commissie af, met de module die past bij jouw rol en die van de ontvanger.
- Bronnen: AVG-art46 (AVG art. 46); AVG-art46-lid2-c (AVG art. 46 lid 2 sub c); AVG-art47 (AVG art. 47); UB-2021-914 (Uitvoeringsbesluit (EU) 2021/914 van de Commissie betreffende standaardcontractbepalingen voor de doorgifte van persoonsgegevens aan derde landen)

### K13.4 — Of je hebt onderzocht of de bescherming in het land van ontvangst werkt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bij waarborgen zonder adequaatheid: doorgiftetoets (transfer impact assessment) naar wetgeving en praktijk van het ontvangende land, met aanvullende maatregelen waar nodig
- Grondslag: art. 46 lid 1 AVG; HvJEU C-311/18 (Schrems II)
- Alleen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false and facts.basis_safeguards != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: tia_done
- Beoordeling:
  - Duidelijk compliant alleen als tia_done waar is (gedocumenteerde doorgiftetoets, met aanvullende maatregelen waar nodig).
  - Beslisregel: review tenzij duidelijk gedocumenteerd. Deze stap levert daarom geen non_compliant op; tia_done onwaar of onbekend: geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is de doorgiftetoets gedocumenteerd, en zijn de aanvullende maatregelen passend?
- Advies bij ❌ of ⚠️: Leg per doorgifte vast of de wetgeving en praktijk in het land van ontvangst de bescherming ondermijnen, en welke aanvullende maatregelen (zoals versleuteling) je neemt.
- Bronnen: AVG-art46-lid1 (AVG art. 46 lid 1); HvJEU-C-311-18 (HvJEU 16 juli 2020, C-311/18, Data Protection Commissioner/Facebook Ireland en Schrems (Schrems II)); EDPB-AB-01-2020 (EDPB, Aanbevelingen 01/2020 over maatregelen ter aanvulling van doorgifte-instrumenten om te waarborgen dat het EU-niveau van bescherming van persoonsgegevens wordt nageleefd)

### K13.5 — Of je je terecht op een uitzondering beroept
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Beroep op een uitzondering van art. 49? Alleen incidenteel en restrictief
- Grondslag: art. 49 AVG
- Alleen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false and facts.basis_art49 != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: art49_occasional, art49_ground
- Beoordeling:
  - Uitzonderingen van art. 49 worden alleen incidenteel en restrictief toegepast; bijna altijd geen duidelijk geval.
  - Duidelijk non_compliant: art49_occasional onwaar, of art49_ground beschrijft een structurele doorgifte (bijvoorbeeld het vaste gebruik van een clouddienst) zonder andere basis.
  - Duidelijk compliant alleen als art49_occasional waar is en art49_ground een uitzondering uit art. 49 lid 1 noemt die volgens de beschrijving in deze enkele situatie duidelijk van toepassing is.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de doorgifte werkelijk incidenteel, en valt die onder de genoemde uitzondering van art. 49 lid 1?
- Advies bij ❌ of ⚠️: Gebruik een uitzondering alleen voor incidentele doorgiften. Regel voor structurele doorgiften een adequaatheidsbesluit of passende waarborgen.
- Bronnen: AVG-art49 (AVG art. 49); AVG-art49-lid1 (AVG art. 49 lid 1)

### K13.6 — De doorgifte staat in je privacyverklaring en je register
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Staat de doorgifte in de privacyverklaring (K5 stap 6) en het register (K8 stap 7)?
- Grondslag: art. 13 lid 1 sub f, art. 14 lid 1 sub f en art. 30 lid 1 sub e AVG
- Alleen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: transfer_in_privacy_statement, transfer_in_register
- Beoordeling:
  - present als transfer_in_privacy_statement en transfer_in_register allebei waar zijn.
  - absent als een van beide onwaar is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vermeld de doorgifte en de basis ervan in je privacyverklaring en in je verwerkingsregister.
- Bronnen: AVG-art13-lid1-f (AVG art. 13 lid 1 sub f); AVG-art14-lid1-f (AVG art. 14 lid 1 sub f); AVG-art30-lid1-e (AVG art. 30 lid 1 sub e)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): transfer_details. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Geen adequaatheid en geen waarborgen → non_compliant.
- Stap 4 → review tenzij duidelijk gedocumenteerd.
- Stap 5 (art. 49) → bijna altijd review; alleen incidenteel en restrictief.
- EU-hosting bij een Amerikaanse aanbieder is op zichzelf geen doorgifte, maar wel een punt van aandacht (toegang door buitenlandse autoriteiten) → vermelden, geen non_compliant.
- Stap 6 → samenloop met K5 stap 6 en K8 stap 7.

## Samenhang met andere kaders

- Kader K5 (/privacyverklaring) — als `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)`: De doorgifte en de waarborg moeten in de privacyverklaring staan.
- Kader K8 (/toets-verwerkingsregister) — als `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false)`: De doorgifte moet in het verwerkingsregister staan.

## Open punten en voorbehouden

- De geldigheid van het DPF ligt in hoger beroep bij het Hof (zaak Latombe, C-703/25 P, hogere voorziening tegen GerEU T-553/23; aanhangig, peildatum 2026-11-10). Bij vernietiging vallen doorgiften op basis van het DPF zonder waarborgen direct onder non_compliant → kaderversie dan direct bijwerken.
- De lijst van landen met een adequaatheidsbesluit moet in de bronnendatabase staan; stap 2 gebruikt alleen die lijst, niet het geheugen van het model.
