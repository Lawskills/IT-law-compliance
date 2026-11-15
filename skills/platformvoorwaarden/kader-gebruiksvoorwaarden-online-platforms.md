# Kader C7 — Gebruiksvoorwaarden voor online platforms (DSA)

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of de voorwaarden van een online dienst (hosting, platform of marktplaats) de informatie bevatten die art. 14 DSA voorschrijft, in duidelijke taal, met de regels voor melden, motiveren, klagen en (bij marktplaatsen) handelaren waar die van toepassing zijn.

Bronnen: DSA-art12-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 12 lid 1); DSA-art12-lid2 (Digital Services Act (Vo. (EU) 2022/2065) art. 12 lid 2); DSA-art14-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 1); DSA-art14-lid2 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 2); DSA-art14-lid3 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 3); DSA-art16-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 16 lid 1); DSA-art17-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 17 lid 1); DSA-art20-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 20 lid 1); DSA-art30-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 30 lid 1)

## Formulier (vragen aan de gebruiker)

- **platform_name**: Hoe heet je website, app of platform?
  - Label (voor de plek-om-in-te-vullen): naam van de dienst
  - Type: text
- **service_type**: Wat voor dienst bied je aan?
  - Label (voor de plek-om-in-te-vullen): wat voor dienst het is
  - Type: enum (conduit / hosting / online_platform / marketplace)
- **micro_small**: Is je onderneming een micro- of kleine onderneming (minder dan 50 medewerkers en een jaaromzet of balanstotaal van ten hoogste 10 miljoen euro)?
  - Label (voor de plek-om-in-te-vullen): of je een micro- of kleine onderneming bent
  - Type: boolean
- **minors**: Is de dienst vooral gericht op minderjarigen, of wordt hij vooral door hen gebruikt?
  - Label (voor de plek-om-in-te-vullen): of de dienst vooral op minderjarigen is gericht
  - Type: boolean
- **contact_point**: Hoe kunnen gebruikers je snel en rechtstreeks bereiken (bijvoorbeeld een e-mailadres of contactformulier)?
  - Label (voor de plek-om-in-te-vullen): het contactpunt voor gebruikers
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `gebruik` (standaardkop: gebruik)

#### C7.1 — Of de beperkingen op het gebruik in de voorwaarden staan
- Grondslag: art. 14 lid 1 DSA
- Toetspunt: De voorwaarden bevatten informatie over de beperkingen die de dienst oplegt aan het gebruik met betrekking tot informatie die gebruikers verstrekken
- Tekstsoort: `append_section` · Nodig: platform_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Wat niet is toegestaan
Gebruikers plaatsen via {{facts.platform_name}} geen inhoud die onrechtmatig is of in strijd is met deze voorwaarden, zoals [IN TE VULLEN: welke soorten inhoud en welk gebruik niet zijn toegestaan].
````

### 2. Onderdeel `moderatie` (standaardkop: moderatie)

#### C7.2 — Of inhoudsmoderatie is beschreven
- Grondslag: art. 14 lid 1 DSA
- Toetspunt: De voorwaarden beschrijven het beleid, de procedures, maatregelen en instrumenten voor inhoudsmoderatie, met inbegrip van algoritmische besluitvorming en menselijke toetsing
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Wij controleren inhoud op naleving van deze voorwaarden. Daarbij gebruiken wij [IN TE VULLEN: welke automatische middelen, of geen]. Besluiten over verwijdering of beperking worden [IN TE VULLEN: hoe menselijke toetsing plaatsvindt]. Mogelijke maatregelen zijn het verwijderen of minder zichtbaar maken van inhoud en het opschorten of beëindigen van een account.
````

### 3. Onderdeel `melden` (standaardkop: melden)

#### C7.8 — Of inhoud gemeld kan worden
- Grondslag: art. 16 DSA
- Toetspunt: Een hostingdienst heeft een gemakkelijk toegankelijk, gebruiksvriendelijk elektronisch mechanisme waarmee iedereen illegale inhoud kan melden
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.service_type != "conduit"`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Illegale inhoud melden
Iedereen kan inhoud die volgens hem illegaal is melden via [IN TE VULLEN: meldformulier]. Wij behandelen meldingen tijdig, zorgvuldig en objectief en laten de melder weten wat wij hebben besloten.
````

### 4. Onderdeel `motivering` (standaardkop: motivering)

#### C7.9 — Of besluiten worden gemotiveerd
- Grondslag: art. 17 DSA
- Toetspunt: Een hostingdienst geeft getroffen gebruikers een duidelijke en specifieke motivering bij beperkingen zoals verwijdering, minder zichtbaar maken of opschorting
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.service_type != "conduit"`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Motivering
Als wij inhoud verwijderen, minder zichtbaar maken of een account beperken, krijg je een duidelijke en specifieke motivering, met de mogelijkheden om daartegen op te komen.
````

### 5. Onderdeel `klachten` (standaardkop: klachten)

#### C7.3 — Of het reglement voor klachten in de voorwaarden staat
- Grondslag: art. 14 lid 1 en art. 20 DSA
- Toetspunt: De voorwaarden bevatten het reglement van het interne systeem voor klachtenafhandeling
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.service_type != "conduit" and facts.service_type != "hosting" and facts.micro_small != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Klachten over moderatiebesluiten
Tegen een besluit over je inhoud of account kun je binnen zes maanden kosteloos en elektronisch een klacht indienen via [IN TE VULLEN: waar]. Wij behandelen klachten tijdig, zorgvuldig en niet uitsluitend geautomatiseerd, en laten je ons besluit weten.
````

### 6. Onderdeel `handelaren` (standaardkop: handelaren)

#### C7.10 — Of handelaren traceerbaar zijn (marktplaats)
- Grondslag: art. 30 DSA
- Toetspunt: Een online platform waarop consumenten overeenkomsten op afstand met handelaren sluiten, vraagt vóór toelating de gegevens van handelaren en spant zich in die te controleren
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.service_type != "conduit" and facts.service_type != "hosting" and facts.service_type != "online_platform" and facts.micro_small != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Handelaren
Handelaren geven vóór toelating hun naam, adres, telefoonnummer en e-mailadres, een identiteitsbewijs, betaalgegevens, hun inschrijving in het handelsregister (als die bestaat) en een verklaring dat zij alleen producten en diensten aanbieden die aan de wet voldoen. Wij spannen ons in deze gegevens te controleren.
````

### 7. Onderdeel `contact` (standaardkop: Wie zijn wij)

#### C7.7 — Of er een contactpunt voor gebruikers is
- Grondslag: art. 12 DSA
- Toetspunt: De dienst wijst een contactpunt aan waarmee gebruikers rechtstreeks en snel kunnen communiceren, en maakt de informatie daarover openbaar
- Tekstsoort: `append_section` · Nodig: contact_point

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Contact
Je bereikt ons rechtstreeks via {{facts.contact_point}}.
````

### 8. Onderdeel `wijzigingen` (standaardkop: wijzigingen)

#### C7.5 — Of gebruikers worden geïnformeerd over wezenlijke wijzigingen
- Grondslag: art. 14 lid 2 DSA
- Toetspunt: De dienst informeert gebruikers over elke wezenlijke wijziging van de voorwaarden
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Wijzigingen
Bij een wezenlijke wijziging van deze voorwaarden informeren wij gebruikers vooraf via [IN TE VULLEN: e-mail of een melding in de dienst].
````

## Toetspunten (voor de eindcontrole)

### C7.1 — Of de beperkingen op het gebruik in de voorwaarden staan
- Grondslag: art. 14 lid 1 DSA
- Toetspunt: De voorwaarden bevatten informatie over de beperkingen die de dienst oplegt aan het gebruik met betrekking tot informatie die gebruikers verstrekken
- Bronnen: DSA-art14-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 1)
- Wat de tekst moet bereiken: Beschrijf welke inhoud en welk gebruik niet zijn toegestaan.

### C7.2 — Of inhoudsmoderatie is beschreven
- Grondslag: art. 14 lid 1 DSA
- Toetspunt: De voorwaarden beschrijven het beleid, de procedures, maatregelen en instrumenten voor inhoudsmoderatie, met inbegrip van algoritmische besluitvorming en menselijke toetsing
- Bronnen: DSA-art14-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 1)
- Wat de tekst moet bereiken: Beschrijf hoe je inhoud modereert, welke automatische middelen je gebruikt en wanneer een mens meekijkt.

### C7.3 — Of het reglement voor klachten in de voorwaarden staat
- Grondslag: art. 14 lid 1 en art. 20 DSA
- Toetspunt: De voorwaarden bevatten het reglement van het interne systeem voor klachtenafhandeling
- Alleen als: `facts.service_type != "conduit" and facts.service_type != "hosting" and facts.micro_small != true`
- Bronnen: DSA-art14-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 1); DSA-art20-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 20 lid 1)
- Wat de tekst moet bereiken: Neem op hoe gebruikers binnen zes maanden kosteloos een klacht indienen tegen een moderatiebesluit en hoe je die behandelt.

### C7.4 — Of de voorwaarden duidelijk en toegankelijk zijn
- Grondslag: art. 14 lid 1 DSA
- Toetspunt: De informatie is opgesteld in duidelijke, eenvoudige, begrijpelijke, gebruiksvriendelijke en ondubbelzinnige taal en is openbaar en gemakkelijk toegankelijk
- Bronnen: DSA-art14-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 1)
- Wat de tekst moet bereiken: Schrijf de voorwaarden in eenvoudige taal en publiceer ze goed vindbaar.

### C7.5 — Of gebruikers worden geïnformeerd over wezenlijke wijzigingen
- Grondslag: art. 14 lid 2 DSA
- Toetspunt: De dienst informeert gebruikers over elke wezenlijke wijziging van de voorwaarden
- Bronnen: DSA-art14-lid2 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 2)
- Wat de tekst moet bereiken: Leg vast hoe je gebruikers informeert over wezenlijke wijzigingen.

### C7.6 — Of de voorwaarden begrijpelijk zijn voor minderjarigen
- Grondslag: art. 14 lid 3 DSA
- Toetspunt: Is de dienst vooral gericht op of gebruikt door minderjarigen, dan worden de voorwaarden en beperkingen uitgelegd op een manier die minderjarigen begrijpen
- Alleen als: `facts.minors != false`
- Bronnen: DSA-art14-lid3 (Digital Services Act (Vo. (EU) 2022/2065) art. 14 lid 3)
- Wat de tekst moet bereiken: Leg de voorwaarden en beperkingen uit op een manier die minderjarigen begrijpen.

### C7.7 — Of er een contactpunt voor gebruikers is
- Grondslag: art. 12 DSA
- Toetspunt: De dienst wijst een contactpunt aan waarmee gebruikers rechtstreeks en snel kunnen communiceren, en maakt de informatie daarover openbaar
- Bronnen: DSA-art12-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 12 lid 1); DSA-art12-lid2 (Digital Services Act (Vo. (EU) 2022/2065) art. 12 lid 2)
- Wat de tekst moet bereiken: Noem een contactpunt waarmee gebruikers je snel en rechtstreeks bereiken.

### C7.8 — Of inhoud gemeld kan worden
- Grondslag: art. 16 DSA
- Toetspunt: Een hostingdienst heeft een gemakkelijk toegankelijk, gebruiksvriendelijk elektronisch mechanisme waarmee iedereen illegale inhoud kan melden
- Alleen als: `facts.service_type != "conduit"`
- Bronnen: DSA-art16-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 16 lid 1)
- Wat de tekst moet bereiken: Beschrijf hoe iedereen illegale inhoud kan melden.

### C7.9 — Of besluiten worden gemotiveerd
- Grondslag: art. 17 DSA
- Toetspunt: Een hostingdienst geeft getroffen gebruikers een duidelijke en specifieke motivering bij beperkingen zoals verwijdering, minder zichtbaar maken of opschorting
- Alleen als: `facts.service_type != "conduit"`
- Bronnen: DSA-art17-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 17 lid 1)
- Wat de tekst moet bereiken: Leg vast dat gebruikers een motivering krijgen bij beperkingen van hun inhoud of account.

### C7.10 — Of handelaren traceerbaar zijn (marktplaats)
- Grondslag: art. 30 DSA
- Toetspunt: Een online platform waarop consumenten overeenkomsten op afstand met handelaren sluiten, vraagt vóór toelating de gegevens van handelaren en spant zich in die te controleren
- Alleen als: `facts.service_type != "conduit" and facts.service_type != "hosting" and facts.service_type != "online_platform" and facts.micro_small != true`
- Bronnen: DSA-art30-lid1 (Digital Services Act (Vo. (EU) 2022/2065) art. 30 lid 1)
- Wat de tekst moet bereiken: Leg vast welke gegevens handelaren vóór toelating moeten geven en dat je die controleert.
