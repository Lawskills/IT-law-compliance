# Kader K5 — Informatieplicht en privacyverklaring

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een privacyverklaring alle informatie bevat die de AVG voorschrijft (art. 12, 13 en 14), of die informatie duidelijk en vindbaar is, en of de verklaring past bij wat de organisatie werkelijk doet.

Bronnen: AVG-art12 (AVG art. 12); AVG-art13 (AVG art. 13); AVG-art14 (AVG art. 14); AVG-art21-lid4 (AVG art. 21 lid 4); AVG-art26-lid2 (AVG art. 26 lid 2); AVG-art27 (AVG art. 27); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB); HvJEU-C-413-23P (HvJEU 4 september 2025, C-413/23 P, EDPS/Gemeenschappelijke Afwikkelingsraad (SRB))

## Formulier (vragen aan de gebruiker)

- **controller_name**: Wat is de officiële naam van je organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van je organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **controller_contact**: Op welk adres en e-mailadres kunnen mensen je bereiken over privacy?
  - Label (voor de plek-om-in-te-vullen): adres en e-mailadres van je organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **has_dpo**: Heb je een functionaris gegevensbescherming (FG)?
  - Label (voor de plek-om-in-te-vullen): of je een functionaris gegevensbescherming hebt
  - Hulp: Ook als je vrijwillig een FG hebt aangesteld. Een privacymedewerker zonder de officiële FG-rol telt niet mee.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **dpo_contact**: Wat zijn de contactgegevens van je FG?
  - Label (voor de plek-om-in-te-vullen): contactgegevens van je FG
  - Hulp: Een functioneel e-mailadres (bijvoorbeeld fg@uwbedrijf.nl) is voldoende. De naam hoeft niet.
  - Type: text · Alleen vragen als: `facts.has_dpo == true` · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **direct_collection**: Krijg je gegevens rechtstreeks van de mensen zelf?
  - Label (voor de plek-om-in-te-vullen): of je gegevens rechtstreeks bij mensen zelf verzamelt
  - Hulp: Bijvoorbeeld via een contactformulier, een account, een bestelling, een sollicitatie of camerabeelden.
  - Type: boolean
- **indirect_collection**: Krijg je ook gegevens over mensen via iemand anders?
  - Label (voor de plek-om-in-te-vullen): of je gegevens via anderen krijgt
  - Hulp: Bijvoorbeeld van een klant die gegevens van zijn eigen klanten aanlevert, van een partner, uit een openbare bron zoals LinkedIn of het KvK-register, of van een adresleverancier.
  - Type: boolean
- **uses_consent**: Vraag je voor een of meer doelen toestemming aan mensen?
  - Label (voor de plek-om-in-te-vullen): of je toestemming gebruikt
  - Hulp: Bijvoorbeeld een aanvinkvakje voor de nieuwsbrief of voor het delen van gegevens. Zo ja, dan moet in je verklaring staan dat mensen hun toestemming kunnen intrekken.
  - Type: boolean
- **uses_legitimate_interest**: Gebruik je gegevens omdat je daar zelf een goede reden voor hebt, zonder toestemming te vragen?
  - Label (voor de plek-om-in-te-vullen): of je je op gerechtvaardigd belang beroept
  - Hulp: Juristen noemen dit 'gerechtvaardigd belang'. Voorbeelden: fraude voorkomen, beveiliging, klanten informeren over vergelijkbare producten, zakelijke contactpersonen beheren.
  - Type: boolean
- **legitimate_interest_description**: Welk belang heb je, per doel? Beschrijf het in één zin per doel.
  - Label (voor de plek-om-in-te-vullen): welk belang je hebt
  - Type: text · Alleen vragen als: `facts.uses_legitimate_interest == true`
- **uses_public_task**: Voer je een taak van algemeen belang of openbaar gezag uit die in de wet is vastgelegd?
  - Label (voor de plek-om-in-te-vullen): of je een wettelijke publieke taak uitvoert
  - Hulp: Dit geldt vooral voor overheden en organisaties met een wettelijke publieke taak. Voor de meeste bedrijven is het antwoord nee.
  - Type: boolean
- **direct_marketing**: Stuur je mensen reclame of aanbiedingen, bijvoorbeeld per e-mail, post of telefoon?
  - Label (voor de plek-om-in-te-vullen): of je aan direct marketing doet
  - Type: boolean
- **transfers_outside_eea**: Worden gegevens opgeslagen of bekeken buiten de Europese Unie, Noorwegen, IJsland en Liechtenstein?
  - Label (voor de plek-om-in-te-vullen): of gegevens buiten de EU/EER terechtkomen
  - Hulp: Denk aan Amerikaanse diensten voor e-mail, nieuwsbrieven, CRM, cloudopslag of AI, en aan support vanuit een land buiten Europa.
  - Type: boolean
- **transfer_details**: Naar welke landen en via welke diensten gaan de gegevens, en op welke basis?
  - Label (voor de plek-om-in-te-vullen): landen en de waarborg per doorgifte
  - Hulp: Bijvoorbeeld: 'Verenigde Staten, Mailchimp, EU-VS Data Privacy Framework' of 'India, supportpartner, standaardcontractbepalingen'.
  - Type: text · Alleen vragen als: `facts.transfers_outside_eea == true`
- **automated_decision_making**: Neemt software of AI zelfstandig besluiten over mensen die voor hen belangrijke gevolgen hebben, zonder dat een medewerker het besluit inhoudelijk beoordeelt?
  - Label (voor de plek-om-in-te-vullen): of een computer zelfstandig belangrijke besluiten over mensen neemt
  - Hulp: Bijvoorbeeld een automatische afwijzing van een sollicitatie, een kredietaanvraag of een klant. Een aanbeveling die een medewerker echt beoordeelt, telt niet.
  - Type: boolean
- **adm_description**: Beschrijf kort wat het systeem besluit, op basis van welke gegevens, en wat de gevolgen voor iemand zijn.
  - Label (voor de plek-om-in-te-vullen): hoe het geautomatiseerde besluit werkt
  - Type: text · Alleen vragen als: `facts.automated_decision_making == true`
- **non_eu_controller**: Is je organisatie buiten de EU gevestigd, en bied je producten of diensten aan mensen in de EU aan of volg je hun gedrag (bijvoorbeeld via tracking of profilering)?
  - Label (voor de plek-om-in-te-vullen): of je organisatie buiten de EU gevestigd is
  - Hulp: Voor bijna alle Nederlandse organisaties is het antwoord nee.
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **eu_representative**: Wie is je vertegenwoordiger in de EU, en hoe is die bereikbaar?
  - Label (voor de plek-om-in-te-vullen): naam en contactgegevens van je vertegenwoordiger in de EU
  - Type: text · Alleen vragen als: `facts.non_eu_controller == true`
- **joint_controllership**: Bepaal je samen met een andere organisatie waarvoor en hoe bepaalde gegevens worden gebruikt?
  - Label (voor de plek-om-in-te-vullen): of je samen met een andere organisatie bepaalt wat er met de gegevens gebeurt
  - Hulp: Bijvoorbeeld een gezamenlijke actie met een partner, een gedeeld platform, of een Facebook-pagina van je bedrijf. Een leverancier die alleen in je opdracht werkt, telt niet.
  - Type: boolean
- **further_processing**: Gebruik je gegevens ook voor een ander doel dan waarvoor je ze oorspronkelijk kreeg?
  - Label (voor de plek-om-in-te-vullen): of je gegevens later voor een nieuw doel gebruikt
  - Hulp: Bijvoorbeeld klantgegevens die later voor een klanttevredenheidsonderzoek of voor het trainen van software worden gebruikt.
  - Type: boolean
- **further_processing_informed**: Heb je de mensen geïnformeerd over dat nieuwe doel voordat je ermee begon?
  - Label (voor de plek-om-in-te-vullen): of je mensen vooraf over het nieuwe doel hebt geïnformeerd
  - Type: boolean · Alleen vragen als: `facts.further_processing == true`
- **relies_on_info_exception**: Informeer je bepaalde mensen bewust niet over het gebruik van hun gegevens?
  - Label (voor de plek-om-in-te-vullen): of je vindt dat je (een deel van de) mensen niet hoeft te informeren
  - Hulp: Bijvoorbeeld omdat ze de informatie al hebben, omdat informeren onmogelijk is of onevenredig veel moeite kost, omdat het doel daardoor mislukt, of omdat een wet of beroepsgeheim het verbiedt. Deze uitzonderingen zijn smal; een juridisch adviseur beoordeelt of ze gelden.
  - Type: boolean
- **relies_on_info_exception_reason**: Welke mensen informeer je niet, waarom niet, en welke maatregelen neem je in plaats daarvan (bijvoorbeeld de informatie openbaar maken)?
  - Label (voor de plek-om-in-te-vullen): waarom je mensen niet informeert
  - Type: text · Alleen vragen als: `facts.relies_on_info_exception == true`
- **indirect_info_timing**: Wanneer informeer je mensen van wie je gegevens via iemand anders hebt gekregen?
  - Label (voor de plek-om-in-te-vullen): wanneer je mensen informeert van wie je gegevens via anderen krijgt
  - Hulp: De wet geeft je hooguit een maand. Benader je iemand eerder, of geef je de gegevens eerder aan een ander, dan moet je op dat moment al informeren.
  - Type: enum (within_one_month / later_or_never) · Alleen vragen als: `facts.indirect_collection == true`
- **info_available_at_collection**: Kunnen mensen de privacyverklaring zien op het moment dat ze hun gegevens aan jou geven?
  - Label (voor de plek-om-in-te-vullen): of de verklaring beschikbaar is op het moment dat je gegevens verzamelt
  - Hulp: Bijvoorbeeld een link bij het contactformulier, bij het aanmaken van een account, in de sollicitatieprocedure of op het camerabord.
  - Type: boolean · Alleen vragen als: `facts.direct_collection == true`
- **publication_location**: Waar staat de privacyverklaring?
  - Label (voor de plek-om-in-te-vullen): waar de verklaring te vinden is
  - Type: enum (website_every_page / website_hidden / on_request / not_published)
- **audience_includes_children**: Is je website of dienst (ook) bedoeld voor kinderen jonger dan 16?
  - Label (voor de plek-om-in-te-vullen): of je diensten (ook) op kinderen gericht zijn
  - Type: boolean
- **audience_language**: In welke taal communiceer je normaal met de mensen over wie de verklaring gaat?
  - Label (voor de plek-om-in-te-vullen): de taal van je doelgroep
  - Type: enum (nl / en / nl_en / other)
- **processing_summary**: Beschrijf in gewone woorden welke gegevens je gebruikt, waarvoor, en met welke partijen je ze deelt.
  - Label (voor de plek-om-in-te-vullen): welke gegevens je gebruikt, waarvoor en met wie je ze deelt
  - Hulp: Zoals je het aan een collega zou uitleggen.
  - Type: text
- **purposes_and_bases**: Voor welke doelen gebruik je gegevens, en op welke grondslag per doel?
  - Label (voor de plek-om-in-te-vullen): de doelen en de grondslag per doel
  - Type: text · Kan uit je verwerkingsregister komen
- **recipients**: Met welke partijen of soorten partijen deel je gegevens?
  - Label (voor de plek-om-in-te-vullen): de ontvangers of categorieën ontvangers
  - Type: text · Kan uit je verwerkingsregister komen
- **retention_periods**: Hoe lang bewaar je de gegevens, per doel of per soort gegevens?
  - Label (voor de plek-om-in-te-vullen): de bewaartermijn per doel of per soort gegevens
  - Type: text · Kan uit je verwerkingsregister komen
- **data_categories**: Welke soorten gegevens krijg je via anderen?
  - Label (voor de plek-om-in-te-vullen): de soorten gegevens die je via anderen krijgt
  - Type: text · Alleen vragen als: `facts.indirect_collection == true` · Kan uit je verwerkingsregister komen
- **data_sources**: Van wie of waar krijg je die gegevens?
  - Label (voor de plek-om-in-te-vullen): de bron van de gegevens die je via anderen krijgt
  - Type: text · Alleen vragen als: `facts.indirect_collection == true`
- **mandatory_data_consequences**: Welke gegevens moeten mensen verplicht geven (bijvoorbeeld om te kunnen bestellen), en wat gebeurt er als ze dat niet doen?
  - Label (voor de plek-om-in-te-vullen): welke gegevens verplicht zijn en wat er gebeurt als iemand ze niet geeft
  - Type: text · Alleen vragen als: `facts.direct_collection == true`
- **joint_arrangement_summary**: Wat heb je afgesproken met de andere organisatie over wie wat regelt (vooral: wie beantwoordt vragen en verzoeken van mensen)?
  - Label (voor de plek-om-in-te-vullen): de afspraken met de organisatie waarmee je samen verantwoordelijk bent
  - Type: text · Alleen vragen als: `facts.joint_controllership == true`
- **has_cookies**: Gebruikt je website cookies, pixels of andere trackers?
  - Label (voor de plek-om-in-te-vullen): of je website cookies of trackers gebruikt
  - Type: boolean

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `contact` (standaardkop: Wie zijn wij)

#### K5.1 — Wie je bent en hoe mensen je bereiken
- Grondslag: art. 13 lid 1 sub a en art. 14 lid 1 sub a AVG
- Toetspunt: Identiteit en contactgegevens van de verwerkingsverantwoordelijke
- Tekstsoort: `insert` · Nodig: controller_name, controller_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Wie zijn wij
Deze privacyverklaring is van {{facts.controller_name}}. Wij zijn verantwoordelijk voor de verwerking van je persoonsgegevens zoals beschreven in deze verklaring.
Je kunt ons bereiken via: {{facts.controller_contact}}.
````

#### K5.2 — Contactgegevens van je functionaris gegevensbescherming
- Grondslag: art. 13 lid 1 sub b en art. 14 lid 1 sub b AVG
- Toetspunt: Contactgegevens van de functionaris voor gegevensbescherming
- Tekstsoort: `insert` · Alleen opnemen als: `facts.has_dpo == true` · Nodig: dpo_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Wij hebben een functionaris gegevensbescherming (FG). Je kunt de FG bereiken via: {{facts.dpo_contact}}.
````

#### K5.19 — Wie je vertegenwoordiger in de EU is
- Grondslag: art. 13 lid 1 sub a en art. 14 lid 1 sub a jo. art. 27 AVG
- Toetspunt: Identiteit en contactgegevens van de vertegenwoordiger in de Unie
- Tekstsoort: `insert` · Alleen opnemen als: `facts.non_eu_controller == true` · Nodig: eu_representative

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Onze vertegenwoordiger in de Europese Unie is: {{facts.eu_representative}}.
````

### 2. Onderdeel `bron` (standaardkop: Van wie wij gegevens krijgen)

#### K5.13 — Welke soorten gegevens je via anderen krijgt
- Grondslag: art. 14 lid 1 sub d AVG
- Toetspunt: De betrokken categorieën van persoonsgegevens
- Tekstsoort: `insert` · Alleen opnemen als: `facts.indirect_collection == true` · Nodig: data_categories

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Wij krijgen ook gegevens over jou via anderen. Het gaat om de volgende soorten gegevens:
{{facts.data_categories}}
````

#### K5.14 — Van wie of waar je de gegevens krijgt
- Grondslag: art. 14 lid 2 sub f AVG
- Toetspunt: De bron van de persoonsgegevens, en in voorkomend geval of die uit openbare bronnen afkomstig zijn
- Tekstsoort: `insert` · Alleen opnemen als: `facts.indirect_collection == true` · Nodig: data_sources

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Deze gegevens krijgen wij van: {{facts.data_sources}}.
````

### 3. Onderdeel `doelen` (standaardkop: Waarvoor gebruiken wij je gegevens)

#### K5.3 — Waarvoor je gegevens gebruikt, en op welke grond
- Grondslag: art. 13 lid 1 sub c en art. 14 lid 1 sub c AVG
- Toetspunt: De verwerkingsdoeleinden en de rechtsgrond, gekoppeld per doel
- Tekstsoort: `append_section` · Nodig: purposes_and_bases

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Waarvoor gebruiken wij je gegevens, en op welke grond
| Doel | Grondslag |
|---|---|
{{facts.purposes_and_bases}}
````

#### K5.4 — Welk belang je hebt als je geen toestemming vraagt
- Grondslag: art. 13 lid 1 sub d en art. 14 lid 2 sub b AVG
- Toetspunt: Omschrijving van de gerechtvaardigde belangen van de verantwoordelijke of een derde
- Tekstsoort: `insert` · Alleen opnemen als: `facts.uses_legitimate_interest == true` · Nodig: legitimate_interest_description

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Voor sommige doelen gebruiken wij je gegevens omdat wij daar een gerechtvaardigd belang bij hebben. Het gaat om de volgende belangen:
{{facts.legitimate_interest_description}}
````

#### K5.11 — Welke gegevens verplicht zijn, en wat er gebeurt als iemand ze niet geeft
- Grondslag: art. 13 lid 2 sub e AVG
- Toetspunt: Of de verstrekking een wettelijke of contractuele verplichting is of noodzakelijk om een overeenkomst te sluiten, of de betrokkene verplicht is de gegevens te verstrekken, en de gevolgen als dat niet gebeurt
- Tekstsoort: `insert` · Alleen opnemen als: `facts.direct_collection == true` · Nodig: mandatory_data_consequences

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Sommige gegevens heb je nodig om met ons een overeenkomst te sluiten of die uit te voeren, of zijn wij wettelijk verplicht te vragen. Het gaat om:
{{facts.mandatory_data_consequences}}
````

### 4. Onderdeel `ontvangers` (standaardkop: Met wie delen wij je gegevens)

#### K5.5 — Met wie je gegevens deelt
- Grondslag: art. 13 lid 1 sub e en art. 14 lid 1 sub e AVG
- Toetspunt: De ontvangers of categorieën ontvangers van de persoonsgegevens
- Tekstsoort: `append_section` · Nodig: recipients

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Met wie delen wij je gegevens
Wij delen je gegevens alleen als dat nodig is voor de doelen in deze verklaring. Het gaat om:
{{facts.recipients}}
Partijen die in onze opdracht werken (verwerkers), mogen je gegevens niet voor eigen doelen gebruiken. Met hen hebben wij een verwerkersovereenkomst.
````

#### K5.6 — Of gegevens buiten Europa terechtkomen, en hoe ze daar beschermd zijn
- Grondslag: art. 13 lid 1 sub f en art. 14 lid 1 sub f AVG
- Toetspunt: Doorgifte naar een derde land, het bestaan of ontbreken van een adequaatheidsbesluit of de passende waarborgen, en hoe een kopie te verkrijgen
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.transfers_outside_eea == true` · Nodig: transfer_details, controller_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Gegevens buiten de Europese Economische Ruimte
Sommige gegevens worden doorgegeven aan partijen buiten de Europese Economische Ruimte (EER). Dit gebeurt alleen als er een passend beschermingsniveau is:
{{facts.transfer_details}}
Wil je een kopie van de waarborgen ontvangen? Neem dan contact met ons op via {{facts.controller_contact}}.
````

#### K5.24 — Wat je hebt afgesproken met de organisatie waarmee je samenwerkt
- Grondslag: art. 26 lid 2 AVG
- Toetspunt: De wezenlijke inhoud van de regeling tussen gezamenlijk verwerkingsverantwoordelijken
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.joint_controllership == true` · Nodig: joint_arrangement_summary

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Samenwerking met een andere organisatie
Voor een deel van de verwerkingen bepalen wij samen met een andere organisatie waarvoor en hoe je gegevens worden gebruikt. Wij hebben daarover het volgende afgesproken:
{{facts.joint_arrangement_summary}}
Je kunt je rechten bij elk van de betrokken organisaties uitoefenen.
````

### 5. Onderdeel `bewaren` (standaardkop: Hoe lang bewaren wij je gegevens)

#### K5.7 — Hoe lang je gegevens bewaart
- Grondslag: art. 13 lid 2 sub a en art. 14 lid 2 sub a AVG
- Toetspunt: De bewaartermijn, of de criteria om die termijn te bepalen
- Tekstsoort: `append_section` · Nodig: retention_periods

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Hoe lang bewaren wij je gegevens
Wij bewaren je gegevens niet langer dan nodig voor het doel waarvoor wij ze hebben gekregen, of zo lang de wet dat voorschrijft:
{{facts.retention_periods}}
````

### 6. Onderdeel `besluiten` (standaardkop: Automatische besluiten)

#### K5.12 — Of een computer zelfstandig belangrijke besluiten neemt, en hoe dat werkt
- Grondslag: art. 13 lid 2 sub f en art. 14 lid 2 sub g AVG
- Toetspunt: Het bestaan van geautomatiseerde besluitvorming (art. 22 lid 1 en 4), met nuttige informatie over de onderliggende logica, het belang en de verwachte gevolgen
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.automated_decision_making == true` · Nodig: adm_description, controller_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Automatische besluiten
Wij nemen sommige besluiten automatisch, zonder dat een medewerker het besluit inhoudelijk beoordeelt:
{{facts.adm_description}}
Je hebt het recht om een medewerker het besluit te laten beoordelen, je standpunt kenbaar te maken en het besluit aan te vechten. Neem daarvoor contact op via {{facts.controller_contact}}.
````

### 7. Onderdeel `rechten` (standaardkop: Je rechten)

#### K5.8 — Welke rechten mensen hebben
- Grondslag: art. 13 lid 2 sub b en art. 14 lid 2 sub c AVG
- Toetspunt: Het recht op inzage, rectificatie, wissing, beperking, bezwaar en overdraagbaarheid
- Tekstsoort: `append_section` · Nodig: controller_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Jouw rechten
Je hebt de volgende rechten:
- **Inzage:** je mag weten welke gegevens wij van jou hebben en een kopie ontvangen.
- **Correctie:** je mag onjuiste gegevens laten verbeteren of aanvullen.
- **Verwijdering:** je mag vragen je gegevens te wissen.
- **Beperking:** je mag vragen het gebruik van je gegevens tijdelijk te beperken.
- **Bezwaar:** je mag bezwaar maken tegen het gebruik van je gegevens.
- **Overdraagbaarheid:** je mag gegevens die je zelf aan ons hebt gegeven, in een gangbaar formaat ontvangen of laten overdragen aan een ander, als wij ze gebruiken op basis van je toestemming of een overeenkomst.
Je kunt een verzoek sturen naar {{facts.controller_contact}}. Wij reageren binnen een maand. Dit is gratis.
````

#### K5.9 — Dat mensen hun toestemming kunnen intrekken
- Grondslag: art. 13 lid 2 sub c en art. 14 lid 2 sub d AVG; art. 7 lid 3 AVG
- Toetspunt: Het recht om de toestemming te allen tijde in te trekken, zonder dat dit de rechtmatigheid van de verwerking daarvoor aantast
- Tekstsoort: `insert` · Alleen opnemen als: `facts.uses_consent == true` · Nodig: controller_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Heb je toestemming gegeven? Dan kun je die altijd weer intrekken, net zo makkelijk als je haar gaf, bijvoorbeeld via {{facts.controller_contact}} of de afmeldlink in onze berichten. Het intrekken geldt voor de toekomst; het gebruik van je gegevens daarvoor blijft rechtmatig.
````

#### K5.10 — Dat mensen een klacht kunnen indienen bij de Autoriteit Persoonsgegevens
- Grondslag: art. 13 lid 2 sub d en art. 14 lid 2 sub e AVG; art. 77 AVG
- Toetspunt: Het recht om een klacht in te dienen bij een toezichthoudende autoriteit
- Tekstsoort: `insert`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Ben je het niet eens met hoe wij met je gegevens omgaan? Neem dan eerst contact met ons op. Je hebt ook het recht een klacht in te dienen bij de Autoriteit Persoonsgegevens (www.autoriteitpersoonsgegevens.nl).
````

#### K5.20 — Dat mensen bezwaar kunnen maken, duidelijk en apart vermeld
- Grondslag: art. 21 lid 2, 3 en 4 AVG
- Toetspunt: Het recht van bezwaar uitdrukkelijk onder de aandacht gebracht, duidelijk en gescheiden van andere informatie; bij direct marketing: bezwaar wordt altijd gehonoreerd
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.uses_legitimate_interest == true or facts.uses_public_task == true or facts.direct_marketing == true` · Nodig: controller_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Jouw recht om bezwaar te maken
Gebruiken wij je gegevens op basis van ons gerechtvaardigd belang? Dan kun je daartegen altijd bezwaar maken, vanwege je specifieke situatie. Wij stoppen dan, tenzij wij dwingende redenen hebben die zwaarder wegen dan jouw belangen.
Gebruiken wij je gegevens voor direct marketing? Dan kun je altijd bezwaar maken. Wij stoppen dan direct met het gebruik voor dat doel.
Je maakt bezwaar via {{facts.controller_contact}} of via de afmeldlink in onze berichten.
````

## Toetspunten (voor de eindcontrole)

### K5.1 — Wie je bent en hoe mensen je bereiken
- Grondslag: art. 13 lid 1 sub a en art. 14 lid 1 sub a AVG
- Toetspunt: Identiteit en contactgegevens van de verwerkingsverantwoordelijke
- Bronnen: AVG-art13-lid1-a (AVG art. 13 lid 1 sub a); AVG-art14-lid1-a (AVG art. 14 lid 1 sub a); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Vermeld de officiële naam van je organisatie en ten minste een adres en een e-mailadres voor privacyvragen.

### K5.2 — Contactgegevens van je functionaris gegevensbescherming
- Grondslag: art. 13 lid 1 sub b en art. 14 lid 1 sub b AVG
- Toetspunt: Contactgegevens van de functionaris voor gegevensbescherming
- Alleen als: `facts.has_dpo == true`
- Bronnen: AVG-art13-lid1-b (AVG art. 13 lid 1 sub b); AVG-art14-lid1-b (AVG art. 14 lid 1 sub b)
- Wat de tekst moet bereiken: Vermeld hoe mensen je functionaris gegevensbescherming kunnen bereiken, bijvoorbeeld via een apart e-mailadres.

### K5.3 — Waarvoor je gegevens gebruikt, en op welke grond
- Grondslag: art. 13 lid 1 sub c en art. 14 lid 1 sub c AVG
- Toetspunt: De verwerkingsdoeleinden en de rechtsgrond, gekoppeld per doel
- Bronnen: AVG-art13-lid1-c (AVG art. 13 lid 1 sub c); AVG-art14-lid1-c (AVG art. 14 lid 1 sub c); AVG-art6-lid1 (AVG art. 6 lid 1); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Maak per doel duidelijk op welke grondslag je de gegevens gebruikt, bijvoorbeeld in een tabel met de kolommen doel, gegevens en grondslag.

### K5.4 — Welk belang je hebt als je geen toestemming vraagt
- Grondslag: art. 13 lid 1 sub d en art. 14 lid 2 sub b AVG
- Toetspunt: Omschrijving van de gerechtvaardigde belangen van de verantwoordelijke of een derde
- Alleen als: `facts.uses_legitimate_interest == true`
- Bronnen: AVG-art13-lid1-d (AVG art. 13 lid 1 sub d); AVG-art14-lid2-b (AVG art. 14 lid 2 sub b); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Beschrijf per doel welk belang je hebt, in gewone woorden.

### K5.5 — Met wie je gegevens deelt
- Grondslag: art. 13 lid 1 sub e en art. 14 lid 1 sub e AVG
- Toetspunt: De ontvangers of categorieën ontvangers van de persoonsgegevens
- Bronnen: AVG-art13-lid1-e (AVG art. 13 lid 1 sub e); AVG-art14-lid1-e (AVG art. 14 lid 1 sub e); AVG-art4-9 (AVG art. 4 punt 9); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB); HvJEU-C-413-23P (HvJEU 4 september 2025, C-413/23 P, EDPS/Gemeenschappelijke Afwikkelingsraad (SRB))
- Wat de tekst moet bereiken: Noem met welke partijen of soorten partijen je gegevens deelt, ook dienstverleners die in je opdracht werken (zoals hosting, e-mail en boekhouding).

### K5.6 — Of gegevens buiten Europa terechtkomen, en hoe ze daar beschermd zijn
- Grondslag: art. 13 lid 1 sub f en art. 14 lid 1 sub f AVG
- Toetspunt: Doorgifte naar een derde land, het bestaan of ontbreken van een adequaatheidsbesluit of de passende waarborgen, en hoe een kopie te verkrijgen
- Alleen als: `facts.transfers_outside_eea == true`
- Bronnen: AVG-art13-lid1-f (AVG art. 13 lid 1 sub f); AVG-art14-lid1-f (AVG art. 14 lid 1 sub f); AVG-art45 (AVG art. 45); AVG-art46 (AVG art. 46); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Vermeld naar welke landen gegevens gaan, op welke basis (bijvoorbeeld het EU-VS Data Privacy Framework of standaardcontractbepalingen), en hoe iemand een kopie van die waarborgen kan opvragen.

### K5.7 — Hoe lang je gegevens bewaart
- Grondslag: art. 13 lid 2 sub a en art. 14 lid 2 sub a AVG
- Toetspunt: De bewaartermijn, of de criteria om die termijn te bepalen
- Bronnen: AVG-art13-lid2-a (AVG art. 13 lid 2 sub a); AVG-art14-lid2-a (AVG art. 14 lid 2 sub a); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Vermeld per doel of per soort gegevens hoe lang je ze bewaart, of welk concreet criterium je gebruikt.

### K5.8 — Welke rechten mensen hebben
- Grondslag: art. 13 lid 2 sub b en art. 14 lid 2 sub c AVG
- Toetspunt: Het recht op inzage, rectificatie, wissing, beperking, bezwaar en overdraagbaarheid
- Bronnen: AVG-art13-lid2-b (AVG art. 13 lid 2 sub b); AVG-art14-lid2-c (AVG art. 14 lid 2 sub c); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Noem alle rechten die mensen hebben (inzage, correctie, verwijdering, beperking, bezwaar en overdraagbaarheid) en hoe ze die kunnen gebruiken.

### K5.9 — Dat mensen hun toestemming kunnen intrekken
- Grondslag: art. 13 lid 2 sub c en art. 14 lid 2 sub d AVG; art. 7 lid 3 AVG
- Toetspunt: Het recht om de toestemming te allen tijde in te trekken, zonder dat dit de rechtmatigheid van de verwerking daarvoor aantast
- Alleen als: `facts.uses_consent == true`
- Bronnen: AVG-art13-lid2-c (AVG art. 13 lid 2 sub c); AVG-art14-lid2-d (AVG art. 14 lid 2 sub d); AVG-art7-lid3 (AVG art. 7 lid 3)
- Wat de tekst moet bereiken: Vermeld dat mensen hun toestemming altijd kunnen intrekken, en hoe.

### K5.10 — Dat mensen een klacht kunnen indienen bij de Autoriteit Persoonsgegevens
- Grondslag: art. 13 lid 2 sub d en art. 14 lid 2 sub e AVG; art. 77 AVG
- Toetspunt: Het recht om een klacht in te dienen bij een toezichthoudende autoriteit
- Bronnen: AVG-art13-lid2-d (AVG art. 13 lid 2 sub d); AVG-art14-lid2-e (AVG art. 14 lid 2 sub e); AVG-art77 (AVG art. 77)
- Wat de tekst moet bereiken: Vermeld dat mensen een klacht kunnen indienen bij de Autoriteit Persoonsgegevens.

### K5.11 — Welke gegevens verplicht zijn, en wat er gebeurt als iemand ze niet geeft
- Grondslag: art. 13 lid 2 sub e AVG
- Toetspunt: Of de verstrekking een wettelijke of contractuele verplichting is of noodzakelijk om een overeenkomst te sluiten, of de betrokkene verplicht is de gegevens te verstrekken, en de gevolgen als dat niet gebeurt
- Alleen als: `facts.direct_collection == true`
- Bronnen: AVG-art13-lid2-e (AVG art. 13 lid 2 sub e); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Vermeld welke gegevens mensen verplicht moeten geven, en wat er gebeurt als ze dat niet doen.

### K5.12 — Of een computer zelfstandig belangrijke besluiten neemt, en hoe dat werkt
- Grondslag: art. 13 lid 2 sub f en art. 14 lid 2 sub g AVG
- Toetspunt: Het bestaan van geautomatiseerde besluitvorming (art. 22 lid 1 en 4), met nuttige informatie over de onderliggende logica, het belang en de verwachte gevolgen
- Alleen als: `facts.automated_decision_making == true`
- Bronnen: AVG-art13-lid2-f (AVG art. 13 lid 2 sub f); AVG-art14-lid2-g (AVG art. 14 lid 2 sub g); AVG-art22 (AVG art. 22); WP251-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake geautomatiseerde individuele besluitvorming en profilering (WP251 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Vermeld dat je volledig geautomatiseerde besluiten neemt, leg in gewone woorden uit op basis waarvan, en wat de gevolgen voor iemand kunnen zijn.

### K5.13 — Welke soorten gegevens je via anderen krijgt
- Grondslag: art. 14 lid 1 sub d AVG
- Toetspunt: De betrokken categorieën van persoonsgegevens
- Alleen als: `facts.indirect_collection == true`
- Bronnen: AVG-art14-lid1-d (AVG art. 14 lid 1 sub d)
- Wat de tekst moet bereiken: Vermeld welke soorten gegevens je via anderen krijgt.

### K5.14 — Van wie of waar je de gegevens krijgt
- Grondslag: art. 14 lid 2 sub f AVG
- Toetspunt: De bron van de persoonsgegevens, en in voorkomend geval of die uit openbare bronnen afkomstig zijn
- Alleen als: `facts.indirect_collection == true`
- Bronnen: AVG-art14-lid2-f (AVG art. 14 lid 2 sub f); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Vermeld van wie of waar je de gegevens krijgt, en of het een openbare bron is.

### K5.15 — Of je mensen op tijd informeert als je hun gegevens via anderen krijgt
- Grondslag: art. 14 lid 3 AVG
- Toetspunt: Informatie binnen een redelijke termijn en uiterlijk binnen een maand na verkrijging, of uiterlijk bij het eerste contact of bij de eerste verstrekking aan een ander
- Alleen als: `facts.indirect_collection == true and facts.relies_on_info_exception != true`
- Bronnen: AVG-art14-lid3 (AVG art. 14 lid 3)
- Wat de tekst moet bereiken: Informeer mensen van wie je gegevens via anderen krijgt uiterlijk binnen een maand, of eerder als je hen eerder benadert of de gegevens aan een ander geeft. Een verwijzing naar de privacyverklaring in je eerste bericht is daarvoor een gangbare manier.

### K5.16 — Of de verklaring duidelijk en begrijpelijk is
- Grondslag: art. 12 lid 1 AVG
- Toetspunt: Beknopt, transparant, begrijpelijk en in duidelijke en eenvoudige taal, in het bijzonder bij informatie voor kinderen
- Bronnen: AVG-art12-lid1 (AVG art. 12 lid 1); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Herschrijf de verklaring in korte zinnen en gewone woorden, in de taal van je doelgroep, met duidelijke kopjes.

### K5.17 — Of mensen de verklaring makkelijk kunnen vinden
- Grondslag: art. 12 lid 1 AVG
- Toetspunt: Gemakkelijk toegankelijk, ook op het moment van verzamelen
- Bronnen: AVG-art12-lid1 (AVG art. 12 lid 1); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Zet een link naar de privacyverklaring op elke pagina van je website (bijvoorbeeld in de voettekst) en bij elk formulier.

### K5.18 — Of de verklaring klopt met wat je werkelijk doet
- Grondslag: art. 5 lid 1 sub a, art. 12 lid 1 en art. 13/14 AVG
- Toetspunt: De verklaring komt overeen met de feitelijke verwerkingen
- Bronnen: AVG-art5-lid1-a (AVG art. 5 lid 1 sub a); AVG-art12-lid1 (AVG art. 12 lid 1); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Pas de verklaring aan zodat die beschrijft wat je werkelijk doet: alle doelen, ontvangers en doorgiften, en niets wat je niet doet.

### K5.19 — Wie je vertegenwoordiger in de EU is
- Grondslag: art. 13 lid 1 sub a en art. 14 lid 1 sub a jo. art. 27 AVG
- Toetspunt: Identiteit en contactgegevens van de vertegenwoordiger in de Unie
- Alleen als: `facts.non_eu_controller == true`
- Bronnen: AVG-art13-lid1-a (AVG art. 13 lid 1 sub a); AVG-art27 (AVG art. 27)
- Wat de tekst moet bereiken: Vermeld de naam en contactgegevens van je vertegenwoordiger in de EU.

### K5.20 — Dat mensen bezwaar kunnen maken, duidelijk en apart vermeld
- Grondslag: art. 21 lid 2, 3 en 4 AVG
- Toetspunt: Het recht van bezwaar uitdrukkelijk onder de aandacht gebracht, duidelijk en gescheiden van andere informatie; bij direct marketing: bezwaar wordt altijd gehonoreerd
- Alleen als: `facts.uses_legitimate_interest == true or facts.uses_public_task == true or facts.direct_marketing == true`
- Bronnen: AVG-art21-lid2 (AVG art. 21 lid 2); AVG-art21-lid3 (AVG art. 21 lid 3); AVG-art21-lid4 (AVG art. 21 lid 4); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Geef het recht op bezwaar een eigen kopje. Vermeld bij direct marketing dat je altijd stopt als iemand bezwaar maakt.

### K5.21 — Of je mensen vooraf informeert als je hun gegevens voor iets nieuws gebruikt
- Grondslag: art. 13 lid 3 en art. 14 lid 4 AVG
- Toetspunt: Informatie over het andere doel en alle relevante verdere informatie vóór de verdere verwerking
- Alleen als: `facts.further_processing == true`
- Bronnen: AVG-art13-lid3 (AVG art. 13 lid 3); AVG-art14-lid4 (AVG art. 14 lid 4)
- Wat de tekst moet bereiken: Informeer mensen voordat je hun gegevens voor een nieuw doel gebruikt. Controleer ook of het nieuwe doel verenigbaar is met het oorspronkelijke doel of een eigen grondslag heeft.

### K5.22 — Of je terecht bepaalde mensen niet informeert
- Grondslag: art. 13 lid 4 en art. 14 lid 5 AVG
- Toetspunt: Beroep op een uitzondering op de informatieplicht: betrokkene beschikt al over de informatie (art. 13 lid 4 / 14 lid 5 sub a); informeren onmogelijk, onevenredige inspanning, of doel onmogelijk of ernstig in gevaar (14 lid 5 sub b); wettelijke regeling (sub c); beroepsgeheim (sub d)
- Alleen als: `facts.relies_on_info_exception == true`
- Bronnen: AVG-art13-lid4 (AVG art. 13 lid 4); AVG-art14-lid5 (AVG art. 14 lid 5); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Leg vast waarom je mensen niet informeert en welke maatregelen je in plaats daarvan neemt; laat dit beoordelen door een juridisch adviseur.

### K5.23 — Of mensen de verklaring zien op het moment dat ze gegevens geven
- Grondslag: art. 13 lid 1 (aanhef) AVG
- Toetspunt: Informatie verstrekt op het moment waarop de persoonsgegevens worden verkregen
- Alleen als: `facts.direct_collection == true and facts.relies_on_info_exception != true`
- Bronnen: AVG-art13-lid1 (AVG art. 13 lid 1); WP260-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake transparantie onder Verordening (EU) 2016/679 (WP260 rev.01), bekrachtigd door de EDPB)
- Wat de tekst moet bereiken: Zet een link naar de privacyverklaring bij elk punt waar je gegevens verzamelt, zoals formulieren, het aanmaken van een account en je vacatures.

### K5.24 — Wat je hebt afgesproken met de organisatie waarmee je samenwerkt
- Grondslag: art. 26 lid 2 AVG
- Toetspunt: De wezenlijke inhoud van de regeling tussen gezamenlijk verwerkingsverantwoordelijken
- Alleen als: `facts.joint_controllership == true`
- Bronnen: AVG-art26-lid2 (AVG art. 26 lid 2); AVG-art26-lid3 (AVG art. 26 lid 3)
- Wat de tekst moet bereiken: Vermeld met welke organisatie je samen verantwoordelijk bent, waarvoor, en bij wie mensen terechtkunnen met vragen en verzoeken.
