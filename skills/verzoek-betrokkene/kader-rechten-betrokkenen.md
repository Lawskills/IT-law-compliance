# Kader K6 — Rechten van betrokkenen

Versie 1.2 · peildatum 2026-11-10

Doel: Controleren of de organisatie verzoeken van mensen over hun eigen gegevens (inzage, correctie, verwijdering, bezwaar en de overige rechten) correct en op tijd kan afhandelen (art. 12 en 15 t/m 22 AVG).

Bronnen: AVG-art12 (AVG art. 12); AVG-art15 (AVG art. 15); AVG-art16 (AVG art. 16); AVG-art17 (AVG art. 17); AVG-art18 (AVG art. 18); AVG-art19 (AVG art. 19); AVG-art20 (AVG art. 20); AVG-art21 (AVG art. 21); AVG-art22 (AVG art. 22); AVG-art23 (AVG art. 23); UAVG-art5-lid4 (UAVG art. 5 lid 4); UAVG-art41 (UAVG art. 41); EDPB-RL-01-2022 (EDPB, Richtsnoeren 01/2022 over de rechten van betrokkenen — recht op inzage); HvJEU-C-154-21 (HvJEU 12 januari 2023, C-154/21, Österreichische Post); HvJEU-C-487-21 (HvJEU 4 mei 2023, C-487/21, FF/Österreichische Datenschutzbehörde); HvJEU-C-307-22 (HvJEU 26 oktober 2023, C-307/22, FT/DW); AP-boete-BKR-2019 (Autoriteit Persoonsgegevens, boetebesluit BKR (geld vragen voor inzage))

## Formulier (vragen aan de gebruiker)

- **has_request_process**: Heb je een vaste werkwijze voor verzoeken van mensen die hun gegevens willen inzien, laten corrigeren of laten verwijderen?
  - Label (voor de plek-om-in-te-vullen): of je een vaste werkwijze hebt voor verzoeken over persoonsgegevens
  - Hulp: Bijvoorbeeld een korte beschrijving wie het verzoek oppakt, hoe je het registreert en wie het antwoord controleert.
  - Type: boolean
- **has_request_contact**: Is er een vast aanspreekpunt voor zulke verzoeken (een persoon of een e-mailadres), en kunnen mensen dat vinden?
  - Label (voor de plek-om-in-te-vullen): of er een vindbaar aanspreekpunt is voor zulke verzoeken
  - Hulp: Bijvoorbeeld een privacy-e-mailadres dat in je privacyverklaring staat.
  - Type: boolean
- **requests_made_easy**: Kunnen mensen een verzoek op een eenvoudige manier bij jou indienen?
  - Label (voor de plek-om-in-te-vullen): of mensen een verzoek eenvoudig kunnen indienen
  - Hulp: Bijvoorbeeld per e-mail, via hun account of via het kanaal waarlangs ze normaal contact met jou hebben. Moeten mensen eerst veel drempels over, zoals een ingewikkeld formulier of een brief per aangetekende post, kies dan nee.
  - Type: boolean
- **response_time**: Hoe snel reageer je op zulke verzoeken?
  - Label (voor de plek-om-in-te-vullen): binnen welke termijn je op verzoeken reageert
  - Type: enum (within_one_month / extended_with_notice / late_or_no_notice)
- **extension_only_complex**: Neem je alleen meer tijd als een verzoek ingewikkeld is of als je veel verzoeken tegelijk krijgt?
  - Label (voor de plek-om-in-te-vullen): of je alleen verlengt bij ingewikkelde of veel verzoeken
  - Hulp: Drukte om andere redenen, vakantie of personeelstekort zijn geen reden om meer tijd te nemen.
  - Type: boolean · Alleen vragen als: `facts.response_time == "extended_with_notice"`
- **request_fees**: Vraag je geld voor het afhandelen van een verzoek?
  - Label (voor de plek-om-in-te-vullen): of je geld vraagt voor een verzoek
  - Type: enum (never / exceptional_only / standard_fee)
- **refuses_based_on_motive**: Weiger je weleens een verzoek, of vraag je er geld voor, omdat je denkt dat iemand het verzoek om een andere reden doet, bijvoorbeeld voor een conflict of een rechtszaak?
  - Label (voor de plek-om-in-te-vullen): of je een verzoek weigert of geld vraagt vanwege de reden van het verzoek
  - Type: boolean
- **id_check**: Hoe controleer je of het verzoek echt van de persoon zelf komt?
  - Label (voor de plek-om-in-te-vullen): hoe je controleert wie het verzoek doet
  - Type: enum (only_when_doubt / always_id_copy / other)
- **id_check_description**: Beschrijf kort hoe je controleert wie het verzoek doet.
  - Label (voor de plek-om-in-te-vullen): hoe je de identiteit controleert
  - Type: text · Alleen vragen als: `facts.id_check == "other"`
- **access_provides_copy**: Krijgt iemand die om inzage vraagt een kopie van alle gegevens die je over hem hebt?
  - Label (voor de plek-om-in-te-vullen): of mensen bij inzage een kopie van hun gegevens krijgen
  - Type: boolean
- **access_provides_details**: Vertel je bij inzage ook waarvoor je de gegevens gebruikt, welke soorten gegevens het zijn, aan wie je ze geeft, hoe lang je ze bewaart, waar ze vandaan komen en welke rechten de persoon heeft?
  - Label (voor de plek-om-in-te-vullen): of je bij inzage ook de toelichting geeft die de wet voorschrijft
  - Hulp: Ook: dat iemand een klacht kan indienen bij de Autoriteit Persoonsgegevens, of er geautomatiseerde besluiten worden genomen, en welke waarborgen er zijn als gegevens buiten de Europese Unie terechtkomen.
  - Type: boolean
- **access_names_recipients**: Noem je bij inzage de namen van de organisaties die de gegevens hebben gekregen, en niet alleen het soort organisaties?
  - Label (voor de plek-om-in-te-vullen): of je bij inzage de concrete ontvangers noemt
  - Hulp: Bijvoorbeeld 'PostNL' en 'Boekhoudkantoor De Vries' in plaats van 'bezorgers' en 'onze accountant'. Geef je gegevens aan niemand door, kies dan ja.
  - Type: boolean
- **access_redacts_others**: Maak je gegevens over andere mensen onleesbaar voordat je een kopie verstrekt?
  - Label (voor de plek-om-in-te-vullen): of je gegevens over anderen afschermt in een kopie
  - Hulp: Bijvoorbeeld namen van collega's of andere klanten in e-mails.
  - Type: boolean
- **erasure_knowledge**: Weet je wanneer je gegevens op verzoek moet verwijderen, en wanneer je ze mag houden, bijvoorbeeld omdat een wet je verplicht ze te bewaren?
  - Label (voor de plek-om-in-te-vullen): of je weet wanneer je gegevens op verzoek moet verwijderen
  - Type: boolean
- **erasure_practice**: Wat doe je als iemand vraagt zijn gegevens te verwijderen? Beschrijf het kort.
  - Label (voor de plek-om-in-te-vullen): wat je doet met een verzoek om verwijdering
  - Hulp: Bijvoorbeeld: 'Wij verwijderen alles behalve de facturen, die wij 7 jaar moeten bewaren, en laten de persoon dat weten.'
  - Type: text
- **direct_marketing**: Stuur je mensen reclame of aanbiedingen, bijvoorbeeld per e-mail, post of telefoon?
  - Label (voor de plek-om-in-te-vullen): of je aan direct marketing doet
  - Type: boolean
- **dm_objection_always_honoured**: Als iemand zegt geen reclame meer te willen ontvangen, stop je daar dan altijd mee, zonder eerst te beoordelen of je toch mag doorgaan?
  - Label (voor de plek-om-in-te-vullen): of je altijd stopt met reclame als iemand dat vraagt
  - Type: boolean · Alleen vragen als: `facts.direct_marketing == true`
- **other_rights_handled**: Kun je ook verzoeken afhandelen om gegevens te corrigeren, het gebruik tijdelijk te beperken of gegevens mee te geven in een bestand?
  - Label (voor de plek-om-in-te-vullen): of je ook de overige verzoeken kunt afhandelen
  - Type: boolean
- **informs_recipients_after_changes**: Als je gegevens corrigeert, verwijdert of het gebruik beperkt, laat je dat dan weten aan de organisaties aan wie je die gegevens eerder hebt gegeven?
  - Label (voor de plek-om-in-te-vullen): of je ontvangers inlicht na correctie, verwijdering of beperking
  - Hulp: Geef je gegevens aan niemand door, kies dan ja.
  - Type: boolean
- **automated_decision_making**: Neemt software of AI zelfstandig besluiten over mensen die voor hen belangrijke gevolgen hebben, zonder dat een medewerker het besluit inhoudelijk beoordeelt?
  - Label (voor de plek-om-in-te-vullen): of een computer zelfstandig belangrijke besluiten over mensen neemt
  - Hulp: Bijvoorbeeld een automatische afwijzing van een sollicitatie, een kredietaanvraag of een klant. Een aanbeveling die een medewerker echt beoordeelt, telt niet.
  - Type: boolean
- **refusal_informs**: Als je een verzoek weigert of er niets mee doet, laat je de persoon dan binnen een maand weten waarom, en dat hij een klacht kan indienen bij de Autoriteit Persoonsgegevens of naar de rechter kan stappen?
  - Label (voor de plek-om-in-te-vullen): of je bij een weigering de reden en de klachtmogelijkheid meldt
  - Type: boolean
- **data_subjects_minors**: Heb je gegevens van kinderen jonger dan 16, of van mensen die onder curatele staan?
  - Label (voor de plek-om-in-te-vullen): of je gegevens hebt van kinderen of van mensen onder curatele
  - Hulp: Bijvoorbeeld leerlingen, jonge sporters of cliënten met een curator of mentor.
  - Type: boolean
- **minors_representation_known**: Weet je wie een verzoek mag doen voor een kind of voor iemand onder curatele, en controleer je dat?
  - Label (voor de plek-om-in-te-vullen): of je weet wie namens een kind of iemand onder curatele een verzoek mag doen
  - Hulp: Voor kinderen onder de 12 is dat de ouder of voogd. Van 12 tot 16 kunnen zowel het kind als de ouder of voogd een verzoek doen. Bij curatele is dat de wettelijk vertegenwoordiger.
  - Type: boolean · Alleen vragen als: `facts.data_subjects_minors == true`
- **relies_on_restriction**: Weiger of beperk je verzoeken omdat een wet dat volgens jou toestaat, bijvoorbeeld om fraude te bestrijden of de rechten van anderen te beschermen?
  - Label (voor de plek-om-in-te-vullen): of je je beroept op een wettelijke uitzondering om een recht te beperken
  - Hulp: Dit gaat niet over verzoeken die duidelijk ongegrond of buitensporig zijn, maar over een wettelijke uitzondering die je inroept.
  - Type: boolean
- **restriction_description**: Welke uitzondering roep je in, bij welke verzoeken, en waarom?
  - Label (voor de plek-om-in-te-vullen): welke uitzondering je inroept en waarom
  - Type: text · Alleen vragen als: `facts.relies_on_restriction == true`

## Toetspunten (voor de eindcontrole)

### K6.1 — Er is een vaste werkwijze en een aanspreekpunt voor verzoeken
- Grondslag: art. 12 lid 2 AVG
- Toetspunt: Vast proces en aanspreekpunt voor verzoeken; het uitoefenen van rechten wordt vergemakkelijkt
- Bronnen: AVG-art12-lid2 (AVG art. 12 lid 2); EDPB-RL-01-2022 (EDPB, Richtsnoeren 01/2022 over de rechten van betrokkenen — recht op inzage)
- Wat de tekst moet bereiken: Leg vast wie verzoeken oppakt en hoe, en zorg voor een vindbaar aanspreekpunt, bijvoorbeeld een privacy-e-mailadres in je privacyverklaring. Maak het indienen van een verzoek zo eenvoudig mogelijk.

### K6.2 — Je reageert op tijd op verzoeken
- Grondslag: art. 12 lid 3 AVG
- Toetspunt: Reactie zonder onredelijke vertraging en uiterlijk binnen één maand; verlenging met twee maanden alleen gezien de complexiteit en het aantal verzoeken, met melding en reden binnen de eerste maand
- Bronnen: AVG-art12-lid3 (AVG art. 12 lid 3); EDPB-RL-01-2022 (EDPB, Richtsnoeren 01/2022 over de rechten van betrokkenen — recht op inzage)
- Wat de tekst moet bereiken: Reageer op elk verzoek binnen een maand. Heb je bij een ingewikkeld verzoek of veel verzoeken meer tijd nodig, meld dat dan binnen die maand met de reden; je krijgt hooguit twee maanden extra.

### K6.3 — Je vraagt geen geld voor verzoeken
- Grondslag: art. 12 lid 5 en art. 15 lid 3 AVG
- Toetspunt: Kosteloos; geld vragen of weigeren alleen bij kennelijk ongegronde of buitensporige verzoeken; redelijke vergoeding alleen voor extra kopieën; het motief van het verzoek doet niet ter zake
- Bronnen: AVG-art12-lid5 (AVG art. 12 lid 5); AVG-art15-lid3 (AVG art. 15 lid 3); HvJEU-C-307-22 (HvJEU 26 oktober 2023, C-307/22, FT/DW); AP-boete-BKR-2019 (Autoriteit Persoonsgegevens, boetebesluit BKR (geld vragen voor inzage))
- Wat de tekst moet bereiken: Handel verzoeken kosteloos af. Vraag alleen een redelijke vergoeding voor extra kopieën, of bij verzoeken die kennelijk ongegrond of buitensporig zijn. Waarom iemand zijn gegevens wil zien, maakt niet uit.

### K6.4 — Je controleert de identiteit niet strenger dan nodig
- Grondslag: art. 12 lid 6 AVG
- Toetspunt: Identiteitscontrole proportioneel; aanvullende gegevens alleen bij redelijke twijfel over de identiteit
- Bronnen: AVG-art12-lid6 (AVG art. 12 lid 6); EDPB-RL-01-2022 (EDPB, Richtsnoeren 01/2022 over de rechten van betrokkenen — recht op inzage)
- Wat de tekst moet bereiken: Vraag alleen om extra gegevens als je redelijke twijfel hebt over wie het verzoek doet. Eis niet standaard een kopie van een identiteitsbewijs.

### K6.5 — Bij inzage krijgt iemand een kopie en alle informatie waar hij recht op heeft
- Grondslag: art. 15 lid 1, 3 en 4 AVG
- Toetspunt: Kopie en alle informatie van art. 15 lid 1, inclusief de concrete ontvangers (C-154/21), met afscherming van gegevens van anderen (art. 15 lid 4)
- Bronnen: AVG-art15-lid1 (AVG art. 15 lid 1); AVG-art15-lid3 (AVG art. 15 lid 3); AVG-art15-lid4 (AVG art. 15 lid 4); HvJEU-C-154-21 (HvJEU 12 januari 2023, C-154/21, Österreichische Post); HvJEU-C-487-21 (HvJEU 4 mei 2023, C-487/21, FF/Österreichische Datenschutzbehörde); EDPB-RL-01-2022 (EDPB, Richtsnoeren 01/2022 over de rechten van betrokkenen — recht op inzage)
- Wat de tekst moet bereiken: Geef bij inzage een getrouwe kopie van alle gegevens, met de informatie uit art. 15 lid 1 AVG en de namen van de ontvangers. Scherm gegevens over andere mensen af.

### K6.6 — Je weet wanneer je gegevens op verzoek moet verwijderen
- Grondslag: art. 17 lid 1 en 3 AVG
- Toetspunt: Bekend wanneer wissen verplicht is en wanneer een uitzondering geldt
- Bronnen: AVG-art17-lid1 (AVG art. 17 lid 1); AVG-art17-lid3 (AVG art. 17 lid 3)
- Wat de tekst moet bereiken: Leg vast wanneer je gegevens op verzoek verwijdert en welke gegevens je moet bewaren (bijvoorbeeld vanwege de fiscale bewaarplicht), en laat de persoon weten wat je hebt verwijderd en wat niet.

### K6.7 — Je stopt altijd met reclame als iemand dat vraagt
- Grondslag: art. 21 lid 2 en 3 AVG
- Toetspunt: Bezwaar tegen direct marketing wordt altijd en zonder afweging gehonoreerd
- Alleen als: `facts.direct_marketing == true`
- Bronnen: AVG-art21-lid2 (AVG art. 21 lid 2); AVG-art21-lid3 (AVG art. 21 lid 3)
- Wat de tekst moet bereiken: Stop altijd en direct met reclame als iemand daartegen bezwaar maakt. Een afweging is bij direct marketing niet toegestaan.

### K6.8 — Je kunt ook de overige verzoeken afhandelen
- Grondslag: art. 16, 18, 19, 20 en 22 AVG
- Toetspunt: Rectificatie, beperking, overdraagbaarheid en art. 22 waar van toepassing; ontvangers informeren over rectificatie, wissing of beperking (art. 19)
- Bronnen: AVG-art16 (AVG art. 16); AVG-art18 (AVG art. 18); AVG-art19 (AVG art. 19); AVG-art20 (AVG art. 20); AVG-art22-lid3 (AVG art. 22 lid 3)
- Wat de tekst moet bereiken: Zorg dat je ook verzoeken om correctie, beperking en overdracht kunt afhandelen, en laat organisaties aan wie je gegevens gaf weten als je die gegevens corrigeert, verwijdert of beperkt.

### K6.9 — Bij een weigering hoort de persoon waarom, en waar hij terechtkan
- Grondslag: art. 12 lid 4 AVG
- Toetspunt: Bij weigering of geen gevolg: binnen een maand informeren over de reden en de mogelijkheid van klacht en beroep
- Bronnen: AVG-art12-lid4 (AVG art. 12 lid 4)
- Wat de tekst moet bereiken: Geef je geen gevolg aan een verzoek, laat dan binnen een maand weten waarom, en dat de persoon een klacht kan indienen bij de Autoriteit Persoonsgegevens of naar de rechter kan stappen.

### K6.10 — Je weet wie namens een kind of iemand onder curatele een verzoek mag doen
- Grondslag: art. 5 lid 4 UAVG
- Toetspunt: Minderjarigen en curatele: onder 12 oefent de wettelijk vertegenwoordiger de rechten uit; van 12 tot 16 kunnen beiden dat
- Alleen als: `facts.data_subjects_minors == true`
- Bronnen: UAVG-art5-lid4 (UAVG art. 5 lid 4)
- Wat de tekst moet bereiken: Leg vast wie een verzoek mag doen voor een kind of voor iemand onder curatele: onder de 12 de wettelijk vertegenwoordiger, van 12 tot 16 zowel het kind als de wettelijk vertegenwoordiger.

### K6.11 — Of je terecht een wettelijke uitzondering inroept
- Grondslag: art. 23 AVG en art. 41 UAVG
- Toetspunt: Beroep op een beperking van de rechten (art. 23 AVG jo. art. 41 UAVG)
- Alleen als: `facts.relies_on_restriction == true`
- Bronnen: AVG-art23 (AVG art. 23); UAVG-art41 (UAVG art. 41)
- Wat de tekst moet bereiken: Leg per verzoek vast welke uitzondering je inroept, waarom die geldt, en waarom de beperking noodzakelijk en evenredig is. Laat dit beoordelen door een juridisch adviseur.
