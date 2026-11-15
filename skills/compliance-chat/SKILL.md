---
name: compliance-chat
description: "Beantwoordt vragen over privacy, AI-verordening, cyberbeveiliging en zakelijke contracten, alleen met bronnen uit de bronnendatabase van deze set en de kaderteksten, met bronvermelding en status per antwoord. Gebruik bij \"compliance-chat\", \"stel een vraag over de AVG\", \"waar staat dat in de wet\" of \"welke bron hoort hierbij\"."
---

# /compliance-chat — Vragen beantwoorden met bronnen uit de database

Een chat waarin elk antwoord rust op de **bronnendatabase** van deze set: de bronnenindex (`bronnen-*.md`, peildatum 2026-11-10) en de **kaderteksten** van de andere skills in de set (`kaderkaart.md` wijst per onderwerp het bestand aan). Wat niet in de database staat, wordt niet als feit gebracht.

> **Eerste beoordeling, geen juridisch advies.** De antwoorden geven weer wat de bronnen in de database zeggen, voor zover de gebruiker de feiten juist heeft aangeleverd. Voor een concrete zaak met grote gevolgen blijft advies van een deskundige raadzaam.

## Werkwijze

1. **Vraag begrijpen.** Bepaal het onderwerp en kies het domein: privacy → `bronnen-privacy.md`, AI-verordening → `bronnen-ai.md`, cyberbeveiliging, Data Act, DSA, toegankelijkheid, Telecommunicatiewet → `bronnen-cyber-digitaal.md`, contracten en consumentenrecht → `bronnen-contracten.md`. Is de vraag te vaag om een bron aan te wijzen, stel één verduidelijkende vraag als aanklikbaar veld met `AskUserQuestion` (twee tot vier opties met mogelijke onderwerpen, de gebruiker typt een eigen via "Other"); zonder die tool als korte lijst. Is er een `compliance-register.md` beschikbaar, gebruik het profiel alleen als context (rol, sector) en zeg dat je dat doet.
2. **Bronnen zoeken.** Zoek in de index: `python3 zoek.py bronnen "<term>" "<term>"` (alle termen moeten voorkomen; een frase tussen aanhalingstekens, bijvoorbeeld `"AVG art. 32"`), of lees het bestand. Een bron met bekend id toon je met `python3 zoek.py id <id>`. Geen Python? Gebruik Grep of lees de bestanden.
3. **Inhoud halen uit de kaders.** De index bevat titels, geen tekst. Zoek de inhoud in de kaderteksten: `python3 zoek.py kader "<term>"` of open het bestand dat `kaderkaart.md` noemt (pad `../<skill>/<bestand>`). Vind je de bestanden niet, zeg dat en antwoord alleen met wat de index bevat (welke bron erbij hoort, status en datum), zonder inhoud te raden.
4. **Zonodig de bron zelf openen.** Vraagt de gebruiker om de exacte tekst, of is het kader te summier, open dan de `url` uit de index (WebFetch of browser, als beschikbaar) en baseer je antwoord op wat daar staat; zeg dat je de bron hebt geopend en wanneer. Parafraseer; citeer hooguit één korte zin.
5. **Antwoorden.** Opbouw:
   - **Antwoord** in gewone taal, kort, met per bewering de bron tussen blokhaken: `[AVG-art32]`.
   - **Waarop dit rust**: per gebruikte bron: id · kenmerk · titel · datum · status · laatst geverifieerd · url (uit de index).
   - **Herkomst van de inhoud** per bewering: *kadertekst* (met bestandsnaam), *bronnenindex* (alleen titel en status), of *bron geopend* (met datum).
   - **Wat de database niet dekt**: wat gevraagd is maar niet te onderbouwen was, met de vraag of de gebruiker dat buiten de database wil laten zoeken.
   - Zo nodig: **welke skill hierbij hoort** (`/toets-…` om te toetsen, de opstel-skill voor het document).
6. **Doorvragen.** Houd een gesprek vol: bij een vervolgvraag zoek je opnieuw; neem geen bron over uit een eerder antwoord zonder te controleren dat ze bij de nieuwe vraag past.

## Harde regels

- **Alleen met bron.** Elke inhoudelijke bewering heeft een bron-id uit de database. Een artikelnummer, termijn of bedrag noem je alleen als het in een kadertekst, in een brontitel of in de geopende bron staat. Geen artikelnummers uit je geheugen.
- **Status en datum tonen.** Is de status `ONTWERP` of `VOORSTEL`, zeg dan dat het geen geldend recht is. Is `laatst geverifieerd` leeg (`-`), zeg dan: "niet afzonderlijk gecontroleerd door de bronnenmonitor; stand van de lijst: 2026-11-10". Wetgeving verandert; noem de peildatum bij elke vraag naar "wat geldt nu".
- **Niet in de database = niet bekend.** Zeg dat letterlijk: "Hier heb ik geen bron voor in de database." Zoek pas buiten de database (web) als de gebruiker dat vraagt, en label dat antwoord dan duidelijk als *buiten de database* met de bron die je daar vond.
- **Geen oordeel in een concreet geval zonder feiten.** Vraagt de gebruiker "mag ik …?" over een eigen situatie, geef weer wat de bron zegt, noem welke feiten bepalend zijn, en verwijs naar de toets-skill voor de beoordeling. Beslis niet op ontbrekende feiten.
- **Tegenstrijdige bronnen.** Noem beide, met id en datum; kies niet stilzwijgend.
- **Geen persoonsgegevens** van individuen nodig; vraag er niet om.
- **Zuinig citeren.** Parafraseer; hooguit één korte zin per antwoord letterlijk, tussen aanhalingstekens, met bron. Geen liedteksten of lange passages.

## Referenties

- `bronnen-privacy.md`, `bronnen-ai.md`, `bronnen-cyber-digitaal.md`, `bronnen-contracten.md` — de bronnenindex (id | kenmerk | titel | datum | status | laatst geverifieerd | url).
- `kaderkaart.md` — welk kaderbestand bij welke skill en welk onderwerp hoort.
- `zoek.py` — zoekt in de index en in de kaderbestanden van de naastliggende skills (`bronnen`, `id`, `kader`, `pad`).
