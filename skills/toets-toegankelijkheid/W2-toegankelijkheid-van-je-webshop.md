# Kader W2 — Toegankelijkheid van je webshop of app (EAA)

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of een webshop of app waarmee consumenten overeenkomsten sluiten onder de toegankelijkheidsregels valt, of de toegankelijkheid is getoetst aan de geharmoniseerde norm, of de verplichte informatie over toegankelijkheid is gepubliceerd en of een beroep op onevenredige last is onderbouwd.

Bronnen: EAA-art13-lid2 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 13 lid 2); EAA-art14-lid1 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 14 lid 1); EAA-art14-lid2 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 14 lid 2); EAA-art15-lid1 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 15 lid 1); EAA-art2-lid2 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 2 lid 2); EAA-art4-lid1 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 4 lid 1); EAA-art4-lid3 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 4 lid 3); EAA-art4-lid5 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 4 lid 5); EAA-bijlage1 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) bijlage 1); EAA-bijlage5 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) bijlage 5)

## Formulier (vragen aan de gebruiker)

- **consumer_ecommerce**: Kunnen consumenten via je website of app producten of diensten kopen of een overeenkomst sluiten?
  - Label (voor de plek-om-in-te-vullen): of consumenten via je website of app bestellen
  - Type: boolean
- **microenterprise**: Heb je minder dan 10 medewerkers én een jaaromzet of balanstotaal van ten hoogste 2 miljoen euro?
  - Label (voor de plek-om-in-te-vullen): of je een micro-onderneming bent
  - Type: boolean
- **tested_against_standard**: Is je website of app getoetst aan de toegankelijkheidsnorm (EN 301 549 / WCAG 2.1 niveau AA) en zijn de belangrijkste knelpunten opgelost?
  - Label (voor de plek-om-in-te-vullen): of de toegankelijkheid is getoetst
  - Type: boolean · Alleen vragen als: `facts.consumer_ecommerce != false and facts.microenterprise != true`
- **accessibility_info_published**: Staat in je voorwaarden of op je website hoe je dienst aan de toegankelijkheidseisen voldoet?
  - Label (voor de plek-om-in-te-vullen): of je informatie over toegankelijkheid publiceert
  - Type: boolean · Alleen vragen als: `facts.consumer_ecommerce != false and facts.microenterprise != true`
- **info_complete**: Beschrijft die informatie de dienst in toegankelijke vorm, hoe aan de eisen wordt voldaan, en hoe mensen contact opnemen over toegankelijkheid?
  - Label (voor de plek-om-in-te-vullen): of die informatie volledig is
  - Type: boolean · Alleen vragen als: `facts.accessibility_info_published != false`
- **claims_burden**: Beroep je je erop dat volledige toegankelijkheid een onevenredige last is, of de dienst fundamenteel zou veranderen?
  - Label (voor de plek-om-in-te-vullen): of je je beroept op een uitzondering
  - Type: boolean · Alleen vragen als: `facts.consumer_ecommerce != false and facts.microenterprise != true`
- **burden_documented**: Heb je die beoordeling schriftelijk vastgelegd met de kosten en baten, en kun je die aan de ACM tonen?
  - Label (voor de plek-om-in-te-vullen): of je die beoordeling hebt vastgelegd
  - Type: boolean · Alleen vragen als: `facts.consumer_ecommerce != false and facts.microenterprise != true and facts.claims_burden != false`

## Toetspunten

### W2.1 — Of de toegankelijkheidsregels voor je gelden
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: E-commercediensten voor consumenten moeten sinds 28 juni 2025 toegankelijk zijn; micro-ondernemingen die diensten verlenen zijn uitgezonderd
- Grondslag: art. 2 lid 2 en art. 4 Richtlijn (EU) 2019/882; Implementatiewet toegankelijkheidsvoorschriften
- Beoordeeld op: de antwoorden
- Nodig: consumer_ecommerce, microenterprise
- Beoordeling:
  - Altijd review: vermeld of de regels waarschijnlijk gelden (consumer_ecommerce true en microenterprise false).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Valt de dienst onder de Europese toegankelijkheidsakte?
- Advies bij ❌ of ⚠️: Ga na of je webshop of app onder de toegankelijkheidsregels valt.
- Bronnen: EAA-art2-lid2 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 2 lid 2); EAA-art4-lid1 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 4 lid 1); EAA-art4-lid5 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 4 lid 5)

### W2.2 — Of je website of app aan de toegankelijkheidseisen voldoet
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De dienst voldoet aan de toegankelijkheidseisen van bijlage I; toepassing van de geharmoniseerde norm (EN 301 549, met WCAG 2.1 AA) geeft een vermoeden van conformiteit
- Grondslag: art. 4 lid 3 en art. 15 Richtlijn (EU) 2019/882, bijlage I
- Alleen als: `facts.consumer_ecommerce != false and facts.microenterprise != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: tested_against_standard
- Beoordeling:
  - present als tested_against_standard true is; absent als false.
  - deze skill test de website niet zelf.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Laat je website of app toetsen aan EN 301 549 / WCAG 2.1 AA en los de knelpunten op.
- Bronnen: EAA-art4-lid3 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 4 lid 3); EAA-art15-lid1 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 15 lid 1); EAA-bijlage1 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) bijlage 1)

### W2.3 — Of je informatie over toegankelijkheid publiceert
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De dienstverlener neemt in de algemene voorwaarden of een gelijkwaardig document informatie op over hoe de dienst aan de eisen voldoet (bijlage V)
- Grondslag: art. 13 lid 2 en bijlage V Richtlijn (EU) 2019/882
- Alleen als: `facts.consumer_ecommerce != false and facts.microenterprise != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: accessibility_info_published
- Beoordeling:
  - present als accessibility_info_published true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Publiceer in je voorwaarden of op je website hoe je dienst aan de toegankelijkheidseisen voldoet.
- Bronnen: EAA-art13-lid2 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 13 lid 2); EAA-bijlage5 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) bijlage 5)

### W2.4 — Of die informatie volledig is
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De informatie beschrijft de dienst in toegankelijke vorm, hoe aan de eisen wordt voldaan, en de contactmogelijkheden
- Grondslag: bijlage V Richtlijn (EU) 2019/882
- Alleen als: `facts.consumer_ecommerce != false and facts.microenterprise != true and facts.accessibility_info_published != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: info_complete
- Beoordeling:
  - present als info_complete true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vul de toegankelijkheidsinformatie aan: beschrijving van de dienst, hoe je aan de eisen voldoet en hoe mensen contact opnemen.
- Bronnen: EAA-bijlage5 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) bijlage 5)

### W2.5 — Of een beroep op onevenredige last is onderbouwd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Beroept de dienstverlener zich op een fundamentele wijziging of onevenredige last, dan legt hij die beoordeling vast, bewaart hij haar en kan hij haar aan de markttoezichthouder tonen
- Grondslag: art. 14 Richtlijn (EU) 2019/882
- Alleen als: `facts.consumer_ecommerce != false and facts.microenterprise != true and facts.claims_burden != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: burden_documented
- Beoordeling:
  - present als burden_documented true is; absent als false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Leg de beoordeling van de onevenredige last schriftelijk vast, met kosten en baten, en bewaar die voor de ACM.
- Bronnen: EAA-art14-lid1 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 14 lid 1); EAA-art14-lid2 (Europese toegankelijkheidsakte (Richtlijn (EU) 2019/882) art. 14 lid 2)

## Regels van dit kader

- Micro-onderneming of geen e-commerce voor consumenten → alle stappen n.v.t.
- Stap 1 is altijd review.
- Een verplichte F-stap absent → non_compliant.

## Open punten en voorbehouden

- Implementatiewet en het besluit eronder letterlijk nalezen (artikelnummers, overgangstermijn tot 28-06-2030 voor bestaande dienstverlening, onevenredige last en melding aan de ACM).
- De bijlage I-eisen per onderdeel (e-commerce, punt IV) nalezen.
