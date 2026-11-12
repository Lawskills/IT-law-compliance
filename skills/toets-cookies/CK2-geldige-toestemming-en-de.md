# Kader CK2 — Geldige toestemming en de cookiebanner

Versie 0.4 · peildatum 2026-11-10

Doel: Controleren of de toestemming voor cookies en trackers die niet onder een uitzondering vallen geldig is: vooraf, actief, vrij, specifiek en geïnformeerd gegeven, even makkelijk te weigeren en in te trekken, aantoonbaar, zonder cookiewall, en met een banner die niet misleidt.

Geldt alleen als: `facts.stores_or_reads != false or facts.uses_other_tracking != false` · poortstap CK0.1 — vervalt als de website of app duidelijk niets opslaat of uitleest (regel van kader CK0)

Bronnen: TW-art11.7a-lid1-a (Telecommunicatiewet art. 11.7a lid 1 sub a); TW-art11.7a-lid1-b (Telecommunicatiewet art. 11.7a lid 1 sub b); TW-art11.7a-lid5 (Telecommunicatiewet art. 11.7a lid 5); TW-art11.1-g (Telecommunicatiewet art. 11.1 onder g); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3); AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid1 (AVG art. 7 lid 1); AVG-art7-lid2 (AVG art. 7 lid 2); AVG-art7-lid3 (AVG art. 7 lid 3); AVG-art7-lid4 (AVG art. 7 lid 4); AVG-art8-lid1 (AVG art. 8 lid 1); AVG-overw32 (AVG overweging 32); AVG-overw42 (AVG overweging 42); AVG-overw43 (AVG overweging 43); UAVG-art5-lid1 (UAVG art. 5 lid 1); HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); HvJEU-C-61-19 (HvJEU 11 november 2020, C-61/19, Orange Romania (bewijslast en vorm van toestemming)); HvJEU-C-252-21 (HvJEU 4 juli 2023, C-252/21, Meta Platforms/Bundeskartellamt); HvJEU-C-604-22 (HvJEU 7 maart 2024, C-604/22, IAB Europe (TC-string als persoonsgegeven; gezamenlijke verantwoordelijkheid)); AP-misleidende-cookiebanners-2024 (Autoriteit Persoonsgegevens, 'AP pakt misleidende cookiebanners aan'); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels)); AP-normuitleg-intrekken-2024 (Autoriteit Persoonsgegevens, 'Normuitleg intrekken van toestemming bij cookiebanners'); AP-normuitleg-cookiewalls (Autoriteit Persoonsgegevens, 'Hoe legt de AP de juridische normen rond cookiewalls uit?'); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten)); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679); EDPB-CBT-2023 (EDPB, Report of the work undertaken by the Cookie Banner Taskforce); EDPB-ADV-08-2024 (EDPB, Advies 08/2024 over geldige toestemming in de context van 'consent or pay'-modellen van grote onlineplatforms)

## Formulier (vragen aan de gebruiker)

- **has_banner**: Heeft je website of app een cookiebanner of een ander venster waarin om toestemming voor cookies wordt gevraagd?
  - Label (voor de plek-om-in-te-vullen): of je website of app een cookiebanner heeft
  - Type: boolean
- **banner_description**: Klopt deze beschrijving van je cookiebanner (eerste laag en instellingen)? Vul aan of verbeter waar nodig.
  - Label (voor de plek-om-in-te-vullen): de bevestigde beschrijving van de eerste laag en de instellingen van de banner
  - Hulp: deze skill beschrijft de screenshots die je hebt geüpload: welke knoppen, teksten, vinkjes en schuifjes er staan. Je bevestigt de beschrijving voordat de toets begint.
  - Type: text
- **uses_cmp**: Welke cookietool (consent management platform) gebruik je, als je er een gebruikt?
  - Label (voor de plek-om-in-te-vullen): welke cookietool je gebruikt
  - Hulp: Bijvoorbeeld Cookiebot, CookieYes, OneTrust of een plug-in van je websitebouwer. Ook met een cookietool blijf je zelf verantwoordelijk voor de instellingen.
  - Type: text
- **placement_timing**: Worden de cookies waarvoor toestemming nodig is pas geplaatst nadat de bezoeker toestemming heeft gegeven, of al bij het openen van de pagina?
  - Label (voor de plek-om-in-te-vullen): of cookies vóór of na de keuze van de bezoeker worden geplaatst
  - Type: enum (after_consent / before_consent)
- **placement_evidence**: Heb je dit gecontroleerd, bijvoorbeeld met een testrapport of scan van je cookietool of door in de browser te kijken welke cookies er vóór je keuze staan?
  - Label (voor de plek-om-in-te-vullen): of je hebt gecontroleerd wanneer de cookies worden geplaatst
  - Hulp: Zonder zo'n controle kan deze skill niet vaststellen dat de cookies echt pas na toestemming worden geplaatst.
  - Type: boolean · Alleen vragen als: `facts.placement_timing != "before_consent"`
- **prechecked_boxes**: Staan er in de banner vinkjes of schuifjes voor cookies vooraf aan, op welke laag dan ook?
  - Label (voor de plek-om-in-te-vullen): of er vinkjes of schuifjes vooraf aan staan
  - Type: boolean
- **implied_consent**: Gaat je website uit van toestemming als de bezoeker verder klikt, scrolt, de banner sluit of niets kiest?
  - Label (voor de plek-om-in-te-vullen): of doorgaan, scrollen of wegklikken als toestemming geldt
  - Type: boolean
- **reject_option**: Hoe kunnen bezoekers cookies weigeren?
  - Label (voor de plek-om-in-te-vullen): hoe en waar bezoekers cookies kunnen weigeren
  - Type: enum (equal_first_layer / first_layer_less_prominent / link_in_text / settings_only / extra_confirmation / none)
- **multiple_purposes**: Gebruik je cookies waarvoor toestemming nodig is voor meer dan één doel, bijvoorbeeld statistieken én advertenties?
  - Label (voor de plek-om-in-te-vullen): of je cookies voor meer dan één doel gebruikt
  - Type: boolean
- **per_purpose_choice**: Kunnen bezoekers per doel kiezen (bijvoorbeeld wel statistieken, geen advertenties), op de eerste of tweede laag?
  - Label (voor de plek-om-in-te-vullen): of bezoekers per doel kunnen kiezen
  - Type: boolean · Alleen vragen als: `facts.multiple_purposes != false`
- **third_party_sharing**: Delen de cookies waarvoor je toestemming vraagt gegevens met andere partijen, zoals advertentie- of socialmediabedrijven?
  - Label (voor de plek-om-in-te-vullen): of de cookies gegevens met andere partijen delen
  - Type: boolean
- **first_layer_third_party_count**: Staat op de eerste laag van de banner dat je gegevens deelt met andere partijen, en met hoeveel?
  - Label (voor de plek-om-in-te-vullen): of de eerste laag vermeldt met hoeveel partijen je gegevens deelt
  - Type: boolean · Alleen vragen als: `facts.third_party_sharing != false`
- **withdrawal_info_before**: Staat in de banner, vóórdat de bezoeker kiest, dat hij zijn toestemming later kan intrekken en hoe?
  - Label (voor de plek-om-in-te-vullen): of de banner vooraf meldt dat en hoe toestemming kan worden ingetrokken
  - Type: boolean
- **withdrawal_method**: Hoe kunnen bezoekers hun keuze later wijzigen of hun toestemming intrekken?
  - Label (voor de plek-om-in-te-vullen): hoe bezoekers hun toestemming kunnen intrekken
  - Type: enum (persistent_button / footer_link / cookie_policy_only / email_or_browser / none)
- **withdrawal_propagated**: Als een bezoeker zijn toestemming intrekt, krijgen de andere partijen die op basis van die toestemming gegevens ontvingen dat dan door?
  - Label (voor de plek-om-in-te-vullen): of andere partijen horen dat een bezoeker zijn toestemming intrekt
  - Hulp: Veel cookietools geven een intrekking automatisch door aan aangesloten advertentiepartijen. Vraag het zo nodig na bij je cookietool.
  - Type: boolean · Alleen vragen als: `facts.third_party_sharing != false`
- **consent_logged**: Leg je (of je cookietool) per bezoeker vast wanneer en waarvoor toestemming is gegeven, en welke versie van de banner toen gold?
  - Label (voor de plek-om-in-te-vullen): of je vastlegt wie wanneer toestemming gaf
  - Type: boolean
- **cookiewall**: Kunnen bezoekers die cookies weigeren je website of app gewoon gebruiken?
  - Label (voor de plek-om-in-te-vullen): of bezoekers die cookies weigeren de website nog kunnen gebruiken
  - Type: enum (none / full_wall / pay_or_ok / limited_access)
- **public_body**: Is je organisatie een overheidsorganisatie of een andere publiekrechtelijke rechtspersoon (zoals een gemeente, provincie of zelfstandig bestuursorgaan met rechtspersoonlijkheid)?
  - Label (voor de plek-om-in-te-vullen): of je organisatie een overheidsorganisatie is
  - Type: boolean · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **targets_children**: Is je website of app (ook) bedoeld voor kinderen jonger dan 16?
  - Label (voor de plek-om-in-te-vullen): of je website of app (ook) bedoeld is voor kinderen jonger dan 16
  - Type: boolean
- **parental_consent**: Geeft bij kinderen jonger dan 16 een ouder of voogd de toestemming, en controleer je dat redelijkerwijs?
  - Label (voor de plek-om-in-te-vullen): of bij kinderen jonger dan 16 een ouder of voogd toestemming geeft
  - Type: boolean · Alleen vragen als: `facts.targets_children != false`

## Toetspunten

### CK2.1 — Of cookies pas worden geplaatst nadat bezoekers toestemming geven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Cookies en trackers die toestemming vereisen, worden pas geplaatst of uitgelezen nadat de gebruiker toestemming heeft gegeven
- Grondslag: art. 11.7a lid 1 sub b Telecommunicatiewet; art. 5 lid 3 Richtlijn 2002/58/EG
- Beoordeeld op: de antwoorden
- Nodig: placement_timing
- Beoordeling:
  - Noem uses_cmp in de onderbouwing als het is ingevuld; een cookietool ontslaat de organisatie niet van haar eigen verantwoordelijkheid voor de instellingen.
  - present: placement_timing is after_consent én placement_evidence is true (controle met een scan, testrapport of in de browser).
  - absent: placement_timing is before_consent.
  - twijfel (⚠️): placement_timing is after_consent maar placement_evidence is false of 'weet ik niet'. Deze skill kan zonder scan niet zelf vaststellen wanneer cookies worden geplaatst.
  - placement_timing onbekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Blijkt uit de aangeleverde gegevens dat niet-vrijgestelde cookies pas na toestemming worden geplaatst?
- Advies bij ❌ of ⚠️: Stel je website of cookietool zo in dat cookies en trackers waarvoor toestemming nodig is pas worden geladen nadat de bezoeker op 'accepteren' klikt. Controleer dat met een scan of in de browser.
- Bronnen: TW-art11.7a-lid1-b (Telecommunicatiewet art. 11.7a lid 1 sub b); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels))

### CK2.2 — Of vinkjes en schuifjes standaard uit staan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen vooraf aangevinkte vakjes of aanstaande schuifjes, op geen enkele laag van de banner
- Grondslag: art. 4 punt 11 AVG; overweging 32 AVG; HvJEU C-673/17 Planet49
- Alleen als: `facts.has_banner != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: prechecked_boxes
- Beoordeling:
  - present: prechecked_boxes is false en banner_description noemt geen aanstaande vinkjes of schuifjes voor cookies waarvoor toestemming nodig is.
  - absent: prechecked_boxes is true, of banner_description noemt vooraf aangevinkte vakjes of aanstaande schuifjes (ook op een tweede laag).
  - prechecked_boxes false terwijl banner_description aanstaande schuifjes voor niet-noodzakelijke cookies beschrijft: twijfel (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zet alle vinkjes en schuifjes voor cookies waarvoor toestemming nodig is standaard uit, ook in de instellingen. Een vooraf aangevinkt vakje is geen toestemming.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); AVG-overw32 (AVG overweging 32); HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels))

### CK2.3 — Of bezoekers zelf actief toestemming geven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen toestemming afgeleid uit doorklikken, scrollen, verder surfen, het sluiten van de banner of niets doen
- Grondslag: art. 4 punt 11 AVG; overweging 32 AVG; HvJEU C-673/17 Planet49
- Beoordeeld op: de antwoorden
- Nodig: implied_consent
- Beoordeling:
  - present: implied_consent is false en banner_description beschrijft een actieve keuze (knop of vinkje).
  - absent: has_banner is false terwijl er cookies zijn waarvoor toestemming nodig is (er wordt geen geldige toestemming gevraagd).
  - absent: implied_consent is true, of banner_description bevat een tekst als 'door verder te gaan gaat u akkoord' of een sluitknop die als toestemming geldt.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Ga alleen uit van toestemming als de bezoeker zelf op 'accepteren' klikt. Verder klikken, scrollen of de banner sluiten is geen toestemming.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); AVG-overw32 (AVG overweging 32); HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten))

### CK2.4 — Of weigeren net zo makkelijk is als accepteren
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Een weigeroptie staat op dezelfde laag als de optie om te accepteren, is even goed zichtbaar en vraagt geen extra klik (AP-vuistregels 4-7)
- Grondslag: art. 4 punt 11 en art. 7 lid 4 AVG; overweging 42 AVG; AP 'Heldere cookiebanners'
- Beoordeeld op: de antwoorden
- Nodig: reject_option
- Beoordeling:
  - present: reject_option is equal_first_layer en banner_description bevestigt een weigerknop op dezelfde laag, even zichtbaar en leesbaar als de accepteerknop.
  - absent: reject_option is settings_only, link_in_text, extra_confirmation of none; of banner_description beschrijft een weigeroptie die alleen na scrollen zichtbaar is of nauwelijks verschilt van de achtergrond (AP: onleesbaar).
  - twijfel (⚠️): reject_option is first_layer_less_prominent (op dezelfde laag, kleiner of minder opvallend, maar goed leesbaar).
  - has_banner false terwijl er cookies zijn waarvoor toestemming nodig is: absent.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de weigeroptie op de eerste laag gelijkwaardig aan de accepteeroptie, of wordt de bezoeker naar accepteren gestuurd?
- Advies bij ❌ of ⚠️: Zet een knop 'weigeren' op de eerste laag van de banner, naast de knop 'accepteren', even groot en even goed zichtbaar. Weigeren mag niet meer klikken kosten dan accepteren.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); AVG-overw42 (AVG overweging 42); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels)); AP-misleidende-cookiebanners-2024 (Autoriteit Persoonsgegevens, 'AP pakt misleidende cookiebanners aan'); EDPB-CBT-2023 (EDPB, Report of the work undertaken by the Cookie Banner Taskforce)

### CK2.5 — Of bezoekers per doel kunnen kiezen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Bij meerdere doelen kan de gebruiker per doel toestemming geven of weigeren (op de eerste of tweede laag)
- Grondslag: art. 4 punt 11 AVG ('specifiek'); overweging 43 AVG; AP 'Heldere cookiebanners' (vuistregel 1)
- Alleen als: `facts.multiple_purposes != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: multiple_purposes, per_purpose_choice
- Beoordeling:
  - present: per_purpose_choice is true. Een knop 'alles accepteren' op de eerste laag mag, als er op de eerste of tweede laag per doel kan worden gekozen.
  - absent: has_banner is false terwijl er cookies zijn waarvoor toestemming nodig is (er wordt geen geldige toestemming gevraagd).
  - absent: per_purpose_choice is false (één keuze voor alle doelen samen).
  - per_purpose_choice onbekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Laat bezoekers per doel kiezen, bijvoorbeeld met aparte schuifjes voor statistieken, advertenties en socialmedia in de instellingen van de banner.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); AVG-overw43 (AVG overweging 43); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels)); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679)

### CK2.6 — Of bezoekers vóór hun keuze weten waarvoor ze toestemming geven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Op de eerste laag: wie toestemming vraagt, de doelen en de (soort) persoonsgegevens, en per doel dát en met hoeveel derden gegevens worden gedeeld; details in een tweede laag of de cookieverklaring. Een verwijzing naar voorwaarden of privacyverklaring is niet genoeg
- Grondslag: art. 11.7a lid 1 sub a Telecommunicatiewet; art. 4 punt 11 en art. 7 lid 2 AVG; HvJEU C-673/17 Planet49; AP 'Heldere cookiebanners' (vuistregel 1)
- Beoordeeld op: de antwoorden
- Nodig: banner_description, third_party_sharing
- Beoordeling:
  - present: banner_description laat zien dat de eerste laag noemt wie toestemming vraagt, voor welke doelen (concreet, zoals 'statistieken', 'gepersonaliseerde advertenties') en welke soort gegevens; en, als third_party_sharing true is, dat gegevens met derden worden gedeeld en met hoeveel (first_layer_third_party_count true).
  - absent: has_banner is false terwijl er cookies zijn waarvoor toestemming nodig is (er wordt geen geldige toestemming gevraagd).
  - absent: de eerste laag noemt geen doelen of alleen vage termen ('voor een betere ervaring', 'social media' zonder doel), of verwijst alleen naar de algemene voorwaarden of de privacyverklaring.
  - absent: third_party_sharing is true en first_layer_third_party_count is false (het aantal derden ontbreekt), of niet duidelijk is wie toestemming vraagt, of een van de doelen is vaag. Informatie weglaten levert de klant niets op (twijfelregel).
  - first_layer_third_party_count 'weet ik niet' terwijl de bannerbeschrijving het niet laat zien: twijfel (⚠️).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Weet de bezoeker op de eerste laag genoeg om een geïnformeerde keuze te maken (doelen, soort gegevens, delen met derden en het aantal)?
- Advies bij ❌ of ⚠️: Vermeld op de eerste laag van de banner wie je bent, voor welke doelen je cookies gebruikt, welke soort gegevens dat betreft, en of en met hoeveel andere partijen je gegevens deelt. Zet de details (welke partijen per doel) in de tweede laag of je cookieverklaring.
- Bronnen: TW-art11.7a-lid1-a (Telecommunicatiewet art. 11.7a lid 1 sub a); AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid2 (AVG art. 7 lid 2); HvJEU-C-673-17 (HvJEU 1 oktober 2019, C-673/17, Planet49 (vooraf aangevinkt vakje is geen geldige toestemming)); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels)); AP-cookies-thema (Autoriteit Persoonsgegevens, themapagina 'Cookies' (soorten cookies, toestemming, cookiewalls, klachten))

### CK2.7 — Of bezoekers vooraf horen dat ze hun toestemming kunnen intrekken, en hoe
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Vóór het geven van toestemming wordt de gebruiker, op dezelfde of een eerdere laag, meegedeeld dat hij de toestemming op ieder moment kan intrekken en hoe
- Grondslag: art. 7 lid 3 derde zin AVG; AP-normuitleg intrekken van toestemming bij cookiebanners (vereiste 1)
- Beoordeeld op: de antwoorden
- Nodig: withdrawal_info_before
- Beoordeling:
  - present: withdrawal_info_before is true en banner_description bevestigt dat de banner (op de eerste laag of op de laag waar de keuze wordt gemaakt) meldt dat en hoe de toestemming kan worden ingetrokken.
  - absent: has_banner is false terwijl er cookies zijn waarvoor toestemming nodig is (er wordt geen geldige toestemming gevraagd).
  - absent: withdrawal_info_before is false, of de melding staat alleen in de cookieverklaring zonder dat de organisatie kan aantonen dat de bezoeker die vóór de keuze zag.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zet in de banner, vóór de keuze, een korte zin als: 'Je kunt je keuze altijd wijzigen via de knop Cookie-instellingen linksonder op elke pagina.'
- Bronnen: AVG-art7-lid3 (AVG art. 7 lid 3); AP-normuitleg-intrekken-2024 (Autoriteit Persoonsgegevens, 'Normuitleg intrekken van toestemming bij cookiebanners'); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels))

### CK2.8 — Of bezoekers hun toestemming altijd en net zo makkelijk kunnen intrekken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Intrekken kan op ieder moment, kosteloos, zonder nadelige gevolgen en even eenvoudig als het geven, bijvoorbeeld via een altijd vindbare link, icoon of knop
- Grondslag: art. 7 lid 3 AVG; overweging 42 AVG; AP-normuitleg intrekken van toestemming bij cookiebanners (vereisten 2-4)
- Beoordeeld op: de antwoorden
- Nodig: withdrawal_method
- Beoordeling:
  - present: withdrawal_method is persistent_button, of footer_link met een duidelijke benaming op elke pagina.
  - absent: withdrawal_method is email_or_browser of none.
  - cookie_policy_only: present als banner_description laat zien dat de instellingen direct bovenaan het cookiebeleid staan en dat het cookiebeleid via een link op elke pagina bereikbaar is (de AP accepteert dat); anders absent (een knop of link die altijd in beeld is kost niets, twijfelregel).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is intrekken op ieder moment mogelijk en even eenvoudig als het geven van toestemming (AP-normuitleg)?
- Advies bij ❌ of ⚠️: Zet een knop of link 'Cookie-instellingen' die altijd in beeld is of onderaan elke pagina staat, waarmee bezoekers met één of twee klikken hun keuze kunnen wijzigen.
- Bronnen: AVG-art7-lid3 (AVG art. 7 lid 3); AVG-overw42 (AVG overweging 42); AP-normuitleg-intrekken-2024 (Autoriteit Persoonsgegevens, 'Normuitleg intrekken van toestemming bij cookiebanners'); EDPB-CBT-2023 (EDPB, Report of the work undertaken by the Cookie Banner Taskforce)

### CK2.9 — Of andere partijen horen dat een bezoeker zijn toestemming intrekt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Heeft de gebruiker toestemming gegeven voor verwerking door derden en trekt hij die in, dan laat de verwerkingsverantwoordelijke dat ook aan die derden weten
- Grondslag: art. 7 lid 3 AVG; AP-normuitleg intrekken van toestemming bij cookiebanners
- Alleen als: `facts.third_party_sharing != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: third_party_sharing, withdrawal_propagated
- Beoordeling:
  - present: withdrawal_propagated is true (bijvoorbeeld doordat de cookietool de intrekking doorgeeft aan de aangesloten partijen).
  - absent: withdrawal_propagated is false.
  - withdrawal_propagated onbekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zorg dat een intrekking wordt doorgegeven aan de partijen die op basis van de toestemming gegevens ontvingen, bijvoorbeeld via de instellingen van je cookietool.
- Bronnen: AVG-art7-lid3 (AVG art. 7 lid 3); AP-normuitleg-intrekken-2024 (Autoriteit Persoonsgegevens, 'Normuitleg intrekken van toestemming bij cookiebanners')

### CK2.10 — Of je kunt aantonen dat bezoekers toestemming gaven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De verwerkingsverantwoordelijke kan aantonen dat de gebruiker toestemming heeft gegeven (wanneer, waarvoor, via welke versie van de banner)
- Grondslag: art. 7 lid 1 AVG; HvJEU C-61/19 Orange Romania
- Beoordeeld op: de antwoorden
- Nodig: consent_logged
- Beoordeling:
  - present: consent_logged is true.
  - absent: consent_logged is false.
  - De wet noemt geen bewaartermijn voor dit bewijs; noem in de onderbouwing dat het bewijs bewaard moet blijven zolang op de toestemming wordt vertrouwd.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Laat je cookietool per bezoeker vastleggen wanneer en waarvoor toestemming is gegeven en welke versie van de banner toen gold.
- Bronnen: AVG-art7-lid1 (AVG art. 7 lid 1); HvJEU-C-61-19 (HvJEU 11 november 2020, C-61/19, Orange Romania (bewijslast en vorm van toestemming)); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679)

### CK2.11 — Of bezoekers die cookies weigeren de website gewoon kunnen gebruiken
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Geen cookiewall: toegang hangt niet af van toestemming voor tracking cookies. Verboden voor diensten van een publiekrechtelijke rechtspersoon (lid 5); volgens de AP en de EDPB geen vrije toestemming bij andere organisaties
- Grondslag: art. 11.7a lid 5 Telecommunicatiewet; art. 4 punt 11 en art. 7 lid 4 AVG; overweging 42 AVG; AP-normuitleg cookiewalls; HvJEU C-252/21 r.o. 150
- Beoordeeld op: de antwoorden
- Nodig: cookiewall, public_body
- Beoordeling:
  - present: cookiewall is none; of cookiewall is limited_access waarbij alleen de ingesloten inhoud van een derde niet laadt en de rest van de website normaal werkt.
  - absent: public_body is true en cookiewall is full_wall (verboden door art. 11.7a lid 5 Tw).
  - absent: public_body is true en cookiewall is pay_or_ok of limited_access waarbij de dienst zelf niet zonder toestemming bruikbaar is.
  - twijfel (⚠️): public_body is false en cookiewall is full_wall (volgens de AP-normuitleg en de EDPB geen vrije toestemming, maar de wet verbiedt het uitdrukkelijk alleen bij publiekrechtelijke rechtspersonen en de cookiewall levert de klant toestemmingen en inkomsten op; twijfelregel: review met die uitleg).
  - twijfel (⚠️): public_body is false en cookiewall is pay_or_ok ("accepteren of betalen": C-252/21 r.o. 150 staat een gelijkwaardig alternatief tegen een passende vergoeding toe; EDPB-advies 08/2024 gaat alleen over grote platforms); of limited_access waarbij onduidelijk is welk deel niet werkt.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de toestemming vrij gegeven, gelet op de toegangsvoorwaarden (cookiewall, betaald alternatief) en het type organisatie?
- Advies bij ❌ of ⚠️: Zorg dat bezoekers die cookies weigeren je website of app normaal kunnen gebruiken. Laat bij weigeren alleen de onderdelen weg die echt van de toestemming afhangen, zoals ingesloten video's van een andere partij.
- Bronnen: TW-art11.7a-lid5 (Telecommunicatiewet art. 11.7a lid 5); AVG-art7-lid4 (AVG art. 7 lid 4); AVG-overw42 (AVG overweging 42); AP-normuitleg-cookiewalls (Autoriteit Persoonsgegevens, 'Hoe legt de AP de juridische normen rond cookiewalls uit?'); EDPB-RL-05-2020 (EDPB, Richtsnoeren 05/2020 inzake toestemming overeenkomstig Verordening (EU) 2016/679); HvJEU-C-252-21 (HvJEU 4 juli 2023, C-252/21, Meta Platforms/Bundeskartellamt); EDPB-ADV-08-2024 (EDPB, Advies 08/2024 over geldige toestemming in de context van 'consent or pay'-modellen van grote onlineplatforms)

### CK2.12 — Of de banner duidelijke woorden gebruikt en bezoekers niet een bepaalde kant op stuurt
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Knopteksten zijn duidelijk ('accepteren', 'weigeren'); geen sturing door kleur, woordkeuze of volgorde waardoor de ene keuze veel meer nadruk krijgt
- Grondslag: art. 4 punt 11 en art. 7 lid 2 AVG; AP 'Heldere cookiebanners' (vuistregel 3)
- Alleen als: `facts.has_banner != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: banner_description
- Beoordeling:
  - Duidelijk geval (compliant): de knoppen heten 'accepteren' en 'weigeren' (of gelijkwaardig), zijn in vorm en kleur gelijkwaardig, en de tekst stuurt niet.
  - Duidelijk geval (non_compliant): sturende of schuldgevoel oproepende teksten ('Ja, graag!' tegenover 'Nee, ik mis liever aanbiedingen'), knoppen als 'Oké' of 'Begrepen' waarbij niet duidelijk is dat de bezoeker toestemming geeft, of een weigeroptie die als onopvallende tekst tussen opvallende accepteerknoppen staat.
  - Kleur- of vormverschil zonder duidelijke sturing: geen duidelijk geval.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Stuurt de vormgeving of woordkeuze de bezoeker naar accepteren, zodat de keuze niet neutraal is?
- Advies bij ❌ of ⚠️: Gebruik neutrale, duidelijke knopteksten zoals 'Accepteren' en 'Weigeren', en geef beide knoppen dezelfde vorm en nadruk.
- Bronnen: AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid2 (AVG art. 7 lid 2); AP-heldere-cookiebanners (Autoriteit Persoonsgegevens, 'Heldere cookiebanners' (9 vuistregels)); EDPB-CBT-2023 (EDPB, Report of the work undertaken by the Cookie Banner Taskforce)

### CK2.13 — Of bij kinderen jonger dan 16 een ouder of voogd toestemming geeft
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Bij een dienst die (ook) is gericht op kinderen jonger dan 16 en toestemming als grondslag: toestemming van de ouder of voogd, met redelijke inspanningen om dat te controleren
- Grondslag: art. 8 lid 1 en 2 AVG; art. 5 lid 1 UAVG
- Alleen als: `facts.targets_children != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: targets_children, parental_consent
- Beoordeling:
  - present: parental_consent is true.
  - absent: parental_consent is false.
  - parental_consent onbekend: ⚠️ (noem welk antwoord ontbreekt).
  - Deze stap geldt alleen voor persoonsgegevens die via de cookies op basis van toestemming worden verwerkt; zijn er zulke cookies niet, noem dat dan in de onderbouwing (aanwezig).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Gebruik op een website of app voor kinderen jonger dan 16 geen cookies waarvoor toestemming nodig is, of regel dat een ouder of voogd de toestemming geeft en controleer dat redelijkerwijs.
- Bronnen: AVG-art8-lid1 (AVG art. 8 lid 1); UAVG-art5-lid1 (UAVG art. 5 lid 1)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): has_banner, banner_description, public_body. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Geen banner (has_banner false) terwijl er cookies zijn waarvoor toestemming nodig is: stap 2 en 12 n.v.t.; stap 3-7 absent → non_compliant.
- Stap 4: weigeren alleen via instellingen of een link in de tekst → non_compliant; weigerknop op dezelfde laag maar minder opvallend → review.
- Stap 11: cookiewall bij een publiekrechtelijke rechtspersoon → non_compliant (art. 11.7a lid 5 Tw); bij een andere organisatie → review (AP en EDPB: geen vrije toestemming; de wet verbiedt het alleen bij de overheid; twijfelregel); 'accepteren of betalen' → review.
- Stap 12 is een afweging: alleen compliant of non_compliant bij duidelijk geval; werkt alleen als review door.

## Samenhang met andere kaders

- Kader K2 (/toets-grondslag) — als `true`: De eisen aan toestemming volgen uit de AVG (K2a); de cookietoestemming gebruikt dezelfde toets.
- Kader CK3 (/cookieverklaring) — als `true`: De informatie in de banner en in de cookieverklaring hangen samen: de details horen in de tweede laag of de cookieverklaring.
- Kader K18 (/samenwerkingsafspraken) — als `facts.third_party_sharing == true`: Bij het delen met advertentiepartijen via een toestemmingsraamwerk kan gezamenlijke verantwoordelijkheid ontstaan (IAB Europe, Fashion ID).

## Open punten en voorbehouden

- Cookiewall bij private organisaties: nu review (twijfelregel, 22-09-2026). De AP en de EDPB achten hem onrechtmatig; de wet verbiedt hem uitdrukkelijk alleen bij publiekrechtelijke rechtspersonen (lid 5) en overweging 25 van de richtlijn noemt voorwaardelijke toegang bij een legitiem doel. Het rapport noemt het AP-standpunt en het boeterisico.
- Digital Omnibus (voorstel, geen geldend recht): keuze met één klik, zes maanden respecteren en browsersignalen zouden stap 4 en 8 veranderen.
