---
name: compliance-update
description: "Werkt je hele compliance-set bij: controleert welke versie je hebt, toont wat er nieuw is, haalt de nieuwe versie op en ruimt oude of dubbele skills op. Gebruik bij \"compliance-update\", \"update de skills\", \"nieuwe versie\", \"werk alles bij\" of \"verwijder de oude skills\"."
---

# /compliance-update — alles in één keer bijwerken

Eén commando om de set op de nieuwste versie te krijgen en oude of dubbele skills op te ruimen. Wat Claude zelf kan, doet het (na jouw akkoord); wat alleen jij in de app kunt doen, krijg je als korte stappenlijst. Behandel elke bevinding als gegeven uit het script: noem geen versienummer of wijziging die het script niet heeft opgeleverd.

## Werkwijze

1. **Waar draait dit?** Bepaal de omgeving:
   - **Claude Code** — je kunt commando's draaien (Bash) en `claude` is beschikbaar: ga naar stap 2.
   - **Claude.ai of een omgeving zonder commando's** — ga naar "Claude.ai" hieronder.
2. **Versie controleren.** Draai `python3 update.py check` (de map van deze skill; geen Python? zeg dat en ga door met stap 3). De uitvoer heeft `geïnstalleerd`, `nieuwste`, `nieuwer` en `wijzigingen` (de changelog-regels sinds jouw versie). Lukt het ophalen niet (`nieuwste` is `null`, de reden staat erbij), zeg dat letterlijk en ga door met stap 3 zonder het versieoordeel.
3. **Samenvatten en akkoord vragen.** Toon in een paar regels: jouw versie, de nieuwste, en per nieuwe versie de kopjes uit `wijzigingen` (geen volledige tekst). Is `nieuwer` onwaar, zeg dat je al op de nieuwste versie zit en ga naar stap 6. Draai in Claude Code ook alvast `python3 update.py oud` en noem wat zou worden opgeruimd. Vraag dan **één keer** met `AskUserQuestion` (aanklikbaar veld) of Claude nu mag bijwerken én de oude skills mag opruimen, met als opties "Ja, bijwerken en opruimen" en "Alleen de wijzigingen laten zien". Na dat akkoord voer je stap 4 en 6 achter elkaar uit, zonder nog een vraag.
4. **Bijwerken (Claude Code, als plugin).** Na akkoord, in deze volgorde en met het resultaat van elk commando erbij:
   ```
   claude plugin marketplace update it-law-compliance
   claude plugin update lawskills@it-law-compliance
   ```
   Een commando dat mislukt: toon de foutmelding, probeer niet iets anders en geef de handmatige variant: `/plugin marketplace update` en daarna `/plugin update lawskills@it-law-compliance` in een gewone Claude Code-sessie. Zeg erbij dat de nieuwe versie pas na een herstart van Claude Code actief wordt (`claude plugin update` zegt dat zelf ook).
5. **Losse installatie (`~/.claude/skills`).** Draai `python3 update.py lokaal`: is `bron` gelijk aan `versie.txt` en geen plugin, dan is dit een kopie. Bijwerken doe je dan met een verse kopie uit de repository (`cp -R skills/* ~/.claude/skills/` na `git pull`); Claude doet dit alleen als de gebruiker de repository-map aanwijst, en vraagt eerst akkoord.
6. **Oude skills opruimen.** Draai `python3 update.py oud`. Staan er losse mappen `chat`, `overzicht` of `onboarding` in `~/.claude/skills`, dan zijn dat de oude namen van `compliance-chat`, `compliance-overzicht` en `compliance-onboarding`: ze staan nu naast elkaar. Vraag akkoord en verwijder alleen die mappen (`rm -r`), nooit andere. Je eigen bestanden (`compliance-register.md`, `huisstijl.md`) blijven staan: die staan in je werkmap of Project, niet in de skillmappen.
7. **Afsluiten.** Zeg wat er is bijgewerkt of verwijderd, of er een herstart nodig is, en wat de gebruiker nog zelf moet doen. Wijzig het register of de huisstijl niet; een nieuwe versie kan nieuwe vragen in een kader hebben, dus een bestaand document of toets kan na de update een andere uitkomst geven: zeg dat bij de wijzigingen die kaders raken.

## Claude.ai

Claude.ai laat skills alleen via de instellingen toe en verwijderen; Claude kan dat niet voor je doen. Geef de gebruiker deze stappen, in deze volgorde (eerst uploaden, dan pas verwijderen, anders mis je even skills):

Een skill met dezelfde naam wordt bij het uploaden vervangen, dus de **bundel** is de weg waarop de oude versie vanzelf verdwijnt: één zip uploaden en klaar. Verwijderen kan een skill of Claude hier niet voor je doen.

1. Haal de nieuwste zip op: download `lawskills-bundel.zip` (of `lawskills-losse-skills.zip`) van de nieuwste release op https://github.com/Lawskills/IT-law-compliance/releases.
2. Open **Instellingen → Skills** (op claude.ai: Instellingen → Capabilities → Skills).
3. Gebruik je de **bundel** (`lawskills-bundel.zip`, één skill met alle mappen)? Upload dan alleen die ene zip: dezelfde naam (`lawskills`) vervangt de oude bundel, en je hoeft niets te verwijderen. Gebruik bundel óf losse skills, niet allebei: stap je van losse skills over op de bundel, verwijder dan eerst alle losse skills uit deze set (anders staan ze dubbel in de lijst en kiest Claude willekeurig).
   Losse skills: upload de zips van de skills die zijn gewijzigd (alle 45 als je het zeker wilt weten). Een skill met dezelfde naam wordt vervangen. Upload `compliance-update` en `compliance-chat` samen met de overige skills: `compliance-chat` leest de kaderbestanden van de andere skills.
4. Heb je de oude skills `chat`, `overzicht` of `onboarding`? Zoek ze in dezelfde lijst, open het menu (⋯) en kies **Verwijderen**. Doe dit pas nadat `compliance-chat`, `compliance-overzicht` en `compliance-onboarding` er staan.
5. Start een **nieuwe chat**: een lopend gesprek gebruikt de oude versie.
6. Controle: vraag `/compliance-update` om de versie te tonen. Het bestand `versie.txt` in deze skill noemt de versie van jouw kopie; vergelijk die met de nieuwste versie in het changelog-bestand van de repository.

## Harde regels

- **Niets verwijderen of installeren zonder akkoord** van de gebruiker, per actie en met de exacte commando's of paden erbij.
- **Alleen deze set aanraken**: `lawskills` en de losse mappen `chat`, `overzicht` en `onboarding`. Nooit andere plugins of skills van de gebruiker.
- **Geen versie of wijziging verzinnen.** Het script levert versies en changelog-regels; kan het dat niet, zeg dat en geef de handmatige stappen.
- **Geen geheimen.** Vraag niet om een token en lees geen `.env`; het script gebruikt `gh` of een al ingestelde `GITHUB_TOKEN`.

## Referenties

- `update.py` — rekenhulp (Python, geen packages): `lokaal`, `check` en `oud`.
- `versie.txt` — de versie waarmee deze kopie is gebouwd (wordt door `tools/sync-shared.py` gezet).
