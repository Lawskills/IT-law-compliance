# Huisstijl en eigen standaardclausules — sjabloon

Peildatum 2026-11-10. Dit is de structuur van `huisstijl.md`. Laat onderdelen leeg waarvoor geen voorkeur bestaat; dan geldt de standaard uit `bepalingen.md`.

## Vragenlijst (route b)

**Organisatie**
1. Naam, rechtsvorm en statutaire zetel van de organisatie?
2. Wie tekent doorgaans (naam en functie), en welk adres/KvK-nummer staat op documenten?

**Taal en toon**
3. Aanspreekvorm in verklaringen en beleid: je/jij of u? Toon: formeel, zakelijk of toegankelijk?
4. Voorkeur voor definities van partijen (Opdrachtgever/Opdrachtnemer, Klant/Leverancier, Verwerkingsverantwoordelijke/Verwerker)?

**Opmaak**
5. Nummering (1, 1.1, 1.1.1 of artikel 1, 2, …)? Kopstijl? Voorkeur voor tabellen of lopende tekst?
6. Aflevering als Word, PDF of Markdown? Standaard voetregel of documentgegevens (versie, datum, eigenaar)?

**Standaardkeuzes** (alleen invullen als je een vaste lijn hebt)
7. Betaaltermijn, opzegtermijn, looptijd en verlenging.
8. Aansprakelijkheid: plafond (bijv. aantal maanden vergoedingen) en uitzonderingen.
9. Toepasselijk recht en bevoegde rechter of arbitrage.
10. Geheimhoudingsduur, meldtermijn datalekken richting leveranciers, bewaartermijnen.

**Eigen clausules**
11. Welke eigen clausules wil je altijd gebruiken? Plak ze, of verwijs naar een bestaand document; noem per clausule het onderwerp en voor welk documenttype.

**Wat nooit mag**
12. Bepalingen die je nooit accepteert of opneemt (bijv. onbeperkte aansprakelijkheid, boetes zonder plafond).

## Structuur van huisstijl.md

```
# Huisstijl — <organisatie>
Versie: <datum> · Eigenaar: <naam>

## Organisatie
<naam, rechtsvorm, zetel, KvK, ondertekenaar>

## Taal en toon
<aanspreekvorm, toon, voorkeur termen>

## Opmaak
<nummering, koppen, tabellen, bestandsvorm, voetregel>

## Standaardkeuzes
- betaaltermijn: …
- opzegtermijn: …
- aansprakelijkheid: …
- toepasselijk recht: …

## Nooit opnemen
- …

## Eigen clausules
### [verwerkersovereenkomst] Subverwerkers
<tekst letterlijk>

### [algemene-voorwaarden] Aansprakelijkheid
<tekst letterlijk>
```

Gebruik bij elke clausule de naam van de skill tussen vierkante haken en het onderwerp zoals dat in `bepalingen.md` van die skill staat, zodat de skill de clausule op de juiste plek vindt.
