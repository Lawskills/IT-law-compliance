# Kader K13c — Doorgiftetoets (TIA)

Versie 1.3 · peildatum 2026-11-10

Doel: Controleren of een organisatie die persoonsgegevens op grond van passende waarborgen buiten de EER doorgeeft, de doorgifte in kaart heeft gebracht, de wetgeving en praktijk in het land van bestemming heeft beoordeeld, waar nodig aanvullende maatregelen neemt, dit documenteert en periodiek herbeoordeelt.

Geldt alleen als: `(facts.data_stored_outside_eea != false or facts.remote_access_outside_eea != false) and facts.transfer_without_adequacy != false and facts.basis_safeguards != false` — de doorgiftetoets hoort bij doorgifte op grond van passende waarborgen (art. 46 AVG; regel van kader K13)

Bronnen: AVG-art44 (AVG art. 44); AVG-art45-lid1 (AVG art. 45 lid 1); AVG-art46-lid1 (AVG art. 46 lid 1); AVG-art46-lid2-c (AVG art. 46 lid 2 sub c); AVG-art5-lid2 (AVG art. 5 lid 2); EDPB-AB-01-2020 (EDPB, Aanbevelingen 01/2020 over maatregelen ter aanvulling van doorgifte-instrumenten om te waarborgen dat het EU-niveau van bescherming van persoonsgegevens wordt nageleefd); GerEU-T-553-23 (Gerecht EU 3 september 2025, T-553/23, Latombe/Commissie); HvJEU-C-311-18 (HvJEU 16 juli 2020, C-311/18, Data Protection Commissioner/Facebook Ireland en Schrems (Schrems II)); SCC-clausule14 (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14); SCC-clausule14-b (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub b); SCC-clausule14-d (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub d); SCC-clausule14-e (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub e); UB-2023-1795 (Uitvoeringsbesluit (EU) 2023/1795 van de Commissie over het passende beschermingsniveau in het kader van het EU-VS Data Privacy Framework)

## Formulier (vragen aan de gebruiker)

- **recipient_country**: Naar welke ontvanger en welk land gaan de gegevens?
  - Label (voor de plek-om-in-te-vullen): naar welk land de gegevens gaan
  - Type: text
- **transfers_mapped**: Heb je in kaart welke gegevens naar wie en welk land gaan, ook via subverwerkers en toegang op afstand?
  - Label (voor de plek-om-in-te-vullen): of de doorgiften in kaart zijn gebracht
  - Type: boolean
- **adequacy**: Geldt voor het land of de ontvanger een adequaatheidsbesluit van de Europese Commissie?
  - Label (voor de plek-om-in-te-vullen): of er een adequaatheidsbesluit geldt
  - Type: enum (none / adequacy_country / dpf_certified)
- **instrument**: Op welk instrument rust de doorgifte?
  - Label (voor de plek-om-in-te-vullen): welk doorgifte-instrument je gebruikt
  - Type: enum (scc / bcr / other) · Alleen vragen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"`
- **law_assessed**: Heb je beoordeeld of wetgeving en praktijk in het land van bestemming (vooral toegang door overheidsdiensten) de bescherming van het instrument aantasten?
  - Label (voor de plek-om-in-te-vullen): of je de wetgeving en praktijk in het land hebt beoordeeld
  - Type: boolean · Alleen vragen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"`
- **law_findings**: Wat was de uitkomst van die beoordeling, en op welke bronnen rust die?
  - Label (voor de plek-om-in-te-vullen): wat de beoordeling opleverde
  - Type: text · Alleen vragen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"`
- **supplementary_measures**: Welke aanvullende maatregelen neem je (bijvoorbeeld versleuteling waarbij alleen jij de sleutel hebt), of waarom zijn die niet nodig?
  - Label (voor de plek-om-in-te-vullen): welke aanvullende maatregelen je neemt
  - Type: text · Alleen vragen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"`
- **documented**: Heb je de toets vastgelegd, zodat je hem op verzoek aan de toezichthouder kunt geven?
  - Label (voor de plek-om-in-te-vullen): of de toets is vastgelegd
  - Type: boolean · Alleen vragen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"`
- **reassessment**: Heb je afgesproken wanneer je de toets opnieuw bekijkt (bijvoorbeeld jaarlijks of bij nieuwe wetgeving)?
  - Label (voor de plek-om-in-te-vullen): of je de toets periodiek herbeoordeelt
  - Type: boolean · Alleen vragen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"`

## Toetspunten

### K13c.1 — Of je weet welke gegevens waarheen gaan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De organisatie heeft de doorgiften in kaart gebracht, inclusief verdere doorgiften en toegang op afstand (EDPB stap 1)
- Grondslag: art. 44 AVG; EDPB-aanbevelingen 01/2020
- Beoordeeld op: de antwoorden
- Nodig: transfers_mapped
- Beoordeling:
  - present als transfers_mapped true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Breng in kaart welke gegevens naar welke ontvangers en landen gaan, ook via subverwerkers.
- Bronnen: AVG-art44 (AVG art. 44); EDPB-AB-01-2020 (EDPB, Aanbevelingen 01/2020 over maatregelen ter aanvulling van doorgifte-instrumenten om te waarborgen dat het EU-niveau van bescherming van persoonsgegevens wordt nageleefd)

### K13c.2 — Of een adequaatheidsbesluit de toets overbodig maakt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geldt een adequaatheidsbesluit (art. 45 AVG), dan is geen doorgiftetoets nodig
- Grondslag: art. 45 AVG; Uitvoeringsbesluit (EU) 2023/1795
- Alleen als: `facts.adequacy != "none"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: adequacy
- Beoordeling:
  - Deze stap geldt alleen als er een adequaatheidsbesluit of DPF-certificering is; zonder besluit is hij n.v.t.
  - Altijd review. Bij een adequaatheidsbesluit of DPF-certificering: compliant kan niet; vermeld dat de rest van de toets niet nodig is en dat de DPF-certificering van de ontvanger moet worden gecontroleerd op de lijst van het Amerikaanse ministerie van Handel.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Geldt het adequaatheidsbesluit voor deze doorgifte?
- Advies bij ❌ of ⚠️: Controleer dat het adequaatheidsbesluit geldt en dat een Amerikaanse ontvanger echt op de DPF-lijst staat.
- Bronnen: AVG-art45-lid1 (AVG art. 45 lid 1); UB-2023-1795 (Uitvoeringsbesluit (EU) 2023/1795 van de Commissie over het passende beschermingsniveau in het kader van het EU-VS Data Privacy Framework); GerEU-T-553-23 (Gerecht EU 3 september 2025, T-553/23, Latombe/Commissie)

### K13c.3 — Of er een doorgifte-instrument is
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Zonder adequaatheidsbesluit rust de doorgifte op een instrument van art. 46 AVG (EDPB stap 2)
- Grondslag: art. 46 lid 1 en 2 AVG
- Alleen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: instrument
- Beoordeling:
  - present als instrument scc of bcr is; bij other: twijfel (⚠️) (een juridisch adviseur beoordeelt of het een instrument van art. 46 of een uitzondering van art. 49 is).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Gebruik een instrument van art. 46 AVG, meestal de standaardcontractbepalingen.
- Bronnen: AVG-art46-lid1 (AVG art. 46 lid 1); AVG-art46-lid2-c (AVG art. 46 lid 2 sub c)

### K13c.4 — Of de wetgeving en praktijk in het land zijn beoordeeld
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De organisatie heeft beoordeeld of wetgeving of praktijk in het derde land de doeltreffendheid van de waarborgen aantast, in het bijzonder toegang door overheidsdiensten (EDPB stap 3; clausule 14 sub b)
- Grondslag: art. 46 lid 1 AVG; HvJ C-311/18; clausule 14
- Alleen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: law_assessed, recipient_country
- Beoordeling:
  - Duidelijk geval non_compliant: law_assessed false.
  - Duidelijk geval compliant: law_assessed true en law_findings noemt concrete bevindingen over overheidstoegang met bronnen.
  - law_assessed true maar law_findings ontbreekt of is algemeen ("het land is veilig"): geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is de beoordeling van wetgeving en praktijk volledig en onderbouwd?
- Advies bij ❌ of ⚠️: Beoordeel en documenteer de wetgeving en praktijk in het land van bestemming, vooral de toegang door overheidsdiensten.
- Bronnen: AVG-art46-lid1 (AVG art. 46 lid 1); HvJEU-C-311-18 (HvJEU 16 juli 2020, C-311/18, Data Protection Commissioner/Facebook Ireland en Schrems (Schrems II)); SCC-clausule14-b (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub b); EDPB-AB-01-2020 (EDPB, Aanbevelingen 01/2020 over maatregelen ter aanvulling van doorgifte-instrumenten om te waarborgen dat het EU-niveau van bescherming van persoonsgegevens wordt nageleefd)

### K13c.5 — Of aanvullende maatregelen zijn genomen waar nodig
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Tasten wet of praktijk de bescherming aan, dan neemt de organisatie aanvullende maatregelen die een wezenlijk gelijkwaardig niveau waarborgen, of zet zij de doorgifte niet voort (EDPB stap 4)
- Grondslag: art. 46 lid 1 AVG; HvJ C-311/18
- Alleen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Beoordeling:
  - Altijd review: of de maatregelen volstaan, is een afweging. Noem de genoemde maatregelen.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Waarborgen de aanvullende maatregelen een wezenlijk gelijkwaardig beschermingsniveau?
- Advies bij ❌ of ⚠️: Neem aanvullende maatregelen als de beoordeling daarom vraagt, zoals versleuteling waarvan alleen jij de sleutel hebt, of stop de doorgifte.
- Bronnen: AVG-art46-lid1 (AVG art. 46 lid 1); HvJEU-C-311-18 (HvJEU 16 juli 2020, C-311/18, Data Protection Commissioner/Facebook Ireland en Schrems (Schrems II)); EDPB-AB-01-2020 (EDPB, Aanbevelingen 01/2020 over maatregelen ter aanvulling van doorgifte-instrumenten om te waarborgen dat het EU-niveau van bescherming van persoonsgegevens wordt nageleefd)

### K13c.6 — Of de toets is vastgelegd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De partijen documenteren de beoordeling en stellen die op verzoek ter beschikking van de toezichthouder (clausule 14 sub d)
- Grondslag: clausule 14 sub d; art. 5 lid 2 AVG
- Alleen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: documented
- Beoordeling:
  - present als documented true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg de doorgiftetoets vast, zodat je hem op verzoek aan de toezichthouder kunt geven.
- Bronnen: SCC-clausule14-d (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub d); AVG-art5-lid2 (AVG art. 5 lid 2)

### K13c.7 — Of de toets periodiek opnieuw wordt bekeken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: De organisatie herbeoordeelt de toets op passende momenten en volgt ontwikkelingen in het land van bestemming (EDPB stap 6)
- Grondslag: EDPB-aanbevelingen 01/2020; clausule 14 sub e
- Alleen als: `facts.adequacy != "adequacy_country" and facts.adequacy != "dpf_certified"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: reassessment
- Beoordeling:
  - present als reassessment true is; absent als false.
  - Geen uitdrukkelijke wettelijke termijn: ontbreken geeft review.
- Is het vereiste afwezig (*absent*): ⚠️
- Advies bij ❌ of ⚠️: Spreek af wanneer je de toets opnieuw bekijkt, bijvoorbeeld jaarlijks en bij nieuwe wetgeving in het land van bestemming.
- Bronnen: EDPB-AB-01-2020 (EDPB, Aanbevelingen 01/2020 over maatregelen ter aanvulling van doorgifte-instrumenten om te waarborgen dat het EU-niveau van bescherming van persoonsgegevens wordt nageleefd); SCC-clausule14-e (Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914) clausule 14 sub e)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): law_findings, supplementary_measures. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Bij een adequaatheidsbesluit of DPF-certificering: alle stappen na stap 2 n.v.t.
- Stap 4 en 5 (A): de beoordeling en de maatregelen zijn afwegingen; alleen een duidelijk ontbrekende beoordeling geeft non_compliant.

## Open punten en voorbehouden

- Actuele status van Uitvoeringsbesluit (EU) 2023/1795 (Data Privacy Framework) nagaan, en van andere adequaatheidsbesluiten.
- EDPB-aanbevelingen 01/2020 (versie 2.0) letterlijk nalezen.
