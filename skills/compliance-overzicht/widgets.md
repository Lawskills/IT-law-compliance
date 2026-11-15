# Widgets — wat het overzicht toont en hoe

Peildatum 2026-11-11. `python3 register.py html compliance-register.md` geeft een zelfstandig HTML-fragment (eigen stijl in de look van de site, werkt op smal scherm). De widgets staan in deze volgorde:

1. **Kop** — organisatie, peildatum, ring met totaalvoortgang, zin met "x van y klaar · z loopt · n open".
2. **Domeinkaarten** — Privacy, Informatiebeveiliging, AI & cyber, Contracten: percentage, balk, "x van y klaar · loopt · open". Geen toepasselijke verplichtingen: `—`.
3. **Voortgang per maand** — lijngrafiek met de totaallijn (dik) en een lijn per domein, y-as 0–100 %, laatste 12 maanden. Eén meetpunt: de grafiek toont dat punt en meldt dat de lijn vanaf de tweede maand verschijnt.
4. **Risico's (open)** — donut hoog / middel / laag met het aantal in het midden; geen open risico's: lege staat.
5. **Volgende stappen** — maximaal zes, in de volgorde van `register-sjabloon.md` (te late taken eerst).
6. **Openstaande taken** — tabel met taak, deadline (te laat in rood met tekst "te laat") en prioriteit.
7. **Recente activiteit** — de zes nieuwste regels uit Activiteit.
8. **Let op** — waarschuwingen (bijvoorbeeld klaar zonder afrondingsdatum). Alleen zichtbaar als er waarschuwingen zijn.
9. **Voetnoot** — wat de voortgang wel en niet is.

Het ontwerp volgt de site: een lichtgrijze achtergrond met zachte vlekken en leisteengrijze glaskaarten met ronde hoeken en witte tekst; rechtsonder staat klein Lawskills™. Er zijn twee accentkleuren met een vaste betekenis: **geel `#FFFF00` = voldoet / klaar** (voortgangsbalken met een lichtgeel spoor, ring, pil, middel en laag risico) en **blauw `#48CAE4` = voldoet niet / nog te doen** (spoor van de ring, hoog risico, "te laat"). Groen en rood worden niet gebruikt. Het formulier van `kader.py formulier` gebruikt dezelfde stijl en dezelfde kleurtokens (`--g-*`); daar is geel de gekozen optie en de knop, blauw de melding "nog verplicht". Kleur draagt nooit alleen de betekenis: domeinlijnen verschillen ook in lijnstijl (doorgetrokken, gestreept, gestippeld), risiconiveaus staan als tekst en "te laat" staat vetgedrukt en onderstreept met de tekst "(te laat)".

## Weergaveroutes, in volgorde van voorkeur

1. **Visualisatietool in de chat** (bijvoorbeeld `show_widget`): roep zo nodig eerst de bijbehorende `read_me` aan, geef de uitvoer van `register.py html` als widgetcode en voeg niets toe aan de inhoud.
2. **HTML-artifact**: schrijf de uitvoer naar `overzicht.html`; publiceer als artifact als het gereedschap beschikbaar is, anders lever het bestand af (openen in de browser).
3. **Diagramtool voor de trendlijn** (`chart_display_v0`, stijl `line`): x-as = `trend.maanden`; series = `Totaal` (`trend.totaal`) en per domein `trend.domeinen[<naam>]`; `null`-waarden weglaten of op de vorige waarde laten staan alleen als dat in de toelichting staat. Rest als tekst uit `register.py text`.
4. **Alleen tekst**: `register.py text` (tabel met balken, sparkline van de trend, lijsten).

## Controle voor het tonen

- Komt het totaal in de kop overeen met de som van de domeinkaarten (klaar en toepasselijk)? Zo niet: niet tonen, eerst zoeken waarom (bijvoorbeeld een verplichting met een onbekend domein, dat als "Overig" wordt geteld).
- Eindigt de trendlijn op dezelfde waarde als de kaarten? Zo niet, dan ontbreekt waarschijnlijk een datum; zeg dat.
