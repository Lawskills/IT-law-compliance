# Kader C5 — Geheimhoudingsovereenkomst (NDA)

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of een geheimhoudingsovereenkomst de vertrouwelijke informatie, de uitzonderingen, het doel, de kring van ontvangers, de duur, de teruggave, de sanctie en het toepasselijk recht duidelijk regelt.

Bronnen: AVG-art28-lid3-b (AVG art. 28 lid 3 sub b); AVG-art32-lid4 (AVG art. 32 lid 4); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); BW6-art91 (Burgerlijk Wetboek Boek 6 art. 6:91); BW6-art92 (Burgerlijk Wetboek Boek 6 art. 6:92); BW6-art94 (Burgerlijk Wetboek Boek 6 art. 6:94); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)

## Formulier (vragen aan de gebruiker)

- **party_a_name**: Wie verstrekt de vertrouwelijke informatie?
  - Label (voor de plek-om-in-te-vullen): naam van de partij die informatie verstrekt
  - Type: text
- **party_b_name**: Wie ontvangt de vertrouwelijke informatie?
  - Label (voor de plek-om-in-te-vullen): naam van de partij die informatie ontvangt
  - Type: text
- **mutual**: Delen beide partijen vertrouwelijke informatie met elkaar (wederzijds)?
  - Label (voor de plek-om-in-te-vullen): of de geheimhouding wederzijds is
  - Type: boolean
- **nda_purpose**: Waarvoor delen jullie de informatie (bijvoorbeeld het verkennen van een samenwerking)?
  - Label (voor de plek-om-in-te-vullen): het doel waarvoor de informatie wordt gedeeld
  - Type: text
- **nda_duration**: Hoe lang moet de informatie geheim blijven?
  - Label (voor de plek-om-in-te-vullen): hoe lang de geheimhouding geldt
  - Type: text
- **penalty**: Welke boete geldt bij overtreding (laat leeg als je geen boete wilt)?
  - Label (voor de plek-om-in-te-vullen): de boete bij overtreding
  - Type: text
- **personal_data**: Worden er persoonsgegevens gedeeld?
  - Label (voor de plek-om-in-te-vullen): of er persoonsgegevens worden gedeeld
  - Type: boolean

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `definitie` (standaardkop: definitie)

#### C5.1 — Wat vertrouwelijke informatie is
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst omschrijft welke informatie vertrouwelijk is
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Vertrouwelijke informatie
Vertrouwelijke informatie is alle niet-openbare informatie die een partij in verband met het doel van deze overeenkomst aan de andere partij verstrekt, in welke vorm ook.
````

### 2. Onderdeel `uitzonderingen` (standaardkop: uitzonderingen)

#### C5.2 — Welke informatie niet vertrouwelijk is
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst noemt de gebruikelijke uitzonderingen: openbare informatie, informatie die de ontvanger al had of zelf ontwikkelde, en een wettelijke plicht of rechterlijk bevel tot verstrekking
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Uitzonderingen
De geheimhouding geldt niet voor informatie die (a) openbaar is of wordt zonder schending van deze overeenkomst, (b) de ontvanger al rechtmatig had, (c) de ontvanger zelfstandig heeft ontwikkeld, of (d) de ontvanger op grond van de wet of een rechterlijke uitspraak moet verstrekken; in dat laatste geval informeert de ontvanger de andere partij vooraf, voor zover dat mag.
````

### 3. Onderdeel `doel` (standaardkop: doel)

#### C5.3 — Waarvoor de informatie gebruikt mag worden
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst beperkt het gebruik van de informatie tot een omschreven doel
- Tekstsoort: `append_section` · Nodig: nda_purpose

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Doel
De ontvanger gebruikt de vertrouwelijke informatie uitsluitend voor: {{facts.nda_purpose}}.
````

### 4. Onderdeel `ontvangers` (standaardkop: Met wie delen wij je gegevens)

#### C5.4 — Wie de informatie mag zien
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst beperkt de kring van ontvangers tot wie de informatie nodig heeft en legt de geheimhouding aan hen op
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Ontvangers
De ontvanger verstrekt vertrouwelijke informatie alleen aan medewerkers en adviseurs die haar voor het doel nodig hebben en die aan een gelijkwaardige geheimhouding zijn gebonden. De ontvanger is verantwoordelijk voor de naleving door hen.
````

### 5. Onderdeel `duur` (standaardkop: duur)

#### C5.5 — Hoe lang de geheimhouding geldt
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst regelt de duur van de geheimhouding, ook na afloop van de samenwerking
- Tekstsoort: `append_section` · Nodig: nda_duration

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Duur
De geheimhouding geldt {{facts.nda_duration}}, ook als de samenwerking eerder eindigt.
````

### 6. Onderdeel `teruggave` (standaardkop: teruggave)

#### C5.6 — Wat er met de informatie gebeurt na afloop
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst regelt teruggave of vernietiging van de informatie na afloop of op verzoek
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Teruggave
Op verzoek en na afloop van de samenwerking geeft de ontvanger de vertrouwelijke informatie terug of vernietigt hij die, behalve voor zover hij die op grond van de wet moet bewaren.
````

### 7. Onderdeel `boete` (standaardkop: boete)

#### C5.7 — Of er een sanctie op overtreding staat
- Grondslag: goede praktijk; art. 6:91, 6:92 en 6:94 BW
- Toetspunt: De overeenkomst regelt de gevolgen van overtreding, bijvoorbeeld een boete; de rechter kan een boete matigen als de billijkheid dat klaarblijkelijk eist
- Tekstsoort: `append_section` · Nodig: penalty

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Boete
Bij overtreding van deze overeenkomst verbeurt de overtredende partij een direct opeisbare boete van {{facts.penalty}}, onverminderd het recht op vergoeding van de werkelijke schade.
````

### 8. Onderdeel `persoonsgegevens` (standaardkop: persoonsgegevens)

#### C5.8 — Of geheimhouding van persoonsgegevens is geregeld
- Grondslag: goede praktijk; art. 28 lid 3 sub b en art. 32 lid 4 AVG
- Toetspunt: Worden persoonsgegevens gedeeld, dan regelt de overeenkomst dat wie ze inziet tot geheimhouding is verplicht en verwijst zij naar de afspraken over de verwerking (verwerkersovereenkomst of gegevensdelingsovereenkomst)
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.personal_data != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Persoonsgegevens
Worden persoonsgegevens gedeeld, dan zijn de personen die ze inzien tot geheimhouding verplicht. Voor de verwerking zelf sluiten partijen een afzonderlijke verwerkers- of gegevensdelingsovereenkomst.
````

### 9. Onderdeel `recht` (standaardkop: recht)

#### C5.9 — Of toepasselijk recht en geschillen zijn geregeld
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst regelt het toepasselijk recht en de bevoegde rechter
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Toepasselijk recht
Op deze overeenkomst is Nederlands recht van toepassing.
````

## Toetspunten (voor de eindcontrole)

### C5.1 — Wat vertrouwelijke informatie is
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst omschrijft welke informatie vertrouwelijk is
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)
- Wat de tekst moet bereiken: Omschrijf welke informatie onder de geheimhouding valt.

### C5.2 — Welke informatie niet vertrouwelijk is
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst noemt de gebruikelijke uitzonderingen: openbare informatie, informatie die de ontvanger al had of zelf ontwikkelde, en een wettelijke plicht of rechterlijk bevel tot verstrekking
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)
- Wat de tekst moet bereiken: Neem de gebruikelijke uitzonderingen op, waaronder een wettelijke plicht tot verstrekking.

### C5.3 — Waarvoor de informatie gebruikt mag worden
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst beperkt het gebruik van de informatie tot een omschreven doel
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)
- Wat de tekst moet bereiken: Leg vast waarvoor de informatie alleen gebruikt mag worden.

### C5.4 — Wie de informatie mag zien
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst beperkt de kring van ontvangers tot wie de informatie nodig heeft en legt de geheimhouding aan hen op
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)
- Wat de tekst moet bereiken: Leg vast dat alleen medewerkers en adviseurs die de informatie nodig hebben haar krijgen, onder dezelfde geheimhouding.

### C5.5 — Hoe lang de geheimhouding geldt
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst regelt de duur van de geheimhouding, ook na afloop van de samenwerking
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)
- Wat de tekst moet bereiken: Leg vast hoe lang de geheimhouding geldt, ook na afloop van de samenwerking.

### C5.6 — Wat er met de informatie gebeurt na afloop
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst regelt teruggave of vernietiging van de informatie na afloop of op verzoek
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)
- Wat de tekst moet bereiken: Leg vast dat de informatie na afloop of op verzoek wordt teruggegeven of vernietigd.

### C5.7 — Of er een sanctie op overtreding staat
- Grondslag: goede praktijk; art. 6:91, 6:92 en 6:94 BW
- Toetspunt: De overeenkomst regelt de gevolgen van overtreding, bijvoorbeeld een boete; de rechter kan een boete matigen als de billijkheid dat klaarblijkelijk eist
- Bronnen: BW6-art91 (Burgerlijk Wetboek Boek 6 art. 6:91); BW6-art92 (Burgerlijk Wetboek Boek 6 art. 6:92); BW6-art94 (Burgerlijk Wetboek Boek 6 art. 6:94)
- Wat de tekst moet bereiken: Leg de gevolgen van overtreding vast, bijvoorbeeld een boete, en of daarnaast schadevergoeding kan worden gevorderd.

### C5.8 — Of geheimhouding van persoonsgegevens is geregeld
- Grondslag: goede praktijk; art. 28 lid 3 sub b en art. 32 lid 4 AVG
- Toetspunt: Worden persoonsgegevens gedeeld, dan regelt de overeenkomst dat wie ze inziet tot geheimhouding is verplicht en verwijst zij naar de afspraken over de verwerking (verwerkersovereenkomst of gegevensdelingsovereenkomst)
- Alleen als: `facts.personal_data != false`
- Bronnen: AVG-art28-lid3-b (AVG art. 28 lid 3 sub b); AVG-art32-lid4 (AVG art. 32 lid 4)
- Wat de tekst moet bereiken: Leg vast dat persoonsgegevens alleen onder geheimhouding worden ingezien, en sluit daarnaast een verwerkers- of gegevensdelingsovereenkomst.

### C5.9 — Of toepasselijk recht en geschillen zijn geregeld
- Grondslag: goede praktijk; art. 6:248 BW en art. 1 Wet bescherming bedrijfsgeheimen als achtergrond
- Toetspunt: De overeenkomst regelt het toepasselijk recht en de bevoegde rechter
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); WBB-art1 (Wet bescherming bedrijfsgeheimen art. 1)
- Wat de tekst moet bereiken: Leg toepasselijk recht en de bevoegde rechter vast.
