# Kader K16 — Geautomatiseerde besluitvorming en profilering

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of een besluit over een persoon volledig geautomatiseerd mag worden genomen (art. 22 AVG), en of de waarborgen er zijn: een uitzondering, menselijke tussenkomst, regels voor bijzondere gegevens, informatie vooraf en uitleg achteraf.

Bronnen: AVG-art4-4 (AVG art. 4 punt 4); AVG-art13-lid2-f (AVG art. 13 lid 2 sub f); AVG-art14-lid2-g (AVG art. 14 lid 2 sub g); AVG-art15-lid1-h (AVG art. 15 lid 1 sub h); AVG-art21 (AVG art. 21); AVG-art22 (AVG art. 22); UAVG-art40 (UAVG art. 40); HvJEU-C-634-21 (HvJEU 7 december 2023, C-634/21, SCHUFA Holding (Scoring)); HvJEU-C-203-22 (HvJEU 27 februari 2025, C-203/22, Dun & Bradstreet Austria); WP251-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake geautomatiseerde individuele besluitvorming en profilering (WP251 rev.01), bekrachtigd door de EDPB)

## Formulier (vragen aan de gebruiker)

- **decision_description**: Beschrijf kort wat de software, scoring of AI over mensen besluit of adviseert, welke gegevens erin gaan, en wat de gevolgen voor iemand zijn.
  - Label (voor de plek-om-in-te-vullen): wat het systeem besluit
  - Hulp: Bijvoorbeeld: 'Het systeem wijst sollicitanten zonder rijbewijs B automatisch af op basis van het sollicitatieformulier; zij krijgen direct een afwijzingsmail.'
  - Type: text
- **decision_domain**: Waar gaat het besluit over?
  - Label (voor de plek-om-in-te-vullen): waarvoor het besluit is
  - Hulp: Werving en selectie, krediet of betalen achteraf, verzekeringen, prijzen, fraudecontrole, toegang tot een dienst of account, of iets anders.
  - Type: enum (recruitment / credit / insurance / pricing / fraud_detection / service_access / other)
- **uses_ai**: Gebruikt het systeem kunstmatige intelligentie, bijvoorbeeld een zelflerend model of een AI-dienst van een leverancier?
  - Label (voor de plek-om-in-te-vullen): of je AI gebruikt voor het besluit
  - Hulp: Een vaste regel die je zelf hebt ingesteld (zoals 'jonger dan 18 jaar = afwijzen') is geen AI.
  - Type: boolean
- **uses_profiling**: Beoordeelt het systeem persoonlijke kenmerken van mensen, zoals hun betaalgedrag, werkprestaties, voorkeuren, betrouwbaarheid of gedrag?
  - Label (voor de plek-om-in-te-vullen): of je mensen profileert
  - Hulp: Dit heet profilering. Denk aan een score, een risicoklasse of een voorspelling over een persoon.
  - Type: boolean
- **solely_automated**: Komt het besluit tot stand zonder dat een medewerker het inhoudelijk beoordeelt en er ook van kan en mag afwijken?
  - Label (voor de plek-om-in-te-vullen): of het besluit zonder inhoudelijke menselijke beoordeling tot stand komt
  - Hulp: Kies 'ja' ook als een medewerker de uitkomst alleen overneemt of afstempelt, of als je een score van een ander bedrijf (bijvoorbeeld een kredietbureau) in de praktijk altijd volgt. Kies 'nee' alleen als een medewerker met voldoende kennis en bevoegdheid elk geval echt bekijkt. Twijfel je, kies dan 'weet ik niet'.
  - Type: boolean
- **human_review_description**: Beschrijf wie het besluit beoordeelt, wat die persoon bekijkt, en hoe vaak die afwijkt van de uitkomst van het systeem.
  - Label (voor de plek-om-in-te-vullen): hoe de medewerker het besluit beoordeelt
  - Type: text · Alleen vragen als: `facts.solely_automated != true`
- **uses_third_party_score**: Gebruik je voor het besluit een score of beoordeling die een ander bedrijf over de persoon heeft gemaakt?
  - Label (voor de plek-om-in-te-vullen): of je een score van een ander bedrijf gebruikt
  - Hulp: Bijvoorbeeld een kredietscore van een kredietbureau of een fraudescore van een betaaldienst.
  - Type: boolean
- **significant_effect**: Heeft het besluit rechtsgevolgen of andere belangrijke gevolgen voor de persoon?
  - Label (voor de plek-om-in-te-vullen): of het besluit belangrijke gevolgen voor mensen heeft
  - Hulp: Bijvoorbeeld afwijzing van een sollicitatie, een lening, betalen achteraf of een verzekering, een duidelijk hogere prijs, of het blokkeren van een account. Een gewone productaanbeveling telt meestal niet.
  - Type: boolean
- **art22_exception**: Waarom mag je dit besluit volledig automatisch nemen?
  - Label (voor de plek-om-in-te-vullen): op welke uitzondering je het geautomatiseerde besluit baseert
  - Hulp: Kies 'nodig voor een overeenkomst' als het besluit nodig is om met de persoon zelf een overeenkomst te sluiten of uit te voeren; 'wettelijk toegestaan' als een wet het automatisch besluiten toestaat; 'uitdrukkelijke toestemming' als de persoon daar uitdrukkelijk mee heeft ingestemd; anders 'geen van deze'.
  - Type: enum (contract / law / explicit_consent / none) · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false`
- **exception_law_description**: Welke wet of wettelijke taak maakt het automatische besluit nodig?
  - Label (voor de plek-om-in-te-vullen): welke wet het besluit toestaat
  - Type: text · Alleen vragen als: `facts.art22_exception == "law"`
- **can_request_human_intervention**: Kan iemand vragen dat een medewerker naar het besluit kijkt?
  - Label (voor de plek-om-in-te-vullen): of mensen om een medewerker kunnen vragen
  - Type: boolean · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false and facts.art22_exception != "none"`
- **can_express_view**: Kan iemand zijn kant van het verhaal vertellen voordat of nadat het besluit is genomen?
  - Label (voor de plek-om-in-te-vullen): of mensen hun standpunt kunnen geven
  - Type: boolean · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false and facts.art22_exception != "none"`
- **can_contest**: Kan iemand bezwaar maken tegen het besluit, zodat het opnieuw wordt bekeken?
  - Label (voor de plek-om-in-te-vullen): of mensen het besluit kunnen aanvechten
  - Type: boolean · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false and facts.art22_exception != "none"`
- **uses_special_categories**: Gebruikt het systeem gegevens over gezondheid, afkomst, religie, politieke voorkeur, vakbondslidmaatschap, seksuele leven of geaardheid, of biometrische of genetische gegevens?
  - Label (voor de plek-om-in-te-vullen): of bijzondere gegevens meetellen in het besluit
  - Hulp: Ook als het systeem zulke gegevens zelf afleidt, bijvoorbeeld uit een foto of uit aankopen.
  - Type: boolean · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false`
- **special_categories_basis**: Op welke grond gebruik je die gegevens in het besluit?
  - Label (voor de plek-om-in-te-vullen): op welke grond je bijzondere gegevens gebruikt
  - Hulp: 'Uitdrukkelijke toestemming' als de persoon daar uitdrukkelijk mee instemde; 'zwaarwegend algemeen belang' als een wet dat voor dit doel regelt; anders 'geen van deze'.
  - Type: enum (explicit_consent / substantial_public_interest / none) · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false and facts.uses_special_categories == true`
- **special_categories_measures**: Heb je extra maatregelen genomen om de rechten van mensen te beschermen bij het gebruik van die gegevens?
  - Label (voor de plek-om-in-te-vullen): of je extra maatregelen neemt voor bijzondere gegevens
  - Hulp: Bijvoorbeeld strengere toegang, controle op discriminatie, of een medewerker die elk besluit met zulke gegevens bekijkt.
  - Type: boolean · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false and facts.uses_special_categories == true`
- **informs_beforehand**: Vertel je mensen vooraf dat er automatisch over hen wordt besloten, hoe dat ongeveer werkt, en wat de gevolgen voor hen kunnen zijn?
  - Label (voor de plek-om-in-te-vullen): of je mensen vooraf informeert over het automatische besluit
  - Hulp: Bijvoorbeeld in je privacyverklaring of bij het formulier waarmee iemand iets aanvraagt.
  - Type: boolean · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false`
- **can_explain_on_request**: Kun je iemand die erom vraagt uitleggen welke werkwijze en welke uitgangspunten zijn gebruikt om tot zijn besluit te komen?
  - Label (voor de plek-om-in-te-vullen): of je een besluit achteraf kunt uitleggen
  - Hulp: Het gaat om uitleg die de persoon begrijpt, bijvoorbeeld welke gegevens de doorslag gaven. Een ingewikkelde formule of de broncode alleen is niet genoeg.
  - Type: boolean · Alleen vragen als: `facts.solely_automated != false and facts.significant_effect != false`
- **dpia_done**: Heb je vóór de start een risicoanalyse voor privacy (DPIA) gedaan voor dit systeem?
  - Label (voor de plek-om-in-te-vullen): of je een DPIA hebt gedaan
  - Type: boolean · Alleen vragen als: `facts.uses_profiling != false and facts.significant_effect != false`

## Toetspunten

### K16.1 — Of het besluit volledig automatisch wordt genomen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Er is sprake van een besluit dat uitsluitend op geautomatiseerde verwerking berust
- Grondslag: art. 22 lid 1 AVG
- Beoordeeld op: de antwoorden
- Nodig: decision_description, solely_automated, uses_third_party_score
- Beoordeling:
  - Dit is een kwalificatiestap: 'compliant' betekent hier dat de kwalificatie (wel of geen uitsluitend geautomatiseerd besluit) duidelijk vaststaat; de toetsing van de waarborgen volgt in stap 3-6. Een duidelijk non_compliant geval bestaat bij deze stap niet.
  - Duidelijk geval (compliant): solely_automated is true en decision_description bevestigt dat het systeem zelf besluit; of solely_automated is false en human_review_description laat zien dat een medewerker elk geval inhoudelijk beoordeelt en in de praktijk kan en mag afwijken.
  - Een medewerker die het resultaat alleen overneemt of afstempelt, telt niet als menselijke tussenkomst (WP251). Blijkt dat uit human_review_description of decision_description terwijl solely_automated false is: geen duidelijk geval.
  - Een score van een derde die in doorslaggevende mate bepaalt of een contract wordt gesloten, valt onder het begrip besluit (C-634/21). uses_third_party_score true en decision_description of human_review_description laat zien dat de score in de praktijk steeds wordt gevolgd, terwijl solely_automated false is: geen duidelijk geval.
  - In alle andere gevallen geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Beoordeelt een bevoegde medewerker elk besluit inhoudelijk, of wordt de uitkomst van het systeem (of de score van een derde) in de praktijk steeds gevolgd?
- Advies bij ❌ of ⚠️: Stel vast of een medewerker elk besluit echt beoordeelt en kan afwijken. Is dat niet zo, dan gelden de extra regels voor volledig automatische besluiten.
- Bronnen: AVG-art22-lid1 (AVG art. 22 lid 1); AVG-art4-4 (AVG art. 4 punt 4); WP251-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake geautomatiseerde individuele besluitvorming en profilering (WP251 rev.01), bekrachtigd door de EDPB); HvJEU-C-634-21 (HvJEU 7 december 2023, C-634/21, SCHUFA Holding (Scoring))

### K16.2 — Of het besluit belangrijke gevolgen voor mensen heeft
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Het besluit heeft rechtsgevolgen voor de betrokkene of treft hem anderszins in aanmerkelijke mate
- Grondslag: art. 22 lid 1 AVG
- Beoordeeld op: de antwoorden
- Nodig: decision_description, significant_effect
- Beoordeling:
  - Dit is een kwalificatiestap: 'compliant' betekent hier dat de kwalificatie (wel of geen rechtsgevolg of aanmerkelijke gevolgen) duidelijk vaststaat. Een duidelijk non_compliant geval bestaat bij deze stap niet.
  - Duidelijk geval (compliant) als significant_effect true is en decision_description gaat over bijvoorbeeld afwijzing van een sollicitatie, krediet, betalen achteraf of een verzekering, of een sterk afwijkende prijs; of als significant_effect false is en decision_description geen van zulke gevolgen noemt.
  - significant_effect false terwijl decision_description een afwijzing, blokkade of sterk afwijkende prijs beschrijft: geen duidelijk geval.
  - In alle andere gevallen geen duidelijk geval.
  - Nee op stap 1 of 2: art. 22 is niet van toepassing; wel gelden de regels over de grondslag voor profilering, de informatieplicht en het recht van bezwaar (art. 21).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Heeft het besluit rechtsgevolgen of treft het de persoon in aanmerkelijke mate?
- Advies bij ❌ of ⚠️: Bepaal of het besluit rechtsgevolgen of andere belangrijke gevolgen voor mensen heeft, zoals een afwijzing of een duidelijk hogere prijs.
- Bronnen: AVG-art22-lid1 (AVG art. 22 lid 1); WP251-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake geautomatiseerde individuele besluitvorming en profilering (WP251 rev.01), bekrachtigd door de EDPB)

### K16.3 — Of je een geldige reden hebt om automatisch te besluiten
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Er geldt een uitzondering van art. 22 lid 2: noodzakelijk voor een overeenkomst, toegestaan bij wet, of uitdrukkelijke toestemming
- Grondslag: art. 22 lid 2 AVG; art. 40 UAVG
- Alleen als: `facts.solely_automated != false and facts.significant_effect != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: solely_automated, significant_effect, art22_exception
- Beoordeling:
  - Aanwezig bij art22_exception contract als decision_description laat zien dat het besluit nodig is om met de betrokkene zelf een overeenkomst te sluiten of uit te voeren.
  - Aanwezig bij art22_exception explicit_consent (de eisen aan de toestemming zelf worden apart getoetst).
  - Bij art22_exception law: aanwezig als exception_law_description een wettelijke verplichting of een taak van algemeen belang noemt waarvoor het besluit noodzakelijk is, en het besluit niet op profilering berust (uses_profiling false). Art. 40 UAVG geldt alleen voor besluiten die niet op profilering berusten; bij uses_profiling true of onbekend, of als exception_law_description geen concrete wet noemt: twijfel (⚠️).
  - Afwezig bij art22_exception none.
  - Overeenkomst met een ander dan de betrokkene, of twijfel of het besluit echt nodig is voor de overeenkomst: twijfel (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is het besluit echt nodig voor de overeenkomst met de betrokkene, of dekt de genoemde wet dit besluit?
- Advies bij ❌ of ⚠️: Neem het besluit niet volledig automatisch, maar laat een medewerker elk geval inhoudelijk beoordelen, tenzij het besluit nodig is voor een overeenkomst met de persoon zelf, een wet het toestaat of de persoon uitdrukkelijk toestemming geeft.
- Bronnen: AVG-art22-lid2 (AVG art. 22 lid 2); AVG-art22-lid2-a (AVG art. 22 lid 2 sub a); AVG-art22-lid2-b (AVG art. 22 lid 2 sub b); AVG-art22-lid2-c (AVG art. 22 lid 2 sub c); UAVG-art40 (UAVG art. 40); WP251-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake geautomatiseerde individuele besluitvorming en profilering (WP251 rev.01), bekrachtigd door de EDPB)

### K16.4 — Of mensen om een medewerker kunnen vragen en bezwaar kunnen maken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Waarborgen: bij uitzondering (a) of (c) het recht op menselijke tussenkomst, het recht om een standpunt kenbaar te maken en het recht om het besluit aan te vechten (art. 22 lid 3 AVG); bij uitzondering (b) via art. 40 UAVG passende maatregelen, voor een organisatie die geen bestuursorgaan is in ieder geval dezelfde drie rechten (art. 40 lid 2 en 3 UAVG)
- Grondslag: art. 22 lid 3 AVG; art. 40 lid 2 en 3 UAVG
- Alleen als: `facts.solely_automated != false and facts.significant_effect != false and facts.art22_exception != "none"` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: solely_automated, significant_effect, art22_exception, can_request_human_intervention, can_express_view, can_contest
- Beoordeling:
  - Aanwezig als can_request_human_intervention, can_express_view en can_contest alle drie true zijn.
  - Afwezig als een van de drie false is.
  - Bij uitzondering law: art. 40 UAVG geldt alleen voor besluiten die niet op profilering berusten; berust het besluit op profilering, dan is dat een tekort in stap 3, niet hier. Voor een bestuursorgaan volstaan volgens art. 40 lid 2 UAVG ook andere passende maatregelen: dan twijfel (⚠️) als niet alle drie de rechten er zijn.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de drie rechten (menselijke tussenkomst, standpunt, aanvechten) in de praktijk echt te gebruiken?
- Advies bij ❌ of ⚠️: Zorg dat iemand altijd kan vragen dat een medewerker naar het besluit kijkt, zijn kant van het verhaal kan vertellen en bezwaar kan maken, en vertel mensen hoe dat werkt.
- Bronnen: AVG-art22-lid3 (AVG art. 22 lid 3); UAVG-art40-lid2 (UAVG art. 40 lid 2); UAVG-art40-lid3 (UAVG art. 40 lid 3); WP251-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake geautomatiseerde individuele besluitvorming en profilering (WP251 rev.01), bekrachtigd door de EDPB)

### K16.5 — Of je bijzondere gegevens in het besluit mag gebruiken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Bijzondere categorieën van persoonsgegevens alleen met uitdrukkelijke toestemming of om redenen van zwaarwegend algemeen belang, én met passende maatregelen
- Grondslag: art. 22 lid 4 AVG
- Alleen als: `facts.solely_automated != false and facts.significant_effect != false and facts.uses_special_categories != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: solely_automated, significant_effect, uses_special_categories, special_categories_basis, special_categories_measures
- Beoordeling:
  - Aanwezig als special_categories_basis explicit_consent of substantial_public_interest is én special_categories_measures true is.
  - Afwezig als special_categories_basis none is, of special_categories_measures false is.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de grond voor het gebruik van bijzondere gegevens juist gekozen, en zijn de maatregelen passend?
- Advies bij ❌ of ⚠️: Gebruik gegevens over bijvoorbeeld gezondheid of afkomst niet in een automatisch besluit, tenzij de persoon daar uitdrukkelijk toestemming voor gaf of een wet dit om zwaarwegende redenen regelt, en neem extra beschermende maatregelen.
- Bronnen: AVG-art22-lid4 (AVG art. 22 lid 4); AVG-art9-lid2-a (AVG art. 9 lid 2 sub a); AVG-art9-lid2-g (AVG art. 9 lid 2 sub g)

### K16.6 — Of je mensen vooraf informeert en een besluit achteraf kunt uitleggen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Informatie vooraf over het bestaan, de onderliggende logica, het belang en de verwachte gevolgen; bij inzage uitleg over de gevolgde procedure en toegepaste beginselen
- Grondslag: art. 13 lid 2 sub f, art. 14 lid 2 sub g en art. 15 lid 1 sub h AVG
- Alleen als: `facts.solely_automated != false and facts.significant_effect != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: solely_automated, significant_effect, informs_beforehand, can_explain_on_request
- Beoordeling:
  - Aanwezig als informs_beforehand true én can_explain_on_request true is.
  - Afwezig als een van beide false is.
  - De tekst in de privacyverklaring zelf wordt getoetst in K5 stap 12; hier gaat het om de praktijk.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de informatie vooraf en de uitleg achteraf begrijpelijk genoeg voor de betrokkene?
- Advies bij ❌ of ⚠️: Vertel mensen vooraf dat er automatisch wordt besloten, hoe dat ongeveer werkt en wat de gevolgen kunnen zijn, en zorg dat je op verzoek begrijpelijk kunt uitleggen welke werkwijze en uitgangspunten tot het besluit leidden.
- Bronnen: AVG-art13-lid2-f (AVG art. 13 lid 2 sub f); AVG-art14-lid2-g (AVG art. 14 lid 2 sub g); AVG-art15-lid1-h (AVG art. 15 lid 1 sub h); HvJEU-C-203-22 (HvJEU 27 februari 2025, C-203/22, Dun & Bradstreet Austria); WP251-rev01 (Artikel 29-werkgroep, Richtsnoeren inzake geautomatiseerde individuele besluitvorming en profilering (WP251 rev.01), bekrachtigd door de EDPB)

### K16.7 — Of je een DPIA moet doen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: DPIA nodig? Profilering waarop besluiten met rechtsgevolgen berusten valt onder art. 35 lid 3 sub a
- Grondslag: art. 35 lid 3 sub a AVG
- Alleen als: `facts.uses_profiling != false and facts.significant_effect != false and facts.dpia_done != true` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: uses_profiling, significant_effect, dpia_done
- Beoordeling:
  - Signalerende stap: de DPIA-plicht zelf wordt in de DPIA-toets beoordeeld. Uitkomst hooguit review.
  - De stap geldt als profilering met rechtsgevolgen of aanmerkelijke gevolgen niet is uitgesloten en er (nog) geen DPIA is gedaan: een DPIA is dan meestal verplicht → review met verwijzing naar de DPIA-toets.
  - geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Is voor deze verwerking een DPIA verplicht, en is die vóór de start gedaan?
- Advies bij ❌ of ⚠️: Laat beoordelen of je voor dit systeem een DPIA moet doen. Bij profilering waarop besluiten met belangrijke gevolgen berusten, is dat meestal verplicht.
- Bronnen: AVG-art35-lid3-a (AVG art. 35 lid 3 sub a)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): decision_description, decision_domain. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 1 of 2 met zekerheid 'nee' (solely_automated false of significant_effect false) → art. 22 niet van toepassing; stap 3-6 not_applicable. Wel gelden K2 (grondslag voor profilering), K5 en het bezwaarrecht (art. 21).
- Stap 1 of 2 'weet ik niet' (null) → stap 3-6 blijven van toepassing en komen op review (ontbrekend feit); nooit not_applicable.
- Stap 1 en 2 zijn open normen → bij twijfel review. Het zijn kwalificatiestappen; zij geven zelf geen non_compliant.
- Stap 3: geen uitzondering → non_compliant.
- Stap 5: bijzondere gegevens zonder uitdrukkelijke toestemming of zwaarwegend algemeen belang én passende maatregelen → non_compliant.
- Stap 7 is signalerend (DPIA → K9) en kan nooit hoger uitkomen dan review. Geen profilering, geen aanmerkelijke gevolgen of DPIA al gedaan → not_applicable (de DPIA-plicht op andere gronden toetst K9).
- Samenloop: AI-systemen voor werving, krediet en verzekeringen kunnen hoog-risico zijn onder de AI-verordening → AI2 (signaal).

## Samenhang met andere kaders

- Kader K2 (/toets-grondslag) — als `facts.uses_profiling == true`: Voor profilering is altijd een grondslag nodig, ook als het geen volledig geautomatiseerd besluit is.
- Kader K2a (/toets-grondslag) — als `facts.art22_exception == "explicit_consent"`: Je baseert het geautomatiseerde besluit op uitdrukkelijke toestemming; die moet aan de eisen voor toestemming voldoen.
- Kader K5 (/privacyverklaring) — als `facts.uses_profiling == true or facts.solely_automated != false`: Mensen moeten in je privacyverklaring lezen dat je profileert of geautomatiseerd besluit, en wat dat voor hen betekent.
- Kader K9 (/dpia) — als `facts.significant_effect != false`: Profilering waarop besluiten met rechtsgevolgen of vergelijkbare gevolgen berusten, vraagt meestal om een DPIA.
- Kader AI2 (/toets-ai-act-basis) — als `facts.uses_ai != false and facts.decision_domain == "recruitment" or facts.uses_ai != false and facts.decision_domain == "credit" or facts.uses_ai != false and facts.decision_domain == "insurance"`: AI-systemen voor werving, krediet en verzekeringen kunnen onder de AI-verordening hoog-risico zijn (signaal).

## Open punten en voorbehouden

- De toepasselijkheid van stap 3-6 hangt af van de antwoorden van de klant (solely_automated, significant_effect), niet van de uitkomst van stap 1 en 2. Twijfelt het model bij stap 1 aan een 'nee' (afstempelen), dan wordt het kader review, maar worden stap 3-6 niet getoetst.
- Stap 4 noemt art. 40 lid 3 UAVG naast art. 22 lid 3 AVG, terwijl stap 4 alleen geldt bij uitzondering (a) en (c) en art. 40 UAVG over uitzondering (b) gaat. Te verifiëren of stap 4 ook moet gelden bij uitzondering (b) voor niet-bestuursorganen.
