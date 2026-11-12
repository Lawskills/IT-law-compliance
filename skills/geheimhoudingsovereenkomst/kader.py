#!/usr/bin/env python3
"""kader.py — vaste rekenregels voor de kaders van compliance-skills.

Het taalmodel beoordeelt de inhoud van een toetspunt; dit script doet de rest,
zodat elke skill dezelfde logica volgt en er geen stappen worden overgeslagen:

  vragen     de volgende golf: alle vragen die nu nodig zijn, gebundeld in aanroepen van hooguit 4 velden
             (ja/nee-vragen als afvinklijst van 3), plus wat er na deze golf nog kan volgen
  stappen    per toetspunt: geldt / n.v.t. / onzeker en welke antwoorden ontbreken
  uitkomst   past de plafonds toe op de oordelen en berekent de kaderuitkomst
  samenhang  welke vervolgkaders of skills volgens de antwoorden in beeld komen
  document   zet de kaderteksten van een opstel-kader samen met [IN TE VULLEN: …] voor wat ontbreekt
  voorstel   stelt antwoorden voor uit het profiel van compliance-register.md (ter bevestiging)
  info       kader-id, versie, peildatum, aantal vragen en toetspunten
  check      controleert de structuur van een kaderbestand (voor onderhoud)

Meerdere kaders tegelijk: geef meer kaderbestanden mee, een map, of 'alle' (alle kaders van de skill
waarin dit script staat, in de volgorde van SKILL.md). Dan gelden één set antwoorden en één set oordelen voor alle kaders: een vraag die
in meer kaders staat wordt één keer gesteld, en een poortregel ('Geldt alleen als' bovenaan een kader)
laat een kader vervallen als een antwoord uit een eerder kader dat zegt. Zo is een skill met vijf kaders
in zo weinig golven mogelijk klaar.

Datums: 'Van toepassing vanaf' (kader) of '- Geldt vanaf' (toetspunt). Is die datum nog niet bereikt,
dan wordt een ❌ een ⚠️ (voorbereidingspunt met de datum); hangt de datum af van een onbekend antwoord,
dan ook. Vandaag = de systeemdatum, of --datum JJJJ-MM-DD.

Antwoorden:  --antwoorden antwoorden.json  of losse  sleutel=waarde  argumenten.
  Waarden: true/false, getallen, tekst. Onbekend = ontbreekt, null, "", "weet ik niet" of "onbekend".
Oordelen:    --oordelen oordelen.json  {"K2.1": "compliant" | "review" | "non_compliant" | "not_applicable", ...}
             (ook ✅ ⚠️ ❌ n.v.t. worden herkend). n.v.t. op grond van een kaderregel geef je mee als
             {"K6.3": {"uitkomst": "n.v.t.", "reden": "regel: stap 1 afwezig → stap 2-7 n.v.t."}}

Logica bij onbekend (drie waarden: ja / nee / onbekend):
  * een vergelijking met een onbekend antwoord is onbekend; `== null` is ja als het antwoord onbekend is;
  * `and` is nee als een deel nee is, anders onbekend als een deel onbekend is, anders ja;
  * `or` is ja als een deel ja is, anders onbekend als een deel onbekend is, anders nee;
  * voorwaarde ja → de stap geldt; nee → n.v.t.; onbekend → de stap geldt en voldoet niet tot het antwoord is ingevuld
    (een stap die niet meetelt: ⚠️ in te vullen).
  * een vraag wordt gesteld als haar voorwaarde ja of onbekend is;
  * een documenttekst wordt opgenomen als haar voorwaarde ja is, en bij onbekend met een [IN TE VULLEN]-markering;
  * n.v.t. ontstaat alleen door een onware voorwaarde, door een kaderregel (met reden) of bij een
    kwalificatiestap ('bij afwezig: n.v.t.'); in dat laatste geval gelden de regels van het kader niet (kader n.v.t.);
  * een poortregel die onwaar is maakt het hele kader n.v.t.; is de poortstap van het eerdere kader niet ✅,
    dan vervalt het kader niet (het is dan niet uitgesloten) en wordt het ⚠️;
  * een poortregel die onbekend is, laat het kader gewoon gelden.

Alleen standaardbibliotheek; Python 3.8+.
"""
import argparse
import datetime as _dt
import html
import json
import re
import sys
from pathlib import Path

UNKNOWN = None  # onbekend in de drie-waardenlogica


class _NVT:
    """Antwoord op een vraag die niet van toepassing was: elke vergelijking ermee is onwaar."""
    def __repr__(self):
        return "n.v.t."


NVT = _NVT()
UNKNOWN_STRINGS = {"", "weet ik niet", "onbekend", "unknown", "?", "n.b.", "nb"}
OUTCOME_ALIASES = {
    "compliant": "compliant", "✅": "compliant", "voldoet": "compliant", "ja": "compliant",
    "review": "review", "⚠️": "review", "⚠": "review", "te beoordelen": "review", "in te vullen": "review",
    "non_compliant": "non_compliant", "❌": "non_compliant", "voldoet niet": "non_compliant", "nee": "non_compliant",
    "not_applicable": "not_applicable", "n.v.t.": "not_applicable", "nvt": "not_applicable", "n.v.t": "not_applicable",
}
ORDER = {"not_applicable": -1, "compliant": 0, "review": 1, "non_compliant": 2}
SYMBOL = {"compliant": "✅", "review": "⚠️", "non_compliant": "❌", "not_applicable": "n.v.t."}
LABEL = {"compliant": "voldoet", "review": "in te vullen", "non_compliant": "voldoet niet", "not_applicable": "n.v.t."}


# ---------------------------------------------------------------- expressies
TOKEN_RE = re.compile(r"""\s*(?:
    (?P<lp>\()|(?P<rp>\))|
    (?P<op>==|!=|>=|<=|>|<)|
    (?P<kw>\band\b|\bor\b|\bnot\b)|
    (?P<fact>facts\.[a-z0-9_]+)|
    (?P<str>"[^"]*")|
    (?P<num>-?\d+(?:\.\d+)?)|
    (?P<lit>\btrue\b|\bfalse\b|\bnull\b)
)""", re.X)


def tokenize(expr):
    pos, out = 0, []
    expr = expr.strip()
    while pos < len(expr):
        m = TOKEN_RE.match(expr, pos)
        if not m or m.end() == pos:
            raise ValueError(f"onbekend teken in voorwaarde bij positie {pos}: {expr[pos:pos+25]!r}")
        kind = m.lastgroup
        val = m.group(kind)
        out.append((kind, val))
        pos = m.end()
        while pos < len(expr) and expr[pos].isspace():
            pos += 1
    return out


class Parser:
    """Grammatica:  or_expr := and_expr ('or' and_expr)* ; and_expr := not_expr ('and' not_expr)* ;
    not_expr := 'not' not_expr | atom ; atom := '(' or_expr ')' | operand op operand."""

    def __init__(self, expr):
        self.expr = expr
        self.toks = tokenize(expr)
        self.i = 0

    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else (None, None)

    def take(self, kind=None, val=None):
        k, v = self.peek()
        if k is None or (kind and k != kind) or (val and v != val):
            raise ValueError(f"verwacht {val or kind}, kreeg {v!r} in: {self.expr}")
        self.i += 1
        return v

    def parse(self):
        node = self.or_expr()
        if self.i != len(self.toks):
            raise ValueError(f"rest na voorwaarde: {self.toks[self.i:]} in: {self.expr}")
        return node

    def or_expr(self):
        parts = [self.and_expr()]
        while self.peek() == ("kw", "or"):
            self.take()
            parts.append(self.and_expr())
        return ("or", parts) if len(parts) > 1 else parts[0]

    def and_expr(self):
        parts = [self.not_expr()]
        while self.peek() == ("kw", "and"):
            self.take()
            parts.append(self.not_expr())
        return ("and", parts) if len(parts) > 1 else parts[0]

    def not_expr(self):
        if self.peek() == ("kw", "not"):
            self.take()
            return ("not", self.not_expr())
        return self.atom()

    def operand(self):
        k, v = self.peek()
        self.i += 1
        if k == "fact":
            return ("fact", v[6:])
        if k == "str":
            return ("lit", v[1:-1])
        if k == "num":
            return ("lit", float(v) if "." in v else int(v))
        if k == "lit":
            return ("lit", {"true": True, "false": False, "null": "__null__"}[v])
        raise ValueError(f"verwacht feit of waarde, kreeg {v!r} in: {self.expr}")

    def atom(self):
        if self.peek()[0] == "lit" and (self.i + 1 >= len(self.toks) or self.toks[self.i + 1][0] in ("kw", "rp")):
            v = self.take("lit")
            return ("const", {"true": True, "false": False}.get(v))
        if self.peek()[0] == "lp":
            self.take("lp")
            node = self.or_expr()
            self.take("rp")
            return node
        left = self.operand()
        op = self.take("op")
        right = self.operand()
        return ("cmp", op, left, right)


def parse_expr(expr):
    return Parser(expr).parse()


def facts_in(node):
    if node[0] == "const":
        return set()
    if node[0] == "cmp":
        return {x[1] for x in node[2:] if x[0] == "fact"}
    if node[0] in ("and", "or"):
        return set().union(*(facts_in(p) for p in node[1]))
    if node[0] == "not":
        return facts_in(node[1])
    return set()


def literals_for(node, acc=None):
    """Geeft {feit: {waarden waarmee het wordt vergeleken}}."""
    acc = {} if acc is None else acc
    if node[0] == "cmp":
        _, op, a, b = node
        if a[0] == "fact" and b[0] == "lit":
            acc.setdefault(a[1], set()).add(b[1])
        if b[0] == "fact" and a[0] == "lit":
            acc.setdefault(b[1], set()).add(a[1])
    elif node[0] in ("and", "or"):
        for p in node[1]:
            literals_for(p, acc)
    elif node[0] == "not":
        literals_for(node[1], acc)
    return acc


def norm_value(v):
    if v is NVT:
        return NVT
    if v is None:
        return UNKNOWN
    if isinstance(v, str):
        s = v.strip()
        low = s.lower()
        if low in UNKNOWN_STRINGS:
            return UNKNOWN
        if low in ("true", "ja", "yes"):
            return True
        if low in ("false", "nee", "no"):
            return False
        if re.fullmatch(r"-?\d+", s):
            return int(s)
        if re.fullmatch(r"-?\d+\.\d+", s):
            return float(s)
        return s
    return v


def evaluate(node, facts):
    """Drie-waardenlogica: True, False of None (onbekend)."""
    t = node[0]
    if t == "or":
        vals = [evaluate(p, facts) for p in node[1]]
        if True in vals:
            return True
        return UNKNOWN if UNKNOWN in vals else False
    if t == "and":
        vals = [evaluate(p, facts) for p in node[1]]
        if False in vals:
            return False
        return UNKNOWN if UNKNOWN in vals else True
    if t == "const":
        return node[1]
    if t == "not":
        v = evaluate(node[1], facts)
        return UNKNOWN if v is UNKNOWN else (not v)
    _, op, a, b = node

    def val(x):
        return norm_value(facts.get(x[1])) if x[0] == "fact" else x[1]

    va, vb = val(a), val(b)
    if va is NVT or vb is NVT:
        return False
    if vb == "__null__" or va == "__null__":
        other = va if vb == "__null__" else vb
        isnull = other is UNKNOWN
        return isnull if op == "==" else (not isnull)
    if va is UNKNOWN or vb is UNKNOWN:
        return UNKNOWN
    try:
        if op == "==":
            return va == vb
        if op == "!=":
            return va != vb
        if op == ">=":
            return va >= vb
        if op == "<=":
            return va <= vb
        if op == ">":
            return va > vb
        if op == "<":
            return va < vb
    except TypeError:
        return UNKNOWN
    raise ValueError(op)


# ---------------------------------------------------------------- parser kaderbestand
BT = "`"


def _field(line, name):
    p = f"- {name}:"
    return line[len(p):].strip() if line.startswith(p) else None


def _cond(text, label):
    m = re.search(re.escape(label) + r":\s*`([^`]*)`", text)
    return m.group(1).strip() if m else None


DATE_RE = re.compile(r"^\s*(\d{4}-\d{2}-\d{2})(?:\s+als\s+`([^`]*)`)?\s*$")


def parse_dates(text, errors=None, where=""):
    """'2027-12-02 als `facts.x == "a"`; 2028-08-02' → [(date, expr|None), ...] (volgorde telt)."""
    out = []
    for part in [x for x in (text or "").split(";") if x.strip()]:
        m = DATE_RE.match(part)
        if not m:
            if errors is not None:
                errors.append(f"{where}: datumregel niet herkend: {part.strip()!r}")
            continue
        try:
            d = _dt.date.fromisoformat(m.group(1))
        except ValueError:
            if errors is not None:
                errors.append(f"{where}: ongeldige datum {m.group(1)}")
            continue
        out.append((d, m.group(2).strip() if m.group(2) else None))
    return out


def parse_kader(path):
    path = Path(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    k = {"file": path.name, "path": str(path), "questions": [], "steps": [], "doc_items": [],
         "samenhang": [], "qualification": [], "errors": [], "gate": None, "poortstap": None, "dates": [],
         "vervalt_als_nvt": []}
    m = re.match(r"# Kader (\S+) — (.+)", lines[0] if lines else "")
    if not m:
        k["errors"].append("eerste regel is geen '# Kader <ID> — <titel>'")
        k["id"], k["title"] = path.stem, path.stem
    else:
        k["id"], k["title"] = m.group(1), m.group(2).strip()
    for ln in lines[1:6]:
        mv = re.match(r"Versie (\S+) · peildatum (\d{4}-\d{2}-\d{2})", ln)
        if mv:
            k["version"], k["peildatum"] = mv.group(1), mv.group(2)
    for ln in lines[1:]:
        if ln.startswith("## "):
            break
        if ln.startswith("Geldt alleen als:"):
            mg = re.match(r"Geldt alleen als: `([^`]*)`(?:\s*·\s*poortstap (\S+))?", ln)
            if mg:
                k["gate"], k["poortstap"] = mg.group(1).strip(), mg.group(2)
            else:
                k["errors"].append("regel 'Geldt alleen als' niet herkend")
        elif ln.startswith("Vervalt als kader"):
            k["vervalt_als_nvt"] = re.findall(r"\b([A-Z]+[0-9]+[a-z]?)\b", ln.split("n.v.t.")[0][len("Vervalt als kader"):])
        elif ln.startswith("Van toepassing vanaf:"):
            k["dates"] = parse_dates(ln.split(":", 1)[1].split(" — ")[0], k["errors"], "Van toepassing vanaf")
    section = None
    cur_q = cur_s = cur_d = None
    onderdeel = None
    in_fence = False
    fence_buf = []
    sub = None
    for raw in lines:
        if raw.startswith("````"):
            if in_fence:
                if cur_d is not None:
                    cur_d["text"] = "\n".join(fence_buf)
                fence_buf = []
            in_fence = not in_fence
            continue
        if in_fence:
            fence_buf.append(raw)
            continue
        if raw.startswith("## "):
            title = raw[3:].strip()
            if title.startswith("Formulier"):
                section = "form"
            elif title.startswith("Opbouw"):
                section = "doc"
            elif title.startswith("Toetspunten (voor de eindcontrole)"):
                section = "doc_checks"
            elif title.startswith("Toetspunten"):
                section = "steps"
            elif title.startswith("Samenhang"):
                section = "samenhang"
            elif title.startswith("Vragen waarop"):
                section = "qual"
            elif title.startswith("Regels van dit kader"):
                section = "rules"
            else:
                section = "other"
            cur_q = cur_s = None
            continue
        if section == "form":
            mq = re.match(r"- \*\*([a-z0-9_]+)\*\*: (.+)", raw)
            if mq:
                cur_q = {"key": mq.group(1), "vraag": mq.group(2).strip(), "type": None, "options": [],
                         "ask_if": None, "label": None, "hulp": None, "eigen_org": False, "uit_register": False}
                k["questions"].append(cur_q)
                continue
            if cur_q and raw.startswith("  - "):
                body = raw[4:]
                if body.startswith("Label"):
                    cur_q["label"] = body.split(":", 1)[1].strip()
                elif body.startswith("Hulp:"):
                    cur_q["hulp"] = body[5:].strip()
                elif body.startswith("Type:"):
                    t = body[5:].strip()
                    mt = re.match(r"(boolean|text|enum|number)\b\s*(\(([^)]*)\))?", t)
                    if not mt:
                        k["errors"].append(f"{cur_q['key']}: onbekend type '{t}'")
                    else:
                        cur_q["type"] = mt.group(1)
                        if mt.group(1) == "enum":
                            cur_q["options"] = [o.strip() for o in (mt.group(3) or "").split("/") if o.strip()]
                    cur_q["ask_if"] = _cond(t, "Alleen vragen als")
                    cur_q["eigen_org"] = "Hoort bij je eigen organisatie" in t
                    cur_q["uit_register"] = "verwerkingsregister" in t
        elif section == "steps":
            ms = re.match(r"### (\S+) — (.+)", raw)
            if ms:
                cur_s = {"id": ms.group(1), "title": ms.group(2).strip(), "kind": None, "counts": True,
                         "applies_if": None, "needed": [], "absent": None, "max": None, "grondslag": None,
                         "vraag": None, "advies": None, "text": [], "dates": []}
                k["steps"].append(cur_s)
                sub = None
                continue
            if cur_s is None:
                continue
            cur_s["text"].append(raw)
            v = _field(raw, "Soort")
            if v is not None:
                cur_s["kind"] = "F" if "(F)" in v else ("A" if "(A)" in v else None)
                cur_s["counts"] = "telt niet mee" not in v
            v = _field(raw, "Alleen als")
            if v is not None:
                cur_s["applies_if"] = _cond(raw, "Alleen als")
            v = _field(raw, "Nodig")
            if v is not None:
                cur_s["needed"] = [x.strip() for x in v.split(",") if x.strip()]
            v = _field(raw, "Is het vereiste afwezig (*absent*)")
            if v is not None:
                cur_s["absent"] = OUTCOME_ALIASES.get(v.strip(), v.strip())
            v = _field(raw, "Hoogste uitkomst")
            if v is not None:
                cur_s["max"] = "review"
            v = _field(raw, "Grondslag")
            if v is not None:
                cur_s["grondslag"] = v
            v = _field(raw, "Geldt vanaf")
            if v is not None:
                cur_s["dates"] = parse_dates(v.split(" — ")[0], k["errors"], f"toetspunt {cur_s['id']}")
            v = _field(raw, "Bij ⚠️ stel je de gebruiker deze vraag")
            if v is not None:
                cur_s["vraag"] = v
            v = _field(raw, "Advies bij ❌ of ⚠️")
            if v is not None:
                cur_s["advies"] = v
            if "Deze stap geeft altijd review" in raw or "Signalerende stap" in raw:
                cur_s["max"] = "review"
        elif section == "doc":
            mo = re.match(r"### \d+\. Onderdeel `([^`]+)` \(standaardkop: (.+)\)", raw)
            if mo:
                onderdeel = {"key": mo.group(1), "kop": mo.group(2).strip()}
                continue
            mi = re.match(r"#### (\S+) — (.+)", raw)
            if mi:
                cur_d = {"id": mi.group(1), "title": mi.group(2).strip(), "onderdeel": onderdeel,
                         "include_if": None, "needed": [], "soort": None, "text": None, "grondslag": None}
                k["doc_items"].append(cur_d)
                continue
            if cur_d is not None:
                if raw.startswith("- Tekstsoort:"):
                    ms2 = re.search(r"`([a-z_]+)`", raw)
                    cur_d["soort"] = ms2.group(1) if ms2 else None
                    cur_d["include_if"] = _cond(raw, "Alleen opnemen als")
                    mn = re.search(r"Nodig: ([a-z0-9_, ]+)", raw)
                    if mn:
                        cur_d["needed"] = [x.strip() for x in mn.group(1).split(",") if x.strip()]
                v = _field(raw, "Grondslag")
                if v is not None:
                    cur_d["grondslag"] = v
        elif section == "doc_checks":
            ms = re.match(r"### (\S+) — (.+)", raw)
            if ms:
                cur_s = {"id": ms.group(1), "title": ms.group(2).strip(), "applies_if": None, "doc_check": True,
                         "kind": None, "counts": True, "needed": [], "absent": None, "max": None, "text": []}
                k["steps"].append(cur_s)
                continue
            if cur_s is not None:
                cur_s["text"].append(raw)
                if raw.startswith("- Alleen als:"):
                    cur_s["applies_if"] = _cond(raw, "Alleen als")
                v = _field(raw, "Grondslag")
                if v is not None:
                    cur_s["grondslag"] = v
        elif section == "samenhang":
            mh = re.match(r"- Kader (\S+) \((/[a-z0-9-]+)\)(?: — als `([^`]*)`)?:? ?(.*)", raw)
            if mh:
                k["samenhang"].append({"kader": mh.group(1), "skill": mh.group(2)[1:], "cond": mh.group(3),
                                       "waarom": mh.group(4).strip()})
            elif re.match(r"- Kader (\S+) \(geen eigen skill", raw):
                mx = re.match(r"- Kader (\S+) \(geen eigen skill[^)]*\)(?: — als `([^`]*)`)?:? ?(.*)", raw)
                k["samenhang"].append({"kader": mx.group(1), "skill": None, "cond": mx.group(2), "waarom": mx.group(3).strip()})
            elif raw.startswith("- "):
                k["samenhang"].append({"kader": None, "skill": None, "cond": None, "waarom": raw[2:], "raw": raw})
        elif section == "qual":
            mm = re.search(r"kwalificatievraag\):\s*([a-z0-9_, ]+)\.", raw)
            if mm:
                k["qualification"] = [x.strip() for x in mm.group(1).split(",") if x.strip()]
    k["kind"] = "document" if (k["doc_items"] or any(s.get("doc_check") for s in k["steps"])) else "toets"
    return k


# ---------------------------------------------------------------- logica
def _read_json_arg(value):
    """Een JSON-bestand of JSON-tekst (ook lange tekst, die geen bestandsnaam kan zijn)."""
    v = value.strip()
    if v.startswith("{") or v.startswith("["):
        return json.loads(v)
    p = Path(value)
    try:
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except OSError:
        pass
    return json.loads(v)


def load_answers(args):
    facts = {}
    if getattr(args, "antwoorden", None):
        facts.update(_read_json_arg(args.antwoorden))
    for kv in getattr(args, "kv", []) or []:
        if "=" not in kv:
            sys.exit(f"argument '{kv}' is geen sleutel=waarde")
        key, val = kv.split("=", 1)
        facts[key.strip()] = val
    return {k: norm_value(v) for k, v in facts.items()}


def is_answered(key, facts):
    return key in facts and facts[key] is not UNKNOWN


def cond_value(expr, facts):
    if not expr:
        return True
    return evaluate(parse_expr(expr), facts)


def _as_list(kaders):
    return [kaders] if isinstance(kaders, dict) else list(kaders)


def gate_state(k, eff, facts, all_keys, skipped=()):
    """Poortregel van een kader: True / False / UNKNOWN / 'pending' (wacht op een antwoord) /
    'ignored' (het antwoord hoort bij een kader dat niet meedoet en is niet gegeven)."""
    expr = k.get("gate")
    if not expr:
        return True, []
    node = parse_expr(expr)
    fs = facts_in(node)
    outside = [f for f in fs if f not in all_keys and f not in facts]
    if outside and len(outside) == len(fs):
        return "ignored", sorted(outside)
    v = evaluate(node, eff)
    if v is UNKNOWN:
        waiting = sorted(f for f in fs if f in all_keys and f not in facts and f not in skipped)
        if waiting:
            return "pending", waiting
    return v, []


def resolve_multi(kaders, facts):
    """Loopt alle vragen van de kaders in volgorde langs (één set antwoorden). Een vraag die in meer kaders
    staat, wordt één keer gesteld. Geeft (eff, vervallen, nu, wacht, poorten)."""
    kaders = _as_list(kaders)
    eff = dict(facts)
    status, skipped, now, pending, gates = {}, [], [], [], {}
    all_keys = {q["key"] for k in kaders for q in k["questions"]}
    for k in kaders:
        g, gw = gate_state(k, eff, facts, all_keys, set(skipped))
        gates[k["id"]] = (g, gw)
        for q in k["questions"]:
            key = q["key"]
            prev = status.get(key)
            if prev in ("now", "pending"):
                continue
            if g is False:
                c = False
            elif g == "pending":
                c = "pending"
            else:
                c = cond_value(q["ask_if"], eff)
            if c is False:
                if prev is None:
                    status[key] = "skipped"
                    skipped.append(key)
                    eff[key] = NVT
                continue
            if prev == "skipped":  # in een eerder kader vervallen, hier wel nodig
                skipped.remove(key)
                eff.pop(key, None)
                if key in facts:
                    eff[key] = facts[key]
            if c == "pending":
                pending.append((q, gw, k["id"]))
                status[key] = "pending"
                continue
            if c is UNKNOWN:
                waiting = [f for f in facts_in(parse_expr(q["ask_if"])) if f not in facts and f not in skipped]
                if waiting:
                    pending.append((q, waiting, k["id"]))
                    status[key] = "pending"
                    continue
            now.append((q, c, k["id"]))
            status[key] = "now"
    return eff, skipped, now, pending, gates


def resolve(k, facts):
    """Eén kader: (eff, vervallen, [(vraag, voorwaarde)], [(vraag, wacht_op)])."""
    eff, skipped, now, pending, _ = resolve_multi([k], facts)
    return eff, skipped, [(q, c) for q, c, _ in now], [(q, w) for q, w, _ in pending]


def unlock_counts(kaders, facts):
    """Per vraag: hoeveel nog niet beantwoorde vragen (direct of via een poortregel) ervan afhangen."""
    deps = {}
    for k in _as_list(kaders):
        gfs = facts_in(parse_expr(k["gate"])) if k.get("gate") else set()
        for q in k["questions"]:
            fs = set(gfs) | (facts_in(parse_expr(q["ask_if"])) if q["ask_if"] else set())
            for f in fs:
                deps.setdefault(f, set()).add(q["key"])
    memo = {}

    def closure(f, stack=()):
        if f in memo:
            return memo[f]
        out = set()
        for d in deps.get(f, ()):
            if d in stack or d in facts:
                continue
            out.add(d)
            out |= closure(d, stack + (f,))
        memo[f] = out
        return out

    return {f: len(closure(f)) for f in deps}


def open_questions(kaders, facts, include_answered=False, prioritize=True):
    kaders = _as_list(kaders)
    eff, skipped, now, pending, gates = resolve_multi(kaders, facts)
    qual = set().union(*(set(k["qualification"]) for k in kaders)) if kaders else set()
    out = []
    for q, c, kid in now:
        if q["key"] in facts and not include_answered:
            continue  # beantwoord, ook als het antwoord 'weet ik niet' was
        out.append({
            "key": q["key"], "vraag": q["vraag"], "type": q["type"],
            "opties": q["options"] or None, "hulp": q["hulp"], "label": q["label"],
            "weet_ik_niet_mag": q["key"] not in qual,
            "eigen_organisatie": q["eigen_org"], "kader": kid,
        })
    if prioritize and len(out) > 4:
        # vragen die andere vragen ontgrendelen eerst, zodat vervolgvragen een ronde eerder kunnen,
        cnt = unlock_counts(kaders, facts)
        order = {q["key"]: i for i, q in enumerate(out)}
        # en de kwalificatievragen (de basis: wat wordt er getoetst), zodat de context ook vooraan staat
        out.sort(key=lambda q: (0 if (cnt.get(q["key"], 0) > 0 or q["key"] in qual) else 1, order[q["key"]]))
    later = [{"key": q["key"], "wacht_op": w, "kader": kid} for q, w, kid in pending if q["key"] not in facts]
    return out, later, skipped


def today_or(d):
    if isinstance(d, _dt.date):
        return d
    return _dt.date.fromisoformat(d) if d else _dt.date.today()


def date_status(clauses, eff, today):
    """Van welke datum geldt een plicht? → None of {'status': geldt|nog_niet|onzeker, 'vanaf': ..., 'datums': [...]}.
    De eerste datum met een ware voorwaarde (of zonder voorwaarde) beslist; datums met een onbekende
    voorwaarde ervoor tellen als mogelijk."""
    if not clauses:
        return None
    cands = []
    for d, expr in clauses:
        v = cond_value(expr, eff) if expr else True
        if v is True:
            cands.append(d)
            break
        if v is UNKNOWN:
            cands.append(d)
    if not cands:
        return None
    fut = [d for d in cands if d > today]
    st = "nog_niet" if len(fut) == len(cands) else ("geldt" if not fut else "onzeker")
    return {"status": st, "vanaf": min(cands).isoformat(), "datums": sorted({d.isoformat() for d in cands})}


def _combine_dates(a, b):
    if not a:
        return b
    if not b:
        return a
    rank = {"geldt": 0, "onzeker": 1, "nog_niet": 2}
    return a if rank[a["status"]] >= rank[b["status"]] else b


_UNSET = object()


def step_status(k, facts, today=None, eff=None, gate=_UNSET):
    if eff is None or gate is _UNSET:
        eff2, _, _, _, gates = resolve_multi([k], facts)
        eff = eff2 if eff is None else eff
        gate = gates[k["id"]][0] if gate is _UNSET else gate
    today = today_or(today)
    kdate = date_status(k.get("dates"), eff, today)
    res = []
    for s in k["steps"]:
        c = False if gate is False else cond_value(s["applies_if"], eff)
        # een vraag die door een eerder antwoord is vervallen (n.v.t.), ontbreekt niet
        missing = [n for n in s.get("needed", []) if not is_answered(n, facts) and eff.get(n) is not NVT]
        dstat = None
        if c is False:
            status, cap = "nvt", "not_applicable"
        else:
            status = "geldt" if c is True else "onzeker"
            cap = "review" if (c is UNKNOWN or s.get("max") == "review") else None
            if missing and not s.get("doc_check"):
                cap = "review" if cap is None else cap
            dstat = _combine_dates(kdate, date_status(s.get("dates"), eff, today))
        row = {"id": s["id"], "titel": s["title"], "status": status, "soort": s.get("kind"),
               "telt_mee": s.get("counts", True), "hoogste_uitkomst": cap,
               "ontbrekende_antwoorden": missing,
               "uitkomst_bij_afwezig": s.get("absent"), "grondslag": s.get("grondslag")}
        if dstat and dstat["status"] != "geldt":
            row["geldt_vanaf"] = dstat
        if gate is False:
            row["reden"] = "poortregel van dit kader is onwaar"
        res.append(row)
    return res


def _oordeel(raw):
    """Een oordeel is een uitkomst ("compliant", "✅", ...) of {"uitkomst": ..., "reden": ...}."""
    reden = None
    if isinstance(raw, dict):
        reden = (raw.get("reden") or "").strip() or None
        raw = raw.get("uitkomst")
    if raw is None:
        return None, reden
    return OUTCOME_ALIASES.get(str(raw).strip().lower(), OUTCOME_ALIASES.get(str(raw).strip(), str(raw).strip())), reden


def aggregate(k, facts, oordelen, today=None, eff=None, gate=_UNSET, note_unknown=True):
    gw = []
    if eff is None or gate is _UNSET:
        eff2, _, _, _, gates = resolve_multi([k], facts)
        eff = eff2 if eff is None else eff
        if gate is _UNSET:
            gate, gw = gates[k["id"]]
    st = {s["id"]: s for s in step_status(k, facts, today=today, eff=eff, gate=gate)}
    absent_rule = {s["id"]: s.get("absent") for s in k["steps"]}
    rows, notes = [], []
    buiten_toepassing = []
    if gate is False:
        notes.append(f"poortregel onwaar ({k['gate']}): dit kader geldt niet"
                     + (f"; dat staat alleen vast als poortstap {k['poortstap']} ✅ is" if k.get("poortstap") else ""))
    elif gate == "ignored":
        notes.append("poortregel niet toegepast: antwoord ontbreekt op " + ", ".join(gw)
                     + " (draai dit kader samen met het kader waar die vraag in staat)")
    for sid, s in st.items():
        o, reden = _oordeel(oordelen.get(sid))
        if o not in (None, "compliant", "review", "non_compliant", "not_applicable"):
            notes.append(f"{sid}: onbekende uitkomst '{o}' → ⚠️")
            o = "review"
        if s["status"] == "nvt":
            if o not in (None, "not_applicable") and gate is not False:
                notes.append(f"{sid}: voorwaarde onwaar, dus n.v.t. (oordeel genegeerd)")
            o = "not_applicable"
        elif o is None:
            o = "review"
            notes.append(f"{sid}: geen oordeel gegeven → ⚠️")
        # niet ingevuld wat nodig is: een stap die meetelt is ❌ (voldoet niet), een stap die niet
        # meetelt (aanbeveling) is ⚠️ (in te vullen). Signalerende stappen en datums blijven ⚠️.
        open_ = s["status"] != "nvt" and (s["status"] == "onzeker" or bool(s["ontbrekende_antwoorden"]))
        if open_ and sid not in buiten_toepassing and o in ("compliant", "review", "non_compliant"):
            mist = ", ".join(s["ontbrekende_antwoorden"]) or "de vraag of dit toetspunt geldt"
            if s["telt_mee"]:
                if o != "non_compliant":
                    notes.append(f"{sid}: niet ingevuld wat nodig is ({mist}) → ❌ voldoet niet")
                o = "non_compliant"
            elif o != "review":
                notes.append(f"{sid}: aanbeveling, niet ingevuld ({mist}) → ⚠️ in te vullen")
                o = "review"
        elif o == "not_applicable":
            if absent_rule.get(sid) == "not_applicable":
                buiten_toepassing.append(sid)  # kwalificatiestap: vereiste duidelijk afwezig
            elif reden:
                notes.append(f"{sid}: n.v.t. op grond van een regel van dit kader ({reden})")
            else:
                o = "review"
                notes.append(f"{sid}: n.v.t. zonder voorwaarde of kaderregel → ⚠️ (geef een reden mee)")
        if o == "non_compliant" and absent_rule.get(sid) == "not_applicable":
            # bij een kwalificatiestap betekent 'afwezig' dat de regels niet gelden, nooit ❌
            o = "not_applicable"
            buiten_toepassing.append(sid)
        cap = s["hoogste_uitkomst"]
        if cap == "review" and o == "compliant" and not open_:
            reason = []
            if s["status"] == "onzeker":
                reason.append("voorwaarde hangt af van een onbekend antwoord")
            if s["ontbrekende_antwoorden"]:
                reason.append("ontbrekend: " + ", ".join(s["ontbrekende_antwoorden"]))
            if not reason:
                reason.append("signalerende stap")
            o = "review"
            notes.append(f"{sid}: ✅ verlaagd naar ⚠️ ({'; '.join(reason)})")

        gv = s.get("geldt_vanaf")
        if gv and o == "non_compliant":
            o = "review"
            if gv["status"] == "nog_niet":
                notes.append(f"{sid}: ❌ wordt ⚠️: voorbereidingspunt, deze plicht geldt pas vanaf {gv['vanaf']}")
            else:
                notes.append(f"{sid}: ❌ wordt ⚠️: of de plicht al geldt hangt af van een onbekend antwoord "
                             f"(mogelijke datums: {', '.join(gv['datums'])})")
        if sid in buiten_toepassing and s["status"] == "onzeker":
            buiten_toepassing.remove(sid)
            o = "review"
            notes.append(f"{sid}: buiten toepassing hangt af van een onbekend antwoord → ⚠️")
        row = {"id": sid, "titel": s["titel"], "uitkomst": o, "symbool": SYMBOL[o], "label": LABEL[o], "telt_mee": s["telt_mee"]}
        if gv:
            row["geldt_vanaf"] = gv["vanaf"] if gv["status"] == "nog_niet" else gv["datums"]
        rows.append(row)
    applicable = [r for r in rows if r["uitkomst"] != "not_applicable"]
    if gate is False:
        total = "not_applicable"
    elif buiten_toepassing:
        total = "not_applicable"
        notes.append("kwalificatiestap(pen) " + ", ".join(buiten_toepassing)
                     + " n.v.t.: de regels van dit kader gelden niet (kader n.v.t.)")
    elif not applicable:
        total = "not_applicable"
    elif any(r["uitkomst"] == "non_compliant" and r["telt_mee"] for r in applicable):
        total = "non_compliant"
    elif any(r["uitkomst"] == "review" or (r["uitkomst"] == "non_compliant" and not r["telt_mee"]) for r in applicable):
        total = "review"
    else:
        total = "compliant"
    unknown_ids = [sid for sid in oordelen if sid not in st]
    if unknown_ids and note_unknown:
        notes.append("onbekende stap-id's genegeerd: " + ", ".join(unknown_ids))
    return {"kader": k["id"], "versie": k.get("version"), "peildatum": k.get("peildatum"),
            "kaderuitkomst": total, "symbool": SYMBOL[total], "label": LABEL[total], "stappen": rows, "opmerkingen": notes,
            "herinnering": "Pas ook de 'Regels van dit kader' toe; geef een n.v.t. op grond van zo'n regel mee als "
                           "{\"uitkomst\": \"n.v.t.\", \"reden\": \"...\"}."}


def aggregate_multi(kaders, facts, oordelen, today=None):
    """Uitkomst voor meer kaders met één set antwoorden en oordelen; past poortregels en poortstappen toe."""
    kaders = _as_list(kaders)
    eff, _, _, _, gates = resolve_multi(kaders, facts)
    results, by_step, notes, totals = [], {}, [], {}
    for k in kaders:
        g = gates[k["id"]][0]
        ids = {s["id"] for s in k["steps"]}
        mine = {sid: v for sid, v in oordelen.items() if sid in ids}
        reopen = False
        if g is False and k.get("poortstap"):
            ps = by_step.get(k["poortstap"])
            if ps is not None and ps != "compliant":
                reopen = True
                g = UNKNOWN
        dropped = [x for x in k.get("vervalt_als_nvt") or [] if totals.get(x) == "not_applicable"]
        if dropped and not reopen:
            g = False
        eff_k = eff
        if reopen:  # vragen van dit kader zijn niet gesteld: hun antwoorden zijn onbekend, niet n.v.t.
            own = {q["key"] for q in k["questions"]}
            eff_k = {x: v for x, v in eff.items() if not (v is NVT and x in own)}
        res = aggregate(k, facts, mine, today=today, eff=eff_k, gate=g, note_unknown=False)
        if dropped and not reopen:
            res["opmerkingen"] = [f"kader {', '.join(dropped)} is n.v.t., dus dit kader ook (regel van {k['id']})"] + \
                [n for n in res["opmerkingen"] if not n.startswith("poortregel onwaar")]
        if reopen:
            gfs = ", ".join(sorted(facts_in(parse_expr(k["gate"]))))
            res["opmerkingen"].insert(0, f"poortstap {k['poortstap']} is niet ✅: dit kader is niet uitgesloten. Zet {gfs} "
                                         f"op 'weet ik niet', stel de vragen van {k['id']} en beoordeel het alsnog")
        for r in res["stappen"]:
            by_step[r["id"]] = r["uitkomst"]
        totals[k["id"]] = res["kaderuitkomst"]
        results.append(res)
    known = set().union(*({s["id"] for s in k["steps"]} for k in kaders)) if kaders else set()
    unknown = [sid for sid in oordelen if sid not in known]
    if unknown:
        notes.append("onbekende stap-id's genegeerd: " + ", ".join(unknown))
    return {"kaders": results,
            "overzicht": [{"kader": r["kader"], "versie": r["versie"], "kaderuitkomst": r["kaderuitkomst"],
                           "symbool": r["symbool"]} for r in results],
            "opmerkingen": notes,
            "herinnering": results[0]["herinnering"] if results else ""}


# ---------------------------------------------------------------- profiel uit het register
def read_profile(path):
    prof, section = {}, None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            section = line.lstrip("#").strip().lower()
            continue
        if section and section.startswith("profiel") and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] not in ("Sleutel", "") and not set(cells[0]) <= set("-: "):
                prof[cells[0]] = cells[1]
    return prof


def _yn(v):
    v = (v or "").strip().lower()
    if v in ("ja", "yes", "true"):
        return True
    if v in ("nee", "no", "false"):
        return False
    return None


def suggest_from_profile(k, prof):
    """Voorstellen (ter bevestiging) voor vragen van dit kader uit het profiel van compliance-register.md."""
    out, hints = {}, []
    qs = {q["key"]: q for q in k["questions"]}
    org = prof.get("Organisatie")
    if org and "IN TE VULLEN" not in org:
        for q in k["questions"]:
            if q["eigen_org"] and q["type"] == "text" and q["key"].endswith("_name"):
                out[q["key"]] = {"waarde": org, "uit": "Organisatie"}
    rol = (prof.get("rol") or "").lower()
    rol_map = {"verwerkingsverantwoordelijke": "controller", "verantwoordelijke": "controller",
               "verwerker": "processor", "beide": "both"}
    if "role" in qs and set(qs["role"]["options"]) >= {"controller", "processor"}:
        for txt, val in rol_map.items():
            if rol.startswith(txt) and val in qs["role"]["options"]:
                out["role"] = {"waarde": val, "uit": "rol"}
                break
    kl = (prof.get("klanten") or "").lower()
    for q in k["questions"]:
        if q["type"] == "enum" and set(q["options"]) == {"business", "consumer", "both"}:
            val = {"bedrijven": "business", "consumenten": "consumer", "beide": "both"}.get(kl)
            if val:
                out[q["key"]] = {"waarde": val, "uit": "klanten"}
    if "transfers_outside_eea" in qs and _yn(prof.get("doorgifte")) is not None:
        out["transfers_outside_eea"] = {"waarde": _yn(prof.get("doorgifte")), "uit": "doorgifte"}
    if "uses_ai_systems" in qs:
        vals = [_yn(prof.get(x)) for x in ("ai_gebruik", "ai_eigen", "ai_inkoop")]
        if True in vals:
            out["uses_ai_systems"] = {"waarde": True, "uit": "ai_gebruik/ai_eigen/ai_inkoop"}
        elif vals and all(v is False for v in vals):
            out["uses_ai_systems"] = {"waarde": False, "uit": "ai_gebruik/ai_eigen/ai_inkoop"}
    med = prof.get("medewerkers")
    if med and "employee_count" in qs:
        hints.append(f"employee_count: profiel zegt '{med}'; vraag het exacte aantal alleen als een drempel ertoe doet")
    if med and "sme" in qs:
        hints.append(f"sme: profiel zegt '{med}' medewerkers")
    return out, hints


def follow_ups(kaders, facts):
    """Vervolgkaders volgens de antwoorden; kaders die zelf meedoen of vervallen, tellen niet."""
    kaders = _as_list(kaders)
    eff, _, _, _, gates = resolve_multi(kaders, facts)
    inside = {k["id"] for k in kaders}
    out, seen = [], set()
    for k in kaders:
        if gates[k["id"]][0] is False:
            continue
        for h in k["samenhang"]:
            if not h.get("kader") or h["kader"] in inside:
                continue
            c = cond_value(h["cond"], eff) if h["cond"] else True
            if c is False or (h["kader"], h["skill"]) in seen:
                continue
            seen.add((h["kader"], h["skill"]))
            out.append({"kader": h["kader"], "skill": ("/" + h["skill"]) if h["skill"] else None,
                        "reden": h["waarom"], "zeker": c is True, "via": k["id"]})
    return out


def fill(text, facts, labels):
    def rep(m):
        key = m.group(1)
        v = facts.get(key)
        if v is UNKNOWN or key not in facts:
            return f"[IN TE VULLEN: {labels.get(key, key)}]"
        if v is True:
            return "ja"
        if v is False:
            return "nee"
        return str(v)
    return re.sub(r"\{\{\s*facts\.([a-z0-9_]+)\s*\}\}", rep, text)


def assemble(k, facts):
    eff = resolve(k, facts)[0]
    labels = {q["key"]: (q["label"] or q["key"]) for q in k["questions"]}
    parts, skipped, uncertain = [], [], []
    for d in k["doc_items"]:
        c = cond_value(d["include_if"], eff)
        if c is False:
            skipped.append(d["id"])
            continue
        txt = fill(d["text"] or "", facts, labels)
        if c is UNKNOWN:
            uncertain.append(d["id"])
            txt = f"[IN TE VULLEN: controleer of dit onderdeel van toepassing is ({d['id']})]\n" + txt
        parts.append({"id": d["id"], "onderdeel": (d["onderdeel"] or {}).get("key"), "tekst": txt})
    body = "\n\n".join(p["tekst"] for p in parts)
    open_points = sorted(set(re.findall(r"\[IN TE VULLEN: [^\]]+\]", body)))
    return {"kader": k["id"], "versie": k.get("version"), "peildatum": k.get("peildatum"),
            "onderdelen": parts, "weggelaten": skipped, "onzeker_opgenomen": uncertain,
            "open_punten": open_points, "tekst": body}


# ---------------------------------------------------------------- structuurcontrole
def check(k):
    errs = list(k["errors"])
    keys = [q["key"] for q in k["questions"]]
    keyset = set(keys)
    seen = set()
    for q in k["questions"]:
        if q["key"] in seen:
            errs.append(f"vraag {q['key']} staat dubbel")
        seen.add(q["key"])
        if q["type"] is None:
            errs.append(f"vraag {q['key']}: geen type")
        if q["type"] == "enum" and len(q["options"]) < 2:
            errs.append(f"vraag {q['key']}: enum met minder dan twee opties")
    pos = {key: i for i, key in enumerate(keys)}
    enum_opts = {q["key"]: set(q["options"]) for q in k["questions"] if q["type"] == "enum"}
    types = {q["key"]: q["type"] for q in k["questions"]}

    def check_expr(where, expr, own_index=None):
        if not expr:
            return
        try:
            node = parse_expr(expr)
        except ValueError as e:
            errs.append(f"{where}: {e}")
            return
        for f in facts_in(node):
            if f not in keyset:
                errs.append(f"{where}: voorwaarde gebruikt onbekend feit '{f}'")
            elif own_index is not None and pos[f] >= own_index:
                errs.append(f"{where}: voorwaarde gebruikt '{f}', dat pas later wordt gevraagd")
        for f, vals in literals_for(node).items():
            t = types.get(f)
            for v in vals:
                if v == "__null__":
                    continue
                if t == "enum" and isinstance(v, str) and v not in enum_opts.get(f, set()):
                    errs.append(f"{where}: '{f}' heeft geen optie \"{v}\" (opties: {sorted(enum_opts.get(f, []))})")
                if t == "boolean" and not isinstance(v, bool):
                    errs.append(f"{where}: '{f}' is ja/nee maar wordt vergeleken met {v!r}")
                if t == "number" and not isinstance(v, (int, float)):
                    errs.append(f"{where}: '{f}' is een getal maar wordt vergeleken met {v!r}")
                if t in ("text",) and isinstance(v, bool):
                    errs.append(f"{where}: '{f}' is tekst maar wordt vergeleken met {v!r}")
    for i, q in enumerate(k["questions"]):
        check_expr(f"vraag {q['key']}", q["ask_if"], own_index=i)
    ids = [s["id"] for s in k["steps"]]
    if len(ids) != len(set(ids)):
        errs.append("dubbele toetspunt-id's: " + ", ".join(sorted({x for x in ids if ids.count(x) > 1})))
    for s in k["steps"]:
        check_expr(f"toetspunt {s['id']}", s["applies_if"])
        for n in s.get("needed", []):
            if n not in keyset:
                errs.append(f"toetspunt {s['id']}: 'Nodig' noemt onbekend feit '{n}'")
        if not s.get("doc_check"):
            if s["kind"] is None:
                errs.append(f"toetspunt {s['id']}: geen Soort (F/A)")
            if s["absent"] not in ("compliant", "review", "non_compliant", "not_applicable"):
                errs.append(f"toetspunt {s['id']}: geen geldige uitkomst bij afwezig ({s['absent']!r})")
            if not s.get("grondslag"):
                errs.append(f"toetspunt {s['id']}: geen grondslag")
            body = "\n".join(s["text"])
            all_opts = set().union(*enum_opts.values()) if enum_opts else set()
            for f in set(re.findall(r"\b([a-z][a-z0-9]*(?:_[a-z0-9]+)+)\b", body)):
                if f in keyset or f in all_opts:
                    continue
                if re.search(r"\b" + re.escape(f) + r"\b (is|=|==|true|false)", body) and f not in ("non_compliant", "not_applicable", "append_section"):
                    errs.append(f"toetspunt {s['id']}: beoordeling noemt onbekend feit '{f}'")
    did = [d["id"] for d in k["doc_items"]]
    for d in k["doc_items"]:
        check_expr(f"tekst {d['id']}", d["include_if"])
        for n in d["needed"]:
            if n not in keyset:
                errs.append(f"tekst {d['id']}: 'Nodig' noemt onbekend feit '{n}'")
        for f in re.findall(r"\{\{\s*facts\.([a-z0-9_]+)\s*\}\}", d["text"] or ""):
            if f not in keyset:
                errs.append(f"tekst {d['id']}: placeholder {{{{facts.{f}}}}} heeft geen vraag")
        if d["text"] is None:
            errs.append(f"tekst {d['id']}: geen tekstblok")
    if k["doc_items"]:
        checks = {s["id"] for s in k["steps"] if s.get("doc_check")}
        for x in did:
            if x not in checks:
                errs.append(f"tekst {x}: geen bijbehorend toetspunt voor de eindcontrole")
    for h in k["samenhang"]:
        if h.get("kader") is None:
            errs.append(f"samenhang: regel niet herkend: {h.get('raw')}")
        else:
            check_expr(f"samenhang {h['kader']}", h["cond"])
    for qk in k["qualification"]:
        if qk not in keyset:
            errs.append(f"kwalificatievraag '{qk}' bestaat niet")
    if k.get("gate"):
        try:
            parse_expr(k["gate"])  # feiten uit eerdere kaders van de skill: controle in tools/validate.py
        except ValueError as e:
            errs.append(f"poortregel: {e}")
        if k.get("poortstap") and not re.fullmatch(r"[A-Z]+[0-9]+[a-z]?\.[0-9]+", k["poortstap"]):
            errs.append(f"poortstap '{k['poortstap']}' is geen toetspunt-id")
    for where, clauses in [("Van toepassing vanaf", k.get("dates") or [])] + \
            [(f"toetspunt {s['id']} (Geldt vanaf)", s.get("dates") or []) for s in k["steps"]]:
        for _, expr in clauses:
            check_expr(where, expr)
    if not k.get("version") or not k.get("peildatum"):
        errs.append("versie of peildatum ontbreekt")
    raw = Path(k["path"]).read_text(encoding="utf-8")
    form_end = raw.find("\n## ", raw.find("## Formulier") + 5)
    rest = raw[form_end:] if form_end > 0 else ""
    if k["kind"] == "toets":
        head_exprs = " ".join([k.get("gate") or ""] + [e or "" for _, e in k.get("dates") or []]
                              + [e or "" for st in k["steps"] for _, e in st.get("dates") or []])
        for q in k["questions"]:
            used_in_form = any(q["key"] in (o["ask_if"] or "") for o in k["questions"])
            used_in_form = used_in_form or re.search(r"\b" + re.escape(q["key"]) + r"\b", head_exprs)
            if not used_in_form and not re.search(r"\b" + re.escape(q["key"]) + r"\b", rest):
                errs.append(f"WAARSCHUWING: vraag {q['key']} is alleen context (niet in voorwaarden of toetspunten)")
    return errs


# ---------------------------------------------------------------- cli
KADER_FILE_RE = re.compile(r"^(K|AI|CK|CB|C|W)[0-9]+[a-z]?-[a-z0-9-]+\.md$")


def batches(items, n=4):
    return [items[i:i + n] for i in range(0, len(items), n)]


# Een AskUserQuestion-aanroep heeft hooguit 4 velden. Ja/nee-vragen (waar "weet ik niet" mag) gaan als
# afvinklijst van hooguit 3 kenmerken in één veld; de vierde optie is "De overige: nee". Aangevinkt = ja,
# "De overige: nee" = nee voor de niet-aangevinkte kenmerken, anders onbekend (nooit nee).
BUNDEL_MAX = 3
AANROEP_MAX = 4


def bundel_groepen(items, size=BUNDEL_MAX):
    """Verdeel items gelijkmatig in zo weinig mogelijk groepen van hooguit `size` (4 → 2+2, 7 → 3+2+2)."""
    n = len(items)
    if not n:
        return []
    k = -(-n // size)
    base, extra = divmod(n, k)
    out, i = [], 0
    for g in range(k):
        step = base + (1 if g < extra else 0)
        out.append(items[i:i + step])
        i += step
    return out


def _toon(v):
    if isinstance(v, bool):
        return "ja" if v else "nee"
    return str(v)


def _suggesties(raw):
    """Leest de uitvoer van `voorstel` (of een los {sleutel: waarde}) als {sleutel: (waarde, uit)}."""
    if isinstance(raw, dict) and isinstance(raw.get("voorgesteld"), dict):
        raw = raw["voorgesteld"]
    out = {}
    for key, v in (raw or {}).items():
        if isinstance(v, dict) and "waarde" in v:
            out[key] = (v["waarde"], v.get("uit"))
        else:
            out[key] = (v, None)
    return out


def velden_voor_golf(qs, kader_volgorde, qual, voorgesteld=None):
    """Zet de vragen van één golf om in velden: een bevestigingsveld voor voorgestelde antwoorden,
    kwalificatievragen apart, ja/nee-vragen als afvinklijst, de rest als enkel veld."""
    sug = _suggesties(voorgesteld)
    velden = []
    bevestig = [q for q in qs if q["key"] in sug]
    rest = [q for q in qs if q["key"] not in sug]
    if bevestig:
        velden.append({"soort": "bevestiging",
                       "vraag": "Kloppen deze antwoorden uit je register en eerdere gegevens?",
                       "opties": ["Ja, alles klopt", "Niet alles klopt: toon ze afzonderlijk"],
                       "voorstellen": [{"sleutel": q["key"], "vraag": q["vraag"], "voorstel": _toon(sug[q["key"]][0]),
                                        "uit": sug[q["key"]][1]} for q in bevestig]})

    def enkel(q):
        return {"soort": "enkel", "sleutel": q["key"], "vraag": q["vraag"], "type": q["type"],
                "opties": q["opties"], "opties_nl": [optie_label(q["key"], o) for o in q["opties"]] if q["opties"] else None,
                "hulp": q["hulp"], "weet_ik_niet_mag": q["weet_ik_niet_mag"],
                "eigen_organisatie": q["eigen_organisatie"], "kader": q["kader"]}

    kw = [q for q in rest if q["key"] in qual]
    velden += [enkel(q) for q in kw]
    rest = [q for q in rest if q["key"] not in qual]
    for kid in kader_volgorde:
        eigen = [q for q in rest if q["kader"] == kid]
        bundelbaar = [q for q in eigen if q["type"] == "boolean" and q["weet_ik_niet_mag"]]
        keys_b = {q["key"] for q in bundelbaar}
        velden += [enkel(q) for q in eigen if q["key"] not in keys_b]
        for groep in bundel_groepen(bundelbaar):
            if len(groep) == 1:
                velden.append(enkel(groep[0]))
            else:
                velden.append({"soort": "afvinklijst", "kader": kid,
                               "kenmerken": [{"sleutel": q["key"], "vraag": q["vraag"], "hulp": q["hulp"]} for q in groep],
                               "extra_optie": "De overige: nee"})
    return velden


# ---------- Nederlandse labels bij de antwoordopties ----------
# De sleutels van een keuzevraag (consent, high, …) zijn Engelse codes; de gebruiker ziet Nederlandse labels, het formulier stuurt
# de code terug. Eén label per code; OPTIE_NL_VRAAG is voor een code die bij één vraag iets anders betekent. Een test eist een
# label voor elke code in elk kader, dus een nieuwe code komt hier bij.
OPTIE_NL = {
    "active_opt_in": "Actieve toestemming (opt-in)", "active_optin": "Actieve toestemming (opt-in)", "adequacy_country": "Land met een adequaatheidsbesluit",
    "after_consent": "Pas nadat de bezoeker toestemming gaf", "always_id_copy": "Altijd een kopie van het identiteitsbewijs", "annex1": "Bijlage I",
    "annex2": "Bijlage II", "annex3": "Bijlage III", "anonymous": "Anoniem", "applicants": "Sollicitanten", "assessing_request": "Een verzoek beoordelen",
    "automated": "Geautomatiseerd", "bcr": "Bindende bedrijfsvoorschriften (BCR)", "before_consent": "Al bij het openen van de pagina",
    "biometric": "Biometrische gegevens", "biometric_categorisation_or_emotion": "Biometrische categorisering of emotieherkenning",
    "biometric_identification": "Biometrische identificatie", "biometric_security": "Biometrische beveiliging", "both": "Allebei",
    "built_own": "Zelf gebouwd", "business": "Zakelijk", "business_contacts": "Zakelijke contacten", "c2c": "Verwerkingsverantwoordelijke naar verwerkingsverantwoordelijke",
    "c2p": "Verwerkingsverantwoordelijke naar verwerker", "p2p": "Verwerker naar verwerker", "p2c": "Verwerker naar verwerkingsverantwoordelijke",
    "client": "De opdrachtgever", "client_controller_party_processor": "Opdrachtgever is verwerkingsverantwoordelijke, de andere partij is verwerker",
    "client_processor_party_controller": "Opdrachtgever is verwerker, de andere partij is verwerkingsverantwoordelijke", "commercial": "Commercieel",
    "complete": "Compleet", "condition_for_other": "Toestemming als voorwaarde voor iets anders", "conduit": "Doorgeefluik (mere conduit)",
    "configured_on_platform": "Ingericht op een platform", "consent": "Toestemming", "consumer": "Consument", "consumers": "Consumenten",
    "contract": "Overeenkomst", "controller": "Verwerkingsverantwoordelijke", "cookie_policy_only": "Alleen via de cookieverklaring",
    "copied": "Gekopieerd", "credit": "Krediet", "credit_scoring": "Kredietwaardigheid beoordelen", "critical_infrastructure": "Kritieke infrastructuur",
    "customer": "Bestaande klant", "customers_and_employees": "Klanten en werknemers", "customers_or_public": "Klanten of publiek",
    "data_unintelligible": "Gegevens onleesbaar voor onbevoegden", "decided_not_to_inform": "Besloten niet te informeren",
    "decided_not_to_notify": "Besloten niet te melden", "deployer": "Gebruiker van de toepassing (deployer)", "designated_for_offers": "Bestemd voor aanbiedingen",
    "device_lost_stolen": "Apparaat verloren of gestolen", "directly_identifiable": "Direct identificeerbaar",
    "disproportionate_public_notice": "Openbare mededeling (individueel informeren kost onevenredig veel moeite)", "distributor": "Distributeur",
    "done_after_start": "Uitgevoerd nadat de verwerking begon", "done_before_start": "Uitgevoerd vóór de start", "dpf_certified": "Ontvanger is DPF-gecertificeerd",
    "each_separately": "Elk apart", "education": "Onderwijs", "email_no_bcc": "E-mail zonder bcc", "email_or_browser": "Via e-mail of de browser",
    "email_wrong_recipient": "E-mail naar de verkeerde ontvanger", "employees": "Werknemers", "employment": "Werk en personeelsbeheer",
    "employment_obligation": "Verplichting uit arbeids- of socialezekerheidsrecht", "en": "Engels", "encrypted_only": "Alleen versleuteld",
    "equal_first_layer": "Even duidelijk op de eerste laag", "eu_or_dutch_law": "EU-recht of Nederlands recht", "exceptional_only": "Alleen in uitzonderlijke gevallen",
    "explicit_consent": "Uitdrukkelijke toestemming", "extended_with_notice": "Verlengd, met bericht aan de verzoeker", "extra_confirmation": "Alleen met een extra bevestiging",
    "finetuned_model": "Bijgetraind model", "first_layer_less_prominent": "Op de eerste laag, minder duidelijk dan accepteren", "footer_link": "Link onderaan de pagina",
    "four_weeks": "Vier weken", "fraud_detection": "Fraudecontrole", "full_wall": "Volledige cookiewall", "general": "Algemeen",
    "general_info_address": "Algemeen informatieadres (zoals info@)", "healthcare": "Gezondheidszorg", "high": "Hoog", "high_risk_removed": "Het hoge risico is weggenomen",
    "hosting": "Hosting", "ideal_charitable": "Ideëel of goed doel", "importer": "Importeur", "incident": "Ik heb nu een incident", "included": "Staat erin",
    "incomplete": "Onvolledig", "independent_controllers": "Zelfstandige verwerkingsverantwoordelijken", "indirectly_identifiable": "Indirect identificeerbaar",
    "insurance": "Verzekeringen", "job_applicants": "Sollicitanten", "joint_controllers": "Gezamenlijke verwerkingsverantwoordelijken", "jointly": "Samen",
    "large": "Groot", "late_or_no_notice": "Te laat of zonder bericht", "later_or_never": "Later of nooit", "law": "Wet",
    "law_enforcement_migration_justice_elections": "Rechtshandhaving, migratie, rechtspraak of verkiezingen", "legal_claim": "Rechtsvordering",
    "legal_obligation": "Wettelijke verplichting", "legitimate_interest": "Gerechtvaardigd belang",
    "legitimate_interest_documented": "Gerechtvaardigd belang, vastgelegd", "legitimate_interest_not_documented": "Gerechtvaardigd belang, niet vastgelegd",
    "letter_misdelivered": "Brief op het verkeerde adres bezorgd", "life_health_insurance": "Levens- of ziektekostenverzekering", "limited_access": "Beperkte toegang",
    "link_in_text": "Link in de tekst", "longer": "Langer", "low": "Laag", "made_public_by_person": "Door de betrokkene zelf openbaar gemaakt",
    "marketplace": "Marktplaats", "medium": "Gemiddeld", "military_defence_security": "Militair, defensie of nationale veiligheid", "modified_system": "Aangepast systeem",
    "narrow_strip": "Alleen een smalle strook", "never": "Nooit", "nl": "Nederlands", "nl_en": "Nederlands en Engels", "no_fixed_period": "Geen vaste termijn",
    "no_law": "Geen wettelijke grondslag", "no_role_in_contract": "Geen rollen in het contract", "non_eu_law": "Recht van een land buiten de EU",
    "none": "Geen van deze", "not_determined": "Nog niet vastgesteld", "not_done": "Niet uitgevoerd", "not_included": "Staat er niet in", "not_possible": "Niet mogelijk",
    "not_published": "Niet gepubliceerd", "not_yet": "Nog niet", "notified": "Gemeld", "on_request": "Alleen op verzoek", "online_platform": "Online platform",
    "only_when_doubt": "Alleen bij twijfel", "other": "Anders", "other_law": "Een andere wet", "other_party": "De andere partij", "outside_eea": "Buiten de EER",
    "own_other": "Andere eigen producten of diensten", "party_processes_for_us": "De andere partij verwerkt gegevens voor mij",
    "pay_or_ok": "Betalen of accepteren", "payroll": "Salarisadministratie", "persistent_button": "Blijvende knop of icoon",
    "personal_employee_address_list": "Lijst met persoonlijke werknemersadressen", "phishing_hacked_account": "Phishing of gehackt account",
    "planned_not_started": "Gepland, nog niet begonnen", "pre_market_testing": "Testen vóór het op de markt brengen", "pre_ticked_box": "Vooraf aangevinkt vakje",
    "prechecked": "Vooraf aangevinkt vakje", "pricing": "Prijsstelling", "private_public_service": "Private organisatie met een publieke dienst",
    "process_check": "Mijn proces controleren", "processor": "Verwerker", "protection_against_offences": "Bescherming tegen strafbare feiten",
    "provider": "Aanbieder (provider)", "pseudonymised_with_key": "Gepseudonimiseerd, met sleutel", "pseudonymised_without_key": "Gepseudonimiseerd, zonder sleutel",
    "public_body": "Overheidsorgaan", "public_services": "Publieke diensten", "public_task": "Publieke taak", "purchased_list": "Gekochte lijst",
    "ransomware": "Ransomware", "recruitment": "Werving en selectie", "resell": "Doorverkopen", "same_or_similar": "Dezelfde of soortgelijke eigen producten of diensten",
    "scc": "Standaardcontractbepalingen (SCC)", "scientific_research_only": "Alleen wetenschappelijk onderzoek", "security_necessary": "Nodig voor beveiliging",
    "service_access": "Toegang tot een dienst of account", "settings_only": "Alleen in de instellingen", "shared_or_exchanged": "We delen of wisselen gegevens uit",
    "silence_or_continued_use": "Stilzwijgen of doorgaan met gebruiken", "small": "Klein", "specific": "Specifiek", "standard_fee": "Standaardbedrag",
    "structured_paper": "Gestructureerd op papier", "students": "Studenten", "substantial_public_interest": "Zwaarwegend algemeen belang", "text_only": "Alleen tekst",
    "third_party": "Producten of diensten van een derde", "time_or_convenience": "Tijdwinst of gemak", "unstructured_paper": "Ongestructureerd op papier",
    "up_to_4_weeks": "Tot vier weken", "vendor_system": "Systeem van een leverancier, ongewijzigd", "via_terms": "Via de algemene voorwaarden",
    "vital_interests": "Vitale belangen", "we_process_for_party": "Ik verwerk gegevens voor de andere partij", "website_every_page": "Op elke pagina van de website",
    "website_hidden": "Op de website, moeilijk te vinden", "website_visitors": "Websitebezoekers", "within_one_month": "Binnen een maand",
    "year_with_consent": "Een jaar, met toestemming", "yes": "Ja", "yes_informed": "Ja, geïnformeerd",
}
OPTIE_NL_VRAAG = {  # (vraagsleutel, code): label, waar de code daar iets anders betekent dan in OPTIE_NL
    ("size", "medium"): "Middelgroot", ("films_public_road", "none"): "Nee", ("second_legal_basis", "none"): "Nee, geen andere grond",
    ("reject_option", "none"): "Weigeren kan niet", ("withdrawal_method", "none"): "Wijzigen of intrekken kan niet",
    ("cookiewall", "none"): "Nee, geen cookiewall", ("signage", "none"): "Geen bord of sticker", ("exempt_basis", "none"): "Geen grond",
    ("incident_scenario", "other"): "Iets anders", ("basis", "none"): "Geen van beide",
    ("audience_language", "other"): "Een andere taal", ("adequacy", "none"): "Nee, geen adequaatheidsbesluit",
}


def optie_label(vraag_sleutel, optie):
    """Nederlands label bij een antwoordoptie; onbekende codes (bijvoorbeeld de al Nederlandse opties van --extra) blijven zoals ze zijn."""
    return OPTIE_NL_VRAAG.get((vraag_sleutel, optie)) or OPTIE_NL.get(optie) or str(optie).replace("_", " ")



# ---------- formulier: alle vragen in één keer ----------

# Zelfde look als de site: lichtgrijze achtergrond met zachte vlekken, leisteen-glaskaarten, twee accenten: geel = voldoet / klaar,
# blauw = voldoet niet / nog te doen (en hover). Geen groen of rood. --g-out/--g-out2 zijn de tekstkleuren buiten de kaarten.
GLAS_TOKENS = ("--g-bg:#f4f6f8;--g-fon:radial-gradient(ellipse 60% 38% at 0 0,rgba(70,82,98,.30),transparent 72%),"
               "radial-gradient(ellipse 50% 40% at 100% 52%,rgba(118,134,152,.34),transparent 70%),"
               "radial-gradient(ellipse 46% 34% at 50% 100%,rgba(176,194,212,.40),transparent 72%),#f4f6f8;"
               "--g-card:rgba(50,54,62,.80);--g-line:rgba(255,255,255,.16);--g-ink:#f5f5f7;"
               "--g-mute:rgba(245,245,247,.62);--g-yes:#FFFF00;--g-no:#48CAE4;--g-out:#0d1117;--g-out2:#3e464f;"
               "--g-sh:0 10px 30px rgba(13,17,23,.18),inset 0 1px 0 rgba(255,255,255,.08);"
               "--g-font:Geist,system-ui,sans-serif")

FORM_CSS = """<style>
.kf{""" + GLAS_TOKENS + """;position:relative;font:15px/1.45 var(--g-font);letter-spacing:-.006em;color:var(--g-out);padding:20px 16px 32px;border-radius:24px;background:var(--g-fon)}
.kf *{box-sizing:border-box}.kf h2{font-size:22px;font-weight:600;letter-spacing:-.04em;margin:0 0 4px}.kf .sub{color:var(--g-out2);font-size:13.5px;margin:0 0 14px;max-width:62ch}
.kf .c,.kf .bar{background:var(--g-card);color:var(--g-ink);border:1px solid var(--g-line);border-radius:20px;box-shadow:var(--g-sh)}
.kf .c{padding:14px 16px;margin:0 0 12px}.kf h3{font-size:13px;font-weight:500;margin:0 0 6px;color:var(--g-mute)}
.kf .q{padding:10px 0;border-top:1px solid var(--g-line)}.kf .q:first-of-type{border-top:0}.kf [hidden]{display:none!important}
.kf .v{font-weight:600}.kf .v::before{content:"";display:inline-block;width:9px;height:9px;margin-right:8px;border-radius:50%;border:1.5px solid var(--g-mute);vertical-align:1px}
.kf .d .v::before{background:var(--g-yes);border-color:var(--g-yes)}.kf .m .v::before{border-color:var(--g-no)}.kf .h{color:var(--g-mute);font-size:12.5px;margin:2px 0 6px}
.kf .o{display:flex;flex-wrap:wrap;gap:6px}.kf .o label{cursor:pointer}.kf .o input{position:absolute;opacity:0}
.kf .o span{display:inline-block;padding:7px 15px;border-radius:999px;border:1px solid var(--g-line);background:rgba(255,255,255,.08);font-size:13.5px;transition:background .18s,color .18s,border-color .18s}
.kf .o label:hover span{background:var(--g-no);color:#04222b;border-color:var(--g-no)}
.kf .o input:checked+span{background:var(--g-yes);color:#0b0b0b;border-color:var(--g-yes);font-weight:600}
.kf .o input:focus-visible+span,.kf textarea:focus-visible,.kf input[type=number]:focus-visible,.kf button:focus-visible{outline:2px solid var(--g-no);outline-offset:3px}
.kf textarea,.kf input[type=number]{width:100%;border-radius:14px;border:1px solid var(--g-line);background:rgba(13,17,23,.30);color:var(--g-ink);padding:9px 12px;font:inherit}
.kf .bar{display:flex;gap:12px;align-items:center;flex-wrap:wrap;border-radius:999px;padding:6px 6px 6px 18px}.kf .pill{font-size:13px;font-weight:500}
.kf .pb{flex:1;min-width:60px;height:7px;border-radius:4px;background:rgba(72,202,228,.45);overflow:hidden}.kf .pb i{display:block;height:100%;width:0;background:var(--g-yes);border-radius:4px;transition:width .25s}
.kf button{height:42px;border:0;border-radius:999px;padding:0 22px;background:rgba(255,255,255,.14);color:var(--g-ink);font:inherit;font-weight:600;cursor:pointer;transition:background .18s,color .18s}.kf button.y{background:var(--g-yes);color:#0b0b0b}
.kf button:hover:not([disabled]){background:var(--g-no);color:#04222b}.kf button[disabled]{opacity:.45;cursor:not-allowed}
.kf .warn{color:var(--g-no);font-size:13px;font-weight:600}.kf .tm{position:absolute;right:18px;bottom:9px;font-size:10.5px;letter-spacing:.02em;color:var(--g-out2);opacity:.75;pointer-events:none}
</style>"""

# Evaluator in JavaScript, gelijk aan evaluate() hierboven (drie-waardenlogica); een test vergelijkt ze.
# Compacte voorwaarde (zie _ast_json): ["|",…] of ["&",…] = of/en, ["!",n] = niet, true/false/null = vaste uitkomst,
# [op, a, b] = vergelijking waarin een feit [sleutel] is en een waarde er rechtstreeks staat.
FORM_EVAL_JS = """var NVT='\\u0000nvt';
function ov(o,g){return Array.isArray(o)?g(o[0]):o}
function ev(n,g){if(!Array.isArray(n))return n;var t=n[0],i,a=[],v;
if(t==='|'||t==='&'){for(i=1;i<n.length;i++)a.push(ev(n[i],g));
if(t==='|'){if(a.indexOf(true)>=0)return true;return a.indexOf(null)>=0?null:false}
if(a.indexOf(false)>=0)return false;return a.indexOf(null)>=0?null:true}
if(t==='!'){v=ev(n[1],g);return v===null?null:!v}
var x=ov(n[1],g),y=ov(n[2],g);
if(x===NVT||y===NVT)return false;
if(x==='__null__'||y==='__null__'){var o=x==='__null__'?y:x,z=o===null;return t==='=='?z:!z}
if(x===null||y===null)return null;
if(t==='==')return x===y;if(t==='!=')return x!==y;
if(typeof x!==typeof y)return null;
if(t==='>=')return x>=y;if(t==='<=')return x<=y;if(t==='>')return x>y;return x<y}
"""

# Velden: g = groepen {t titel, p poort, q vragen}; vraag {k sleutel, v vraag, t type (b ja/nee, e keuze, n getal, leeg = tekst),
# h hulp, o opties, l afwijkende labels, r verplicht, a voorwaarde, w voorgevulde waarde}; L = Nederlandse label per optiecode. "Weet ik niet" kan bij elke vraag die niet verplicht is.
FORM_JS = "<script>\n(function(){" + FORM_EVAL_JS + """
var D=JSON.parse(document.getElementById('kfdata').textContent),A={},R=document.getElementById('kf'),Q=[],G=[],F=document.createDocumentFragment(),
B=R.querySelector('button'),P=R.querySelector('.pill'),W=R.querySelector('.warn'),PB=R.querySelector('.pb i');
function E(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e}
D.g.forEach(function(g){var C=E('div','c'),gr={el:C,p:g.p,qs:[]};G.push(gr);C.appendChild(E('h3','',g.t));
g.q.forEach(function(q){var X=E('div','q'),t=q.t,c=q.w;X.appendChild(E('div','v',q.v+(q.r?' *':'')));
if(q.h)X.appendChild(E('div','h',q.h));
if(c!==undefined)A[q.k]=c;
if(t==='b'||t==='e'){var O=E('div','o'),ops=t==='b'?[['ja','Ja'],['nee','Nee']]:q.o.map(function(z){return[z,(q.l&&q.l[z])||D.L[z]||z.replace(/_/g,' ')]});
O.setAttribute('role','radiogroup');O.setAttribute('aria-label',q.v);if(!q.r)ops.push(['__onbekend','Weet ik niet']);
ops.forEach(function(z){var L=E('label'),I=document.createElement('input');I.type='radio';I.name=q.k;
I.checked=c!==undefined&&(z[0]==='__onbekend'?c==='weet ik niet':c===z[0]||(t==='b'&&c===(z[0]==='ja')));
I.addEventListener('change',function(){A[q.k]=z[0]==='__onbekend'?'weet ik niet':(t==='b'?z[0]==='ja':z[0]);upd()});
L.appendChild(I);L.appendChild(E('span','',z[1]));O.appendChild(L)});X.appendChild(O)}
else{var T=document.createElement(t==='n'?'input':'textarea');if(t==='n')T.type='number';else T.rows=2;
T.setAttribute('aria-label',q.v);if(c!==undefined)T.value=c;
T.addEventListener('input',function(){if(T.value==='')delete A[q.k];else A[q.k]=t==='n'?Number(T.value):T.value;upd()});X.appendChild(T)}
var z={q:q,el:X,hid:false};Q.push(z);gr.qs.push(z);C.appendChild(X)});F.appendChild(C)});
R.querySelector('.cs').appendChild(F);
function nv(v){return(v===undefined||v===null||v===''||v==='weet ik niet'||v==='onbekend')?null:v}
function vis(){var hid={},ch=true,n=0;
while(ch&&n++<10){ch=false;var g=function(k){return hid[k]?NVT:nv(A[k])};
G.forEach(function(gr){var off=gr.p&&ev(gr.p,g)===false;gr.qs.forEach(function(z){var h=off||(z.q.a&&ev(z.q.a,g)===false);if(h&&!hid[z.q.k]){hid[z.q.k]=1;ch=true}})})}
return hid}
function upd(){var hid=vis(),tot=0,k=0,mis=0,g=function(x){return hid[x]?NVT:nv(A[x])};
Q.forEach(function(z){z.hid=!!hid[z.q.k];z.el.hidden=z.hid;if(!z.hid){tot++;var a=A[z.q.k],d=a!==undefined&&a!=='',m=!d&&z.q.r&&(!z.q.a||ev(z.q.a,g)===true);if(d)k++;if(m)mis++;z.el.className='q'+(d?' d':m?' m':'')}});
G.forEach(function(gr){gr.el.hidden=gr.qs.every(function(z){return z.hid})});
P.textContent=k+' van '+tot+' ingevuld';PB.style.width=(tot?100*k/tot:0)+'%';B.className=k?'y':'';B.disabled=mis>0;W.textContent=mis?('Nog verplicht: '+mis+' met *'):''}
B.addEventListener('click',function(){var out={};Q.forEach(function(z){if(!z.hid&&A[z.q.k]!==undefined&&A[z.q.k]!=='')out[z.q.k]=A[z.q.k]});
sendPrompt('Mijn antwoorden op het formulier (niet ingevuld = weet ik niet):\\n'+JSON.stringify(out))});upd()})();
</script>"""


def _vraag_kort(q):
    return (q.get("label") or q["vraag"]).rstrip("?. ")


def _alleen_als(expr, by_key):
    """Gewone-taalregel bij een voorwaarde: noemt de onderwerpen waar het antwoord van afhangt."""
    if not expr:
        return None
    try:
        keys = sorted(facts_in(parse_expr(expr)))
    except ValueError:
        return None
    namen = [_vraag_kort(by_key[x]) for x in keys if x in by_key]
    if not namen:
        return None
    return "Alleen invullen als dit speelt, afhankelijk van: " + "; ".join(namen)


def _ast_json(node):
    """Voorwaarde als compacte geneste lijst voor de JavaScript-evaluator in het formulier: ["|",…] of ["&",…] (of/en),
    ["!",n] (niet), true/false/null (vaste uitkomst) en [op, a, b] (vergelijking; een feit is [sleutel], een waarde staat er rechtstreeks)."""
    t = node[0]
    if t in ("and", "or"):
        return ["&" if t == "and" else "|"] + [_ast_json(p) for p in node[1]]
    if t == "not":
        return ["!", _ast_json(node[1])]
    if t == "const":
        return node[1]
    op = lambda o: [o[1]] if o[0] == "fact" else o[1]  # noqa: E731
    return [node[1], op(node[2]), op(node[3])]


def _ast_of(expr):
    if not expr:
        return None
    try:
        return _ast_json(parse_expr(expr))
    except ValueError:
        return None


def formulier_data(ks, facts, voorgesteld=None, alles=False, extra=None):
    """Alle vragen van de kaders in één formulier, per kader gegroepeerd. Beantwoorde vragen blijven (voorgevuld)
    als alles=True; anders vallen ze weg. Elke vraag met een voorwaarde heeft een 'ast' en een 'alleen_als'-regel:
    het formulier verbergt een vraag live zodra de voorwaarde onwaar wordt (onbekend = tonen), net als kader.py."""
    sug = _suggesties(voorgesteld)
    by_key = {q["key"]: q for k in ks for q in k["questions"]}
    by_extra = {q["sleutel"]: {"key": q["sleutel"], "vraag": q["vraag"], "label": q.get("label")}
                for g in (extra or []) for q in g.get("vragen", [])}
    by_extra.update(by_key)
    qual = set().union(*(set(k["qualification"]) for k in ks)) if ks else set()
    groepen, totaal = [], 0
    for g in (extra or []):  # eigen groepen vooraf: keuzes vooraf, huisstijl, namen en adressen (geen kadervragen)
        vr = []
        for q in g.get("vragen", []):
            if q["sleutel"] in facts and not alles:
                continue
            item = {"sleutel": q["sleutel"], "vraag": q["vraag"], "type": q.get("type") or "text",
                    "opties": q.get("opties"), "hulp": q.get("hulp"), "verplicht": bool(q.get("verplicht")),
                    "weet_ik_niet_mag": not q.get("verplicht"), "alleen_als": None, "ast": _ast_of(q.get("ask_if"))}
            if item["opties"]:
                item["opties_nl"] = [optie_label(q["sleutel"], o) for o in item["opties"]]
            if q.get("ask_if"):
                item["alleen_als"] = _alleen_als(q["ask_if"], by_extra)
            if q["sleutel"] in facts:
                item["waarde"] = facts[q["sleutel"]]
            vr.append(item)
        if vr:
            groepen.append({"kader": g.get("kader", "Vooraf"), "titel": g.get("titel", "Voor we beginnen"),
                            "alleen_als": None, "poort": None, "vragen": vr})
            totaal += len(vr)
    for k in ks:
        vr = []
        for q in sorted(k["questions"], key=lambda x: 0 if x["key"] in qual else 1):
            if q["key"] in facts and not alles:
                continue
            item = {"sleutel": q["key"], "vraag": q["vraag"], "type": q["type"], "opties": q["options"] or None,
                    "hulp": q["hulp"], "verplicht": q["key"] in qual,
                    "weet_ik_niet_mag": q["key"] not in qual, "alleen_als": _alleen_als(q["ask_if"], by_key),
                    "ast": _ast_of(q["ask_if"])}
            if item["opties"]:
                item["opties_nl"] = [optie_label(q["key"], o) for o in item["opties"]]
            if q["key"] in facts:
                item["waarde"] = facts[q["key"]]
            elif q["key"] in sug:
                item["waarde"] = sug[q["key"]][0]
                item["voorgesteld_uit"] = sug[q["key"]][1]
            vr.append(item)
        if vr:
            # een poortregel met poortstap hangt ook van de uitkomst van die stap af: die blijft altijd zichtbaar
            poort = _ast_of(k.get("gate")) if not k.get("poortstap") else None
            groepen.append({"kader": k["id"], "titel": k["title"], "alleen_als": _alleen_als(k.get("gate"), by_key),
                            "poort": poort, "vragen": vr})
            totaal += len(vr)
    return {"kader": "+".join(k["id"] for k in ks) or "intake", "totaal": totaal, "groepen": groepen}


_TYPE_KORT = {"boolean": "b", "enum": "e", "number": "n"}


def _vraag_slim(q, L):
    """Eén vraag in de korte velden van het formulier (minder tekst om te genereren en te laden); zie FORM_JS.
    Nederlandse optielabels: de gewone komen één keer in L (per formulier), afwijkende per vraag in l."""
    d = {"k": q["sleutel"], "v": q["vraag"]}
    if q["type"] in _TYPE_KORT:
        d["t"] = _TYPE_KORT[q["type"]]
    if q.get("hulp"):
        d["h"] = q["hulp"]
    if q.get("opties"):
        d["o"] = q["opties"]
        eigen = {}
        for o in q["opties"]:
            lab = optie_label(q["sleutel"], o)
            if lab == str(o).replace("_", " "):
                continue  # gelijk aan wat het formulier zelf van de code maakt
            if lab == OPTIE_NL.get(o):
                L[o] = lab
            else:
                eigen[o] = lab
        if eigen:
            d["l"] = eigen
    if q.get("verplicht"):
        d["r"] = 1
    if q.get("ast"):
        d["a"] = q["ast"]
    if q.get("waarde") is not None and q["waarde"] != "":  # ook false en 0 zijn antwoorden
        d["w"] = q["waarde"]
    return d


def formulier_html(data, verzend=None):
    """Zelfstandig HTML-fragment: het hele formulier met één Verstuur-knop; de pagina bouwt de velden uit de
    ingesloten JSON, verbergt vragen live en roept sendPrompt aan met de antwoorden. Leeg = onbekend."""
    groepen, L = [], {}
    for g in data["groepen"]:
        gg = {"t": g["titel"], "q": [_vraag_slim(q, L) for q in g["vragen"]]}
        if g.get("poort"):
            gg["p"] = g["poort"]
        groepen.append(gg)
    payload = json.dumps({"g": groepen, "L": L}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return (FORM_CSS + '<div class="kf" id="kf"><h2>Vragenformulier</h2>'
            '<p class="sub">Vul in wat je weet. Wat je leeg laat telt als "weet ik niet" (dan blijft het een aandachtspunt). '
            'Vragen die door een antwoord niet meer nodig zijn, verdwijnen vanzelf.</p><div class="cs"></div>'
            '<div class="bar"><span class="pill"></span><span class="pb"><i></i></span><span class="warn" role="status"></span><button type="button">Verstuur antwoorden</button></div>'
            '<small class="tm">Lawskills&trade;</small></div>'
            f'<script type="application/json" id="kfdata">{payload}</script>' + (verzend or "") + FORM_JS)


def formulier_tekst(data):
    """Het hele formulier als één genummerde lijst voor een bericht (zonder widget of browser)."""
    regels = [f"Vragenformulier — beantwoord alles in één bericht, bijvoorbeeld \"1: ja\", \"2: nee\". "
              "Wat je overslaat telt als weet ik niet. Vragen met 'alleen als' sla je over als die voorwaarde niet speelt.", ""]
    n = 0
    for g in data["groepen"]:
        regels.append(f"**{g['titel']}**")
        if g.get("alleen_als"):
            regels.append(f"_{g['alleen_als']}_")
        for q in g["vragen"]:
            n += 1
            if q["type"] == "boolean":
                opt = "ja / nee" + (" / weet ik niet" if q["weet_ik_niet_mag"] else "")
            elif q["type"] == "enum":
                opt = " / ".join(q.get("opties_nl") or [o.replace("_", " ") for o in q["opties"]]) + (" / weet ik niet" if q["weet_ik_niet_mag"] else "")
            else:
                opt = "open antwoord" if q["type"] == "text" else "getal"
            ster = " *" if q["verplicht"] else ""
            extra = f" — {q['alleen_als']}" if q.get("alleen_als") else ""
            regels.append(f"{n}. {q['vraag']}{ster} [{opt}]{extra}")
            if q.get("hulp"):
                regels.append(f"   ({q['hulp']})")
        regels.append("")
    regels.append("* = verplicht")
    return "\n".join(regels)


def formulier_serveren(data, uitvoer, timeout=1800):
    """Zet het formulier op een lokale pagina (127.0.0.1), opent de browser en wacht op de antwoorden;
    die gaan als JSON naar <uitvoer>. Voor Claude Code op de computer van de gebruiker."""
    import http.server
    import threading
    import webbrowser

    verzend = ("<script>window.sendPrompt=function(t){var j=t.slice(t.indexOf('\\n')+1);"
               "fetch('/antwoorden',{method:'POST',body:j}).then(function(){document.body.innerHTML="
               "'<p style=\"font:16px system-ui;color:#0d1117;padding:24px\">Verzonden. Ga terug naar Claude; je mag dit tabblad sluiten.</p>'})};</script>")
    pagina = ("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"
              "<title>Lawskills · Formulier</title><body style='margin:0;padding:16px;background:#f4f6f8'>"
              "<div style='max-width:760px;margin:0 auto'>" + formulier_html(data, verzend) + "</div>")
    klaar = threading.Event()

    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            b = pagina.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_POST(self):
            n = int(self.headers.get("Content-Length") or 0)
            body = self.rfile.read(n).decode("utf-8")
            try:
                json.loads(body)
            except ValueError:
                self.send_response(400)
                self.end_headers()
                return
            Path(uitvoer).write_text(body, encoding="utf-8")
            self.send_response(200)
            self.end_headers()
            klaar.set()

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
    url = f"http://127.0.0.1:{srv.server_address[1]}/"
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    print(f"Formulier staat op {url} — antwoorden komen in {uitvoer}", flush=True)
    try:
        webbrowser.open(url)
    except Exception:
        pass
    ok = klaar.wait(timeout)
    srv.shutdown()
    return 0 if ok else 2


def kaders_in_dir(d):
    """Alle kaderbestanden in een skillmap, in de volgorde waarin SKILL.md ze noemt."""
    d = Path(d)
    files = [f for f in sorted(d.iterdir()) if KADER_FILE_RE.match(f.name)]
    skill = next((d / n for n in ("SKILL.md", "INSTRUCTIES.md") if (d / n).exists()), None)  # in de bundel heet SKILL.md INSTRUCTIES.md
    if skill:
        txt = skill.read_text(encoding="utf-8")
        files.sort(key=lambda f: (txt.find(f.name) if f.name in txt else len(txt), f.name))
    return files


def split_args(items):
    paths, kv = [], []
    for it in items:
        if it == "alle":  # alle kaders van de skill waar dit script in staat, waar je het ook draait
            paths.extend(kaders_in_dir(Path(__file__).resolve().parent))
        elif "=" in it and not Path(it).exists():
            kv.append(it)
        elif Path(it).is_dir():
            paths.extend(kaders_in_dir(it))
        else:
            paths.append(Path(it))
    return paths, kv


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    for name in ("vragen", "stappen", "uitkomst", "samenhang", "document", "check", "info", "voorstel", "formulier"):
        p = sp.add_parser(name)
        p.add_argument("args", nargs="*" if name == "formulier" else "+", metavar="kader",
                       help="kaderbestand(en), een skillmap of 'alle' (alle kaders van deze skill), daarna eventueel sleutel=waarde")
        p.add_argument("--antwoorden", help="JSON-bestand of JSON-tekst met antwoorden")
        p.add_argument("--datum", help="datum van vandaag (JJJJ-MM-DD); standaard de systeemdatum")
        if name == "uitkomst":
            p.add_argument("--oordelen", required=True, help="JSON-bestand of JSON-tekst {toetspunt: uitkomst}")
        if name == "vragen":
            p.add_argument("--alles", action="store_true", help="ook al beantwoorde vragen tonen")
            p.add_argument("--voorgesteld", help="JSON-bestand of -tekst met de uitvoer van `voorstel`: die antwoorden "
                                                 "komen als één bevestigingsveld in de golf in plaats van als losse vragen")
        if name == "formulier":
            p.add_argument("--alles", action="store_true", help="ook al beantwoorde vragen tonen (voorgevuld)")
            p.add_argument("--voorgesteld", help="JSON-bestand of -tekst met de uitvoer van `voorstel`: voorgevulde antwoorden")
            p.add_argument("--html", action="store_true", help="HTML-fragment (glasformulier) in plaats van JSON")
            p.add_argument("--tekst", action="store_true", help="het hele formulier als één genummerde lijst (voor een bericht)")
            p.add_argument("--serve", metavar="UITVOER", help="zet het formulier op een lokale pagina, open de browser en schrijf "
                                                              "de antwoorden naar dit JSON-bestand zodra de gebruiker verstuurt")
            p.add_argument("--extra", help="JSON-bestand of -tekst met extra groepen vooraan: "
                                           "[{\"titel\": …, \"vragen\": [{\"sleutel\", \"vraag\", \"type\", \"opties\", \"hulp\", \"verplicht\"}]}]")
        if name == "document":
            p.add_argument("--tekst", action="store_true", help="alleen de samengestelde tekst tonen")
        if name == "voorstel":
            p.add_argument("--register", required=True, help="pad naar compliance-register.md")
    a = ap.parse_args(argv)
    paths, a.kv = split_args(a.args)
    if not paths and not (a.cmd == "formulier" and a.extra):
        sys.exit("geef minstens één kaderbestand of skillmap")
    ks = [parse_kader(p) for p in paths]
    multi = len(ks) > 1
    today = today_or(a.datum)
    label = "+".join(k["id"] for k in ks) or "formulier"
    if a.cmd == "check":
        out, rc = [], 0
        for k in ks:
            res = check(k)
            errs = [e for e in res if not e.startswith("WAARSCHUWING")]
            warns = [e[len("WAARSCHUWING: "):] for e in res if e.startswith("WAARSCHUWING")]
            out.append({"kader": k["id"], "fouten": errs, "waarschuwingen": warns})
            rc = rc or (1 if errs else 0)
        print(json.dumps(out if multi else out[0], ensure_ascii=False, indent=1))
        return rc
    facts = load_answers(a)
    unknown_keys = sorted(set(facts) - {q["key"] for k in ks for q in k["questions"]})
    if a.cmd == "info":
        infos = [{"kader": k["id"], "titel": k["title"], "versie": k.get("version"), "peildatum": k.get("peildatum"),
                  "soort": k["kind"], "vragen": len(k["questions"]), "toetspunten": len(k["steps"]),
                  "kwalificatievragen": k["qualification"], "poortregel": k.get("gate"),
                  "poortstap": k.get("poortstap"),
                  "van_toepassing_vanaf": [(d.isoformat(), e) for d, e in k.get("dates") or []]} for k in ks]
        out = {"kaders": infos} if multi else infos[0]
    elif a.cmd == "vragen":
        qs, later, skipped = open_questions(ks, facts, include_answered=a.alles, prioritize=False)
        gates = resolve_multi(ks, facts)[4]
        qual = set().union(*(set(k["qualification"]) for k in ks))
        vv = (a.voorgesteld or "").strip()
        raw_sug = _read_json_arg(vv) if vv and (vv.startswith("{") or Path(vv).exists()) else None  # geen bestand = geen voorstel
        velden = velden_voor_golf(qs, [k["id"] for k in ks], qual, raw_sug)
        aanroepen = batches(velden, AANROEP_MAX)
        out = {"kader": label, "nu_vragen": len(qs), "velden": len(velden), "aanroepen": aanroepen,
               "volgende_golf": len(later), "later": later, "vervallen": skipped, "klaar": not qs and not later,
               "uitleg": "Stel ALLE aanroepen uit 'aanroepen' in één blok (elke aanroep = één AskUserQuestion met "
                         "hooguit 4 velden). Draai dit pas opnieuw als de hele golf is beantwoord: de vragen onder "
                         "'later' komen dan vanzelf als volgende golf, tot 'klaar' true is."}
        if multi:
            out["kaders"] = [k["id"] for k in ks]
            out["poorten"] = {kid: ("geldt niet" if g is False else "wacht op " + ", ".join(w) if g == "pending"
                                    else "geldt") for kid, (g, w) in gates.items()}
    elif a.cmd == "formulier":
        vv = (a.voorgesteld or "").strip()
        raw_sug = _read_json_arg(vv) if vv and (vv.startswith("{") or Path(vv).exists()) else None
        ex = _read_json_arg(a.extra) if a.extra else None
        data = formulier_data(ks, facts, raw_sug, alles=a.alles, extra=ex)
        if a.serve:
            return formulier_serveren(data, a.serve)
        if a.tekst:
            print(formulier_tekst(data))
            return 0
        if a.html:
            print(formulier_html(data))
            return 0
        out = data
    elif a.cmd == "stappen":
        eff, _, _, _, gates = resolve_multi(ks, facts)
        per = [{"kader": k["id"], "geldt": gates[k["id"]][0] is not False,
                "stappen": step_status(k, facts, today=today, eff=eff, gate=gates[k["id"]][0])} for k in ks]
        out = {"kaders": per} if multi else {"kader": ks[0]["id"], "stappen": per[0]["stappen"]}
    elif a.cmd == "uitkomst":
        oordelen = _read_json_arg(a.oordelen)
        out = aggregate_multi(ks, facts, oordelen, today=today) if multi else aggregate(ks[0], facts, oordelen, today=today)
    elif a.cmd == "voorstel":
        prof = read_profile(a.register)
        sug, hints = {}, []
        for k in ks:
            s1, h1 = suggest_from_profile(k, prof)
            for key, v in s1.items():
                sug.setdefault(key, v)
            hints += [h for h in h1 if h not in hints]
        out = {"kader": label, "voorgesteld": sug, "hints": hints,
               "uitleg": "Geef deze uitvoer door aan `vragen --voorgesteld`: de antwoorden komen dan als één bevestigingsveld in de eerste golf; "
                         "een voorstel is pas een antwoord na bevestiging."}
    elif a.cmd == "samenhang":
        out = {"kader": label, "vervolg": follow_ups(ks, facts)}
    elif a.cmd == "document":
        docs = [k for k in ks if k["doc_items"]]
        if len(docs) != 1:
            sys.exit("document werkt met precies één opstel-kader")
        out = assemble(docs[0], facts)
        if a.tekst:
            print(out["tekst"])
            return 0
    if unknown_keys:
        out["waarschuwing"] = "onbekende antwoordsleutels genegeerd: " + ", ".join(unknown_keys)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
