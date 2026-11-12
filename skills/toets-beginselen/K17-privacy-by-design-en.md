# Kader K17 — Privacy by design en by default

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of gegevensbescherming is ingebouwd in een nieuwe tool, dienst of proces (art. 25 lid 1 AVG), en of de standaardinstellingen op het minimum staan: hoeveelheid gegevens, bewaartermijn en toegankelijkheid (art. 25 lid 2 AVG).

Bronnen: AVG-art25 (AVG art. 25); AVG-art25-lid1 (AVG art. 25 lid 1); AVG-art25-lid2 (AVG art. 25 lid 2); AVG-art5-lid1 (AVG art. 5 lid 1); AVG-overw78 (AVG overweging 78); EDPB-RL-04-2019 (EDPB, Richtsnoeren 4/2019 inzake artikel 25 Gegevensbescherming door ontwerp en door standaardinstellingen, versie 2.0)

## Formulier (vragen aan de gebruiker)

- **tool_description**: Beschrijf kort de nieuwe tool, dienst of werkwijze: waarvoor gebruik je hem, van wie verwerkt hij gegevens, en welke gegevens?
  - Label (voor de plek-om-in-te-vullen): wat de tool, dienst of het proces doet
  - Hulp: Bijvoorbeeld: 'Een online planningstool voor onze thuiszorgmedewerkers met naam, adres en zorgtijden van cliënten.'
  - Type: text
- **design_measures**: Welke maatregelen heb je bij het inrichten genomen om zo weinig mogelijk gegevens te gebruiken en ze goed te beschermen?
  - Label (voor de plek-om-in-te-vullen): welke privacymaatregelen in het ontwerp zitten
  - Hulp: Bijvoorbeeld: namen vervangen door codes (pseudonimiseren), alleen noodzakelijke velden, automatisch verwijderen na een termijn, toegang per rol, versleuteling. Heb je niets bijzonders geregeld, zeg dat dan gewoon.
  - Type: text
- **risk_level**: Hoe gevoelig zijn de gegevens en het gebruik ervan, denk je?
  - Label (voor de plek-om-in-te-vullen): hoe gevoelig de gegevens en de verwerking zijn
  - Hulp: Hoog: bijvoorbeeld gezondheid, financiële gegevens, gegevens van kinderen, of heel veel mensen. Laag: bijvoorbeeld alleen zakelijke contactgegevens.
  - Type: enum (low / medium / high)
- **default_only_necessary_fields**: Vraagt de tool standaard alleen de gegevens die je voor dit doel echt nodig hebt, en zijn andere velden optioneel?
  - Label (voor de plek-om-in-te-vullen): of standaard alleen de nodige gegevens worden gevraagd
  - Hulp: Kijk naar de verplichte velden in formulieren en naar wat de tool automatisch vastlegt, zoals locatie of apparaatgegevens.
  - Type: boolean
- **default_fields_description**: Welke gegevens zijn verplicht of worden standaard vastgelegd?
  - Label (voor de plek-om-in-te-vullen): welke gegevens standaard worden verzameld
  - Type: text
- **default_retention_minimal**: Staat de standaard bewaartermijn in de tool op de kortste termijn die je voor dit doel nodig hebt?
  - Label (voor de plek-om-in-te-vullen): of de standaard bewaartermijn op het minimum staat
  - Hulp: Bijvoorbeeld: gegevens worden automatisch verwijderd na afloop van de termijn. 'Voor altijd bewaren' als standaard is meestal te lang.
  - Type: boolean
- **default_retention_setting**: Wat is de standaard bewaartermijn in de tool, en waarom is die nodig?
  - Label (voor de plek-om-in-te-vullen): de standaard bewaartermijn
  - Type: text
- **public_by_default**: Worden gegevens standaard zichtbaar voor een onbepaald aantal mensen, zonder dat iemand dat eerst zelf aanzet?
  - Label (voor de plek-om-in-te-vullen): of gegevens standaard voor iedereen zichtbaar zijn
  - Hulp: Bijvoorbeeld profielen die standaard openbaar zijn, of een gedeelde link die iedereen kan openen. Zichtbaar alleen voor bevoegde collega's telt niet.
  - Type: boolean
- **uses_external_vendor**: Gebruik je hiervoor software of een online dienst van een leverancier?
  - Label (voor de plek-om-in-te-vullen): of je een tool of dienst van een leverancier gebruikt
  - Type: boolean
- **vendor_privacy_considered**: Heb je bij de keuze van de leverancier gekeken naar privacyvriendelijke instellingen en opties, en die zo nodig aangepast?
  - Label (voor de plek-om-in-te-vullen): of je bij de keuze op privacyinstellingen hebt gelet
  - Type: boolean · Alleen vragen als: `facts.uses_external_vendor == true`
- **vendor_defaults_exceed_need**: Verzamelt of deelt de dienst met de standaardinstellingen meer gegevens dan je nodig hebt, en staan die instellingen nog zo?
  - Label (voor de plek-om-in-te-vullen): of de standaardinstellingen van de dienst meer verzamelen dan nodig
  - Hulp: Bijvoorbeeld standaard aanstaande analyse- of trackingfuncties, of het delen van gegevens met de leverancier voor productverbetering.
  - Type: boolean · Alleen vragen als: `facts.uses_external_vendor == true`

## Toetspunten

### K17.1 — Of privacy in het ontwerp is ingebouwd
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bij het ontwerp en bij de verwerking zelf zijn passende technische en organisatorische maatregelen genomen om de beginselen van art. 5 uit te voeren, rekening houdend met de stand van de techniek, de uitvoeringskosten, de aard, omvang, context en doelen, en de risico's
- Grondslag: art. 25 lid 1 AVG
- Beoordeeld op: de antwoorden
- Nodig: tool_description, design_measures, risk_level
- Beoordeling:
  - Duidelijk compliant: design_measures noemt concrete maatregelen die passen bij de gegevens en het risico uit tool_description, zoals pseudonimisering, minimalisatie, automatische verwijdering, toegang per rol, en de standaardinstellingen (stap 2-4) staan op het minimum.
  - Duidelijk non_compliant: design_measures zegt dat er niets is geregeld of noemt geen enkele maatregel, terwijl risk_level high is of tool_description gevoelige gegevens noemt.
  - Art. 25 laat ruimte voor een afweging van techniek, kosten en risico; alleen een duidelijk geval geeft compliant of non_compliant.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de genoemde maatregelen passend bij de aard van de gegevens en het risico van deze verwerking?
- Advies bij ❌ of ⚠️: Bouw privacy in de inrichting in: gebruik alleen de gegevens die nodig zijn, vervang namen door codes waar dat kan, stel automatische verwijdering in en geef alleen toegang aan wie het nodig heeft.
- Bronnen: AVG-art25-lid1 (AVG art. 25 lid 1); AVG-art5-lid1 (AVG art. 5 lid 1); EDPB-RL-04-2019 (EDPB, Richtsnoeren 4/2019 inzake artikel 25 Gegevensbescherming door ontwerp en door standaardinstellingen, versie 2.0)

### K17.2 — Standaard alleen de gegevens die nodig zijn
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Standaard worden alleen persoonsgegevens verwerkt die noodzakelijk zijn voor elk specifiek doel, wat betreft de hoeveelheid verzamelde gegevens en de mate waarin ze worden verwerkt
- Grondslag: art. 25 lid 2 AVG
- Beoordeeld op: de antwoorden
- Nodig: default_only_necessary_fields
- Beoordeling:
  - Aanwezig als default_only_necessary_fields true is en default_fields_description (als ingevuld) geen gegevens noemt die voor het doel in tool_description kennelijk niet nodig zijn.
  - Afwezig als default_only_necessary_fields false is.
  - default_only_necessary_fields true maar default_fields_description noemt verplichte velden die voor het doel niet nodig lijken: twijfel (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn alle verplichte of standaard verzamelde gegevens nodig voor het doel?
- Advies bij ❌ of ⚠️: Maak alleen de velden verplicht die je voor het doel echt nodig hebt, maak de rest optioneel en zet automatische registratie van extra gegevens standaard uit.
- Bronnen: AVG-art25-lid2 (AVG art. 25 lid 2); EDPB-RL-04-2019 (EDPB, Richtsnoeren 4/2019 inzake artikel 25 Gegevensbescherming door ontwerp en door standaardinstellingen, versie 2.0)

### K17.3 — Standaard zo kort mogelijk bewaren
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De standaardbewaartermijn staat op het minimum dat voor het doel nodig is
- Grondslag: art. 25 lid 2 AVG
- Beoordeeld op: de antwoorden
- Nodig: default_retention_minimal
- Beoordeling:
  - Aanwezig als default_retention_minimal true is en default_retention_setting (als ingevuld) een termijn of criterium noemt.
  - Afwezig als default_retention_minimal false is, of default_retention_setting zegt dat gegevens standaard onbeperkt worden bewaard.
  - De juistheid van de termijn zelf wordt getoetst bij bewaartermijnen (K4); hier gaat het om de standaardinstelling.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Staat de standaardbewaartermijn op het minimum voor het doel?
- Advies bij ❌ of ⚠️: Stel in de tool een standaard bewaartermijn in die niet langer is dan nodig, bij voorkeur met automatische verwijdering.
- Bronnen: AVG-art25-lid2 (AVG art. 25 lid 2); EDPB-RL-04-2019 (EDPB, Richtsnoeren 4/2019 inzake artikel 25 Gegevensbescherming door ontwerp en door standaardinstellingen, versie 2.0)

### K17.4 — Gegevens niet standaard voor iedereen zichtbaar
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Gegevens worden standaard niet zonder menselijke tussenkomst toegankelijk gemaakt voor een onbepaald aantal natuurlijke personen
- Grondslag: art. 25 lid 2 AVG
- Beoordeeld op: de antwoorden
- Nodig: public_by_default
- Beoordeling:
  - Aanwezig als public_by_default false is.
  - Afwezig als public_by_default true is (bijvoorbeeld profielen standaard openbaar).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Worden gegevens standaard alleen gedeeld met bevoegde personen?
- Advies bij ❌ of ⚠️: Zet de standaardinstelling op 'niet openbaar': laat gegevens alleen zichtbaar worden voor een grotere groep als iemand dat zelf bewust aanzet.
- Bronnen: AVG-art25-lid2 (AVG art. 25 lid 2); EDPB-RL-04-2019 (EDPB, Richtsnoeren 4/2019 inzake artikel 25 Gegevensbescherming door ontwerp en door standaardinstellingen, versie 2.0)

### K17.5 — Of je bij de keuze van een leverancier op privacy hebt gelet
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bij de keuze van een leverancier is gelet op privacyvriendelijke instellingen en opties (overweging 78)
- Grondslag: art. 25 AVG; overweging 78 AVG
- Alleen als: `facts.uses_external_vendor == true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: vendor_privacy_considered, vendor_defaults_exceed_need
- Beoordeling:
  - Duidelijk compliant: vendor_privacy_considered true én vendor_defaults_exceed_need false.
  - vendor_defaults_exceed_need true: standaardinstellingen van een SaaS-dienst die meer verzamelen dan nodig → geen duidelijk geval (review), met het advies de instellingen aan te passen.
  - vendor_privacy_considered false: geen duidelijk geval.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Verzamelt of deelt de dienst met de huidige instellingen meer dan nodig, en kan de klant dat aanpassen?
- Advies bij ❌ of ⚠️: Loop de instellingen van de dienst na en zet functies die meer gegevens verzamelen of delen dan je nodig hebt uit. Let bij een nieuwe leverancier vooraf op privacyvriendelijke opties.
- Bronnen: AVG-art25 (AVG art. 25); AVG-overw78 (AVG overweging 78); EDPB-RL-04-2019 (EDPB, Richtsnoeren 4/2019 inzake artikel 25 Gegevensbescherming door ontwerp en door standaardinstellingen, versie 2.0)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): tool_description, uses_external_vendor. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Art. 25 is resultaatgericht maar laat ruimte → stap 1 en 5 alleen compliant of non_compliant bij een duidelijk geval; anders review.
- Stap 2-4 zijn concreet toetsbaar aan de gekozen instellingen.
- Stap 5: standaardinstellingen van een SaaS-dienst die meer verzamelen dan nodig → review met advies de instellingen aan te passen.

## Open punten en voorbehouden

- Overweging 78 richt zich deels tot producenten; de plicht uit art. 25 ligt bij de verwerkingsverantwoordelijke. Stap 5 blijft daarom een afwegingsstap.
