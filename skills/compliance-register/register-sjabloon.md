# Register — structuur

Peildatum 2026-11-10. `compliance-register.md` is een Markdown-bestand met vijf secties, elk met één tabel. De kolomnamen en statuswaarden zijn vast: `/compliance-overzicht` en `register.py` lezen ze zo.

## Secties en kolommen

**Profiel** — `Sleutel | Waarde`. Bevat `Organisatie`, `Register aangemaakt` en per vraag uit `onboarding-vragen.md` de sleutel met het antwoord (`onbekend` als het niet bekend is).

**Verplichtingen** — `ID | Skill | Domein | Onderwerp | Status | Toepasselijk sinds | Afgerond op | Volgende review | Opmerking`
- `ID`: `V-001`, `V-002`, … (wordt automatisch gevuld).
- `Domein`: exact `Privacy`, `Informatiebeveiliging`, `AI & cyber` of `Contracten`.
- `Status`: `open` (nog niet gestart), `loopt`, `klaar`, `n.v.t.` (met reden in `Opmerking`).
- Datums als `JJJJ-MM-DD`. `Afgerond op` hoort bij `klaar`; zonder datum telt de verplichting mee in de score maar niet in de trendlijn.

**Taken** — `ID | Taak | Skill | Deadline | Prioriteit | Status`
- `ID`: `T-001`, …; `Prioriteit`: `hoog`, `middel`, `laag`; `Status`: `open` of `klaar`.

**Risico's** — `ID | Omschrijving | Niveau | Skill | Status`
- `ID`: `R-001`, …; `Niveau`: `hoog`, `middel`, `laag` (inschatting van de gebruiker); `Status`: `open` of `beheerst`.

**Activiteit** — `Datum | Skill | Gebeurtenis | Uitkomst`. Eén regel per gebeurtenis, nieuwste onderaan of bovenaan maakt niet uit; het overzicht sorteert zelf.

## Hoe het overzicht rekent

- **Voortgang per domein** = aantal verplichtingen met status `klaar` ÷ aantal toepasselijke verplichtingen (alles behalve `n.v.t.`), afgerond op een geheel getal. Zonder toepasselijke verplichtingen is er geen percentage (`—`).
- **Totaal** = dezelfde berekening over alle domeinen samen. Alle verplichtingen wegen even zwaar. Dit is een voortgangsmaat, geen oordeel over naleving.
- **Trend** = per maand de stand op de laatste dag van die maand, berekend uit `Toepasselijk sinds` en `Afgerond op`. De huidige maand gebruikt de huidige stand. Verplichtingen zonder afrondingsdatum tellen in eerdere maanden niet als klaar.
- **Open risico's** = risico's met status `open`, per niveau.
- **Volgende stappen** = in deze volgorde: taken die te laat zijn, open hoge risico's, verlopen reviews, deadlines binnen 30 dagen, open verplichtingen, lopende verplichtingen.

## Registerregel bij een afgerond document

Na elk document of elke toets uit deze set kan de gebruiker zeggen "registreer dit". Dan komen er twee wijzigingen:
1. de verplichting krijgt status `klaar` (of `loopt`) met `Afgerond op` = vandaag;
2. een activiteitsregel: datum · skill · wat er is gedaan · uitkomst (bijvoorbeeld ✅ ⚠️ ❌ van een toets, of "opgesteld").
Een toets met ⚠️ of ❌ leidt tot een taak of risico, alleen op instructie van de gebruiker of met zijn bevestiging.
