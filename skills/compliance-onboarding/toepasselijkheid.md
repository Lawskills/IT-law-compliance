# Toepasselijkheid — van profielantwoord naar verplichting

Peildatum 2026-11-10. Deze tabel bepaalt welke regels in het register komen. Elke regel wordt aan de gebruiker getoond met het antwoord waarop ze rust.

## Regels voor het toepassen

- **Alleen wat volgt uit een antwoord.** Zet een regel in het register als de kolom "Geldt als" waar is volgens de antwoorden. Noem bij elke regel het antwoord waarop ze rust (sleutel en waarde).
- **"Weet ik niet" is geen "nee".** Bij een onbekend antwoord komt de regel in het register met status `open` en de opmerking "toepasselijkheid vaststellen"; de bijbehorende toets-skill beslist.
- **Drempels en uitzonderingen beslist de toets, niet deze tabel.** Waar de wet drempels kent (bijvoorbeeld de omvang bij de Cyberbeveiligingswet, de uitzondering van het verwerkingsregister, de DPIA-criteria) wordt alleen de toets-skill als verplichting opgenomen: "Toetsen: …". Beslis niet zelf dat iets niet geldt.
- **`n.v.t.` alleen op een expliciet "nee".** Een duidelijk "nee" op de voorwaarde geeft status `n.v.t.` met de reden in de opmerking. Zet geen n.v.t.-regels voor onderwerpen waarover niets is gevraagd.
- **Domeinen** zijn: Privacy, Informatiebeveiliging, AI & cyber, Contracten. Gebruik exact deze namen in het register.
- De kolom "Skill" is de map van de skill. Kies de toets-skill als de vraag "geldt het en wat is de stand?" is, en de opstel-skill als er een document bij hoort; neem bij een toets die tot een document leidt beide op als aparte regels alleen als de gebruiker het document ook wil.

## Tabel

| Onderwerp | Skill | Domein | Geldt als | Opmerking |
|---|---|---|---|---|
| Toepasselijkheid AVG en rol vaststellen | toets-toepasselijkheid-rol | Privacy | rol = weet ik niet, of gegevens_soorten niet leeg | Altijd nuttig als de rol onduidelijk is |
| Grondslag per verwerkingsdoel | toets-grondslag | Privacy | gegevens_soorten niet leeg | Extra aandacht bij bijzondere_gegevens = ja |
| Beginselen en privacy by design | toets-beginselen | Privacy | gegevens_soorten niet leeg | Vooral bij nieuwe tools of processen |
| Verwerkingsregister (art. 30) | toets-verwerkingsregister | Privacy | gegevens_soorten niet leeg | De toets beslist over de uitzondering voor kleine organisaties |
| Privacyverklaring | privacyverklaring | Privacy | rol = verantwoordelijke of beide of onbekend, en gegevens_soorten niet leeg | |
| Bewaarbeleid | bewaarbeleid | Privacy | rol = verantwoordelijke of beide, en gegevens_soorten niet leeg | |
| Procedure voor verzoeken van betrokkenen | verzoek-betrokkene | Privacy | rol = verantwoordelijke of beide, en gegevens_soorten niet leeg | Document wordt per verzoek opgesteld; in het register staat de procedure |
| Datalekprocedure | datalekprocedure | Privacy | gegevens_soorten niet leeg | Bij datalek_proces = nee of onbekend: status open |
| Verwerkersovereenkomsten met leveranciers | verwerkersovereenkomst | Privacy | verwerkers = ja, of rol = verwerker of beide | Eén regel per leveranciersgroep als de gebruiker dat wil |
| Subverwerkersovereenkomsten | subverwerkersovereenkomst | Privacy | rol = verwerker of beide, en subverwerkers = ja | |
| Afspraken bij gegevens delen | gegevensdelingsovereenkomst | Privacy | delen = ja | |
| Regeling gezamenlijke verantwoordelijkheid | samenwerkingsafspraken | Privacy | gezamenlijk = ja | |
| Doorgifte buiten de EER toetsen | toets-doorgifte | Privacy | doorgifte = ja of onbekend | |
| Standaardcontractbepalingen en bijlagen | scc-bijlagen | Privacy | doorgifte = ja | Alleen als de toets passende waarborgen vraagt; anders status open met opmerking |
| DPIA | dpia | Privacy | bijzondere_gegevens = ja, of omvang = meer dan 100.000 of weet ik niet, of profilering_besluiten = ja, of camera = ja | Deze voorwaarden agenderen alleen de DPIA-toets (geen wettelijke drempel); de toets beslist of een DPIA verplicht is |
| Functionaris gegevensbescherming toetsen | toets-fg-plicht | Privacy | gegevens_soorten niet leeg | |
| Geautomatiseerde besluiten en profilering | toets-geautomatiseerde-besluiten | Privacy | profilering_besluiten = ja of onbekend | |
| Cameratoezicht | toets-cameratoezicht | Privacy | camera = ja | |
| Personeelszaken en werving | toets-hr-privacy | Privacy | hr = ja | |
| Cookies en trackers toetsen | toets-cookies | Privacy | trackers = ja of onbekend | |
| Cookieverklaring | cookieverklaring | Privacy | trackers = ja | |
| Commerciële berichten en acquisitie | toets-direct-marketing | Privacy | marketing = ja | |
| Informatiebeveiligingsbeleid | beveiligingsbeleid | Informatiebeveiliging | gegevens_soorten niet leeg | Bij beveiliging_basis zonder "beleid": status open |
| Beveiliging van persoonsgegevens toetsen | toets-beveiliging | Informatiebeveiliging | gegevens_soorten niet leeg | |
| Cyberbeveiligingswet toetsen | toets-cyberbeveiligingswet | AI & cyber | nis2_sector = ja of onbekend | De toets beslist over sector en omvang |
| AI-verordening: basis (rol, verboden, geletterdheid, transparantie) | toets-ai-act-basis | AI & cyber | ai_gebruik = ja of ai_eigen = ja of ai_inkoop = ja of een van deze onbekend | |
| AI-gebruiksbeleid voor medewerkers | ai-gebruiksbeleid | AI & cyber | ai_gebruik = ja | |
| AI-inkoopafspraken | ai-inkoopafspraken | AI & cyber | ai_inkoop = ja | |
| AI met hoog risico | toets-ai-act-hoog-risico | AI & cyber | ai_hoog_risico = ja of onbekend | |
| Algemene voorwaarden | algemene-voorwaarden | Contracten | verkoop = ja | Bij een webshop of app voor consumenten hoort daar de online ontbindingsfunctie bij (art. 6:230oa BW, sinds juni 2026); noem dat in de opmerking |
| Verplichte informatie op de website | website-verplichte-informatie | Contracten | website is niet "geen" | |
| Toegankelijkheid van webshop of app | toets-toegankelijkheid | Contracten | website = webshop voor consumenten of app | De toets beslist over uitzonderingen |
| Gebruiksvoorwaarden platform | platformvoorwaarden | Contracten | website = platform waar gebruikers inhoud plaatsen | |
| SaaS-overeenkomst | saas-overeenkomst | Contracten | overeenkomsten bevat SaaS/cloud leveren | |
| Softwarelicentie | softwarelicentie | Contracten | overeenkomsten bevat software licentiëren | |
| Service level agreement | sla | Contracten | overeenkomsten bevat SLA | |
| Ontwikkelovereenkomst | ontwikkelovereenkomst | Contracten | overeenkomsten bevat software laten bouwen | |
| Geheimhoudingsovereenkomst | geheimhoudingsovereenkomst | Contracten | overeenkomsten bevat NDA | |

## Niet in het register

- **Datalekmelding** (`datalekmelding`): gebeurtenis, geen doorlopende verplichting. Registreer een melding als activiteit zodra ze is opgesteld.
- **Huisstijl** (`huisstijl-en-standaardclausules`): hulpmiddel, geen verplichting. Het resultaat is het bestand `huisstijl.md`.
