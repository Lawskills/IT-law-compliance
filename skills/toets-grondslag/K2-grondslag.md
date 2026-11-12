# Kader K2 — Grondslag

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een verwerking (per doel) een geldige grondslag heeft: vooraf vastgesteld, passend bij het doel, en voldoend aan de voorwaarden van de gekozen grondslag (toestemming, overeenkomst, gerechtvaardigd belang, wettelijke verplichting, algemeen belang of vitale belangen). Ook de verenigbaarheidstoets bij gebruik voor een nieuw doel.

Bronnen: AVG-art6-lid1 (AVG art. 6 lid 1); AVG-art6-lid3 (AVG art. 6 lid 3); AVG-art6-lid4 (AVG art. 6 lid 4); AVG-overw46 (AVG overweging 46); AVG-art4-11 (AVG art. 4 punt 11); AVG-art7 (AVG art. 7); AVG-art8 (AVG art. 8); UAVG-art5 (UAVG art. 5); HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679); HvJEU-C-252-21 (HvJEU 4 juli 2023, C-252/21, Meta Platforms/Bundeskartellamt); EDPB-RL-02-2019 (EDPB, Richtsnoeren 2/2019 over de verwerking van persoonsgegevens op grond van artikel 6, lid 1, onder b), AVG in het kader van de levering van onlinediensten aan betrokkenen); HvJEU-C-13-16 (HvJEU 4 mei 2017, C-13/16, Rīgas satiksme (drie cumulatieve voorwaarden gerechtvaardigd belang)); HvJEU-C-621-22 (HvJEU 4 oktober 2024, C-621/22, Koninklijke Nederlandse Lawn Tennisbond (KNLTB)); EDPB-RL-01-2024 (EDPB, Richtsnoeren 1/2024 over de verwerking van persoonsgegevens op basis van artikel 6, lid 1, onder f), AVG (gerechtvaardigd belang))

## Formulier (vragen aan de gebruiker)

- **purpose_description**: Om welk doel gaat het? Beschrijf in één of twee zinnen wat je voor dit doel met welke gegevens doet.
  - Label (voor de plek-om-in-te-vullen): het doel en de gegevens
  - Hulp: Bijvoorbeeld: 'bestellingen bezorgen: naam, adres en telefoonnummer van klanten' of 'nieuwsbrief sturen: e-mailadres'.
  - Type: text
- **data_subject_type**: Over wie gaan de gegevens voor dit doel vooral?
  - Label (voor de plek-om-in-te-vullen): over wie de gegevens voor dit doel gaan
  - Type: enum (consumers / employees / applicants / business_contacts / website_visitors / other)
- **is_public_authority**: Is je organisatie een overheidsinstantie?
  - Label (voor de plek-om-in-te-vullen): of je organisatie een overheidsinstantie is
  - Hulp: Voor bedrijven is het antwoord nee.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **basis_determined_in_advance**: Heb je voor dit doel vóórdat je begon vastgesteld op welke grond je de gegevens mag gebruiken?
  - Label (voor de plek-om-in-te-vullen): of je vooraf hebt vastgesteld op welke grond je de gegevens gebruikt
  - Hulp: Bijvoorbeeld in je verwerkingsregister of in een intern overzicht.
  - Type: boolean
- **legal_basis**: Op welke grond gebruik je de gegevens voor dit doel?
  - Label (voor de plek-om-in-te-vullen): de grondslag voor dit doel
  - Hulp: Kies de grond die je zelf hebt vastgesteld. Weet je het niet, kies dan 'weet ik niet'.
  - Type: enum (consent / contract / legal_obligation / vital_interests / public_task / legitimate_interest / not_determined)
- **second_legal_basis**: Beroep je je voor dit doel daarnaast nog op een andere grond?
  - Label (voor de plek-om-in-te-vullen): een tweede grondslag voor hetzelfde doel
  - Type: enum (none / consent / contract / legal_obligation / vital_interests / public_task / legitimate_interest) · Alleen vragen als: `facts.legal_basis != "not_determined"`
- **switched_basis_afterwards**: Ben je voor dit doel ooit achteraf overgestapt op een andere grond, bijvoorbeeld nadat iemand zijn toestemming introk?
  - Label (voor de plek-om-in-te-vullen): of je achteraf van grondslag bent gewisseld
  - Type: boolean
- **new_purpose_for_existing_data**: Gebruik je voor dit doel gegevens die je oorspronkelijk voor een ander doel had verzameld?
  - Label (voor de plek-om-in-te-vullen): of je voor dit doel gegevens gebruikt die je voor iets anders kreeg
  - Hulp: Bijvoorbeeld klantgegevens uit bestellingen die je nu gebruikt voor een klanttevredenheidsonderzoek of om software te trainen.
  - Type: boolean
- **original_purpose**: Voor welk doel had je de gegevens oorspronkelijk verzameld?
  - Label (voor de plek-om-in-te-vullen): het oorspronkelijke doel
  - Type: text · Alleen vragen als: `facts.new_purpose_for_existing_data == true`
- **compatibility_explanation**: Hoe hangt het nieuwe doel samen met het oude, hoe gevoelig zijn de gegevens, wat merken de mensen ervan, en welke maatregelen neem je (bijvoorbeeld pseudonimiseren)?
  - Label (voor de plek-om-in-te-vullen): het verband tussen het oude en het nieuwe doel
  - Type: text · Alleen vragen als: `facts.new_purpose_for_existing_data == true`
- **informed_about_new_purpose**: Heb je de mensen over het nieuwe doel geïnformeerd voordat je ermee begon?
  - Label (voor de plek-om-in-te-vullen): of je mensen vooraf over het nieuwe doel hebt geïnformeerd
  - Type: boolean · Alleen vragen als: `facts.new_purpose_for_existing_data == true`
- **consent_method**: Hoe geven mensen voor dit doel hun toestemming?
  - Label (voor de plek-om-in-te-vullen): hoe mensen toestemming geven
  - Type: enum (active_opt_in / pre_ticked_box / silence_or_continued_use) · Alleen vragen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"`
- **consent_required_for_service**: Moet iemand toestemming geven om je product of dienst te kunnen krijgen?
  - Label (voor de plek-om-in-te-vullen): of toestemming een voorwaarde is voor je dienst
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"`
- **power_imbalance**: Vraag je de toestemming aan mensen die van jou afhankelijk zijn, zoals je eigen medewerkers?
  - Label (voor de plek-om-in-te-vullen): of er een machtsverhouding is
  - Hulp: Bijvoorbeeld werkgever en werknemer, of overheid en burger.
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"`
- **consent_bundled**: Is de toestemming voor dit doel gecombineerd met toestemming voor andere doelen, of met het accepteren van je algemene voorwaarden?
  - Label (voor de plek-om-in-te-vullen): of de toestemming is gecombineerd met iets anders
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"`
- **consent_information_complete**: Vertel je mensen bij het vragen van toestemming wie je bent, waarvoor je de gegevens gebruikt, welke gegevens het zijn en dat ze hun toestemming kunnen intrekken?
  - Label (voor de plek-om-in-te-vullen): of mensen weten waarvoor ze toestemming geven
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"`
- **withdrawal_as_easy**: Kunnen mensen hun toestemming net zo makkelijk intrekken als geven?
  - Label (voor de plek-om-in-te-vullen): of intrekken even makkelijk is als geven
  - Hulp: Bijvoorbeeld met één klik op een afmeldlink als de toestemming ook met één klik werd gegeven.
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"`
- **consent_recorded**: Leg je vast wie wanneer waarvoor toestemming gaf, en met welke tekst?
  - Label (voor de plek-om-in-te-vullen): of je kunt aantonen dat iemand toestemming gaf
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"`
- **subjects_under_16**: Kan het bij dit doel (ook) gaan om kinderen jonger dan 16 jaar?
  - Label (voor de plek-om-in-te-vullen): of het (ook) om kinderen jonger dan 16 gaat
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"`
- **parental_consent_obtained**: Geeft bij kinderen jonger dan 16 een ouder of voogd de toestemming?
  - Label (voor de plek-om-in-te-vullen): of een ouder of voogd toestemming geeft
  - Type: boolean · Alleen vragen als: `facts.subjects_under_16 == true`
- **free_counselling_service_for_minors**: Gaat het om een hulp- of adviesdienst die je rechtstreeks en gratis aan kinderen aanbiedt?
  - Label (voor de plek-om-in-te-vullen): of het gaat om gratis hulp of advies aan kinderen
  - Hulp: Bijvoorbeeld een kindertelefoon of een gratis hulplijn voor jongeren.
  - Type: boolean · Alleen vragen als: `facts.subjects_under_16 == true`
- **subject_is_contract_party**: Heb je voor dit doel een overeenkomst met de persoon zelf over wie de gegevens gaan, of wil die persoon op eigen verzoek een overeenkomst met jou sluiten?
  - Label (voor de plek-om-in-te-vullen): of de persoon zelf partij is bij de overeenkomst
  - Hulp: Een contactpersoon bij een zakelijke klant is zelf geen partij: de overeenkomst is dan met het bedrijf.
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "contract" or facts.second_legal_basis == "contract"`
- **contract_necessity_explanation**: Waarom kun je de overeenkomst niet uitvoeren zonder deze gegevens voor dit doel?
  - Label (voor de plek-om-in-te-vullen): waarom de gegevens nodig zijn voor de overeenkomst
  - Type: text · Alleen vragen als: `facts.legal_basis == "contract" or facts.second_legal_basis == "contract"`
- **legitimate_interest_description**: Welk belang heb je bij dit gebruik van de gegevens? Beschrijf het concreet.
  - Label (voor de plek-om-in-te-vullen): welk belang je hebt
  - Hulp: Bijvoorbeeld: 'voorkomen dat iemand met gestolen betaalgegevens bij ons bestelt'.
  - Type: text · Alleen vragen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`
- **li_necessity_explanation**: Waarom is dit gebruik van de gegevens nodig voor dat belang? Kan het ook met minder gegevens of op een minder ingrijpende manier, bijvoorbeeld door toestemming te vragen?
  - Label (voor de plek-om-in-te-vullen): waarom de verwerking nodig is voor dat belang
  - Type: text · Alleen vragen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`
- **reasonable_expectation**: Zouden de mensen dit gebruik redelijkerwijs verwachten op het moment dat ze je hun gegevens gaven?
  - Label (voor de plek-om-in-te-vullen): of mensen dit gebruik kunnen verwachten
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`
- **vulnerable_subjects**: Gaat het (ook) om kwetsbare mensen, zoals kinderen?
  - Label (voor de plek-om-in-te-vullen): of het om kwetsbare mensen gaat
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`
- **li_safeguards**: Welke maatregelen neem je om de gevolgen voor mensen te beperken?
  - Label (voor de plek-om-in-te-vullen): welke maatregelen je neemt om mensen te beschermen
  - Hulp: Bijvoorbeeld een eenvoudige afmeldmogelijkheid, zo min mogelijk gegevens gebruiken, of een korte bewaartermijn.
  - Type: text · Alleen vragen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`
- **li_assessment_documented**: Heb je schriftelijk vastgelegd waarom jouw belang zwaarder weegt dan de belangen van de mensen om wie het gaat?
  - Label (voor de plek-om-in-te-vullen): of je de belangenafweging hebt vastgelegd
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`
- **li_in_privacy_statement**: Staat in je privacyverklaring welk belang je voor dit doel hebt?
  - Label (voor de plek-om-in-te-vullen): of je belang in de privacyverklaring staat
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`
- **objection_right_mentioned_separately**: Wijs je mensen er duidelijk en apart van andere informatie op dat ze bezwaar kunnen maken?
  - Label (voor de plek-om-in-te-vullen): of het bezwaarrecht apart wordt gemeld
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`
- **legal_obligation_source**: Waar komt de verplichting vandaan?
  - Label (voor de plek-om-in-te-vullen): waar de verplichting vandaan komt
  - Type: enum (eu_or_dutch_law / contract / non_eu_law) · Alleen vragen als: `facts.legal_basis == "legal_obligation" or facts.second_legal_basis == "legal_obligation"`
- **legal_obligation_provision**: Welke wet of welk wetsartikel verplicht je tot dit gebruik van de gegevens?
  - Label (voor de plek-om-in-te-vullen): de wet of het wetsartikel
  - Type: text · Alleen vragen als: `facts.legal_basis == "legal_obligation" or facts.second_legal_basis == "legal_obligation"`
- **beyond_legal_requirement**: Gebruik of bewaar je voor dit doel meer gegevens, of langer, dan de wet voorschrijft?
  - Label (voor de plek-om-in-te-vullen): of je meer of langer verwerkt dan de wet vraagt
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "legal_obligation" or facts.second_legal_basis == "legal_obligation"`
- **public_task_in_law**: Is de taak waarvoor je de gegevens gebruikt in een Nederlandse wet of Europese regel vastgelegd?
  - Label (voor de plek-om-in-te-vullen): of de taak in de wet is vastgelegd
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "public_task" or facts.second_legal_basis == "public_task"`
- **public_task_provision**: In welke wet of regel staat die taak?
  - Label (voor de plek-om-in-te-vullen): de wettelijke basis van de taak
  - Type: text · Alleen vragen als: `facts.legal_basis == "public_task" or facts.second_legal_basis == "public_task"`
- **vital_interest_situation**: Beschrijf de situatie waarin je de gegevens gebruikt om iemands leven of gezondheid te beschermen.
  - Label (voor de plek-om-in-te-vullen): de noodsituatie
  - Type: text · Alleen vragen als: `facts.legal_basis == "vital_interests" or facts.second_legal_basis == "vital_interests"`
- **other_basis_possible**: Zou je in deze situatie ook toestemming kunnen vragen, of past een andere grond?
  - Label (voor de plek-om-in-te-vullen): of een andere grond mogelijk is
  - Type: boolean · Alleen vragen als: `facts.legal_basis == "vital_interests" or facts.second_legal_basis == "vital_interests"`

## Toetspunten

### K2.1 — Of je vooraf hebt bepaald op welke grond je de gegevens gebruikt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Per doel is vooraf een grondslag uit art. 6 lid 1 vastgesteld
- Grondslag: art. 6 lid 1 AVG
- Beoordeeld op: de antwoorden
- Nodig: basis_determined_in_advance, legal_basis
- Beoordeling:
  - absent als legal_basis not_determined is: geen grondslag → non_compliant.
  - present als legal_basis een van de zes grondslagen is, basis_determined_in_advance waar is, second_legal_basis ontbreekt of none is, en switched_basis_afterwards onwaar is.
  - Meerdere grondslagen voor één doel (second_legal_basis anders dan none): twijfel (⚠️). Elke grondslag moet zelfstandig kloppen.
  - switched_basis_afterwards waar: twijfel (⚠️). Achteraf wisselen, bijvoorbeeld van toestemming naar gerechtvaardigd belang na intrekking, is niet toegestaan.
  - basis_determined_in_advance onwaar terwijl nu wel een grondslag is gekozen: twijfel (⚠️) (de grondslag moet vooraf zijn vastgesteld).
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is vóór de verwerking een grondslag vastgesteld, en kloppen bij meerdere grondslagen alle grondslagen zelfstandig?
- Advies bij ❌ of ⚠️: Stel per doel vast op welke grond je de gegevens gebruikt, vóórdat je begint, en leg dat vast (bijvoorbeeld in je verwerkingsregister). Kies één grond per doel; stap niet achteraf over op een andere grond.
- Bronnen: AVG-art6-lid1 (AVG art. 6 lid 1)

### K2.2 — Of de gekozen grond past bij het doel
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De gekozen grondslag past bij het doel; toetsing per grondslag in de subkaders K2a-K2e
- Grondslag: art. 6 lid 1 en lid 3 AVG; overweging 46 AVG
- Alleen als: `facts.legal_basis != "not_determined"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: purpose_description, legal_basis, data_subject_type, is_public_authority
- Beoordeling:
  - Duidelijk non_compliant: een overheidsinstantie die zich voor haar taakuitoefening op gerechtvaardigd belang beroept (art. 6 lid 1, laatste alinea).
  - Duidelijk non_compliant: overeenkomst als grondslag voor een doel dat typisch niet onder de overeenkomst valt (profilering voor advertenties, nieuwsbrief, productverbetering), of voor gegevens van contactpersonen bij een zakelijke klant (dan meestal gerechtvaardigd belang).
  - Duidelijk compliant: typische combinaties, zoals adres voor levering, betaalgegevens of salarisadministratie voor werknemers op grond van de overeenkomst; fiscale bewaarplicht op grond van een wettelijke verplichting; nieuwsbrief op grond van toestemming.
  - Wettelijke verplichting (c) en algemeen belang (e) vereisen een basis in Unierecht of Nederlands recht (art. 6 lid 3); vitale belangen (d) alleen als geen andere grondslag past (overweging 46). De toets per grondslag staat in de subkaders; een non_compliant in een subkader betekent dat de grondslag niet past.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Past de gekozen grondslag bij dit doel, gelet op de uitkomsten van het subkader?
- Advies bij ❌ of ⚠️: Kies de grond die past bij wat je werkelijk doet. Voor een nieuwsbrief is dat meestal toestemming, voor het uitvoeren van een bestelling de overeenkomst, voor wettelijke bewaarplichten de wettelijke verplichting.
- Bronnen: AVG-art6-lid1 (AVG art. 6 lid 1); AVG-art6-lid3 (AVG art. 6 lid 3); AVG-overw46 (AVG overweging 46)

### K2.3 — Of een nieuw doel verenigbaar is met het oorspronkelijke doel
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Verenigbaarheidstoets bij verdere verwerking: verband tussen de doelen, context, aard van de gegevens, gevolgen, waarborgen; niet verenigbaar → nieuwe grondslag; vooraf informeren
- Grondslag: art. 6 lid 4 AVG; art. 13 lid 3 en art. 14 lid 4 AVG
- Alleen als: `facts.new_purpose_for_existing_data == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: original_purpose, compatibility_explanation, informed_about_new_purpose
- Beoordeling:
  - Weeg de factoren van art. 6 lid 4: verband tussen het oude en nieuwe doel, de context waarin de gegevens zijn verzameld, de aard van de gegevens, de gevolgen voor betrokkenen en passende waarborgen (zoals versleuteling of pseudonimisering).
  - Berust de verdere verwerking op toestemming of op een wettelijke bepaling, dan is de verenigbaarheidstoets volgens art. 6 lid 4 niet nodig.
  - Duidelijk non_compliant: het nieuwe doel staat duidelijk los van het oude doel (ander verband, andere context, gevolgen die mensen niet verwachten) en er is geen eigen, passende grondslag voor het nieuwe doel.
  - Duidelijk non_compliant: informed_about_new_purpose onwaar (art. 13 lid 3 / 14 lid 4).
  - Duidelijk compliant alleen als het nieuwe doel nauw aansluit bij het oude, de gevolgen beperkt zijn, er waarborgen zijn én informed_about_new_purpose waar is.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het nieuwe doel verenigbaar met het oorspronkelijke doel, of is een eigen grondslag nodig, en zijn betrokkenen vooraf geïnformeerd?
- Advies bij ❌ of ⚠️: Gebruik je gegevens voor een nieuw doel, toets dan of dat past bij het oude doel. Past het niet, dan heb je een nieuwe grond nodig (bijvoorbeeld toestemming). Informeer mensen in elk geval vóórdat je met het nieuwe doel begint.
- Bronnen: AVG-art6-lid4 (AVG art. 6 lid 4); AVG-art13-lid3 (AVG art. 13 lid 3); AVG-art14-lid4 (AVG art. 14 lid 4)

### K2a.1 — Of mensen actief toestemming geven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Toestemming door een actieve, ondubbelzinnige handeling; vooraf aangevinkt vakje, stilzwijgen of doorgaan met browsen is geen toestemming
- Grondslag: art. 4 lid 11 AVG
- Alleen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: consent_method
- Beoordeling:
  - present als consent_method active_opt_in is.
  - absent als consent_method pre_ticked_box (C-673/17) of silence_or_continued_use is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Laat mensen zelf actief toestemming geven, bijvoorbeeld door een leeg vakje aan te vinken. Een vooraf aangevinkt vakje, niet reageren of doorgaan met browsen is geen toestemming.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679)

### K2a.2 — Of mensen vrij kunnen kiezen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Toestemming is vrij gegeven: geen machtsverhouding, en de dienst is niet afhankelijk gemaakt van toestemming voor een verwerking die voor die dienst niet nodig is
- Grondslag: art. 4 lid 11 en art. 7 lid 4 AVG
- Alleen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: consent_required_for_service, power_imbalance, purpose_description
- Beoordeling:
  - Duidelijk non_compliant: consent_required_for_service waar en het doel is voor die dienst kennelijk niet nodig (bijvoorbeeld toestemming voor de nieuwsbrief als voorwaarde om te kunnen bestellen) (art. 7 lid 4).
  - power_imbalance waar (werkgever–werknemer, overheid–burger): in de regel geen duidelijk geval.
  - consent_required_for_service waar zonder dat duidelijk is of de verwerking voor de dienst nodig is: geen duidelijk geval.
  - Duidelijk compliant: consent_required_for_service onwaar en power_imbalance onwaar.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Kan de betrokkene echt vrij weigeren zonder nadeel, gelet op de machtsverhouding en de koppeling aan de dienst?
- Advies bij ❌ of ⚠️: Maak je dienst niet afhankelijk van toestemming voor iets wat voor die dienst niet nodig is. Vraag geen toestemming aan mensen die van jou afhankelijk zijn, zoals medewerkers, tenzij weigeren echt geen gevolgen heeft; kies anders een andere grond.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid4 (AVG art. 7 lid 4); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679)

### K2a.3 — Of de toestemming per doel apart wordt gevraagd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Toestemming is specifiek per doel, niet gebundeld met andere doelen of met algemene voorwaarden
- Grondslag: art. 4 lid 11 en art. 7 lid 2 AVG
- Alleen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: consent_bundled
- Beoordeling:
  - present als consent_bundled onwaar is.
  - absent als consent_bundled waar is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vraag voor elk doel apart toestemming, los van je algemene voorwaarden.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid2 (AVG art. 7 lid 2); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679)

### K2a.4 — Of mensen weten waarvoor ze toestemming geven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geïnformeerde toestemming: wie, welk doel, welke gegevens, recht op intrekken
- Grondslag: art. 4 lid 11 en art. 7 lid 3 AVG
- Alleen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: consent_information_complete
- Beoordeling:
  - present als consent_information_complete waar is.
  - absent als consent_information_complete onwaar is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vermeld bij het vragen van toestemming wie je bent, waarvoor je de gegevens gebruikt, welke gegevens het zijn en dat mensen hun toestemming altijd kunnen intrekken.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid3 (AVG art. 7 lid 3); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679)

### K2a.5 — Of mensen hun toestemming makkelijk kunnen intrekken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Intrekken is even makkelijk als geven, en de betrokkene wordt daarover vóór het geven geïnformeerd
- Grondslag: art. 7 lid 3 AVG
- Alleen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: withdrawal_as_easy, consent_information_complete
- Beoordeling:
  - present als withdrawal_as_easy waar is en consent_information_complete waar is (dat laatste omvat de mededeling over intrekken vóór het geven).
  - absent als withdrawal_as_easy onwaar is, of als consent_information_complete onwaar is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zorg dat intrekken net zo makkelijk is als toestemming geven, bijvoorbeeld met een afmeldlink, en vertel mensen dat al voordat ze toestemming geven.
- Bronnen: AVG-art7-lid3 (AVG art. 7 lid 3); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679)

### K2a.6 — Of je kunt aantonen dat mensen toestemming gaven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De verwerkingsverantwoordelijke kan aantonen dat de betrokkene toestemming heeft gegeven
- Grondslag: art. 7 lid 1 AVG
- Alleen als: `facts.legal_basis == "consent" or facts.second_legal_basis == "consent"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: consent_recorded
- Beoordeling:
  - present als consent_recorded waar is.
  - absent als consent_recorded onwaar is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg vast wie wanneer toestemming gaf, waarvoor, en met welke tekst op dat moment.
- Bronnen: AVG-art7-lid1 (AVG art. 7 lid 1); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679)

### K2a.7 — Of een ouder of voogd toestemming geeft bij kinderen jonger dan 16
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Betrokkene jonger dan 16: toestemming van de wettelijk vertegenwoordiger (art. 8 AVG bij online diensten rechtstreeks aan het kind; anders art. 5 lid 1 UAVG); uitzondering voor kosteloze hulp- en adviesdiensten (art. 5 lid 6 UAVG)
- Grondslag: art. 8 lid 1 AVG; art. 5 lid 1, 3 en 6 UAVG
- Alleen als: `facts.legal_basis == "consent" and facts.subjects_under_16 != false or facts.second_legal_basis == "consent" and facts.subjects_under_16 != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: subjects_under_16, parental_consent_obtained
- Beoordeling:
  - In Nederland is onder de 16 altijd toestemming van de wettelijk vertegenwoordiger nodig: bij een online dienst die rechtstreeks aan het kind wordt aangeboden via art. 8 AVG, in alle andere gevallen via art. 5 lid 1 UAVG.
  - present als parental_consent_obtained waar is, of als free_counselling_service_for_minors waar is (art. 5 lid 6 UAVG).
  - absent als parental_consent_obtained onwaar is en free_counselling_service_for_minors niet waar is.
  - subjects_under_16 of parental_consent_obtained ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Een kind vanaf 12 kan de toestemming zelf intrekken (art. 5 lid 3 UAVG); noem dit in de toelichting.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is toestemming van de wettelijk vertegenwoordiger verkregen, of geldt de uitzondering voor kosteloze hulp- en adviesdiensten?
- Advies bij ❌ of ⚠️: Vraag bij kinderen jonger dan 16 toestemming aan een ouder of voogd. Kinderen vanaf 12 jaar kunnen die toestemming zelf intrekken.
- Bronnen: AVG-art8-lid1 (AVG art. 8 lid 1); UAVG-art5-lid1 (UAVG art. 5 lid 1); UAVG-art5-lid3 (UAVG art. 5 lid 3); UAVG-art5-lid6 (UAVG art. 5 lid 6)

### K2b.1 — Of de persoon zelf partij is bij de overeenkomst
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De betrokkene is zelf partij bij de overeenkomst, of het gaat om precontractuele stappen op diens verzoek
- Grondslag: art. 6 lid 1 sub b AVG
- Alleen als: `facts.legal_basis == "contract" or facts.second_legal_basis == "contract"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: subject_is_contract_party, data_subject_type
- Beoordeling:
  - present als subject_is_contract_party waar is en data_subject_type niet business_contacts is.
  - absent als subject_is_contract_party onwaar is.
  - absent als data_subject_type business_contacts is: gegevens van een contactpersoon bij een zakelijke klant vallen niet onder deze grondslag (meestal gerechtvaardigd belang).
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: De grond 'overeenkomst' geldt alleen voor gegevens van de persoon met wie je zelf de overeenkomst hebt. Voor contactpersonen bij zakelijke klanten is dat meestal gerechtvaardigd belang.
- Bronnen: AVG-art6-lid1-b (AVG art. 6 lid 1 sub b); EDPB-RL-02-2019 (EDPB, Richtsnoeren 2/2019 over de verwerking van persoonsgegevens op grond van artikel 6, lid 1, onder b), AVG in het kader van de levering van onlinediensten aan betrokkenen)

### K2b.2 — Of de gegevens echt nodig zijn om de overeenkomst uit te voeren
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De verwerking is objectief onmisbaar voor de hoofdprestatie; 'handig' of 'commercieel nuttig' is niet genoeg
- Grondslag: art. 6 lid 1 sub b AVG
- Alleen als: `facts.legal_basis == "contract" or facts.second_legal_basis == "contract"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: purpose_description, contract_necessity_explanation
- Beoordeling:
  - Duidelijk compliant (typisch ✅): adres voor levering, betaalgegevens, salarisadministratie voor werknemers.
  - Duidelijk non_compliant (typisch ❌): profilering voor advertenties, nieuwsbrief, productverbetering (C-252/21: 'handig' of 'commercieel nuttig' is niet genoeg).
  - contract_necessity_explanation noemt alleen gemak, efficiëntie of commercieel nut: non_compliant als duidelijk is dat de hoofdprestatie ook zonder deze verwerking kan worden geleverd.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Kan de hoofdprestatie van de overeenkomst worden geleverd zonder deze verwerking?
- Advies bij ❌ of ⚠️: Gebruik de grond 'overeenkomst' alleen voor gegevens zonder welke je de afgesproken dienst niet kunt leveren. Voor extra's, zoals een nieuwsbrief of advertenties, kies je een andere grond.
- Bronnen: AVG-art6-lid1-b (AVG art. 6 lid 1 sub b); HvJEU-C-252-21 (HvJEU 4 juli 2023, C-252/21, Meta Platforms/Bundeskartellamt); EDPB-RL-02-2019 (EDPB, Richtsnoeren 2/2019 over de verwerking van persoonsgegevens op grond van artikel 6, lid 1, onder b), AVG in het kader van de levering van onlinediensten aan betrokkenen)

### K2c.1 — Of je een echt en rechtmatig belang hebt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Belang: concreet, reëel en rechtmatig; commercieel belang kan
- Grondslag: art. 6 lid 1 sub f AVG
- Alleen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: legitimate_interest_description, is_public_authority, li_assessment_documented
- Beoordeling:
  - Het belang moet concreet, reëel en rechtmatig zijn (C-13/16: drie cumulatieve voorwaarden). Een commercieel belang kan gerechtvaardigd zijn, mits niet in strijd met de wet (C-621/22); het eerdere strengere AP-standpunt is daarmee achterhaald.
  - Duidelijk non_compliant: het belang is vaag ('bedrijfsvoering', 'ons belang') of onwettig; of is_public_authority waar en het gaat om de taakuitoefening (art. 6 lid 1, laatste alinea).
  - Duidelijk compliant alleen bij een concreet, rechtmatig belang én li_assessment_documented waar (beslisregel K2c: ✅ alleen bij een duidelijk en gedocumenteerd geval).
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het belang concreet, reëel en rechtmatig?
- Advies bij ❌ of ⚠️: Omschrijf je belang concreet, bijvoorbeeld 'voorkomen dat iemand met gestolen betaalgegevens bestelt'. Een vage omschrijving als 'bedrijfsvoering' is niet genoeg.
- Bronnen: AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); HvJEU-C-13-16 (HvJEU 4 mei 2017, C-13/16, Rīgas satiksme (drie cumulatieve voorwaarden gerechtvaardigd belang)); HvJEU-C-621-22 (HvJEU 4 oktober 2024, C-621/22, Koninklijke Nederlandse Lawn Tennisbond (KNLTB)); EDPB-RL-01-2024 (EDPB, Richtsnoeren 1/2024 over de verwerking van persoonsgegevens op basis van artikel 6, lid 1, onder f), AVG (gerechtvaardigd belang))

### K2c.2 — Of het ook minder ingrijpend kan
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Noodzaak: het doel kan niet even doeltreffend met minder ingrijpende middelen worden bereikt
- Grondslag: art. 6 lid 1 sub f AVG
- Alleen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: li_necessity_explanation, li_assessment_documented
- Beoordeling:
  - Toets of het doel even doeltreffend kan worden bereikt met minder gegevens of een minder ingrijpende verwerking. In C-621/22 wees het Hof op het vragen van toestemming als minder ingrijpend alternatief.
  - Duidelijk non_compliant: li_necessity_explanation laat zelf zien dat een even doeltreffend, minder ingrijpend alternatief voorhanden is en niet wordt gebruikt.
  - Duidelijk compliant alleen als geen minder ingrijpend alternatief voor de hand ligt én li_assessment_documented waar is.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de verwerking noodzakelijk, of kan het doel even doeltreffend met minder ingrijpende middelen worden bereikt?
- Advies bij ❌ of ⚠️: Ga na of je hetzelfde kunt bereiken met minder gegevens of op een minder ingrijpende manier, bijvoorbeeld door toestemming te vragen. Leg die afweging vast.
- Bronnen: AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); HvJEU-C-621-22 (HvJEU 4 oktober 2024, C-621/22, Koninklijke Nederlandse Lawn Tennisbond (KNLTB)); EDPB-RL-01-2024 (EDPB, Richtsnoeren 1/2024 over de verwerking van persoonsgegevens op basis van artikel 6, lid 1, onder f), AVG (gerechtvaardigd belang))

### K2c.3 — Of jouw belang zwaarder weegt dan dat van de mensen om wie het gaat
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Afweging: de belangen of grondrechten van de betrokkene wegen niet zwaarder; factoren: redelijke verwachtingen, aard van de gegevens, omvang, gevolgen, kwetsbare betrokkenen, waarborgen
- Grondslag: art. 6 lid 1 sub f AVG; overweging 47 AVG
- Alleen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: purpose_description, reasonable_expectation, vulnerable_subjects, li_assessment_documented
- Beoordeling:
  - Factoren: redelijke verwachtingen bij verzameling (overweging 47), aard van de gegevens, omvang, gevolgen, kwetsbare betrokkenen (kinderen), waarborgen (opt-out, minimalisatie, korte bewaartermijn; li_safeguards).
  - Duidelijk non_compliant: reasonable_expectation onwaar en vulnerable_subjects waar, zonder waarborgen van betekenis.
  - Duidelijk compliant alleen als reasonable_expectation waar is, vulnerable_subjects onwaar, er waarborgen zijn én li_assessment_documented waar is.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Wegen de belangen of grondrechten van de betrokkenen zwaarder dan het belang van de organisatie?
- Advies bij ❌ of ⚠️: Weeg jouw belang af tegen de belangen van de mensen om wie het gaat: verwachten zij dit, hoe gevoelig zijn de gegevens, en welke maatregelen neem je (zoals een eenvoudige afmeldmogelijkheid of een korte bewaartermijn)?
- Bronnen: AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); AVG-overw47 (AVG overweging 47); HvJEU-C-621-22 (HvJEU 4 oktober 2024, C-621/22, Koninklijke Nederlandse Lawn Tennisbond (KNLTB)); EDPB-RL-01-2024 (EDPB, Richtsnoeren 1/2024 over de verwerking van persoonsgegevens op basis van artikel 6, lid 1, onder f), AVG (gerechtvaardigd belang))

### K2c.4 — Of je de belangenafweging hebt vastgelegd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De afweging is vastgelegd, zodat de verwerkingsverantwoordelijke haar kan aantonen
- Grondslag: art. 5 lid 2 AVG
- Alleen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: li_assessment_documented
- Beoordeling:
  - present als li_assessment_documented waar is.
  - absent als li_assessment_documented onwaar is → review: dit maakt de verwerking niet zonder meer onrechtmatig, maar de klant kan de rechtmatigheid dan niet aantonen.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Kan de klant de belangenafweging aantonen?
- Advies bij ❌ of ⚠️: Leg de belangenafweging schriftelijk vast: jouw belang, waarom de verwerking nodig is, en waarom de belangen van de mensen om wie het gaat niet zwaarder wegen.
- Bronnen: AVG-art5-lid2 (AVG art. 5 lid 2); EDPB-RL-01-2024 (EDPB, Richtsnoeren 1/2024 over de verwerking van persoonsgegevens op basis van artikel 6, lid 1, onder f), AVG (gerechtvaardigd belang))

### K2c.5 — Of je belang en het bezwaarrecht in de privacyverklaring staan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Het belang wordt vermeld in de privacyverklaring, en het recht van bezwaar wordt apart gemeld
- Grondslag: art. 13 lid 1 sub d, art. 14 lid 2 sub b en art. 21 lid 4 AVG
- Alleen als: `facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: li_in_privacy_statement, objection_right_mentioned_separately
- Beoordeling:
  - present als li_in_privacy_statement waar is en objection_right_mentioned_separately waar is.
  - absent als een van beide onwaar is. De inhoudelijke toets van de verklaring gebeurt in de toets van de privacyverklaring.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vermeld in je privacyverklaring welk belang je hebt, en wijs mensen duidelijk en apart op hun recht om bezwaar te maken.
- Bronnen: AVG-art13-lid1-d (AVG art. 13 lid 1 sub d); AVG-art14-lid2-b (AVG art. 14 lid 2 sub b); AVG-art21-lid4 (AVG art. 21 lid 4)

### K2d.1 — Welke wet je verplicht om de gegevens te gebruiken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Een concrete wettelijke bepaling uit Unierecht of Nederlands recht verplicht de verwerking; een contractuele verplichting of recht van een land buiten de EU telt niet
- Grondslag: art. 6 lid 1 sub c en lid 3 AVG
- Alleen als: `facts.legal_basis == "legal_obligation" or facts.second_legal_basis == "legal_obligation"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: legal_obligation_source, legal_obligation_provision
- Beoordeling:
  - present als legal_obligation_source eu_or_dutch_law is en legal_obligation_provision een concrete wet of bepaling noemt.
  - absent als legal_obligation_source contract of non_eu_law is: dat is geen wettelijke verplichting in deze zin.
  - absent als er geen aanwijsbare bepaling is (legal_obligation_provision leeg of alleen 'de wet').
  - legal_obligation_provision 'weet ik niet' bij eu_or_dutch_law: twijfel (⚠️).
  - Ontbrekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de genoemde bepaling een wettelijke verplichting uit Unierecht of Nederlands recht die deze verwerking vereist?
- Advies bij ❌ of ⚠️: Noem de concrete wet of het wetsartikel dat je verplicht. Een afspraak in een contract of een wet van een land buiten de EU is geen wettelijke verplichting in de zin van de AVG; kies dan een andere grond.
- Bronnen: AVG-art6-lid1-c (AVG art. 6 lid 1 sub c); AVG-art6-lid3 (AVG art. 6 lid 3)

### K2d.2 — Of je niet meer doet dan de wet vraagt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De verwerking blijft binnen wat de bepaling vereist (niet meer gegevens, niet langer bewaren)
- Grondslag: art. 6 lid 1 sub c en lid 3 AVG
- Alleen als: `facts.legal_basis == "legal_obligation" or facts.second_legal_basis == "legal_obligation"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: beyond_legal_requirement, legal_obligation_provision
- Beoordeling:
  - Duidelijk non_compliant: beyond_legal_requirement waar (meer gegevens of langer dan de bepaling vereist).
  - Duidelijk compliant: beyond_legal_requirement onwaar en de bepaling is concreet genoemd.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Blijft de verwerking binnen wat de wettelijke bepaling vereist?
- Advies bij ❌ of ⚠️: Gebruik en bewaar alleen de gegevens die de wet voorschrijft, en niet langer dan de wet vraagt. Voor wat je daarnaast doet, heb je een andere grond nodig.
- Bronnen: AVG-art6-lid1-c (AVG art. 6 lid 1 sub c); AVG-art6-lid3 (AVG art. 6 lid 3)

### K2e.1 — Of je taak van algemeen belang in de wet staat
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Grondslag (e): een taak van algemeen belang of openbaar gezag die in Unierecht of Nederlands recht is vastgelegd
- Grondslag: art. 6 lid 1 sub e en lid 3 AVG
- Alleen als: `facts.legal_basis == "public_task" or facts.second_legal_basis == "public_task"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: public_task_in_law
- Beoordeling:
  - present als public_task_in_law waar is en public_task_provision een concrete wettelijke basis noemt.
  - absent als public_task_in_law onwaar is.
  - Voor gewone bedrijven zelden van toepassing: bij twijfel (geen of vage public_task_provision, of een bedrijf zonder wettelijke publieke taak) twijfel (⚠️).
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de taak in Unierecht of Nederlands recht vastgelegd, en valt deze verwerking daaronder?
- Advies bij ❌ of ⚠️: Deze grond geldt alleen voor een taak die in de wet is vastgelegd. Voor de meeste bedrijven past een andere grond.
- Bronnen: AVG-art6-lid1-e (AVG art. 6 lid 1 sub e); AVG-art6-lid3 (AVG art. 6 lid 3)

### K2e.2 — Of het gaat om iemands leven of gezondheid in een noodsituatie
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Grondslag (d): bescherming van iemands leven of gezondheid in een situatie waarin geen andere grondslag past
- Grondslag: art. 6 lid 1 sub d AVG; overweging 46 AVG
- Alleen als: `facts.legal_basis == "vital_interests" or facts.second_legal_basis == "vital_interests"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: vital_interest_situation, other_basis_possible
- Beoordeling:
  - Duidelijk non_compliant: vital_interest_situation beschrijft geen bedreiging van leven of gezondheid, of other_basis_possible waar (overweging 46: alleen als geen andere grondslag past).
  - Duidelijk compliant: een acute bedreiging van leven of gezondheid én other_basis_possible onwaar.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Gaat het om bescherming van leven of gezondheid, en past echt geen andere grondslag?
- Advies bij ❌ of ⚠️: Deze grond is alleen bedoeld voor noodsituaties waarin iemands leven of gezondheid op het spel staat en geen andere grond past.
- Bronnen: AVG-art6-lid1-d (AVG art. 6 lid 1 sub d); AVG-overw46 (AVG overweging 46)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): purpose_description, data_subject_type, is_public_authority, second_legal_basis, original_purpose, compatibility_explanation, contract_necessity_explanation, legitimate_interest_description, li_necessity_explanation, vital_interest_situation. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Het kader wordt per doel doorlopen; een subkader geldt alleen als de klant die grondslag voor dit doel noemt (applies_if).
- Stap 1: geen grondslag → non_compliant; meerdere grondslagen voor één doel → review (elke grondslag moet zelfstandig kloppen); achteraf wisselen is niet toegestaan.
- Overheidsinstanties kunnen zich voor hun taakuitoefening niet op gerechtvaardigd belang beroepen (art. 6 lid 1, laatste alinea). Grondslag (c) en (e) vereisen een basis in Unierecht of Nederlands recht (art. 6 lid 3). Grondslag (d) alleen als geen andere grondslag past (overweging 46).
- K2b: typisch ✅ adres voor levering, betaalgegevens, salarisadministratie voor werknemers; typisch ❌ profilering voor advertenties, nieuwsbrief, productverbetering.
- K2c: stap 1 t/m 3 zijn afwegingen. ✅ alleen bij een duidelijk en gedocumenteerd geval; ❌ bij een duidelijke tekortkoming; anders review. Stap 4 zonder vastgelegde afweging → review, niet non_compliant.
- K2a wordt ook gebruikt door CK2 (cookietoestemming).
- Nieuw doel (stap 3) of gerechtvaardigd belang → ook route K5 (informatieplicht).

## Samenhang met andere kaders

- Kader K5 (/privacyverklaring) — als `facts.new_purpose_for_existing_data == true or facts.legal_basis == "legitimate_interest" or facts.second_legal_basis == "legitimate_interest"`: Een nieuw doel en een gerechtvaardigd belang moeten in de privacyverklaring staan; bij gerechtvaardigd belang ook het bezwaarrecht apart.

## Open punten en voorbehouden

- K2c.5 overlapt met K5 (stap 4 en 20). Bij een volledige route telt de bevinding in beide kaders; dubbeltelling in het rapport voorkomen.
