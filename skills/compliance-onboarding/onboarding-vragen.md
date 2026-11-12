# Onboarding — vragenlijst (snelle route)

Peildatum 2026-11-11. De onboarding is **één formulier** (ongeveer drie minuten): `kader.py formulier --extra onboarding-formulier.json` maakt het uit `onboarding-formulier.json`, waarin elke vraag een sleutel heeft en afhankelijke vragen een voorwaarde (`ask_if`); wat door een antwoord niet meer nodig is verdwijnt vanzelf. De tabellen hieronder blijven de bron van de vragen en van wat een antwoord voor het register betekent. In het formulier is elk kenmerk een eigen ja/nee-vraag; de profielsleutels worden zo gevuld: `gegevens_soorten` = de soorten waarvoor `gegevens_*` ja is (`hr` = ja als `gegevens_medewerkers` of `gegevens_sollicitanten` ja is, anders `onbekend`); `website` uit `webshop`, `platform` en `website_info` (alle drie nee = geen website); `overeenkomsten` = de `ov_*`-sleutels die ja zijn; `beveiliging_basis` = `beveiligingsbeleid` en `tweestap_backups`; `bestaand` = de `doc_*`-sleutels die ja zijn; `Afgerond op` volgt uit `bestaand_bijgewerkt` zoals bij vraag 20.

Regels voor het verwerken van de antwoorden:

- **In het formulier** is elk kenmerk een eigen vraag Ja / Nee / Weet ik niet: leeg of "weet ik niet" = `onbekend`, nooit `nee`; "Wat is al aanwezig?" en "Welke documenten bestaan al?": alles wat niet ja is telt als `niet aangetoond`/niet bestaand (status `open`).
- **Afvinklijst met "Geen van deze"** (alleen bij een tool die geen formulier kan tonen): een aangevinkte optie = `ja` op de bijbehorende sleutel; **"Geen van deze" aangevinkt = `nee`** op alle sleutels van die vraag; **niets aangevinkt = `onbekend`**. "Weet ik niet" en een niet-beantwoorde vraag zijn altijd `onbekend`, nooit `nee` (zie `toepasselijkheid.md`).
- **Lijst "Wat is al aanwezig?"**: niet aangevinkt telt als `niet aangetoond`: de verplichting krijgt status `open`, ongeacht of het antwoord "nee" of "weet ik niet" was. Dat maakt voor het register geen verschil en scheelt een vraag per onderwerp.
- **Overslaan wat niet nodig is.** Is de rol "verwerkingsverantwoordelijke", vraag dan niet naar subverwerkers; zijn er geen persoonsgegevens, sla groep 2 en 5 grotendeels over; kies je "Geen AI", vraag dan niet naar hoog risico. Is een document aangeleverd, vul daaruit voor en laat bevestigen in het formulier (eerste optie "(voorgesteld)").
- Vraag niet om persoonsgegevens van individuele mensen en niet om wachtwoorden, sleutels of identiteitsnummers.
- **Tegenstrijdigheid** (bijvoorbeeld 1–9 medewerkers met een omzet boven € 10 miljoen): één keer terugvragen vóór gebruik, na het formulier, in één bericht.

De **sleutel** achter elke vraag is de naam in het profiel van het register.

## Groep 1 — Organisatie en rol (4 vragen)

| # | Vraag | Type | Opties | Sleutel |
|---|---|---|---|---|
| 1 | Hoeveel mensen werken er, inclusief ingehuurden? | enkel | 1–9 · 10–49 · 50–249 · 250 of meer | `medewerkers` |
| 2 | Is de jaaromzet of het balanstotaal hoger dan € 10 miljoen? | enkel | Ja · Nee · Weet ik niet | `omzet_balans` |
| 3 | Wie zijn je klanten? | enkel | Bedrijven · Consumenten · Beide | `klanten` |
| 4 | Wat is je rol bij persoonsgegevens? | enkel | Ik bepaal zelf waarvoor en hoe (verwerkingsverantwoordelijke) · Ik verwerk in opdracht van klanten (verwerker) · Beide · Weet ik niet | `rol` |

Niet meer gevraagd: sector (komt terug bij `nis2_sector`), vestigingsland (de set richt zich op Nederlands recht en Europese regels; zet `vestiging` op "niet gevraagd").

## Groep 2 — Persoonsgegevens (4 vragen)

| # | Vraag | Type | Opties | Sleutels |
|---|---|---|---|---|
| 5 | Van wie verwerk je persoonsgegevens? | afvinklijst | Klanten · Medewerkers · Sollicitanten · Websitebezoekers (leveranciers en overigen via Other) | `gegevens_soorten`; `hr` = ja bij Medewerkers of Sollicitanten, anders `onbekend` |
| 6 | Wat van dit gebeurt er? | afvinklijst | Bijzondere gegevens (gezondheid of ziekmelding, geloof, afkomst, biometrisch, strafrechtelijk) · Camera's (beveiliging, werkvloer, slim) · Besluiten of profielen die grotendeels automatisch worden bepaald · Geen van deze | `bijzondere_gegevens`, `camera`, `profilering_besluiten` |
| 7 | Om hoeveel personen gaat het ongeveer? | enkel | Minder dan 1.000 · 1.000–100.000 · Meer dan 100.000 · Weet ik niet | `omvang` |
| 8 | Wat van dit geldt voor je gegevens? | afvinklijst | Leveranciers verwerken ze voor mij (cloud, e-mail, boekhouding, salaris, CRM) · Ze gaan naar of zijn toegankelijk vanuit landen buiten de EER (bijvoorbeeld een VS-clouddienst) · Ik deel ze met organisaties die ze voor hun eigen doel gebruiken · Geen van deze | `verwerkers`, `doorgifte`, `delen` |

## Groep 3 — Website, marketing en overeenkomsten (4 vragen)

| # | Vraag | Type | Opties | Sleutels |
|---|---|---|---|---|
| 9 | Wat heb je online? | afvinklijst | Webshop · App of platform (ook waar gebruikers zelf inhoud plaatsen) · Alleen een informatieve website · Geen website | `website`; webshop + klanten = Consumenten of Beide geeft "webshop voor consumenten", anders "webshop voor bedrijven"; bij "App of platform" noteer je de vraag "platform met gebruikersinhoud?" als `open` bij platformvoorwaarden |
| 10 | Wat van dit doe je? | afvinklijst | Cookies of trackers gebruiken (ook analytics, advertenties, chatwidget) · Nieuwsbrief, commerciële berichten of koude acquisitie · Producten of diensten verkopen (met of zonder eigen algemene voorwaarden) · Geen van deze | `trackers`, `marketing`, `verkoop` |
| 11 | Wat lever of laat je maken? | afvinklijst | SaaS of cloud leveren · Software licentiëren · Software bouwen of laten bouwen · Geen van deze | `overeenkomsten` (SaaS/cloud, licentie, laten bouwen) |
| 12 | Welke afspraken sluit je regelmatig? | afvinklijst | Service level agreement (beschikbaarheid en support) · Geheimhouding (NDA) · Geen van deze | `overeenkomsten` (SLA, NDA) |

## Groep 4 — AI, cyber en beveiliging (4 vragen)

| # | Vraag | Type | Opties | Sleutels |
|---|---|---|---|---|
| 13 | Hoe komt AI voor in je organisatie? | afvinklijst | Medewerkers gebruiken AI-tools (chatbots, schrijf-, code-, vertaaltools) · Ik bouw of lever AI, of bouw AI in mijn product · Ik koop AI-systemen of -onderdelen in · Geen van deze | `ai_gebruik`, `ai_eigen`, `ai_inkoop` |
| 14 | Gebruik je AI voor werving of beoordeling van personeel, kredietwaardigheid, toegang tot diensten, biometrische identificatie, veiligheidsonderdelen of kritieke infrastructuur? | enkel | Ja · Nee · Weet ik niet | `ai_hoog_risico` (alleen als vraag 13 AI oplevert; anders `nee`) |
| 15 | Werkt de organisatie in energie, vervoer, bankwezen, zorg, water, digitale infrastructuur, ICT-dienstverlening, overheid, post, afval, chemie, voedsel, industrie, digitale platforms of onderzoek? | enkel | Ja (welke: via Other) · Nee · Weet ik niet | `nis2_sector` |
| 16 | Wat is al aanwezig? | afvinklijst | Schriftelijk beveiligingsbeleid · Tweestapsverificatie en geteste back-ups · Vaste datalekprocedure (wie meldt, wie beslist, register) · FG of vast aanspreekpunt privacy | `beveiliging_basis`, `datalek_proces`, `fg` (zie de regel voor "Wat is al aanwezig?") |

## Groep 5 — Samenwerking en bestaande documenten (≤ 4 vragen, vaak 2)

| # | Vraag | Type | Opties | Sleutels |
|---|---|---|---|---|
| 17 | Schakel je zelf leveranciers in voor gegevens van klanten? (alleen als rol = verwerker of beide) | enkel | Ja · Nee · Weet ik niet | `subverwerkers` |
| 18 | Bepaal je samen met een andere organisatie waarvoor en hoe gegevens worden gebruikt? (alleen bij persoonsgegevens) | enkel | Ja · Nee · Weet ik niet | `gezamenlijk` |
| 19 | Welke van deze documenten bestaan al? | afvinklijst | Privacyverklaring · Verwerkersovereenkomst(en) · Verwerkingsregister · Beveiligings- of datalekbeleid (overige via Other) | `bestaand` (alleen documenten die voor deze organisatie gelden) |
| 20 | Wanneer zijn die voor het laatst bijgewerkt? (alleen als er in vraag 19 iets bestaat) | enkel | Dit jaar · Vorig jaar · Langer geleden · Weet ik niet | `Afgerond op`: "Dit jaar" en "Vorig jaar" zijn bij benadering (1 januari van dat jaar met de opmerking "datum bij benadering"); "Langer geleden" en "Weet ik niet" laten de datum leeg. Eén antwoord geldt voor alle aangevinkte documenten; wijkt er één af, zeg het via Other |

## Groep 6 — Huisstijl (4 vragen)

Alleen de basis; standaardkeuzes (betaaltermijn, opzegtermijn, aansprakelijkheidsplafond, rechter) en eigen clausules worden nu **niet** gevraagd: noem aan het eind dat ze later kunnen met `/huisstijl-en-standaardclausules`. Vraag H1 tot H4 van `../huisstijl-en-standaardclausules/huisstijl-sjabloon.md` en laat niets weg dat daar verplicht is; is dat bestand niet bij de hand, gebruik dan deze vier:

| # | Vraag | Type | Opties |
|---|---|---|---|
| H1 | Wat is de rechtsvorm? Typ bij Other de naam met rechtsvorm (bijvoorbeeld "Voorbeeld B.V.") als je die wilt vastleggen | enkel | Eenmanszaak of eigen project · BV of NV · Stichting of vereniging · VOF, maatschap of anders |
| H2 | Hoe spreek je lezers aan en welke toon? | enkel | U, formeel · U, zakelijk · Je/jij, toegankelijk · Geen voorkeur |
| H3 | Welke partijnamen gebruik je in overeenkomsten? | enkel | Opdrachtgever/Opdrachtnemer · Klant/Leverancier · Verwerkingsverantwoordelijke/Verwerker · Geen voorkeur |
| H4 | Welke opmaak? Kies één nummering en één bestandsvorm | afvinklijst | Nummering 1.1.1 · Artikel 1, 2, … · Word · PDF |

Bij H1 zonder getypte naam: `Organisatie` = `[IN TE VULLEN]`. KvK-nummer, zetel en ondertekenaar komen pas bij het eerste document dat ze nodig heeft.
