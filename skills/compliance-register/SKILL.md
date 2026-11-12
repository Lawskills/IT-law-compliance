---
name: compliance-register
description: "Toont je hele compliance-register: profiel, alle verplichtingen, taken, risico's en activiteit, zoals ze in jouw register staan, met filters op domein, status of onderdeel. Gebruik bij \"compliance-register\", \"laat mijn register zien\", \"toon het hele register\", \"alle verplichtingen\" of \"wat staat er in mijn register\"."
---

# /compliance-register — Je hele register in beeld

Toont **alles** wat in je `compliance-register.md` staat, onderdeel voor onderdeel, zonder berekening of samenvatting: Profiel, Verplichtingen, Taken, Risico's en Activiteit. Wil je een dashboard met voortgang en trend, gebruik dan `/compliance-overzicht`. Wil je weten of je een verwerkingsregister (art. 30 AVG) moet bijhouden, gebruik dan `/toets-verwerkingsregister`; dat is een ander document dan dit register.

> **Toont wat er staat.** Deze skill laat de inhoud van je register zien en verzint niets. Ontbreekt iets, dan is het register niet compleet; de skill vult het niet aan. Het is geen oordeel over naleving en geen juridisch advies.

## Werkwijze

1. **Register zoeken.** Zoek `compliance-register.md` in de bijlagen, de projectbestanden of de werkmap. Is er geen register, zeg dat in één zin en verwijs naar `/compliance-onboarding`; toon niets.
2. **Valideren.** Draai `python3 register.py validate compliance-register.md` (script in deze map). Meld fouten (onbekende status, ongeldige datum) in één regel en toon het register daarna toch, met de waarschuwing erbij.
3. **Tonen.** Draai `python3 register.py show compliance-register.md` voor het hele register als tabellen. Vraagt de gebruiker om een deel, geef dan een filter mee:
   - `--sectie profiel|verplichtingen|taken|risicos|activiteit`
   - `--status open|loopt|klaar|n.v.t.` (bij taken `open|klaar`, bij risico's `open|beheerst`)
   - `--domein Privacy|Informatiebeveiliging|"AI & cyber"|Contracten` (alleen verplichtingen)
   Is Python niet beschikbaar, lees dan het bestand zelf en geef de tabellen ongewijzigd weer.
4. **Weergave.** Toon de tabellen in de reply, volledig; kort ze niet in en laat geen kolommen of regels weg. Is het register lang, toon dan eerst de aantallen per onderdeel en bied filters aan, maar houd de volledige lijst beschikbaar.
5. **Toelichting.** Maximaal drie regels naast de tabellen: hoeveel regels er per onderdeel staan en wat er in `validate` is gemeld. Geen conclusies over naleving.
6. **Bijwerken.** Zegt de gebruiker "registreer: …", gebruik dan de werkwijze van `/compliance-overzicht` (`register.py add|set`, alleen wat de gebruiker zegt, hele bestand teruggeven). Toon daarna alleen een nieuwe lijst als de gebruiker dat vraagt.

## Harde regels

- **Alles uit het register.** Geen voorbeeldregels, geen aanvullingen, geen geschatte datums of niveaus.
- **Niets weglaten.** Een leeg veld blijft zichtbaar als `–`; een lege sectie meldt dat er geen regels zijn.
- **Geen persoonsgegevens** in het register of in de weergave.
- **Bronnen.** Wil de gebruiker weten waarop een verplichting rust, verwijs naar `/compliance-chat`.

## Referenties

- `register.py` — leest het register (`show`, `validate`, `add`, `set`, `metrics`, `text`, `html`).
- `register-sjabloon.md` — structuur van het register: secties, kolommen en toegestane waarden.
