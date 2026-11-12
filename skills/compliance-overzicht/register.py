#!/usr/bin/env python3
"""Compliance-register: lezen, bijwerken en samenvatten.

Alle cijfers in het overzicht worden hier uit het register berekend. Er zijn geen
vaste of voorbeeldwaarden: een leeg register geeft lege widgets.

Gebruik:
  python3 register.py init    <register.md> [--org "Naam"] [--today JJJJ-MM-DD]
  python3 register.py metrics <register.md> [--today JJJJ-MM-DD]   -> JSON
  python3 register.py html    <register.md> [--today JJJJ-MM-DD]   -> HTML-fragment (widgets)
  python3 register.py text    <register.md> [--today JJJJ-MM-DD]   -> tekstoverzicht (Markdown)
  python3 register.py show    <register.md> [--sectie S] [--status S] [--domein D]  -> het hele register als tabellen
  python3 register.py validate <register.md>                       -> fouten en waarschuwingen
  python3 register.py add     <register.md> <sectie> kolom=waarde ...  (ID wordt automatisch gevuld)
  python3 register.py set     <register.md> <sectie> <ID> kolom=waarde ...
Secties: verplichtingen | taken | risicos | activiteit | profiel
"""
import sys, re, json, datetime, html, calendar

DOMEINEN = ["Privacy", "Informatiebeveiliging", "AI & cyber", "Contracten"]
SECTIES = {
    "profiel": ("Profiel", ["Sleutel", "Waarde"]),
    "verplichtingen": ("Verplichtingen", ["ID", "Skill", "Domein", "Onderwerp", "Status", "Toepasselijk sinds", "Afgerond op", "Volgende review", "Opmerking"]),
    "taken": ("Taken", ["ID", "Taak", "Skill", "Deadline", "Prioriteit", "Status"]),
    "risicos": ("Risico's", ["ID", "Omschrijving", "Niveau", "Skill", "Status"]),
    "activiteit": ("Activiteit", ["Datum", "Skill", "Gebeurtenis", "Uitkomst"]),
}
PREFIX = {"verplichtingen": "V", "taken": "T", "risicos": "R"}
STATUS_V = {"open", "loopt", "klaar", "n.v.t."}
STATUS_T = {"open", "klaar"}
STATUS_R = {"open", "beheerst"}
NIVEAU = {"hoog", "middel", "laag"}
MAANDEN = ["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]


# ---------- lezen en schrijven ----------
def cells(line):
    s = line.strip()
    if s.startswith("|"): s = s[1:]
    if s.endswith("|"): s = s[:-1]
    return [c.strip() for c in s.split("|")]


def is_sep(line):
    return bool(re.match(r"^\s*\|?\s*:?-{2,}", line)) and set(line.replace("|", "").replace(":", "").replace("-", "").strip()) == set()


def norm(h):
    n = re.sub(r"[^a-z0-9]+", "_", h.lower()).strip("_")
    return "risicos" if n == "risico_s" else n


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read().split("\n")


def section_bounds(lines):
    """naam (genormaliseerd) -> (kop_index, einde_index)"""
    heads = [(i, norm(l[3:])) for i, l in enumerate(lines) if l.startswith("## ")]
    out = {}
    for n, (i, name) in enumerate(heads):
        out[name] = (i, heads[n + 1][0] if n + 1 < len(heads) else len(lines))
    return out


def parse_tables(lines):
    """-> {sectie: [dict, ...]} met genormaliseerde kolomnamen; rijen krijgen _regel."""
    res = {}
    for name, (a, z) in section_bounds(lines).items():
        rows, header = [], None
        for i in range(a + 1, z):
            l = lines[i]
            if not l.strip().startswith("|"):
                continue
            if header is None:
                header = [norm(c) for c in cells(l)]
                continue
            if is_sep(l):
                continue
            c = cells(l)
            c += [""] * (len(header) - len(c))
            d = {header[k]: c[k] for k in range(len(header))}
            d["_regel"] = i
            if any(v for k, v in d.items() if k != "_regel"):
                rows.append(d)
        res[name] = rows
    return res


def d(s):
    try:
        return datetime.date.fromisoformat(s.strip())
    except Exception:
        return None


def clean(v):
    return str(v).replace("|", "/").replace("\n", " ").strip()


def template(org, today):
    L = ["# Compliance-register", "",
         "Dit bestand is de bron van `/compliance-overzicht`. Alle cijfers daar worden hieruit berekend; wat hier niet staat, bestaat voor het overzicht niet.",
         "Bewaar het als bestand in je Project of werk het bij via `/compliance-overzicht` (\"registreer: …\").", "",
         "## Profiel", "", "| Sleutel | Waarde |", "|---|---|",
         f"| Organisatie | {clean(org)} |", f"| Register aangemaakt | {today} |", "",
         "## Verplichtingen", "",
         "Status: `open`, `loopt`, `klaar` of `n.v.t.`. Datums als JJJJ-MM-DD. Een verplichting telt voor het overzicht pas als `klaar` met een afrondingsdatum.", "",
         "| ID | Skill | Domein | Onderwerp | Status | Toepasselijk sinds | Afgerond op | Volgende review | Opmerking |",
         "|---|---|---|---|---|---|---|---|---|", "",
         "## Taken", "", "Prioriteit: `hoog`, `middel`, `laag`. Status: `open` of `klaar`.", "",
         "| ID | Taak | Skill | Deadline | Prioriteit | Status |", "|---|---|---|---|---|---|", "",
         "## Risico's", "", "Niveau: `hoog`, `middel`, `laag`. Status: `open` of `beheerst`.", "",
         "| ID | Omschrijving | Niveau | Skill | Status |", "|---|---|---|---|---|", "",
         "## Activiteit", "", "| Datum | Skill | Gebeurtenis | Uitkomst |", "|---|---|---|---|", ""]
    return "\n".join(L)


def add_row(path, sectie, kv, today):
    lines = read(path)
    name, cols = SECTIES[sectie]
    b = section_bounds(lines).get(norm(name))
    if not b:
        lines += ["", f"## {name}", "", "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
        b = section_bounds(lines)[norm(name)]
    a, z = b
    last = None
    for i in range(a + 1, z):
        if lines[i].strip().startswith("|"):
            last = i
    rows = parse_tables(lines).get(norm(name), [])
    kv = {norm(k): v for k, v in kv.items()}
    if "id" in cols[0].lower() and sectie in PREFIX:
        n = 0
        for r in rows:
            m = re.match(rf"^{PREFIX[sectie]}-(\d+)$", r.get("id", ""))
            if m: n = max(n, int(m.group(1)))
        kv.setdefault("id", f"{PREFIX[sectie]}-{n + 1:03d}")
    if sectie == "activiteit":
        kv.setdefault("datum", today)
    if sectie == "verplichtingen":
        kv.setdefault("toepasselijk_sinds", today)
        if kv.get("status", "").lower() == "klaar":
            kv.setdefault("afgerond_op", today)
    vals = [clean(kv.get(norm(c), "")) for c in cols]
    lines.insert(last + 1, "| " + " | ".join(vals) + " |")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return vals


def set_row(path, sectie, rid, kv):
    lines = read(path)
    name, cols = SECTIES[sectie]
    rows = parse_tables(lines).get(norm(name), [])
    key = norm(cols[0])
    for r in rows:
        if r.get(key, "") == rid:
            old = cells(lines[r["_regel"]])
            old += [""] * (len(cols) - len(old))
            for k, v in kv.items():
                nk = norm(k)
                for j, c in enumerate(cols):
                    if norm(c) == nk:
                        old[j] = clean(v)
            lines[r["_regel"]] = "| " + " | ".join(old) + " |"
            open(path, "w", encoding="utf-8").write("\n".join(lines))
            return old
    raise SystemExit(f"ID {rid} niet gevonden in {name}")


# ---------- berekenen ----------
def month_end(y, m):
    return datetime.date(y, m, calendar.monthrange(y, m)[1])


def months_between(a, b):
    y, m = a.year, a.month
    out = []
    while (y, m) <= (b.year, b.month):
        out.append((y, m))
        m += 1
        if m == 13: y, m = y + 1, 1
    return out


def compute(path, today):
    lines = read(path)
    T = parse_tables(lines)
    prof = {r.get("sleutel", ""): r.get("waarde", "") for r in T.get("profiel", [])}
    org = prof.get("Organisatie", "")
    created = d(prof.get("Register aangemaakt", "")) or today
    warn, vers = [], T.get("verplichtingen", [])
    for v in vers:
        st = v.get("status", "").lower()
        v["_st"] = st
        if st not in STATUS_V: warn.append(f"{v.get('id','?')}: onbekende status '{v.get('status','')}'")
        v["_dom"] = v.get("domein", "") if v.get("domein", "") in DOMEINEN else "Overig"
    appl = [v for v in vers if v["_st"] != "n.v.t."]
    doms = DOMEINEN + (["Overig"] if any(v["_dom"] == "Overig" for v in appl) else [])

    def stats(sub):
        n = len(sub); k = sum(v["_st"] == "klaar" for v in sub)
        return {"toepasselijk": n, "klaar": k, "loopt": sum(v["_st"] == "loopt" for v in sub),
                "open": sum(v["_st"] == "open" for v in sub), "score": round(100 * k / n) if n else None}
    domein = {dm: stats([v for v in appl if v["_dom"] == dm]) for dm in doms}
    totaal = stats(appl)

    zonder_datum = [v.get("id", "?") for v in appl if v["_st"] == "klaar" and not d(v.get("afgerond_op", ""))]
    if zonder_datum:
        warn.append("Klaar zonder afrondingsdatum (telt mee in de score, niet in de trend): " + ", ".join(zonder_datum))

    # trend: per maandeinde de stand uit de datums in het register
    starts = [d(v.get("toepasselijk_sinds", "")) or created for v in appl]
    ends = [d(v.get("afgerond_op", "")) for v in appl if d(v.get("afgerond_op", ""))]
    trend = {"maanden": [], "totaal": [], "domeinen": {dm: [] for dm in doms}}
    if appl:
        first = min(starts + ends)
        for (y, m) in months_between(first, today)[-12:]:
            last_day = min(month_end(y, m), today)
            cur = (y, m) == (today.year, today.month)
            trend["maanden"].append(f"{MAANDEN[m-1]} {str(y)[2:]}")

            def pt(sub):
                if cur:
                    return stats(sub)["score"]
                ap = [v for v in sub if (d(v.get("toepasselijk_sinds", "")) or created) <= last_day]
                if not ap: return None
                k = sum(1 for v in ap if v["_st"] == "klaar" and d(v.get("afgerond_op", "")) and d(v["afgerond_op"]) <= last_day)
                return round(100 * k / len(ap))
            trend["totaal"].append(pt(appl))
            for dm in doms:
                trend["domeinen"][dm].append(pt([v for v in appl if v["_dom"] == dm]))

    # taken
    taken = T.get("taken", [])
    open_taken = [t for t in taken if t.get("status", "").lower() != "klaar"]
    pr = {"hoog": 0, "middel": 1, "laag": 2}
    for t in open_taken:
        dl = d(t.get("deadline", ""))
        t["_dl"] = dl
        t["_te_laat"] = bool(dl and dl < today)
    open_taken.sort(key=lambda t: (t["_dl"] is None, t["_dl"] or datetime.date.max, pr.get(t.get("prioriteit", "").lower(), 3)))
    # risico's
    risk = [r for r in T.get("risicos", []) if r.get("status", "").lower() != "beheerst"]
    rc = {n: sum(r.get("niveau", "").lower() == n for r in risk) for n in ("hoog", "middel", "laag")}
    for r in risk:
        if r.get("niveau", "").lower() not in NIVEAU: warn.append(f"{r.get('id','?')}: onbekend niveau '{r.get('niveau','')}'")
    # activiteit
    act = sorted(T.get("activiteit", []), key=lambda r: d(r.get("datum", "")) or datetime.date.min, reverse=True)
    # reviews
    reviews = [v for v in vers if v["_st"] == "klaar" and d(v.get("volgende_review", "")) and d(v["volgende_review"]) < today]
    # volgende stappen (deterministisch, in deze volgorde)
    stappen = []
    for t in open_taken:
        if t["_te_laat"]: stappen.append(f"Taak te laat sinds {t['deadline']}: {t.get('taak','')}")
    for r in risk:
        if r.get("niveau", "").lower() == "hoog": stappen.append(f"Hoog risico open: {r.get('omschrijving','')}")
    for v in reviews:
        stappen.append(f"Review verlopen sinds {v['volgende_review']}: {v.get('onderwerp','')} ({v.get('skill','')})")
    for t in open_taken:
        if not t["_te_laat"] and t["_dl"] and (t["_dl"] - today).days <= 30:
            stappen.append(f"Deadline {t['deadline']}: {t.get('taak','')}")
    for v in appl:
        if v["_st"] == "open":
            stappen.append(f"Nog te starten: {v.get('onderwerp','')} (/{v.get('skill','')})")
    for v in appl:
        if v["_st"] == "loopt":
            stappen.append(f"Afronden: {v.get('onderwerp','')} (/{v.get('skill','')})")
    return {
        "peildatum": str(today), "organisatie": org, "register_aangemaakt": str(created),
        "leeg": not vers and not taken and not risk and not act,
        "totaal": totaal, "domeinen": domein, "trend": trend,
        "risicos": {"open": len(risk), **rc},
        "taken_open": [{"id": t.get("id", ""), "taak": t.get("taak", ""), "skill": t.get("skill", ""), "deadline": t.get("deadline", ""),
                        "prioriteit": t.get("prioriteit", ""), "te_laat": t["_te_laat"]} for t in open_taken],
        "reviews_verlopen": len(reviews),
        "activiteit": [{k: r.get(k, "") for k in ("datum", "skill", "gebeurtenis", "uitkomst")} for r in act[:8]],
        "volgende_stappen": stappen[:8], "waarschuwingen": warn,
    }


def validate(path):
    lines = read(path)
    T = parse_tables(lines)
    errs = []
    for r in T.get("verplichtingen", []):
        if r.get("status", "").lower() not in STATUS_V: errs.append(f"Verplichting {r.get('id','?')}: status '{r.get('status','')}' is geen open/loopt/klaar/n.v.t.")
        if r.get("domein", "") not in DOMEINEN: errs.append(f"Verplichting {r.get('id','?')}: domein '{r.get('domein','')}' hoort bij {DOMEINEN}")
        for k in ("toepasselijk_sinds", "afgerond_op", "volgende_review"):
            if r.get(k, "") and not d(r[k]): errs.append(f"Verplichting {r.get('id','?')}: {k} '{r[k]}' is geen JJJJ-MM-DD")
        if r.get("status", "").lower() == "klaar" and not r.get("afgerond_op"): errs.append(f"Verplichting {r.get('id','?')}: klaar zonder afrondingsdatum")
    for r in T.get("taken", []):
        if r.get("status", "").lower() not in STATUS_T: errs.append(f"Taak {r.get('id','?')}: status moet open of klaar zijn")
        if r.get("deadline", "") and not d(r["deadline"]): errs.append(f"Taak {r.get('id','?')}: deadline '{r['deadline']}' is geen JJJJ-MM-DD")
        if r.get("prioriteit", "").lower() not in pr_set(): errs.append(f"Taak {r.get('id','?')}: prioriteit moet hoog, middel of laag zijn")
    for r in T.get("risicos", []):
        if r.get("niveau", "").lower() not in NIVEAU: errs.append(f"Risico {r.get('id','?')}: niveau moet hoog, middel of laag zijn")
        if r.get("status", "").lower() not in STATUS_R: errs.append(f"Risico {r.get('id','?')}: status moet open of beheerst zijn")
    for r in T.get("activiteit", []):
        if not d(r.get("datum", "")): errs.append(f"Activiteit '{r.get('gebeurtenis','')}': datum '{r.get('datum','')}' is geen JJJJ-MM-DD")
    ids = [r.get("id") for s in ("verplichtingen", "taken", "risicos") for r in T.get(s, [])]
    for i in set(ids):
        if i and ids.count(i) > 1: errs.append(f"ID {i} komt meerdere keren voor")
    return errs


def pr_set():
    return {"hoog", "middel", "laag"}


# ---------- uitvoer: tekst ----------
def bar(p, n=10):
    if p is None: return "·" * n
    k = round(p / 100 * n)
    return "█" * k + "░" * (n - k)


def spark(vals):
    chars = "▁▂▃▄▅▆▇█"
    return "".join("·" if v is None else chars[min(7, int(v / 100 * 7.999))] for v in vals)


def fmt(p):
    return "—" if p is None else f"{p}%"


def text(M):
    o = [f"# Overzicht{' — ' + M['organisatie'] if M['organisatie'] else ''}", f"Peildatum {M['peildatum']}", ""]
    if M["leeg"]:
        return "\n".join(o + ["Het register is nog leeg. Draai `/compliance-onboarding` om je profiel en je verplichtingen vast te leggen; tot die tijd valt er niets te berekenen."])
    t = M["totaal"]
    o += [f"**Voortgang totaal: {fmt(t['score'])}** ({t['klaar']} van {t['toepasselijk']} toepasselijke verplichtingen klaar, {t['loopt']} lopend, {t['open']} open)", ""]
    o += ["| Domein | Voortgang | Klaar / toepasselijk | Loopt | Open |", "|---|---|---|---|---|"]
    for dm, s in M["domeinen"].items():
        o.append(f"| {dm} | {bar(s['score'])} {fmt(s['score'])} | {s['klaar']} / {s['toepasselijk']} | {s['loopt']} | {s['open']} |")
    tr = M["trend"]
    o += ["", "**Trend (voortgang per maand)**", ""]
    if len(tr["maanden"]) >= 2:
        o.append(f"`{spark(tr['totaal'])}`  " + " → ".join(f"{m} {fmt(v)}" for m, v in zip(tr["maanden"], tr["totaal"])))
    else:
        o.append("De trendlijn verschijnt vanaf de tweede maand met registerdata; er is nu één meetpunt" + (f" ({tr['maanden'][0]}: {fmt(tr['totaal'][0])})." if tr["maanden"] else "."))
    r = M["risicos"]
    o += ["", f"**Open risico's: {r['open']}** — hoog {r['hoog']} · middel {r['middel']} · laag {r['laag']}", "", "**Openstaande taken**", ""]
    if M["taken_open"]:
        o += ["| Taak | Skill | Deadline | Prioriteit |", "|---|---|---|---|"]
        for x in M["taken_open"][:6]:
            o.append(f"| {x['taak']} | {x['skill']} | {x['deadline'] or '—'}{' ⚠️ te laat' if x['te_laat'] else ''} | {x['prioriteit']} |")
    else:
        o.append("Geen open taken in het register.")
    o += ["", "**Recente activiteit**", ""]
    o += [f"- {a['datum']} · {a['skill']} · {a['gebeurtenis']}" + (f" → {a['uitkomst']}" if a["uitkomst"] else "") for a in M["activiteit"][:6]] or ["Nog geen activiteit geregistreerd."]
    o += ["", "**Volgende stappen**", ""]
    o += [f"{i}. {s}" for i, s in enumerate(M["volgende_stappen"][:5], 1)] or ["Geen openstaande punten volgens het register."]
    if M["waarschuwingen"]:
        o += ["", "**Let op**", ""] + [f"- {w}" for w in M["waarschuwingen"]]
    o += ["", "_Voortgang = verplichtingen met status `klaar` gedeeld door het aantal toepasselijke verplichtingen in je eigen register. Het is een voortgangsmaat, geen oordeel over naleving; alle verplichtingen wegen even zwaar._"]
    return "\n".join(o)


# ---------- uitvoer: widgets (HTML-fragment) ----------
COL = {"Privacy": "#FFFF00", "Informatiebeveiliging": "#48CAE4", "AI & cyber": "#e8ecf5", "Contracten": "#aab2c2", "Overig": "#7a8294", "Totaal": "#ffffff"}
DASH = {"Privacy": "", "Informatiebeveiliging": "6 3", "AI & cyber": "2 3", "Contracten": "10 4", "Overig": "1 4"}
# Zelfde look als de site (lichtgrijs met leisteen-glaskaarten); geel (#FFFF00) = voldoet/klaar, blauw (#48CAE4) = voldoet niet/nog te doen.
# Geen groen of rood. Dezelfde tokens als het formulier in kader.py (een test bewaakt dat ze gelijk blijven).
GLAS_TOKENS = ("--g-bg:#f4f6f8;--g-fon:radial-gradient(ellipse 60% 38% at 0 0,rgba(70,82,98,.30),transparent 72%),"
               "radial-gradient(ellipse 50% 40% at 100% 52%,rgba(118,134,152,.34),transparent 70%),"
               "radial-gradient(ellipse 46% 34% at 50% 100%,rgba(176,194,212,.40),transparent 72%),#f4f6f8;"
               "--g-card:rgba(50,54,62,.80);--g-line:rgba(255,255,255,.16);--g-ink:#f5f5f7;"
               "--g-mute:rgba(245,245,247,.62);--g-yes:#FFFF00;--g-no:#48CAE4;--g-out:#0d1117;--g-out2:#3e464f;"
               "--g-sh:0 10px 30px rgba(13,17,23,.18),inset 0 1px 0 rgba(255,255,255,.08);"
               "--g-font:Geist,system-ui,sans-serif")
CSS = """
<style>
.cmp{""" + GLAS_TOKENS + """;position:relative;font:14px/1.45 var(--g-font);letter-spacing:-.006em;color:var(--g-ink);padding:16px 16px 34px;border-radius:24px;background:var(--g-fon)}
.cmp *{box-sizing:border-box}.cmp h1{font-size:22px;font-weight:600;letter-spacing:-.04em;margin:0;color:var(--g-ink)}.cmp h2{font-size:13px;margin:0 0 8px;color:var(--g-mute);font-weight:500}
.cmp .sub{color:var(--g-mute);font-size:12px}
.cmp .card,.cmp .hero{background:var(--g-card);border:1px solid var(--g-line);border-radius:20px;padding:14px 16px;backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);box-shadow:var(--g-sh)}
.cmp .hero{display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap;margin-bottom:12px}
.cmp .grid{display:grid;gap:12px}.cmp .g4{grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}.cmp .g2{grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin-top:12px}
.cmp .big{font-size:30px;font-weight:600;letter-spacing:-.04em;line-height:1.1;color:var(--g-yes)}.cmp .bar{height:7px;border-radius:4px;background:rgba(72,202,228,.45);margin:8px 0 6px;overflow:hidden}.cmp .bar i{display:block;height:100%;border-radius:4px}
.cmp .pill{display:inline-block;border-radius:999px;padding:3px 12px;background:var(--g-yes);color:#0b0b0b;font-weight:600;font-size:12.5px;margin-top:6px}
.cmp table{color:inherit;font:inherit;width:100%;border-collapse:collapse;font-size:13px}.cmp td,.cmp th{padding:6px 4px;text-align:left;border-bottom:1px solid var(--g-line);vertical-align:top}.cmp th{color:var(--g-mute);font-weight:500;font-size:11.5px}
.cmp ul,.cmp ol{margin:0;padding-left:18px}.cmp li{margin:3px 0}.cmp .tag{display:inline-block;padding:0 6px;border-radius:8px;border:1px solid currentColor;font-size:11px}
.cmp .late{color:var(--g-no);font-weight:700;text-decoration:underline}.cmp .empty{color:var(--g-mute);font-style:italic}.cmp .leg{display:flex;gap:12px;flex-wrap:wrap;font-size:12px;margin-top:6px}.cmp .leg svg{vertical-align:middle;margin-right:4px}
.cmp .big.n{color:var(--g-no)}.cmp .pill.n{background:var(--g-no);color:#04222b}.cmp .note{margin-top:12px;font-size:11px;color:var(--g-out2)}.cmp .tm{position:absolute;right:18px;bottom:9px;font-size:10.5px;letter-spacing:.02em;color:var(--g-out2);opacity:.75;pointer-events:none}
</style>"""


def e(s): return html.escape(str(s), quote=True)


def ring(p, size=84):
    r = 34; c = 2 * 3.14159265 * r
    off = c * (1 - (p or 0) / 100)
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 84 84" role="img" aria-label="Voortgang totaal {fmt(p)}">'
            f'<circle cx="42" cy="42" r="{r}" fill="none" stroke="rgba(72,202,228,.55)" stroke-width="9"/>'
            + (f'<circle cx="42" cy="42" r="{r}" fill="none" stroke="#FFFF00" stroke-width="9" stroke-linecap="round" stroke-dasharray="{c:.1f}" stroke-dashoffset="{off:.1f}" transform="rotate(-90 42 42)"/>' if p else '')
            + f'<text x="42" y="47" text-anchor="middle" font-size="16" font-weight="700" fill="#f5f5f7">{fmt(p)}</text></svg>')


def line_chart(tr):
    ms = tr["maanden"]
    W, H, L, R, Tp, B = 560, 200, 38, 26, 10, 26
    if not ms:
        return '<p class="empty">Nog geen verplichtingen in het register; de trendlijn verschijnt zodra er verplichtingen met datums zijn.</p>'
    n = len(ms)
    x = lambda i: L + (W - L - R) * (i / (n - 1) if n > 1 else 0.5)
    y = lambda v: Tp + (H - Tp - B) * (1 - v / 100)
    g = [f'<line x1="{L}" y1="{y(v):.1f}" x2="{W-R}" y2="{y(v):.1f}" stroke="var(--g-line)"/><text x="{L-6}" y="{y(v)+4:.1f}" text-anchor="end" font-size="10" fill="var(--g-mute)">{v}%</text>' for v in (0, 25, 50, 75, 100)]
    for i, m in enumerate(ms):
        if n <= 7 or i % 2 == n % 2 or i == n - 1:
            g.append(f'<text x="{x(i):.1f}" y="{H-8}" text-anchor="middle" font-size="10" fill="var(--g-mute)">{e(m)}</text>')

    def path(vals, col, w, dash=""):
        pts = [(x(i), y(v)) for i, v in enumerate(vals) if v is not None]
        if not pts: return ""
        s = ""
        if len(pts) > 1:
            s += f'<polyline fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" {dash} points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in pts) + '"/>'
        s += "".join(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="{3 if w>2 else 2.2}" fill="{col}"/>' for a, b in pts)
        return s
    for dm, vals in tr["domeinen"].items():
        g.append(path(vals, COL.get(dm, "#b8bfcc"), 1.8, f'stroke-dasharray="{DASH.get(dm, "")}"' if DASH.get(dm) else ""))
    g.append(path(tr["totaal"], "#ffffff", 2.8))
    sw = lambda col, da: f'<svg width="22" height="8" viewBox="0 0 22 8"><line x1="0" y1="4" x2="22" y2="4" stroke="{col}" stroke-width="2.4"' + (f' stroke-dasharray="{da}"' if da else "") + '/></svg>'
    leg = "".join(f'<span>{sw(COL.get(dm, "#b8bfcc"), DASH.get(dm, ""))}{e(dm)}</span>' for dm in tr["domeinen"]) + f'<span>{sw("#ffffff", "")}<b>Totaal</b></span>'
    note = '' if n > 1 else '<p class="sub">Eén meetpunt: de lijn verschijnt vanaf de tweede maand.</p>'
    return f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Voortgang per maand">{"".join(g)}</svg><div class="leg">{leg}</div>{note}'


def donut(r):
    tot = r["open"]
    if not tot:
        return '<p class="empty">Geen open risico\'s in het register.</p>'
    segs = [("hoog", r["hoog"], "#48CAE4"), ("middel", r["middel"], "#FFFF00"), ("laag", r["laag"], "rgba(255,255,0,.5)")]
    rr = 38; c = 2 * 3.14159265 * rr; off = 0; parts = []
    for nm, n, col in segs:
        if not n: continue
        ln = c * n / tot
        parts.append(f'<circle cx="50" cy="50" r="{rr}" fill="none" stroke="{col}" stroke-width="14" stroke-dasharray="{ln:.1f} {c-ln:.1f}" stroke-dashoffset="{-off:.1f}" transform="rotate(-90 50 50)"/>')
        off += ln
    leg = "".join(f'<li><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:{col};border:1px solid rgba(255,255,255,.5);vertical-align:-1px;margin-right:6px"></span>{nm}: <b>{n}</b></li>' for nm, n, col in segs)
    return (f'<div style="display:flex;gap:14px;align-items:center"><svg width="110" height="110" viewBox="0 0 100 100" role="img" aria-label="{tot} open risico\'s">{"".join(parts)}'
            f'<text x="50" y="56" text-anchor="middle" font-size="20" font-weight="700" fill="#f5f5f7">{tot}</text></svg><ul style="list-style:none;padding:0">{leg}</ul></div>')


def html_out(M):
    if M["leeg"]:
        return CSS + f'<div class="cmp"><div class="hero"><div><h1>Overzicht{" — " + e(M["organisatie"]) if M["organisatie"] else ""}</h1><div class="sub">Peildatum {e(M["peildatum"])}</div></div></div><div class="card"><p class="empty">Het register is nog leeg, dus er is niets om te berekenen. Draai <b>/compliance-onboarding</b> om je profiel en verplichtingen vast te leggen.</p></div><small class="tm">Lawskills&trade;</small></div>'
    t = M["totaal"]
    cards = ""
    for dm, s in M["domeinen"].items():
        col = COL.get(dm, "#777")
        cards += (f'<div class="card"><h2>{e(dm)}</h2><div class="big{"" if s["score"] else " n"}">{fmt(s["score"])}</div>'
                  f'<div class="bar"><i style="width:{s["score"] or 0}%;background:var(--g-yes)"></i></div>'
                  f'<div class="sub">{s["klaar"]} van {s["toepasselijk"]} klaar · {s["loopt"]} loopt · {s["open"]} open</div></div>')
    taken = "".join(f'<tr><td>{e(x["taak"])}<div class="sub">/{e(x["skill"])}</div></td><td class="{"late" if x["te_laat"] else ""}">{e(x["deadline"] or "—")}{" (te laat)" if x["te_laat"] else ""}</td><td>{e(x["prioriteit"])}</td></tr>' for x in M["taken_open"][:6])
    taken = f'<table><tr><th>Taak</th><th>Deadline</th><th>Prio</th></tr>{taken}</table>' if taken else '<p class="empty">Geen open taken in het register.</p>'
    act = "".join(f'<li><span class="sub">{e(a["datum"])}</span> · {e(a["gebeurtenis"])}' + (f' <span class="sub">→ {e(a["uitkomst"])}</span>' if a["uitkomst"] else "") + f' <span class="sub">(/{e(a["skill"])})</span></li>' for a in M["activiteit"][:6])
    act = f"<ul>{act}</ul>" if act else '<p class="empty">Nog geen activiteit geregistreerd.</p>'
    st = "".join(f"<li>{e(s)}</li>" for s in M["volgende_stappen"][:6])
    st = f"<ol>{st}</ol>" if st else '<p class="empty">Geen openstaande punten volgens het register.</p>'
    warn = "".join(f"<li>{e(w)}</li>" for w in M["waarschuwingen"])
    warn = f'<div class="card" style="margin-top:12px"><h2>Let op</h2><ul>{warn}</ul></div>' if warn else ""
    return (CSS + f'<div class="cmp"><div class="hero"><div><h1>Overzicht{" — " + e(M["organisatie"]) if M["organisatie"] else ""}</h1>'
            f'<div class="sub">Peildatum {e(M["peildatum"])} · {t["klaar"]} van {t["toepasselijk"]} toepasselijke verplichtingen klaar · {t["loopt"]} loopt · {t["open"]} open</div><span class="pill{"" if t["score"] else " n"}">{fmt(t["score"])} klaar</span></div>{ring(t["score"])}</div>'
            f'<div class="grid g4">{cards}</div>'
            f'<div class="card" style="margin-top:12px"><h2>Voortgang per maand</h2>{line_chart(M["trend"])}</div>'
            f'<div class="grid g2"><div class="card"><h2>Risico\'s (open)</h2>{donut(M["risicos"])}</div><div class="card"><h2>Volgende stappen</h2>{st}</div></div>'
            f'<div class="grid g2"><div class="card"><h2>Openstaande taken</h2>{taken}</div><div class="card"><h2>Recente activiteit</h2>{act}</div></div>{warn}'
            f'<p class="note">Voortgang = verplichtingen met status klaar ÷ toepasselijke verplichtingen in je eigen register; alle verplichtingen wegen even zwaar. Het is een voortgangsmaat, geen oordeel over naleving of juridisch advies. Kleur: geel = klaar, blauw = nog te doen; de tekst erbij zegt hetzelfde.</p><small class="tm">Lawskills&trade;</small></div>')


# ---------- volledig register tonen ----------
def show(path, sectie=None, status=None, domein=None):
    """Het hele register als Markdown-tabellen, zoals het in het bestand staat (geen berekeningen, niets weggelaten).
    Filters: sectie (profiel|verplichtingen|taken|risicos|activiteit), status, domein (alleen verplichtingen)."""
    tabs = parse_tables(read(path))
    out = []
    for key, (titel, kolommen) in SECTIES.items():
        if sectie and key != sectie:
            continue
        rijen = tabs.get(norm(titel), [])
        if status:
            rijen = [x for x in rijen if x.get("status", "").lower() == status.lower()] if key in ("verplichtingen", "taken", "risicos") else rijen
        if domein and key == "verplichtingen":
            rijen = [x for x in rijen if x.get("domein", "").lower() == domein.lower()]
        elif domein and key != "verplichtingen":
            continue
        if status and key in ("profiel", "activiteit"):
            continue
        out.append(f"## {titel} ({len(rijen)})")
        if not rijen:
            out.append("_Geen regels in het register._")
            out.append("")
            continue
        out.append("| " + " | ".join(kolommen) + " |")
        out.append("|" + "|".join("---" for _ in kolommen) + "|")
        for x in rijen:
            out.append("| " + " | ".join(clean(x.get(norm(k), "")) or "–" for k in kolommen) + " |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


# ---------- cli ----------
def main(a):
    if len(a) < 2 or a[0] in ("-h", "--help"):
        print(__doc__); return 0
    cmd, path = a[0], a[1]
    rest = a[2:]
    today = datetime.date.today()
    org = ""
    if "--today" in rest:
        i = rest.index("--today"); today = datetime.date.fromisoformat(rest[i + 1]); del rest[i:i + 2]
    if "--org" in rest:
        i = rest.index("--org"); org = rest[i + 1]; del rest[i:i + 2]
    if cmd == "init":
        import os
        if os.path.exists(path): raise SystemExit(f"{path} bestaat al; niet overschreven")
        open(path, "w", encoding="utf-8").write(template(org, today)); print(f"Register aangemaakt: {path}")
    elif cmd == "metrics":
        print(json.dumps(compute(path, today), ensure_ascii=False, indent=1))
    elif cmd == "html":
        print(html_out(compute(path, today)))
    elif cmd == "show":
        f = {}
        for k in ("--sectie", "--status", "--domein"):
            if k in rest:
                i = rest.index(k); f[k[2:]] = norm(rest[i + 1]) if k == "--sectie" else rest[i + 1]; del rest[i:i + 2]
        if f.get("sectie") and f["sectie"] not in SECTIES: raise SystemExit(f"Onbekende sectie {f['sectie']}; kies uit {list(SECTIES)}")
        print(show(path, f.get("sectie"), f.get("status"), f.get("domein")))
    elif cmd == "text":
        print(text(compute(path, today)))
    elif cmd == "validate":
        errs = validate(path)
        print("\n".join(errs) if errs else "Register is geldig.")
        return 1 if errs else 0
    elif cmd in ("add", "set"):
        sectie = norm(rest[0])
        if sectie not in SECTIES: raise SystemExit(f"Onbekende sectie {rest[0]}; kies uit {list(SECTIES)}")
        if cmd == "add":
            kv = dict(x.split("=", 1) for x in rest[1:]); print(add_row(path, sectie, kv, str(today)))
        else:
            kv = dict(x.split("=", 1) for x in rest[2:]); print(set_row(path, sectie, rest[1], kv))
    else:
        raise SystemExit(f"Onbekend commando {cmd}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
