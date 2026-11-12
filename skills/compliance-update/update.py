#!/usr/bin/env python3
"""Rekenhulp voor /compliance-update (alleen standaardbibliotheek).

  python3 update.py lokaal        geïnstalleerde versie en waar die vandaan komt (JSON)
  python3 update.py check         vergelijkt met de nieuwste versie op GitHub en toont de wijzigingen sinds jouw versie (JSON)
  python3 update.py oud [map]     zoekt losse oude skills (chat, overzicht, onboarding) in ~/.claude/skills of de gegeven map (JSON)

`check` leest de publieke repository (zonder inloggen); lukt dat niet, dan probeert het `gh api` of een token in GITHUB_TOKEN of GH_TOKEN.
Lukt niets, dan staat er `"nieuwste": null` en een reden; de update zelf werkt dan nog steeds via de plugincommando's.
"""
import base64
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = "Lawskills/IT-law-compliance"
BRANCH = "main"
OUD = ["chat", "overzicht", "onboarding"]  # oude namen vóór compliance-chat/-overzicht/-onboarding


def versie_tuple(v):
    return tuple(int(x) for x in re.findall(r"\d+", v)[:3]) if v else ()


def lokaal():
    # 1. als plugin: skills/<naam>/ staat twee mappen onder de pluginroot met .claude-plugin/plugin.json
    for up in (HERE.parent.parent, HERE.parent.parent.parent):
        pj = up / ".claude-plugin" / "plugin.json"
        if pj.exists():
            data = json.loads(pj.read_text(encoding="utf-8"))
            return {"versie": data.get("version"), "bron": "plugin", "pad": str(up)}
    # 2. losse skill (Claude.ai of ~/.claude/skills): versie.txt naast dit bestand
    vt = HERE / "versie.txt"
    if vt.exists():
        return {"versie": vt.read_text(encoding="utf-8").strip(), "bron": "versie.txt", "pad": str(HERE)}
    return {"versie": None, "bron": None, "pad": str(HERE)}


def github_raw(path):
    """Geeft (tekst, reden). Eerst de publieke raw-URL, dan gh, dan token."""
    reden = ""
    try:
        with urllib.request.urlopen(f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{path}", timeout=30) as resp:
            tekst = resp.read().decode("utf-8")
            if tekst.strip():
                return tekst, None
    except Exception as e:  # noqa: BLE001
        reden = f"publiek: {type(e).__name__}; "
    try:
        r = subprocess.run(["gh", "api", f"repos/{REPO}/contents/{path}", "-H", "Accept: application/vnd.github.raw"],
                           capture_output=True, text=True, timeout=30)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout, None
        reden += (r.stderr or r.stdout).strip()[:200] or "gh gaf geen uitvoer"
    except (OSError, subprocess.SubprocessError) as e:
        reden += f"gh niet beschikbaar ({type(e).__name__})"
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        try:
            req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/contents/{path}",
                                         headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github.raw"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8"), None
        except Exception as e:  # noqa: BLE001
            reden += f"; token: {type(e).__name__}"
    return None, reden


def nieuwe_regels(changelog, sinds):
    """Kopjes '## datum · x.y.z — titel' met een versie hoger dan `sinds`, met hun inhoud."""
    delen = re.split(r"^(?=## )", changelog, flags=re.M)
    uit = []
    for d in delen:
        m = re.match(r"## .*?· (\d+\.\d+\.\d+)", d)
        if m and versie_tuple(m.group(1)) > versie_tuple(sinds):
            uit.append(d.strip())
    return uit


def check():
    lok = lokaal()
    out = {"geïnstalleerd": lok["versie"], "bron": lok["bron"], "nieuwste": None, "nieuwer": None, "wijzigingen": [], "reden": None}
    pj, reden = github_raw(".claude-plugin/plugin.json")
    if pj is None:
        out["reden"] = f"GitHub niet bereikbaar: {reden}"
        return out
    out["nieuwste"] = json.loads(pj).get("version")
    out["nieuwer"] = versie_tuple(out["nieuwste"]) > versie_tuple(lok["versie"]) if lok["versie"] else None
    if out["nieuwer"] or lok["versie"] is None:
        cl, reden = github_raw("CHANGELOG.md")
        if cl:
            out["wijzigingen"] = nieuwe_regels(cl, lok["versie"] or "0.0.0")
        else:
            out["reden"] = f"CHANGELOG niet opgehaald: {reden}"
    return out


def oud(map_=None):
    basis = Path(map_).expanduser() if map_ else Path.home() / ".claude" / "skills"
    gevonden = []
    for n in OUD:
        p = basis / n
        if (p / "SKILL.md").exists():
            gevonden.append(str(p))
    return {"map": str(basis), "oude_skills": gevonden}


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "lokaal"
    if cmd == "lokaal":
        res = lokaal()
    elif cmd == "check":
        res = check()
    elif cmd == "oud":
        res = oud(argv[2] if len(argv) > 2 else None)
    else:
        print(__doc__)
        return 2
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
