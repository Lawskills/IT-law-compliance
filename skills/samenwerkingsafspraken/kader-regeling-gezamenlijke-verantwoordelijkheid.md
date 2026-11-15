# Kader K18b — Regeling gezamenlijke verantwoordelijkheid (document)

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een regeling tussen gezamenlijk verwerkingsverantwoordelijken op transparante wijze ieders verantwoordelijkheden vastlegt, met name voor de rechten van betrokkenen en de informatieplicht, de feitelijke rollen weerspiegelt, de kern beschikbaar maakt voor betrokkenen en hun rechten tegen elke partij intact laat.

Bronnen: AVG-art26-lid1 (AVG art. 26 lid 1); AVG-art26-lid2 (AVG art. 26 lid 2); AVG-art26-lid3 (AVG art. 26 lid 3); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)

## Formulier (vragen aan de gebruiker)

- **party_a_name**: Wat is de naam van jouw organisatie?
  - Label (voor de plek-om-in-te-vullen): naam van de eerste partij
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **party_b_name**: Met welke organisatie bepaal je samen doel en middelen?
  - Label (voor de plek-om-in-te-vullen): naam van de andere partij
  - Type: text
- **set_by_law**: Is de verdeling van de verantwoordelijkheden al in een wet geregeld?
  - Label (voor de plek-om-in-te-vullen): of de wet de verdeling al regelt
  - Type: boolean
- **joint_operations**: Welke onderdelen van de verwerking bepalen jullie samen?
  - Label (voor de plek-om-in-te-vullen): welke onderdelen jullie samen bepalen
  - Type: text
- **rights_handler**: Wie van jullie handelt verzoeken van betrokkenen af?
  - Label (voor de plek-om-in-te-vullen): wie verzoeken van betrokkenen afhandelt
  - Type: text
- **info_handler**: Wie van jullie informeert de betrokkenen (art. 13 en 14 AVG), en waar?
  - Label (voor de plek-om-in-te-vullen): wie betrokkenen informeert
  - Type: text
- **essence_location**: Waar kunnen betrokkenen de kern van de regeling lezen?
  - Label (voor de plek-om-in-te-vullen): waar betrokkenen de kern lezen
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `onderdelen` (standaardkop: onderdelen)

#### K18b.1 — Of vastligt welke onderdelen gezamenlijk zijn
- Grondslag: art. 26 lid 1 AVG; EDPB-richtsnoeren 07/2020
- Toetspunt: De regeling beschrijft voor welke verwerkingen of onderdelen de partijen gezamenlijk verantwoordelijk zijn
- Tekstsoort: `append_section` · Nodig: joint_operations

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Gezamenlijke verwerking
Partijen zijn gezamenlijk verwerkingsverantwoordelijk voor: {{facts.joint_operations}}. Voor andere verwerkingen is elke partij zelf verantwoordelijk.
````

### 2. Onderdeel `verdeling` (standaardkop: verdeling)

#### K18b.2 — Wie de rechten van betrokkenen en de informatieplicht regelt
- Grondslag: art. 26 lid 1 AVG
- Toetspunt: De regeling legt op transparante wijze vast wie welke verplichting nakomt, in het bijzonder de uitoefening van de rechten van betrokkenen en de informatieplicht van art. 13 en 14, tenzij de wet de verdeling regelt
- Tekstsoort: `append_section` · Nodig: rights_handler, info_handler

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Verdeling van verplichtingen
1. Verzoeken van betrokkenen worden afgehandeld door: {{facts.rights_handler}}.
2. De informatie aan betrokkenen (artikel 13 en 14 AVG) verstrekt: {{facts.info_handler}}.
````

### 3. Onderdeel `beschikbaar` (standaardkop: beschikbaar)

#### K18b.5 — Of betrokkenen de kern van de regeling kunnen lezen
- Grondslag: art. 26 lid 2 AVG
- Toetspunt: De wezenlijke inhoud van de regeling wordt aan de betrokkenen beschikbaar gesteld
- Tekstsoort: `append_section` · Nodig: essence_location

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Informatie voor betrokkenen
De kern van deze regeling is voor betrokkenen beschikbaar in: {{facts.essence_location}}.
````

### 4. Onderdeel `contact` (standaardkop: Wie zijn wij)

#### K18b.6 — Of er een contactpunt is
- Grondslag: art. 26 lid 1 AVG ("kan")
- Toetspunt: De regeling kan een contactpunt voor betrokkenen aanwijzen
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Contactpunt
Betrokkenen kunnen met vragen over de gezamenlijke verwerking terecht bij [IN TE VULLEN: contactpunt]. Zij kunnen hun rechten daarnaast bij elke partij uitoefenen.
````

## Toetspunten (voor de eindcontrole)

### K18b.1 — Of vastligt welke onderdelen gezamenlijk zijn
- Grondslag: art. 26 lid 1 AVG; EDPB-richtsnoeren 07/2020
- Toetspunt: De regeling beschrijft voor welke verwerkingen of onderdelen de partijen gezamenlijk verantwoordelijk zijn
- Bronnen: AVG-art26-lid1 (AVG art. 26 lid 1); EDPB-RL-07-2020 (EDPB, Richtsnoeren 07/2020 over de begrippen "verwerkingsverantwoordelijke" en "verwerker" in de AVG)
- Wat de tekst moet bereiken: Beschrijf voor welke verwerkingen of onderdelen jullie samen verantwoordelijk zijn, en voor welke ieder zelf.

### K18b.2 — Wie de rechten van betrokkenen en de informatieplicht regelt
- Grondslag: art. 26 lid 1 AVG
- Toetspunt: De regeling legt op transparante wijze vast wie welke verplichting nakomt, in het bijzonder de uitoefening van de rechten van betrokkenen en de informatieplicht van art. 13 en 14, tenzij de wet de verdeling regelt
- Bronnen: AVG-art26-lid1 (AVG art. 26 lid 1)
- Wat de tekst moet bereiken: Leg vast wie verzoeken van betrokkenen afhandelt en wie hen informeert.

### K18b.3 — Of de regeling de werkelijke rollen weerspiegelt
- Grondslag: art. 26 lid 2 AVG
- Toetspunt: De regeling weerspiegelt de respectieve rollen en verhoudingen van de partijen ten opzichte van de betrokkenen
- Bronnen: AVG-art26-lid2 (AVG art. 26 lid 2)
- Wat de tekst moet bereiken: Controleer of de afspraken passen bij wat ieder in de praktijk doet.

### K18b.4 — Of betrokkenen hun rechten bij elke partij kunnen uitoefenen
- Grondslag: art. 26 lid 3 AVG
- Toetspunt: De regeling beperkt niet dat betrokkenen hun rechten bij en tegen elk van de verwerkingsverantwoordelijken kunnen uitoefenen
- Bronnen: AVG-art26-lid3 (AVG art. 26 lid 3)
- Wat de tekst moet bereiken: Neem op dat betrokkenen hun rechten bij elke partij kunnen uitoefenen, ongeacht de onderlinge afspraken.

### K18b.5 — Of betrokkenen de kern van de regeling kunnen lezen
- Grondslag: art. 26 lid 2 AVG
- Toetspunt: De wezenlijke inhoud van de regeling wordt aan de betrokkenen beschikbaar gesteld
- Bronnen: AVG-art26-lid2 (AVG art. 26 lid 2)
- Wat de tekst moet bereiken: Leg vast waar betrokkenen de kern van de regeling kunnen lezen.

### K18b.6 — Of er een contactpunt is
- Grondslag: art. 26 lid 1 AVG ("kan")
- Toetspunt: De regeling kan een contactpunt voor betrokkenen aanwijzen
- Bronnen: AVG-art26-lid1 (AVG art. 26 lid 1)
- Wat de tekst moet bereiken: Overweeg één contactpunt voor betrokkenen aan te wijzen.
