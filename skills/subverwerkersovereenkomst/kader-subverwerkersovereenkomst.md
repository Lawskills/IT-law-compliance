# Kader K19 — Subverwerkersovereenkomst

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een overeenkomst tussen een verwerker en een subverwerker de toestemming van de verwerkingsverantwoordelijke volgt en dezelfde verplichtingen inzake gegevensbescherming oplegt als de verwerkersovereenkomst (art. 28 lid 3 sub a-h AVG).

Bronnen: AVG-art28-lid2 (AVG art. 28 lid 2); AVG-art28-lid3 (AVG art. 28 lid 3); AVG-art28-lid3-a (AVG art. 28 lid 3 sub a); AVG-art28-lid3-b (AVG art. 28 lid 3 sub b); AVG-art28-lid3-c (AVG art. 28 lid 3 sub c); AVG-art28-lid3-d (AVG art. 28 lid 3 sub d); AVG-art28-lid3-e (AVG art. 28 lid 3 sub e); AVG-art28-lid3-f (AVG art. 28 lid 3 sub f); AVG-art28-lid3-g (AVG art. 28 lid 3 sub g); AVG-art28-lid3-h (AVG art. 28 lid 3 sub h); AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art32-lid1 (AVG art. 32 lid 1); EDPB-ADV-22-2024 (EDPB, Advies 22/2024 over bepaalde verplichtingen die voortvloeien uit het inschakelen van verwerkers en subverwerkers); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)

## Formulier (vragen aan de gebruiker)

- **processor_name**: Wat is de naam van je organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van jouw organisatie (verwerker)
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **subprocessor_name**: Welke leverancier schakel je in als subverwerker?
  - Label (voor de plek-om-in-te-vullen): naam van de subverwerker
  - Type: text
- **controller_authorised**: Heeft je klant (de verwerkingsverantwoordelijke) vooraf schriftelijk toestemming gegeven voor deze subverwerker, specifiek of algemeen?
  - Label (voor de plek-om-in-te-vullen): of de verwerkingsverantwoordelijke toestemming gaf
  - Type: boolean
- **processing_description**: Welke verwerking doet de subverwerker, voor welk doel, met welke gegevens en van wie?
  - Label (voor de plek-om-in-te-vullen): welke verwerking de subverwerker doet
  - Type: text
- **security_measures**: Waar staan de beveiligingsmaatregelen van de subverwerker (bijvoorbeeld een bijlage)?
  - Label (voor de plek-om-in-te-vullen): waar de beveiligingsmaatregelen staan
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `onderwerp` (standaardkop: Onderwerp van de verwerking)

#### K19.1 — Waarover de subverwerking gaat
- Grondslag: art. 28 lid 3 (aanhef) en lid 4 AVG
- Toetspunt: De overeenkomst beschrijft onderwerp, duur, aard en doel van de verwerking, soort persoonsgegevens en categorieën betrokkenen
- Tekstsoort: `append_section` · Nodig: processing_description

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Onderwerp van de verwerking
Subverwerker verwerkt in opdracht van Verwerker persoonsgegevens voor: {{facts.processing_description}}.
````

### 2. Onderdeel `instructies` (standaardkop: Verwerking op instructie)

#### K19.3 — Of de subverwerker alleen op instructie verwerkt
- Grondslag: art. 28 lid 3 sub a en lid 4 AVG
- Toetspunt: De subverwerker verwerkt alleen op basis van schriftelijke instructies, ook bij doorgifte buiten de EER
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Verwerking op instructie
Subverwerker verwerkt de persoonsgegevens uitsluitend op basis van schriftelijke instructies van Verwerker, die de instructies van de verwerkingsverantwoordelijke volgen, ook wat betreft doorgifte naar een derde land.
````

### 3. Onderdeel `geheimhouding` (standaardkop: Geheimhouding)

#### K19.4 — Of geheimhouding is geregeld
- Grondslag: art. 28 lid 3 sub b en lid 4 AVG
- Toetspunt: Wie bij de subverwerker de gegevens verwerkt, is tot geheimhouding verplicht
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Geheimhouding
Subverwerker waarborgt dat de personen die de persoonsgegevens verwerken tot geheimhouding zijn verplicht.
````

### 4. Onderdeel `beveiliging` (standaardkop: Beveiliging)

#### K19.5 — Of beveiliging is geregeld
- Grondslag: art. 28 lid 3 sub c en lid 4 AVG
- Toetspunt: De subverwerker neemt de maatregelen van art. 32 AVG en biedt voldoende garanties voor passende technische en organisatorische maatregelen
- Tekstsoort: `append_section` · Nodig: security_measures

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Beveiliging
Subverwerker neemt alle maatregelen die op grond van artikel 32 AVG vereist zijn, zoals beschreven in: {{facts.security_measures}}.
````

### 5. Onderdeel `subverwerkers` (standaardkop: Subverwerkers)

#### K19.6 — Of verdere subverwerkers zijn geregeld
- Grondslag: art. 28 lid 3 sub d, lid 2 en lid 4 AVG; EDPB-advies 22/2024
- Toetspunt: De subverwerker schakelt alleen een verdere subverwerker in onder dezelfde voorwaarden (toestemming en dezelfde verplichtingen)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Verdere subverwerkers
Subverwerker schakelt geen andere verwerker in zonder voorafgaande schriftelijke toestemming en legt die dezelfde verplichtingen op als in deze overeenkomst.
````

### 6. Onderdeel `bijstand` (standaardkop: Bijstand)

#### K19.7 — Of bijstand is geregeld
- Grondslag: art. 28 lid 3 sub e en f en lid 4 AVG
- Toetspunt: De subverwerker helpt bij verzoeken van betrokkenen en bij de verplichtingen van art. 32-36 (beveiliging, datalekken, DPIA, voorafgaande raadpleging)
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Bijstand
Subverwerker verleent Verwerker bijstand bij het beantwoorden van verzoeken van betrokkenen en bij de verplichtingen van de artikelen 32 tot en met 36 AVG, en meldt een inbreuk in verband met persoonsgegevens zonder onredelijke vertraging aan Verwerker.
````

### 7. Onderdeel `einde` (standaardkop: Einde van de verwerking)

#### K19.8 — Of verwijderen of teruggeven is geregeld
- Grondslag: art. 28 lid 3 sub g en lid 4 AVG
- Toetspunt: Na afloop wist of retourneert de subverwerker de persoonsgegevens, tenzij opslag wettelijk verplicht is
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Einde van de verwerking
Na afloop van de dienstverlening wist Subverwerker de persoonsgegevens of geeft hij ze terug, naar keuze van Verwerker, en verwijdert hij bestaande kopieën, tenzij opslag wettelijk verplicht is.
````

### 8. Onderdeel `audit` (standaardkop: Informatie en audits)

#### K19.9 — Of informatie en audits zijn geregeld
- Grondslag: art. 28 lid 3 sub h en lid 4 AVG
- Toetspunt: De subverwerker stelt alle informatie beschikbaar die nodig is om naleving aan te tonen en maakt audits mogelijk
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Informatie en audits
Subverwerker stelt alle informatie beschikbaar die nodig is om de naleving van deze overeenkomst aan te tonen en maakt audits en inspecties door of namens Verwerker of de verwerkingsverantwoordelijke mogelijk.
````

#### K19.10 — Of de aansprakelijkheid van de verwerker is benoemd
- Grondslag: goede praktijk; art. 28 lid 4 (laatste zin) AVG
- Toetspunt: Komt de subverwerker zijn verplichtingen niet na, dan blijft de eerste verwerker tegenover de verwerkingsverantwoordelijke volledig aansprakelijk; de overeenkomst regelt het verhaal tussen verwerker en subverwerker
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Aansprakelijkheid
Subverwerker vergoedt Verwerker de schade die Verwerker lijdt doordat Subverwerker deze overeenkomst niet nakomt, waaronder aanspraken van de verwerkingsverantwoordelijke.
````

## Toetspunten (voor de eindcontrole)

### K19.1 — Waarover de subverwerking gaat
- Grondslag: art. 28 lid 3 (aanhef) en lid 4 AVG
- Toetspunt: De overeenkomst beschrijft onderwerp, duur, aard en doel van de verwerking, soort persoonsgegevens en categorieën betrokkenen
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); AVG-art28-lid4 (AVG art. 28 lid 4)
- Wat de tekst moet bereiken: Beschrijf welke verwerking de subverwerker doet, voor welk doel, met welke gegevens en van wie.

### K19.2 — Of de verwerkingsverantwoordelijke toestemming gaf
- Grondslag: art. 28 lid 2 AVG; EDPB-advies 22/2024
- Toetspunt: De verwerker schakelt de subverwerker pas in na voorafgaande specifieke of algemene schriftelijke toestemming van de verwerkingsverantwoordelijke; bij algemene toestemming informeert de verwerker over beoogde veranderingen en kan de verwerkingsverantwoordelijke bezwaar maken
- Bronnen: AVG-art28-lid2 (AVG art. 28 lid 2); EDPB-ADV-22-2024 (EDPB, Advies 22/2024 over bepaalde verplichtingen die voortvloeien uit het inschakelen van verwerkers en subverwerkers)
- Wat de tekst moet bereiken: Vraag je klant vooraf schriftelijk toestemming voor deze subverwerker, of meld hem bij algemene toestemming vooraf zodat hij bezwaar kan maken.

### K19.3 — Of de subverwerker alleen op instructie verwerkt
- Grondslag: art. 28 lid 3 sub a en lid 4 AVG
- Toetspunt: De subverwerker verwerkt alleen op basis van schriftelijke instructies, ook bij doorgifte buiten de EER
- Bronnen: AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art28-lid3-a (AVG art. 28 lid 3 sub a)
- Wat de tekst moet bereiken: Leg vast dat de subverwerker alleen op schriftelijke instructie verwerkt.

### K19.4 — Of geheimhouding is geregeld
- Grondslag: art. 28 lid 3 sub b en lid 4 AVG
- Toetspunt: Wie bij de subverwerker de gegevens verwerkt, is tot geheimhouding verplicht
- Bronnen: AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art28-lid3-b (AVG art. 28 lid 3 sub b)
- Wat de tekst moet bereiken: Leg geheimhouding vast voor wie bij de subverwerker de gegevens verwerkt.

### K19.5 — Of beveiliging is geregeld
- Grondslag: art. 28 lid 3 sub c en lid 4 AVG
- Toetspunt: De subverwerker neemt de maatregelen van art. 32 AVG en biedt voldoende garanties voor passende technische en organisatorische maatregelen
- Bronnen: AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art28-lid3-c (AVG art. 28 lid 3 sub c); AVG-art32-lid1 (AVG art. 32 lid 1)
- Wat de tekst moet bereiken: Leg de beveiligingsmaatregelen van de subverwerker vast.

### K19.6 — Of verdere subverwerkers zijn geregeld
- Grondslag: art. 28 lid 3 sub d, lid 2 en lid 4 AVG; EDPB-advies 22/2024
- Toetspunt: De subverwerker schakelt alleen een verdere subverwerker in onder dezelfde voorwaarden (toestemming en dezelfde verplichtingen)
- Bronnen: AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art28-lid3-d (AVG art. 28 lid 3 sub d); AVG-art28-lid2 (AVG art. 28 lid 2); EDPB-ADV-22-2024 (EDPB, Advies 22/2024 over bepaalde verplichtingen die voortvloeien uit het inschakelen van verwerkers en subverwerkers)
- Wat de tekst moet bereiken: Leg vast dat verdere subverwerkers alleen met toestemming en onder dezelfde verplichtingen worden ingeschakeld.

### K19.7 — Of bijstand is geregeld
- Grondslag: art. 28 lid 3 sub e en f en lid 4 AVG
- Toetspunt: De subverwerker helpt bij verzoeken van betrokkenen en bij de verplichtingen van art. 32-36 (beveiliging, datalekken, DPIA, voorafgaande raadpleging)
- Bronnen: AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art28-lid3-e (AVG art. 28 lid 3 sub e); AVG-art28-lid3-f (AVG art. 28 lid 3 sub f)
- Wat de tekst moet bereiken: Leg vast dat de subverwerker helpt bij verzoeken van betrokkenen, datalekken en DPIA's.

### K19.8 — Of verwijderen of teruggeven is geregeld
- Grondslag: art. 28 lid 3 sub g en lid 4 AVG
- Toetspunt: Na afloop wist of retourneert de subverwerker de persoonsgegevens, tenzij opslag wettelijk verplicht is
- Bronnen: AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art28-lid3-g (AVG art. 28 lid 3 sub g)
- Wat de tekst moet bereiken: Leg vast dat de gegevens na afloop worden gewist of teruggegeven.

### K19.9 — Of informatie en audits zijn geregeld
- Grondslag: art. 28 lid 3 sub h en lid 4 AVG
- Toetspunt: De subverwerker stelt alle informatie beschikbaar die nodig is om naleving aan te tonen en maakt audits mogelijk
- Bronnen: AVG-art28-lid4 (AVG art. 28 lid 4); AVG-art28-lid3-h (AVG art. 28 lid 3 sub h)
- Wat de tekst moet bereiken: Leg vast dat de subverwerker informatie geeft en audits mogelijk maakt.

### K19.10 — Of de aansprakelijkheid van de verwerker is benoemd
- Grondslag: goede praktijk; art. 28 lid 4 (laatste zin) AVG
- Toetspunt: Komt de subverwerker zijn verplichtingen niet na, dan blijft de eerste verwerker tegenover de verwerkingsverantwoordelijke volledig aansprakelijk; de overeenkomst regelt het verhaal tussen verwerker en subverwerker
- Bronnen: AVG-art28-lid4 (AVG art. 28 lid 4)
- Wat de tekst moet bereiken: Regel het verhaal tussen jou en de subverwerker: jij blijft tegenover je klant volledig aansprakelijk.
