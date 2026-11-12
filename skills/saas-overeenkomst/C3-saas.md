# Kader C3 — SaaS- en cloudovereenkomst (met de Data Act)

Versie 0.1 · peildatum 2026-11-10

Doel: Controleren of een overeenkomst voor een clouddienst de verplichte overstapbepalingen van de Data Act bevat, de kosten van overstappen volgens art. 29 regelt, verwijst naar een verwerkersovereenkomst als er persoonsgegevens worden verwerkt, en de gebruikelijke onderdelen regelt.

Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3); BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a); BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248); DA-art25-lid1 (Data Act (Vo. (EU) 2023/2854) art. 25 lid 1); DA-art25-lid2-a (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub a); DA-art25-lid2-b (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub b); DA-art25-lid2-c (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub c); DA-art25-lid2-d (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub d); DA-art25-lid2-e (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub e); DA-art25-lid2-f (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub f); DA-art25-lid2-g (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub g); DA-art25-lid2-h (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub h); DA-art25-lid4 (Data Act (Vo. (EU) 2023/2854) art. 25 lid 4); DA-art29-lid1 (Data Act (Vo. (EU) 2023/2854) art. 29 lid 1); DA-art29-lid2 (Data Act (Vo. (EU) 2023/2854) art. 29 lid 2)

## Formulier (vragen aan de gebruiker)

- **supplier_name**: Wie levert de dienst?
  - Label (voor de plek-om-in-te-vullen): naam van de aanbieder
  - Type: text
- **customer_name**: Wie neemt de dienst af?
  - Label (voor de plek-om-in-te-vullen): naam van de klant
  - Type: text
- **service_name**: Om welke dienst gaat het?
  - Label (voor de plek-om-in-te-vullen): welke dienst
  - Type: text
- **data_processing_service**: Is het een digitale dienst die op afstand flexibel toegang geeft tot rekenkracht, opslag, software of een platform (zoals SaaS, PaaS of IaaS)?
  - Label (voor de plek-om-in-te-vullen): of het een gegevensverwerkingsdienst is
  - Hulp: Dat is een gegevensverwerkingsdienst in de zin van de Data Act (art. 2 punt 8).
  - Type: boolean
- **test_version**: Gaat het om een gratis test- of evaluatieversie voor beperkte tijd, niet voor productie?
  - Label (voor de plek-om-in-te-vullen): of het een test- of evaluatieversie is
  - Type: boolean
- **personal_data**: Verwerkt de aanbieder bij de dienst persoonsgegevens voor de klant?
  - Label (voor de plek-om-in-te-vullen): of de aanbieder persoonsgegevens verwerkt
  - Type: boolean
- **notice_period**: Welke opzegtermijn geldt voordat het overstappen begint (ten hoogste twee maanden)?
  - Label (voor de plek-om-in-te-vullen): de opzegtermijn voor overstappen
  - Type: text
- **exportable_data**: Welke gegevens en digitale activa kan de klant bij overstappen meenemen?
  - Label (voor de plek-om-in-te-vullen): welke gegevens en digitale activa exporteerbaar zijn
  - Type: text
- **retrieval_period**: Hoe lang kan de klant na de overgangsperiode zijn gegevens ophalen (ten minste 30 dagen)?
  - Label (voor de plek-om-in-te-vullen): de ophaalperiode
  - Type: text
- **contract_term**: Wat is de looptijd en hoe wordt opgezegd?
  - Label (voor de plek-om-in-te-vullen): de looptijd
  - Type: text
- **liability_cap**: Tot welk bedrag of welke grens is de aanbieder aansprakelijk?
  - Label (voor de plek-om-in-te-vullen): de grens van de aansprakelijkheid
  - Type: text

## Opbouw van het document en de teksten

Volg deze volgorde. Een tekst met een voorwaarde (`Alleen opnemen als`) laat je weg als de voorwaarde niet geldt (`weet ik niet` telt als niet bekend: neem de tekst op met een `[IN TE VULLEN: …]`).

### 1. Onderdeel `dienst` (standaardkop: dienst)

#### C3.1 — Welke dienst wordt geleverd
- Grondslag: goede praktijk; art. 6:248 BW als achtergrond
- Toetspunt: De overeenkomst beschrijft de dienst, de functionaliteit en wat de klant ervoor mag gebruiken
- Tekstsoort: `append_section` · Nodig: service_name

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Dienst
Aanbieder levert aan Klant {{facts.service_name}} als online dienst, zoals beschreven in de dienstbeschrijving bij deze overeenkomst.
````

### 2. Onderdeel `looptijd` (standaardkop: looptijd)

#### C3.11 — Of looptijd en opzegging zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De overeenkomst regelt looptijd, verlenging en opzegging
- Tekstsoort: `append_section` · Nodig: contract_term

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Looptijd
Looptijd en opzegging: {{facts.contract_term}}. Het recht van Klant om over te stappen volgens deze overeenkomst geldt daarnaast.
````

### 3. Onderdeel `overstappen` (standaardkop: overstappen)

#### C3.2 — Of de klant kan overstappen of exporteren binnen 30 dagen
- Grondslag: art. 25 lid 1 en lid 2 sub a Data Act
- Toetspunt: De overeenkomst stelt de klant in staat over te stappen naar een andere aanbieder of naar eigen infrastructuur, of alle exporteerbare gegevens en digitale activa te exporteren, zonder onnodige vertraging en uiterlijk na de verplichte maximale overgangsperiode van 30 kalenderdagen, met redelijke bijstand, bedrijfscontinuïteit en beveiliging tijdens het overstappen
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.data_processing_service != false and facts.test_version != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
1. Klant kan op verzoek overstappen naar een andere aanbieder of naar eigen ICT-infrastructuur, of alle exporteerbare gegevens en digitale activa exporteren. Aanbieder rondt dit af zonder onnodige vertraging en uiterlijk na een overgangsperiode van 30 kalenderdagen.
2. Aanbieder verleent tijdens het overstappen redelijke bijstand, zorgt voor de continuïteit van de dienst en handhaaft een hoog beveiligingsniveau.
````

#### C3.3 — Of de overeenkomst eindigt na het overstappen
- Grondslag: art. 25 lid 2 sub b Data Act
- Toetspunt: De overeenkomst bepaalt dat zij wordt beëindigd na afronding van het overstappen of, als de klant alleen wil wissen, aan het einde van de opzegtermijn
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.data_processing_service != false and facts.test_version != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
3. De overeenkomst eindigt zodra het overstappen met succes is afgerond, of aan het einde van de opzegtermijn als Klant alleen om wissing van zijn gegevens vraagt.
````

#### C3.4 — Of de opzegtermijn voor overstappen ten hoogste twee maanden is
- Grondslag: art. 25 lid 2 sub c Data Act
- Toetspunt: De overeenkomst noemt een maximale opzegtermijn voor het starten van het overstappen die niet langer is dan twee maanden
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.data_processing_service != false and facts.test_version != true` · Nodig: notice_period

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
4. Klant kan het overstappen starten met een opzegtermijn van {{facts.notice_period}}, die niet langer is dan twee maanden.
````

### 4. Onderdeel `data` (standaardkop: data)

#### C3.5 — Of vastligt welke gegevens en digitale activa mee kunnen
- Grondslag: art. 25 lid 2 sub d en e Data Act
- Toetspunt: De overeenkomst specificeert uitputtend alle categorieën gegevens en digitale activa die kunnen worden overgezet, ten minste alle exporteerbare gegevens; uitzonderingen voor bedrijfsgeheimen alleen als die de overstap niet belemmeren
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.data_processing_service != false and facts.test_version != true` · Nodig: exportable_data

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
1. Bij overstappen kan Klant de volgende gegevens en digitale activa meenemen: {{facts.exportable_data}}.
````

#### C3.6 — Of de klant ten minste 30 dagen heeft om gegevens op te halen
- Grondslag: art. 25 lid 2 sub f Data Act
- Toetspunt: De overeenkomst noemt een ophaalperiode van ten minste 30 kalenderdagen, die begint na de overgangsperiode
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.data_processing_service != false and facts.test_version != true` · Nodig: retrieval_period

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
2. Na de overgangsperiode kan Klant zijn gegevens ophalen gedurende {{facts.retrieval_period}}, en ten minste 30 kalenderdagen.
````

#### C3.7 — Of de gegevens daarna volledig worden gewist
- Grondslag: art. 25 lid 2 sub g Data Act
- Toetspunt: De overeenkomst garandeert de volledige wissing van alle exporteerbare gegevens en digitale activa na afloop van de ophaalperiode of eerdere succesvolle overstap
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.data_processing_service != false and facts.test_version != true`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
3. Na afloop van de ophaalperiode wist Aanbieder alle exporteerbare gegevens en digitale activa van Klant volledig, tenzij een wettelijke bewaarplicht geldt.
````

### 5. Onderdeel `privacy` (standaardkop: privacy)

#### C3.9 — Of er een verwerkersovereenkomst is
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Verwerkt de aanbieder persoonsgegevens voor de klant, dan bevat of verwijst de overeenkomst naar een verwerkersovereenkomst volgens art. 28 lid 3 AVG
- Tekstsoort: `append_section` · Alleen opnemen als: `facts.personal_data != false`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Persoonsgegevens
Voor de verwerking van persoonsgegevens door Aanbieder in opdracht van Klant sluiten partijen een verwerkersovereenkomst die voldoet aan artikel 28 lid 3 AVG.
````

### 6. Onderdeel `beschikbaarheid` (standaardkop: beschikbaarheid)

#### C3.10 — Of beschikbaarheid en ondersteuning zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De overeenkomst of een SLA regelt beschikbaarheid en ondersteuning
- Tekstsoort: `append_section`

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Beschikbaarheid
Voor beschikbaarheid, ondersteuning en storingen geldt de service level agreement bij deze overeenkomst.
````

### 7. Onderdeel `aansprakelijkheid` (standaardkop: aansprakelijkheid)

#### C3.12 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 6:233 onder a BW als achtergrond
- Toetspunt: De overeenkomst regelt de aansprakelijkheid van de aanbieder
- Tekstsoort: `append_section` · Nodig: liability_cap

Tekst (vul `{{facts.x}}` in met het antwoord; ontbreekt het antwoord: `[IN TE VULLEN: <label van het feit>]`):

````
## Aansprakelijkheid
De aansprakelijkheid van Aanbieder is beperkt tot {{facts.liability_cap}}, behalve bij opzet of bewuste roekeloosheid.
````

## Toetspunten (voor de eindcontrole)

### C3.1 — Welke dienst wordt geleverd
- Grondslag: goede praktijk; art. 6:248 BW als achtergrond
- Toetspunt: De overeenkomst beschrijft de dienst, de functionaliteit en wat de klant ervoor mag gebruiken
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Beschrijf welke dienst wordt geleverd en waarvoor de klant die mag gebruiken.

### C3.2 — Of de klant kan overstappen of exporteren binnen 30 dagen
- Grondslag: art. 25 lid 1 en lid 2 sub a Data Act
- Toetspunt: De overeenkomst stelt de klant in staat over te stappen naar een andere aanbieder of naar eigen infrastructuur, of alle exporteerbare gegevens en digitale activa te exporteren, zonder onnodige vertraging en uiterlijk na de verplichte maximale overgangsperiode van 30 kalenderdagen, met redelijke bijstand, bedrijfscontinuïteit en beveiliging tijdens het overstappen
- Alleen als: `facts.data_processing_service != false and facts.test_version != true`
- Bronnen: DA-art25-lid1 (Data Act (Vo. (EU) 2023/2854) art. 25 lid 1); DA-art25-lid2-a (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub a); DA-art25-lid4 (Data Act (Vo. (EU) 2023/2854) art. 25 lid 4)
- Wat de tekst moet bereiken: Neem op dat de klant binnen ten hoogste 30 kalenderdagen kan overstappen of alles kan exporteren, met bijstand van de aanbieder.

### C3.3 — Of de overeenkomst eindigt na het overstappen
- Grondslag: art. 25 lid 2 sub b Data Act
- Toetspunt: De overeenkomst bepaalt dat zij wordt beëindigd na afronding van het overstappen of, als de klant alleen wil wissen, aan het einde van de opzegtermijn
- Alleen als: `facts.data_processing_service != false and facts.test_version != true`
- Bronnen: DA-art25-lid2-b (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub b)
- Wat de tekst moet bereiken: Leg vast dat de overeenkomst eindigt zodra het overstappen is afgerond.

### C3.4 — Of de opzegtermijn voor overstappen ten hoogste twee maanden is
- Grondslag: art. 25 lid 2 sub c Data Act
- Toetspunt: De overeenkomst noemt een maximale opzegtermijn voor het starten van het overstappen die niet langer is dan twee maanden
- Alleen als: `facts.data_processing_service != false and facts.test_version != true`
- Bronnen: DA-art25-lid2-c (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub c)
- Wat de tekst moet bereiken: Leg een opzegtermijn voor overstappen vast van ten hoogste twee maanden.

### C3.5 — Of vastligt welke gegevens en digitale activa mee kunnen
- Grondslag: art. 25 lid 2 sub d en e Data Act
- Toetspunt: De overeenkomst specificeert uitputtend alle categorieën gegevens en digitale activa die kunnen worden overgezet, ten minste alle exporteerbare gegevens; uitzonderingen voor bedrijfsgeheimen alleen als die de overstap niet belemmeren
- Alleen als: `facts.data_processing_service != false and facts.test_version != true`
- Bronnen: DA-art25-lid2-d (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub d); DA-art25-lid2-e (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub e)
- Wat de tekst moet bereiken: Specificeer welke gegevens en digitale activa de klant bij overstappen kan meenemen.

### C3.6 — Of de klant ten minste 30 dagen heeft om gegevens op te halen
- Grondslag: art. 25 lid 2 sub f Data Act
- Toetspunt: De overeenkomst noemt een ophaalperiode van ten minste 30 kalenderdagen, die begint na de overgangsperiode
- Alleen als: `facts.data_processing_service != false and facts.test_version != true`
- Bronnen: DA-art25-lid2-f (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub f)
- Wat de tekst moet bereiken: Geef de klant na de overgangsperiode ten minste 30 kalenderdagen om zijn gegevens op te halen.

### C3.7 — Of de gegevens daarna volledig worden gewist
- Grondslag: art. 25 lid 2 sub g Data Act
- Toetspunt: De overeenkomst garandeert de volledige wissing van alle exporteerbare gegevens en digitale activa na afloop van de ophaalperiode of eerdere succesvolle overstap
- Alleen als: `facts.data_processing_service != false and facts.test_version != true`
- Bronnen: DA-art25-lid2-g (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub g)
- Wat de tekst moet bereiken: Garandeer dat de gegevens na de ophaalperiode volledig worden gewist.

### C3.8 — Of de kosten van overstappen kloppen met de Data Act
- Grondslag: art. 25 lid 2 sub h en art. 29 Data Act
- Toetspunt: Overstapkosten zijn in de overeenkomst geregeld volgens art. 29: vanaf 12 januari 2027 mag de aanbieder geen overstapkosten meer rekenen; tot die datum ten hoogste de kosten die rechtstreeks met het overstappen verband houden
- Alleen als: `facts.data_processing_service != false and facts.test_version != true`
- Bronnen: DA-art25-lid2-h (Data Act (Vo. (EU) 2023/2854) art. 25 lid 2 sub h); DA-art29-lid1 (Data Act (Vo. (EU) 2023/2854) art. 29 lid 1); DA-art29-lid2 (Data Act (Vo. (EU) 2023/2854) art. 29 lid 2)
- Wat de tekst moet bereiken: Reken na 12 januari 2027 geen overstapkosten meer, en tot die datum alleen de kosten die rechtstreeks met het overstappen te maken hebben.

### C3.9 — Of er een verwerkersovereenkomst is
- Grondslag: art. 28 lid 3 AVG
- Toetspunt: Verwerkt de aanbieder persoonsgegevens voor de klant, dan bevat of verwijst de overeenkomst naar een verwerkersovereenkomst volgens art. 28 lid 3 AVG
- Alleen als: `facts.personal_data != false`
- Bronnen: AVG-art28-lid3 (AVG art. 28 lid 3)
- Wat de tekst moet bereiken: Sluit een verwerkersovereenkomst of verwijs ernaar.

### C3.10 — Of beschikbaarheid en ondersteuning zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De overeenkomst of een SLA regelt beschikbaarheid en ondersteuning
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Regel beschikbaarheid en ondersteuning, of verwijs naar een SLA.

### C3.11 — Of looptijd en opzegging zijn geregeld
- Grondslag: goede praktijk
- Toetspunt: De overeenkomst regelt looptijd, verlenging en opzegging
- Bronnen: BW6-art248 (Burgerlijk Wetboek Boek 6 art. 6:248)
- Wat de tekst moet bereiken: Leg looptijd, verlenging en opzegging vast.

### C3.12 — Of aansprakelijkheid is geregeld
- Grondslag: goede praktijk; art. 6:233 onder a BW als achtergrond
- Toetspunt: De overeenkomst regelt de aansprakelijkheid van de aanbieder
- Bronnen: BW6-art233-a (Burgerlijk Wetboek Boek 6 art. 6:233 onder a)
- Wat de tekst moet bereiken: Leg de aansprakelijkheid vast, zonder opzet en bewuste roekeloosheid uit te sluiten.
