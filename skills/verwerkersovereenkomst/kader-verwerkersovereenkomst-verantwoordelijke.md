# Kader K7 — Verwerkersovereenkomst (toets vanuit de verantwoordelijke)

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een verwerkersovereenkomst die de klant als verwerkingsverantwoordelijke sluit met een leverancier alle bepalingen bevat die art. 28 AVG voorschrijft, en signaleren waar aanvullende afspraken ontbreken of de verplichtingen uithollen.

Bronnen: AVG-art28 (AVG art. 28); AVG-art28-lid1 (AVG art. 28 lid 1); AVG-art28-lid3 (AVG art. 28 lid 3); AVG-art28-lid9 (AVG art. 28 lid 9); AVG-art33-lid2 (AVG art. 33 lid 2); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG); UB-2021-915 (Uitvoeringsbesluit (EU) 2021/915 van de Commissie betreffende standaardcontractbepalingen tussen verwerkingsverantwoordelijken en verwerkers als bedoeld in artikel 28, lid 7, van Verordening (EU) 2016/679 en artikel 29, lid 7, van Verordening (EU) 2018/1725)

## Formulier (vragen aan de gebruiker)

- **controller_name**: Wat is de officiële naam van je organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van je organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **processor_name**: Wat is de naam van de dienstverlener met wie je de overeenkomst sluit?
  - Label (voor de plek-om-in-te-vullen): naam van de dienstverlener
  - Type: text
- **processing_subject**: Voor welke dienst worden de gegevens verwerkt?
  - Label (voor de plek-om-in-te-vullen): het onderwerp van de verwerking
  - Hulp: Bijvoorbeeld 'de planningssoftware voor onze monteurs' of 'de salarisadministratie'.
  - Type: text
- **processing_duration**: Hoe lang duurt de verwerking?
  - Label (voor de plek-om-in-te-vullen): de duur van de verwerking
  - Hulp: Meestal: zolang de hoofdovereenkomst loopt. Noem de looptijd of het moment waarop de verwerking eindigt.
  - Type: text
- **processing_nature_purpose**: Wat doet de dienstverlener met de gegevens, en waarvoor?
  - Label (voor de plek-om-in-te-vullen): de aard en het doel van de verwerking
  - Hulp: Bijvoorbeeld 'opslaan en tonen van klantadressen zodat monteurs hun afspraken kunnen plannen'.
  - Type: text
- **personal_data_categories**: Welke soorten gegevens gaan naar de dienstverlener?
  - Label (voor de plek-om-in-te-vullen): de soorten persoonsgegevens
  - Hulp: Bijvoorbeeld naam, adres, telefoonnummer, e-mailadres, BSN of gezondheidsgegevens.
  - Type: text
- **data_subject_categories**: Over welke groepen mensen gaan die gegevens?
  - Label (voor de plek-om-in-te-vullen): de categorieën betrokkenen
  - Hulp: Bijvoorbeeld klanten, medewerkers, sollicitanten of patiënten.
  - Type: text
- **security_measures**: Welke beveiligingsmaatregelen neemt de dienstverlener, of in welk document staan ze?
  - Label (voor de plek-om-in-te-vullen): de beveiligingsmaatregelen van de verwerker
  - Hulp: Bijvoorbeeld 'versleuteling, tweefactorauthenticatie, dagelijkse back-ups, zie bijlage 2' of een verwijzing naar een beveiligingsdocument.
  - Type: text
- **approved_subprocessors**: Welke andere partijen schakelt de dienstverlener in (bijvoorbeeld hosting of e-mail), en waarvoor?
  - Label (voor de plek-om-in-te-vullen): de subverwerkers waarvoor toestemming wordt gegeven
  - Hulp: Noem per partij de naam, de dienst en het land waar de gegevens staan.
  - Type: text
- **subprocessor_notice_period**: Hoe lang van tevoren moet een nieuwe of vervangende subverwerker worden gemeld?
  - Label (voor de plek-om-in-te-vullen): de termijn voor het melden van een nieuwe subverwerker
  - Hulp: De wet schrijft geen termijn voor; kies een termijn die lang genoeg is om bezwaar te kunnen maken, bijvoorbeeld een aantal weken.
  - Type: text
- **storage_locations**: In welke landen slaat de dienstverlener de gegevens op, en vanuit welke landen kan hij (of een partij die hij inschakelt) erbij?
  - Label (voor de plek-om-in-te-vullen): waar de gegevens worden opgeslagen en vanwaar ze toegankelijk zijn
  - Hulp: Denk ook aan support of beheer vanuit een ander land. Staat dit in de documentatie van de dienstverlener, dan kun je het daaruit overnemen.
  - Type: text
- **transfers_outside_eea**: Worden de gegevens opgeslagen of bekeken buiten de Europese Unie, Noorwegen, IJsland en Liechtenstein?
  - Label (voor de plek-om-in-te-vullen): of gegevens buiten de EU/EER terechtkomen
  - Hulp: Denk aan Amerikaanse clouddiensten, en aan support of beheer vanuit een land buiten Europa.
  - Type: boolean
- **processor_guarantees_checked**: Heb je, voordat je met de dienstverlener in zee ging, nagegaan of die de gegevens goed kan beschermen?
  - Label (voor de plek-om-in-te-vullen): of je hebt nagegaan of de dienstverlener de gegevens goed kan beschermen
  - Hulp: Bijvoorbeeld door te kijken naar certificeringen (zoals ISO 27001), een beveiligingsdocument of auditrapport, of naar ervaringen van anderen.
  - Type: boolean
- **processor_guarantees_description**: Hoe heb je dat nagegaan, en wat bleek daaruit?
  - Label (voor de plek-om-in-te-vullen): hoe je dat hebt nagegaan
  - Type: text · Alleen vragen als: `facts.processor_guarantees_checked == true`

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `onderwerp` (standaardkop: Onderwerp van de verwerking)

#### K7.2 — Waarover de overeenkomst gaat: onderwerp, duur, doel, gegevens en betrokkenen
- Grondslag: art. 28 lid 3 (aanhef) AVG
- Toetspunt: Onderwerp en duur van de verwerking, aard en doel, soort persoonsgegevens, categorieën betrokkenen, en de rechten en verplichtingen van de verwerkingsverantwoordelijke
- Tekstsoort: `append_section` · Nodig: processing_subject, processing_duration, processing_nature_purpose, personal_data_categories, data_subject_categories

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Onderwerp, duur, aard en doel van de verwerking
1. Verwerker verwerkt persoonsgegevens in opdracht van Verwerkingsverantwoordelijke in het kader van: {{facts.processing_subject}}.
2. De verwerking duurt: {{facts.processing_duration}}.
3. Aard en doel van de verwerking: {{facts.processing_nature_purpose}}.
4. Soorten persoonsgegevens: {{facts.personal_data_categories}}.
5. Categorieën betrokkenen: {{facts.data_subject_categories}}.
6. Verwerkingsverantwoordelijke bepaalt het doel van en de middelen voor de verwerking. Verwerkingsverantwoordelijke heeft de rechten en verplichtingen die in deze overeenkomst en in de AVG aan hem zijn toegekend, waaronder het recht om Verwerker instructies te geven en om de naleving van deze overeenkomst te controleren.
````

### 2. Onderdeel `instructies` (standaardkop: Verwerking op instructie)

#### K7.3 — Of de verwerker alleen op instructie werkt
- Grondslag: art. 28 lid 3 sub a AVG
- Toetspunt: De verwerker verwerkt alleen op basis van schriftelijke instructies van de verwerkingsverantwoordelijke, ook bij doorgifte naar een derde land of internationale organisatie, tenzij een Unierechtelijke of lidstatelijke verplichting geldt; in dat geval meldt de verwerker dat vooraf, tenzij die wetgeving dat om gewichtige redenen van algemeen belang verbiedt
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Verwerking op instructie
1. Verwerker verwerkt de persoonsgegevens uitsluitend op basis van schriftelijke instructies van Verwerkingsverantwoordelijke, mede met betrekking tot doorgiften van persoonsgegevens aan een derde land of een internationale organisatie.
2. Is Verwerker op grond van een op hem van toepassing zijnde bepaling van Unierecht of lidstatelijk recht tot een verwerking verplicht, dan stelt Verwerker Verwerkingsverantwoordelijke voorafgaand aan die verwerking in kennis van dat wettelijke voorschrift, tenzij die wetgeving deze kennisgeving om gewichtige redenen van algemeen belang verbiedt.
````

#### K7.14 — Of de verwerker waarschuwt bij een instructie die in strijd is met de wet
- Grondslag: art. 28 lid 3, laatste alinea, AVG
- Toetspunt: De verwerker stelt de verwerkingsverantwoordelijke onmiddellijk in kennis als een instructie naar zijn mening inbreuk oplevert op de AVG of op andere Unierechtelijke of lidstatelijke bepalingen inzake gegevensbescherming
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Instructie in strijd met de wet
Verwerker stelt Verwerkingsverantwoordelijke onmiddellijk in kennis indien een instructie naar zijn mening inbreuk oplevert op de AVG of op andere Unierechtelijke of lidstatelijke bepalingen inzake gegevensbescherming.
````

### 3. Onderdeel `geheimhouding` (standaardkop: Geheimhouding)

#### K7.4 — Of de medewerkers van de verwerker tot geheimhouding verplicht zijn
- Grondslag: art. 28 lid 3 sub b AVG
- Toetspunt: Waarborg dat de tot verwerking gemachtigde personen zich tot vertrouwelijkheid hebben verbonden of door een passende wettelijke verplichting tot vertrouwelijkheid gebonden zijn
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Geheimhouding
Verwerker waarborgt dat de personen die gemachtigd zijn de persoonsgegevens te verwerken, zich ertoe hebben verbonden vertrouwelijkheid in acht te nemen of door een passende wettelijke verplichting tot vertrouwelijkheid zijn gebonden.
````

### 4. Onderdeel `beveiliging` (standaardkop: Beveiliging)

#### K7.5 — Of de verwerker de gegevens goed beveiligt
- Grondslag: art. 28 lid 3 sub c jo. art. 32 AVG
- Toetspunt: De verwerker neemt alle maatregelen die op grond van art. 32 AVG vereist zijn
- Tekstsoort: `append_section` · Nodig: security_measures

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Beveiliging
1. Verwerker neemt alle maatregelen die op grond van artikel 32 AVG vereist zijn. Rekening houdend met de stand van de techniek, de uitvoeringskosten, de aard, de omvang, de context en de verwerkingsdoeleinden en de risico's voor de rechten en vrijheden van personen, treft Verwerker passende technische en organisatorische maatregelen om een op het risico afgestemd beveiligingsniveau te waarborgen.
2. De maatregelen zijn beschreven in: {{facts.security_measures}}.
````

### 5. Onderdeel `subverwerkers` (standaardkop: Subverwerkers)

#### K7.6 — Onder welke voorwaarden de verwerker andere partijen mag inschakelen
- Grondslag: art. 28 lid 3 sub d jo. lid 2 en lid 4 AVG
- Toetspunt: Voorafgaande specifieke of algemene schriftelijke toestemming voor subverwerkers; bij algemene toestemming melding van beoogde wijzigingen met de mogelijkheid bezwaar te maken; dezelfde verplichtingen aan de subverwerker opleggen; de verwerker blijft volledig aansprakelijk
- Tekstsoort: `append_section` · Nodig: approved_subprocessors, subprocessor_notice_period

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Inschakeling van subverwerkers
1. Verwerker schakelt geen andere verwerker (subverwerker) in zonder voorafgaande schriftelijke toestemming van Verwerkingsverantwoordelijke. Verwerkingsverantwoordelijke geeft hierbij algemene schriftelijke toestemming voor de inschakeling van de volgende subverwerkers: {{facts.approved_subprocessors}}.
2. Verwerker informeert Verwerkingsverantwoordelijke ten minste {{facts.subprocessor_notice_period}} voorafgaand aan een beoogde toevoeging of vervanging van een subverwerker. Verwerkingsverantwoordelijke kan binnen die termijn bezwaar maken tegen de wijziging.
3. Verwerker legt aan iedere subverwerker bij overeenkomst of andere rechtshandeling dezelfde verplichtingen inzake gegevensbescherming op als die in deze overeenkomst zijn opgenomen, met name de verplichting afdoende garanties te bieden met betrekking tot het toepassen van passende technische en organisatorische maatregelen, zodat de verwerking aan de AVG voldoet.
4. Komt een subverwerker zijn verplichtingen inzake gegevensbescherming niet na, dan blijft Verwerker ten aanzien van Verwerkingsverantwoordelijke volledig aansprakelijk voor het nakomen van de verplichtingen van die subverwerker.
````

### 6. Onderdeel `bijstand` (standaardkop: Bijstand)

#### K7.7 — Of de verwerker helpt bij verzoeken van mensen over hun gegevens
- Grondslag: art. 28 lid 3 sub e AVG
- Toetspunt: Bijstand door passende technische en organisatorische maatregelen bij het vervullen van de plicht om verzoeken van betrokkenen te beantwoorden (hoofdstuk III AVG)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Bijstand bij verzoeken van betrokkenen
Rekening houdend met de aard van de verwerking verleent Verwerker Verwerkingsverantwoordelijke door middel van passende technische en organisatorische maatregelen, voor zover mogelijk, bijstand bij het vervullen van diens plicht om verzoeken van betrokkenen om uitoefening van hun rechten uit hoofdstuk III van de AVG te beantwoorden.
````

#### K7.8 — Of de verwerker helpt bij beveiliging, datalekken en risicobeoordelingen
- Grondslag: art. 28 lid 3 sub f jo. art. 32-36 AVG
- Toetspunt: Bijstand bij het nakomen van de verplichtingen uit art. 32 tot en met 36 AVG (beveiliging, melding en communicatie van datalekken, DPIA, voorafgaande raadpleging), rekening houdend met de aard van de verwerking en de informatie waarover de verwerker beschikt
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Bijstand bij beveiliging, datalekken en DPIA
1. Rekening houdend met de aard van de verwerking en de hem ter beschikking staande informatie verleent Verwerker Verwerkingsverantwoordelijke bijstand bij het doen nakomen van de verplichtingen uit de artikelen 32 tot en met 36 AVG: de beveiliging van de verwerking, de melding van een inbreuk in verband met persoonsgegevens aan de toezichthoudende autoriteit en de mededeling daarvan aan de betrokkene, de gegevensbeschermingseffectbeoordeling en de voorafgaande raadpleging van de toezichthoudende autoriteit.
2. Verwerker informeert Verwerkingsverantwoordelijke zonder onredelijke vertraging zodra hij kennis heeft genomen van een inbreuk in verband met persoonsgegevens.
````

### 7. Onderdeel `locatie` (standaardkop: Locatie van de verwerking)

#### K7.12 — Waar de gegevens staan en vanwaar ze toegankelijk zijn
- Grondslag: art. 28 lid 3 sub a AVG (instructie over doorgiften) en art. 44 AVG
- Toetspunt: Vermelding van de locaties waar de persoonsgegevens worden opgeslagen en vanwaar ze toegankelijk zijn; bij doorgifte buiten de EER door naar het kader doorgifte
- Tekstsoort: `append_section` · Nodig: storage_locations

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Locatie van de verwerking
1. Verwerker en de door hem ingeschakelde subverwerkers slaan de persoonsgegevens uitsluitend op, en hebben er uitsluitend toegang toe, op de volgende locaties: {{facts.storage_locations}}.
2. Verwerker geeft de persoonsgegevens niet door aan een derde land of een internationale organisatie, en wijzigt de locaties niet, zonder voorafgaande schriftelijke instructie van Verwerkingsverantwoordelijke en met inachtneming van hoofdstuk V van de AVG.
````

### 8. Onderdeel `audit` (standaardkop: Informatie en audits)

#### K7.10 — Of de verwerker informatie geeft en controles toestaat
- Grondslag: art. 28 lid 3 sub h AVG
- Toetspunt: De verwerker stelt alle informatie ter beschikking die nodig is om de nakoming van art. 28 aan te tonen, en maakt audits, waaronder inspecties, door de verwerkingsverantwoordelijke of een door hem gemachtigde controleur mogelijk en draagt eraan bij
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Informatie en audits
Verwerker stelt alle informatie ter beschikking van Verwerkingsverantwoordelijke die nodig is om de nakoming van de verplichtingen uit artikel 28 AVG en deze overeenkomst aan te tonen. Verwerker maakt audits, waaronder inspecties, door Verwerkingsverantwoordelijke of een door Verwerkingsverantwoordelijke gemachtigde controleur mogelijk en draagt daaraan bij.
````

### 9. Onderdeel `einde` (standaardkop: Einde van de verwerking)

#### K7.9 — Wat er met de gegevens gebeurt als de overeenkomst eindigt
- Grondslag: art. 28 lid 3 sub g AVG
- Toetspunt: Na afloop van de dienstverlening, naar keuze van de verwerkingsverantwoordelijke, alle persoonsgegevens wissen of terugbezorgen en bestaande kopieën verwijderen, tenzij opslag Unierechtelijk of lidstatelijk verplicht is
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Einde van de verwerking
Na afloop van de verwerkingsdiensten wist Verwerker, naar keuze van Verwerkingsverantwoordelijke, alle persoonsgegevens of bezorgt hij deze aan Verwerkingsverantwoordelijke terug, en verwijdert hij bestaande kopieën, tenzij opslag van de persoonsgegevens Unierechtelijk of lidstatelijk verplicht is.
````

## Toetspunten (voor de eindcontrole)

### K7.1 — Er is een schriftelijke verwerkersovereenkomst
- Grondslag: art. 28 lid 3 (aanhef) en lid 9 AVG
- Toetspunt: Een overeenkomst of andere rechtshandeling die de verwerker ten aanzien van de verwerkingsverantwoordelijke bindt, schriftelijk vastgelegd (elektronisch is toegestaan)
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); AVG-art28-lid9 (AVG art. 28 lid 9); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Sluit een schriftelijke verwerkersovereenkomst met de leverancier. Elektronisch aanvaarden is voldoende, maar de overeenkomst moet alle verplichte bepalingen bevatten.

### K7.2 — Waarover de overeenkomst gaat: onderwerp, duur, doel, gegevens en betrokkenen
- Grondslag: art. 28 lid 3 (aanhef) AVG
- Toetspunt: Onderwerp en duur van de verwerking, aard en doel, soort persoonsgegevens, categorieën betrokkenen, en de rechten en verplichtingen van de verwerkingsverantwoordelijke
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG); UB-2021-915 (Uitvoeringsbesluit (EU) 2021/915 van de Commissie betreffende standaardcontractbepalingen tussen verwerkingsverantwoordelijken en verwerkers als bedoeld in artikel 28, lid 7, van Verordening (EU) 2016/679 en artikel 29, lid 7, van Verordening (EU) 2018/1725)
- Wat de tekst moet bereiken: Beschrijf in de overeenkomst of een bijlage het onderwerp en de duur van de verwerking, wat er met de gegevens gebeurt en waarvoor, welke soorten gegevens het betreft en over welke groepen mensen.

### K7.3 — Of de verwerker alleen op instructie werkt
- Grondslag: art. 28 lid 3 sub a AVG
- Toetspunt: De verwerker verwerkt alleen op basis van schriftelijke instructies van de verwerkingsverantwoordelijke, ook bij doorgifte naar een derde land of internationale organisatie, tenzij een Unierechtelijke of lidstatelijke verplichting geldt; in dat geval meldt de verwerker dat vooraf, tenzij die wetgeving dat om gewichtige redenen van algemeen belang verbiedt
- Bronnen: AVG-art28-lid3-a (AVG art. 28 lid 3 sub a); AVG-art29 (AVG art. 29); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker de gegevens alleen gebruikt op schriftelijke instructie van de verwerkingsverantwoordelijke, ook bij doorgifte buiten de EER, en dat hij een wettelijke verplichting om anders te handelen vooraf meldt.

### K7.4 — Of de medewerkers van de verwerker tot geheimhouding verplicht zijn
- Grondslag: art. 28 lid 3 sub b AVG
- Toetspunt: Waarborg dat de tot verwerking gemachtigde personen zich tot vertrouwelijkheid hebben verbonden of door een passende wettelijke verplichting tot vertrouwelijkheid gebonden zijn
- Bronnen: AVG-art28-lid3-b (AVG art. 28 lid 3 sub b); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat iedereen die bij de verwerker met de gegevens werkt, tot geheimhouding verplicht is.

### K7.5 — Of de verwerker de gegevens goed beveiligt
- Grondslag: art. 28 lid 3 sub c jo. art. 32 AVG
- Toetspunt: De verwerker neemt alle maatregelen die op grond van art. 32 AVG vereist zijn
- Bronnen: AVG-art28-lid3-c (AVG art. 28 lid 3 sub c); AVG-art32 (AVG art. 32); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker alle beveiligingsmaatregelen neemt die art. 32 AVG vereist, en beschrijf die maatregelen in een bijlage.

### K7.6 — Onder welke voorwaarden de verwerker andere partijen mag inschakelen
- Grondslag: art. 28 lid 3 sub d jo. lid 2 en lid 4 AVG
- Toetspunt: Voorafgaande specifieke of algemene schriftelijke toestemming voor subverwerkers; bij algemene toestemming melding van beoogde wijzigingen met de mogelijkheid bezwaar te maken; dezelfde verplichtingen aan de subverwerker opleggen; de verwerker blijft volledig aansprakelijk
- Bronnen: AVG-art28-lid3-d (AVG art. 28 lid 3 sub d); AVG-art28-lid2 (AVG art. 28 lid 2); AVG-art28-lid4 (AVG art. 28 lid 4); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker alleen andere partijen inschakelt met voorafgaande schriftelijke toestemming, dat hij wijzigingen vooraf meldt zodat bezwaar mogelijk is, en dat hij dezelfde verplichtingen aan die partijen oplegt.

### K7.7 — Of de verwerker helpt bij verzoeken van mensen over hun gegevens
- Grondslag: art. 28 lid 3 sub e AVG
- Toetspunt: Bijstand door passende technische en organisatorische maatregelen bij het vervullen van de plicht om verzoeken van betrokkenen te beantwoorden (hoofdstuk III AVG)
- Bronnen: AVG-art28-lid3-e (AVG art. 28 lid 3 sub e); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker helpt als mensen hun rechten uitoefenen, bijvoorbeeld bij een verzoek om inzage of verwijdering.

### K7.8 — Of de verwerker helpt bij beveiliging, datalekken en risicobeoordelingen
- Grondslag: art. 28 lid 3 sub f jo. art. 32-36 AVG
- Toetspunt: Bijstand bij het nakomen van de verplichtingen uit art. 32 tot en met 36 AVG (beveiliging, melding en communicatie van datalekken, DPIA, voorafgaande raadpleging), rekening houdend met de aard van de verwerking en de informatie waarover de verwerker beschikt
- Bronnen: AVG-art28-lid3-f (AVG art. 28 lid 3 sub f); AVG-art32 (AVG art. 32); AVG-art33 (AVG art. 33); AVG-art33-lid2 (AVG art. 33 lid 2); AVG-art34 (AVG art. 34); AVG-art35 (AVG art. 35); AVG-art36 (AVG art. 36); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker helpt bij beveiliging, het melden van datalekken, een DPIA en een eventuele voorafgaande raadpleging van de Autoriteit Persoonsgegevens.

### K7.9 — Wat er met de gegevens gebeurt als de overeenkomst eindigt
- Grondslag: art. 28 lid 3 sub g AVG
- Toetspunt: Na afloop van de dienstverlening, naar keuze van de verwerkingsverantwoordelijke, alle persoonsgegevens wissen of terugbezorgen en bestaande kopieën verwijderen, tenzij opslag Unierechtelijk of lidstatelijk verplicht is
- Bronnen: AVG-art28-lid3-g (AVG art. 28 lid 3 sub g); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker na afloop, naar jouw keuze, alle gegevens wist of teruggeeft en kopieën verwijdert, tenzij de wet opslag verplicht.

### K7.10 — Of de verwerker informatie geeft en controles toestaat
- Grondslag: art. 28 lid 3 sub h AVG
- Toetspunt: De verwerker stelt alle informatie ter beschikking die nodig is om de nakoming van art. 28 aan te tonen, en maakt audits, waaronder inspecties, door de verwerkingsverantwoordelijke of een door hem gemachtigde controleur mogelijk en draagt eraan bij
- Bronnen: AVG-art28-lid3-h (AVG art. 28 lid 3 sub h); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker alle informatie geeft die nodig is om naleving aan te tonen, en controles (audits en inspecties) door jou of een door jou aangewezen controleur mogelijk maakt.

### K7.11 — Hoe snel de verwerker een datalek aan jou meldt
- Grondslag: art. 33 lid 2 AVG
- Toetspunt: Een meldtermijn voor datalekken van de verwerker aan de verwerkingsverantwoordelijke. Wettelijk: zonder onredelijke vertraging (art. 33 lid 2); een concrete termijn is gangbaar maar niet voorgeschreven
- Bronnen: AVG-art33-lid2 (AVG art. 33 lid 2); AVG-art33-lid1 (AVG art. 33 lid 1); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Spreek een concrete termijn af waarbinnen de verwerker een datalek aan jou meldt, zodat je zelf binnen 72 uur bij de Autoriteit Persoonsgegevens kunt melden.

### K7.12 — Waar de gegevens staan en vanwaar ze toegankelijk zijn
- Grondslag: art. 28 lid 3 sub a AVG (instructie over doorgiften) en art. 44 AVG
- Toetspunt: Vermelding van de locaties waar de persoonsgegevens worden opgeslagen en vanwaar ze toegankelijk zijn; bij doorgifte buiten de EER door naar het kader doorgifte
- Bronnen: AVG-art28-lid3-a (AVG art. 28 lid 3 sub a); AVG-art44 (AVG art. 44); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast waar de gegevens worden opgeslagen en vanuit welke landen de verwerker en zijn subverwerkers erbij kunnen.

### K7.13 — Of de afspraken over aansprakelijkheid de verplichtingen niet uithollen
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Aansprakelijkheidsbepalingen mogen de AVG-verplichtingen uit de verwerkersovereenkomst niet uithollen
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Controleer of de afspraken over aansprakelijkheid de verplichtingen van de verwerker niet in de praktijk buiten werking stellen.

### K7.14 — Of de verwerker waarschuwt bij een instructie die in strijd is met de wet
- Grondslag: art. 28 lid 3, laatste alinea, AVG
- Toetspunt: De verwerker stelt de verwerkingsverantwoordelijke onmiddellijk in kennis als een instructie naar zijn mening inbreuk oplevert op de AVG of op andere Unierechtelijke of lidstatelijke bepalingen inzake gegevensbescherming
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker je direct waarschuwt als hij vindt dat een instructie in strijd is met de privacywetgeving.

### K7.15 — Of je hebt nagegaan dat de dienstverlener de gegevens goed kan beschermen
- Grondslag: art. 28 lid 1 AVG
- Toetspunt: De verwerkingsverantwoordelijke doet alleen een beroep op verwerkers die afdoende garanties bieden voor passende technische en organisatorische maatregelen; heeft de klant dit nagegaan (certificering, beveiligingsinformatie, reputatie)?
- Bronnen: AVG-art28-lid1 (AVG art. 28 lid 1); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Ga na of de dienstverlener de gegevens goed kan beschermen, bijvoorbeeld aan de hand van een certificering, een beveiligingsdocument of een auditrapport, en leg vast wat je hebt gecontroleerd.
