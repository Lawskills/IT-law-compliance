# Kader C4 — Softwarelicentie / EULA

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of een softwarelicentie de omvang van het gebruiksrecht duidelijk regelt, de dwingende rechten van de gebruiker uit de Auteurswet (reservekopie, observeren en testen, decompilatie voor interoperabiliteit) niet uitsluit, bij consumenten de wettelijke rechten voor digitale inhoud niet beperkt, en de gebruikelijke onderdelen regelt.

Bronnen: AW-art45i (Auteurswet art. 45i); AW-art45k (Auteurswet art. 45k); AW-art45l (Auteurswet art. 45l); AW-art45m (Auteurswet art. 45m); BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); BW7-art50aa (Burgerlijk Wetboek Boek 7 art. 7:50aa)

## Formulier (vragen aan de gebruiker)

- **licensor_name**: Wie geeft de licentie?
  - Label (voor de plek-om-in-te-vullen): naam van de licentiegever
  - Type: text
- **licensee_name**: Wie krijgt de licentie?
  - Label (voor de plek-om-in-te-vullen): naam van de licentienemer
  - Type: text
- **software_name**: Om welke software gaat het?
  - Label (voor de plek-om-in-te-vullen): welke software
  - Type: text
- **audience**: Is de licentienemer een bedrijf of een consument?
  - Label (voor de plek-om-in-te-vullen): met wie je de licentie sluit
  - Type: enum (business / consumer / both)
- **license_scope**: Hoeveel gebruikers of installaties, voor welke duur en voor welk gebied geldt de licentie?
  - Label (voor de plek-om-in-te-vullen): de omvang van het gebruiksrecht
  - Type: text
- **updates_terms**: Welke updates en welk onderhoud krijgt de licentienemer, en hoe lang?
  - Label (voor de plek-om-in-te-vullen): de afspraken over updates
  - Type: text
- **liability_cap**: Tot welk bedrag of welke grens is de licentiegever aansprakelijk?
  - Label (voor de plek-om-in-te-vullen): de grens van de aansprakelijkheid
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `licentie` (standaardkop: licentie)

#### C4.1 — Wat de licentienemer met de software mag
- Grondslag: goede praktijk; art. 45i Auteurswet (toestemming van de rechthebbende) als achtergrond
- Toetspunt: De licentie beschrijft de omvang van het gebruiksrecht: aantal gebruikers of installaties, duur, gebied en doel
- Tekstsoort: `append_section` · Nodig: software_name, license_scope

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Licentie
Licentiegever verleent Licentienemer een niet-exclusief recht om {{facts.software_name}} te gebruiken, met deze omvang: {{facts.license_scope}}.
````

### 2. Onderdeel `overdracht` (standaardkop: overdracht)

#### C4.2 — Of overdracht en sublicenties zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De licentie regelt of de licentie overdraagbaar is en of sublicenties zijn toegestaan
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Overdracht
Licentienemer mag de licentie niet overdragen en geen sublicenties verlenen zonder voorafgaande schriftelijke toestemming van Licentiegever.
````

### 3. Onderdeel `updates` (standaardkop: updates)

#### C4.4 — Of updates en onderhoud zijn geregeld
- Grondslag: goede praktijk; titel 7.1A BW (updates bij consumenten) als achtergrond
- Toetspunt: De licentie regelt welke updates en welk onderhoud de licentienemer krijgt en hoe lang
- Tekstsoort: `append_section` · Nodig: updates_terms

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Updates en onderhoud
{{facts.updates_terms}}
````

### 4. Onderdeel `garantie` (standaardkop: garantie)

#### C4.6 — Of garantie en gebreken zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De licentie regelt wat er gebeurt bij gebreken in de software
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Gebreken
Licentiegever spant zich in gebreken die Licentienemer meldt binnen een redelijke termijn te herstellen. Voor consumenten gelden daarnaast de wettelijke rechten.
````

### 5. Onderdeel `opensource` (standaardkop: opensource)

#### C4.7 — Of open-sourceonderdelen worden genoemd
- Grondslag: goede praktijk
- Toetspunt: De licentie noemt open-sourceonderdelen en hun licenties, of verwijst naar een overzicht
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Open source
De software kan open-sourceonderdelen bevatten. Daarvoor gelden de licenties in het overzicht dat Licentiegever bij de software levert.
````

### 6. Onderdeel `aansprakelijkheid` (standaardkop: aansprakelijkheid)

#### C4.8 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 6:233 onder a BW als achtergrond
- Toetspunt: De licentie regelt de aansprakelijkheid van de licentiegever
- Tekstsoort: `append_section` · Nodig: liability_cap

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Aansprakelijkheid
De aansprakelijkheid van Licentiegever is beperkt tot {{facts.liability_cap}}, behalve bij opzet of bewuste roekeloosheid.
````

### 7. Onderdeel `einde` (standaardkop: Einde van de verwerking)

#### C4.9 — Wat er gebeurt als de licentie eindigt
- Grondslag: goede praktijk
- Toetspunt: De licentie regelt wanneer zij eindigt en wat de licentienemer dan moet doen
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Einde van de licentie
Bij het einde van de licentie stopt Licentienemer met het gebruik van de software en verwijdert hij de geïnstalleerde exemplaren.
````

### 8. Onderdeel `recht` (standaardkop: recht)

#### C4.10 — Of toepasselijk recht is geregeld
- Grondslag: goede praktijk
- Toetspunt: De licentie regelt het toepasselijk recht en de bevoegde rechter
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Toepasselijk recht
Op deze licentie is Nederlands recht van toepassing.
````

## Toetspunten (voor de eindcontrole)

### C4.1 — Wat de licentienemer met de software mag
- Grondslag: goede praktijk; art. 45i Auteurswet (toestemming van de rechthebbende) als achtergrond
- Toetspunt: De licentie beschrijft de omvang van het gebruiksrecht: aantal gebruikers of installaties, duur, gebied en doel
- Bronnen: AW-art45i (Auteurswet art. 45i)
- Wat de tekst moet bereiken: Beschrijf hoeveel gebruikers of installaties, voor welke duur en waarvoor de software mag worden gebruikt.

### C4.2 — Of overdracht en sublicenties zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De licentie regelt of de licentie overdraagbaar is en of sublicenties zijn toegestaan
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Leg vast of de licentie mag worden overgedragen en of sublicenties zijn toegestaan.

### C4.3 — Of de dwingende rechten van de gebruiker niet worden uitgesloten
- Grondslag: art. 45k, 45l en 45m Auteurswet (dwingend)
- Toetspunt: De licentie sluit niet uit dat de rechtmatige verkrijger een reservekopie maakt voor zover nodig voor het beoogde gebruik, de werking observeert en test om de onderliggende ideeën vast te stellen, en decompileert voor zover nodig voor interoperabiliteit onder de voorwaarden van de wet
- Bronnen: AW-art45k (Auteurswet art. 45k); AW-art45l (Auteurswet art. 45l); AW-art45m (Auteurswet art. 45m)
- Wat de tekst moet bereiken: Maak een uitzondering op het kopieer- en decompilatieverbod voor wat de Auteurswet de gebruiker dwingend toestaat (reservekopie, observeren en testen, decompilatie voor interoperabiliteit).

### C4.4 — Of updates en onderhoud zijn geregeld
- Grondslag: goede praktijk; titel 7.1A BW (updates bij consumenten) als achtergrond
- Toetspunt: De licentie regelt welke updates en welk onderhoud de licentienemer krijgt en hoe lang
- Bronnen: BW7-art50aa (Burgerlijk Wetboek Boek 7 art. 7:50aa)
- Wat de tekst moet bereiken: Leg vast welke updates en welk onderhoud de licentienemer krijgt, en hoe lang.

### C4.5 — Of de wettelijke rechten van consumenten bij digitale inhoud niet worden beperkt
- Grondslag: art. 7:50aa e.v. BW
- Toetspunt: Bij consumenten beperkt de licentie de dwingende rechten van titel 7.1A BW niet (conformiteit, updates, rechten bij gebreken)
- Alleen als: `facts.audience != "business"`
- Bronnen: BW7-art50aa (Burgerlijk Wetboek Boek 7 art. 7:50aa)
- Wat de tekst moet bereiken: Beperk de wettelijke rechten van consumenten bij gebreken en updates niet.

### C4.6 — Of garantie en gebreken zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De licentie regelt wat er gebeurt bij gebreken in de software
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Leg vast wat er gebeurt als de software gebreken heeft.

### C4.7 — Of open-sourceonderdelen worden genoemd
- Grondslag: goede praktijk
- Toetspunt: De licentie noemt open-sourceonderdelen en hun licenties, of verwijst naar een overzicht
- Bronnen: AW-art45i (Auteurswet art. 45i)
- Wat de tekst moet bereiken: Noem de open-sourceonderdelen en hun licenties, of verwijs naar een overzicht.

### C4.8 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 6:233 onder a BW als achtergrond
- Toetspunt: De licentie regelt de aansprakelijkheid van de licentiegever
- Bronnen: BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a)
- Wat de tekst moet bereiken: Leg de aansprakelijkheid vast, zonder opzet en bewuste roekeloosheid uit te sluiten.

### C4.9 — Wat er gebeurt als de licentie eindigt
- Grondslag: goede praktijk
- Toetspunt: De licentie regelt wanneer zij eindigt en wat de licentienemer dan moet doen
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Leg vast wanneer de licentie eindigt en wat de licentienemer dan moet doen.

### C4.10 — Of toepasselijk recht is geregeld
- Grondslag: goede praktijk
- Toetspunt: De licentie regelt het toepasselijk recht en de bevoegde rechter
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Leg toepasselijk recht en de bevoegde rechter vast.
