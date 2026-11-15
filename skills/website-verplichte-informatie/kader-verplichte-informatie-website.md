# Kader W1 — Verplichte informatie op je website

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of een website de verplichte bedrijfsgegevens vermeldt en, bij online bestellen, de informatie over het bestelproces en de ontvangstbevestiging geeft.

Bronnen: BW3-art15d-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15d lid 1); BW3-art15e-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15e lid 1); BW6-art227b-lid1 (Burgerlijk Wetboek Boek 6 art. 6:227b lid 1); BW6-art227c-lid1 (Burgerlijk Wetboek Boek 6 art. 6:227c lid 1)

## Formulier (vragen aan de gebruiker)

- **business_name**: Wat is de (handels)naam van je onderneming?
  - Label (voor de plek-om-in-te-vullen): naam van je onderneming
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **in_trade_register**: Sta je ingeschreven bij de Kamer van Koophandel?
  - Label (voor de plek-om-in-te-vullen): of je in het handelsregister staat
  - Type: boolean
- **has_vat_number**: Heb je een btw-identificatienummer voor activiteiten waarvoor je btw rekent?
  - Label (voor de plek-om-in-te-vullen): of je een btw-identificatienummer hebt
  - Type: boolean
- **licensed**: Heb je voor je activiteiten een vergunning van een toezichthouder nodig (bijvoorbeeld financiële diensten)?
  - Label (voor de plek-om-in-te-vullen): of je een vergunning nodig hebt
  - Type: boolean
- **regulated_profession**: Oefen je een gereglementeerd beroep uit (bijvoorbeeld advocaat, notaris, arts, accountant)?
  - Label (voor de plek-om-in-te-vullen): of je een gereglementeerd beroep uitoefent
  - Type: boolean
- **sells_online**: Kunnen klanten via je website of app bestellen of een overeenkomst sluiten?
  - Label (voor de plek-om-in-te-vullen): of klanten online een overeenkomst sluiten
  - Type: boolean
- **confirms_receipt**: Krijgt de klant direct een bevestiging dat je zijn bestelling hebt ontvangen?
  - Label (voor de plek-om-in-te-vullen): of je de ontvangst van een bestelling bevestigt
  - Type: boolean · Alleen vragen als: `facts.sells_online != false`
- **address**: Wat is je vestigingsadres?
  - Label (voor de plek-om-in-te-vullen): het vestigingsadres
  - Type: text
- **email**: Op welk e-mailadres ben je bereikbaar?
  - Label (voor de plek-om-in-te-vullen): het e-mailadres
  - Type: text
- **kvk_number**: Wat is je KvK-nummer?
  - Label (voor de plek-om-in-te-vullen): het KvK-nummer
  - Type: text
- **vat_number**: Wat is je btw-identificatienummer?
  - Label (voor de plek-om-in-te-vullen): het btw-identificatienummer
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `gegevens` (standaardkop: gegevens)

#### W1.1 — Of je naam op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: De website vermeldt de naam van de onderneming
- Tekstsoort: `append_section` · Nodig: business_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Bedrijfsgegevens
{{facts.business_name}}
````

#### W1.2 — Of je adres op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: De website vermeldt het geografische adres waar de onderneming is gevestigd (geen postbus)
- Tekstsoort: `append_section` · Nodig: address

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Adres: {{facts.address}}
````

#### W1.3 — Of je snel bereikbaar bent, ook per e-mail
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: De website vermeldt gegevens waarmee snel en rechtstreeks contact kan worden opgenomen, waaronder een e-mailadres
- Tekstsoort: `append_section` · Nodig: email

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
E-mail: {{facts.email}}
````

### 2. Onderdeel `registratie` (standaardkop: registratie)

#### W1.4 — Of je KvK-inschrijving op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: Staat de onderneming in een handelsregister, dan vermeldt de website dat register en het inschrijvingsnummer
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.in_trade_register != false` · Nodig: kvk_number

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
KvK-nummer: {{facts.kvk_number}}
````

#### W1.5 — Of je btw-identificatienummer op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: Verricht de onderneming btw-plichtige activiteiten, dan vermeldt de website het btw-identificatienummer
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.has_vat_number != false` · Nodig: vat_number

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Btw-identificatienummer: {{facts.vat_number}}
````

### 3. Onderdeel `toezicht` (standaardkop: toezicht)

#### W1.6 — Of je toezichthouder op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: Is voor de activiteit een vergunning nodig, dan vermeldt de website de gegevens van de toezichthoudende autoriteit
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.licensed != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Vergunning en toezicht: [IN TE VULLEN: toezichthouder en vergunningnummer].
````

#### W1.7 — Of je beroepsgegevens op de website staan
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: Bij een gereglementeerd beroep vermeldt de website de beroepsorganisatie, de beroepstitel en het land waar die is toegekend, en de beroepsregels of waar die te vinden zijn
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.regulated_profession != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Beroep: [IN TE VULLEN: beroepsorganisatie, beroepstitel en waar de beroepsregels te vinden zijn].
````

### 4. Onderdeel `bestellen` (standaardkop: bestellen)

#### W1.8 — Of het bestelproces wordt uitgelegd
- Grondslag: art. 6:227b lid 1 BW
- Toetspunt: Vóór het sluiten van een elektronische overeenkomst informeert de website over de technische stappen, of en waar de overeenkomst wordt opgeslagen, hoe invoerfouten kunnen worden hersteld en in welke talen de overeenkomst kan worden gesloten
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.sells_online != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Zo bestel je
Je kiest een product, controleert je bestelling in het overzicht en kunt daar fouten herstellen voordat je de bestelling plaatst. Na het plaatsen ontvang je een bevestiging per e-mail. Wij bewaren je bestelling en je kunt die terugvinden in [IN TE VULLEN: waar]. Bestellen kan in het Nederlands.
````

## Toetspunten (voor de eindcontrole)

### W1.1 — Of je naam op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: De website vermeldt de naam van de onderneming
- Bronnen: BW3-art15d-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15d lid 1)
- Wat de tekst moet bereiken: Vermeld de naam van je onderneming.

### W1.2 — Of je adres op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: De website vermeldt het geografische adres waar de onderneming is gevestigd (geen postbus)
- Bronnen: BW3-art15d-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15d lid 1)
- Wat de tekst moet bereiken: Vermeld je vestigingsadres (geen postbus).

### W1.3 — Of je snel bereikbaar bent, ook per e-mail
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: De website vermeldt gegevens waarmee snel en rechtstreeks contact kan worden opgenomen, waaronder een e-mailadres
- Bronnen: BW3-art15d-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15d lid 1)
- Wat de tekst moet bereiken: Vermeld een e-mailadres waarop je bereikbaar bent.

### W1.4 — Of je KvK-inschrijving op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: Staat de onderneming in een handelsregister, dan vermeldt de website dat register en het inschrijvingsnummer
- Alleen als: `facts.in_trade_register != false`
- Bronnen: BW3-art15d-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15d lid 1)
- Wat de tekst moet bereiken: Vermeld je KvK-nummer.

### W1.5 — Of je btw-identificatienummer op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: Verricht de onderneming btw-plichtige activiteiten, dan vermeldt de website het btw-identificatienummer
- Alleen als: `facts.has_vat_number != false`
- Bronnen: BW3-art15d-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15d lid 1)
- Wat de tekst moet bereiken: Vermeld je btw-identificatienummer.

### W1.6 — Of je toezichthouder op de website staat
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: Is voor de activiteit een vergunning nodig, dan vermeldt de website de gegevens van de toezichthoudende autoriteit
- Alleen als: `facts.licensed != false`
- Bronnen: BW3-art15d-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15d lid 1)
- Wat de tekst moet bereiken: Vermeld bij welke toezichthouder je een vergunning hebt.

### W1.7 — Of je beroepsgegevens op de website staan
- Grondslag: art. 3:15d lid 1 BW
- Toetspunt: Bij een gereglementeerd beroep vermeldt de website de beroepsorganisatie, de beroepstitel en het land waar die is toegekend, en de beroepsregels of waar die te vinden zijn
- Alleen als: `facts.regulated_profession != false`
- Bronnen: BW3-art15d-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15d lid 1)
- Wat de tekst moet bereiken: Vermeld je beroepsorganisatie, beroepstitel en waar de beroepsregels te vinden zijn.

### W1.8 — Of het bestelproces wordt uitgelegd
- Grondslag: art. 6:227b lid 1 BW
- Toetspunt: Vóór het sluiten van een elektronische overeenkomst informeert de website over de technische stappen, of en waar de overeenkomst wordt opgeslagen, hoe invoerfouten kunnen worden hersteld en in welke talen de overeenkomst kan worden gesloten
- Alleen als: `facts.sells_online != false`
- Bronnen: BW6-art227b-lid1 (Burgerlijk Wetboek Boek 6 art. 6:227b lid 1)
- Wat de tekst moet bereiken: Leg uit hoe bestellen werkt, hoe de klant fouten herstelt, of de overeenkomst wordt bewaard en in welke talen.

### W1.9 — Of je de ontvangst van een bestelling bevestigt
- Grondslag: art. 6:227c BW
- Toetspunt: Bij een elektronisch gesloten overeenkomst bevestigt de dienstverlener langs elektronische weg zo spoedig mogelijk de ontvangst van de aanvaarding
- Alleen als: `facts.sells_online != false`
- Bronnen: BW6-art227c-lid1 (Burgerlijk Wetboek Boek 6 art. 6:227c lid 1)
- Wat de tekst moet bereiken: Stuur direct na een bestelling automatisch een ontvangstbevestiging.

### W1.10 — Of reclame herkenbaar is
- Grondslag: art. 3:15e BW
- Toetspunt: Commerciële communicatie (zoals aanbiedingen en nieuwsbrieven) is als zodanig herkenbaar en noemt van wie zij komt; voorwaarden van acties zijn gemakkelijk te vinden
- Bronnen: BW3-art15e-lid1 (Burgerlijk Wetboek Boek 3 art. 3:15e lid 1)
- Wat de tekst moet bereiken: Maak reclame herkenbaar en zet de voorwaarden van acties erbij.
