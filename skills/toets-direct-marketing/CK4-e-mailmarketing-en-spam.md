# Kader CK4 — E-mailmarketing en spam (art. 11.7 Tw)

Versie 0.4 · peildatum 2026-11-10

Doel: Controleren of de organisatie haar commerciële, ideële of charitatieve berichten per e-mail, sms, berichtendienst, fax of belcomputer mag versturen (toestemming, bestaande klanten, zakelijke ontvangers, donateurs), en of de berichten voldoen aan de eisen: herkenbare afzender, geldig afmeldadres, afmelden in elk bericht, afmeldingen direct verwerken.

Bronnen: TW-art11.7-lid1 (Telecommunicatiewet art. 11.7 lid 1); TW-art11.7-lid2 (Telecommunicatiewet art. 11.7 lid 2); TW-art11.7-lid3-a (Telecommunicatiewet art. 11.7 lid 3 sub a); TW-art11.7-lid3-b (Telecommunicatiewet art. 11.7 lid 3 sub b); TW-art11.7-lid4 (Telecommunicatiewet art. 11.7 lid 4); TW-art11.7-lid5 (Telecommunicatiewet art. 11.7 lid 5); TW-art11.7-lid7 (Telecommunicatiewet art. 11.7 lid 7); TW-art11.7-lid8 (Telecommunicatiewet art. 11.7 lid 8); TW-art11.1-g (Telecommunicatiewet art. 11.1 onder g); TW-art11.1-i (Telecommunicatiewet art. 11.1 onder i); EPR-art13-lid1 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 1); EPR-art13-lid2 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 2); EPR-art13-lid4 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 4); BW-art3-15e-lid1 (Burgerlijk Wetboek art. 3:15e lid 1 (commerciële communicatie als dienst van de informatiemaatschappij)); AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid1 (AVG art. 7 lid 1); AVG-art7-lid3 (AVG art. 7 lid 3); AVG-art7-lid4 (AVG art. 7 lid 4); AVG-art8-lid1 (AVG art. 8 lid 1); AVG-art21-lid2 (AVG art. 21 lid 2); AVG-art21-lid3 (AVG art. 21 lid 3); ACM-spam (Autoriteit Consument & Markt, 'Spam voorkomen in uw reclame'); HvJEU-C-102-20 (HvJEU 25 november 2021, C-102/20, StWL Städtische Werke Lauf a.d. Pegnitz (reclame in de e-mailinbox)); HvJEU-C-654-23 (HvJEU 13 november 2025, C-654/23, Inteligo Media (nieuwsbrief aan gebruikers van een gratis account; art. 13 lid 2)); EDPB-RL-02-2023 (EDPB, Richtsnoeren 2/2023 over de technische reikwijdte van artikel 5, lid 3, van de e-privacyrichtlijn); TW-art11.7a-lid1 (Telecommunicatiewet art. 11.7a lid 1); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3)

## Formulier (vragen aan de gebruiker)

- **sends_marketing_messages**: Stuur je reclame, nieuwsbrieven, aanbiedingen of andere wervende berichten per e-mail, sms, WhatsApp of een andere berichtendienst, per fax of via een belcomputer?
  - Label (voor de plek-om-in-te-vullen): of je wervende berichten per e-mail, sms of berichtendienst verstuurt
  - Hulp: Ook een nieuwsbrief met vooral nieuws telt mee als er aanbiedingen in staan of als hij lezers naar je producten of diensten leidt. Een orderbevestiging of factuur zonder reclame telt niet mee.
  - Type: boolean
- **transactional_with_promo**: Staat er in je orderbevestigingen, facturen, wachtwoordmails of andere dienstberichten ook reclame, een aanbieding of een oproep om iets te kopen of te geven?
  - Label (voor de plek-om-in-te-vullen): of er in dienstberichten ook reclame of aanbiedingen staan
  - Hulp: Ook een kortingscode of 'bekijk ook deze producten' onder een orderbevestiging telt als reclame.
  - Type: boolean · Alleen vragen als: `facts.sends_marketing_messages == false`
- **message_description**: Beschrijf kort welke berichten je verstuurt, via welk kanaal, aan wie en hoe vaak.
  - Label (voor de plek-om-in-te-vullen): wat je verstuurt, aan wie en hoe vaak
  - Hulp: Bijvoorbeeld: 'Maandelijkse nieuwsbrief per e-mail met aanbiedingen aan klanten en aanmelders via de website.'
  - Type: text
- **sender_purpose**: Met welk doel verstuur je de berichten?
  - Label (voor de plek-om-in-te-vullen): het soort organisatie en doel van de berichten
  - Type: enum (commercial / ideal_charitable) · Hoort bij je eigen organisatie (vul eenmalig in, hergebruik)
- **recipient_type**: Aan wie stuur je de berichten?
  - Label (voor de plek-om-in-te-vullen): wie de berichten ontvangen
  - Type: enum (consumers / business / both)
- **relies_on_consent**: Stuur je (een deel van) de berichten aan mensen die zich daar zelf voor hebben aangemeld of toestemming voor gaven?
  - Label (voor de plek-om-in-te-vullen): of je (een deel van) de berichten stuurt omdat ontvangers zich hebben aangemeld
  - Type: boolean
- **consent_method**: Hoe gaven die ontvangers toestemming?
  - Label (voor de plek-om-in-te-vullen): hoe ontvangers toestemming gaven
  - Type: enum (active_optin / prechecked / via_terms / condition_for_other / purchased_list) · Alleen vragen als: `facts.relies_on_consent != false`
- **consent_provable**: Kun je per ontvanger aantonen wanneer, hoe en met welke tekst hij toestemming gaf?
  - Label (voor de plek-om-in-te-vullen): of je per ontvanger kunt aantonen dat hij toestemming gaf
  - Hulp: Bijvoorbeeld met een registratie van de aanmelding (datum, tijd, formulier) of een bevestiging per e-mail (dubbele opt-in). De ACM vraagt je dit tot vijf jaar na verzending te kunnen bewijzen.
  - Type: boolean · Alleen vragen als: `facts.relies_on_consent != false`
- **relies_on_customer_exception**: Stuur je berichten aan bestaande klanten die zich niet apart hebben aangemeld, omdat ze eerder iets bij jou kochten of een dienst afnamen?
  - Label (voor de plek-om-in-te-vullen): of je berichten stuurt aan bestaande klanten zonder aparte aanmelding
  - Type: boolean
- **sale_context**: Kreeg je de e-mailadressen of telefoonnummers van deze klanten bij een aankoop of bij het afnemen van een dienst (ook een gratis account dat bij je verdienmodel hoort)?
  - Label (voor de plek-om-in-te-vullen): of je de adressen van klanten kreeg bij een aankoop of een afgenomen dienst
  - Type: boolean · Alleen vragen als: `facts.relies_on_customer_exception != false`
- **similar_own_products**: Waarover gaan de berichten aan bestaande klanten?
  - Label (voor de plek-om-in-te-vullen): waarover de berichten aan bestaande klanten gaan
  - Type: enum (same_or_similar / own_other / third_party) · Alleen vragen als: `facts.relies_on_customer_exception != false`
- **relies_on_business_exception**: Stuur je berichten aan bedrijven of zakelijke contactpersonen die zich niet hebben aangemeld?
  - Label (voor de plek-om-in-te-vullen): of je zakelijke ontvangers mailt zonder dat zij zich hebben aangemeld
  - Type: boolean
- **business_address_designated**: Welke adressen gebruik je voor die zakelijke ontvangers?
  - Label (voor de plek-om-in-te-vullen): welke zakelijke adressen je gebruikt
  - Type: enum (designated_for_offers / general_info_address / personal_employee_address_list / outside_eea) · Alleen vragen als: `facts.relies_on_business_exception != false`
- **relies_on_donor_exception**: Stuur je als ideële of charitatieve organisatie berichten aan mensen die aan jou hebben geschonken, zonder dat zij zich apart hebben aangemeld?
  - Label (voor de plek-om-in-te-vullen): of je als goed doel berichten stuurt aan donateurs zonder aparte aanmelding
  - Type: boolean
- **donor_context**: Kreeg je deze adressen bij een schenking aan je organisatie, en gebruik je ze alleen voor je eigen ideële of charitatieve doelen?
  - Label (voor de plek-om-in-te-vullen): of je de adressen van donateurs kreeg bij een schenking en ze alleen voor eigen doelen gebruikt
  - Type: boolean · Alleen vragen als: `facts.relies_on_donor_exception != false`
- **optout_at_collection**: Konden klanten of donateurs al op het moment dat je hun adres kreeg, makkelijk en gratis aangeven dat ze geen berichten willen (bijvoorbeeld met een vakje bij het bestellen)?
  - Label (voor de plek-om-in-te-vullen): of mensen zich al bij het verzamelen van hun adres konden afmelden
  - Type: boolean · Alleen vragen als: `facts.relies_on_customer_exception != false or facts.relies_on_donor_exception != false`
- **sender_identified**: Staat in elk bericht duidelijk de echte naam van je organisatie als afzender (geen fantasienaam)?
  - Label (voor de plek-om-in-te-vullen): of elk bericht duidelijk vermeldt van wie het komt
  - Type: boolean
- **valid_stop_address**: Staat in elk bericht een werkend adres (e-mailadres, postadres of nummer) waar de ontvanger kan vragen om geen berichten meer te krijgen?
  - Label (voor de plek-om-in-te-vullen): of elk bericht een geldig adres vermeldt om de berichten te laten stoppen
  - Type: boolean
- **recognisable_as_ad**: Is aan het bericht (bijvoorbeeld aan de onderwerpregel en de afzender) meteen te zien dat het om reclame of een nieuwsbrief gaat?
  - Label (voor de plek-om-in-te-vullen): of de berichten herkenbaar zijn als reclame
  - Type: boolean
- **unsubscribe_in_every_message**: Kan de ontvanger zich in elk bericht gratis en eenvoudig afmelden, bijvoorbeeld met één klik op een afmeldlink, zonder in te loggen of een vragenlijst in te vullen?
  - Label (voor de plek-om-in-te-vullen): of elk bericht een gratis en eenvoudige afmeldmogelijkheid heeft
  - Type: boolean
- **unsubscribes_processed**: Stop je direct met het sturen van berichten als iemand zich afmeldt of bezwaar maakt, ook in andere systemen en bij andere afdelingen?
  - Label (voor de plek-om-in-te-vullen): of afmeldingen en bezwaren direct worden verwerkt
  - Type: boolean
- **uses_tell_a_friend**: Kunnen mensen via je website of berichten een aanbieding doorsturen naar iemand anders ('stuur door aan een vriend')?
  - Label (voor de plek-om-in-te-vullen): of je 'stuur door aan een vriend' gebruikt
  - Type: boolean
- **uses_third_party_lists**: Krijg je adressen via andere partijen, bijvoorbeeld via acties of winspellen van anderen (co-registratie) of door adressen te kopen of te huren?
  - Label (voor de plek-om-in-te-vullen): of je adressen via andere partijen verkrijgt
  - Type: boolean
- **tell_a_friend_conditions**: Hoe werkt het doorsturen? Beloon je mensen ervoor, ziet de doorsturer het hele bericht vooraf, staat erin bij wie de ontvanger kan klagen, bewaar je het adres van de ontvanger, en is het formulier beveiligd tegen misbruik?
  - Label (voor de plek-om-in-te-vullen): hoe 'stuur door aan een vriend' is ingericht
  - Type: text · Alleen vragen als: `facts.uses_tell_a_friend != false`
- **calls_for_marketing**: Bel je (of een callcenter in je opdracht) mensen om producten, diensten of goede doelen aan te bieden?
  - Label (voor de plek-om-in-te-vullen): of je belt voor marketing
  - Hulp: Dezelfde vraag als in kader CK5 (telemarketing); het antwoord geldt voor beide.
  - Type: boolean
- **email_tracking**: Meet je of ontvangers je berichten openen of op links klikken?
  - Label (voor de plek-om-in-te-vullen): of je meet of ontvangers je berichten openen of op links klikken
  - Hulp: Veel nieuwsbriefprogramma's doen dit standaard met een onzichtbaar plaatje (pixel) of persoonlijke links.
  - Type: boolean
- **email_tracking_consent**: Hebben ontvangers toestemming gegeven voor het meten of zij je berichten openen en op links klikken?
  - Label (voor de plek-om-in-te-vullen): of ontvangers toestemming gaven voor het meten van openen en klikken
  - Type: boolean · Alleen vragen als: `facts.email_tracking != false`
- **may_include_children**: Kunnen zich ook kinderen jonger dan 16 aanmelden voor je berichten?
  - Label (voor de plek-om-in-te-vullen): of zich ook kinderen jonger dan 16 kunnen aanmelden
  - Type: boolean · Alleen vragen als: `facts.relies_on_consent != false`

## Toetspunten

### CK4.1 — Of je berichten onder de regels voor ongevraagde reclame vallen
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Ongevraagde communicatie voor commerciële, ideële of charitatieve doeleinden via automatische oproepsystemen, fax of elektronische berichten (e-mail, sms, berichtendiensten)
- Grondslag: art. 11.7 lid 1 en art. 11.1 onder i Telecommunicatiewet; art. 13 lid 1 Richtlijn 2002/58/EG; HvJEU C-102/20 StWL; HvJEU C-654/23 Inteligo Media
- Beoordeeld op: de antwoorden
- Nodig: sends_marketing_messages, message_description
- Beoordeling:
  - Kwalificatiestap: 'compliant' betekent dat de kwalificatie (wel of niet onder art. 11.7 Tw) duidelijk vaststaat. Een duidelijk non_compliant geval bestaat bij deze stap niet.
  - Duidelijk geval (compliant, valt eronder): sends_marketing_messages is true en message_description beschrijft reclame, aanbiedingen, een nieuwsbrief die (ook) naar eigen producten, diensten of acties leidt (Inteligo), reclame in een e-mailinbox (StWL), of fondsenwerving.
  - Duidelijk geval (compliant, valt er niet onder): sends_marketing_messages is false en message_description beschrijft alleen transactionele of dienstberichten (orderbevestiging, factuur, wachtwoordherstel, wijziging van voorwaarden) zonder wervende inhoud.
  - Gemengde berichten (bijvoorbeeld een orderbevestiging met een aanbieding, transactional_with_promo true of 'weet ik niet') of een vereniging die alleen leden informeert: geen duidelijk geval. De stappen 2-10 en 12 blijven dan gelden.
  - sends_marketing_messages onbekend: ⚠️ (noem welk antwoord ontbreekt).
  - Kwalificatie 'valt er niet onder' (sends_marketing_messages false en transactional_with_promo false): stap 2-10 en 12 zijn niet van toepassing; stap 11 (telefonische marketing) kan wel gelden.
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Is dit ongevraagde communicatie voor commerciële, ideële of charitatieve doeleinden in de zin van art. 11.7 Tw?
- Advies bij ❌ of ⚠️: Ga ervan uit dat nieuwsbrieven en berichten met aanbiedingen onder de regels voor ongevraagde reclame vallen, ook als er vooral nieuws in staat.
- Bronnen: TW-art11.7-lid1 (Telecommunicatiewet art. 11.7 lid 1); TW-art11.1-i (Telecommunicatiewet art. 11.1 onder i); EPR-art13-lid1 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 1); HvJEU-C-102-20 (HvJEU 25 november 2021, C-102/20, StWL Städtische Werke Lauf a.d. Pegnitz (reclame in de e-mailinbox)); HvJEU-C-654-23 (HvJEU 13 november 2025, C-654/23, Inteligo Media (nieuwsbrief aan gebruikers van een gratis account; art. 13 lid 2))

### CK4.2 — Of je kunt aantonen dat ontvangers vooraf toestemming gaven
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Voorafgaande, actieve, specifieke toestemming voor reclame van deze afzender, die de verzender per ontvanger kan aantonen; geldt voor alle ontvangers voor wie geen uitzondering (lid 3-5) wordt gebruikt
- Grondslag: art. 11.7 lid 1 en art. 11.1 onder g Telecommunicatiewet; art. 4 punt 11, art. 7 lid 1 en 4 en art. 8 AVG
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false) and (facts.relies_on_consent != false or (facts.relies_on_customer_exception != true and facts.relies_on_business_exception != true and facts.relies_on_donor_exception != true))` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: relies_on_consent
- Beoordeling:
  - present: relies_on_consent is true, consent_method is active_optin en consent_provable is true.
  - absent: relies_on_consent is true en consent_method is prechecked, via_terms of purchased_list; of consent_provable is false (de verzender moet de toestemming kunnen aantonen, lid 1).
  - absent: relies_on_consent is false en relies_on_customer_exception, relies_on_business_exception en relies_on_donor_exception zijn alle drie false (geen enkele geldige basis).
  - twijfel (⚠️): consent_method is condition_for_other (art. 7 lid 4 AVG vraagt daar 'zoveel mogelijk rekening mee te houden'; alleen bij duidelijke druk absent); of may_include_children is true of 'weet ik niet' (art. 8 AVG, art. 5 UAVG).
  - relies_on_consent true met consent_method of consent_provable onbekend: ⚠️ (noem welk antwoord ontbreekt).
  - relies_on_consent false terwijl een van de andere bases onbekend is: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Is de toestemming vooraf, actief, specifiek en aantoonbaar gegeven (art. 11.7 lid 1 Tw, art. 7 AVG)?
- Advies bij ❌ of ⚠️: Stuur reclame alleen aan mensen die zich daar zelf actief voor hebben aangemeld, met een leeg vakje of een aparte aanmelding waarin duidelijk staat dat het om reclame van jou gaat. Leg elke aanmelding vast en bewaar het bewijs tot vijf jaar na de laatste verzending.
- Bronnen: TW-art11.7-lid1 (Telecommunicatiewet art. 11.7 lid 1); TW-art11.1-g (Telecommunicatiewet art. 11.1 onder g); EPR-art13-lid1 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 1); AVG-art4-11 (AVG art. 4 punt 11); AVG-art7-lid1 (AVG art. 7 lid 1); AVG-art7-lid4 (AVG art. 7 lid 4); AVG-art8-lid1 (AVG art. 8 lid 1); ACM-spam (Autoriteit Consument & Markt, 'Spam voorkomen in uw reclame')

### CK4.3 — Of je bestaande klanten volgens de regels mailt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Klantuitzondering: contactgegevens verkregen van de eigen klant in het kader van de verkoop van een product of dienst; verzet kosteloos en gemakkelijk geboden bij het verzamelen én bij elk bericht
- Grondslag: art. 11.7 lid 4 Telecommunicatiewet; art. 13 lid 2 Richtlijn 2002/58/EG; HvJEU C-654/23 Inteligo Media
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false) and facts.relies_on_customer_exception != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: relies_on_customer_exception, sale_context, optout_at_collection, unsubscribe_in_every_message
- Beoordeling:
  - present: sale_context is true, optout_at_collection is true en unsubscribe_in_every_message is true.
  - absent: sale_context is false (bijvoorbeeld adressen van aanvragers van een offerte die niets kochten, of van bezoekers van een beurs), optout_at_collection is false, of unsubscribe_in_every_message is false.
  - Een gratis account telt als verkoop als het deel uitmaakt van het verdienmodel (Inteligo Media); twijfel daarover: twijfel (⚠️) (levert de klant marketingbereik op, twijfelregel: review).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Mail bestaande klanten zonder aparte aanmelding alleen als je hun adres kreeg bij een aankoop, als ze zich bij het bestellen al konden afmelden, en als elk bericht een afmeldlink heeft.
- Bronnen: TW-art11.7-lid4 (Telecommunicatiewet art. 11.7 lid 4); EPR-art13-lid2 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 2); HvJEU-C-654-23 (HvJEU 13 november 2025, C-654/23, Inteligo Media (nieuwsbrief aan gebruikers van een gratis account; art. 13 lid 2)); ACM-spam (Autoriteit Consument & Markt, 'Spam voorkomen in uw reclame')

### CK4.4 — Of berichten aan bestaande klanten over je eigen, vergelijkbare producten gaan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: De klantuitzondering geldt alleen voor eigen gelijksoortige producten of diensten
- Grondslag: art. 11.7 lid 4 Telecommunicatiewet; art. 13 lid 2 Richtlijn 2002/58/EG
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false) and facts.relies_on_customer_exception != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: relies_on_customer_exception, similar_own_products
- Beoordeling:
  - present: similar_own_products is same_or_similar (de ACM: producten of diensten die te maken hebben met eerdere aankopen).
  - absent: similar_own_products is third_party (aanbiedingen van andere bedrijven of partners).
  - twijfel (⚠️): similar_own_products is own_other (eigen, maar uit een heel ander assortiment); 'gelijksoortig' is een open norm.
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Zijn de aangeboden producten of diensten gelijksoortig aan wat de klant eerder afnam (art. 11.7 lid 4 Tw)?
- Advies bij ❌ of ⚠️: Stuur bestaande klanten zonder aparte aanmelding alleen aanbiedingen voor je eigen producten of diensten die lijken op wat ze eerder kochten. Voor andere aanbiedingen heb je toestemming nodig.
- Bronnen: TW-art11.7-lid4 (Telecommunicatiewet art. 11.7 lid 4); EPR-art13-lid2 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 2); ACM-spam (Autoriteit Consument & Markt, 'Spam voorkomen in uw reclame')

### CK4.5 — Of je zakelijke ontvangers zonder aanmelding mag mailen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Zakelijke uitzondering: rechtspersoon of natuurlijk persoon in de uitoefening van beroep of bedrijf; elektronische contactgegevens die de ontvanger voor het ontvangen van zulke communicatie heeft bestemd en bekendgemaakt, gebruikt in overeenstemming met dat doel; of ontvanger buiten de EER
- Grondslag: art. 11.7 lid 3 sub a en b Telecommunicatiewet; art. 1.1 Telecommunicatiewet (eindgebruiker)
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false) and facts.relies_on_business_exception != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: relies_on_business_exception, business_address_designated
- Beoordeling:
  - present: business_address_designated is designated_for_offers en het bericht past bij het doel waarvoor het adres is bekendgemaakt.
  - absent: business_address_designated is personal_employee_address_list (persoonlijke adressen van medewerkers zijn niet door het bedrijf bestemd voor het ontvangen van aanbiedingen).
  - absent: recipient_type is consumers (de uitzondering geldt alleen voor ontvangers in de uitoefening van hun beroep of bedrijf). Bij recipient_type both geldt de uitzondering alleen voor de zakelijke ontvangers; zeg dat in de onderbouwing.
  - twijfel (⚠️): business_address_designated is general_info_address (niet duidelijk dat het adres voor aanbiedingen is bestemd) of outside_eea (de regels van het land van de ontvanger gelden, lid 3 sub b).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Heeft de zakelijke ontvanger dit adres bestemd en bekendgemaakt voor het ontvangen van deze communicatie (art. 11.7 lid 3 sub a Tw)?
- Advies bij ❌ of ⚠️: Mail zakelijke ontvangers zonder aanmelding alleen op adressen die zij zelf hebben bekendgemaakt voor het ontvangen van aanbiedingen. Vraag anders eerst toestemming.
- Bronnen: TW-art11.7-lid3-a (Telecommunicatiewet art. 11.7 lid 3 sub a); TW-art11.7-lid3-b (Telecommunicatiewet art. 11.7 lid 3 sub b); ACM-spam (Autoriteit Consument & Markt, 'Spam voorkomen in uw reclame')

### CK4.6 — Of je als goed doel donateurs volgens de regels benadert
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Uitzondering voor ideële en charitatieve organisaties: gegevens verkregen bij een schenking, gebruikt voor eigen ideële of charitatieve doeleinden, verzet geboden bij verzamelen én bij elk bericht
- Grondslag: art. 11.7 lid 5 Telecommunicatiewet
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false) and facts.relies_on_donor_exception != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: relies_on_donor_exception, sender_purpose, donor_context, optout_at_collection, unsubscribe_in_every_message
- Beoordeling:
  - present: sender_purpose is ideal_charitable, donor_context is true, optout_at_collection is true en unsubscribe_in_every_message is true.
  - absent: sender_purpose is commercial (de uitzondering geldt alleen voor ideële of charitatieve organisaties), donor_context is false, optout_at_collection is false of unsubscribe_in_every_message is false.
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Mail donateurs zonder aparte aanmelding alleen voor je eigen doelen, als je hun adres kreeg bij een schenking en ze zich zowel toen als in elk bericht makkelijk kunnen afmelden.
- Bronnen: TW-art11.7-lid5 (Telecommunicatiewet art. 11.7 lid 5)

### CK4.7 — Of elk bericht duidelijk vermeldt van wie het komt en hoe de ontvanger het kan laten stoppen
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Elk bericht vermeldt de werkelijke identiteit van degene namens wie het wordt verstuurd en een geldig adres of nummer om de communicatie te laten beëindigen, en is herkenbaar als commerciële communicatie
- Grondslag: art. 11.7 lid 7 Telecommunicatiewet; art. 3:15e lid 1 BW; art. 13 lid 4 Richtlijn 2002/58/EG
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false)` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: sender_identified, valid_stop_address, recognisable_as_ad
- Beoordeling:
  - present: sender_identified, valid_stop_address en recognisable_as_ad zijn alle drie true.
  - absent: een van de drie is false (bijvoorbeeld een fantasienaam als afzender, een afmeldadres dat niet werkt, of reclame die zich voordoet als persoonlijk bericht).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Vermeld in elk bericht de echte naam van je organisatie en een werkend adres om de berichten te laten stoppen, en maak in de onderwerpregel duidelijk dat het om reclame of een nieuwsbrief gaat.
- Bronnen: TW-art11.7-lid7 (Telecommunicatiewet art. 11.7 lid 7); BW-art3-15e-lid1 (Burgerlijk Wetboek art. 3:15e lid 1 (commerciële communicatie als dienst van de informatiemaatschappij)); EPR-art13-lid4 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 4); ACM-spam (Autoriteit Consument & Markt, 'Spam voorkomen in uw reclame')

### CK4.8 — Of ontvangers zich in elk bericht gratis en makkelijk kunnen afmelden
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Elk bericht bevat een kosteloze en eenvoudige afmeldmogelijkheid
- Grondslag: art. 11.7 lid 4 sub b, lid 5 sub b en lid 7 sub b Telecommunicatiewet; art. 7 lid 3 AVG; art. 13 lid 2 Richtlijn 2002/58/EG
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false)` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: unsubscribe_in_every_message
- Beoordeling:
  - present: unsubscribe_in_every_message is true.
  - absent: unsubscribe_in_every_message is false (bijvoorbeeld afmelden alleen na inloggen, via een vragenlijst, via een betaalde sms, of niet in elk bericht).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Zet in elk bericht een afmeldlink waarmee de ontvanger zich met één klik gratis kan afmelden, zonder in te loggen of vragen te beantwoorden.
- Bronnen: TW-art11.7-lid4 (Telecommunicatiewet art. 11.7 lid 4); TW-art11.7-lid5 (Telecommunicatiewet art. 11.7 lid 5); TW-art11.7-lid7 (Telecommunicatiewet art. 11.7 lid 7); AVG-art7-lid3 (AVG art. 7 lid 3); EPR-art13-lid2 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 13 lid 2); ACM-spam (Autoriteit Consument & Markt, 'Spam voorkomen in uw reclame')

### CK4.9 — Of je direct stopt als iemand zich afmeldt of bezwaar maakt
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Na afmelding of bezwaar tegen direct marketing worden de gegevens niet langer voor direct marketing gebruikt, in alle systemen
- Grondslag: art. 21 lid 2 en 3 AVG; art. 7 lid 3 AVG
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false)` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: unsubscribes_processed
- Beoordeling:
  - present: unsubscribes_processed is true.
  - absent: unsubscribes_processed is false (bijvoorbeeld afgemelde ontvangers die nog berichten krijgen via een ander systeem of een andere afdeling).
- Is het vereiste afwezig (*absent*): ❌
- Advies bij ❌ of ⚠️: Verwerk afmeldingen en bezwaren direct en in alle systemen waarmee je berichten verstuurt, zodat afgemelde ontvangers geen berichten meer krijgen.
- Bronnen: AVG-art21-lid2 (AVG art. 21 lid 2); AVG-art21-lid3 (AVG art. 21 lid 3); AVG-art7-lid3 (AVG art. 7 lid 3)

### CK4.10 — Of 'stuur door aan een vriend' en adressen via anderen volgens de regels gaan
- Soort: Formeel (F): ja/nee-toets op de feiten · telt mee voor de kaderuitkomst
- Toetspunt: Tell-a-friend alleen onder de vijf ACM-voorwaarden; adressen via co-registratie of gekochte bestanden alleen met aantoonbare toestemming voor deze afzender
- Grondslag: art. 11.7 lid 1 Telecommunicatiewet; ACM 'Spam voorkomen in uw reclame'
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false) and (facts.uses_tell_a_friend != false or facts.uses_third_party_lists != false)` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: uses_tell_a_friend, uses_third_party_lists
- Beoordeling:
  - present: uses_third_party_lists is false en tell_a_friend_conditions laat zien dat aan alle vijf ACM-voorwaarden is voldaan: geen beloning voor doorsturen, klachtadres in het bericht, doorsturer ziet het hele bericht vooraf, geen opslag of hergebruik van het adres van de ontvanger, formulier beveiligd tegen misbruik.
  - absent: mensen worden beloond voor het doorsturen, of de adressen van ontvangers worden bewaard en opnieuw gebruikt (dan is de organisatie zelf de verzender van ongevraagde berichten zonder toestemming, art. 11.7 lid 1).
  - twijfel (⚠️): uses_third_party_lists is true (de toestemming moet per afzender aantoonbaar zijn; zie stap 2), of niet alle vijf voorwaarden blijken uit tell_a_friend_conditions.
  - tell_a_friend_conditions ontbreekt bij uses_tell_a_friend true: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ❌
- Bij ⚠️ stel je de gebruiker deze vraag: Voldoet het doorsturen aan de ACM-voorwaarden, en is voor adressen via derden de toestemming per afzender aantoonbaar?
- Advies bij ❌ of ⚠️: Beloon niemand voor het doorsturen van je berichten, bewaar de adressen van ontvangers niet, en gebruik gekochte adressen of adressen uit acties van anderen alleen als je per adres kunt aantonen dat de ontvanger toestemming gaf voor berichten van jou.
- Bronnen: TW-art11.7-lid1 (Telecommunicatiewet art. 11.7 lid 1); ACM-spam (Autoriteit Consument & Markt, 'Spam voorkomen in uw reclame')

### CK4.11 — Of je consumenten mag bellen voor marketing
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt niet mee voor de kaderuitkomst (signalerende stap)
- Toetspunt: Telefonische marketing aan natuurlijke personen: voorafgaande toestemming (lid 2), met de uitzonderingen van lid 4-6; geen nummerweergave blokkeren (lid 8). Wordt getoetst in kader CK5 (telemarketing)
- Grondslag: art. 11.7 lid 2 en 8 Telecommunicatiewet
- Alleen als: `facts.calls_for_marketing != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: calls_for_marketing
- Beoordeling:
  - Deze stap geeft altijd review en verwijst door: telefonische marketing toets je met kader CK5 in deze skill (toestemming, bestaande klanten, recht van verzet, nummerweergave). Draai je CK4 en CK5 samen, noem dan hier alleen de uitkomst van CK5.
- Is het vereiste afwezig (*absent*): ⚠️
- Hoogste uitkomst: ⚠️ (deze stap signaleert; hij wordt nooit ✅)
- Bij ⚠️ stel je de gebruiker deze vraag: Wil je de telefonische marketing ook toetsen (kader CK5)?
- Advies bij ❌ of ⚠️: Bel consumenten alleen voor marketing als zij daar vooraf toestemming voor gaven of als een wettelijke uitzondering geldt, en toon altijd je nummer. Laat dit beoordelen door een juridisch adviseur.
- Bronnen: TW-art11.7-lid2 (Telecommunicatiewet art. 11.7 lid 2); TW-art11.7-lid8 (Telecommunicatiewet art. 11.7 lid 8)

### CK4.12 — Of je meten of berichten worden geopend alleen met toestemming doet
- Soort: Afweging (A): ✅ of ❌ alleen bij een duidelijk geval, anders ⚠️ · telt mee voor de kaderuitkomst
- Toetspunt: Open- en kliktracking met pixels of persoonlijke links in e-mails valt onder art. 11.7a Tw en vereist toestemming, tenzij een uitzondering geldt
- Grondslag: art. 11.7a lid 1 Telecommunicatiewet; art. 5 lid 3 Richtlijn 2002/58/EG; EDPB Richtsnoeren 2/2023
- Alleen als: `(facts.sends_marketing_messages != false or facts.transactional_with_promo != false) and facts.email_tracking != false` (is een antwoord in deze voorwaarde onbekend, dan geldt de stap en wordt het ⚠️)
- Beoordeeld op: de antwoorden
- Nodig: email_tracking, email_tracking_consent
- Beoordeling:
  - Duidelijk geval (compliant): email_tracking_consent is true (ontvangers gaven toestemming voor het meten van openen en klikken).
  - Duidelijk geval (non_compliant): email_tracking is true en email_tracking_consent is false; de harde toets zit in CK1 stap 4.
  - email_tracking_consent onbekend: ⚠️ (noem welk antwoord ontbreekt).
- Is het vereiste afwezig (*absent*): ⚠️
- Bij ⚠️ stel je de gebruiker deze vraag: Vereist de open- en kliktracking in de berichten toestemming onder art. 11.7a Tw, en is die gegeven?
- Advies bij ❌ of ⚠️: Vraag bij de aanmelding ook toestemming voor het meten of berichten worden geopend en links worden aangeklikt, of zet het meten per ontvanger uit in je nieuwsbriefprogramma.
- Bronnen: EDPB-RL-02-2023 (EDPB, Richtsnoeren 2/2023 over de technische reikwijdte van artikel 5, lid 3, van de e-privacyrichtlijn); TW-art11.7a-lid1 (Telecommunicatiewet art. 11.7a lid 1); EPR-art5-lid3 (Richtlijn 2002/58/EG (e-privacyrichtlijn) art. 5 lid 3)

## Vragen waarop "weet ik niet" geen goed antwoord is

Voor deze vragen moet de gebruiker het antwoord eerst uitzoeken (het is een kwalificatievraag): message_description, sender_purpose. Geeft hij toch "weet ik niet", dan wordt de bijbehorende stap ⚠️ en zeg je dat het antwoord eerst nodig is.

## Regels van dit kader

- Stap 1 is een kwalificatiestap en geeft nooit non_compliant. sends_marketing_messages false én transactional_with_promo false → stap 2-10 en 12 not_applicable. Dienstberichten met reclame vallen onder de regels.
- Stap 3 en 8 kunnen bij de klantuitzondering allebei non_compliant worden door een ontbrekende afmeldlink (lid 4 én lid 7); het rapport mag die bevinding samenvoegen.
- Stap 2-10 zijn verplichte F-stappen: één non_compliant → kader non_compliant.
- Stap 2-6 gelden per basis die de organisatie gebruikt. Geen enkele geldige basis (alle vier false) → stap 2 non_compliant. 'Weet ik niet' over een basis → de bijbehorende stap geldt en eindigt in review.

## Samenhang met andere kaders

- Kader K5 (/privacyverklaring) — als `facts.sends_marketing_messages != false`: Bij het verzamelen van e-mailadressen moet de organisatie informeren over het gebruik voor marketing en over het bezwaarrecht (art. 13 en 21 lid 4 AVG).
- Kader K2 (/toets-grondslag) — als `facts.relies_on_consent != false`: Bij toestemming gelden de AVG-eisen aan toestemming (K2a). Bij de klantuitzondering is volgens Inteligo Media geen aparte AVG-grondslag nodig.
- Kader CK1 (/toets-cookies) — als `facts.email_tracking == true`: Open- en kliktracking in e-mails valt onder de cookieregels (art. 11.7a Tw).
- Kader CK5 (/toets-direct-marketing) — als `facts.calls_for_marketing != false`: Bellen voor marketing toets je met CK5 (opt-in, klantuitzondering, recht van verzet, nummerweergave).
- Kader K6 (/verzoek-betrokkene) — als `facts.sends_marketing_messages != false`: Bezwaar tegen direct marketing moet altijd en direct worden gehonoreerd (art. 21 lid 2-3 AVG).

## Open punten en voorbehouden

- Telefonische marketing (art. 11.7 lid 2, 4-6 en 8 Tw): de termijnen voor het bellen van (oud-)klanten en donateurs staan in lagere regelgeving; een eigen kader alleen bij vraag.
- Relatie met de AVG-grondslag: volgens Inteligo Media is art. 13 lid 2 e-privacyrichtlijn een zelfstandige grondslag voor de klantuitzondering; K2 verwijst hiernaar.
- Digital Omnibus (voorstel, geen geldend recht) raakt art. 13 e-privacyrichtlijn (voorzover bekend) niet; opnieuw checken bij een Raadsmandaat.
