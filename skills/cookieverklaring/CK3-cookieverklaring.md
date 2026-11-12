# Kader CK3 — Informatie en cookieverklaring

Versie 0.3 · peildatum 2026-11-10

Doel: Controleren of de cookieverklaring duidelijke en volledige informatie geeft: welke cookies, met welk doel, van welke partijen, hoe lang, hoe de toestemming kan worden ingetrokken, wie verantwoordelijk is en op welke grond, en of de verklaring overeenkomt met de cookies die werkelijk worden gebruikt.

Bronnen: TW-art11.7a-lid1-a (Telecommunicatiewet art. 11.7a lid 1 sub a); AVG-art7-lid3 (AVG art. 7 lid 3); AVG-art12-lid1 (AVG art. 12 lid 1); AVG-art13-lid1-a (AVG art. 13 lid 1 sub a); AVG-art13-lid1-c (AVG art. 13 lid 1 sub c); AVG-art13-lid1-e (AVG art. 13 lid 1 sub e); AVG-art13-lid1-f (AVG art. 13 lid 1 sub f); AVG-art13-lid2-a (AVG art. 13 lid 2 sub a); AVG-art13-lid2-b (AVG art. 13 lid 2 sub b); AVG-art13-lid2-c (AVG art. 13 lid 2 sub c); AVG-art21-lid4 (AVG art. 21 lid 4); HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); AP-cookies-organisatie (Autoriteit Persoonsgegevens, 'Cookies en uw organisatie: zorg voor een goed beleid'); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten)); AP-normuitleg-intrekken-2024 (Autoriteit Persoonsgegevens, 'Normuitleg intrekken van toestemming bij cookiebanners')

## Formulier (vragen aan de gebruiker)

- **controller_name**: Wat is de officiële naam van je organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van je organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **controller_contact**: Op welk adres en e-mailadres kunnen bezoekers je bereiken met vragen over cookies en privacy?
  - Label (voor de plek-om-in-te-vullen): adres en e-mailadres van je organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **cookie_overview**: Geef per cookie of categorie de naam, van welke partij hij is, waarvoor hij dient en hoe lang hij blijft staan.
  - Label (voor de plek-om-in-te-vullen): het overzicht van je cookies met naam, partij, doel en looptijd
  - Hulp: Een export uit je cookietool is het makkelijkst. Heb je de cookiecheck gedaan, dan wordt de lijst daaruit overgenomen.
  - Type: text
- **third_parties**: Welke andere partijen plaatsen via je website cookies of ontvangen gegevens, en voor welk doel?
  - Label (voor de plek-om-in-te-vullen): de andere partijen die cookies plaatsen of gegevens ontvangen, per doel
  - Type: text
- **withdrawal_instructions**: Hoe kunnen bezoekers hun cookiekeuze wijzigen of hun toestemming intrekken?
  - Label (voor de plek-om-in-te-vullen): hoe bezoekers hun keuze kunnen wijzigen of hun toestemming kunnen intrekken
  - Hulp: Bijvoorbeeld: 'via de knop Cookie-instellingen linksonder op elke pagina'.
  - Type: text
- **uses_consent_cookies**: Gebruikt je website cookies of trackers waarvoor je toestemming vraagt, zoals voor statistieken van een andere partij, advertenties of socialmedia?
  - Label (voor de plek-om-in-te-vullen): of je cookies gebruikt waarvoor toestemming nodig is
  - Type: boolean
- **personal_data_via_cookies**: Worden via de cookies gegevens verzameld die iets zeggen over een persoon of apparaat, zoals een IP-adres, een uniek nummer of surfgedrag?
  - Label (voor de plek-om-in-te-vullen): of via de cookies persoonsgegevens worden verwerkt
  - Type: boolean
- **legal_bases**: Op welke grond gebruik je de gegevens per categorie cookies (bijvoorbeeld toestemming voor advertentiecookies, gerechtvaardigd belang voor statistieken)?
  - Label (voor de plek-om-in-te-vullen): de grondslag per categorie cookies
  - Type: text · Alleen vragen als: `facts.personal_data_via_cookies != false`
- **privacy_statement_link**: Waar staat je privacyverklaring (webadres)?
  - Label (voor de plek-om-in-te-vullen): de vindplaats van je privacyverklaring
  - Type: text
- **transfers_outside_eea**: Komen gegevens uit cookies van andere partijen terecht buiten de Europese Unie, Noorwegen, IJsland en Liechtenstein?
  - Label (voor de plek-om-in-te-vullen): of cookies van derden gegevens buiten de EU/EER brengen
  - Hulp: Denk aan Amerikaanse advertentie-, statistiek- en socialmediadiensten.
  - Type: boolean
- **transfer_details**: Naar welke landen en via welke partijen gaan de gegevens, en op welke basis?
  - Label (voor de plek-om-in-te-vullen): landen, partijen en de waarborg per doorgifte
  - Hulp: Bijvoorbeeld: 'Verenigde Staten, Meta, EU-VS Data Privacy Framework'.
  - Type: text · Alleen vragen als: `facts.transfers_outside_eea != false`
- **statement_findable**: Is de cookieverklaring te vinden via een link in de banner en onderaan elke pagina?
  - Label (voor de plek-om-in-te-vullen): of de cookieverklaring vanaf de banner en elke pagina te vinden is
  - Type: boolean

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `contact` (standaardkop: Wie zijn wij)

#### CK3.6 — Wie verantwoordelijk is voor de cookies en hoe bezoekers je bereiken
- Grondslag: art. 11.7a lid 1 sub a Telecommunicatiewet (informatie overeenkomstig de AVG); art. 13 lid 1 sub a AVG
- Toetspunt: De verklaring noemt de naam en contactgegevens van de website-eigenaar, of verwijst duidelijk naar een privacyverklaring waarin die staan
- Tekstsoort: `insert` · Nodig: controller_name, controller_contact

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Wie zijn wij
Deze cookieverklaring is van {{facts.controller_name}}. Je kunt ons bereiken via: {{facts.controller_contact}}.
````

### 2. Onderdeel `cookies` (standaardkop: Welke cookies gebruiken wij)

#### CK3.1 — Welke cookies je gebruikt
- Grondslag: art. 11.7a lid 1 sub a Telecommunicatiewet; AP 'Cookies en uw organisatie'
- Toetspunt: De verklaring noemt de cookies en vergelijkbare technieken, per naam of per categorie
- Tekstsoort: `append_section` · Nodig: cookie_overview

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Welke cookies gebruiken wij
Hieronder staat per cookie of categorie welke cookies wij gebruiken, van welke partij ze zijn, waarvoor ze dienen en hoe lang ze blijven staan.
{{facts.cookie_overview}}
````

#### CK3.2 — Waarvoor je de cookies gebruikt
- Grondslag: art. 11.7a lid 1 sub a Telecommunicatiewet ('in ieder geval over de doeleinden'); art. 13 lid 1 sub c AVG
- Toetspunt: De verklaring noemt het doel per cookie of categorie
- Tekstsoort: `replace` · Nodig: cookie_overview

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Welke cookies gebruiken wij en waarvoor
Hieronder staat per cookie of categorie waarvoor wij hem gebruiken, van welke partij hij is en hoe lang hij blijft staan.
{{facts.cookie_overview}}
````

#### CK3.4 — Hoe lang de cookies blijven staan
- Grondslag: HvJEU C-673/17 Planet49 (werkingsduur van de cookies); art. 13 lid 2 sub a AVG; AP 'Cookies en uw organisatie'
- Toetspunt: De verklaring noemt de looptijd (werkingsduur) per cookie of categorie
- Tekstsoort: `replace` · Nodig: cookie_overview

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Welke cookies gebruiken wij en hoe lang
Hieronder staat per cookie of categorie hoe lang hij blijft staan, van welke partij hij is en waarvoor hij dient.
{{facts.cookie_overview}}
````

### 3. Onderdeel `derden` (standaardkop: Andere partijen)

#### CK3.3 — Welke andere partijen cookies plaatsen of gegevens ontvangen
- Grondslag: art. 13 lid 1 sub e AVG; HvJEU C-673/17 Planet49 (toegang van derden); AP 'Cookies en uw organisatie'
- Toetspunt: De verklaring noemt welke derden cookies plaatsen of de gegevens ontvangen, per doel
- Tekstsoort: `insert` · Nodig: third_parties

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Andere partijen
De volgende partijen plaatsen via onze website cookies of ontvangen gegevens, voor de genoemde doelen:
{{facts.third_parties}}
````

#### CK3.8 — Of gegevens uit cookies buiten Europa terechtkomen
- Grondslag: art. 13 lid 1 sub f AVG
- Toetspunt: Bij doorgifte buiten de EER via cookies van derden: vermelding van de doorgifte en de waarborg, of een duidelijke verwijzing naar de privacyverklaring waarin dit staat
- Tekstsoort: `insert` · Alleen opnemen als: `facts.transfers_outside_eea != false` · Nodig: transfer_details

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Gegevens buiten de Europese Unie
Sommige partijen die via onze website cookies plaatsen, verwerken gegevens buiten de Europese Economische Ruimte: {{facts.transfer_details}}.
````

### 4. Onderdeel `grondslag` (standaardkop: Op welke grond gebruiken wij deze gegevens)

#### CK3.7 — Op welke grond je de gegevens uit cookies gebruikt
- Grondslag: art. 13 lid 1 sub c en lid 2 sub b AVG; art. 21 lid 4 AVG
- Toetspunt: De verklaring noemt de grondslag per categorie (toestemming, of gerechtvaardigd belang met het recht van bezwaar), of verwijst duidelijk naar de privacyverklaring waarin dat staat
- Tekstsoort: `insert` · Alleen opnemen als: `facts.personal_data_via_cookies != false` · Nodig: legal_bases, privacy_statement_link

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Op welke grond gebruiken wij deze gegevens
{{facts.legal_bases}}
Gebruiken wij gegevens op basis van ons gerechtvaardigd belang, dan kun je daartegen bezwaar maken. Meer informatie staat in onze privacyverklaring: {{facts.privacy_statement_link}}.
````

### 5. Onderdeel `toestemming` (standaardkop: Je keuze wijzigen)

#### CK3.5 — Hoe bezoekers hun toestemming kunnen intrekken
- Grondslag: art. 7 lid 3 AVG; art. 13 lid 2 sub c AVG; AP-normuitleg intrekken van toestemming bij cookiebanners
- Toetspunt: De verklaring legt uit hoe de toestemming kan worden ingetrokken en de cookiekeuze kan worden gewijzigd
- Tekstsoort: `insert` · Alleen opnemen als: `facts.uses_consent_cookies != false` · Nodig: withdrawal_instructions

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Je keuze wijzigen
Je kunt je toestemming voor cookies altijd intrekken of je keuze wijzigen: {{facts.withdrawal_instructions}}. Intrekken is gratis en net zo makkelijk als toestemming geven. Het intrekken geldt vanaf dat moment.
````

## Toetspunten (voor de eindcontrole)

### CK3.1 — Welke cookies je gebruikt
- Grondslag: art. 11.7a lid 1 sub a Telecommunicatiewet; AP 'Cookies en uw organisatie'
- Toetspunt: De verklaring noemt de cookies en vergelijkbare technieken, per naam of per categorie
- Bronnen: TW-art11.7a-lid1-a (Telecommunicatiewet art. 11.7a lid 1 sub a); AP-cookies-organisatie (Autoriteit Persoonsgegevens, 'Cookies en uw organisatie: zorg voor een goed beleid'); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten))
- Wat de tekst moet bereiken: Neem in je cookieverklaring een overzicht op van de cookies die je gebruikt, per naam of per categorie.

### CK3.2 — Waarvoor je de cookies gebruikt
- Grondslag: art. 11.7a lid 1 sub a Telecommunicatiewet ('in ieder geval over de doeleinden'); art. 13 lid 1 sub c AVG
- Toetspunt: De verklaring noemt het doel per cookie of categorie
- Bronnen: TW-art11.7a-lid1-a (Telecommunicatiewet art. 11.7a lid 1 sub a); AVG-art13-lid1-c (AVG art. 13 lid 1 sub c); AP-cookies-organisatie (Autoriteit Persoonsgegevens, 'Cookies en uw organisatie: zorg voor een goed beleid')
- Wat de tekst moet bereiken: Vermeld per cookie of categorie concreet waarvoor je hem gebruikt.

### CK3.3 — Welke andere partijen cookies plaatsen of gegevens ontvangen
- Grondslag: art. 13 lid 1 sub e AVG; HvJEU C-673/17 Planet49 (toegang van derden); AP 'Cookies en uw organisatie'
- Toetspunt: De verklaring noemt welke derden cookies plaatsen of de gegevens ontvangen, per doel
- Bronnen: AVG-art13-lid1-e (AVG art. 13 lid 1 sub e); HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); AP-cookies-organisatie (Autoriteit Persoonsgegevens, 'Cookies en uw organisatie: zorg voor een goed beleid')
- Wat de tekst moet bereiken: Noem bij naam welke andere partijen via je website cookies plaatsen of gegevens ontvangen, en voor welk doel.

### CK3.4 — Hoe lang de cookies blijven staan
- Grondslag: HvJEU C-673/17 Planet49 (werkingsduur van de cookies); art. 13 lid 2 sub a AVG; AP 'Cookies en uw organisatie'
- Toetspunt: De verklaring noemt de looptijd (werkingsduur) per cookie of categorie
- Bronnen: HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); AVG-art13-lid2-a (AVG art. 13 lid 2 sub a); AP-cookies-organisatie (Autoriteit Persoonsgegevens, 'Cookies en uw organisatie: zorg voor een goed beleid')
- Wat de tekst moet bereiken: Vermeld per cookie of categorie hoe lang de cookie blijft staan.

### CK3.5 — Hoe bezoekers hun toestemming kunnen intrekken
- Grondslag: art. 7 lid 3 AVG; art. 13 lid 2 sub c AVG; AP-normuitleg intrekken van toestemming bij cookiebanners
- Toetspunt: De verklaring legt uit hoe de toestemming kan worden ingetrokken en de cookiekeuze kan worden gewijzigd
- Alleen als: `facts.uses_consent_cookies != false`
- Bronnen: AVG-art7-lid3 (AVG art. 7 lid 3); AVG-art13-lid2-c (AVG art. 13 lid 2 sub c); AP-normuitleg-intrekken-2024 (Autoriteit Persoonsgegevens, 'Normuitleg intrekken van toestemming bij cookiebanners'); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten))
- Wat de tekst moet bereiken: Leg in je cookieverklaring uit hoe bezoekers hun keuze kunnen wijzigen of hun toestemming kunnen intrekken, bijvoorbeeld via een knop die op elke pagina staat.

### CK3.6 — Wie verantwoordelijk is voor de cookies en hoe bezoekers je bereiken
- Grondslag: art. 11.7a lid 1 sub a Telecommunicatiewet (informatie overeenkomstig de AVG); art. 13 lid 1 sub a AVG
- Toetspunt: De verklaring noemt de naam en contactgegevens van de website-eigenaar, of verwijst duidelijk naar een privacyverklaring waarin die staan
- Bronnen: TW-art11.7a-lid1-a (Telecommunicatiewet art. 11.7a lid 1 sub a); AVG-art13-lid1-a (AVG art. 13 lid 1 sub a); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten))
- Wat de tekst moet bereiken: Vermeld wie verantwoordelijk is voor de cookies op je website en hoe bezoekers je kunnen bereiken, of verwijs duidelijk naar je privacyverklaring.

### CK3.7 — Op welke grond je de gegevens uit cookies gebruikt
- Grondslag: art. 13 lid 1 sub c en lid 2 sub b AVG; art. 21 lid 4 AVG
- Toetspunt: De verklaring noemt de grondslag per categorie (toestemming, of gerechtvaardigd belang met het recht van bezwaar), of verwijst duidelijk naar de privacyverklaring waarin dat staat
- Alleen als: `facts.personal_data_via_cookies != false`
- Bronnen: AVG-art13-lid1-c (AVG art. 13 lid 1 sub c); AVG-art13-lid2-b (AVG art. 13 lid 2 sub b); AVG-art21-lid4 (AVG art. 21 lid 4)
- Wat de tekst moet bereiken: Vermeld per categorie cookies op welke grond je de gegevens gebruikt, en bij gerechtvaardigd belang dat bezoekers bezwaar kunnen maken. Je kunt ook verwijzen naar je privacyverklaring als het daar staat.

### CK3.8 — Of gegevens uit cookies buiten Europa terechtkomen
- Grondslag: art. 13 lid 1 sub f AVG
- Toetspunt: Bij doorgifte buiten de EER via cookies van derden: vermelding van de doorgifte en de waarborg, of een duidelijke verwijzing naar de privacyverklaring waarin dit staat
- Alleen als: `facts.transfers_outside_eea != false`
- Bronnen: AVG-art13-lid1-f (AVG art. 13 lid 1 sub f)
- Wat de tekst moet bereiken: Vermeld dat gegevens uit cookies van andere partijen buiten de Europese Unie terechtkomen, naar welke landen, en op welke basis dat is toegestaan.

### CK3.9 — Of de cookieverklaring makkelijk te vinden en te begrijpen is
- Grondslag: art. 12 lid 1 AVG; art. 7 lid 2 AVG; AP 'Cookies en uw organisatie'
- Toetspunt: De verklaring is goed vindbaar vanaf de banner en elke pagina, en in duidelijke en eenvoudige taal geschreven
- Bronnen: AVG-art12-lid1 (AVG art. 12 lid 1); AP-cookies-organisatie (Autoriteit Persoonsgegevens, 'Cookies en uw organisatie: zorg voor een goed beleid')
- Wat de tekst moet bereiken: Zet een link naar je cookieverklaring in de banner en onderaan elke pagina, en schrijf de verklaring in korte, duidelijke zinnen.

### CK3.10 — Of de verklaring klopt met de cookies die je werkelijk gebruikt
- Grondslag: art. 11.7a lid 1 sub a Telecommunicatiewet ('duidelijke en volledige informatie'); art. 12 lid 1 AVG
- Toetspunt: Elke cookie uit de aangeleverde cookielijst staat, naar naam of categorie, in de verklaring; de verklaring noemt geen categorieën die verzwijgen wat er gebeurt
- Bronnen: TW-art11.7a-lid1-a (Telecommunicatiewet art. 11.7a lid 1 sub a); AVG-art12-lid1 (AVG art. 12 lid 1)
- Wat de tekst moet bereiken: Werk je cookieverklaring bij zodat alle cookies en partijen die je werkelijk gebruikt erin staan. Controleer dit na elke wijziging aan je website.
