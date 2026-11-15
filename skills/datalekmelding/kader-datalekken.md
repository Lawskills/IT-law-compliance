# Kader K12 — Datalekken

Versie 1.2 · peildatum 2026-11-10

Doel: Twee toepassingen: (1) controleren of de organisatie een datalekproces heeft (procedure, registratie van alle lekken, verwerkers die lekken melden); (2) acute hulp bij een incident: is het een datalek, moet het binnen 72 uur bij de Autoriteit Persoonsgegevens worden gemeld, moeten betrokkenen worden geïnformeerd, en is de melding volledig.

Bronnen: AVG-art4-12 (AVG art. 4 punt 12); AVG-art33 (AVG art. 33); AVG-art34 (AVG art. 34); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG); EDPB-RL-01-2021 (EDPB, Richtsnoeren 01/2021 met voorbeelden betreffende de melding van inbreuken in verband met persoonsgegevens); AP-boete-Booking-2021 (Autoriteit Persoonsgegevens, boete aan Booking.com voor te laat melden van een datalek); AP-datalekken-2025 (Autoriteit Persoonsgegevens, rapportage datalekken 2025 (44.374 meldingen; bijna driekwart verkeerd bezorgde brieven of e-mails)); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))

## Formulier (vragen aan de gebruiker)

- **mode**: Wil je je datalekproces controleren, of heb je nu een incident?
  - Label (voor de plek-om-in-te-vullen): waarvoor je deze toets gebruikt
  - Type: enum (process_check / incident)
- **has_breach_procedure**: Heb je een procedure voor datalekken: wie wat doet, wie beslist over melden, en hoe je de meldtermijn van 72 uur haalt?
  - Label (voor de plek-om-in-te-vullen): of je een datalekprocedure hebt
  - Type: boolean · Alleen vragen als: `facts.mode == "process_check"`
- **documents_all_breaches**: Leg je alle datalekken vast, ook de lekken die je niet meldt, met wat er gebeurde, de gevolgen en de maatregelen die je nam?
  - Label (voor de plek-om-in-te-vullen): of je alle datalekken vastlegt
  - Hulp: Bijvoorbeeld in een datalekregister. De vorm mag je zelf kiezen.
  - Type: boolean · Alleen vragen als: `facts.mode == "process_check"`
- **uses_processors**: Heb je dienstverleners die persoonsgegevens voor jou verwerken, zoals hosting, software in de cloud of een salarisadministrateur?
  - Label (voor de plek-om-in-te-vullen): of je dienstverleners hebt die gegevens voor jou verwerken
  - Type: boolean · Alleen vragen als: `facts.mode == "process_check"`
- **processors_know_breach_duty**: Weten die dienstverleners dat zij een datalek zonder onnodige vertraging aan jou moeten melden?
  - Label (voor de plek-om-in-te-vullen): of je dienstverleners weten dat ze lekken direct aan jou moeten melden
  - Hulp: Meestal staat dit in de verwerkersovereenkomst.
  - Type: boolean · Alleen vragen als: `facts.mode == "process_check" and facts.uses_processors == true`
- **incident_scenario**: Welke omschrijving past het best bij het incident?
  - Label (voor de plek-om-in-te-vullen): wat voor incident het is
  - Type: enum (email_wrong_recipient / email_no_bcc / letter_misdelivered / device_lost_stolen / phishing_hacked_account / ransomware / other) · Alleen vragen als: `facts.mode == "incident"`
- **incident_description**: Wat is er gebeurd? Beschrijf het kort.
  - Label (voor de plek-om-in-te-vullen): wat er is gebeurd
  - Type: text · Alleen vragen als: `facts.mode == "incident"`
- **personal_data_involved**: Zijn er gegevens over personen bij betrokken, zoals namen, adressen, e-mailadressen, klant- of personeelsgegevens?
  - Label (voor de plek-om-in-te-vullen): of er persoonsgegevens bij betrokken zijn
  - Type: boolean · Alleen vragen als: `facts.mode == "incident"`
- **data_affected**: Om welke gegevens gaat het?
  - Label (voor de plek-om-in-te-vullen): welke gegevens het betreft
  - Type: text · Alleen vragen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- **special_categories_or_bsn**: Zitten er gevoelige gegevens bij, zoals gezondheidsgegevens, strafrechtelijke gegevens of burgerservicenummers (BSN)?
  - Label (voor de plek-om-in-te-vullen): of er gevoelige gegevens of BSN's bij zitten
  - Type: boolean · Alleen vragen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- **affected_persons_count**: Om hoeveel mensen gaat het ongeveer?
  - Label (voor de plek-om-in-te-vullen): hoeveel mensen het betreft
  - Type: number · Alleen vragen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- **hours_since_awareness**: Hoeveel uur geleden heb je ontdekt dat er iets mis was?
  - Label (voor de plek-om-in-te-vullen): hoeveel uur geleden je het lek ontdekte
  - Hulp: De termijn van 72 uur voor een melding bij de Autoriteit Persoonsgegevens begint op het moment dat je van het lek weet.
  - Type: number · Alleen vragen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- **ap_notification_status**: Heb je het lek gemeld bij de Autoriteit Persoonsgegevens?
  - Label (voor de plek-om-in-te-vullen): of je het lek bij de Autoriteit Persoonsgegevens hebt gemeld
  - Type: enum (notified / not_yet / decided_not_to_notify) · Alleen vragen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- **notified_hours_after_awareness**: Hoeveel uur nadat je het lek ontdekte, heb je het gemeld?
  - Label (voor de plek-om-in-te-vullen): hoeveel uur na ontdekking je meldde
  - Type: number · Alleen vragen als: `facts.mode == "incident" and facts.ap_notification_status == "notified"`
- **delay_reason**: Als je later dan 72 uur meldde: wat was de reden, en heb je die bij de melding vermeld?
  - Label (voor de plek-om-in-te-vullen): de reden voor een melding na 72 uur
  - Type: text · Alleen vragen als: `facts.mode == "incident" and facts.ap_notification_status == "notified"`
- **notification_complete**: Stond in je melding: wat er gebeurde, welke soorten en hoeveel mensen en gegevens het betrof, een contactpersoon, de waarschijnlijke gevolgen en de maatregelen die je nam of voorstelt?
  - Label (voor de plek-om-in-te-vullen): of de melding alle verplichte informatie bevatte
  - Type: boolean · Alleen vragen als: `facts.mode == "incident" and facts.ap_notification_status == "notified"`
- **supplementing_later**: Vul je informatie die je nog niet had, zo snel mogelijk aan bij de Autoriteit Persoonsgegevens?
  - Label (voor de plek-om-in-te-vullen): of je ontbrekende informatie later aanvult
  - Type: boolean · Alleen vragen als: `facts.mode == "incident" and facts.ap_notification_status == "notified" and facts.notification_complete == false`
- **breach_documented**: Heb je het lek vastgelegd, met wat er gebeurde, de gevolgen en de maatregelen die je nam?
  - Label (voor de plek-om-in-te-vullen): of je het lek hebt vastgelegd
  - Type: boolean · Alleen vragen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- **subjects_informed**: Heb je de mensen van wie gegevens zijn gelekt, geïnformeerd?
  - Label (voor de plek-om-in-te-vullen): of je de betrokken mensen hebt geïnformeerd
  - Type: enum (yes_informed / not_yet / decided_not_to_inform) · Alleen vragen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- **art34_exception**: Als je de betrokkenen niet informeert: welke reden past?
  - Label (voor de plek-om-in-te-vullen): waarom je de betrokkenen niet informeert
  - Type: enum (none / data_unintelligible / high_risk_removed / disproportionate_public_notice) · Alleen vragen als: `facts.mode == "incident" and facts.personal_data_involved != false and facts.subjects_informed != "yes_informed"`
- **recipient_known_trusted**: Is de verkeerde ontvanger bekend en betrouwbaar (bijvoorbeeld een vaste zakenrelatie)?
  - Label (voor de plek-om-in-te-vullen): of de verkeerde ontvanger bekend en betrouwbaar is
  - Type: boolean · Alleen vragen als: `facts.incident_scenario == "email_wrong_recipient"`
- **recipient_confirmed_deletion**: Heeft de ontvanger bevestigd dat de e-mail is verwijderd?
  - Label (voor de plek-om-in-te-vullen): of de ontvanger heeft bevestigd dat de e-mail is verwijderd
  - Type: boolean · Alleen vragen als: `facts.incident_scenario == "email_wrong_recipient"`
- **visible_address_count**: Hoeveel e-mailadressen waren zichtbaar?
  - Label (voor de plek-om-in-te-vullen): hoeveel e-mailadressen zichtbaar waren
  - Type: number · Alleen vragen als: `facts.incident_scenario == "email_no_bcc"`
- **address_list_sensitive**: Zeggen de adressen of het feit dat iemand op de lijst staat iets gevoeligs, bijvoorbeeld dat iemand patiënt is of lid van een bepaalde groep?
  - Label (voor de plek-om-in-te-vullen): of de adressen of de lijst iets gevoeligs zeggen
  - Type: boolean · Alleen vragen als: `facts.incident_scenario == "email_no_bcc"`
- **mail_returned_or_destroyed**: Heb je de brief of het pakket teruggekregen, of is het vernietigd?
  - Label (voor de plek-om-in-te-vullen): of de brief of het pakket is teruggekregen of vernietigd
  - Type: boolean · Alleen vragen als: `facts.incident_scenario == "letter_misdelivered"`
- **device_encrypted**: Was het apparaat versleuteld?
  - Label (voor de plek-om-in-te-vullen): of het apparaat versleuteld was
  - Type: boolean · Alleen vragen als: `facts.incident_scenario == "device_lost_stolen"`
- **remote_wipe_possible**: Kan het apparaat op afstand worden gewist?
  - Label (voor de plek-om-in-te-vullen): of het apparaat op afstand kan worden gewist
  - Type: boolean · Alleen vragen als: `facts.incident_scenario == "device_lost_stolen"`
- **compromised_systems_and_duration**: Tot welke systemen en gegevens had de aanvaller toegang, en hoe lang?
  - Label (voor de plek-om-in-te-vullen): welke systemen en gegevens, en hoe lang er toegang was
  - Type: text · Alleen vragen als: `facts.incident_scenario == "phishing_hacked_account"`
- **password_reset_and_mfa**: Is het wachtwoord gewijzigd en is tweestapsverificatie (MFA) aangezet?
  - Label (voor de plek-om-in-te-vullen): of het wachtwoord is gewijzigd en tweestapsverificatie aan staat
  - Type: boolean · Alleen vragen als: `facts.incident_scenario == "phishing_hacked_account"`
- **ransomware_data_effect**: Zijn de gegevens versleuteld, gekopieerd, of allebei?
  - Label (voor de plek-om-in-te-vullen): wat er met de gegevens is gebeurd
  - Type: enum (encrypted_only / copied / both) · Alleen vragen als: `facts.incident_scenario == "ransomware"`
- **backup_available**: Is er een bruikbare back-up?
  - Label (voor de plek-om-in-te-vullen): of er een bruikbare back-up is
  - Type: boolean · Alleen vragen als: `facts.incident_scenario == "ransomware"`

## Toetspunten (voor de eindcontrole)

### K12.1 — Er is een datalekprocedure
- Grondslag: art. 33 en art. 34 AVG
- Toetspunt: Er is een datalekprocedure
- Alleen als: `facts.mode == "process_check"`
- Bronnen: AVG-art33 (AVG art. 33); AVG-art34 (AVG art. 34); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG)
- Wat de tekst moet bereiken: Leg vast wat medewerkers doen bij een datalek: bij wie ze het melden, wie beslist over een melding bij de Autoriteit Persoonsgegevens, en hoe je zorgt dat een melding zo mogelijk binnen 72 uur na ontdekking gebeurt.

### K12.2 — Je legt alle datalekken vast
- Grondslag: art. 33 lid 5 AVG
- Toetspunt: Alle datalekken worden gedocumenteerd, ook niet-gemelde, met feiten, gevolgen en genomen maatregelen; de vorm is vrij
- Alleen als: `facts.mode == "process_check"`
- Bronnen: AVG-art33-lid5 (AVG art. 33 lid 5); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG)
- Wat de tekst moet bereiken: Houd een datalekregister bij waarin je elk lek vastlegt, ook lekken die je niet meldt: wat er gebeurde, de gevolgen, de maatregelen en waarom je wel of niet binnen 72 uur meldde.

### K12.3 — Je dienstverleners melden lekken direct aan jou
- Grondslag: art. 33 lid 2 AVG
- Toetspunt: Verwerkers weten dat zij een inbreuk zonder onredelijke vertraging aan de verwerkingsverantwoordelijke moeten melden
- Alleen als: `facts.mode == "process_check" and facts.uses_processors != false`
- Bronnen: AVG-art33-lid2 (AVG art. 33 lid 2); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG)
- Wat de tekst moet bereiken: Spreek met elke dienstverlener af dat die een datalek zonder onnodige vertraging aan jou meldt, zodat je zelf binnen 72 uur kunt melden. Meestal hoort dit in de verwerkersovereenkomst.

### K12.4 — Of het incident een datalek is
- Grondslag: art. 4 lid 12 AVG
- Toetspunt: Inbreuk in verband met persoonsgegevens: een inbreuk op de beveiliging die leidt tot vernietiging, verlies, wijziging, ongeoorloofde verstrekking of toegang
- Alleen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- Bronnen: AVG-art4-12 (AVG art. 4 punt 12); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG); EDPB-RL-01-2021 (EDPB, Richtsnoeren 01/2021 met voorbeelden betreffende de melding van inbreuken in verband met persoonsgegevens); AP-datalekken-2025 (Autoriteit Persoonsgegevens, rapportage datalekken 2025 (44.374 meldingen; bijna driekwart verkeerd bezorgde brieven of e-mails))
- Wat de tekst moet bereiken: Behandel dit als een datalek. Leg het vast en beoordeel meteen of je het moet melden: een melding bij de Autoriteit Persoonsgegevens moet zo mogelijk binnen 72 uur nadat je het lek ontdekte.

### K12.5 — Of je het lek moet melden bij de Autoriteit Persoonsgegevens
- Grondslag: art. 33 lid 1 en lid 5 AVG
- Toetspunt: Is een risico voor betrokkenen onwaarschijnlijk? Ja → niet melden, wel documenteren. Nee → melden bij de AP
- Alleen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- Bronnen: AVG-art33-lid1 (AVG art. 33 lid 1); AVG-art33-lid5 (AVG art. 33 lid 5); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG); EDPB-RL-01-2021 (EDPB, Richtsnoeren 01/2021 met voorbeelden betreffende de melding van inbreuken in verband met persoonsgegevens); Cbw (Cyberbeveiligingswet (implementatie NIS2-richtlijn))
- Wat de tekst moet bereiken: Is een risico voor de betrokkenen niet onwaarschijnlijk, meld het lek dan bij de Autoriteit Persoonsgegevens, zo mogelijk binnen 72 uur nadat je het ontdekte. Twijfel je, meld dan. Meld je niet, leg dan vast waarom. Deze skill meldt nooit namens jou.

### K12.6 — Of je op tijd meldt
- Grondslag: art. 33 lid 1 en lid 4 AVG
- Toetspunt: Melding zonder onredelijke vertraging en zo mogelijk binnen 72 uur na kennisname; later → met opgave van redenen; informatie mag in fasen
- Alleen als: `facts.mode == "incident" and facts.personal_data_involved != false and facts.ap_notification_status != "decided_not_to_notify"`
- Bronnen: AVG-art33-lid1 (AVG art. 33 lid 1); AVG-art33-lid4 (AVG art. 33 lid 4); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG); AP-boete-Booking-2021 (Autoriteit Persoonsgegevens, boete aan Booking.com voor te laat melden van een datalek)
- Wat de tekst moet bereiken: Meld zonder onredelijke vertraging en zo mogelijk binnen 72 uur nadat je het lek ontdekte. Heb je nog niet alle informatie, meld dan toch en vul later aan. Meld je na 72 uur, geef dan de reden van de vertraging.

### K12.7 — Of je de betrokken mensen moet informeren
- Grondslag: art. 34 lid 1 en lid 3 AVG
- Toetspunt: Bij een hoog risico ook betrokkenen informeren, tenzij een uitzondering van art. 34 lid 3 geldt (versleuteling, risico weggenomen, onevenredige inspanning → openbare mededeling)
- Alleen als: `facts.mode == "incident" and facts.personal_data_involved != false`
- Bronnen: AVG-art34-lid1 (AVG art. 34 lid 1); AVG-art34-lid3 (AVG art. 34 lid 3); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG); EDPB-RL-01-2021 (EDPB, Richtsnoeren 01/2021 met voorbeelden betreffende de melding van inbreuken in verband met persoonsgegevens)
- Wat de tekst moet bereiken: Is er een hoog risico voor de mensen van wie gegevens zijn gelekt, informeer hen dan zonder onnodige vertraging, in duidelijke taal, met wat er gebeurde en wat zij zelf kunnen doen. Los daarvan geldt voor de melding bij de Autoriteit Persoonsgegevens de grens van 72 uur.

### K12.8 — Of je melding alle verplichte informatie bevat
- Grondslag: art. 33 lid 3 en lid 4 AVG
- Toetspunt: De melding bevat de gegevens van art. 33 lid 3: aard van de inbreuk, categorieën en aantallen, contactpunt, waarschijnlijke gevolgen, genomen of voorgestelde maatregelen
- Alleen als: `facts.mode == "incident" and facts.personal_data_involved != false and facts.ap_notification_status == "notified"`
- Bronnen: AVG-art33-lid3 (AVG art. 33 lid 3); AVG-art33-lid4 (AVG art. 33 lid 4); EDPB-RL-09-2022 (EDPB, Richtsnoeren 9/2022 inzake de melding van inbreuken in verband met persoonsgegevens krachtens de AVG)
- Wat de tekst moet bereiken: Vul de melding aan met wat er gebeurde, welke soorten en hoeveel mensen en gegevens het betreft, een contactpersoon, de waarschijnlijke gevolgen en de maatregelen die je nam. Informatie die je binnen 72 uur nog niet had, mag je later aanvullen.
