# Kader CK0 — Vallen je cookies en trackers onder de cookieregels?

Versie 0.4 · peildatum 2026-11-10

Doel: Vaststellen of art. 11.7a Telecommunicatiewet van toepassing is (slaat de website of app informatie op in, of leest zij informatie uit, het apparaat van de bezoeker), of daarbij persoonsgegevens worden verwerkt (dan geldt ook de AVG), en of derden via de website of app cookies of trackers plaatsen.

Bronnen: TW-art11.7a-lid1 (Telecommunicatiewet art. 11.7a lid 1); TW-art11.7a-lid2 (Telecommunicatiewet art. 11.7a lid 2); TW-art11.7a-lid4 (Telecommunicatiewet art. 11.7a lid 4); TW-art11.1-a (Telecommunicatiewet art. 11.1 onder a); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3); EDPB-RL-02-2023 (EDPB, Richtsnoeren 2/2023 over de technische reikwijdte van artikel 5, lid 3, van de e-privacyrichtlijn); AVG-art4-1 (AVG art. 4 punt 1); HvJEU-C-604-22 (HvJEU 7 maart 2024, C-604/22, IAB Europe (TC-string als persoonsgegeven; gezamenlijke verantwoordelijkheid)); HvJEU-C-40-17 (HvJEU, C-40/17, Fashion ID)

## Formulier (vragen aan de gebruiker)

- **site_or_app**: Om welke website of app gaat het?
  - Label (voor de plek-om-in-te-vullen): de website of app die wordt getoetst
  - Hulp: Bijvoorbeeld het webadres van je website of de naam van je app.
  - Type: text
- **stores_or_reads**: Plaatst je website of app cookies, of slaat zij op een andere manier iets op op het apparaat van de bezoeker (bijvoorbeeld in de opslag van de browser of via een onderdeel in je app), of leest zij daar iets uit?
  - Label (voor de plek-om-in-te-vullen): of je website of app iets opslaat op of uitleest van het apparaat van de bezoeker
  - Hulp: Bijna elke website doet dit, al is het maar voor een winkelmandje of het onthouden van de cookiekeuze. Je websitebouwer of cookietool kan dit meestal laten zien.
  - Type: boolean
- **tech_description**: Welke cookies, scripts, pixels, tags of onderdelen van andere partijen gebruikt je website of app? Plak de lijst uit je cookietool of beschrijf ze.
  - Label (voor de plek-om-in-te-vullen): welke cookies, scripts, pixels en onderdelen van derden je gebruikt
  - Hulp: Bijvoorbeeld: 'sessiecookie van onze webshop, Google Analytics, Meta-pixel, ingesloten YouTube-video's'. Een export uit je cookietool is het best.
  - Type: text
- **uses_other_tracking**: Gebruik je ook andere technieken om bezoekers te herkennen of te volgen, zoals pixels, tags, 'fingerprinting' of meten via je eigen server?
  - Label (voor de plek-om-in-te-vullen): of je andere volgtechnieken gebruikt dan cookies
  - Hulp: Een pixel is een onzichtbaar plaatje of script van bijvoorbeeld een advertentiebedrijf. Fingerprinting herkent een apparaat aan zijn instellingen. Weet je het niet, vraag het dan aan je websitebouwer of marketingbureau.
  - Type: boolean
- **other_tracking_description**: Welke andere technieken zijn dat, en wat doen ze?
  - Label (voor de plek-om-in-te-vullen): welke andere volgtechnieken je gebruikt
  - Type: text · Alleen vragen als: `facts.uses_other_tracking != false`
- **third_party_content**: Plaatsen of lezen andere partijen via je website of app cookies of trackers, bijvoorbeeld een advertentienetwerk, socialmediaknoppen, ingesloten video's of kaarten, of een chat- of statistiekdienst?
  - Label (voor de plek-om-in-te-vullen): of andere partijen via je website of app cookies of trackers plaatsen
  - Type: boolean
- **personal_data**: Worden via de cookies of trackers gegevens verzameld die iets zeggen over een persoon of een apparaat, zoals een IP-adres, een klant- of apparaatnummer of surfgedrag?
  - Label (voor de plek-om-in-te-vullen): of via de cookies of trackers persoonsgegevens worden verwerkt
  - Hulp: Ook een uniek nummer in een cookie waarmee een bezoeker bij een volgend bezoek wordt herkend, telt mee. Alleen volledig anonieme tellingen tellen niet.
  - Type: boolean
- **cross_site_tracking**: Worden gegevens over het gebruik van je website of app gecombineerd met gegevens over andere websites of apps, bijvoorbeeld voor gerichte advertenties?
  - Label (voor de plek-om-in-te-vullen): of bezoekers ook op andere websites of apps worden gevolgd
  - Type: boolean · Alleen vragen als: `facts.stores_or_reads != false or facts.uses_other_tracking != false`

## Toetspunten

### CK0.1 — Of je website of app iets opslaat op of uitleest van het apparaat van bezoekers
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Via een elektronisch communicatienetwerk wordt informatie opgeslagen in, of toegang verkregen tot informatie in, de randapparatuur van de gebruiker (lid 1), ook als dat op een andere wijze wordt bewerkstelligd (lid 2)
- Grondslag: art. 11.7a lid 1 en 2 Telecommunicatiewet; art. 5 lid 3 Richtlijn 2002/58/EG
- Beoordeeld op: de antwoorden
- Nodig: stores_or_reads, tech_description
- Beoordeling:
  - Dit is een kwalificatiestap: 'compliant' betekent dat de kwalificatie (wel of geen opslag of uitlezing) duidelijk vaststaat. Een duidelijk non_compliant geval bestaat bij deze stap niet.
  - Duidelijk geval (compliant, kwalificatie: valt eronder): stores_or_reads is true, of tech_description noemt cookies, local of session storage, SDK's, pixels, tags of scripts van derden.
  - Duidelijk geval (compliant, kwalificatie: valt er niet onder): stores_or_reads is false, uses_other_tracking is false en tech_description beschrijft een website of app zonder cookies, opslag op het apparaat, scripts van derden of pixels.
  - stores_or_reads false terwijl tech_description cookies, trackers of onderdelen van derden noemt: geen duidelijk geval.
  - In alle andere gevallen geen duidelijk geval.
  - Kwalificatie 'valt er niet onder' (en stap 2 ook): CK1, CK2 en CK3 zijn voor deze website of app niet van toepassing.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Wordt er informatie opgeslagen in, of uitgelezen uit, het apparaat van de bezoeker (art. 11.7a lid 1 en 2 Tw)?
- Advies bij ❌ of ⚠️: Maak een lijst van alle cookies, scripts, pixels en onderdelen van andere partijen op je website of app, bijvoorbeeld met de scan in je cookietool, zodat duidelijk is wat er op het apparaat van bezoekers wordt opgeslagen of uitgelezen.
- Bronnen: TW-art11.7a-lid1 (Telecommunicatiewet art. 11.7a lid 1); TW-art11.7a-lid2 (Telecommunicatiewet art. 11.7a lid 2); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3)

### CK0.2 — Of ook andere volgtechnieken dan cookies onder de regels vallen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Technieken zonder klassieke cookie (pixels, tags, fingerprinting, lokale opslag, server-side of IP-tracking) vallen onder art. 5 lid 3 als er informatie uit de apparatuur wordt uitgelezen of daarin wordt opgeslagen
- Grondslag: art. 11.7a lid 1 en 2 Telecommunicatiewet; art. 5 lid 3 Richtlijn 2002/58/EG; EDPB Richtsnoeren 2/2023
- Alleen als: `facts.uses_other_tracking != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: uses_other_tracking, other_tracking_description
- Beoordeling:
  - Kwalificatiestap: 'compliant' betekent dat duidelijk vaststaat of de techniek onder de regels valt.
  - Duidelijk geval (compliant, valt eronder): tracking pixels of tags van derden (ook in e-mails), fingerprinting-scripts die apparaatkenmerken uitlezen, SDK's in apps en opslag in local of session storage. De EDPB-richtsnoeren 2/2023 rekenen deze technieken uitdrukkelijk tot de reikwijdte.
  - Meting die uitsluitend op de eigen server plaatsvindt zonder dat er iets in de browser of app wordt opgeslagen of uitgelezen, of alleen op basis van het IP-adres: geen duidelijk geval (de reikwijdte hangt af van de technische uitvoering).
  - other_tracking_description ontbreekt of is 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Wordt met deze techniek informatie uit het apparaat van de bezoeker uitgelezen of daarin opgeslagen, zodat art. 11.7a Tw geldt (EDPB Richtsnoeren 2/2023)?
- Advies bij ❌ of ⚠️: Behandel pixels, tags, fingerprinting en opslag in de browser op dezelfde manier als cookies: vraag toestemming, tenzij een wettelijke uitzondering geldt.
- Bronnen: TW-art11.7a-lid2 (Telecommunicatiewet art. 11.7a lid 2); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3); EDPB-RL-02-2023 (EDPB, Richtsnoeren 2/2023 over de technische reikwijdte van artikel 5, lid 3, van de e-privacyrichtlijn)

### CK0.3 — Of via de cookies persoonsgegevens worden verwerkt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Via de cookies of trackers worden persoonsgegevens verwerkt (IP-adres, unieke identificator, profiel); tracking over verschillende diensten wordt vermoed een verwerking van persoonsgegevens te zijn (lid 4)
- Grondslag: art. 11.7a lid 4 Telecommunicatiewet; art. 4 punt 1 AVG
- Alleen als: `facts.stores_or_reads != false or facts.uses_other_tracking != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: personal_data
- Beoordeling:
  - Kwalificatiestap: 'compliant' betekent dat duidelijk vaststaat of er persoonsgegevens worden verwerkt.
  - Voorrang: personal_data false terwijl tech_description tracking-, advertentie- of analysetools noemt → geen duidelijk geval (dit criterium gaat voor de criteria hieronder).
  - Duidelijk geval (compliant, wel persoonsgegevens): personal_data is true, of cross_site_tracking is true (wettelijk vermoeden van art. 11.7a lid 4), of tech_description noemt advertentie-, social-media- of analysetools die een uniek nummer of het IP-adres verwerken.
  - Duidelijk geval (compliant, geen persoonsgegevens): personal_data is false en tech_description noemt alleen cookies zonder unieke identificatie (bijvoorbeeld een taalkeuze of de cookiekeuze zelf) en geen tools van derden.
  - Geen persoonsgegevens betekent niet dat art. 11.7a niet geldt: de Tw-regels gelden ook zonder persoonsgegevens (Planet49).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Worden via de cookies of trackers persoonsgegevens verwerkt, of geldt het vermoeden van art. 11.7a lid 4 Tw?
- Advies bij ❌ of ⚠️: Ga ervan uit dat je persoonsgegevens verwerkt als cookies of trackers een uniek nummer, het IP-adres of surfgedrag vastleggen. Dan gelden ook de AVG-regels, zoals een grondslag en informatie in je privacyverklaring.
- Bronnen: TW-art11.7a-lid4 (Telecommunicatiewet art. 11.7a lid 4); AVG-art4-1 (AVG art. 4 punt 1); HvJEU-C-604-22 (HvJEU 7 maart 2024, C-604/22, IAB Europe (TC-string als persoonsgegeven; gezamenlijke verantwoordelijkheid))

### CK0.4 — Of andere partijen via je website of app cookies plaatsen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Derden plaatsen of lezen via de website of app informatie uit; de website-eigenaar regelt de toestemming voor die derden en is voor het verzamelen en doorgeven mogelijk gezamenlijk verantwoordelijk (Fashion ID)
- Grondslag: art. 11.7a lid 1 Telecommunicatiewet; art. 26 AVG; HvJEU C-40/17 Fashion ID
- Alleen als: `facts.third_party_content != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: third_party_content, tech_description
- Beoordeling:
  - Kwalificatiestap: 'compliant' betekent dat duidelijk vaststaat welke derden via de website of app cookies of trackers plaatsen.
  - Duidelijk geval (compliant): third_party_content is true en tech_description noemt de derde partijen (bijvoorbeeld een advertentienetwerk, socialmediaplatform, videodienst of chatdienst).
  - third_party_content true zonder dat tech_description de partijen noemt: geen duidelijk geval.
  - third_party_content onbekend: ⚠️ (noem welk antwoord ontbreekt).
  - Noem in de onderbouwing dat de website-eigenaar de toestemming voor deze derden moet regelen en dat hij voor het verzamelen en doorgeven van de gegevens mogelijk samen met de derde verantwoordelijk is (K18).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Welke derden plaatsen of lezen via de website informatie uit, en is de website-eigenaar voor het verzamelen en doorgeven gezamenlijk verantwoordelijk (Fashion ID)?
- Advies bij ❌ of ⚠️: Maak een overzicht van alle andere partijen die via je website of app cookies of trackers plaatsen. Je moet voor hen toestemming vragen en hen noemen in je cookieverklaring.
- Bronnen: TW-art11.7a-lid1 (Telecommunicatiewet art. 11.7a lid 1); HvJEU-C-40-17 (HvJEU, C-40/17, Fashion ID); HvJEU-C-604-22 (HvJEU 7 maart 2024, C-604/22, IAB Europe (TC-string als persoonsgegeven; gezamenlijke verantwoordelijkheid))

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): site_or_app. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- CK0 geeft nooit non_compliant: het kwalificeert. 'compliant' = de kwalificatie staat vast.
- Stap 1 duidelijk 'geen opslag of uitlezing' en uses_other_tracking false → CK1, CK2 en CK3 not_applicable voor deze website of app. Geeft stap 1 review, dan blijven CK1-CK3 in de route. In de rekenhulp hebben CK1 en CK2 hiervoor een poortregel met poortstap CK0.1: hun vragen vervallen bij twee keer 'nee', en `kader.py uitkomst` meldt het als CK0.1 daarna niet ✅ is.
- Stap 3: wel persoonsgegevens → ook K0 en K2 (related). Geen persoonsgegevens → de Tw-regels (CK1-CK3) blijven gelden.
- Antwoordt de gebruiker 'nee' op opslag en op andere technieken terwijl tech_description cookies of trackers noemt, dan zijn stap 2 en 3 n.v.t. maar geeft stap 1 review; CK1-CK3 blijven dan in de route en de persoonsgegevens worden daar en via K0 (related op personal_data) alsnog beoordeeld.
- Stap 4: derden → ook K18 en de derde partijen in CK3.
- 'Weet ik niet' bij een verplicht feit → review.

## Samenhang met andere kaders

- Kader K0 (/toets-toepasselijkheid-rol) — als `facts.personal_data != false`: Via de cookies of trackers worden (mogelijk) persoonsgegevens verwerkt; dan geldt ook de AVG.
- Kader K2 (/toets-grondslag) — als `facts.personal_data != false`: Voor de verwerking van persoonsgegevens via cookies is een grondslag nodig; voor tracking is dat toestemming.
- Kader K18 (/samenwerkingsafspraken) — als `facts.third_party_content == true`: Wie een plug-in of tracker van een derde insluit, is voor het verzamelen en doorgeven mogelijk samen met die derde verantwoordelijk (Fashion ID).
- Kader K5 (/privacyverklaring) — als `facts.personal_data != false`: Het gebruik van cookies die persoonsgegevens verwerken, hoort ook in de privacyverklaring.

## Open punten en voorbehouden

- Digital Omnibus (voorstel, geen geldend recht): als de cookieregels voor persoonsgegevens naar de AVG gaan, verandert de kwalificatie in stap 3 en het toezicht.
