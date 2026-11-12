# Kader AI6 — Hoog risico: grondrechtentoets (art. 27)

Versie 0.4 · peildatum 2026-11-10

Doel: Controleren of een gebruiksverantwoordelijke die daartoe verplicht is, vóór het eerste gebruik van een hoogrisico-AI-systeem een beoordeling van de gevolgen voor de grondrechten uitvoert met de inhoud van art. 27 lid 1, die actueel houdt, de markttoezichtautoriteit op de hoogte brengt en laat aansluiten op de DPIA.

Van toepassing vanaf: 2027-12-02 — art. 113, derde alinea, onder c, zoals gewijzigd bij Verordening (EU) 2026/1744 (de grondrechtentoets geldt alleen voor systemen uit bijlage III)

Bronnen: AIVO-art27-lid1 (AI-verordening art. 27 lid 1); AIVO-art27-lid2 (AI-verordening art. 27 lid 2); AIVO-art27-lid3 (AI-verordening art. 27 lid 3); AIVO-art27-lid4 (AI-verordening art. 27 lid 4); AIVO-art27-lid5 (AI-verordening art. 27 lid 5); AIVO-overw96 (AI-verordening overweging 96); AIVO-bijlage3 (AI-verordening bijlage III); AIVO-art113 (AI-verordening art. 113); VO-2026-1744 (Verordening (EU) 2026/1744 van het Europees Parlement en de Raad van 8 juli 2026 tot wijziging van onder meer Verordening (EU) 2024/1689 (Digital Omnibus on AI)); AIVO-art111-lid2 (AI-verordening art. 111 lid 2)

## Formulier (vragen aan de gebruiker)

- **system_name**: Om welk AI-systeem gaat het?
  - Label (voor de plek-om-in-te-vullen): welk systeem het is
  - Type: text
- **deployer_type**: Wat voor organisatie ben je?
  - Label (voor de plek-om-in-te-vullen): wat voor organisatie je bent
  - Hulp: Openbare diensten zijn bijvoorbeeld onderwijs, zorg, sociale diensten, huisvesting en rechtsbijstand, ook als een private organisatie ze levert.
  - Type: enum (public_body / private_public_service / other) · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **annex3_area**: In welk gebied gebruik je het systeem?
  - Label (voor de plek-om-in-te-vullen): in welk gevoelig gebied je het systeem gebruikt
  - Type: enum (none / employment / education / credit_scoring / life_health_insurance / biometric / critical_infrastructure / public_services / law_enforcement_migration_justice_elections)
- **fria_done**: Heb je vóór het eerste gebruik beoordeeld wat het systeem kan betekenen voor de grondrechten van de mensen die het raakt?
  - Label (voor de plek-om-in-te-vullen): of je de grondrechtentoets vóór het eerste gebruik hebt gedaan
  - Hulp: Bijvoorbeeld het recht op gelijke behandeling, privacy, of een eerlijke procedure. Een eerdere toets voor een vergelijkbaar gebruik mag je hergebruiken.
  - Type: boolean
- **fria_relies_on_earlier**: Gebruik je een eerdere grondrechtentoets (van jezelf of van de aanbieder) voor een vergelijkbaar geval?
  - Label (voor de plek-om-in-te-vullen): of je een eerdere toets voor een vergelijkbaar geval hergebruikt
  - Type: boolean · Alleen vragen als: `facts.fria_done != false`
- **fria_process_description**: Beschrijft de toets in welk werkproces je het systeem gebruikt, en of dat past bij het doel dat de aanbieder opgeeft?
  - Label (voor de plek-om-in-te-vullen): of de toets beschrijft in welk proces en voor welk doel je het systeem gebruikt
  - Type: boolean · Alleen vragen als: `facts.fria_done != false`
- **fria_period_frequency**: Staat in de toets hoe lang en hoe vaak je het systeem gaat gebruiken?
  - Label (voor de plek-om-in-te-vullen): of de toets beschrijft hoe lang en hoe vaak je het systeem gebruikt
  - Type: boolean · Alleen vragen als: `facts.fria_done != false`
- **fria_affected_groups**: Staat in de toets welke groepen mensen het systeem waarschijnlijk raakt?
  - Label (voor de plek-om-in-te-vullen): of de toets beschrijft welke personen en groepen het raakt
  - Type: boolean · Alleen vragen als: `facts.fria_done != false`
- **fria_risks**: Welke risico's voor die groepen noemt de toets? Schrijf 'geen' als de toets geen risico's noemt.
  - Label (voor de plek-om-in-te-vullen): welke risico's voor die groepen de toets noemt
  - Hulp: Bijvoorbeeld: 'oudere sollicitanten kunnen lager scoren', 'mensen zonder vaste woonplaats krijgen vaker een afwijzing'. Gebruik ook wat de aanbieder in de gebruiksaanwijzing noemt.
  - Type: text · Alleen vragen als: `facts.fria_done != false`
- **fria_oversight_measures**: Beschrijft de toets hoe je het menselijk toezicht uitvoert, zoals de gebruiksaanwijzing vraagt?
  - Label (voor de plek-om-in-te-vullen): of de toets beschrijft hoe je menselijk toezicht uitvoert
  - Type: boolean · Alleen vragen als: `facts.fria_done != false`
- **fria_mitigation_complaints**: Staat in de toets wat je doet als een risico zich voordoet, wie daarover beslist, en hoe mensen kunnen klagen?
  - Label (voor de plek-om-in-te-vullen): of de toets beschrijft wat je doet als een risico zich voordoet, met interne afspraken en een klachtenregeling
  - Type: boolean · Alleen vragen als: `facts.fria_done != false`
- **changes_since**: Is er sinds de toets iets veranderd aan het gebruik, de groepen die het raakt of de risico's?
  - Label (voor de plek-om-in-te-vullen): of er sinds de toets iets wezenlijks is veranderd
  - Type: boolean · Alleen vragen als: `facts.fria_done != false`
- **fria_updated**: Heb je de toets bijgewerkt na die verandering?
  - Label (voor de plek-om-in-te-vullen): of je de toets hebt bijgewerkt
  - Type: boolean · Alleen vragen als: `facts.changes_since != false`
- **authority_notified**: Heb je de uitkomsten van de toets met het formulier van het AI-bureau aan de markttoezichtautoriteit gestuurd?
  - Label (voor de plek-om-in-te-vullen): of je de markttoezichtautoriteit hebt geïnformeerd
  - Type: boolean · Alleen vragen als: `facts.fria_done != false`
- **personal_data**: Verwerkt het systeem persoonsgegevens?
  - Label (voor de plek-om-in-te-vullen): of het systeem persoonsgegevens verwerkt
  - Type: boolean
- **linked_to_dpia**: Sluit de grondrechtentoets aan op je DPIA, bijvoorbeeld door ernaar te verwijzen of ze samen te voegen?
  - Label (voor de plek-om-in-te-vullen): of de toets aansluit op de DPIA
  - Type: boolean · Alleen vragen als: `facts.personal_data != false and facts.fria_done != false`

## Toetspunten

### AI6.1 — Of je vóór het eerste gebruik een grondrechtentoets hebt gedaan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De verplichte gebruiksverantwoordelijke voert vóór de ingebruikname een beoordeling uit van de gevolgen die het gebruik van het systeem kan hebben voor de grondrechten; de plicht geldt voor het eerste gebruik en mag in vergelijkbare gevallen steunen op eerdere beoordelingen van hemzelf of van de aanbieder
- Grondslag: art. 27 lid 1 en 2 AI-verordening
- Alleen als: `facts.annex3_area != "none" and ((facts.deployer_type != "other" and facts.annex3_area != "critical_infrastructure") or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance")` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: deployer_type, annex3_area, fria_done
- Beoordeling:
  - present als fria_done true is; absent als false.
  - fria_relies_on_earlier true: in vergelijkbare gevallen mag je steunen op een eerdere grondrechtentoets of op een bestaande effectbeoordeling van de aanbieder (art. 27 lid 2). Present alleen als uit de antwoorden blijkt dat die toets bij dit gebruik past; anders geen duidelijk geval (⚠️).
  - annex3_area none (geen gebied uit bijlage III, bijvoorbeeld een systeem uit bijlage I): de grondrechtentoets geldt niet; de stap is dan n.v.t. via de voorwaarde.
  - Is deployer_type of annex3_area 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt) (de stap geldt, want de plicht is niet uit te sluiten).
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Doe vóór het eerste gebruik een grondrechtentoets: beschrijf het proces, hoe lang en hoe vaak je het systeem gebruikt, wie het raakt, welke risico's er zijn, hoe het menselijk toezicht werkt en wat je doet als het misgaat. Je kunt een bestaande DPIA als basis gebruiken.
- Bronnen: AIVO-art27-lid1 (AI-verordening art. 27 lid 1); AIVO-art27-lid2 (AI-verordening art. 27 lid 2); AIVO-overw96 (AI-verordening overweging 96)

### AI6.2 — Of de toets het gebruik beschrijft: proces, duur en wie het raakt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De beoordeling bevat (a) een beschrijving van de processen van de gebruiksverantwoordelijke waarin het systeem wordt gebruikt overeenkomstig het beoogde doel, (b) de periode en frequentie van het beoogde gebruik, en (c) de categorieën natuurlijke personen en groepen die gevolgen kunnen ondervinden
- Grondslag: art. 27 lid 1 sub a, b en c AI-verordening
- Alleen als: `(facts.annex3_area != "none" and ((facts.deployer_type != "other" and facts.annex3_area != "critical_infrastructure") or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance")) and facts.fria_done != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: fria_process_description, fria_period_frequency, fria_affected_groups
- Beoordeling:
  - present als fria_process_description, fria_period_frequency en fria_affected_groups alle drie true zijn.
  - absent als een van de drie false is; noem welke onderdelen ontbreken.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vul de toets aan met wat ontbreekt: in welk werkproces je het systeem gebruikt, hoe lang en hoe vaak, en welke groepen mensen het raakt.
- Bronnen: AIVO-art27-lid1 (AI-verordening art. 27 lid 1)

### AI6.3 — Of de toets de risico's voor die mensen benoemt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: De beoordeling bevat (d) de specifieke risico's op schade die gevolgen kunnen hebben voor de geïdentificeerde categorieën personen of groepen, rekening houdend met de informatie van de aanbieder (art. 13)
- Grondslag: art. 27 lid 1 sub d AI-verordening
- Alleen als: `(facts.annex3_area != "none" and ((facts.deployer_type != "other" and facts.annex3_area != "critical_infrastructure") or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance")) and facts.fria_done != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: fria_risks
- Beoordeling:
  - Duidelijk geval compliant: fria_risks noemt ten minste één concreet risico, gekoppeld aan een groep personen, dat past bij het gebied (bijvoorbeeld ongelijke behandeling bij werving of krediet).
  - Duidelijk geval non_compliant: fria_risks is leeg of 'geen' terwijl het systeem besluiten over personen ondersteunt in een gebied van bijlage III. Een toets zonder enig risico is in die gebieden niet geloofwaardig.
  - Algemene of vage risico's ('privacy', 'fouten') zonder groep of gevolg: geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Benoemt de toets de specifieke risico's op schade voor de geïdentificeerde groepen, met de informatie van de aanbieder?
- Advies bij ❌ of ⚠️: Benoem per groep mensen welke schade het systeem kan veroorzaken, bijvoorbeeld ongelijke behandeling of een onterechte afwijzing. Gebruik daarbij de beperkingen en risico's die de aanbieder in de gebruiksaanwijzing noemt.
- Bronnen: AIVO-art27-lid1 (AI-verordening art. 27 lid 1)

### AI6.4 — Of de toets het toezicht en de maatregelen bij problemen beschrijft
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De beoordeling bevat (e) een beschrijving van de uitvoering van maatregelen voor menselijk toezicht volgens de gebruiksaanwijzing, en (f) de maatregelen die worden genomen als die risico's zich voordoen, met de regelingen voor interne governance en klachtenmechanismen
- Grondslag: art. 27 lid 1 sub e en f AI-verordening
- Alleen als: `(facts.annex3_area != "none" and ((facts.deployer_type != "other" and facts.annex3_area != "critical_infrastructure") or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance")) and facts.fria_done != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: fria_oversight_measures, fria_mitigation_complaints
- Beoordeling:
  - present als fria_oversight_measures en fria_mitigation_complaints beide true zijn.
  - absent als een van beide false is; noem welk onderdeel ontbreekt.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Beschrijf in de toets hoe het menselijk toezicht werkt, wat je doet als een risico zich voordoet, wie daarover beslist, en hoe mensen een klacht kunnen indienen.
- Bronnen: AIVO-art27-lid1 (AI-verordening art. 27 lid 1)

### AI6.5 — Of je de toets bijwerkt als er iets verandert
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Als tijdens het gebruik een van de beoordeelde elementen is gewijzigd of niet langer actueel is, neemt de gebruiksverantwoordelijke de nodige stappen om de informatie bij te werken
- Grondslag: art. 27 lid 2 AI-verordening
- Alleen als: `(facts.annex3_area != "none" and ((facts.deployer_type != "other" and facts.annex3_area != "critical_infrastructure") or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance")) and facts.fria_done != false and facts.changes_since != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: changes_since, fria_updated
- Beoordeling:
  - present als fria_updated true is; absent als false.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Werk de grondrechtentoets bij nu het gebruik, de groepen of de risico's zijn veranderd, en spreek af wanneer je hem opnieuw bekijkt.
- Bronnen: AIVO-art27-lid2 (AI-verordening art. 27 lid 2)

### AI6.6 — Of je de toezichthouder hebt geïnformeerd
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Na de beoordeling stelt de gebruiksverantwoordelijke de markttoezichtautoriteit in kennis van de resultaten, met het ingevulde model van het AI-bureau (art. 27 lid 5); bij een vrijstelling op grond van art. 46 lid 1 kan van deze kennisgeving worden afgezien
- Grondslag: art. 27 lid 3 en 5 AI-verordening
- Alleen als: `(facts.annex3_area != "none" and ((facts.deployer_type != "other" and facts.annex3_area != "critical_infrastructure") or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance")) and facts.fria_done != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: authority_notified
- Beoordeling:
  - present als authority_notified true is; absent als false.
  - Het model (vragenlijst) van het AI-bureau is mogelijk nog niet gepubliceerd; vermeld dat in de onderbouwing als authority_notified false is.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Stuur de uitkomsten van de grondrechtentoets aan de markttoezichtautoriteit, met het formulier van het AI-bureau zodra dat beschikbaar is.
- Bronnen: AIVO-art27-lid3 (AI-verordening art. 27 lid 3); AIVO-art27-lid5 (AI-verordening art. 27 lid 5)

### AI6.7 — Of de toets aansluit op je DPIA
- Soort: Formeel (F): ja/nee-toets op de feiten · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Als een plicht uit art. 27 al is vervuld door de DPIA (art. 35 AVG), vult de grondrechtentoets die DPIA aan
- Grondslag: art. 27 lid 4 AI-verordening; art. 35 AVG
- Alleen als: `(facts.annex3_area != "none" and ((facts.deployer_type != "other" and facts.annex3_area != "critical_infrastructure") or facts.annex3_area == "credit_scoring" or facts.annex3_area == "life_health_insurance")) and facts.fria_done != false and facts.personal_data != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: personal_data, linked_to_dpia
- Beoordeling:
  - present als linked_to_dpia true is; absent als false.
  - Niet verplicht als vormvereiste: ontbreken geeft review. Dubbel werk is geen overtreding.
  - Ontbrekend of 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Advies bij ❌ of ⚠️: Laat de grondrechtentoets en de DPIA op elkaar aansluiten: verwijs naar de DPIA voor wat daar al staat, of voeg ze samen in één document.
- Bronnen: AIVO-art27-lid4 (AI-verordening art. 27 lid 4)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): system_name. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Wanneer dit geldt: de plichten van dit kader (hoofdstuk III, afdeling 1 tot en met 3) gelden vanaf 2 december 2027 (de grondrechtentoets geldt alleen voor systemen uit bijlage III) (art. 113 zoals gewijzigd bij Verordening (EU) 2026/1744). Tot die datum is een ❌ een voorbereidingspunt: de rekenhulp maakt er een ⚠️ met de datum van ('Van toepassing vanaf'). Een systeem dat vóór die datum in de handel of in gebruik is, valt er alleen onder als het ontwerp daarna ingrijpend verandert; een systeem dat bedoeld is voor overheidsinstanties moet uiterlijk 2 augustus 2030 voldoen (art. 111 lid 2). Noem dit in het rapport als het systeem al vóór de datum in gebruik is.
- Is de organisatie niet verplicht (geen overheid, geen openbare dienst, of kritieke infrastructuur; en geen krediet- of verzekeringsgebied) → alle stappen not_applicable → kader not_applicable.
- Stap 1 absent (geen toets) → stap 2-7 not_applicable (fria_done false) en kader non_compliant.
- Stap 3 (A) geeft alleen compliant of non_compliant als duidelijk geval.

## Samenhang met andere kaders

- Kader K9 (/dpia) — als `facts.personal_data != false`: De grondrechtentoets vult de DPIA aan; wat al in de DPIA staat, hoef je niet opnieuw te doen (art. 27 lid 4).

## Open punten en voorbehouden

- Officiële tekst van art. 27 zoals gewijzigd bij Vo. (EU) 2026/1744 nalezen.
- Het model (vragenlijst) van het AI-bureau (art. 27 lid 5): na publicatie de feiten daarop afstemmen en de beoordeling daarop baseren.
- Overweging 96 als uitleg van 'openbare diensten' gebruikt; te verifiëren welke Nederlandse organisaties daaronder vallen (onderwijs, zorg, woningcorporaties).
