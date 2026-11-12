# IT-law-compliance — Lawskills

**45 Claude skills for Dutch and EU IT law and compliance.** You start a skill, answer a few questions in clickable fields, and Claude drafts the document or produces an assessment report, with the legal basis for each point. Anything missing or uncertain is clearly marked (`[IN TE VULLEN: …]` = "to be completed", or ⚠️).

[Nederlandse versie](README.md) · [Releases](https://github.com/Lawskills/IT-law-compliance/releases) · [Changelog](CHANGELOG.md) · [Licence](#licence)

Repository and website: [Lawskills/IT-law-compliance](https://github.com/Lawskills/IT-law-compliance) · [lawskills.github.io/IT-law-compliance](https://lawskills.github.io/IT-law-compliance/)

> **Language:** the skills themselves are in Dutch and are built on Dutch and EU law. They work in any Claude conversation, but questions, documents and reports are in Dutch. This page and the licence information are also available in English.

## Why this project

Much compliance work in small and medium-sized businesses is repetitive: a data processing agreement, a privacy notice, a cookie check, a DPIA. The rules are set by law, but applying them takes time and mistakes hide in the details. Lawskills captures those rules in assessment frameworks with fixed decision rules, so Claude asks the same questions and makes the same assessment at every step, and says when something is uncertain instead of guessing.

## What it does

- **Drafting** (24 skills): data processing agreement, privacy notice, DPIA, data breach procedure, NDA, SLA, SaaS agreement, general terms and conditions, AI use policy and more.
- **Assessments** (16 skills): GDPR (role, legal basis, principles, security, international transfers), cookies, direct marketing, the AI Act, the Dutch Cybersecurity Act (NIS2 implementation) and accessibility. Every check gets ✅ complies, ❌ does not comply, ⚠️ to be filled in, or n/a, with the legal basis and a next step.
- **Workspace** (4 skills): onboarding with a compliance register, a dashboard, a source-bound Q&A skill that only answers from the source list, and an update skill.

Missing never means "complies": a required answer that is missing (including "I don't know") gives ❌ does not comply; for a recommendation it gives ⚠️ to be filled in. Never silently "complies" or "not applicable".

## Getting started

1. **Install** the skills (see [Installation](#installation)).
2. **Start with onboarding:** say `/compliance-onboarding`. Claude asks once about your organisation, determines which obligations apply to you and creates your register (`compliance-register.md`). Keep that file in a Project or your working folder; the skills do not remember it on their own.
3. **Pick what you need:** draft a document (for example `/privacyverklaring`, privacy notice) or run an assessment (for example `/toets-cookies`, cookie check). You answer the questions in clickable fields.
4. **Register the result:** after a finished document, say "registreer dit" ("register this"). `/compliance-overzicht` then shows your progress, open issues and tasks.

## Installation

### Claude.ai (recommended: one bundle)

Claude.ai shows every skill separately in one list. The bundle gives you a single entry, `lawskills`, with a menu: you pick a topic and then the assessment or document.

1. Download `lawskills-bundel.zip` from the [latest release](https://github.com/Lawskills/IT-law-compliance/releases/latest).
2. Go to **Settings → Skills** (Customize → Skills → Add → Upload skill) and upload the zip.
3. Open a new chat and type `lawskills`.

Use either the bundle or the individual skills, not both. Prefer individual skills? Download `lawskills-losse-skills.zip` from the same release, unzip it and upload the zip of each skill. Install all of them: `/compliance-chat` reads the files of the other skills.

### Claude Code

```
/plugin marketplace add Lawskills/IT-law-compliance
/plugin install lawskills@it-law-compliance
```

The skills are then called `/lawskills:verwerkersovereenkomst`, `/lawskills:toets-cookies` and so on. Type `/lawskills:` to see them all. For short names (`/dpia`), copy the `skills/` folder to `~/.claude/skills/`.

## Updating

- **Claude Code:** say `/lawskills:compliance-update`. It shows your version and what is new, updates the plugin (after your approval) and removes old or duplicate skills. Restart Claude Code afterwards. Manually: `/plugin marketplace update`, then `/plugin update lawskills@it-law-compliance` (terminal only, not in the chat).
- **Claude.ai:** download the latest `lawskills-bundel.zip`, upload it under the same name (the old one is replaced) and start a new chat. A running conversation keeps using the old version.

## Skills

Skill names are Dutch; the description is in English.

### Workspace

| Skill | What it does |
|---|---|
| `/compliance-onboarding` | Asks about your organisation, determines which obligations apply, records your house style and creates the register |
| `/compliance-overzicht` | Dashboard: progress per domain, monthly trend, open risks, tasks and next steps, all from your register (progress = share of obligations marked done, not a compliance score) |
| `/compliance-register` | Shows your whole register: profile, obligations, tasks, risks and activity, exactly as they are recorded, with filters by domain or status |
| `/compliance-chat` | Answers questions on privacy, AI, cyber and contracts, only from the project's source list, with a citation and status per statement |
| `/compliance-update` | Checks your version, shows what is new and updates the set |

### Drafting

| Skill | What it drafts | Legal basis |
|---|---|---|
| `/huisstijl-en-standaardclausules` | Your own house style and standard clauses, used by all drafting skills | your own choices, subject to the law |
| `/verwerkersovereenkomst` | Data processing agreement, as controller or processor | Art. 28 GDPR |
| `/subverwerkersovereenkomst` | Agreement with a sub-processor | Art. 28(2) and (4) GDPR |
| `/gegevensdelingsovereenkomst` | Data sharing agreement between independent controllers | Arts. 5, 6, 32, 33 and 44–46 GDPR, good practice |
| `/samenwerkingsafspraken` | Joint controller arrangement | Art. 26 GDPR |
| `/scc-bijlagen` | Annexes to the Standard Contractual Clauses (transfers outside the EEA) | Arts. 44–46 GDPR and the SCCs |
| `/privacyverklaring` | Privacy notice | Arts. 13 and 14 GDPR |
| `/cookieverklaring` | Cookie notice | Dutch Telecommunications Act, art. 11.7a; GDPR |
| `/dpia` | Data protection impact assessment | Art. 35 GDPR |
| `/datalekprocedure` | Data breach procedure | Arts. 33 and 34 GDPR |
| `/datalekmelding` | Data breach notification to the Dutch DPA | Art. 33 GDPR |
| `/verzoek-betrokkene` | Reply to an access, rectification, erasure or other data subject request | Arts. 12–22 GDPR |
| `/bewaarbeleid` | Retention policy | Art. 5(1)(e) GDPR |
| `/beveiligingsbeleid` | Information security policy | Art. 32 GDPR |
| `/geheimhoudingsovereenkomst` | NDA, one-way or mutual | Dutch Civil Code art. 6:248, Trade Secrets Act, good practice |
| `/ai-gebruiksbeleid` | AI use policy for staff | AI Act (incl. art. 4), good practice |
| `/ai-inkoopafspraken` | AI annex to a procurement agreement | AI Act, art. 28 GDPR, EU model clauses for AI procurement (MCC-AI) |
| `/algemene-voorwaarden` | General terms and conditions, B2B or B2C | Dutch Civil Code books 6 and 7 |
| `/sla` | Service level agreement | good practice, GDPR, Data Act |
| `/saas-overeenkomst` | SaaS or cloud agreement with switching rules | Data Act (incl. art. 25), art. 28 GDPR |
| `/softwarelicentie` | Software licence (EULA) | Dutch Copyright Act, Civil Code book 7 |
| `/ontwikkelovereenkomst` | Software development agreement with IP transfer | Dutch Copyright Act, Civil Code book 7 |
| `/platformvoorwaarden` | Terms of use for an online platform | Digital Services Act |
| `/website-verplichte-informatie` | Mandatory business information for your website | Dutch Civil Code arts. 3:15d and 6:227b ff. |

### Assessments

| Skill | What it checks |
|---|---|
| `/toets-toepasselijkheid-rol` | Does the GDPR apply, and are you controller, processor or joint controller? |
| `/toets-grondslag` | Valid legal basis per purpose; special categories, criminal data and the Dutch citizen service number (BSN) |
| `/toets-beginselen` | Principles of art. 5 GDPR, retention periods, privacy by design and by default |
| `/toets-verwerkingsregister` | Duty to keep a record of processing activities and its contents (art. 30 GDPR) |
| `/toets-fg-plicht` | Must you appoint a data protection officer? |
| `/toets-beveiliging` | Appropriate security measures (art. 32 GDPR) |
| `/toets-doorgifte` | Transfers outside the EEA and the transfer impact assessment (TIA) |
| `/toets-cameratoezicht` | Camera surveillance by businesses |
| `/toets-hr-privacy` | Sick leave and absent employees; recruitment and selection |
| `/toets-geautomatiseerde-besluiten` | Automated decision-making and profiling (art. 22 GDPR) |
| `/toets-cookies` | Cookies and trackers, exemptions, consent and the cookie banner |
| `/toets-direct-marketing` | Email marketing, spam and telemarketing |
| `/toets-ai-act-basis` | AI system and role, prohibited practices, high-risk signal, AI literacy, transparency |
| `/toets-ai-act-hoog-risico` | High-risk AI obligations per role (deployer, provider, importer, distributor) and the fundamental rights impact assessment |
| `/toets-cyberbeveiligingswet` | Obligations under the Dutch Cybersecurity Act |
| `/toets-toegankelijkheid` | Accessibility of a web shop or app (European Accessibility Act) |

An assessment or document starts with a single intake: every question that is needed now comes at once, yes/no questions as a checklist of three, and only questions that depend on an answer follow in one second round (usually the last). A question that no longer applies to you is skipped. An obligation that only applies later, such as the AI Act's high-risk obligations (from 2 December 2027 or 2 August 2028), is shown as a preparation item with its date.

## Limitations

- The skills are a tool, **not legal advice**. Check facts, amounts and choices before using a document, and consult a specialist for unusual situations.
- An assessment only evaluates what you state or provide; it cannot verify whether that is correct.
- Laws change. A weekly source check reduces the risk of outdated text but does not rule it out. Content as of: 2026-11-10.
- Default clauses (term, liability, notification periods) are common market choices, not legal requirements.
- Structure and decision rules are tested automatically on every change; the legal content is not yet tested systematically. Please report errors via an [issue](https://github.com/Lawskills/IT-law-compliance/issues).
- No personal data of data subjects is requested; you fill in names and similar details yourself.

## Licence

© 2026 Akram al Khafaji.

- **Texts** (skills, frameworks, documentation): [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You may use, share and adapt them, also commercially, provided you credit *Akram al Khafaji* with a link to this repository and indicate what you changed.
- **Code** (the `.py` files): [MIT](LICENSE-CODE).

Third-party material and sources: [NOTICE.md](NOTICE.md). No warranty; this is a tool, not legal advice.
