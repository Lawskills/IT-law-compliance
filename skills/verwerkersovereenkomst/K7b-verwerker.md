# Kader K7b — Verwerkersovereenkomst (toets vanuit de verwerker)

Versie 1.2 · peildatum 2026-11-10

Doel: Toetsen of een verwerkersovereenkomst die de klant als verwerker van zijn opdrachtgever krijgt, aan art. 28 AVG voldoet, en signaleren welke bepalingen verder gaan dan de wet vereist.

Bronnen: AVG-art28 (AVG art. 28); AVG-art28-lid3 (AVG art. 28 lid 3); AVG-art28-lid10 (AVG art. 28 lid 10); AVG-art29 (AVG art. 29); AVG-art30-lid2 (AVG art. 30 lid 2); AVG-art32 (AVG art. 32); AVG-art33-lid2 (AVG art. 33 lid 2); AVG-art37 (AVG art. 37); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)

## Formulier (vragen aan de gebruiker)

- **processor_name**: Wat is de officiële naam van je organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van je organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **controller_name**: Wat is de naam van de opdrachtgever die je de overeenkomst heeft voorgelegd?
  - Label (voor de plek-om-in-te-vullen): naam van je opdrachtgever
  - Type: text
- **processing_subject**: Voor welke dienst die je levert, verwerk je de gegevens van je opdrachtgever?
  - Label (voor de plek-om-in-te-vullen): het onderwerp van de verwerking
  - Hulp: Bijvoorbeeld 'de salarisadministratie' of 'hosting en beheer van de webshop'.
  - Type: text
- **processing_duration**: Hoe lang duurt de verwerking?
  - Label (voor de plek-om-in-te-vullen): de duur van de verwerking
  - Hulp: Meestal: zolang de hoofdovereenkomst loopt. Noem de looptijd of het moment waarop de verwerking eindigt.
  - Type: text
- **processing_nature_purpose**: Wat doe je met de gegevens, en waarvoor?
  - Label (voor de plek-om-in-te-vullen): de aard en het doel van de verwerking
  - Hulp: Bijvoorbeeld 'loonstroken en aangiften maken voor de medewerkers van de opdrachtgever'.
  - Type: text
- **personal_data_categories**: Welke soorten gegevens krijg je van je opdrachtgever?
  - Label (voor de plek-om-in-te-vullen): de soorten persoonsgegevens
  - Hulp: Bijvoorbeeld naam, adres, telefoonnummer, e-mailadres, BSN of gezondheidsgegevens.
  - Type: text
- **data_subject_categories**: Over welke groepen mensen gaan die gegevens?
  - Label (voor de plek-om-in-te-vullen): de categorieën betrokkenen
  - Hulp: Bijvoorbeeld klanten, medewerkers, sollicitanten of patiënten.
  - Type: text
- **security_measures**: Welke beveiligingsmaatregelen neem je, of in welk document staan ze?
  - Label (voor de plek-om-in-te-vullen): de beveiligingsmaatregelen van de verwerker
  - Hulp: Bijvoorbeeld 'versleuteling, tweefactorauthenticatie, dagelijkse back-ups, zie bijlage 2'.
  - Type: text
- **approved_subprocessors**: Welke andere partijen schakel je in voor deze dienst (bijvoorbeeld hosting, e-mail, boekhoudsoftware of AI)?
  - Label (voor de plek-om-in-te-vullen): de subverwerkers waarvoor toestemming wordt gegeven
  - Hulp: Noem per partij de naam, de dienst en het land waar de gegevens staan.
  - Type: text
- **subprocessor_notice_period**: Hoe lang van tevoren kun je een nieuwe of vervangende partij melden aan je opdrachtgever?
  - Label (voor de plek-om-in-te-vullen): de termijn voor het melden van een nieuwe subverwerker
  - Hulp: De wet schrijft geen termijn voor; kies een termijn die lang genoeg is om bezwaar te kunnen maken, bijvoorbeeld een aantal weken.
  - Type: text
- **processor_own_purposes**: Gebruik je de gegevens van je opdrachtgever ook voor eigen doelen?
  - Label (voor de plek-om-in-te-vullen): of je de gegevens ook voor eigen doelen gebruikt
  - Hulp: Bijvoorbeeld om je product te verbeteren, om AI of software te trainen, of voor vergelijkingen tussen klanten (benchmarking). Ook als je de gegevens daarvoor eerst samenvoegt of anonimiseert.
  - Type: boolean
- **after_hours_breach_capacity**: Kun je een datalek ook buiten kantooruren en in het weekend opmerken en aan je opdrachtgever doorgeven?
  - Label (voor de plek-om-in-te-vullen): of je ook buiten kantooruren een datalek kunt signaleren en doorgeven
  - Type: boolean
- **certifications_held**: Welke beveiligingscertificeringen of keurmerken heb je?
  - Label (voor de plek-om-in-te-vullen): je beveiligingscertificeringen
  - Hulp: Bijvoorbeeld ISO 27001 of ISAE 3402. Heb je er geen, vul dan 'geen' in.
  - Type: text
- **current_subprocessors**: Welke andere partijen schakel je op dit moment in voor deze dienst?
  - Label (voor de plek-om-in-te-vullen): de partijen die je nu inschakelt
  - Hulp: Bijvoorbeeld hosting, e-mail, boekhoudsoftware of een AI-dienst. Schakel je niemand in, vul dan 'geen' in.
  - Type: text
- **can_delete_on_termination**: Kun je na het einde van de opdracht alle gegevens van je opdrachtgever wissen of teruggeven, ook uit back-ups, binnen de termijn die in de overeenkomst staat?
  - Label (voor de plek-om-in-te-vullen): of je na afloop alle gegevens kunt wissen of teruggeven, ook uit back-ups
  - Hulp: Denk aan back-ups die automatisch een bepaalde tijd worden bewaard, en aan kopieën bij partijen die je inschakelt.
  - Type: boolean

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `onderwerp` (standaardkop: Onderwerp van de verwerking)

#### K7b.1b — Waarover de overeenkomst gaat: onderwerp, duur, doel, gegevens en betrokkenen
- Grondslag: art. 28 lid 3 (aanhef) AVG
- Toetspunt: Onderwerp en duur van de verwerking, aard en doel, soort persoonsgegevens, categorieën betrokkenen, en de rechten en verplichtingen van de verwerkingsverantwoordelijke (toetspunt K7 stap 2)
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

#### K7b.1c — Of de verwerker alleen op instructie werkt
- Grondslag: art. 28 lid 3 sub a AVG
- Toetspunt: De verwerker verwerkt alleen op basis van schriftelijke instructies van de verwerkingsverantwoordelijke, ook bij doorgifte naar een derde land of internationale organisatie, tenzij een Unierechtelijke of lidstatelijke verplichting geldt; in dat geval meldt de verwerker dat vooraf, tenzij die wetgeving dat om gewichtige redenen van algemeen belang verbiedt (toetspunt K7 stap 3)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Verwerking op instructie
1. Verwerker verwerkt de persoonsgegevens uitsluitend op basis van schriftelijke instructies van Verwerkingsverantwoordelijke, mede met betrekking tot doorgiften van persoonsgegevens aan een derde land of een internationale organisatie.
2. Is Verwerker op grond van een op hem van toepassing zijnde bepaling van Unierecht of lidstatelijk recht tot een verwerking verplicht, dan stelt Verwerker Verwerkingsverantwoordelijke voorafgaand aan die verwerking in kennis van dat wettelijke voorschrift, tenzij die wetgeving deze kennisgeving om gewichtige redenen van algemeen belang verbiedt.
````

#### K7b.1k — Of de verwerker waarschuwt bij een instructie die in strijd is met de wet
- Grondslag: art. 28 lid 3, laatste alinea, AVG
- Toetspunt: De verwerker stelt de verwerkingsverantwoordelijke onmiddellijk in kennis als een instructie naar zijn mening inbreuk oplevert op de AVG of op andere Unierechtelijke of lidstatelijke bepalingen inzake gegevensbescherming (toetspunt K7 stap 14)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Instructie in strijd met de wet
Verwerker stelt Verwerkingsverantwoordelijke onmiddellijk in kennis indien een instructie naar zijn mening inbreuk oplevert op de AVG of op andere Unierechtelijke of lidstatelijke bepalingen inzake gegevensbescherming.
````

### 3. Onderdeel `geheimhouding` (standaardkop: Geheimhouding)

#### K7b.1d — Of de medewerkers van de verwerker tot geheimhouding verplicht zijn
- Grondslag: art. 28 lid 3 sub b AVG
- Toetspunt: Waarborg dat de tot verwerking gemachtigde personen zich tot vertrouwelijkheid hebben verbonden of door een passende wettelijke verplichting tot vertrouwelijkheid gebonden zijn (toetspunt K7 stap 4)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Geheimhouding
Verwerker waarborgt dat de personen die gemachtigd zijn de persoonsgegevens te verwerken, zich ertoe hebben verbonden vertrouwelijkheid in acht te nemen of door een passende wettelijke verplichting tot vertrouwelijkheid zijn gebonden.
````

### 4. Onderdeel `beveiliging` (standaardkop: Beveiliging)

#### K7b.1e — Of de verwerker de gegevens goed beveiligt
- Grondslag: art. 28 lid 3 sub c jo. art. 32 AVG
- Toetspunt: De verwerker neemt alle maatregelen die op grond van art. 32 AVG vereist zijn (toetspunt K7 stap 5)
- Tekstsoort: `append_section` · Nodig: security_measures

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Beveiliging
1. Verwerker neemt alle maatregelen die op grond van artikel 32 AVG vereist zijn. Rekening houdend met de stand van de techniek, de uitvoeringskosten, de aard, de omvang, de context en de verwerkingsdoeleinden en de risico's voor de rechten en vrijheden van personen, treft Verwerker passende technische en organisatorische maatregelen om een op het risico afgestemd beveiligingsniveau te waarborgen.
2. De maatregelen zijn beschreven in: {{facts.security_measures}}.
````

### 5. Onderdeel `subverwerkers` (standaardkop: Subverwerkers)

#### K7b.1f — Onder welke voorwaarden de verwerker andere partijen mag inschakelen
- Grondslag: art. 28 lid 3 sub d jo. lid 2 en lid 4 AVG
- Toetspunt: Voorafgaande specifieke of algemene schriftelijke toestemming voor subverwerkers; bij algemene toestemming melding van beoogde wijzigingen met de mogelijkheid bezwaar te maken; dezelfde verplichtingen aan de subverwerker opleggen; de verwerker blijft volledig aansprakelijk (toetspunt K7 stap 6)
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

#### K7b.1g — Of de verwerker helpt bij verzoeken van mensen over hun gegevens
- Grondslag: art. 28 lid 3 sub e AVG
- Toetspunt: Bijstand door passende technische en organisatorische maatregelen bij het vervullen van de plicht om verzoeken van betrokkenen te beantwoorden (hoofdstuk III AVG) (toetspunt K7 stap 7)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Bijstand bij verzoeken van betrokkenen
Rekening houdend met de aard van de verwerking verleent Verwerker Verwerkingsverantwoordelijke door middel van passende technische en organisatorische maatregelen, voor zover mogelijk, bijstand bij het vervullen van diens plicht om verzoeken van betrokkenen om uitoefening van hun rechten uit hoofdstuk III van de AVG te beantwoorden.
````

#### K7b.1h — Of de verwerker helpt bij beveiliging, datalekken en risicobeoordelingen
- Grondslag: art. 28 lid 3 sub f jo. art. 32-36 AVG
- Toetspunt: Bijstand bij het nakomen van de verplichtingen uit art. 32 tot en met 36 AVG (beveiliging, melding en communicatie van datalekken, DPIA, voorafgaande raadpleging), rekening houdend met de aard van de verwerking en de informatie waarover de verwerker beschikt (toetspunt K7 stap 8)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Bijstand bij beveiliging, datalekken en DPIA
1. Rekening houdend met de aard van de verwerking en de hem ter beschikking staande informatie verleent Verwerker Verwerkingsverantwoordelijke bijstand bij het doen nakomen van de verplichtingen uit de artikelen 32 tot en met 36 AVG: de beveiliging van de verwerking, de melding van een inbreuk in verband met persoonsgegevens aan de toezichthoudende autoriteit en de mededeling daarvan aan de betrokkene, de gegevensbeschermingseffectbeoordeling en de voorafgaande raadpleging van de toezichthoudende autoriteit.
2. Verwerker informeert Verwerkingsverantwoordelijke zonder onredelijke vertraging zodra hij kennis heeft genomen van een inbreuk in verband met persoonsgegevens.
````

### 7. Onderdeel `audit` (standaardkop: Informatie en audits)

#### K7b.1j — Of de verwerker informatie geeft en controles toestaat
- Grondslag: art. 28 lid 3 sub h AVG
- Toetspunt: De verwerker stelt alle informatie ter beschikking die nodig is om de nakoming van art. 28 aan te tonen, en maakt audits, waaronder inspecties, door de verwerkingsverantwoordelijke of een door hem gemachtigde controleur mogelijk en draagt eraan bij (toetspunt K7 stap 10)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Informatie en audits
Verwerker stelt alle informatie ter beschikking van Verwerkingsverantwoordelijke die nodig is om de nakoming van de verplichtingen uit artikel 28 AVG en deze overeenkomst aan te tonen. Verwerker maakt audits, waaronder inspecties, door Verwerkingsverantwoordelijke of een door Verwerkingsverantwoordelijke gemachtigde controleur mogelijk en draagt daaraan bij.
````

### 8. Onderdeel `einde` (standaardkop: Einde van de verwerking)

#### K7b.1i — Wat er met de gegevens gebeurt als de overeenkomst eindigt
- Grondslag: art. 28 lid 3 sub g AVG
- Toetspunt: Na afloop van de dienstverlening, naar keuze van de verwerkingsverantwoordelijke, alle persoonsgegevens wissen of terugbezorgen en bestaande kopieën verwijderen, tenzij opslag Unierechtelijk of lidstatelijk verplicht is (toetspunt K7 stap 9)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Einde van de verwerking
Na afloop van de verwerkingsdiensten wist Verwerker, naar keuze van Verwerkingsverantwoordelijke, alle persoonsgegevens of bezorgt hij deze aan Verwerkingsverantwoordelijke terug, en verwijdert hij bestaande kopieën, tenzij opslag van de persoonsgegevens Unierechtelijk of lidstatelijk verplicht is.
````

## Toetspunten (voor de eindcontrole)

### K7b.1a — Er is een schriftelijke verwerkersovereenkomst
- Grondslag: art. 28 lid 3 (aanhef) en lid 9 AVG
- Toetspunt: Een overeenkomst of andere rechtshandeling die de verwerker ten aanzien van de verwerkingsverantwoordelijke bindt, schriftelijk vastgelegd (elektronisch is toegestaan) (toetspunt K7 stap 1)
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); AVG-art28-lid9 (AVG art. 28 lid 9); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Sluit een schriftelijke verwerkersovereenkomst met je opdrachtgever. Elektronisch aanvaarden is voldoende, maar de overeenkomst moet alle verplichte bepalingen bevatten.

### K7b.1b — Waarover de overeenkomst gaat: onderwerp, duur, doel, gegevens en betrokkenen
- Grondslag: art. 28 lid 3 (aanhef) AVG
- Toetspunt: Onderwerp en duur van de verwerking, aard en doel, soort persoonsgegevens, categorieën betrokkenen, en de rechten en verplichtingen van de verwerkingsverantwoordelijke (toetspunt K7 stap 2)
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG); UB-2021-915 (Uitvoeringsbesluit (EU) 2021/915 van de Commissie betreffende standaardcontractbepalingen tussen verwerkingsverantwoordelijken en verwerkers als bedoeld in artikel 28, lid 7, van Verordening (EU) 2016/679 en artikel 29, lid 7, van Verordening (EU) 2018/1725)
- Wat de tekst moet bereiken: Beschrijf in de overeenkomst of een bijlage het onderwerp en de duur van de verwerking, wat er met de gegevens gebeurt en waarvoor, welke soorten gegevens het betreft en over welke groepen mensen.

### K7b.1c — Of de verwerker alleen op instructie werkt
- Grondslag: art. 28 lid 3 sub a AVG
- Toetspunt: De verwerker verwerkt alleen op basis van schriftelijke instructies van de verwerkingsverantwoordelijke, ook bij doorgifte naar een derde land of internationale organisatie, tenzij een Unierechtelijke of lidstatelijke verplichting geldt; in dat geval meldt de verwerker dat vooraf, tenzij die wetgeving dat om gewichtige redenen van algemeen belang verbiedt (toetspunt K7 stap 3)
- Bronnen: AVG-art28-lid3-a (AVG art. 28 lid 3 sub a); AVG-art29 (AVG art. 29); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker de gegevens alleen gebruikt op schriftelijke instructie van de verwerkingsverantwoordelijke, ook bij doorgifte buiten de EER, en dat hij een wettelijke verplichting om anders te handelen vooraf meldt.

### K7b.1d — Of de medewerkers van de verwerker tot geheimhouding verplicht zijn
- Grondslag: art. 28 lid 3 sub b AVG
- Toetspunt: Waarborg dat de tot verwerking gemachtigde personen zich tot vertrouwelijkheid hebben verbonden of door een passende wettelijke verplichting tot vertrouwelijkheid gebonden zijn (toetspunt K7 stap 4)
- Bronnen: AVG-art28-lid3-b (AVG art. 28 lid 3 sub b); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat iedereen die bij de verwerker met de gegevens werkt, tot geheimhouding verplicht is.

### K7b.1e — Of de verwerker de gegevens goed beveiligt
- Grondslag: art. 28 lid 3 sub c jo. art. 32 AVG
- Toetspunt: De verwerker neemt alle maatregelen die op grond van art. 32 AVG vereist zijn (toetspunt K7 stap 5)
- Bronnen: AVG-art28-lid3-c (AVG art. 28 lid 3 sub c); AVG-art32 (AVG art. 32); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker alle beveiligingsmaatregelen neemt die art. 32 AVG vereist, en beschrijf die maatregelen in een bijlage.

### K7b.1f — Onder welke voorwaarden de verwerker andere partijen mag inschakelen
- Grondslag: art. 28 lid 3 sub d jo. lid 2 en lid 4 AVG
- Toetspunt: Voorafgaande specifieke of algemene schriftelijke toestemming voor subverwerkers; bij algemene toestemming melding van beoogde wijzigingen met de mogelijkheid bezwaar te maken; dezelfde verplichtingen aan de subverwerker opleggen; de verwerker blijft volledig aansprakelijk (toetspunt K7 stap 6)
- Bronnen: AVG-art28-lid3-d (AVG art. 28 lid 3 sub d); AVG-art28-lid2 (AVG art. 28 lid 2); AVG-art28-lid4 (AVG art. 28 lid 4); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker alleen andere partijen inschakelt met voorafgaande schriftelijke toestemming, dat hij wijzigingen vooraf meldt zodat bezwaar mogelijk is, en dat hij dezelfde verplichtingen aan die partijen oplegt.

### K7b.1g — Of de verwerker helpt bij verzoeken van mensen over hun gegevens
- Grondslag: art. 28 lid 3 sub e AVG
- Toetspunt: Bijstand door passende technische en organisatorische maatregelen bij het vervullen van de plicht om verzoeken van betrokkenen te beantwoorden (hoofdstuk III AVG) (toetspunt K7 stap 7)
- Bronnen: AVG-art28-lid3-e (AVG art. 28 lid 3 sub e); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker helpt als mensen hun rechten uitoefenen, bijvoorbeeld bij een verzoek om inzage of verwijdering.

### K7b.1h — Of de verwerker helpt bij beveiliging, datalekken en risicobeoordelingen
- Grondslag: art. 28 lid 3 sub f jo. art. 32-36 AVG
- Toetspunt: Bijstand bij het nakomen van de verplichtingen uit art. 32 tot en met 36 AVG (beveiliging, melding en communicatie van datalekken, DPIA, voorafgaande raadpleging), rekening houdend met de aard van de verwerking en de informatie waarover de verwerker beschikt (toetspunt K7 stap 8)
- Bronnen: AVG-art28-lid3-f (AVG art. 28 lid 3 sub f); AVG-art32 (AVG art. 32); AVG-art33 (AVG art. 33); AVG-art33-lid2 (AVG art. 33 lid 2); AVG-art34 (AVG art. 34); AVG-art35 (AVG art. 35); AVG-art36 (AVG art. 36); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat de verwerker helpt bij beveiliging, het melden van datalekken, een DPIA en een eventuele voorafgaande raadpleging van de Autoriteit Persoonsgegevens.

### K7b.1i — Wat er met de gegevens gebeurt als de overeenkomst eindigt
- Grondslag: art. 28 lid 3 sub g AVG
- Toetspunt: Na afloop van de dienstverlening, naar keuze van de verwerkingsverantwoordelijke, alle persoonsgegevens wissen of terugbezorgen en bestaande kopieën verwijderen, tenzij opslag Unierechtelijk of lidstatelijk verplicht is (toetspunt K7 stap 9)
- Bronnen: AVG-art28-lid3-g (AVG art. 28 lid 3 sub g); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat je na afloop, naar keuze van je opdrachtgever, alle gegevens wist of teruggeeft en kopieën verwijdert, tenzij de wet opslag verplicht.

### K7b.1j — Of de verwerker informatie geeft en controles toestaat
- Grondslag: art. 28 lid 3 sub h AVG
- Toetspunt: De verwerker stelt alle informatie ter beschikking die nodig is om de nakoming van art. 28 aan te tonen, en maakt audits, waaronder inspecties, door de verwerkingsverantwoordelijke of een door hem gemachtigde controleur mogelijk en draagt eraan bij (toetspunt K7 stap 10)
- Bronnen: AVG-art28-lid3-h (AVG art. 28 lid 3 sub h); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat je alle informatie geeft die nodig is om naleving aan te tonen, en controles (audits en inspecties) door je opdrachtgever of een door hem aangewezen controleur mogelijk maakt.

### K7b.1k — Of de verwerker waarschuwt bij een instructie die in strijd is met de wet
- Grondslag: art. 28 lid 3, laatste alinea, AVG
- Toetspunt: De verwerker stelt de verwerkingsverantwoordelijke onmiddellijk in kennis als een instructie naar zijn mening inbreuk oplevert op de AVG of op andere Unierechtelijke of lidstatelijke bepalingen inzake gegevensbescherming (toetspunt K7 stap 14)
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Leg vast dat je je opdrachtgever direct waarschuwt als je vindt dat een instructie in strijd is met de privacywetgeving.

### K7b.2 — Of je de gegevens alleen voor je opdrachtgever gebruikt
- Grondslag: art. 28 lid 10 en art. 29 AVG
- Toetspunt: Klopt de rolverdeling? Gebruikt de verwerker de gegevens volgens de overeenkomst of in de praktijk ook voor eigen doelen (bijvoorbeeld productverbetering, AI-training, benchmarking), dan is hij voor dat deel verwerkingsverantwoordelijke (art. 28 lid 10)
- Bronnen: AVG-art28-lid10 (AVG art. 28 lid 10); AVG-art29 (AVG art. 29); AVG-art4-7 (AVG art. 4 punt 7); AVG-art4-8 (AVG art. 4 punt 8); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Gebruik je de gegevens ook voor eigen doelen, dan ben je voor dat deel zelf verantwoordelijk en gelden daarvoor alle AVG-plichten van een verantwoordelijke. Stem dit af met je opdrachtgever en leg de rolverdeling vast.

### K7b.3 — Of de termijn voor het melden van een datalek haalbaar is
- Grondslag: art. 33 lid 2 AVG
- Toetspunt: Meldtermijn datalek: is de termijn haalbaar (bijvoorbeeld binnen enkele uren, ook buiten kantooruren)? Wettelijk is alleen "zonder onredelijke vertraging" vereist
- Bronnen: AVG-art33-lid2 (AVG art. 33 lid 2); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: De wet eist alleen dat je een datalek zonder onredelijke vertraging meldt. Een kortere afgesproken termijn is toegestaan, maar ga na of je die ook buiten kantooruren kunt halen.

### K7b.4 — Of je aan de gevraagde beveiligingsnormen kunt voldoen
- Grondslag: art. 28 lid 3 sub c jo. art. 32 AVG
- Toetspunt: Beveiliging: worden specifieke normen of certificeringen geëist (bijvoorbeeld ISO 27001) die de verwerker niet heeft? Geen wettelijke eis
- Bronnen: AVG-art28-lid3-c (AVG art. 28 lid 3 sub c); AVG-art32 (AVG art. 32); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: De wet eist passende beveiliging, geen specifieke certificering. Vraagt de overeenkomst een certificering die je niet hebt, dan is dat een afspraak die verder gaat dan de wet.

### K7b.5 — Welke afspraken er over controles (audits) zijn
- Grondslag: art. 28 lid 3 sub h AVG
- Toetspunt: Audits: wie betaalt, hoe vaak, met welke aankondiging? Art. 28 lid 3 sub h vereist medewerking, niet onbeperkte kosteloze audits
- Bronnen: AVG-art28-lid3-h (AVG art. 28 lid 3 sub h); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: De wet eist dat je meewerkt aan audits, niet dat die onbeperkt en kosteloos zijn. Afspraken over kosten, frequentie en aankondiging zijn gebruikelijk.

### K7b.6 — Of je je huidige leveranciers mag blijven gebruiken
- Grondslag: art. 28 lid 2 en lid 4 AVG
- Toetspunt: Subverwerkers: zijn de huidige subverwerkers (hosting, e-mail, AI) al toegestaan? Specifieke toestemming per subverwerker kan de dienstverlening blokkeren
- Bronnen: AVG-art28-lid2 (AVG art. 28 lid 2); AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art28-lid3-d (AVG art. 28 lid 3 sub d); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Controleer of alle partijen die je nu inschakelt in de overeenkomst zijn toegestaan. Vraagt de overeenkomst toestemming per partij, ga dan na of je je dienst kunt blijven leveren als een partij wordt vervangen.

### K7b.7 — Hoe aansprakelijkheid en vrijwaring zijn geregeld
- Grondslag: art. 28 lid 3 AVG (bevat geen verplichte bepaling over aansprakelijkheid)
- Toetspunt: Aansprakelijkheid en vrijwaring: onbeperkte aansprakelijkheid of vrijwaring voor boetes van de verwerkingsverantwoordelijke; commerciële en verzekeringsvraag
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: De wet schrijft geen aansprakelijkheidsregeling in de verwerkersovereenkomst voor. Onbeperkte aansprakelijkheid of een vrijwaring voor boetes is een commerciële afspraak; ga na of je verzekering dit dekt.

### K7b.8 — Of je de gegevens na afloop echt kunt wissen of teruggeven
- Grondslag: art. 28 lid 3 sub g AVG
- Toetspunt: Einde: kan de verwerker de gegevens na afloop daadwerkelijk wissen of teruggeven, ook uit back-ups, binnen een genoemde termijn?
- Bronnen: AVG-art28-lid3-g (AVG art. 28 lid 3 sub g); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Ga na of je na afloop alle gegevens kunt wissen of teruggeven, ook uit back-ups en bij partijen die je inschakelt. Lukt dat niet binnen de afgesproken termijn, stem dan een haalbare termijn af.
