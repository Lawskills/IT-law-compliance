# Kader K13b — Standaardcontractbepalingen voor doorgifte (document)

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een set standaardcontractbepalingen de juiste module gebruikt, ongewijzigd is, de keuzes in clausule 9, 17 en 18 bevat, volledig ingevulde bijlagen heeft en of de doorgiftetoets van clausule 14 is gedaan.

Bronnen: AVG-art46-lid2-c (AVG art. 46 lid 2 sub c); SCC-clausule1 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 1); SCC-clausule13 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 13); SCC-clausule14-b (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub b); SCC-clausule14-d (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub d); SCC-clausule17 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 17); SCC-clausule18 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 18); SCC-clausule2 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 2); SCC-clausule5 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 5); SCC-clausule6 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 6); SCC-clausule8 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 8); SCC-clausule9-a (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 9 sub a)

## Formulier (vragen aan de gebruiker)

- **module**: Wie geeft door aan wie?
  - Label (voor de plek-om-in-te-vullen): welke module bij jullie rollen past
  - Type: enum (c2c / c2p / p2p / p2c)
- **subprocessor_option**: Is voor subverwerkers specifieke voorafgaande toestemming (optie 1) of algemene schriftelijke toestemming (optie 2) gekozen?
  - Label (voor de plek-om-in-te-vullen): de keuze in clausule 9
  - Type: enum (specific / general) · Alleen vragen als: `facts.module != "c2c" and facts.module != "p2c"`
- **tia_done**: Heb je de doorgiftetoets (de beoordeling van de wetgeving en praktijk in het land van de ontvanger) gedaan en vastgelegd?
  - Label (voor de plek-om-in-te-vullen): of de doorgiftetoets is gedaan
  - Type: boolean
- **exporter_name**: Wie geeft de gegevens door (exporteur)?
  - Label (voor de plek-om-in-te-vullen): naam van de gegevensexporteur
  - Type: text
- **importer_name**: Wie ontvangt de gegevens (importeur), en in welk land?
  - Label (voor de plek-om-in-te-vullen): naam van de gegevensimporteur
  - Type: text
- **transfer_description**: Welke gegevens van wie worden doorgegeven, waarvoor, hoe vaak en hoe lang worden ze bewaard?
  - Label (voor de plek-om-in-te-vullen): beschrijving van de doorgifte
  - Type: text
- **supervisory_authority**: Welke toezichthouder is bevoegd (meestal de Autoriteit Persoonsgegevens)?
  - Label (voor de plek-om-in-te-vullen): de bevoegde toezichthouder
  - Type: text
- **toms**: Welke beveiligingsmaatregelen neemt de importeur?
  - Label (voor de plek-om-in-te-vullen): de technische en organisatorische maatregelen
  - Type: text
- **subprocessors_list**: Welke subverwerkers zijn goedgekeurd (naam, land, taak)?
  - Label (voor de plek-om-in-te-vullen): de lijst van subverwerkers
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `bijlage1a` (standaardkop: bijlage1a)

#### K13b.3 — Of bijlage I.A (partijen) is ingevuld
- Grondslag: clausule 6 en bijlage I.A
- Toetspunt: Bijlage I.A noemt de partijen met naam, adres, contactpersoon, activiteiten en rol
- Tekstsoort: `append_section` · Nodig: exporter_name, importer_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Gegevensexporteur: {{facts.exporter_name}}
Gegevensimporteur: {{facts.importer_name}}
Van elke partij: adres, contactpersoon, activiteiten in verband met de doorgifte, rol, ondertekening en datum: [IN TE VULLEN].
````

### 2. Onderdeel `bijlage1b` (standaardkop: bijlage1b)

#### K13b.4 — Of bijlage I.B (beschrijving) is ingevuld
- Grondslag: clausule 6 en bijlage I.B
- Toetspunt: Bijlage I.B beschrijft de categorieën betrokkenen en gegevens, gevoelige gegevens, frequentie, aard en doel van de doorgifte, bewaartermijn en (bij doorgifte aan subverwerkers) onderwerp en duur
- Tekstsoort: `append_section` · Nodig: transfer_description

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
{{facts.transfer_description}}
````

### 3. Onderdeel `bijlage1c` (standaardkop: bijlage1c)

#### K13b.5 — Of bijlage I.C (toezichthouder) is ingevuld
- Grondslag: clausule 13 en bijlage I.C
- Toetspunt: Bijlage I.C noemt de bevoegde toezichthoudende autoriteit volgens clausule 13
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.module != "p2c"` · Nodig: supervisory_authority

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Bevoegde toezichthoudende autoriteit: {{facts.supervisory_authority}}.
````

### 4. Onderdeel `bijlage2` (standaardkop: bijlage2)

#### K13b.6 — Of bijlage II (maatregelen) specifiek is ingevuld
- Grondslag: clausule 8 en bijlage II
- Toetspunt: Bijlage II beschrijft de technische en organisatorische maatregelen van de importeur specifiek, niet in algemene termen
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.module != "p2c"` · Nodig: toms

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
{{facts.toms}}
````

### 5. Onderdeel `bijlage3` (standaardkop: bijlage3)

#### K13b.8 — Of bijlage III (subverwerkers) is ingevuld
- Grondslag: clausule 9 sub a en bijlage III
- Toetspunt: Bij specifieke toestemming bevat bijlage III de lijst van goedgekeurde subverwerkers
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.module != "c2c" and facts.module != "p2c" and facts.subprocessor_option != "general"` · Nodig: subprocessors_list

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
{{facts.subprocessors_list}}
````

## Toetspunten (voor de eindcontrole)

### K13b.1 — Of de juiste module is gebruikt
- Grondslag: clausule 1 en de modules van Uitvoeringsbesluit (EU) 2021/914; art. 46 lid 2 sub c AVG
- Toetspunt: De gebruikte module(s) passen bij de rollen van exporteur en importeur
- Bronnen: SCC-clausule1 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 1); AVG-art46-lid2-c (AVG art. 46 lid 2 sub c)
- Wat de tekst moet bereiken: Gebruik de module die bij jullie rollen past.

### K13b.2 — Of de clausules ongewijzigd zijn en voorgaan
- Grondslag: clausule 2 en 5
- Toetspunt: De clausules zijn niet gewijzigd en worden niet tegengesproken door andere afspraken; bij strijd gaan de clausules voor
- Bronnen: SCC-clausule2 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 2); SCC-clausule5 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 5)
- Wat de tekst moet bereiken: Neem de clausules ongewijzigd op en laat ze voorgaan op andere afspraken.

### K13b.3 — Of bijlage I.A (partijen) is ingevuld
- Grondslag: clausule 6 en bijlage I.A
- Toetspunt: Bijlage I.A noemt de partijen met naam, adres, contactpersoon, activiteiten en rol
- Bronnen: SCC-clausule6 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 6)
- Wat de tekst moet bereiken: Vul bijlage I.A in met beide partijen.

### K13b.4 — Of bijlage I.B (beschrijving) is ingevuld
- Grondslag: clausule 6 en bijlage I.B
- Toetspunt: Bijlage I.B beschrijft de categorieën betrokkenen en gegevens, gevoelige gegevens, frequentie, aard en doel van de doorgifte, bewaartermijn en (bij doorgifte aan subverwerkers) onderwerp en duur
- Bronnen: SCC-clausule6 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 6)
- Wat de tekst moet bereiken: Vul bijlage I.B concreet in.

### K13b.5 — Of bijlage I.C (toezichthouder) is ingevuld
- Grondslag: clausule 13 en bijlage I.C
- Toetspunt: Bijlage I.C noemt de bevoegde toezichthoudende autoriteit volgens clausule 13
- Alleen als: `facts.module != "p2c"`
- Bronnen: SCC-clausule13 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 13)
- Wat de tekst moet bereiken: Vul de bevoegde toezichthouder in.

### K13b.6 — Of bijlage II (maatregelen) specifiek is ingevuld
- Grondslag: clausule 8 en bijlage II
- Toetspunt: Bijlage II beschrijft de technische en organisatorische maatregelen van de importeur specifiek, niet in algemene termen
- Alleen als: `facts.module != "p2c"`
- Bronnen: SCC-clausule8 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 8)
- Wat de tekst moet bereiken: Beschrijf de beveiligingsmaatregelen van de importeur concreet.

### K13b.7 — Of de keuze voor subverwerkers is gemaakt
- Grondslag: clausule 9 sub a
- Toetspunt: In clausule 9 is optie 1 (specifieke toestemming) of optie 2 (algemene toestemming met een termijn voor voorafgaande kennisgeving) gekozen en ingevuld
- Alleen als: `facts.module != "c2c" and facts.module != "p2c"`
- Bronnen: SCC-clausule9-a (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 9 sub a)
- Wat de tekst moet bereiken: Kies in clausule 9 optie 1 of 2 en vul bij optie 2 de termijn in.

### K13b.8 — Of bijlage III (subverwerkers) is ingevuld
- Grondslag: clausule 9 sub a en bijlage III
- Toetspunt: Bij specifieke toestemming bevat bijlage III de lijst van goedgekeurde subverwerkers
- Alleen als: `facts.module != "c2c" and facts.module != "p2c" and facts.subprocessor_option != "general"`
- Bronnen: SCC-clausule9-a (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 9 sub a)
- Wat de tekst moet bereiken: Vul bijlage III in met de goedgekeurde subverwerkers.

### K13b.9 — Of toepasselijk recht en rechter zijn gekozen
- Grondslag: clausule 17 en 18
- Toetspunt: Clausule 17 (recht van een lidstaat dat rechten van derde-begunstigden toestaat) en clausule 18 (rechter van een lidstaat) zijn ingevuld
- Bronnen: SCC-clausule17 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 17); SCC-clausule18 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 18)
- Wat de tekst moet bereiken: Vul in clausule 17 en 18 het recht en de rechter van een lidstaat in.

### K13b.10 — Of de doorgiftetoets is gedaan
- Grondslag: clausule 14 sub b en d
- Toetspunt: De partijen verklaren dat zij de wetgeving en praktijk in het land van bestemming hebben beoordeeld en documenteren die beoordeling
- Bronnen: SCC-clausule14-b (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub b); SCC-clausule14-d (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub d)
- Wat de tekst moet bereiken: Doe en documenteer de doorgiftetoets (zie de check Doorgiftetoets).
