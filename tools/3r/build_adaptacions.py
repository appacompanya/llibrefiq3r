"""Genera digital/js/adaptacions-dades.js (window.FQ_ADAPT) a partir de contingut/3r/adaptacions.yaml."""
import json, os, sys, yaml
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
d = yaml.safe_load(open(os.path.join(ROOT, "contingut", "3r", "adaptacions.yaml"), encoding="utf-8"))
P = set(d["perfils"])
for k, v in (d.get("fitxes") or {}).items():
    for p, x in (v or {}).items():
        if p not in P: sys.exit(f"{k}: perfil desconegut {p}")
        if x != "no_cal" and not isinstance(x, dict): sys.exit(f"{k}/{p}: ha de ser no_cal o un diccionari")
out = {"perfils": d["perfils"], "llengues": d.get("llengues", []), "glossari": {str(k): v for k, v in d["glossari"].items()}, "fitxes": d.get("fitxes") or {}}
p = os.path.join(ROOT, "digital", "js", "adaptacions-dades.js")
open(p, "w", encoding="utf-8").write("/* Generat per tools/3r/build_adaptacions.py a partir de contingut/3r/adaptacions.yaml. No l'editis a mà. */\nwindow.FQ_ADAPT = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n")
print("Generat", os.path.relpath(p, ROOT), "·", sum(len(v) for v in out["glossari"].values()), "paraules ·", len(out["fitxes"]), "fitxes amb decisions")
