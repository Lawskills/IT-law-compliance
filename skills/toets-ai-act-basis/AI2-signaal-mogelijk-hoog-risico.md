# Kader AI2 — Signaal: mogelijk hoog risico

Versie 0.4 · peildatum 2026-11-10

Doel: Signaleren of een AI-toepassing mogelijk een hoog-risicosysteem is (art. 6 met bijlage I of bijlage III), zodat de organisatie op tijd kan voorbereiden. De plichten gelden vanaf 2 december 2027 (bijlage III) en 2 augustus 2028 (bijlage I). Deze skill classificeert niet definitief.

Geldt alleen als: `facts.system_infers != false` · poortstap AI0.1 — vervalt als de toepassing duidelijk geen AI-systeem is (regel van kader AI0)

Bronnen: AIVO-art6-lid1 (AI-verordening art. 6 lid 1); AIVO-art6-lid1a (AI-verordening art. 6 lid 1a); AIVO-art6-lid1b (AI-verordening art. 6 lid 1b); AIVO-art6-lid1c (AI-verordening art. 6 lid 1c); AIVO-art6-lid2 (AI-verordening art. 6 lid 2); AIVO-art6-lid3 (AI-verordening art. 6 lid 3); AIVO-art6-lid4 (AI-verordening art. 6 lid 4); AIVO-art26 (AI-verordening art. 26); AIVO-art27 (AI-verordening art. 27); AIVO-art49-lid2 (AI-verordening art. 49 lid 2); AIVO-art113 (AI-verordening art. 113); AIVO-bijlage1 (AI-verordening bijlage I); AIVO-bijlage3 (AI-verordening bijlage III); AIVO-overw53 (AI-verordening overweging 53); AIVO-overw57 (AI-verordening overweging 57); AIVO-overw58 (AI-verordening overweging 58); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

## Formulier (vragen aan de gebruiker)

- **app_purpose**: Waarvoor gebruik je de toepassing, en bij of over wie?
  - Label (voor de plek-om-in-te-vullen): waarvoor en bij wie je de toepassing gebruikt
  - Hulp: Overgenomen uit de eerste vragen over deze toepassing. Vul aan als dat nodig is.
  - Type: text
- **annex1_product**: Is de toepassing zelf een product, of een veiligheidsonderdeel van een product, waarvoor Europese veiligheidsregels gelden en een keuring door een externe instantie nodig is?
  - Label (voor de plek-om-in-te-vullen): of de toepassing (onderdeel van) een product is waarvoor Europese veiligheidsregels gelden
  - Hulp: Bijvoorbeeld medische hulpmiddelen, speelgoed, liften, voertuigen, drukapparatuur of radioapparatuur. Een AI-functie die alleen het gebruiksgemak of de efficiëntie verbetert, telt niet, tenzij een storing de gezondheid of veiligheid in gevaar brengt.
  - Type: boolean
- **annex1_product_type**: Om welk product gaat het, en wat doet de AI-functie daarin?
  - Label (voor de plek-om-in-te-vullen): om welk product het gaat
  - Type: text · Alleen vragen als: `facts.annex1_product != false`
- **annex3_area**: Gebruik je de toepassing voor een van deze doelen?
  - Label (voor de plek-om-in-te-vullen): in welk gevoelig gebied je de toepassing gebruikt
  - Hulp: Kies het doel dat het best past. Twijfel je, kies dan 'Weet ik niet'.
  - Type: enum (none / employment / education / credit_scoring / life_health_insurance / biometric_identification / biometric_categorisation_or_emotion / critical_infrastructure / public_services / law_enforcement_migration_justice_elections)
- **annex3_description**: Beschrijf kort wat de toepassing in dat gebied doet en wie er de gevolgen van merkt.
  - Label (voor de plek-om-in-te-vullen): hoe de toepassing in dat gebied wordt gebruikt
  - Hulp: Bijvoorbeeld: 'Het systeem rangschikt binnenkomende cv's; een recruiter bekijkt alleen de bovenste tien.'
  - Type: text · Alleen vragen als: `facts.annex3_area != "none"`
- **provider_claims_not_high_risk**: Zegt de leverancier (of zeg je als aanbieder) dat het systeem geen hoog risico is, ook al wordt het in dit gebied gebruikt?
  - Label (voor de plek-om-in-te-vullen): of de aanbieder zegt dat het systeem geen hoog risico is
  - Hulp: Een aanbieder mag dat alleen als het systeem een beperkte, ondersteunende taak heeft en geen profielen van personen maakt, en moet dat vastleggen en registreren.
  - Type: boolean · Alleen vragen als: `facts.annex3_area != "none"`
- **profiling**: Beoordeelt het systeem individuele personen, of voorspelt het iets over hen, zoals hun prestaties, betrouwbaarheid, gedrag of voorkeuren?
  - Label (voor de plek-om-in-te-vullen): of het systeem personen beoordeelt of voorspellingen over hen doet
  - Type: boolean · Alleen vragen als: `facts.annex3_area != "none"`

## Toetspunten

### AI2.1 — Of je toepassing onder de productregels valt (mogelijk hoog risico vanaf 2 augustus 2028)
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Signaal: het AI-systeem is een product, of een veiligheidscomponent van een product, onder de harmonisatiewetgeving van bijlage I, waarvoor een conformiteitsbeoordeling door een derde vereist is
- Grondslag: art. 6 lid 1, 1a-1c en bijlage I AI-verordening; art. 113 (zoals gewijzigd bij Verordening (EU) 2026/1744)
- Alleen als: `facts.annex1_product != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: annex1_product
- Beoordeling:
  - Deze stap signaleert en classificeert niet: de uitkomst is altijd review. Onderbouw welk signaal er is en noem de toepassingsdatum 2 augustus 2028.
  - Beide voorwaarden van art. 6 lid 1 gelden cumulatief: (a) product of veiligheidscomponent onder bijlage I, en (b) conformiteitsbeoordeling door een derde vereist.
  - Sinds Verordening (EU) 2026/1744: een systeem dat uitsluitend wordt gebruikt voor niet-veiligheidsgerelateerde gebruikersondersteuning, prestatie-optimalisatie, efficiëntie, automatisering, gemak of kwaliteitscontrole is geen veiligheidscomponent (lid 1a), maar een systeem waarvan falen of storing de gezondheid en veiligheid in gevaar brengt wel (lid 1b); een product dat alleen vanwege andere risico's dan gezondheid en veiligheid door een derde moet worden beoordeeld, voldoet niet aan lid 1 sub b (lid 1c). Wijst annex1_product_type daarop, vermeld dat in de onderbouwing.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Is het AI-systeem een (veiligheidscomponent van een) product onder bijlage I waarvoor een conformiteitsbeoordeling door een derde vereist is (art. 6 lid 1 en lid 1a-1c)?
- Advies bij ❌ of ⚠️: Mogelijk hoog risico vanaf 2 augustus 2028. Laat een juridisch adviseur beoordelen of de AI-functie een veiligheidscomponent is en of een keuring door een externe instantie nodig is, en vraag de fabrikant welke eisen hij volgt.
- Bronnen: AIVO-art6-lid1 (AI-verordening art. 6 lid 1); AIVO-art6-lid1a (AI-verordening art. 6 lid 1a); AIVO-art6-lid1b (AI-verordening art. 6 lid 1b); AIVO-art6-lid1c (AI-verordening art. 6 lid 1c); AIVO-bijlage1 (AI-verordening bijlage I); AIVO-art113 (AI-verordening art. 113); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI2.2 — Of je de toepassing gebruikt in een gevoelig gebied (mogelijk hoog risico vanaf 2 december 2027)
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Signaal: het AI-systeem wordt gebruikt in een gebied van bijlage III (biometrie, kritieke infrastructuur, onderwijs, werk, essentiële diensten waaronder krediet en levens- en ziektekostenverzekeringen, rechtshandhaving, migratie, rechtspraak en democratische processen)
- Grondslag: art. 6 lid 2 en bijlage III AI-verordening; art. 113 (zoals gewijzigd bij Verordening (EU) 2026/1744)
- Alleen als: `facts.annex3_area != "none"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: annex3_area, app_purpose
- Beoordeling:
  - Deze stap signaleert en classificeert niet: de uitkomst is altijd review. Noem het gebied, het betreffende punt van bijlage III en de toepassingsdatum 2 december 2027.
  - Werk (bijlage III punt 4): werving en selectie (gerichte vacatures, sollicitaties analyseren en filteren, kandidaten beoordelen); besluiten over arbeidsvoorwaarden, promotie of ontslag; taken toewijzen op basis van individueel gedrag of persoonlijke kenmerken; prestaties en gedrag monitoren en beoordelen.
  - Onderwijs (punt 3): toegang of toelating, beoordelen van leerresultaten, het passende onderwijsniveau bepalen, toezicht op verboden gedrag tijdens toetsen.
  - Krediet (punt 5 sub b): kredietwaardigheid of kredietscore van natuurlijke personen; niet voor systemen die uitsluitend fraude opsporen. Verzekeringen (punt 5 sub c): alleen levens- en ziektekostenverzekeringen van natuurlijke personen. Wijst app_purpose of annex3_description op fraudedetectie of een ander type verzekering, vermeld dat het signaal mogelijk vervalt.
  - Biometrie (punt 1): identificatie op afstand (niet: verificatie van wie iemand zegt te zijn), categorisering naar gevoelige kenmerken, en emotieherkenning. Emotieherkenning op het werk of in het onderwijs is verboden (AI1 stap 6).
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Valt het beoogde gebruik onder een punt van bijlage III, en geldt een van de uitzonderingen binnen dat punt (bijvoorbeeld fraudedetectie of biometrische verificatie)?
- Advies bij ❌ of ⚠️: Mogelijk hoog risico vanaf 2 december 2027. Laat een juridisch adviseur de toepassing classificeren. Vraag de leverancier nu al om documentatie en een gebruiksaanwijzing, regel menselijk toezicht en doe een DPIA als de toepassing persoonsgegevens verwerkt. Gebruik je de toepassing voor medewerkers, betrek dan de ondernemingsraad; voor systemen die medewerkers volgen of beoordelen is naar Nederlands recht vaak nu al instemming nodig.
- Bronnen: AIVO-art6-lid2 (AI-verordening art. 6 lid 2); AIVO-bijlage3 (AI-verordening bijlage III); AIVO-overw57 (AI-verordening overweging 57); AIVO-overw58 (AI-verordening overweging 58); AIVO-art113 (AI-verordening art. 113); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI))

### AI2.3 — Of de uitzondering voor systemen zonder groot risico kan gelden
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Bij een bijlage III-gebied en een beroep op art. 6 lid 3: de voorwaarden van de uitzondering (sub a-d, geen profilering) en de documentatie en registratie door de aanbieder (art. 6 lid 4, art. 49 lid 2)
- Grondslag: art. 6 lid 3 en 4 en art. 49 lid 2 AI-verordening; overweging 53
- Alleen als: `facts.annex3_area != "none" and facts.provider_claims_not_high_risk != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: provider_claims_not_high_risk, profiling
- Beoordeling:
  - Deze stap geeft altijd review: Deze toets beoordeelt de uitzondering niet definitief.
  - De uitzondering vereist dat het systeem geen significant risico vormt en (a) een beperkte procedurele taak uitvoert, (b) het resultaat van een eerder voltooide menselijke activiteit verbetert, (c) besluitvormingspatronen of afwijkingen detecteert zonder de menselijke beoordeling te vervangen of te beïnvloeden zonder behoorlijke menselijke toetsing, of (d) een voorbereidende taak uitvoert.
  - Bij profiling true geldt de uitzondering nooit (art. 6 lid 3, laatste alinea): vermeld dat het systeem dan hoog risico blijft.
  - Het is de aanbieder die de beoordeling vóór het in de handel brengen documenteert (lid 4) en het systeem registreert (art. 49 lid 2). Een gebruiksverantwoordelijke kan zich er niet zelf op beroepen, maar kan de documentatie opvragen.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Voldoet het systeem aan een van de voorwaarden van art. 6 lid 3 sub a-d zonder profilering, en heeft de aanbieder de beoordeling gedocumenteerd en geregistreerd?
- Advies bij ❌ of ⚠️: Vraag de aanbieder om de vastgelegde beoordeling waarom het systeem geen hoog risico is, en om het registratienummer in de EU-databank. Maakt het systeem profielen van personen, dan geldt de uitzondering niet.
- Bronnen: AIVO-art6-lid3 (AI-verordening art. 6 lid 3); AIVO-art6-lid4 (AI-verordening art. 6 lid 4); AIVO-art49-lid2 (AI-verordening art. 49 lid 2); AIVO-overw53 (AI-verordening overweging 53)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): app_purpose. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 1 of 2 van toepassing (ja of 'weet ik niet') → kader review: 'mogelijk hoog risico', met de datum (2-8-2028 bijlage I, 2-12-2027 bijlage III) en het advies een juridisch adviseur te laten classificeren.
- Geen signaal (annex1_product false en annex3_area none) → alle stappen not_applicable → kader not_applicable (geen compliant, omdat deze skill niet definitief classificeert).
- Het rapport noemt wat de organisatie nu al kan doen (documentatie opvragen, menselijk toezicht, DPIA, ondernemingsraad, FRIA voorbereiden); dat zijn geen toetspunten.

## Samenhang met andere kaders

- Kader K16 (/toets-geautomatiseerde-besluiten) — als `facts.annex3_area == "employment" or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance" or facts.annex3_area == "education"`: Beslissingen over sollicitanten, werknemers, leerlingen, krediet of verzekeringen kunnen ook onder de AVG-regels voor geautomatiseerde besluiten vallen.
- Kader K9 (/dpia) — als `facts.annex3_area != "none" or facts.annex1_product != false`: Voor een mogelijk hoog-risicosysteem dat persoonsgegevens verwerkt, is vrijwel altijd een DPIA nodig.
- Kader K3 (/toets-grondslag) — als `facts.annex3_area == "biometric_identification" or facts.annex3_area == "biometric_categorisation_or_emotion"`: Biometrische gegevens zijn bijzondere persoonsgegevens (art. 9 AVG, art. 29 UAVG).
- Kader AI5 (/toets-ai-act-hoog-risico) — als `facts.annex3_area != "none" or facts.annex1_product != false`: Gebruik je het systeem onder je eigen verantwoordelijkheid, dan gelden de plichten van de gebruiksverantwoordelijke (art. 26).
- Kader AI7 (/toets-ai-act-hoog-risico) — als `facts.annex3_area != "none" or facts.annex1_product != false`: Ontwikkel je het systeem of bied je het onder je eigen naam aan, dan gelden de plichten van de aanbieder (art. 16).

## Open punten en voorbehouden

- Concept-richtsnoeren classificatie hoog risico (Commissie, 19-5-2026) zijn nog een concept; na vaststelling de criteria aanscherpen.
- Samenloop met de WOR (instemmingsrecht ondernemingsraad bij personeelsvolgsystemen, art. 27 lid 1 sub l WOR) in een apart kader of in K14/K17 vastleggen; nu alleen in de suggestie genoemd.
