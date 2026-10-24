"""Extracció única (fase 1): converteix el JSON de extreu_contingut.js en la font única contingut/3r/*.yaml.
Els identificadors són EXACTAMENT els actuals (claus de D, worksheet_id i item_id de la base de dades,
id de les evidències i dels ítems d'EVAL). No es renumera res. Totes les entrades comencen a versio: 1.

Ús: node tools/3r/extreu_contingut.js > /tmp/extret.json
    python3 tools/3r/extreu_contingut.py /tmp/extret.json
Després d'aquesta extracció, la font de veritat és el YAML: no tornis a executar aquest script
si ja has editat el YAML (el sobreescriuria)."""
import json, os, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "contingut", "3r")
X = json.load(open(sys.argv[1]))
if os.path.exists(os.path.join(OUT, "curriculum.yaml")) and "--força" not in sys.argv:
    sys.exit("contingut/3r ja existeix: la font de veritat ja és el YAML. Fes servir --força només si saps què fas.")

# Repartiment de CE per SdA aprovat per l'usuari (24/10/2026)
CE_APROVADES = {1: ["CE2", "CE3", "CE5"], 2: ["CE1", "CE2", "CE4"], 3: ["CE1", "CE5", "CE6"],
                4: ["CE1", "CE2", "CE3"], 5: ["CE1", "CE2", "CE5"], 6: ["CE1", "CE4", "CE6"]}
LEGACY_SDA2 = {"ruta", "repte", "rub", "lab", "f1", "f2", "labc", "inf", "video", "mapa", "prova", "solpr", "diana", "solf2"}


class Dumper(yaml.SafeDumper):
    pass
def _str(d, s):
    if "\n" in s: return d.represent_scalar("tag:yaml.org,2002:str", s, style="|")
    return d.represent_scalar("tag:yaml.org,2002:str", s)
Dumper.add_representer(str, _str)
def dump(obj, path, head):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(head)
        yaml.dump(obj, f, Dumper=Dumper, allow_unicode=True, sort_keys=False, width=1000)

# ---------- currículum (textos literals de la programació, dades/full.md) ----------
md = open(os.path.join(HERE, "dades", "full.md")).read()
ces = []
for m in re.finditer(r"\*\*Competència específica (\d)\.\*\* (.+)", md):
    ces.append({"id": f"CE{m.group(1)}", "text": m.group(2).strip(), "criteris": []})
for m in re.finditer(r"^\| (\d\.\d) (.+?) \| [\d, ]+ \|$", md, re.M):
    cid, text = m.group(1), m.group(2).strip()
    ce = ces[int(cid[0]) - 1]
    if any(c["id"] == cid for c in ce["criteris"]): continue
    c = {"id": cid, "nom_curt": X["CRIT_NAMES"].get(cid), "text": text}
    if not text.endswith("."):
        c["pendent"] = "Text tallat a la programació (full.md): cal completar-lo amb el literal del Decret 175/2022."
    ce["criteris"].append(c)
dump({"font": "Decret 175/2022, annex 3 (Física i química, 1r a 3r d'ESO). Textos copiats de la programació (tools/3r/dades/full.md); noms curts de CRIT_NAMES (digital/profe.html).",
      "versio": 1, "competencies": ces},
     os.path.join(OUT, "curriculum.yaml"),
     "# Font única del currículum de 3r. No inventis textos: han de ser literals del decret.\n")

# ---------- documents ----------
D, F = X["D"], X["FITXES"]
def sda_of(k):
    m = re.match(r"^d([1-6])", k)
    if m: return int(m.group(1))
    if k in LEGACY_SDA2: return 2
    return 0
SES_KEYS = {"t": "titol", "ph": "fase", "p": "text", "half": "mitja", "d": "docs", "dt": "docs_professorat", "l": "enllacos"}
TEA_KEYS = {"b": "bloc", "s": "text", "d": "docs", "u": "url", "ul": "url_text"}
def ren(o, M):
    unk = set(o) - set(M)
    if unk: raise SystemExit(f"clau desconeguda {unk} a {o}")
    return {M[k]: v for k, v in o.items()}

def doc_entry(k):
    d = D[k]
    e = {"uid": k, "versio": 1, "fitxer": d["f"], "titol": d["l"]}
    unk = set(d) - {"f", "l", "t"}
    if unk: raise SystemExit(f"clau desconeguda a D[{k}]: {unk}")
    if d.get("t"): e["professorat"] = True
    if k in F:
        fx = F[k]
        e["digital"] = {"origen": fx["origen"], "titol": fx["titol"], "sda": fx["sda"], "preguntes": [
            {"uid": f"{k}.{p['id']}", "id": p["id"], "versio": 1, "tipus": p["tipus"], "etiqueta": p["etiqueta"],
             "criteris": [], "camps": [f"{k}.{c}" for c in p["camps"]]} for p in fx["preguntes"]]}
    return e

docs_by = {}
for k in D: docs_by.setdefault(sda_of(k), []).append(k)
extra = [k for k in F if k not in D]
if extra: raise SystemExit(f"fitxes digitals sense entrada a D: {extra}")

L, LA = X["L"], X["L_arrel"]
arrel = {k: LA[k]["u"] for k in L if LA[k] != L[k]}
assert all(set(LA[k]) == set(L[k]) and {x: y for x, y in LA[k].items() if x != "u"} == {x: y for x, y in L[k].items() if x != "u"} for k in L)
dump({"versio": 1,
      "ordre_documents": list(D.keys()),
      "enllacos": L,
      "enllacos_url_arrel": arrel,
      "documents": {k: doc_entry(k) for k in docs_by.get(0, [])}},
     os.path.join(OUT, "comuns.yaml"),
     "# Documents del curs (sessió 0, tancament, enquesta, recuperacions, annexos) i enllaços (L).\n"
     "# ordre_documents: ordre de D a les pàgines (els documents nous que no hi siguin s'afegeixen al final).\n"
     "# enllacos_url_arrel: URL diferent a /index.html (les pàgines de /digital/ hi afegeixen ../).\n")

EV = X["EVAL"]
for s in X["SDAS"]:
    n = s["n"]
    unk = set(s) - {"n", "c", "title", "q", "meta", "ready", "sessions", "teacher"}
    if unk: raise SystemExit(f"clau desconeguda a SDAS[{n}]: {unk}")
    evs = []
    for ev in EV[str(n)]:
        cand = [f"d{n}{ev['id']}"] + ([ev["id"]] if n == 2 else [])
        if ev["id"] == "prova": cand += [f"d{n}solpr"] + (["solpr"] if n == 2 else [])
        inst = [k for k in cand if k in D]  # només coincidències exactes de nom; la resta, per revisar a mà
        e = {"uid": f"s{n}.{ev['id']}", "id": ev["id"], "versio": 1, "titol": ev["l"], "instruments": inst, "items": []}
        for it in ev["items"]:
            i = {"uid": f"s{n}.{ev['id']}.{it['id']}", "id": it["id"], "versio": 1, "titol": it["l"], "criteris": it["c"]}
            if "d" in it: i["descriptors"] = it["d"]
            e["items"].append(i)
        evs.append(e)
    obj = {"sda": n, "versio": 1, "color": s["c"], "titol": s["title"], "repte": s["q"], "meta": s["meta"], "publicada": s["ready"],
           "ce_aprovades": CE_APROVADES[n],
           "sessions": [ren(x, SES_KEYS) for x in s["sessions"]],
           "professorat": [ren(x, TEA_KEYS) for x in s.get("teacher", [])],
           "documents": {k: doc_entry(k) for k in docs_by.get(n, [])},
           "evidencies": evs}
    dump(obj, os.path.join(OUT, "sda", f"sda{n}.yaml"),
         f"# SdA {n}: font única (sessions, documents, fitxes digitals, evidències i criteris).\n"
         "# uid = identificador estable (el mateix que a la base de dades). No el canviïs mai ni el reutilitzis.\n"
         "# versio: puja-la quan el canvi sigui de fons (canvia què es pregunta o què s'avalua); les errates no.\n"
         "# Els camps d'una pregunta hereten la versio de la pregunta.\n")
print("fet:", OUT)
