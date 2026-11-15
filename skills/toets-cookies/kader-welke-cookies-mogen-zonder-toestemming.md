# Kader CK1 — Welke cookies mogen zonder toestemming?

Versie 0.4 · peildatum 2026-11-10

Doel: Vaststellen of de cookies en trackers die zonder toestemming worden geplaatst, echt onder een wettelijke uitzondering vallen (uitsluitend communicatie, strikt noodzakelijk voor de gevraagde dienst, of beperkt analytisch met geen of geringe gevolgen voor de privacy), en of er voor die cookies een AVG-grondslag is.

Geldt alleen als: `facts.stores_or_reads != false or facts.uses_other_tracking != false` · poortstap CK0.1 — vervalt als de website of app duidelijk niets opslaat of uitleest (regel van kader CK0)

Bronnen: TW-art11.7a-lid1 (Telecommunicatiewet art. 11.7a lid 1); TW-art11.7a-lid3-a (Telecommunicatiewet art. 11.7a lid 3 sub a); TW-art11.7a-lid3-b (Telecommunicatiewet art. 11.7a lid 3 sub b); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten)); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels)); AP-cookies-organisatie (Autoriteit Persoonsgegevens, 'Cookies en uw organisatie: zorg voor een goed beleid'); EDPB-RL-02-2023 (EDPB, Richtsnoeren 2/2023 over de technische reikwijdte van artikel 5, lid 3, van de e-privacyrichtlijn); AVG-art6-lid1-b (AVG art. 6 lid 1 sub b); AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); AVG-art21-lid1 (AVG art. 21 lid 1); HvJEU-C-40-17 (HvJEU, C-40/17, Fashion ID)

## Formulier (vragen aan de gebruiker)

- **cookie_list**: Welke cookies en trackers gebruikt je website of app? Geef per cookie de naam, van welke partij hij is, waarvoor hij dient en hoe lang hij blijft staan.
  - Label (voor de plek-om-in-te-vullen): de lijst van cookies en trackers met partij, doel en looptijd
  - Hulp: Een export uit je cookietool is het makkelijkst. Het overzicht uit de vorige vraag wordt hier overgenomen; vul het zo nodig aan.
  - Type: text
- **no_consent_cookies**: Welke van deze cookies en trackers worden geplaatst zonder dat de bezoeker eerst toestemming geeft?
  - Label (voor de plek-om-in-te-vullen): welke cookies en trackers je plaatst zonder eerst toestemming te vragen
  - Hulp: Vaak zijn dat de cookies die in je cookietool als 'noodzakelijk', 'functioneel' of 'analytisch' zijn ingedeeld. Weet je het niet, kijk dan in de instellingen van je cookietool of vraag het je websitebouwer.
  - Type: text
- **has_functional_without_consent**: Plaats je cookies zonder toestemming omdat ze nodig zijn om de website te laten werken, zoals voor een winkelmandje, inloggen, beveiliging of het onthouden van de cookiekeuze?
  - Label (voor de plek-om-in-te-vullen): of je functionele cookies zonder toestemming plaatst
  - Type: boolean
- **functional_description**: Welke cookies zijn dat, en waarvoor zijn ze nodig?
  - Label (voor de plek-om-in-te-vullen): welke functionele cookies je plaatst en waarom ze nodig zijn
  - Type: text · Alleen vragen als: `facts.has_functional_without_consent != false`
- **has_analytics_without_consent**: Plaats je statistiek- of analysecookies zonder toestemming, bijvoorbeeld om bezoekersaantallen te meten?
  - Label (voor de plek-om-in-te-vullen): of je analytische cookies zonder toestemming plaatst
  - Type: boolean
- **analytics_tool**: Welke analysetool gebruik je, en waar draait die (op je eigen server of bij de aanbieder)?
  - Label (voor de plek-om-in-te-vullen): welke analysetool je gebruikt en hoe die is ingericht
  - Hulp: Bijvoorbeeld 'Matomo op onze eigen server' of 'Google Analytics 4'.
  - Type: text · Alleen vragen als: `facts.has_analytics_without_consent != false`
- **analytics_ip_truncated**: Wordt het IP-adres van bezoekers in de analysetool ingekort of helemaal niet opgeslagen?
  - Label (voor de plek-om-in-te-vullen): of het IP-adres in de analysetool wordt ingekort of niet wordt opgeslagen
  - Type: boolean · Alleen vragen als: `facts.has_analytics_without_consent != false`
- **analytics_data_shared**: Mag de aanbieder van de analysetool de gegevens ook voor zijn eigen doelen gebruiken, bijvoorbeeld via een instelling als 'gegevens delen' of koppelingen met advertentiediensten?
  - Label (voor de plek-om-in-te-vullen): of de aanbieder van de analysetool de gegevens ook voor eigen doelen gebruikt
  - Hulp: Bij veel tools staat dit standaard aan. Kijk in de beheeromgeving bij de instellingen voor het delen van gegevens.
  - Type: boolean · Alleen vragen als: `facts.has_analytics_without_consent != false`
- **analytics_linked_other_services**: Worden de statistieken gekoppeld aan andere diensten of gegevens, zoals advertentieaccounts, klantprofielen of het volgen van bezoekers op andere websites?
  - Label (voor de plek-om-in-te-vullen): of de analysegegevens worden gekoppeld aan andere diensten of profielen
  - Type: boolean · Alleen vragen als: `facts.has_analytics_without_consent != false`
- **analytics_processor_agreement**: Heb je met de aanbieder van de analysetool een verwerkersovereenkomst, of draait de tool volledig op je eigen server?
  - Label (voor de plek-om-in-te-vullen): of je met de aanbieder van de analysetool een verwerkersovereenkomst hebt
  - Type: boolean · Alleen vragen als: `facts.has_analytics_without_consent != false`
- **analytics_outside_eea**: Worden de analysegegevens opgeslagen of bekeken buiten de Europese Unie, Noorwegen, IJsland en Liechtenstein?
  - Label (voor de plek-om-in-te-vullen): of de analysegegevens buiten de EU/EER terechtkomen
  - Type: boolean · Alleen vragen als: `facts.has_analytics_without_consent != false`
- **exempt_cookies_personal_data**: Verwerken de cookies die je zonder toestemming plaatst gegevens over personen, zoals een uniek nummer, een inlognaam of een IP-adres?
  - Label (voor de plek-om-in-te-vullen): of je cookies zonder toestemming persoonsgegevens verwerken
  - Hulp: Ook een inlog- of sessiecookie met een uniek nummer dat aan een account of bezoek is gekoppeld, telt mee. Alleen cookies zonder enig uniek kenmerk (zoals een taalkeuze) tellen niet.
  - Type: boolean · Alleen vragen als: `facts.has_functional_without_consent != false or facts.has_analytics_without_consent != false`
- **exempt_basis**: Op welke grond gebruik je de gegevens uit die cookies?
  - Label (voor de plek-om-in-te-vullen): op welke grond je die cookies gebruikt
  - Hulp: Juristen noemen dit de grondslag. Een vrijstelling van de cookietoestemming betekent niet dat je geen grondslag nodig hebt.
  - Type: enum (legitimate_interest_documented / legitimate_interest_not_documented / contract / none) · Alleen vragen als: `facts.exempt_cookies_personal_data != false and (facts.has_functional_without_consent != false or facts.has_analytics_without_consent != false)`
- **objection_possible**: Kunnen bezoekers makkelijk bezwaar maken tegen deze cookies, bijvoorbeeld met een schuifje in de banner of op je cookiepagina?
  - Label (voor de plek-om-in-te-vullen): of bezoekers makkelijk bezwaar kunnen maken
  - Type: boolean · Alleen vragen als: `facts.exempt_basis == "legitimate_interest_documented" or facts.exempt_basis == "legitimate_interest_not_documented"`
- **has_marketing_cookies**: Gebruik je cookies of trackers voor advertenties, het volgen van bezoekers, socialmediaknoppen of het meten van campagnes?
  - Label (voor de plek-om-in-te-vullen): of je tracking-, advertentie- of socialmediacookies gebruikt
  - Hulp: Bijvoorbeeld een Meta-pixel, Google Ads, LinkedIn Insight Tag, TikTok-pixel of retargeting. Een statistiektool die aan advertentiediensten is gekoppeld, wordt apart gevraagd en telt in de toets ook mee.
  - Type: boolean
- **marketing_without_consent**: Worden (sommige van) deze cookies geplaatst zonder toestemming, bijvoorbeeld omdat ze als 'functioneel' of 'analytisch' zijn ingedeeld of omdat je je op je gerechtvaardigd belang beroept?
  - Label (voor de plek-om-in-te-vullen): of zulke cookies ook zonder toestemming worden geplaatst
  - Type: boolean · Alleen vragen als: `facts.has_marketing_cookies != false`
- **session_recording**: Gebruik je een dienst die klikken, muisbewegingen of hele bezoeken opneemt (heatmaps of sessie-opnames)?
  - Label (voor de plek-om-in-te-vullen): of je sessie-opnames of heatmaps gebruikt
  - Type: boolean
- **embeds_third_party**: Staan er op je website ingesloten video's, kaarten, socialmediaberichten of chatvensters van andere partijen?
  - Label (voor de plek-om-in-te-vullen): of je ingesloten inhoud van andere partijen gebruikt
  - Hulp: Bijvoorbeeld een YouTube-video, een Google Maps-kaart, een Instagram-bericht of een chatvenster van een externe dienst.
  - Type: boolean
- **embeds_load_before_consent**: Laadt die ingesloten inhoud al meteen bij het openen van de pagina, of pas nadat de bezoeker toestemming heeft gegeven of erop klikt?
  - Label (voor de plek-om-in-te-vullen): of die ingesloten inhoud al laadt voordat de bezoeker toestemming geeft
  - Type: boolean · Alleen vragen als: `facts.embeds_third_party != false`

## Toetspunten

### CK1.1 — Of je cookies zonder toestemming echt nodig zijn om de website te laten werken
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Opslag of toegang zonder toestemming uitsluitend voor de communicatie over het netwerk (lid 3 sub a) of strikt noodzakelijk om de door de gebruiker gevraagde dienst te leveren (lid 3 sub b, eerste deel)
- Grondslag: art. 11.7a lid 3 sub a en b Telecommunicatiewet; art. 5 lid 3 tweede zin Richtlijn 2002/58/EG
- Alleen als: `facts.has_functional_without_consent != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: has_functional_without_consent, functional_description
- Beoordeling:
  - Duidelijk geval (compliant): de beschreven cookies dienen alleen voor een functie waar de bezoeker zelf om vraagt en zonder welke die functie niet werkt: winkelmandje, inloggen, beveiliging van de sessie, load balancing, onthouden van taal of van de cookiekeuze.
  - Duidelijk geval (non_compliant): een als 'functioneel' ingedeelde cookie dient voor statistieken, advertenties, A/B-testen, personalisatie of gaat naar een derde die hem ook voor eigen doelen gebruikt. 'Handig voor ons' of 'voor een betere ervaring' is niet strikt noodzakelijk. Deze cookies vallen ook onder stap 4.
  - Functie die de bezoeker niet zelf vraagt maar die de website wel prettiger maakt (bijvoorbeeld het onthouden van recent bekeken producten): geen duidelijk geval.
  - functional_description ontbreekt of is 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn deze cookies strikt noodzakelijk voor een dienst waar de bezoeker uitdrukkelijk om vraagt (art. 11.7a lid 3 Tw)?
- Advies bij ❌ of ⚠️: Plaats zonder toestemming alleen cookies die echt nodig zijn voor wat de bezoeker zelf vraagt, zoals een winkelmandje of inloggen. Zet andere cookies in een categorie waarvoor je toestemming vraagt.
- Bronnen: TW-art11.7a-lid3-a (Telecommunicatiewet art. 11.7a lid 3 sub a); TW-art11.7a-lid3-b (Telecommunicatiewet art. 11.7a lid 3 sub b); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten))

### CK1.2 — Of je statistiekcookies zonder toestemming weinig gevolgen hebben voor de privacy
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Opslag of toegang om informatie te verkrijgen over de kwaliteit of effectiviteit van een geleverde dienst van de informatiemaatschappij, met geen of geringe gevolgen voor de persoonlijke levenssfeer (lid 3 sub b, tweede deel)
- Grondslag: art. 11.7a lid 3 sub b Telecommunicatiewet
- Alleen als: `facts.has_analytics_without_consent != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: has_analytics_without_consent, analytics_tool, analytics_ip_truncated, analytics_data_shared, analytics_linked_other_services, analytics_processor_agreement
- Beoordeling:
  - De concrete voorwaarden hieronder staan niet in de wet. Ze komen uit een eerdere AP-handleiding over het privacyvriendelijk instellen van analysetools en worden als criteria gebruikt. Zonder bewijs van de instellingen is dit nooit een duidelijk geval.
  - Duidelijk geval (compliant): de tool meet alleen het gebruik van de eigen website of app, analytics_ip_truncated is true, analytics_data_shared is false, analytics_linked_other_services is false, analytics_processor_agreement is true (of de tool draait volledig op de eigen server), en er is geen volgen over andere websites. De AP noemt Matomo, Plausible, Apache Superset en OpenPanel als alternatieven, 'mits goed ingesteld'.
  - Duidelijk geval (non_compliant): analytics_data_shared is true of analytics_linked_other_services is true (bijvoorbeeld koppeling met advertentiediensten of het volgen van bezoekers over andere websites). Dan vallen de cookies ook onder stap 4.
  - Een van de instellingen ontbreekt of is 'weet ik niet': ⚠️ (noem welk antwoord ontbreekt).
  - Eigen, afgeschermde heatmaps of sessie-opnames (session_recording true, geen derde met eigen doelen, ingevoerde gegevens afgeschermd): geen duidelijk geval.
  - analytics_outside_eea true: noem de samenloop met K13. Is er een adequaatheidsbesluit of passende waarborg (bijvoorbeeld het EU-VS Data Privacy Framework) en zijn de overige voorwaarden duidelijk vervuld, dan verandert dit de uitkomst niet. Ontbreekt een waarborg of is die onbekend: geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Heeft de analytische cookie geen of geringe gevolgen voor de persoonlijke levenssfeer (art. 11.7a lid 3 sub b Tw), gelet op de instellingen van de tool?
- Advies bij ❌ of ⚠️: Stel je analysetool privacyvriendelijk in: kort het IP-adres in, zet het delen van gegevens met de aanbieder uit, koppel de statistieken niet aan andere diensten en sluit een verwerkersovereenkomst. Lukt dat niet, vraag dan toestemming voor de statistiekcookies.
- Bronnen: TW-art11.7a-lid3-b (Telecommunicatiewet art. 11.7a lid 3 sub b); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten)); AP-cookies-organisatie (Autoriteit Persoonsgegevens, 'Cookies en uw organisatie: zorg voor een goed beleid')

### CK1.3 — Of je voor cookies zonder toestemming een geldige grond onder de AVG hebt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Cookies die zonder toestemming persoonsgegevens verwerken, hebben een AVG-grondslag nodig: gerechtvaardigd belang met een aantoonbare belangenafweging en een makkelijke bezwaarmogelijkheid, of de overeenkomst bij cookies die nodig zijn voor een door de bezoeker afgenomen dienst
- Grondslag: art. 6 lid 1 sub b en f en art. 21 lid 1 AVG; AP 'Heldere cookiebanners' (vuistregel 9)
- Alleen als: `facts.exempt_cookies_personal_data != false and (facts.has_functional_without_consent != false or facts.has_analytics_without_consent != false)` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: exempt_cookies_personal_data, exempt_basis
- Beoordeling:
  - Duidelijk geval (compliant): exempt_basis is legitimate_interest_documented en objection_possible is true; of exempt_basis is contract en de cookies zijn aantoonbaar nodig voor een dienst die de bezoeker afneemt (inloggen, bestellen).
  - Duidelijk geval (non_compliant): exempt_basis is none.
  - Duidelijk geval (non_compliant): exempt_basis is legitimate_interest_not_documented, of objection_possible is false (de AP eist een aantoonbare afweging en een makkelijke bezwaarmogelijkheid; niet vastleggen of geen bezwaar mogelijk maken levert de klant niets op, twijfelregel).
  - objection_possible 'weet ik niet' bij gerechtvaardigd belang: ⚠️ (noem welk antwoord ontbreekt).
  - Een vrijstelling van de toestemmingsplicht in de Telecommunicatiewet is geen AVG-grondslag.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is er voor de vrijgestelde cookies een AVG-grondslag, met (bij gerechtvaardigd belang) een aantoonbare afweging en een makkelijke bezwaarmogelijkheid?
- Advies bij ❌ of ⚠️: Leg vast op welke grond je de gegevens uit je functionele en statistiekcookies gebruikt. Kies je voor gerechtvaardigd belang, leg dan de belangenafweging vast en maak bezwaar maken makkelijk, bijvoorbeeld met een schuifje in de banner.
- Bronnen: AVG-art6-lid1-b (AVG art. 6 lid 1 sub b); AVG-art6-lid1-f (AVG art. 6 lid 1 sub f); AVG-art21-lid1 (AVG art. 21 lid 1); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels))

### CK1.4 — Of je cookies voor advertenties en volgen pas na toestemming plaatst
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Cookies en trackers die niet onder een uitzondering van lid 3 vallen (tracking, advertenties, social media, delen met derden voor eigen doelen), worden uitsluitend met toestemming geplaatst; gerechtvaardigd belang is geen grondslag voor tracking of gepersonaliseerde advertenties
- Grondslag: art. 11.7a lid 1 en 3 Telecommunicatiewet; AP 'Heldere cookiebanners' (vuistregel 9)
- Beoordeeld op: de antwoorden
- Nodig: no_consent_cookies, has_marketing_cookies
- Beoordeling:
  - Controleer no_consent_cookies aan de hand van cookie_list: een cookie of tracker voor advertenties of volgen die in cookie_list staat en zonder toestemming wordt geplaatst, maakt deze stap absent.
  - present: in no_consent_cookies staan alleen functionele cookies en statistiekcookies die in stap 1 en 2 niet duidelijk non_compliant zijn, en marketing_without_consent is false (of has_marketing_cookies is false).
  - absent: marketing_without_consent is true; of no_consent_cookies noemt advertentie-, tracking- of socialmediacookies of -pixels (bijvoorbeeld Meta-pixel, Google Ads, LinkedIn Insight Tag, TikTok-pixel, retargeting); of een analysetool deelt gegevens met de aanbieder voor diens eigen doelen of is gekoppeld aan advertentiediensten (analytics_data_shared of analytics_linked_other_services true); of sessie-opnames of heatmaps van een derde die de gegevens ook zelf gebruikt of waarbij ingevoerde gegevens niet worden afgeschermd, zonder toestemming; of ingesloten inhoud laadt trackers van een derde vóór de toestemming (embeds_load_before_consent true).
  - twijfel (⚠️): de lijst noemt tools waarvan niet duidelijk is of ze tracken (ontbrekende informatie), of eigen afgeschermde sessie-opnames of een 'privacyvriendelijke modus' van ingesloten inhoud zonder toestemming (levert de klant inzicht of inhoud op, twijfelregel: review).
  - no_consent_cookies of has_marketing_cookies onbekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Worden er cookies of trackers die niet onder art. 11.7a lid 3 Tw vallen zonder toestemming geplaatst?
- Advies bij ❌ of ⚠️: Plaats cookies en trackers voor advertenties, volgen, socialmedia en statistieken die gegevens met de aanbieder delen pas nadat de bezoeker toestemming heeft gegeven. Een beroep op je gerechtvaardigd belang is daarvoor niet genoeg.
- Bronnen: TW-art11.7a-lid3-a (Telecommunicatiewet art. 11.7a lid 3 sub a); TW-art11.7a-lid3-b (Telecommunicatiewet art. 11.7a lid 3 sub b); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels))

### CK1.5 — Of ingesloten video's, kaarten en berichten van andere partijen pas na toestemming laden
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Ingesloten inhoud van derden (video, kaart, socialmediabericht, chatvenster) laadt pas na toestemming, of zonder opslag of uitlezing op het apparaat van de bezoeker
- Grondslag: art. 11.7a lid 1 en 3 Telecommunicatiewet; HvJEU C-40/17 Fashion ID
- Alleen als: `facts.embeds_third_party != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: embeds_third_party, embeds_load_before_consent
- Beoordeling:
  - Duidelijk geval (compliant): embeds_load_before_consent is false, dus de inhoud laadt pas na toestemming of na een klik waarbij de bezoeker weet dat de derde gegevens ontvangt.
  - Duidelijk geval (non_compliant): embeds_load_before_consent is true en de derde plaatst of leest daarbij cookies of trackers (bijvoorbeeld een standaard ingesloten video of socialmediabericht). Dit valt ook onder stap 4 en CK2 stap 1.
  - Gebruik van een 'privacyvriendelijke modus' van de aanbieder zonder bewijs dat er niets wordt opgeslagen of uitgelezen: geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Plaatst of leest de ingesloten inhoud van de derde al informatie op het apparaat vóór de toestemming?
- Advies bij ❌ of ⚠️: Laad ingesloten video's, kaarten en socialmediaberichten pas nadat de bezoeker toestemming heeft gegeven, bijvoorbeeld met een klikbare afbeelding die uitlegt dat de andere partij dan gegevens ontvangt.
- Bronnen: TW-art11.7a-lid1 (Telecommunicatiewet art. 11.7a lid 1); TW-art11.7a-lid3-b (Telecommunicatiewet art. 11.7a lid 3 sub b); HvJEU-C-40-17 (HvJEU, C-40/17, Fashion ID)

## Regels van dit kader

- Stap 4 is de harde grens (F, verplicht): non_compliant → kader non_compliant.
- Stap 2: nooit compliant zonder bewijs van alle instellingen (IP ingekort, niet delen, niet koppelen, verwerkersovereenkomst of eigen server).

## Samenhang met andere kaders

- Kader CK2 (/toets-cookies) — als `facts.has_marketing_cookies != false`: Voor cookies die niet onder een uitzondering vallen, is geldige toestemming nodig.
- Kader K2 (/toets-grondslag) — als `facts.exempt_cookies_personal_data != false`: Ook cookies zonder toestemmingsplicht hebben een AVG-grondslag nodig als ze persoonsgegevens verwerken (meestal gerechtvaardigd belang).
- Kader K13 (/toets-doorgifte) — als `facts.analytics_outside_eea == true`: De analysetool geeft gegevens door naar een land buiten de EER.

## Open punten en voorbehouden

- Art. 5 lid 3 e-privacyrichtlijn kent geen uitzondering voor analytische cookies; de ruimere Nederlandse uitzondering (art. 11.7a lid 3 sub b, sinds 2015) laat een juridisch adviseur beoordelen op richtlijnconformiteit.
- De voorwaarden voor privacyvriendelijke analytics (stap 2) komen uit een oudere AP-handleiding die niet meer als actuele publicatie op de AP-website staat. Bij een nieuwe AP-publicatie de criteria bijwerken.
- Digital Omnibus (voorstel, geen geldend recht): een uitgebreide lijst van doelen zonder toestemming (o.a. bereiksmeting, beveiliging, mogelijk contextuele advertenties) zou stap 1 en 2 veranderen.
