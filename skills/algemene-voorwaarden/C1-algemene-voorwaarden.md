# Kader C1 — Algemene voorwaarden

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of algemene voorwaarden op tijd aan de klant ter beschikking worden gesteld, geen bedingen bevatten die bij consumenten verboden of vermoedelijk onredelijk zijn, de verplichte consumenteninformatie bevatten en de gebruikelijke onderdelen regelen.

Bronnen: AVG-art13-lid1 (AVG art. 13 lid 1); AVG-art28-lid3 (AVG art. 28 lid 3); BW6-art119a (Burgerlijk Wetboek Boek 6 art. 6:119a); BW6-art230m-lid1 (Burgerlijk Wetboek Boek 6 art. 6:230m lid 1); BW6-art230o-lid1 (Burgerlijk Wetboek Boek 6 art. 6:230o lid 1); BW6-art231 (Burgerlijk Wetboek Boek 6 art. 6:231); BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a); BW6-art233-b (Burgerlijk Wetboek Boek 6 art. 6:233 onder b); BW6-art234 (Burgerlijk Wetboek Boek 6 art. 6:234); BW6-art235-lid1 (Burgerlijk Wetboek Boek 6 art. 6:235 lid 1); BW6-art236 (Burgerlijk Wetboek Boek 6 art. 6:236); BW6-art237 (Burgerlijk Wetboek Boek 6 art. 6:237); BW6-art237-f (Burgerlijk Wetboek Boek 6 art. 6:237 onder f); BW6-art238-lid2 (Burgerlijk Wetboek Boek 6 art. 6:238 lid 2); BW7-art50aa (Burgerlijk Wetboek Boek 7 art. 7:50aa)

## Formulier (vragen aan de gebruiker)

- **supplier_name**: Wat is de naam van je organisatie (de gebruiker van de voorwaarden)?
  - Label (voor de plek-om-in-te-vullen): naam van jouw organisatie
  - Type: text · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **audience**: Gebruik je de voorwaarden voor zakelijke klanten, consumenten of beide?
  - Label (voor de plek-om-in-te-vullen): met wie je de voorwaarden gebruikt
  - Type: enum (business / consumer / both)
- **provided_before_contract**: Krijgt de klant de voorwaarden vóór of bij het sluiten van de overeenkomst, bijvoorbeeld als pdf of met een link die hij kan opslaan?
  - Label (voor de plek-om-in-te-vullen): of de klant de voorwaarden vóór of bij het sluiten krijgt
  - Hulp: Alleen verwijzen ("onze voorwaarden zijn van toepassing") zonder de tekst te geven is niet genoeg.
  - Type: boolean
- **distance_selling**: Sluit je overeenkomsten met consumenten op afstand, zoals via je website, e-mail of telefoon?
  - Label (voor de plek-om-in-te-vullen): of je op afstand verkoopt
  - Type: boolean · Alleen vragen als: `facts.audience != "business"`
- **online_interface**: Sluiten consumenten de overeenkomst (ook) via je website of app?
  - Label (voor de plek-om-in-te-vullen): of consumenten via je website of app bestellen
  - Hulp: Dan moet je sinds juni 2026 een online ontbindingsfunctie aanbieden: een duidelijk zichtbare knop waarmee de consument binnen de bedenktijd de overeenkomst ontbindt (art. 6:230oa BW).
  - Type: boolean · Alleen vragen als: `facts.audience != "business" and facts.distance_selling != false`
- **withdrawal_function_location**: Waar staat de ontbindingsfunctie, en hoe heet de knop?
  - Label (voor de plek-om-in-te-vullen): waar de ontbindingsfunctie staat en hoe de knop heet
  - Hulp: Bijvoorbeeld 'onderaan elke pagina en in "Mijn bestellingen": knop "Overeenkomst ontbinden"'. Een algemene knop als 'Contact' of 'Retourneren' is niet genoeg.
  - Type: text · Alleen vragen als: `facts.online_interface != false and facts.audience != "business" and facts.distance_selling != false`
- **digital_content**: Lever je digitale inhoud of digitale diensten, zoals software, een app, een online dienst of downloads?
  - Label (voor de plek-om-in-te-vullen): of je digitale inhoud of diensten levert
  - Type: boolean
- **processes_customer_data**: Verwerk je voor je zakelijke klanten persoonsgegevens in hun opdracht (bijvoorbeeld als softwareleverancier)?
  - Label (voor de plek-om-in-te-vullen): of je persoonsgegevens voor zakelijke klanten verwerkt
  - Type: boolean · Alleen vragen als: `facts.audience != "consumer"`
- **payment_term**: Binnen hoeveel dagen moet de klant betalen?
  - Label (voor de plek-om-in-te-vullen): de betaaltermijn
  - Type: text
- **liability_cap**: Tot welk bedrag of welke grens wil je aansprakelijk zijn (bijvoorbeeld het factuurbedrag of de uitkering van je verzekering)?
  - Label (voor de plek-om-in-te-vullen): de grens van je aansprakelijkheid
  - Type: text
- **court**: Welke rechter wil je bij geschillen met zakelijke klanten (bijvoorbeeld rechtbank Amsterdam)?
  - Label (voor de plek-om-in-te-vullen): de bevoegde rechter bij zakelijke klanten
  - Type: text
- **privacy_url**: Op welke pagina staat je privacyverklaring?
  - Label (voor de plek-om-in-te-vullen): waar je privacyverklaring staat
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `toepassing` (standaardkop: toepassing)

#### C1.2 — Op wie en wat de voorwaarden van toepassing zijn
- Grondslag: goede praktijk; art. 6:231 BW
- Toetspunt: De voorwaarden noemen de gebruiker en op welke aanbiedingen en overeenkomsten ze van toepassing zijn
- Tekstsoort: `append_section` · Nodig: supplier_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Toepasselijkheid
1. Deze algemene voorwaarden zijn van {{facts.supplier_name}}.
2. Ze zijn van toepassing op alle aanbiedingen van {{facts.supplier_name}} en op alle overeenkomsten die {{facts.supplier_name}} sluit, tenzij partijen schriftelijk anders afspreken.
````

### 2. Onderdeel `aanbod` (standaardkop: aanbod)

#### C1.9 — Of aanbod en totstandkoming zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De voorwaarden regelen wanneer een aanbod geldt en hoe de overeenkomst tot stand komt
- Tekstsoort: `append_section` · Nodig: supplier_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Aanbod en overeenkomst
1. Een aanbod van {{facts.supplier_name}} is vrijblijvend, tenzij in het aanbod een termijn voor aanvaarding staat.
2. De overeenkomst komt tot stand op het moment dat de klant het aanbod aanvaardt.
````

### 3. Onderdeel `prijs` (standaardkop: prijs)

#### C1.10 — Of prijzen en betaling zijn geregeld
- Grondslag: goede praktijk; art. 6:119a BW (wettelijke handelsrente bij handelsovereenkomsten) als achtergrond
- Toetspunt: De voorwaarden regelen prijzen en de betaaltermijn
- Tekstsoort: `append_section` · Nodig: payment_term

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Prijzen en betaling
1. De klant betaalt binnen {{facts.payment_term}} na de factuurdatum.
2. Betaalt de klant niet op tijd, dan is hij de wettelijke rente verschuldigd. Een consument ontvangt eerst een herinnering met een termijn van ten minste veertien dagen voordat incassokosten in rekening worden gebracht.
````

### 4. Onderdeel `herroeping` (standaardkop: herroeping)

#### C1.6 — Of je consumenten informeert over het herroepingsrecht
- Grondslag: art. 6:230m lid 1 en 6:230o BW
- Toetspunt: Bij overeenkomsten op afstand informeert de handelaar de consument over de voorwaarden, de termijn van veertien dagen en de modaliteiten voor de uitoefening van het herroepingsrecht, en over het modelformulier
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.audience != "business" and facts.distance_selling != false` · Nodig: supplier_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Herroepingsrecht
1. Een consument die een overeenkomst op afstand sluit, kan die overeenkomst gedurende een bedenktijd van veertien dagen zonder opgave van redenen ontbinden, behalve in de gevallen die de wet uitzondert.
2. De consument meldt de ontbinding aan {{facts.supplier_name}} met het modelformulier voor herroeping of op een andere ondubbelzinnige manier.
````

#### C1.6a — Of de consument online kan ontbinden met de ontbindingsfunctie
- Grondslag: art. 6:230oa en 6:230m lid 1 sub h BW
- Toetspunt: Bij een via een online-interface gesloten overeenkomst op afstand kan de consument binnen de ontbindingstermijn ontbinden via een duidelijk zichtbare en ondubbelzinnig aangeduide ontbindingsfunctie, met een bevestigingsstap en een ontvangstbevestiging op een duurzame gegevensdrager; de consument wordt vooraf geïnformeerd over de beschikbaarheid en de plaats van de functie
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.audience != "business" and facts.distance_selling != false and facts.online_interface != false` · Nodig: withdrawal_function_location

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
3. Is de overeenkomst via de website of app gesloten, dan kan de consument ook ontbinden met de ontbindingsfunctie: {{facts.withdrawal_function_location}}. De functie is beschikbaar zolang de bedenktijd loopt. De consument vult daar zijn naam, de gegevens van de overeenkomst en het e-mailadres voor de bevestiging in en bevestigt de ontbinding in een aparte stap; een reden is niet nodig. {{facts.supplier_name}} bevestigt de ontvangst direct per e-mail, met de inhoud van de verklaring en de datum en het tijdstip waarop die is ingediend. Het modelformulier en de andere manieren van ontbinden blijven mogelijk.
````

### 5. Onderdeel `aansprakelijkheid` (standaardkop: aansprakelijkheid)

#### C1.11 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 6:237 onder f BW (consument) en art. 6:233 onder a BW als achtergrond
- Toetspunt: De voorwaarden regelen de aansprakelijkheid van de gebruiker, zonder uitsluiting bij opzet of bewuste roekeloosheid
- Tekstsoort: `append_section` · Nodig: supplier_name, liability_cap

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Aansprakelijkheid
1. De aansprakelijkheid van {{facts.supplier_name}} is beperkt tot {{facts.liability_cap}}.
2. Deze beperking geldt niet bij opzet of bewuste roekeloosheid van {{facts.supplier_name}} of haar leidinggevenden, en niet voor zover de wet een beperking tegenover consumenten niet toestaat.
````

### 6. Onderdeel `privacy` (standaardkop: privacy)

#### C1.12 — Of er een verwijzing naar een verwerkersovereenkomst is
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Verwerkt de leverancier persoonsgegevens in opdracht van de zakelijke klant, dan verwijzen de voorwaarden naar een verwerkersovereenkomst die voldoet aan art. 28 lid 3 AVG (of bevatten ze die)
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.audience != "consumer" and facts.processes_customer_data != false` · Nodig: supplier_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Persoonsgegevens
Voor zover {{facts.supplier_name}} bij de uitvoering van de overeenkomst persoonsgegevens verwerkt in opdracht van de klant, sluiten partijen een verwerkersovereenkomst die voldoet aan artikel 28 lid 3 AVG.
````

#### C1.13 — Of de voorwaarden naar je privacyverklaring verwijzen
- Grondslag: goede praktijk; art. 12 en 13 AVG als achtergrond
- Toetspunt: De voorwaarden verwijzen naar de privacyverklaring waarin staat hoe de gebruiker persoonsgegevens van klanten verwerkt
- Tekstsoort: `append_section` · Nodig: supplier_name, privacy_url

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
Hoe {{facts.supplier_name}} persoonsgegevens van klanten verwerkt, staat in de privacyverklaring op {{facts.privacy_url}}.
````

### 7. Onderdeel `geschillen` (standaardkop: geschillen)

#### C1.14 — Of toepasselijk recht en geschillen zijn geregeld
- Grondslag: goede praktijk; art. 6:236 BW (consumenten) als achtergrond
- Toetspunt: De voorwaarden regelen het toepasselijk recht en de bevoegde rechter; tegenover consumenten blijft de rechter van hun woonplaats bevoegd
- Tekstsoort: `append_section` · Nodig: supplier_name, court

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Toepasselijk recht en geschillen
1. Op overeenkomsten met {{facts.supplier_name}} is Nederlands recht van toepassing.
2. Geschillen met zakelijke klanten worden voorgelegd aan {{facts.court}}. Een consument kan een geschil voorleggen aan de rechter die volgens de wet bevoegd is.
````

## Toetspunten (voor de eindcontrole)

### C1.1 — Of de klant de voorwaarden op tijd krijgt
- Grondslag: art. 6:233 onder b en 6:234 BW
- Toetspunt: De gebruiker biedt de wederpartij een redelijke mogelijkheid om van de algemene voorwaarden kennis te nemen: ter hand stellen (bij elektronische overeenkomsten elektronisch ter beschikking stellen, zodat ze kunnen worden opgeslagen) vóór of bij het sluiten van de overeenkomst
- Bronnen: BW6-art231 (Burgerlijk Wetboek Boek 6 art. 6:231); BW6-art233-b (Burgerlijk Wetboek Boek 6 art. 6:233 onder b); BW6-art234 (Burgerlijk Wetboek Boek 6 art. 6:234)
- Wat de tekst moet bereiken: Stuur de voorwaarden mee met de offerte of orderbevestiging (als pdf), of laat de klant ze bij een online bestelling openen en opslaan vóór hij bestelt.

### C1.2 — Op wie en wat de voorwaarden van toepassing zijn
- Grondslag: goede praktijk; art. 6:231 BW
- Toetspunt: De voorwaarden noemen de gebruiker en op welke aanbiedingen en overeenkomsten ze van toepassing zijn
- Bronnen: BW6-art231 (Burgerlijk Wetboek Boek 6 art. 6:231)
- Wat de tekst moet bereiken: Zet bovenaan wie de voorwaarden gebruikt en op welke aanbiedingen en overeenkomsten ze van toepassing zijn.

### C1.3 — Of er bedingen in staan die bij consumenten altijd onredelijk zijn (zwarte lijst)
- Grondslag: art. 6:236 BW
- Toetspunt: Bij consumenten bevatten de voorwaarden geen beding van de lijst van art. 6:236 BW (onder meer het recht op nakoming of ontbinding ontzeggen, de verjaringstermijn tot minder dan een jaar verkorten, een prijsverhoging binnen drie maanden zonder recht om te ontbinden, een stilzwijgende verlenging zonder opzegmogelijkheid, of een andere rechter dan die van de woonplaats van de consument)
- Alleen als: `facts.audience != "business"`
- Bronnen: BW6-art236 (Burgerlijk Wetboek Boek 6 art. 6:236)
- Wat de tekst moet bereiken: Schrap of herschrijf het beding dat op de zwarte lijst van art. 6:236 BW staat: het is tegenover consumenten altijd vernietigbaar.

### C1.4 — Of er bedingen in staan die bij consumenten vermoedelijk onredelijk zijn (grijze lijst)
- Grondslag: art. 6:237 BW
- Toetspunt: Bij consumenten wordt een beding van de lijst van art. 6:237 BW vermoed onredelijk bezwarend te zijn (onder meer de eigen prestatie wezenlijk mogen wijzigen, aansprakelijkheid beperken of uitsluiten, een lange looptijd of opzegtermijn)
- Alleen als: `facts.audience != "business"`
- Bronnen: BW6-art237 (Burgerlijk Wetboek Boek 6 art. 6:237)
- Wat de tekst moet bereiken: Laat de bedingen die op de grijze lijst kunnen staan beoordelen, of beperk ze zodat ze redelijk zijn tegenover consumenten.

### C1.5 — Of bedingen voor zakelijke klanten onredelijk bezwarend kunnen zijn
- Grondslag: art. 6:233 onder a en 6:235 BW
- Toetspunt: Een beding is vernietigbaar als het, gelet op de aard en inhoud van de overeenkomst, de wijze van totstandkoming, de kenbare belangen en de omstandigheden, onredelijk bezwarend is voor de wederpartij
- Alleen als: `facts.audience != "consumer"`
- Bronnen: BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a); BW6-art235-lid1 (Burgerlijk Wetboek Boek 6 art. 6:235 lid 1)
- Wat de tekst moet bereiken: Laat bedingen die de klant zwaar benadelen beoordelen, vooral een volledige uitsluiting van aansprakelijkheid.

### C1.6 — Of je consumenten informeert over het herroepingsrecht
- Grondslag: art. 6:230m lid 1 en 6:230o BW
- Toetspunt: Bij overeenkomsten op afstand informeert de handelaar de consument over de voorwaarden, de termijn van veertien dagen en de modaliteiten voor de uitoefening van het herroepingsrecht, en over het modelformulier
- Alleen als: `facts.audience != "business" and facts.distance_selling != false`
- Bronnen: BW6-art230m-lid1 (Burgerlijk Wetboek Boek 6 art. 6:230m lid 1); BW6-art230o-lid1 (Burgerlijk Wetboek Boek 6 art. 6:230o lid 1)
- Wat de tekst moet bereiken: Beschrijf het herroepingsrecht: de consument kan de overeenkomst binnen veertien dagen zonder opgave van redenen ontbinden, hoe hij dat doet en dat hij het modelformulier kan gebruiken.

### C1.6a — Of de consument online kan ontbinden met de ontbindingsfunctie
- Grondslag: art. 6:230oa en 6:230m lid 1 sub h BW
- Toetspunt: Bij een via een online-interface gesloten overeenkomst op afstand kan de consument binnen de ontbindingstermijn ontbinden via een duidelijk zichtbare en ondubbelzinnig aangeduide ontbindingsfunctie, met een bevestigingsstap en een ontvangstbevestiging op een duurzame gegevensdrager; de consument wordt vooraf geïnformeerd over de beschikbaarheid en de plaats van de functie
- Alleen als: `facts.audience != "business" and facts.distance_selling != false and facts.online_interface != false`
- Bronnen: BW6-art230oa (Burgerlijk Wetboek Boek 6 art. 6:230oa, ingevoegd bij Stb. 2026, 153); RL-2023-2673 (Richtlijn (EU) 2023/2673, art. 11 bis Richtlijn 2011/83/EU)
- Wat de tekst moet bereiken: Vertel waar de ontbindingsfunctie staat en hoe ze werkt. De knop zelf bouw je op de website; de voorwaarden alleen zijn niet genoeg.

### C1.7 — Of de voorwaarden de wettelijke rechten bij digitale inhoud niet beperken
- Grondslag: art. 7:50aa e.v. BW
- Toetspunt: Bij digitale inhoud of diensten voor consumenten beperken de voorwaarden de dwingende regels van titel 7.1A BW niet (conformiteit, updates, rechten bij gebreken)
- Alleen als: `facts.audience != "business" and facts.digital_content != false`
- Bronnen: BW7-art50aa (Burgerlijk Wetboek Boek 7 art. 7:50aa)
- Wat de tekst moet bereiken: Beperk de wettelijke rechten van consumenten bij gebreken en updates van digitale inhoud niet; verwijs naar de wettelijke regeling.

### C1.8 — Of de voorwaarden voor consumenten duidelijk en begrijpelijk zijn
- Grondslag: art. 6:238 lid 2 BW
- Toetspunt: Bedingen voor consumenten zijn duidelijk en begrijpelijk geformuleerd; bij twijfel geldt de voor de consument gunstigste uitleg
- Alleen als: `facts.audience != "business"`
- Bronnen: BW6-art238-lid2 (Burgerlijk Wetboek Boek 6 art. 6:238 lid 2)
- Wat de tekst moet bereiken: Herschrijf onduidelijke bedingen in gewone taal.

### C1.9 — Of aanbod en totstandkoming zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De voorwaarden regelen wanneer een aanbod geldt en hoe de overeenkomst tot stand komt
- Bronnen: BW6-art231 (Burgerlijk Wetboek Boek 6 art. 6:231)
- Wat de tekst moet bereiken: Leg vast hoe lang een aanbod geldig is en wanneer de overeenkomst tot stand komt.

### C1.10 — Of prijzen en betaling zijn geregeld
- Grondslag: goede praktijk; art. 6:119a BW (wettelijke handelsrente bij handelsovereenkomsten) als achtergrond
- Toetspunt: De voorwaarden regelen prijzen en de betaaltermijn
- Bronnen: BW6-art119a (Burgerlijk Wetboek Boek 6 art. 6:119a)
- Wat de tekst moet bereiken: Leg de betaaltermijn vast en wat er gebeurt als de klant te laat betaalt.

### C1.11 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 6:237 onder f BW (consument) en art. 6:233 onder a BW als achtergrond
- Toetspunt: De voorwaarden regelen de aansprakelijkheid van de gebruiker, zonder uitsluiting bij opzet of bewuste roekeloosheid
- Bronnen: BW6-art237-f (Burgerlijk Wetboek Boek 6 art. 6:237 onder f); BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a)
- Wat de tekst moet bereiken: Leg vast tot welke grens je aansprakelijk bent, en sluit opzet en bewuste roekeloosheid niet uit.

### C1.12 — Of er een verwijzing naar een verwerkersovereenkomst is
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Verwerkt de leverancier persoonsgegevens in opdracht van de zakelijke klant, dan verwijzen de voorwaarden naar een verwerkersovereenkomst die voldoet aan art. 28 lid 3 AVG (of bevatten ze die)
- Alleen als: `facts.audience != "consumer" and facts.processes_customer_data != false`
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3)
- Wat de tekst moet bereiken: Verwijs naar je verwerkersovereenkomst, of sluit er een met elke zakelijke klant voor wie je persoonsgegevens verwerkt.

### C1.13 — Of de voorwaarden naar je privacyverklaring verwijzen
- Grondslag: goede praktijk; art. 12 en 13 AVG als achtergrond
- Toetspunt: De voorwaarden verwijzen naar de privacyverklaring waarin staat hoe de gebruiker persoonsgegevens van klanten verwerkt
- Bronnen: AVG-art13-lid1 (AVG art. 13 lid 1)
- Wat de tekst moet bereiken: Verwijs naar je privacyverklaring.

### C1.14 — Of toepasselijk recht en geschillen zijn geregeld
- Grondslag: goede praktijk; art. 6:236 BW (consumenten) als achtergrond
- Toetspunt: De voorwaarden regelen het toepasselijk recht en de bevoegde rechter; tegenover consumenten blijft de rechter van hun woonplaats bevoegd
- Bronnen: BW6-art236 (Burgerlijk Wetboek Boek 6 art. 6:236)
- Wat de tekst moet bereiken: Leg toepasselijk recht en de bevoegde rechter vast; laat consumenten bij hun eigen rechter.
