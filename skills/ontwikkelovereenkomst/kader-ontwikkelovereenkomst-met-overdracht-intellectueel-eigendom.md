# Kader C6 — Ontwikkelovereenkomst met overdracht van intellectueel eigendom

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of een ontwikkelovereenkomst het werk, de oplevering en acceptatie regelt, de rechten op het resultaat geldig overdraagt (akte) of een passende licentie geeft, en de gebruikelijke onderdelen regelt.

Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); AW-art2-lid2 (Auteurswet art. 2 lid 2); AW-art25 (Auteurswet art. 25); AW-art45i (Auteurswet art. 45i); BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a); BW7-art400 (Burgerlijk Wetboek Boek 7 art. 7:400); BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)

## Formulier (vragen aan de gebruiker)

- **developer_name**: Wie ontwikkelt het werk?
  - Label (voor de plek-om-in-te-vullen): naam van de ontwikkelaar
  - Type: text
- **client_name**: Voor wie wordt het ontwikkeld?
  - Label (voor de plek-om-in-te-vullen): naam van de opdrachtgever
  - Type: text
- **project_name**: Wat wordt er ontwikkeld?
  - Label (voor de plek-om-in-te-vullen): het project
  - Type: text
- **ip_transfer_intended**: Moeten de rechten op het resultaat (zoals auteursrecht op de code) naar de opdrachtgever gaan?
  - Label (voor de plek-om-in-te-vullen): of de rechten naar de opdrachtgever moeten gaan
  - Type: boolean
- **personal_data_access**: Krijgt de ontwikkelaar toegang tot persoonsgegevens van de opdrachtgever (bijvoorbeeld testdata of productie)?
  - Label (voor de plek-om-in-te-vullen): of de ontwikkelaar toegang krijgt tot persoonsgegevens
  - Type: boolean
- **acceptance_period**: Binnen hoeveel dagen test de opdrachtgever een oplevering?
  - Label (voor de plek-om-in-te-vullen): de acceptatietermijn
  - Type: text
- **liability_cap**: Tot welk bedrag of welke grens is de ontwikkelaar aansprakelijk?
  - Label (voor de plek-om-in-te-vullen): de grens van de aansprakelijkheid
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `opdracht` (standaardkop: opdracht)

#### C6.1 — Wat er wordt ontwikkeld
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: De overeenkomst beschrijft het werk, de specificaties en de planning
- Tekstsoort: `append_section` · Nodig: project_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Opdracht
Opdrachtnemer ontwikkelt voor Opdrachtgever {{facts.project_name}}, volgens de specificaties in de bijlage bij deze overeenkomst.
````

### 2. Onderdeel `overdracht` (standaardkop: overdracht)

#### C6.3 — Of de overdracht in de tekst staat
- Grondslag: art. 2 lid 2 Auteurswet
- Toetspunt: De overeenkomst bevat een overdrachtsbepaling die alle rechten op het resultaat overdraagt
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.ip_transfer_intended != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Overdracht van rechten
1. Opdrachtnemer draagt hierbij aan Opdrachtgever over, die hierbij aanvaardt, alle rechten van intellectueel eigendom op de resultaten van de opdracht, waaronder het auteursrecht op de programmatuur, de broncode en de documentatie, zodra die rechten ontstaan.
2. Voor zover een nadere akte nodig is, werkt Opdrachtnemer daaraan op eerste verzoek mee.
````

### 3. Onderdeel `licentie` (standaardkop: licentie)

#### C6.4 — Of er een licentie is als de rechten niet overgaan
- Grondslag: goede praktijk; art. 45i Auteurswet als achtergrond
- Toetspunt: Blijven de rechten bij de ontwikkelaar, dan regelt de overeenkomst een gebruiksrecht voor de opdrachtgever
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.ip_transfer_intended != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Gebruiksrecht
De rechten op de resultaten blijven bij Opdrachtnemer. Opdrachtgever krijgt een eeuwigdurend, niet-exclusief recht om de resultaten te gebruiken en te laten aanpassen voor zijn eigen bedrijfsvoering.
````

### 4. Onderdeel `persoonlijkheid` (standaardkop: persoonlijkheid)

#### C6.5 — Of persoonlijkheidsrechten zijn geregeld
- Grondslag: goede praktijk; art. 25 Auteurswet
- Toetspunt: De overeenkomst regelt de persoonlijkheidsrechten van de maker, voor zover de wet toestaat daar afstand van te doen
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.ip_transfer_intended != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Persoonlijkheidsrechten
Opdrachtnemer doet, voor zover de wet dat toestaat, afstand van zijn persoonlijkheidsrechten op de resultaten, zodat Opdrachtgever die zonder naamsvermelding mag gebruiken en wijzigen.
````

### 5. Onderdeel `oplevering` (standaardkop: oplevering)

#### C6.6 — Of broncode en documentatie worden opgeleverd
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: De overeenkomst regelt de oplevering van de broncode en documentatie
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Oplevering
Opdrachtnemer levert bij elke oplevering de broncode, de documentatie en wat nodig is om de programmatuur te installeren en te onderhouden.
````

### 6. Onderdeel `acceptatie` (standaardkop: acceptatie)

#### C6.7 — Of acceptatie is geregeld
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: De overeenkomst regelt hoe en binnen welke termijn de opdrachtgever een oplevering test en accepteert
- Tekstsoort: `append_section` · Nodig: acceptance_period

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Acceptatie
Opdrachtgever test een oplevering binnen {{facts.acceptance_period}}. Gebreken meldt hij gemotiveerd; Opdrachtnemer herstelt ze en levert opnieuw op.
````

### 7. Onderdeel `derden` (standaardkop: Andere partijen)

#### C6.8 — Of rechten van derden en open source zijn geregeld
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: De overeenkomst regelt het gebruik van onderdelen van derden en open source, en een vrijwaring voor inbreuk op rechten van derden
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Rechten van derden
Opdrachtnemer gebruikt onderdelen van derden of open source alleen na melding aan Opdrachtgever en met licenties die het beoogde gebruik toelaten. Opdrachtnemer vrijwaart Opdrachtgever voor aanspraken van derden wegens inbreuk door de opgeleverde resultaten.
````

### 8. Onderdeel `geheimhouding` (standaardkop: Geheimhouding)

#### C6.9 — Of geheimhouding is geregeld
- Grondslag: goede praktijk; art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst regelt geheimhouding van vertrouwelijke informatie
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Geheimhouding
Partijen houden vertrouwelijke informatie van de ander geheim en gebruiken die alleen voor de opdracht.
````

### 9. Onderdeel `privacy` (standaardkop: privacy)

#### C6.10 — Of er een verwerkersovereenkomst is
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Krijgt de ontwikkelaar toegang tot persoonsgegevens, dan regelt of verwijst de overeenkomst naar een verwerkersovereenkomst volgens art. 28 lid 3 AVG
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.personal_data_access != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Persoonsgegevens
Krijgt Opdrachtnemer toegang tot persoonsgegevens, dan sluiten partijen een verwerkersovereenkomst die voldoet aan artikel 28 lid 3 AVG.
````

### 10. Onderdeel `escrow` (standaardkop: escrow)

#### C6.11 — Of escrow is geregeld als de rechten bij de ontwikkelaar blijven
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: Blijven de rechten en de broncode bij de ontwikkelaar, dan regelt de overeenkomst toegang tot de broncode bij faillissement of stoppen (escrow)
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.ip_transfer_intended != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Broncode-escrow
Opdrachtnemer deponeert de broncode bij een escrowagent. Bij faillissement of het staken van het onderhoud krijgt Opdrachtgever toegang tot de broncode.
````

### 11. Onderdeel `aansprakelijkheid` (standaardkop: aansprakelijkheid)

#### C6.12 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 6:233 onder a BW als achtergrond
- Toetspunt: De overeenkomst regelt de aansprakelijkheid
- Tekstsoort: `append_section` · Nodig: liability_cap

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Aansprakelijkheid
De aansprakelijkheid van Opdrachtnemer is beperkt tot {{facts.liability_cap}}, behalve bij opzet of bewuste roekeloosheid.
````

## Toetspunten (voor de eindcontrole)

### C6.1 — Wat er wordt ontwikkeld
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: De overeenkomst beschrijft het werk, de specificaties en de planning
- Bronnen: BW7-art400 (Burgerlijk Wetboek Boek 7 art. 7:400); BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401)
- Wat de tekst moet bereiken: Beschrijf wat er wordt ontwikkeld en verwijs naar de specificaties.

### C6.2 — Of de rechten geldig naar de opdrachtgever gaan
- Grondslag: art. 2 lid 2 Auteurswet
- Toetspunt: Moeten de rechten naar de opdrachtgever, dan worden zij geleverd bij een daartoe bestemde akte (een door beide partijen ondertekend geschrift waarin de rechten worden overgedragen); alleen de in de akte vermelde bevoegdheden of wat uit de aard of strekking van de titel noodzakelijk voortvloeit, gaan over
- Alleen als: `facts.ip_transfer_intended != false`
- Bronnen: AW-art2-lid2 (Auteurswet art. 2 lid 2)
- Wat de tekst moet bereiken: Neem een overdracht op in de ondertekende overeenkomst zelf ("Opdrachtnemer draagt hierbij over aan Opdrachtgever ..."), met een opsomming van de rechten, of maak een aparte akte van overdracht.

### C6.3 — Of de overdracht in de tekst staat
- Grondslag: art. 2 lid 2 Auteurswet
- Toetspunt: De overeenkomst bevat een overdrachtsbepaling die alle rechten op het resultaat overdraagt
- Alleen als: `facts.ip_transfer_intended != false`
- Bronnen: AW-art2-lid2 (Auteurswet art. 2 lid 2)
- Wat de tekst moet bereiken: Neem een overdrachtsbepaling op.

### C6.4 — Of er een licentie is als de rechten niet overgaan
- Grondslag: goede praktijk; art. 45i Auteurswet als achtergrond
- Toetspunt: Blijven de rechten bij de ontwikkelaar, dan regelt de overeenkomst een gebruiksrecht voor de opdrachtgever
- Alleen als: `facts.ip_transfer_intended != true`
- Bronnen: AW-art45i (Auteurswet art. 45i)
- Wat de tekst moet bereiken: Regel een licentie voor de opdrachtgever als de rechten bij de ontwikkelaar blijven.

### C6.5 — Of persoonlijkheidsrechten zijn geregeld
- Grondslag: goede praktijk; art. 25 Auteurswet
- Toetspunt: De overeenkomst regelt de persoonlijkheidsrechten van de maker, voor zover de wet toestaat daar afstand van te doen
- Alleen als: `facts.ip_transfer_intended != false`
- Bronnen: AW-art25 (Auteurswet art. 25)
- Wat de tekst moet bereiken: Regel de persoonlijkheidsrechten, voor zover de wet afstand toestaat.

### C6.6 — Of broncode en documentatie worden opgeleverd
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: De overeenkomst regelt de oplevering van de broncode en documentatie
- Bronnen: BW7-art400 (Burgerlijk Wetboek Boek 7 art. 7:400); BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401)
- Wat de tekst moet bereiken: Leg vast dat de broncode en documentatie worden opgeleverd.

### C6.7 — Of acceptatie is geregeld
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: De overeenkomst regelt hoe en binnen welke termijn de opdrachtgever een oplevering test en accepteert
- Bronnen: BW7-art400 (Burgerlijk Wetboek Boek 7 art. 7:400); BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401)
- Wat de tekst moet bereiken: Leg een acceptatieprocedure met termijn vast.

### C6.8 — Of rechten van derden en open source zijn geregeld
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: De overeenkomst regelt het gebruik van onderdelen van derden en open source, en een vrijwaring voor inbreuk op rechten van derden
- Bronnen: BW7-art400 (Burgerlijk Wetboek Boek 7 art. 7:400); BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401)
- Wat de tekst moet bereiken: Regel onderdelen van derden en open source, en een vrijwaring voor inbreuk op rechten van derden.

### C6.9 — Of geheimhouding is geregeld
- Grondslag: goede praktijk; art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst regelt geheimhouding van vertrouwelijke informatie
- Bronnen: WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)
- Wat de tekst moet bereiken: Regel geheimhouding van vertrouwelijke informatie.

### C6.10 — Of er een verwerkersovereenkomst is
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Krijgt de ontwikkelaar toegang tot persoonsgegevens, dan regelt of verwijst de overeenkomst naar een verwerkersovereenkomst volgens art. 28 lid 3 AVG
- Alleen als: `facts.personal_data_access != false`
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3)
- Wat de tekst moet bereiken: Sluit een verwerkersovereenkomst als de ontwikkelaar persoonsgegevens kan inzien.

### C6.11 — Of escrow is geregeld als de rechten bij de ontwikkelaar blijven
- Grondslag: goede praktijk; art. 7:400 en 7:401 BW als achtergrond
- Toetspunt: Blijven de rechten en de broncode bij de ontwikkelaar, dan regelt de overeenkomst toegang tot de broncode bij faillissement of stoppen (escrow)
- Alleen als: `facts.ip_transfer_intended != true`
- Bronnen: BW7-art400 (Burgerlijk Wetboek Boek 7 art. 7:400); BW7-art401 (Burgerlijk Wetboek Boek 7 art. 7:401)
- Wat de tekst moet bereiken: Overweeg escrow van de broncode als de rechten bij de ontwikkelaar blijven.

### C6.12 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 6:233 onder a BW als achtergrond
- Toetspunt: De overeenkomst regelt de aansprakelijkheid
- Bronnen: BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a)
- Wat de tekst moet bereiken: Leg de aansprakelijkheid vast, zonder opzet en bewuste roekeloosheid uit te sluiten.
