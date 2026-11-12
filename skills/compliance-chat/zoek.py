#!/usr/bin/env python3
"""Zoekt in de bronnendatabase van /compliance-chat en in de kaderteksten van de overige skills.

  python3 zoek.py bronnen <term> [<term> ...]   alle termen moeten voorkomen (hoofdletterongevoelig); een frase tussen aanhalingstekens, bijvoorbeeld "art. 32"
  python3 zoek.py id <bronid>                   toont één bron
  python3 zoek.py kader <term> [<term> ...]     zoekt in kaderbestanden van de naastliggende skills
  python3 zoek.py pad                           toont waar de kaderbestanden worden gezocht
Uitvoer: alleen wat in de bestanden staat; niets wordt aangevuld.
"""
import sys, os, glob, re
HIER = os.path.dirname(os.path.abspath(__file__))
KADER = re.compile(r"^(K|AI|CK|CB|C|W)[0-9]+[a-z]?-[a-z0-9-]+\.md$")
SKIP = re.compile(r"^(SKILL|bepalingen|huisstijl-sjabloon|kaderkaart|register-sjabloon|onboarding-vragen|toepasselijkheid|widgets)\.md$|^bronnen-")


def bron_regels():
    for f in sorted(glob.glob(os.path.join(HIER, "bronnen-*.md"))):
        for l in open(f, encoding="utf-8"):
            if l.count(" | ") >= 6 and not l.startswith("#"):
                yield os.path.basename(f), l.rstrip("\n")


def kader_dirs():
    out = []
    for base in (os.path.dirname(HIER), "/mnt/skills/user", "/mnt/skills", os.path.expanduser("~/.claude/skills")):
        if os.path.isdir(base) and base not in out:
            out.append(base)
    return out


def kaderbestanden():
    seen, res = set(), []
    for base in kader_dirs():
        for p in glob.glob(os.path.join(base, "*", "*.md")):
            n = os.path.basename(p)
            if not KADER.match(n):
                continue  # alleen kaderbestanden van deze set (bijv. K2-grondslag.md), geen bestanden van andere skills
            if SKIP.match(n) or os.path.basename(os.path.dirname(p)) in ("compliance-chat", "compliance-overzicht", "compliance-onboarding"):
                continue
            key = (os.path.basename(os.path.dirname(p)), n)
            if key not in seen:
                seen.add(key); res.append(p)
    return res


def main(a):
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); return 0
    cmd, terms = a[0], [t.lower() for t in a[1:]]
    if cmd == "pad":
        print("\n".join(kader_dirs())); print(len(kaderbestanden()), "kaderbestanden gevonden"); return 0
    if cmd == "bronnen":
        n = 0
        for f, l in bron_regels():
            if all(t in l.lower() for t in terms):
                print(l); n += 1
                if n >= 40: print("... (meer dan 40 treffers; verfijn met extra termen)"); break
        if not n: print("Geen treffers in de bronnendatabase.")
    elif cmd == "id":
        hit = [l for f, l in bron_regels() if l.split(" | ")[0].lower() == terms[0]]
        print("\n".join(hit) if hit else "Dit id staat niet in de bronnendatabase.")
    elif cmd == "kader":
        fs, n = kaderbestanden(), 0
        if not fs: print("Geen kaderbestanden van andere skills gevonden; antwoord dan alleen uit de bronnenindex en zeg dat."); return 0
        for p in fs:
            sk = os.path.basename(os.path.dirname(p))
            for i, l in enumerate(open(p, encoding="utf-8"), 1):
                if all(t in l.lower() for t in terms):
                    print(f"{sk}/{os.path.basename(p)}:{i}: {l.strip()[:300]}"); n += 1
                    if n >= 40: print("... (meer dan 40 treffers; verfijn)"); return 0
        if not n: print("Geen treffers in de kaderbestanden.")
    else:
        raise SystemExit("Onbekend commando; zie --help")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except BrokenPipeError:
        sys.exit(0)
