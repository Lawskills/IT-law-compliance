# Kader K9 — DPIA-toets

Versie 1.2 · peildatum 2026-11-10

Doel: Vaststellen of een gegevensbeschermingseffectbeoordeling (DPIA) verplicht is (art. 35 lid 1 en 3 AVG, de AP-lijst en de negen WP248-criteria), en, als de klant dat vraagt, of een uitgevoerde DPIA de minimale onderdelen van art. 35 lid 7 bevat en of voorafgaande raadpleging van de AP nodig was (art. 36).

Bronnen: AVG-art35 (AVG art. 35); AVG-art35-lid1 (AVG art. 35 lid 1); AVG-art35-lid3 (AVG art. 35 lid 3); AVG-art35-lid4 (AVG art. 35 lid 4); AVG-art35-lid7 (AVG art. 35 lid 7); AVG-art35-lid11 (AVG art. 35 lid 11); AVG-art36-lid1 (AVG art. 36 lid 1); AP-DPIA-lijst-2019 (Besluit van de Autoriteit Persoonsgegevens inzake de lijst van verwerkingen van persoonsgegevens waarvoor een gegevensbeschermingseffectbeoordeling (DPIA) verplicht is); WP248-rev01 (Artikel 29-werkgroep, Richtsnoeren voor gegevensbeschermingseffectbeoordelingen (DPIA) en bepaling of een verwerking "waarschijnlijk een hoog risico inhoudt" (WP248 rev.01), bekrachtigd door de EDPB)

## Formulier (vragen aan de gebruiker)

- **processing_description**: Beschrijf de verwerking waar het om gaat: welke gegevens, van wie, waarvoor, met welke systemen, en hoeveel mensen het ongeveer betreft.
  - Label (voor de plek-om-in-te-vullen): een beschrijving van de verwerking
  - Type: text
- **art35_profiling**: Beoordeel je stelselmatig en uitgebreid persoonlijke kenmerken van mensen met behulp van software (bijvoorbeeld profilering), en neem je op basis daarvan besluiten met rechtsgevolgen of andere ingrijpende gevolgen voor hen?
  - Label (voor de plek-om-in-te-vullen): of je mensen stelselmatig automatisch beoordeelt en daar belangrijke besluiten op baseert
  - Hulp: Bijvoorbeeld een automatische kredietbeoordeling, of een systeem dat sollicitanten rangschikt en op basis waarvan mensen worden afgewezen.
  - Type: boolean
- **art35_special_large_scale**: Gebruik je op grote schaal gegevens over gezondheid, afkomst, religie, politieke opvattingen, vakbondslidmaatschap, seksuele gerichtheid, genetische of biometrische gegevens, of gegevens over strafbare feiten?
  - Label (voor de plek-om-in-te-vullen): of je op grote schaal gevoelige of strafrechtelijke gegevens gebruikt
  - Type: boolean
- **art35_public_monitoring**: Houd je stelselmatig en op grote schaal toezicht op plekken die voor iedereen toegankelijk zijn, bijvoorbeeld met camera's?
  - Label (voor de plek-om-in-te-vullen): of je openbare ruimtes stelselmatig en op grote schaal in de gaten houdt
  - Type: boolean
- **on_ap_list**: Staat deze soort verwerking op de lijst van de Autoriteit Persoonsgegevens met verwerkingen waarvoor een DPIA altijd verplicht is?
  - Label (voor de plek-om-in-te-vullen): of de verwerking op de DPIA-lijst van de Autoriteit Persoonsgegevens staat
  - Type: boolean
- **dpia_status**: Heb je voor deze verwerking een DPIA uitgevoerd?
  - Label (voor de plek-om-in-te-vullen): of je een DPIA hebt uitgevoerd, en wanneer
  - Type: enum (done_before_start / done_after_start / planned_not_started / not_done)
- **wp248_scoring**: Beoordeel of scoor je mensen, bijvoorbeeld op kredietwaardigheid, gezondheid, prestaties, gedrag of voorkeuren?
  - Label (voor de plek-om-in-te-vullen): of je mensen beoordeelt of een score geeft
  - Type: boolean
- **wp248_automated_decision**: Neemt software automatisch besluiten over mensen met rechtsgevolgen of een vergelijkbaar ingrijpend effect?
  - Label (voor de plek-om-in-te-vullen): of software besluiten neemt met rechtsgevolg of een vergelijkbaar effect
  - Type: boolean
- **wp248_systematic_monitoring**: Volg of observeer je mensen stelselmatig, bijvoorbeeld met camera's, locatiegegevens of het monitoren van computergebruik?
  - Label (voor de plek-om-in-te-vullen): of je mensen stelselmatig volgt of in de gaten houdt
  - Type: boolean
- **wp248_sensitive_data**: Gaat het om gevoelige of zeer persoonlijke gegevens, zoals gezondheid, strafrechtelijke gegevens, financiële gegevens of locatiegegevens?
  - Label (voor de plek-om-in-te-vullen): of het om gevoelige of zeer persoonlijke gegevens gaat
  - Type: boolean
- **wp248_large_scale**: Gaat het om veel mensen, veel gegevens, een lange periode of een groot gebied?
  - Label (voor de plek-om-in-te-vullen): of het om een grote schaal gaat
  - Type: boolean
- **wp248_matching_datasets**: Koppel of combineer je gegevens uit verschillende bronnen, op een manier die mensen niet zouden verwachten?
  - Label (voor de plek-om-in-te-vullen): of je gegevensverzamelingen combineert
  - Type: boolean
- **wp248_vulnerable_subjects**: Gaat het om kwetsbare mensen, zoals kinderen, patiënten, ouderen, of werknemers tegenover hun werkgever?
  - Label (voor de plek-om-in-te-vullen): of het om kwetsbare mensen gaat
  - Type: boolean
- **wp248_innovative_technology**: Gebruik je nieuwe of innovatieve technologie, zoals AI, gezichtsherkenning of slimme apparaten?
  - Label (voor de plek-om-in-te-vullen): of je nieuwe technologie gebruikt
  - Type: boolean
- **wp248_prevents_rights**: Kan de verwerking ertoe leiden dat mensen een recht niet kunnen uitoefenen of een dienst of contract niet krijgen?
  - Label (voor de plek-om-in-te-vullen): of de verwerking mensen kan uitsluiten van een recht of dienst
  - Type: boolean
- **uses_ai**: Gebruik je bij deze verwerking AI of andere zelflerende software?
  - Label (voor de plek-om-in-te-vullen): of je AI gebruikt bij deze verwerking
  - Type: boolean
- **uses_cameras**: Gebruik je camera's bij deze verwerking?
  - Label (voor de plek-om-in-te-vullen): of je camera's gebruikt
  - Type: boolean
- **processing_changed**: Is deze verwerking sinds de vorige beoordeling veranderd, of zijn de risico's voor de mensen veranderd?
  - Label (voor de plek-om-in-te-vullen): of de verwerking of het risico is veranderd
  - Hulp: Bijvoorbeeld nieuwe gegevens, een nieuw doel, een nieuwe leverancier of nieuwe software.
  - Type: boolean
- **reassessed_after_change**: Heb je na die wijziging opnieuw beoordeeld of een DPIA nodig is, of je DPIA bijgewerkt?
  - Label (voor de plek-om-in-te-vullen): of je na de wijziging opnieuw hebt beoordeeld
  - Type: boolean · Alleen vragen als: `facts.processing_changed == true`
- **dpia_document_review**: Wil je ook laten controleren of je DPIA de onderdelen bevat die de wet voorschrijft?
  - Label (voor de plek-om-in-te-vullen): of je de inhoud van je DPIA wilt laten controleren
  - Type: boolean · Alleen vragen als: `facts.dpia_status == "done_before_start" or facts.dpia_status == "done_after_start"`
- **dpia_has_description**: Beschrijft je DPIA de verwerking en de doelen systematisch, inclusief (als dat van toepassing is) het gerechtvaardigde belang?
  - Label (voor de plek-om-in-te-vullen): of de DPIA de verwerking en de doelen beschrijft
  - Type: boolean · Alleen vragen als: `facts.dpia_document_review == true`
- **dpia_has_necessity**: Beoordeelt je DPIA of de verwerking noodzakelijk is en in verhouding staat tot het doel?
  - Label (voor de plek-om-in-te-vullen): of de DPIA de noodzaak en evenredigheid beoordeelt
  - Type: boolean · Alleen vragen als: `facts.dpia_document_review == true`
- **dpia_has_risk_assessment**: Beoordeelt je DPIA de risico's voor de mensen van wie je de gegevens gebruikt?
  - Label (voor de plek-om-in-te-vullen): of de DPIA de risico's voor mensen beoordeelt
  - Type: boolean · Alleen vragen als: `facts.dpia_document_review == true`
- **dpia_has_measures**: Beschrijft je DPIA welke maatregelen je neemt om die risico's aan te pakken?
  - Label (voor de plek-om-in-te-vullen): of de DPIA maatregelen tegen de risico's beschrijft
  - Type: boolean · Alleen vragen als: `facts.dpia_document_review == true`
- **has_dpo**: Heb je een functionaris gegevensbescherming (FG)?
  - Label (voor de plek-om-in-te-vullen): of je een functionaris gegevensbescherming hebt
  - Hulp: Ook als je vrijwillig een FG hebt aangesteld.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **dpia_dpo_advice**: Heb je bij de DPIA het advies van je functionaris gegevensbescherming gevraagd?
  - Label (voor de plek-om-in-te-vullen): of je de FG om advies hebt gevraagd
  - Type: boolean · Alleen vragen als: `facts.dpia_document_review == true and facts.has_dpo == true`
- **dpia_views_sought**: Heb je de mening gevraagd van de mensen om wie het gaat, of van hun vertegenwoordigers (bijvoorbeeld de ondernemingsraad)?
  - Label (voor de plek-om-in-te-vullen): of je de mening van betrokkenen hebt gevraagd
  - Type: boolean · Alleen vragen als: `facts.dpia_document_review == true`
- **dpia_views_reason**: Licht toe hoe je de mening hebt gevraagd, of waarom je dat niet passend vond.
  - Label (voor de plek-om-in-te-vullen): waarom je de mening wel of niet hebt gevraagd
  - Type: text · Alleen vragen als: `facts.dpia_document_review == true`
- **dpia_high_residual_risk**: Blijft er volgens je DPIA na de maatregelen nog een hoog risico voor de mensen over?
  - Label (voor de plek-om-in-te-vullen): of er na de maatregelen een hoog risico overblijft
  - Type: boolean · Alleen vragen als: `facts.dpia_document_review == true`
- **ap_prior_consultation**: Heb je de Autoriteit Persoonsgegevens geraadpleegd voordat je met de verwerking begon?
  - Label (voor de plek-om-in-te-vullen): of je de Autoriteit Persoonsgegevens vooraf hebt geraadpleegd
  - Type: boolean · Alleen vragen als: `facts.dpia_high_residual_risk == true`

## Toetspunten (voor de eindcontrole)

### K9.1 — Of de wet voor deze verwerking altijd een DPIA eist
- Grondslag: art. 35 lid 1 en lid 3 AVG
- Toetspunt: Valt de verwerking onder art. 35 lid 3 (a: systematische en uitgebreide beoordeling met profilering en ingrijpende besluiten; b: grootschalige verwerking van bijzondere of strafrechtelijke gegevens; c: stelselmatige en grootschalige monitoring van openbaar toegankelijke ruimten)? Ja = DPIA verplicht
- Bronnen: AVG-art35-lid1 (AVG art. 35 lid 1); AVG-art35-lid3-a (AVG art. 35 lid 3 sub a); AVG-art35-lid3-b (AVG art. 35 lid 3 sub b); AVG-art35-lid3-c (AVG art. 35 lid 3 sub c)
- Wat de tekst moet bereiken: Voer een DPIA uit voordat je met deze verwerking begint (of alsnog, zo snel mogelijk, als de verwerking al loopt).

### K9.2 — Of de verwerking op de DPIA-lijst van de toezichthouder staat
- Grondslag: art. 35 lid 4 AVG; Besluit AP inzake lijst van verwerkingen waarvoor een DPIA verplicht is
- Toetspunt: Staat de verwerking op de AP-lijst (Stcrt. 2019, 64418)? Ja = DPIA verplicht
- Bronnen: AVG-art35-lid4 (AVG art. 35 lid 4); AP-DPIA-lijst-2019 (Besluit van de Autoriteit Persoonsgegevens inzake de lijst van verwerkingen van persoonsgegevens waarvoor een gegevensbeschermingseffectbeoordeling (DPIA) verplicht is)
- Wat de tekst moet bereiken: Controleer of je verwerking op de lijst van de Autoriteit Persoonsgegevens staat. Zo ja, voer een DPIA uit voordat je begint.

### K9.3 — Hoeveel risicokenmerken de verwerking heeft
- Grondslag: art. 35 lid 1 AVG; WP248 rev.01
- Toetspunt: Hoeveel van de negen WP248-criteria gelden? Twee of meer → in de meeste gevallen DPIA nodig; één of geen → meestal geen DPIA, onderbouwing vastleggen
- Bronnen: AVG-art35-lid1 (AVG art. 35 lid 1); WP248-rev01 (Artikel 29-werkgroep, Richtsnoeren voor gegevensbeschermingseffectbeoordelingen (DPIA) en bepaling of een verwerking "waarschijnlijk een hoog risico inhoudt" (WP248 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Bij twee of meer risicokenmerken: voer een DPIA uit. Bij één of geen: leg vast waarom je geen DPIA uitvoert.

### K9.4 — Of je opnieuw hebt beoordeeld na een wijziging
- Grondslag: art. 35 lid 11 AVG
- Toetspunt: Bestaande verwerking gewijzigd, of veranderd risico? Opnieuw toetsen
- Alleen als: `facts.processing_changed == true`
- Bronnen: AVG-art35-lid11 (AVG art. 35 lid 11)
- Wat de tekst moet bereiken: Beoordeel na elke wijziging van de verwerking of van het risico opnieuw of een DPIA nodig is, en werk een bestaande DPIA bij.

### K9.5 — De DPIA beschrijft de verwerking en de doelen
- Grondslag: art. 35 lid 7 sub a AVG
- Toetspunt: Systematische beschrijving van de verwerking en de doelen (inclusief eventueel gerechtvaardigd belang)
- Alleen als: `facts.dpia_document_review == true`
- Bronnen: AVG-art35-lid7-a (AVG art. 35 lid 7 sub a)
- Wat de tekst moet bereiken: Neem in de DPIA een systematische beschrijving op van de verwerking en de doelen, en van het gerechtvaardigde belang als je je daarop beroept.

### K9.6 — De DPIA beoordeelt noodzaak en evenredigheid
- Grondslag: art. 35 lid 7 sub b AVG
- Toetspunt: Beoordeling van de noodzaak en evenredigheid van de verwerking
- Alleen als: `facts.dpia_document_review == true`
- Bronnen: AVG-art35-lid7-b (AVG art. 35 lid 7 sub b)
- Wat de tekst moet bereiken: Beoordeel in de DPIA of de verwerking noodzakelijk is en in verhouding staat tot het doel.

### K9.7 — De DPIA beoordeelt de risico's voor mensen
- Grondslag: art. 35 lid 7 sub c AVG
- Toetspunt: Beoordeling van de risico's voor de rechten en vrijheden van betrokkenen
- Alleen als: `facts.dpia_document_review == true`
- Bronnen: AVG-art35-lid7-c (AVG art. 35 lid 7 sub c)
- Wat de tekst moet bereiken: Beoordeel in de DPIA welke risico's de verwerking heeft voor de mensen om wie het gaat.

### K9.8 — De DPIA beschrijft maatregelen tegen de risico's
- Grondslag: art. 35 lid 7 sub d AVG
- Toetspunt: De beoogde maatregelen om de risico's aan te pakken
- Alleen als: `facts.dpia_document_review == true`
- Bronnen: AVG-art35-lid7-d (AVG art. 35 lid 7 sub d)
- Wat de tekst moet bereiken: Beschrijf in de DPIA welke maatregelen je neemt om de risico's aan te pakken.

### K9.9 — Je hebt je functionaris gegevensbescherming om advies gevraagd
- Grondslag: art. 35 lid 2 AVG
- Toetspunt: Advies van de FG gevraagd (als er een FG is)
- Alleen als: `facts.dpia_document_review == true and facts.has_dpo == true`
- Bronnen: AVG-art35-lid2 (AVG art. 35 lid 2)
- Wat de tekst moet bereiken: Vraag je functionaris gegevensbescherming om advies bij de DPIA en leg dat advies vast.

### K9.10 — Of je waar passend de mening van betrokkenen hebt gevraagd
- Grondslag: art. 35 lid 9 AVG
- Toetspunt: Waar passend de mening van betrokkenen of hun vertegenwoordigers gevraagd
- Alleen als: `facts.dpia_document_review == true`
- Bronnen: AVG-art35-lid9 (AVG art. 35 lid 9)
- Wat de tekst moet bereiken: Vraag waar passend de mening van de mensen om wie het gaat of van hun vertegenwoordigers (bijvoorbeeld de ondernemingsraad), of leg vast waarom dat niet passend is.

### K9.11 — Of je de toezichthouder vooraf hebt geraadpleegd bij een hoog restrisico
- Grondslag: art. 36 lid 1 AVG
- Toetspunt: Blijft er na maatregelen een hoog restrisico? Dan is voorafgaande raadpleging van de AP verplicht
- Alleen als: `facts.dpia_document_review == true`
- Bronnen: AVG-art36-lid1 (AVG art. 36 lid 1)
- Wat de tekst moet bereiken: Blijft er na je maatregelen een hoog risico over, raadpleeg dan de Autoriteit Persoonsgegevens voordat je met de verwerking begint.
