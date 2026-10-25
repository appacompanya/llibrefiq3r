"""Construeix les dades del llibre de 3r a partir de la font única (contingut/3r/*.yaml) i les valida.

Genera:
  digital/js/dades-generades.js      window.FQ3_DADES = {D, D_alumne, L, L_arrel, SDAS, SDAS_alumne, EVAL, CRIT_NAMES}
  contingut/3r/generat/uids.json     índex de tots els uid amb la seva versio (per a la base de dades i artefactes.py)

Valida (i ho diu clarament; no canvia mai el contingut pedagògic):
  - uid únics; ítems d'avaluació únics dins de cada SdA (el registre els desa per SdA + id)
  - criteris existents al currículum; els 21 criteris s'avaluen almenys una vegada
  - CE avaluades a cada SdA = ce_aprovades (repartiment aprovat)
  - documents referenciats a les sessions existeixen
  - les fitxes digitals publicades (digital/js/fitxes*.js) no tenen camps que no siguin al YAML
  - (--respostes DIR) cada (worksheet_id, item_id) de responses/feedback/submissions té un uid

Ús:
  python3 tools/3r/build_dades.py                  genera i valida
  python3 tools/3r/build_dades.py --compara        a més, compara el resultat amb els blocs escrits a mà de les 3 pàgines
  python3 tools/3r/build_dades.py --respostes /workspace/backups/2026-10-24
  python3 tools/3r/build_dades.py --aplica-html    escriu els blocs generats dins de les 3 pàgines (font única → web)
  python3 tools/3r/build_dades.py --mapa FITXER    copia el mapa SdA → evidències → criteris → CE
  --estricte: surt amb error si hi ha avisos de validació (per a CI)."""
import json, os, re, subprocess, sys, glob
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
C = os.path.join(ROOT, "contingut", "3r")
SES = {"titol": "t", "fase": "ph", "text": "p", "mitja": "half", "docs": "d", "docs_professorat": "dt", "enllacos": "l"}
TEA = {"bloc": "b", "text": "s", "docs": "d", "url": "u", "url_text": "ul"}
RESERVATS = {"_paste", "_global"}   # item_id tècnics: indici d'enganxat i comentari global


def load():
    cur = yaml.safe_load(open(os.path.join(C, "curriculum.yaml")))
    com = yaml.safe_load(open(os.path.join(C, "comuns.yaml")))
    sdas = [yaml.safe_load(open(f)) for f in sorted(glob.glob(os.path.join(C, "sda", "sda*.yaml")), key=lambda f: int(re.search(r"(\d+)\.yaml$", f).group(1)))]
    return cur, com, sdas


def build(cur, com, sdas):
    docs = dict(com["documents"])
    for s in sdas:
        for k, d in s["documents"].items():
            if k in docs: raise SystemExit(f"document {k} definit dues vegades")
            docs[k] = d
    order = [k for k in com["ordre_documents"] if k in docs] + [k for k in docs if k not in com["ordre_documents"]]
    D, DA = {}, {}
    for k in order:
        d = docs[k]
        e = {"f": d["fitxer"], "l": d["titol"]}
        if d.get("professorat"): e["t"] = 1
        else: DA[k] = dict(e)
        D[k] = e
    L = com["enllacos"]
    LA = {k: ({**v, "u": com["enllacos_url_arrel"][k]} if k in com["enllacos_url_arrel"] else v) for k, v in L.items()}
    S, SA, EVAL = [], [], {}
    for s in sdas:
        ses = [{SES[k]: v for k, v in x.items()} for x in s["sessions"]]
        base = {"n": s["sda"], "c": s["color"], "title": s["titol"], "q": s["repte"], "meta": s["meta"], "ready": s["publicada"]}
        S.append({**base, "sessions": ses, "teacher": [{TEA[k]: v for k, v in x.items()} for x in s["professorat"]]})
        SA.append({**base, "sessions": [{k: v for k, v in x.items() if k != "dt"} for x in ses], "teacher": []})
        EVAL[str(s["sda"])] = [{"id": e["id"], "l": e["titol"], "items": [
            {"id": i["id"], "l": i["titol"], "c": i["criteris"], **({"d": i["descriptors"]} if "descriptors" in i else {})}
            for i in e["items"]]} for e in s["evidencies"]]
    CRIT = {c["id"]: c["nom_curt"] for ce in cur["competencies"] for c in ce["criteris"]}
    return {"D": D, "D_alumne": DA, "L": L, "L_arrel": LA, "SDAS": S, "SDAS_alumne": SA, "EVAL": EVAL, "CRIT_NAMES": CRIT}, docs


def uids_index(cur, com, sdas, docs):
    U = {}
    def add(uid, **kw):
        if uid in U and U[uid] != kw: raise ValueError(uid)
        U[uid] = kw
    errs = []
    for ce in cur["competencies"]:
        for c in ce["criteris"]: U[f"crit.{c['id']}"] = {"tipus": "criteri", "ce": ce["id"], "versio": cur["versio"]}
    for k, d in docs.items():
        try: add(k, tipus="document", versio=d["versio"], sda=d.get("digital", {}).get("sda"))
        except ValueError: errs.append(f"uid repetit: {k}")
        for p in d.get("digital", {}).get("preguntes", []):
            try: add(p["uid"], tipus="pregunta", versio=p["versio"], document=k)
            except ValueError: errs.append(f"uid repetit: {p['uid']}")
            for c in p["camps"]:
                if c == p["uid"]: continue
                try: add(c, tipus="camp", versio=p["versio"], document=k, pregunta=p["uid"])
                except ValueError: errs.append(f"uid repetit: {c}")
    for s in sdas:
        for e in s["evidencies"]:
            try: add(e["uid"], tipus="evidencia", versio=e["versio"], sda=s["sda"])
            except ValueError: errs.append(f"uid repetit: {e['uid']}")
            for i in e["items"]:
                try: add(i["uid"], tipus="item_avaluacio", versio=i["versio"], sda=s["sda"], evidencia=e["uid"], criteris=i["criteris"])
                except ValueError: errs.append(f"uid repetit: {i['uid']}")
    return U, errs


def validate(cur, com, sdas, docs, out):
    W = []
    crit = {c["id"]: ce["id"] for ce in cur["competencies"] for c in ce["criteris"]}
    if len(cur["competencies"]) != 6 or len(crit) != 21:
        W.append(f"el currículum ha de tenir 6 CE i 21 criteris (en té {len(cur['competencies'])} i {len(crit)})")
    for ce in cur["competencies"]:
        for c in ce["criteris"]:
            if c.get("pendent"): W.append(f"criteri {c['id']}: {c['pendent']}")
    covered = {}
    for s in sdas:
        n = s["sda"]; ces = set(); ids = {}
        for e in s["evidencies"]:
            for i in e["items"]:
                if i["id"] in ids: W.append(f"SdA {n}: l'ítem «{i['id']}» és a {ids[i['id']]} i a {e['id']} (el registre els confondria)")
                ids[i["id"]] = e["id"]
                for c in i["criteris"]:
                    if c not in crit: W.append(f"SdA {n}: {i['uid']} avalua el criteri {c}, que no existeix"); continue
                    ces.add(crit[c]); covered.setdefault(c, set()).add(n)
        ap = set(s["ce_aprovades"])
        falten, sobren = sorted(ap - ces), sorted(ces - ap)
        if falten or sobren:
            W.append(f"SdA {n}: CE aprovades {', '.join(sorted(ap))}; avaluades {', '.join(sorted(ces))}"
                     + (f" · FALTEN {', '.join(falten)}" if falten else "") + (f" · SOBREN {', '.join(sobren)}" if sobren else ""))
        prin, sec = s.get("ce_principals") or [], s.get("ce_secundaria") or []
        if len(sec) > 1:
            W.append(f"SdA {n}: com a màxim una CE secundària (n'hi ha {len(sec)})")
        if set(prin) & set(sec) or set(prin) | set(sec) != ap:
            W.append(f"SdA {n}: ce_principals {prin} i ce_secundaria {sec} no coincideixen amb ce_aprovades {sorted(ap)}")
        if any("pes" in e for e in s["evidencies"]):
            W.append(f"SdA {n}: encara hi ha pesos (pes:) a les evidències; l'avaluació és qualitativa, sense percentatges")
        for x in s["sessions"] + s["professorat"]:
            for k in x.get("docs", []) + x.get("docs_professorat", []):
                if k not in docs: W.append(f"SdA {n}: la sessió «{x.get('titol') or x.get('bloc')}» fa servir el document {k}, que no existeix")
    nc = [c for c in crit if c not in covered]
    if nc: W.append(f"criteris que no s'avaluen enlloc: {', '.join(nc)}")
    once = sorted((c for c, v in covered.items() if len(v) == 1), key=lambda x: [int(y) for y in x.split('.')])
    info = [f"criteris avaluats: {len(covered)}/21; avaluats en una sola SdA: {len(once)} ({', '.join(once)})"]
    # fitxes publicades vs YAML
    js = r"""global.window={};require(process.argv[1]+'/digital/js/fitxes.js');const m=new Set(Object.keys(window.FITXES));
require(process.argv[1]+'/digital/js/fitxes-auto.js');const o={};
for(const[k,f]of Object.entries(window.FITXES)){const c=[];if(m.has(k)){for(const b of f.blocks){if(!b.id)continue;if(b.type==='group')b.items.forEach(x=>c.push(String(x.id)));else c.push(String(b.id));}}else Object.keys(f.fields||{}).forEach(x=>c.push(x));o[k]=c;}
console.log(JSON.stringify(o));"""
    pub = json.loads(subprocess.check_output(["node", "-e", js, ROOT]))
    for ws, camps in pub.items():
        d = docs.get(ws)
        if not d or "digital" not in d: W.append(f"la fitxa digital {ws} no és al YAML"); continue
        y = {c for p in d["digital"]["preguntes"] for c in p["camps"]}
        nous = [c for c in camps if f"{ws}.{c}" not in y]
        if nous: W.append(f"fitxa {ws}: camps publicats sense uid al YAML: {', '.join(nous)}")
        if len(set(camps)) != len(camps): W.append(f"fitxa {ws}: camps repetits a la fitxa publicada")
        falten = [c for c in sorted(y) if c.split(".", 1)[1] not in camps and not any(p.get("retirada") for p in d["digital"]["preguntes"] if c in p["camps"])]
        if falten: W.append(f"fitxa {ws}: camps del YAML que ja no són a la fitxa publicada (marca la pregunta com a retirada: true): {', '.join(falten)}")
    for k, d in docs.items():
        if "digital" in d and k not in pub: W.append(f"{k} té fitxa digital al YAML però no a digital/js")
    return W, info


def orphans(dirpath, U, docs):
    res = {}
    for t in ["responses", "feedback", "submissions"]:
        f = os.path.join(dirpath, f"public.{t}.json")
        if not os.path.exists(f): continue
        rows = json.load(open(f)); bad = {}
        for r in rows:
            ws, it = r["worksheet_id"], r.get("item_id")
            if ws not in docs: bad.setdefault(f"{ws} (document)", 0); bad[f"{ws} (document)"] += 1; continue
            if it is None: continue
            base = it[5:] if it.startswith("auto:") else it
            if base in RESERVATS or f"{ws}.{base}" in U: continue
            bad[f"{ws}.{it}"] = bad.get(f"{ws}.{it}", 0) + 1
        res[t] = (len(rows), bad)
    return res


def mapa(cur, sdas, docs):
    """Mapa final SdA → evidències → instruments → criteris → CE (per a qui escriu la programació)."""
    key = lambda x: [int(y) for y in x.split(".")]
    crit = {c["id"]: {"ce": ce["id"], "nom_curt": c["nom_curt"], "text": c["text"]} for ce in cur["competencies"] for c in ce["criteris"]}
    out = {"generat_per": "tools/3r/build_dades.py --mapa", "font": "contingut/3r (font única)",
           "terminologia": "«activitat de demostració d'assoliment» (no «prova»): és el terme del web, del llibre i de la programació; "
                           "l'identificador intern de l'evidència continua sent «prova» (uid sN.prova) perquè no es pot canviar. "
                           "Es conserva «prova de la flama» com a procediment de laboratori.",
           "avaluacio": "Qualitativa (NA, AS, AN, AE). Sense pesos: el nivell d'un criteri i d'una CE és la mitjana no ponderada "
                        "dels aspectes on apareixen, arrodonida a l'alça. Dues CE principals per SdA i, com a màxim, una de secundària "
                        "si té evidència amb rúbrica. La nota automàtica de les fitxes digitals formatives és orientativa i no entra "
                        "a la mitjana oficial. Les fitxes qualificadores es valoren a la rúbrica de l'evidència, no amb el nivell automàtic agregat.",
           "competencies": {ce["id"]: ce["text"] for ce in cur["competencies"]}, "criteris": crit, "sda": []}
    cov = {}
    for s in sdas:
        evs = []
        for e in s["evidencies"]:
            cs = sorted({c for i in e["items"] for c in i["criteris"]}, key=key)
            for c in cs: cov.setdefault(c, []).append(s["sda"])
            evs.append({"uid": e["uid"], "titol": e["titol"], "versio": e["versio"], "tipus": "qualificadora",
                        "instruments": [{"uid": k, "fitxer": docs[k]["fitxer"], "titol": docs[k]["titol"],
                                         "on": "bucket professorat" if docs[k].get("professorat") else "docs/ (alumnat)",
                                         "avaluacio": docs[k].get("avaluacio"),
                                         **({"part_qualificadora": docs[k]["part_qualificadora"]} if docs[k].get("part_qualificadora") else {})}
                                        for k in e.get("instruments", [])],
                        "criteris": cs, "ce": sorted({crit[c]["ce"] for c in cs}),
                        "items": [{"uid": i["uid"], "titol": i["titol"], "criteris": i["criteris"], "versio": i["versio"]} for i in e["items"]]})
        cs = sorted({c for e in evs for c in e["criteris"]}, key=key)
        out["sda"].append({"sda": s["sda"], "titol": s["titol"], "repte": s["repte"],
                           "ce_principals": s.get("ce_principals") or [], "ce_secundaria": s.get("ce_secundaria") or [],
                           "ce": sorted({crit[c]["ce"] for c in cs}),
                           "ce_aprovades": s["ce_aprovades"], "criteris": cs, "evidencies": evs})
    # taules 10 (CE × SdA) i 11 (SdA × CE)
    t10 = {ce["id"]: {str(s["sda"]): sorted([c for c in s["criteris"] if crit[c]["ce"] == ce["id"]], key=key) for s in out["sda"]} for ce in cur["competencies"]}
    out["taula10_ce_x_sda"] = t10
    out["taula11_sda_x_ce"] = {str(s["sda"]): {ce: [c for c in s["criteris"] if crit[c]["ce"] == ce] for ce in out["competencies"]} for s in out["sda"]}
    out["resum"] = {"evidencies": sum(len(s["evidencies"]) for s in out["sda"]),
                    "criteris_coberts": f"{len(cov)}/{len(crit)}",
                    "criteris_una_sola_sda": [c for c in sorted(cov, key=key) if len(set(cov[c])) == 1],
                    "sda_per_criteri": {c: sorted(set(v)) for c, v in sorted(cov.items(), key=lambda x: key(x[0]))}}
    return out


PAGINES = [("digital/profe.html", {"D": "D", "L": "L", "SDAS": "SDAS", "EVAL": "EVAL", "CRIT_NAMES": "CRIT_NAMES"}),
           ("digital/index.html", {"D": "D_alumne", "L": "L", "SDAS": "SDAS_alumne"}),
           ("index.html", {"D": "D_alumne", "L": "L_arrel", "SDAS": "SDAS_alumne"})]


def lit(v):
    """Literal JS llegible: una entrada per línia al primer nivell."""
    if isinstance(v, dict):
        return "{\n" + ",\n".join(f"  {json.dumps(k, ensure_ascii=False)}: {json.dumps(x, ensure_ascii=False)}" for k, x in v.items()) + "\n}"
    if isinstance(v, list):
        return "[\n" + ",\n".join("  " + json.dumps(x, ensure_ascii=False) for x in v) + "\n]"
    return json.dumps(v, ensure_ascii=False)


def aplica_html(out):
    """Substitueix els blocs const D/L/SDAS/EVAL/CRIT_NAMES de les 3 pàgines pels generats (marcats)."""
    js = ("const grab=require(process.argv[1]+'/tools/3r/lib/jsliteral.js');const f=process.argv[2];const r={};"
          "for(const n of JSON.parse(process.argv[3])){const g=grab(f,n);r[n]=[g.start,g.end];}console.log(JSON.stringify(r));")
    for f, blocs in PAGINES:
        path = os.path.join(ROOT, f)
        pos = json.loads(subprocess.check_output(["node", "-e", js, ROOT, path, json.dumps(list(blocs))]))
        txt = open(path, encoding="utf-8").read()
        # node dóna posicions en unitats UTF-16 (els emojis en compten 2): les convertim a índexs de Python
        u16 = txt.encode("utf-16-le")
        cp = lambda i: len(u16[:2 * i].decode("utf-16-le"))
        pos = {n: (cp(a), cp(b)) for n, (a, b) in pos.items()}
        for n, (a, b) in sorted(pos.items(), key=lambda x: -x[1][0]):
            marca = "/* generat per tools/3r/build_dades.py a partir de contingut/3r: no l'editis a mà */\n"
            pre = txt[:a]
            new = ("" if pre.endswith(marca) else marca) + f"const {n} = {lit(out[blocs[n]])}"
            txt = txt[:a] + new + txt[b:]
        open(path, "w", encoding="utf-8").write(txt)
        print(f"  {f}: {', '.join(blocs)} actualitzats")


def js_out(o):
    return ("/* Generat per tools/3r/build_dades.py a partir de contingut/3r/*.yaml. No l'editis a mà:\n"
            "   edita el YAML i torna a executar l'script. */\n"
            "window.FQ3_DADES = " + json.dumps(o, ensure_ascii=False, indent=1) + ";\n")


COMPARA = r"""
const grab=require(process.argv[1]+'/tools/3r/lib/jsliteral.js');const R=process.argv[1];
global.window={};require(R+'/digital/js/dades-generades.js');const G=window.FQ3_DADES;
const canon=(x)=>Array.isArray(x)?x.map(canon):(x&&typeof x==='object')?Object.fromEntries(Object.keys(x).sort().map(k=>[k,canon(x[k])])):x;
const J=JSON.stringify;const res=[];
const cases=[['digital/profe.html','D','D'],['digital/profe.html','L','L'],['digital/profe.html','SDAS','SDAS'],['digital/profe.html','EVAL','EVAL'],['digital/profe.html','CRIT_NAMES','CRIT_NAMES'],
['digital/index.html','D','D_alumne'],['digital/index.html','L','L'],['digital/index.html','SDAS','SDAS_alumne'],
['index.html','D','D_alumne'],['index.html','L','L_arrel'],['index.html','SDAS','SDAS_alumne']];
for(const[f,n,g]of cases){const v=grab(R+'/'+f,n).val;res.push({pagina:f,bloc:n,generat:g,identic_amb_ordre:J(v)===J(G[g]),equivalent:J(canon(v))===J(canon(G[g]))});}
console.log(JSON.stringify(res));"""


def main():
    a = sys.argv[1:]
    cur, com, sdas = load()
    out, docs = build(cur, com, sdas)
    U, uerr = uids_index(cur, com, sdas, docs)
    W, info = validate(cur, com, sdas, docs, out)
    W = uerr + W
    open(os.path.join(ROOT, "digital", "js", "dades-generades.js"), "w").write(js_out(out))
    os.makedirs(os.path.join(C, "generat"), exist_ok=True)
    json.dump(U, open(os.path.join(C, "generat", "uids.json"), "w"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"Generat digital/js/dades-generades.js i contingut/3r/generat/uids.json ({len(U)} uid)")
    for i in info: print("·", i)
    print(f"\nValidació: {len(W)} avís(os)")
    for w in W: print("  ✗", w)
    if "--respostes" in a:
        d = a[a.index("--respostes") + 1]
        print("\nRespostes desades sense uid (orfes):")
        for t, (n, bad) in orphans(d, U, docs).items():
            print(f"  {t}: {n} files, {sum(bad.values())} orfes" + (f" → {bad}" if bad else ""))
            if bad: W.append(f"orfes a {t}")
    if "--aplica-html" in a:
        print("\nActualitzo les pàgines amb les dades generades:"); aplica_html(out)
    if "--compara" in a:
        r = json.loads(subprocess.check_output(["node", "-e", COMPARA, ROOT]))
        print("\nComparació amb els blocs escrits a mà:")
        for x in r:
            st = "IDÈNTIC" if x["identic_amb_ordre"] else ("EQUIVALENT (només canvia l'ordre de claus)" if x["equivalent"] else "DIFERENT")
            print(f"  {x['pagina']:20} {x['bloc']:10} ← {x['generat']:12} {st}")
    M = mapa(cur, sdas, docs)
    json.dump(M, open(os.path.join(C, "generat", "mapa_ce.json"), "w"), ensure_ascii=False, indent=1)
    print(f"Mapa de CE: contingut/3r/generat/mapa_ce.json ({M['resum']['evidencies']} evidències, criteris {M['resum']['criteris_coberts']})")
    if "--mapa" in a:
        dst = a[a.index("--mapa") + 1]; os.makedirs(os.path.dirname(dst), exist_ok=True)
        json.dump(M, open(dst, "w"), ensure_ascii=False, indent=1); print(f"  i còpia a {dst}")
    if "--estricte" in a and W: sys.exit(1)


if __name__ == "__main__":
    main()
