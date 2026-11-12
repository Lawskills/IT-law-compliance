# Kader C2 — Service level agreement (SLA)

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of een SLA de gebruikelijke en meetbare afspraken bevat over beschikbaarheid, ondersteuning, storingen, onderhoud, back-ups, beveiliging, rapportage en de gevolgen als de afspraken niet worden gehaald, en waar de wet raakt (datalekken, overstappen) die verplichtingen niet uitholt.

Bronnen: AVG-art28-lid3-f (AVG art. 28 lid 3 sub f); AVG-art32-lid1 (AVG art. 32 lid 1); AVG-art32-lid1-c (AVG art. 32 lid 1 sub c); AVG-art33-lid2 (AVG art. 33 lid 2); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); DA-art23 (Data Act (Vo. (EU) 2023/2854) art. 23); DA-art25-lid1 (Data Act (Vo. (EU) 2023/2854) art. 25 lid 1); NIS2-art21-lid2-d (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub d)

## Formulier (vragen aan de gebruiker)

- **supplier_name**: Wie levert de dienst?
  - Label (voor de plek-om-in-te-vullen): naam van de leverancier
  - Type: text
- **customer_name**: Wie neemt de dienst af?
  - Label (voor de plek-om-in-te-vullen): naam van de afnemer
  - Type: text
- **service_name**: Om welke dienst gaat het?
  - Label (voor de plek-om-in-te-vullen): welke dienst
  - Type: text
- **personal_data**: Verwerkt de leverancier bij de dienst persoonsgegevens voor de afnemer?
  - Label (voor de plek-om-in-te-vullen): of de leverancier persoonsgegevens verwerkt
  - Type: boolean
- **cloud_service**: Is het een clouddienst (software, platform of infrastructuur op afstand)?
  - Label (voor de plek-om-in-te-vullen): of het een clouddienst is
  - Type: boolean
- **availability**: Welke beschikbaarheid spreken jullie af, en over welke periode (bijvoorbeeld 99,5% per maand)?
  - Label (voor de plek-om-in-te-vullen): de beschikbaarheid
  - Type: text
- **support_hours**: Wanneer is er ondersteuning (bijvoorbeeld werkdagen 9-17 uur)?
  - Label (voor de plek-om-in-te-vullen): de ondersteuningstijden
  - Type: text
- **response_times**: Welke reactie- en oplostijden gelden per prioriteit?
  - Label (voor de plek-om-in-te-vullen): de reactietijden
  - Type: text
- **maintenance_window**: Wanneer vindt gepland onderhoud plaats en hoe lang van tevoren wordt het aangekondigd?
  - Label (voor de plek-om-in-te-vullen): het onderhoudsvenster
  - Type: text
- **backup_terms**: Hoe vaak worden back-ups gemaakt en hoe snel kan worden hersteld?
  - Label (voor de plek-om-in-te-vullen): de back-upafspraken
  - Type: text
- **service_credits**: Wat krijgt de afnemer als de afspraken niet worden gehaald (bijvoorbeeld een korting op de maandprijs)?
  - Label (voor de plek-om-in-te-vullen): de gevolgen bij het niet halen van de afspraken
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `dienst` (standaardkop: dienst)

#### C2.1 — Welke dienst de SLA dekt
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA beschrijft de dienst en wat wel en niet onder de afspraken valt
- Tekstsoort: `append_section` · Nodig: service_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Dienst
Deze SLA geldt voor {{facts.service_name}} die Leverancier aan Afnemer levert. Wat niet in deze SLA staat, valt buiten de servicenormen.
````

### 2. Onderdeel `beschikbaarheid` (standaardkop: beschikbaarheid)

#### C2.2 — Of beschikbaarheid meetbaar is afgesproken
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA noemt een beschikbaarheidspercentage met meetperiode, meetmethode en uitzonderingen (zoals gepland onderhoud)
- Tekstsoort: `append_section` · Nodig: availability

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Beschikbaarheid
1. Leverancier spant zich in voor een beschikbaarheid van {{facts.availability}}.
2. Gepland onderhoud dat volgens deze SLA is aangekondigd, telt niet mee als onbeschikbaarheid.
3. Leverancier meet de beschikbaarheid en deelt de meting op verzoek met Afnemer.
````

### 3. Onderdeel `onderhoud` (standaardkop: onderhoud)

#### C2.3 — Of gepland onderhoud is geregeld
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA regelt wanneer gepland onderhoud plaatsvindt en hoe het wordt aangekondigd
- Tekstsoort: `append_section` · Nodig: maintenance_window

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Onderhoud
Gepland onderhoud vindt plaats {{facts.maintenance_window}}.
````

### 4. Onderdeel `support` (standaardkop: support)

#### C2.4 — Of ondersteuning en reactietijden zijn afgesproken
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA noemt ondersteuningstijden, contactkanalen en reactie- en oplostijden per prioriteit
- Tekstsoort: `append_section` · Nodig: support_hours, response_times

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Ondersteuning
1. Ondersteuning is beschikbaar: {{facts.support_hours}}.
2. Reactie- en oplostijden per prioriteit: {{facts.response_times}}.
````

### 5. Onderdeel `incidenten` (standaardkop: incidenten)

#### C2.5 — Of storingen worden gemeld en opgelost
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA regelt hoe storingen worden gemeld, geprioriteerd en afgehandeld
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Storingen
Afnemer meldt een storing via het kanaal dat Leverancier daarvoor aanwijst. Leverancier bevestigt de melding, bepaalt de prioriteit volgens deze SLA en houdt Afnemer op de hoogte tot de storing is opgelost.
````

### 6. Onderdeel `backup` (standaardkop: backup)

#### C2.6 — Of back-ups en herstel zijn geregeld
- Grondslag: goede praktijk; art. 32 lid 1 sub c AVG (bij persoonsgegevens) als achtergrond
- Toetspunt: De SLA regelt back-ups en hersteltijden (hoeveel gegevens maximaal verloren mogen gaan en hoe snel de dienst terug is)
- Tekstsoort: `append_section` · Nodig: backup_terms

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Back-ups en herstel
Back-ups en herstel: {{facts.backup_terms}}.
````

### 7. Onderdeel `beveiliging` (standaardkop: Beveiliging)

#### C2.10 — Of beveiliging is afgesproken
- Grondslag: goede praktijk; art. 32 AVG en art. 21 lid 2 sub d NIS2 (toeleveringsketen, voor organisaties onder de Cyberbeveiligingswet) als achtergrond
- Toetspunt: De SLA of de onderliggende overeenkomst regelt de beveiligingsmaatregelen van de leverancier
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Beveiliging
Leverancier neemt passende technische en organisatorische beveiligingsmaatregelen, zoals beschreven in de beveiligingsbijlage bij de overeenkomst.
````

### 8. Onderdeel `rapportage` (standaardkop: rapportage)

#### C2.8 — Of er wordt gerapporteerd over de prestaties
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA regelt hoe vaak en hoe Leverancier rapporteert over beschikbaarheid en storingen
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Rapportage
Leverancier rapporteert periodiek over de beschikbaarheid en de afgehandelde storingen.
````

### 9. Onderdeel `gevolgen` (standaardkop: gevolgen)

#### C2.7 — Of de gevolgen zijn geregeld als de afspraken niet worden gehaald
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA regelt wat er gebeurt als de servicenormen niet worden gehaald (bijvoorbeeld servicecredits) en hoe dat zich verhoudt tot aansprakelijkheid en ontbinding
- Tekstsoort: `append_section` · Nodig: service_credits

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Gevolgen bij het niet halen van de normen
Haalt Leverancier de servicenormen niet, dan geldt: {{facts.service_credits}}.
````

### 10. Onderdeel `exit` (standaardkop: exit)

#### C2.11 — Of overstappen en teruggave van gegevens zijn geregeld
- Grondslag: art. 23 en 25 Data Act
- Toetspunt: Bij een clouddienst regelt de overeenkomst het overstappen naar een andere aanbieder en de export van gegevens volgens de Data Act (mag in de hoofdovereenkomst staan)
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.cloud_service != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Overstappen en gegevens
Voor overstappen naar een andere aanbieder en de export van gegevens gelden de bepalingen daarover in de hoofdovereenkomst, die voldoen aan artikel 25 van de Dataverordening.
````

## Toetspunten (voor de eindcontrole)

### C2.1 — Welke dienst de SLA dekt
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA beschrijft de dienst en wat wel en niet onder de afspraken valt
- Bronnen: BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Beschrijf welke dienst de SLA dekt en wat erbuiten valt.

### C2.2 — Of beschikbaarheid meetbaar is afgesproken
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA noemt een beschikbaarheidspercentage met meetperiode, meetmethode en uitzonderingen (zoals gepland onderhoud)
- Bronnen: BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Spreek een beschikbaarheid af met meetperiode en meetmethode, en noem wat niet meetelt.

### C2.3 — Of gepland onderhoud is geregeld
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA regelt wanneer gepland onderhoud plaatsvindt en hoe het wordt aangekondigd
- Bronnen: BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Leg vast wanneer onderhoud plaatsvindt en hoe lang van tevoren het wordt aangekondigd.

### C2.4 — Of ondersteuning en reactietijden zijn afgesproken
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA noemt ondersteuningstijden, contactkanalen en reactie- en oplostijden per prioriteit
- Bronnen: BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Spreek ondersteuningstijden af en reactie- en oplostijden per prioriteit.

### C2.5 — Of storingen worden gemeld en opgelost
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA regelt hoe storingen worden gemeld, geprioriteerd en afgehandeld
- Bronnen: BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Leg vast hoe Afnemer een storing meldt en hoe Leverancier die afhandelt en terugkoppelt.

### C2.6 — Of back-ups en herstel zijn geregeld
- Grondslag: goede praktijk; art. 32 lid 1 sub c AVG (bij persoonsgegevens) als achtergrond
- Toetspunt: De SLA regelt back-ups en hersteltijden (hoeveel gegevens maximaal verloren mogen gaan en hoe snel de dienst terug is)
- Bronnen: AVG-art32-lid1-c (AVG art. 32 lid 1 sub c)
- Wat de tekst moet bereiken: Spreek af hoe vaak back-ups worden gemaakt en hoe snel na een incident wordt hersteld.

### C2.7 — Of de gevolgen zijn geregeld als de afspraken niet worden gehaald
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA regelt wat er gebeurt als de servicenormen niet worden gehaald (bijvoorbeeld servicecredits) en hoe dat zich verhoudt tot aansprakelijkheid en ontbinding
- Bronnen: BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Leg vast wat Afnemer krijgt als de normen niet worden gehaald, en of dat de enige vergoeding is.

### C2.8 — Of er wordt gerapporteerd over de prestaties
- Grondslag: goede praktijk; art. 7:401 BW en art. 6:248 BW als achtergrond
- Toetspunt: De SLA regelt hoe vaak en hoe Leverancier rapporteert over beschikbaarheid en storingen
- Bronnen: BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Spreek een periodieke rapportage af over beschikbaarheid en storingen.

### C2.9 — Of datalekken op tijd worden gemeld
- Grondslag: art. 33 lid 2 en art. 28 lid 3 sub f AVG
- Toetspunt: Verwerkt de leverancier persoonsgegevens, dan beperkt de SLA de plicht om een inbreuk in verband met persoonsgegevens zonder onredelijke vertraging aan de afnemer te melden niet
- Alleen als: `facts.personal_data != false`
- Bronnen: AVG-art33-lid2 (AVG art. 33 lid 2); AVG-art28-lid3-f (AVG art. 28 lid 3 sub f)
- Wat de tekst moet bereiken: Laat datalekken zonder onredelijke vertraging melden, of verwijs naar de verwerkersovereenkomst.

### C2.10 — Of beveiliging is afgesproken
- Grondslag: goede praktijk; art. 32 AVG en art. 21 lid 2 sub d NIS2 (toeleveringsketen, voor organisaties onder de Cyberbeveiligingswet) als achtergrond
- Toetspunt: De SLA of de onderliggende overeenkomst regelt de beveiligingsmaatregelen van de leverancier
- Bronnen: AVG-art32-lid1 (AVG art. 32 lid 1); NIS2-art21-lid2-d (NIS2-richtlijn (Richtlijn (EU) 2022/2555) art. 21 lid 2 sub d)
- Wat de tekst moet bereiken: Neem op welke beveiligingsmaatregelen de leverancier neemt, of verwijs naar een beveiligingsbijlage.

### C2.11 — Of overstappen en teruggave van gegevens zijn geregeld
- Grondslag: art. 23 en 25 Data Act
- Toetspunt: Bij een clouddienst regelt de overeenkomst het overstappen naar een andere aanbieder en de export van gegevens volgens de Data Act (mag in de hoofdovereenkomst staan)
- Alleen als: `facts.cloud_service != false`
- Bronnen: DA-art23 (Data Act (Vo. (EU) 2023/2854) art. 23); DA-art25-lid1 (Data Act (Vo. (EU) 2023/2854) art. 25 lid 1)
- Wat de tekst moet bereiken: Verwijs naar de overstap- en exportbepalingen in de hoofdovereenkomst, of neem ze op (Data Act art. 25).
