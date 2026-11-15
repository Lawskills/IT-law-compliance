# IT-law-compliance — Lawskills

**45 Claude-skills voor Nederlands en Europees IT-recht en compliance.** Je start een skill, beantwoordt een paar vragen in aanklikbare velden en Claude schrijft het document of geeft een toetsrapport, met de wettelijke grondslag erbij. Wat nog ontbreekt of onzeker is, staat zichtbaar gemarkeerd (`[IN TE VULLEN: …]` of ⚠️).

[English version](README.en.md) · [Releases](https://github.com/Lawskills/IT-law-compliance/releases) · [Wijzigingen](CHANGELOG.md) · [Licentie](#licentie)

Repository en website: [Lawskills/IT-law-compliance](https://github.com/Lawskills/IT-law-compliance) · [lawskills.github.io/IT-law-compliance](https://lawskills.github.io/IT-law-compliance/)

## Waarom dit project

Veel compliancewerk in het mkb is herhaling: een verwerkersovereenkomst, een privacyverklaring, een cookietoets, een DPIA. De regels staan vast in de wet, maar het toepassen kost tijd en een fout zit snel in een detail. Lawskills legt die regels vast in toetsingskaders met vaste rekenregels, zodat Claude per stap dezelfde vragen stelt en dezelfde afweging maakt, en zegt wanneer iets niet zeker is in plaats van te gokken.

## Wat het doet

- **Opstellen** (24 skills): verwerkersovereenkomst, privacyverklaring, DPIA, datalekprocedure, NDA, SLA, SaaS-overeenkomst, algemene voorwaarden, AI-gebruiksbeleid en meer.
- **Toetsen** (16 skills): AVG (rol, grondslag, beginselen, beveiliging, doorgifte), cookies, direct marketing, AI-verordening, Cyberbeveiligingswet en toegankelijkheid. Elk toetspunt krijgt ✅ voldoet, ⚠️ in te vullen, ❌ voldoet niet of n.v.t., met grondslag en vervolgstap.
- **Werkruimte** (4 skills): onboarding met register, dashboard, een bronnenchat die alleen uit de bronnenlijst antwoordt, en een update-skill.

Niet ingevuld is nooit "voldoet": een antwoord dat nodig is maar ontbreekt (ook "weet ik niet"), geeft ❌ voldoet niet; bij een aanbeveling ⚠️ in te vullen. Nooit stilzwijgend "voldoet" of "geldt niet".

## Aan de slag

1. **Installeer** de skills (zie [Installeren](#installeren)).
2. **Start met onboarding:** zeg `/compliance-onboarding`. Claude stelt eenmalig vragen over je organisatie, bepaalt welke verplichtingen voor jou gelden en maakt je register (`compliance-register.md`). Bewaar dat bestand in een Project of je werkmap; de skills onthouden het niet vanzelf.
3. **Kies wat je nodig hebt:** een document opstellen (bijvoorbeeld `/privacyverklaring`) of iets toetsen (bijvoorbeeld `/toets-cookies`). Je beantwoordt de vragen als aanklikbare velden.
4. **Registreer het resultaat:** zeg na een afgerond document "registreer dit". Met `/compliance-overzicht` zie je daarna je voortgang, open punten en taken.

## Installeren

### Claude.ai (aanbevolen: één bundel)

Claude.ai laat alle skills los in één lijst zien. Met de bundel heb je één regel, `lawskills`, met een menu: je kiest een onderwerp en daarna de toets of het document.

1. Download `lawskills-bundel.zip` van de nieuwste release (rechts op deze pagina onder *Releases*).
2. Ga naar **Instellingen → Skills** en upload de zip.
3. Open een nieuwe chat en typ `lawskills`.

Gebruik de bundel of de losse skills, niet allebei: verwijder bij het overstappen eerst de losse skills uit deze set. Claude herkent bij de bundel een losse vraag minder snel vanzelf; begin daarom bij `lawskills`.

Liever losse skills? Download `lawskills-losse-skills.zip` uit dezelfde release, pak die uit en upload de zips per skill. Installeer ze dan allemaal: `/compliance-chat` leest de bestanden van de andere skills.

### Claude Code

```
/plugin marketplace add Lawskills/IT-law-compliance
/plugin install lawskills@it-law-compliance
```

De skills heten dan `/lawskills:verwerkersovereenkomst`, `/lawskills:toets-cookies` enzovoort. Typ `/lawskills:` en alle skills staan onder die ene naam. Willen je korte namen (`/dpia`), kopieer dan de map `skills/` naar `~/.claude/skills/`.

## Bijwerken

- **Claude Code:** zeg `/lawskills:compliance-update`. Die toont je versie en wat er nieuw is, werkt de plugin bij (na jouw akkoord) en ruimt oude of dubbele skills op. Start Claude Code daarna opnieuw op. Handmatig kan ook: `/plugin marketplace update` en daarna `/plugin update lawskills@it-law-compliance`. Die commando's werken alleen in de Claude Code-terminal, niet in de chat.
- **Claude.ai:** download de nieuwste `lawskills-bundel.zip`, upload die onder dezelfde naam (de oude wordt vervangen) en begin een nieuwe chat. Een lopend gesprek gebruikt nog de oude versie. `/compliance-update` loopt deze stappen met je door.
- **Oude skills:** had je vroeger de skills `chat`, `overzicht` of `onboarding`? Die heten nu `compliance-chat`, `compliance-overzicht` en `compliance-onboarding`. Verwijder de oude via het menu (⋯) in Instellingen → Skills, nadat de nieuwe er staan.

## Hulpskills

| Skill | Wat het doet |
|---|---|
| `/compliance-onboarding` | Stelt alle relevante vragen over je organisatie, bepaalt welke verplichtingen voor jou gelden, legt je huisstijl vast en maakt het register |
| `/compliance-overzicht` | Toont je dashboard: voortgang per domein, trend per maand, open risico's, taken en volgende stappen. Alle getallen komen uit jouw register; de voortgang is het aandeel verplichtingen dat op `klaar` staat, geen nalevingsscore |
| `/compliance-register` | Toont je hele register: profiel, verplichtingen, taken, risico's en activiteit, precies zoals ze erin staan, met filters op domein of status |
| `/compliance-chat` | Beantwoordt vragen over privacy, AI, cyber en contracten, alleen met bronnen uit de bronnenlijst van deze set, met bronvermelding en status per bewering |
| `/compliance-update` | Controleert je versie, toont wat er nieuw is en werkt de set bij |

## Documenten opstellen

Je beantwoordt de vragen en Claude schrijft het volledige document, met de keuzes die je hebt gemaakt en een lijst van wat je nog moet invullen of controleren. Heb je een eigen huisstijl of eigen standaardclausules? Leg ze eenmalig vast met `/huisstijl-en-standaardclausules`; de andere skills gebruiken die daarna.

| Skill | Wat het opstelt | Grondslag |
|---|---|---|
| `/huisstijl-en-standaardclausules` | Je eigen huisstijl en standaardclausules vastleggen, die alle opstel-skills gebruiken | eigen keuzes, met voorrang van de wet |
| `/verwerkersovereenkomst` | Verwerkersovereenkomst, als verantwoordelijke of als verwerker | art. 28 AVG |
| `/subverwerkersovereenkomst` | Overeenkomst met een subverwerker | art. 28 lid 2 en 4 AVG |
| `/gegevensdelingsovereenkomst` | Afspraken tussen zelfstandige verantwoordelijken | art. 5, 6, 32, 33 en 44–46 AVG, goede praktijk |
| `/samenwerkingsafspraken` | Regeling gezamenlijke verwerkingsverantwoordelijkheid | art. 26 AVG |
| `/scc-bijlagen` | Bijlagen bij de standaardcontractbepalingen (doorgifte buiten de EER) | art. 44–46 AVG en de SCC-clausules |
| `/privacyverklaring` | Privacyverklaring | art. 13 en 14 AVG |
| `/cookieverklaring` | Cookieverklaring | Telecommunicatiewet 11.7a, AVG |
| `/dpia` | Gegevensbeschermingseffectbeoordeling | art. 35 AVG |
| `/datalekprocedure` | Procedure voor datalekken | art. 33 en 34 AVG |
| `/datalekmelding` | Melding van een datalek aan de Autoriteit Persoonsgegevens | art. 33 AVG |
| `/verzoek-betrokkene` | Antwoord op een inzage-, correctie-, verwijder- of ander verzoek | art. 12 t/m 22 AVG |
| `/bewaarbeleid` | Bewaarbeleid | art. 5 lid 1 sub e AVG |
| `/beveiligingsbeleid` | Informatiebeveiligingsbeleid | art. 32 AVG |
| `/geheimhoudingsovereenkomst` | NDA, eenzijdig of wederzijds | art. 6:248 BW, Wet bescherming bedrijfsgeheimen, goede praktijk |
| `/ai-gebruiksbeleid` | AI-gebruiksbeleid voor medewerkers | AI-verordening (o.a. art. 4), goede praktijk |
| `/ai-inkoopafspraken` | AI-bijlage bij een inkoopovereenkomst | AI-verordening, art. 28 AVG, EU-modelclausules (MCC-AI) |
| `/algemene-voorwaarden` | Algemene voorwaarden, zakelijk of consument | Boek 6 en 7 BW |
| `/sla` | Service level agreement | goede praktijk, AVG, Data Act |
| `/saas-overeenkomst` | SaaS- of cloudovereenkomst met overstapregels | Data Act (o.a. art. 25), art. 28 AVG |
| `/softwarelicentie` | Softwarelicentie (EULA) | Auteurswet, Boek 7 BW |
| `/ontwikkelovereenkomst` | Ontwikkelovereenkomst met overdracht van intellectueel eigendom | Auteurswet, Boek 7 BW |
| `/platformvoorwaarden` | Gebruiksvoorwaarden voor een online platform | Digital Services Act |
| `/website-verplichte-informatie` | Verplichte bedrijfsinformatie voor je website | art. 3:15d en 6:227b e.v. BW |

## Toetsen

Een toetsskill stelt eerst vragen en beoordeelt dan elk toetspunt met een uitkomst: ✅ voldoet, ⚠️ in te vullen, ❌ voldoet niet, of n.v.t. (geldt niet voor jou), met de wettelijke grondslag erbij en wat je kunt doen.

| Skill | Wat het toetst |
|---|---|
| `/toets-toepasselijkheid-rol` | Is de AVG van toepassing, en ben je verantwoordelijke, verwerker of gezamenlijk verantwoordelijke? |
| `/toets-grondslag` | Geldige grondslag per doel; bijzondere persoonsgegevens, strafrechtelijke gegevens en BSN |
| `/toets-beginselen` | Beginselen van art. 5 AVG, bewaartermijnen en privacy by design en by default |
| `/toets-verwerkingsregister` | Registerplicht en inhoud van het register (art. 30 AVG) |
| `/toets-fg-plicht` | Moet je een functionaris gegevensbescherming aanstellen? |
| `/toets-beveiliging` | Passende beveiligingsmaatregelen (art. 32 AVG) |
| `/toets-doorgifte` | Doorgifte buiten de EER en de doorgiftetoets (TIA) |
| `/toets-cameratoezicht` | Cameratoezicht door bedrijven |
| `/toets-hr-privacy` | Verzuim en zieke werknemers; werving en selectie |
| `/toets-geautomatiseerde-besluiten` | Geautomatiseerde besluitvorming en profilering (art. 22 AVG) |
| `/toets-cookies` | Cookies en trackers, uitzonderingen, toestemming en cookiebanner |
| `/toets-direct-marketing` | E-mailmarketing, spam en telemarketing |
| `/toets-ai-act-basis` | AI-systeem en rol, verboden praktijken, signaal hoog risico, AI-geletterdheid, transparantie |
| `/toets-ai-act-hoog-risico` | Plichten bij hoogrisico-AI per rol (gebruiker, aanbieder, importeur, distributeur) en de grondrechtentoets |
| `/toets-cyberbeveiligingswet` | Plichten uit de Cyberbeveiligingswet |
| `/toets-toegankelijkheid` | Toegankelijkheid van een webshop of app (European Accessibility Act) |

Een toets of document begint met één intake: alle vragen die nu nodig zijn komen in één keer, ja/nee-vragen als afvinklijst van drie, en alleen vragen die van een antwoord afhangen volgen daarna in één tweede ronde (meestal is dat de laatste). Een vraag die voor jou niet meer geldt, wordt overgeslagen. "Weet ik niet" mag bijna altijd; het toetspunt komt dan op ⚠️ (nooit stilzwijgend op "voldoet" of "geldt niet"). Een plicht die pas later gaat gelden, bijvoorbeeld de hoogrisicoplichten van de AI-verordening (vanaf 2 december 2027 of 2 augustus 2028), staat als voorbereidingspunt met de datum erbij.

## Beperkingen

- De skills zijn een hulpmiddel en geen juridisch advies. Controleer feiten, bedragen en keuzes voordat je een document gebruikt, en raadpleeg bij een bijzondere situatie een gespecialiseerd adviseur.
- Een toets beoordeelt alleen wat je zelf aangeeft of aanlevert; ze kan niet nagaan of dat klopt.
- Wet- en regelgeving verandert. Een wekelijkse bronnencontrole verkleint het risico op verouderde teksten, maar sluit het niet uit. Peildatum van de huidige inhoud: 2026-11-10.
- Standaardbepalingen (duur, aansprakelijkheid, meldtermijnen) zijn gangbare keuzes, geen wettelijke eisen. Let bij complexe contracten (SaaS, ontwikkelovereenkomst, platformvoorwaarden, AI-inkoop) extra op de gekozen aansprakelijkheid en looptijd.
- De structuur en de rekenregels worden bij elke wijziging automatisch getest; de juridische inhoud nog niet systematisch. Meld fouten via een issue.
- `/compliance-overzicht` rekent met wat in je register staat; een register dat je niet bijhoudt geeft een verouderd overzicht.
- Er worden geen persoonsgegevens van betrokkenen gevraagd; namen van verzoekers en dergelijke vul je zelf in.

## Meer

- Wijzigingen per versie: [CHANGELOG.md](CHANGELOG.md)
- Fouten of suggesties: open een [issue](https://github.com/Lawskills/IT-law-compliance/issues)

## Licentie

© 2026 Akram al Khafaji.

- **Teksten** (skills, kaders, documentatie): [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). Je mag ze gebruiken, delen en bewerken, ook commercieel, mits je de naam *Akram al Khafaji* en een link naar deze repository noemt en aangeeft wat je hebt gewijzigd.
- **Code** (de `.py`-bestanden): [MIT](LICENSE-CODE).

Bronvermelding van gebruikt materiaal: [NOTICE.md](NOTICE.md). Er is geen garantie; dit is een hulpmiddel, geen juridisch advies.
