"""Genera les dades de les adaptacions (window.FQ_ADAPT) d'un curs.
   3r: contingut/3r/adaptacions.yaml → digital/js/adaptacions-dades.js
   2n: contingut/2n/adaptacions.yaml → 2n/digital/js/adaptacions-dades.js (perfils i llengues es comparteixen amb 3r)
   Ús: python3 -B tools/3r/build_adaptacions.py [3r|2n]"""
import json, os, sys, yaml
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
curs = sys.argv[1] if len(sys.argv) > 1 else "3r"
base = yaml.safe_load(open(os.path.join(ROOT, "contingut", "3r", "adaptacions.yaml"), encoding="utf-8"))
d = base if curs == "3r" else yaml.safe_load(open(os.path.join(ROOT, "contingut", curs, "adaptacions.yaml"), encoding="utf-8"))
perfils = d.get("perfils") or base["perfils"]; llengues = d.get("llengues") or base.get("llengues", [])
P = set(perfils)
for k, v in (d.get("fitxes") or {}).items():
    for p, x in (v or {}).items():
        if p not in P: sys.exit(f"{k}: perfil desconegut {p}")
        if x != "no_cal" and not isinstance(x, dict): sys.exit(f"{k}/{p}: ha de ser no_cal o un diccionari")
        if isinstance(x, dict):
            if "treu" in x and (p != "basics" or not isinstance(x["treu"], list)): sys.exit(f"{k}/{p}: «treu» només a basics i com a llista")
            if "redueix" in x and (p != "basics" or not isinstance(x["redueix"], dict)): sys.exit(f"{k}/{p}: «redueix» només a basics i com a diccionari")
            x["treu"] = [str(i) for i in x.get("treu", [])] if "treu" in x else x.pop("treu", None) or None
            if x.get("treu") is None: x.pop("treu", None)
out = {"perfils": perfils, "llengues": llengues, "glossari": {str(k): v for k, v in (d.get("glossari") or {}).items()}, "fitxes": d.get("fitxes") or {}}
p = os.path.join(ROOT, *([] if curs == "3r" else [curs]), "digital", "js", "adaptacions-dades.js")
open(p, "w", encoding="utf-8").write(f"/* Generat per tools/3r/build_adaptacions.py a partir de contingut/{curs}/adaptacions.yaml. No l'editis a mà. */\nwindow.FQ_ADAPT = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n")
print("Generat", os.path.relpath(p, ROOT), "·", sum(len(v) for v in out["glossari"].values()), "paraules ·", len(out["fitxes"]), "fitxes amb decisions")
