"""Registre de dependències dels artefactes de 3r (què cal regenerar quan canvia una activitat).

Cada artefacte (PDF de docs/, PDF del bucket «professorat», fitxa digital, taules 10-11 i annexos de la
programació) declara de quins uid@versio depèn i guarda:
  - empremta: hash del contingut de les seves dependències (definició al YAML)
  - generador_hash: hash del generador (si és disponible; els de tools/3r/privat no són al repositori)
  - hash: hash del fitxer (sha256) o eTag de Supabase Storage per al bucket
Quan canvies el YAML o un generador, l'empremta canvia i --check diu CAL REGENERAR.

Ús:
  python3 tools/3r/artefactes.py --registra   recalcula i desa contingut/3r/artefactes.json (després de regenerar)
  python3 tools/3r/artefactes.py --check      compara amb el registre i diu què cal regenerar o què falta
  python3 tools/3r/artefactes.py --registra-imatges   desa el hash de les imatges que fa servir cada PDF (sense tocar res més)
  --bucket FITXER.json  llista d'objectes del bucket (per defecte contingut/3r/generat/bucket-professorat.json)"""
import hashlib, json, os, re, subprocess, sys, glob
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
C = os.path.join(ROOT, "contingut", "3r")
REG = os.path.join(C, "artefactes.json")
sys.path.insert(0, HERE)
import build_dades as B
sys.path.insert(0, os.path.join(HERE, "lib"))
import imatges as IM

GEN_SDA = {1: "gen_detectius.py", 2: "gen_sda1.py", 3: "gen_mobil.py", 4: "gen_hidrogen.py", 5: "gen_cel.py", 6: "gen_energia.py"}
PRIVAT = set(GEN_SDA.values()) | {"mn_ampl.py", "mn_adapt.py"}


def sha(b): return hashlib.sha256(b).hexdigest()
def hfile(p): return sha(open(p, "rb").read()) if os.path.exists(p) else None
def canon(o): return json.dumps(o, ensure_ascii=False, sort_keys=True).encode()


def gen_path(name):
    return os.path.join(HERE, "privat" if name in PRIVAT else "generadors", name)


def generator_for(k, sda):
    if re.match(r"^d\dsolamp$|^d\damp$", k): return "mn_ampl.py"
    if re.match(r"^d\dadap$|^d\dbas$", k): return "mn_adapt.py"
    if k.startswith("dcR"): return "mn_recup.py"
    if k == "dannex": return "gen_annexos.py"
    if k.startswith("dc"): return "gen_curs.py"
    return GEN_SDA.get(sda)


def taules_programacio(sdas, cur):
    """Taules 10 i 11 de la programació (criteris de cada CE per SdA) derivades de les evidències."""
    t = {}
    for s in sdas:
        for e in s["evidencies"]:
            for i in e["items"]:
                for c in i["criteris"]:
                    t.setdefault(f"CE{c.split('.')[0]}", {}).setdefault(s["sda"], set()).add(c)
    key = lambda x: [int(y) for y in x.split(".")]
    return {ce: {str(n): sorted(v, key=key) for n, v in sorted(d.items())} for ce, d in sorted(t.items())}


def taula10_full_md():
    md = open(os.path.join(HERE, "dades", "full.md")).read()
    a = md.index("| CE | Paper | SdA 1 |"); rows = md[a:].split("\n\n")[0].splitlines()[2:]
    t = {}
    for r in rows:
        cells = [c.strip() for c in r.strip("|").split("|")]
        if not cells or not cells[0].startswith("CE"): continue
        for n, v in enumerate(cells[2:], 1):
            if v: t.setdefault(cells[0], {})[str(n)] = [x.strip() for x in v.split(",")]
    return t


def compute(bucket_file):
    cur, com, sdas = B.load()
    out, docs = B.build(cur, com, sdas)
    sda_of = {}
    for s in sdas:
        for k in s["documents"]: sda_of[k] = s["sda"]
    ev_by_doc = {}
    for s in sdas:
        for e in s["evidencies"]:
            for k in e.get("instruments", []): ev_by_doc.setdefault(k, []).append(e)
    bucket = {o["nom"]: o for o in json.load(open(bucket_file))["objectes"]}
    fx = json.loads(subprocess.check_output(["node", "-e",
        "global.window={};require(process.argv[1]+'/digital/js/fitxes.js');const m=Object.keys(window.FITXES);require(process.argv[1]+'/digital/js/fitxes-auto.js');"
        "const o={};for(const[k,v]of Object.entries(window.FITXES))o[k]={manual:m.includes(k),spec:v};console.log(JSON.stringify(o));", ROOT]))
    A = {}
    def deps_for(k):
        d = docs[k]; dep = [f"{k}@{d['versio']}"]; defs = [d]
        for e in ev_by_doc.get(k, []):
            dep += [f"{e['uid']}@{e['versio']}"] + [f"{i['uid']}@{i['versio']}" for i in e["items"]]; defs.append(e)
        for p in d.get("digital", {}).get("preguntes", []): dep.append(f"{p['uid']}@{p['versio']}")
        return dep, defs
    for k, d in docs.items():
        dep, defs = deps_for(k)
        g = generator_for(k, sda_of.get(k))
        gh = hfile(gen_path(g)) if g else None
        emp = sha(canon(defs))
        if d.get("professorat"):
            o = bucket.get(d["fitxer"])
            local = os.path.join(ROOT, "docs", d["fitxer"])
            if o:
                ph, pnota = "etag:" + o["etag"], None
            elif os.path.exists(local):
                ph, pnota = hfile(local), "no és al bucket; la còpia que s'obre és docs/"
            else:
                ph, pnota = None, None
            rec = {"tipus": "pdf-professorat", "document": k, "generador": g, "generador_hash": gh,
                "depen_de": dep, "empremta": emp, "hash": ph}
            if pnota: rec["nota"] = pnota
            A[f"professorat/{d['fitxer']}"] = rec
        else:
            p = os.path.join(ROOT, "docs", d["fitxer"])
            A[f"docs/{d['fitxer']}"] = {"tipus": "pdf-alumnat", "document": k, "generador": g, "generador_hash": gh,
                "depen_de": dep, "empremta": emp, "hash": hfile(p)}
        if "digital" in d:
            spec = fx.get(k)
            if spec and not spec["manual"]:
                src = A.get(f"docs/{d['fitxer']}", {}).get("hash") or ""
                emp2 = sha(canon(d["digital"]) + src.encode() + (hfile(os.path.join(HERE, "generadors", "build_fitxes_auto.py")) or "").encode())
                g2 = "build_fitxes_auto.py (a partir del PDF)"
            else:
                emp2 = sha(canon(d["digital"])); g2 = "digital/js/fitxes.js (escrita a mà)"
            A[f"digital/{k}"] = {"tipus": "fitxa-digital", "document": k, "generador": g2,
                "depen_de": [f"{k}@{d['versio']}"] + [f"{p['uid']}@{p['versio']}" for p in d["digital"]["preguntes"]],
                "empremta": emp2, "hash": sha(canon(spec["spec"])) if spec else None}
    # programació
    tp = taules_programacio(sdas, cur)
    all_ev = [f"{i['uid']}@{i['versio']}" for s in sdas for e in s["evidencies"] for i in e["items"]]
    for t in ["taula10", "taula11"]:
        A[f"programacio/{t}"] = {"tipus": "programacio", "generador": "build_prog_final.py (tools/3r/dades/full.md)",
            "depen_de": ["curriculum@%d" % cur["versio"]] + all_ev, "empremta": sha(canon(tp)),
            "hash": sha(canon(taula10_full_md())), "coherent_amb_full_md": tp == taula10_full_md()}
    sda_v = [f"sda{s['sda']}@{s['versio']}" for s in sdas]
    ann_emp = sha(canon(sdas) + canon(cur) + (hfile(os.path.join(HERE, "dades", "full.md")) or "").encode() + (hfile(os.path.join(HERE, "generadors", "gen_annexos.py")) or "").encode())
    for key in ["docs/programacio-annexos.pdf", "professorat/programacio-annexos.pdf"]:
        if key in A:
            A[key]["depen_de"] = ["curriculum@%d" % cur["versio"]] + sda_v; A[key]["empremta"] = ann_emp
    if "professorat/programacio-annexos.pdf" not in A and "programacio-annexos.pdf" in bucket:
        A["professorat/programacio-annexos.pdf"] = {"tipus": "pdf-professorat", "document": None, "generador": "gen_annexos.py",
            "depen_de": ["curriculum@%d" % cur["versio"]] + sda_v, "empremta": ann_emp, "hash": "etag:" + bucket["programacio-annexos.pdf"]["etag"]}
    pub_ann = os.path.join(ROOT, "docs", "programacio-annexos.pdf")
    if os.path.exists(pub_ann):
        A["docs/programacio-annexos.pdf"] = {"tipus": "pdf-public", "document": None, "generador": "gen_annexos.py",
            "nota": "còpia pública dels annexos (el document dannex enllaça la del bucket)",
            "depen_de": ["curriculum@%d" % cur["versio"]] + sda_v, "empremta": ann_emp, "hash": hfile(pub_ann)}
    # objectes del bucket que cap document no enllaça
    linked = {a.split("/", 1)[1] for a in A if a.startswith("professorat/")}
    orfes = sorted(set(bucket) - linked)
    # PDF de docs/ sense document
    docs_pdf = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "docs", "*.pdf")))
    # Un PDF de docs/ enllaçat com a professorat (còpia de reserva) no és orfe.
    docs_linked = {a.split("/", 1)[1] for a in A if a.startswith(("docs/", "professorat/"))}
    return A, orfes, sorted(set(docs_pdf) - docs_linked), tp


def imatges_de(art, x):
    """Imatges (id → hash) que conté un artefacte. Font exacta: l'HTML que el generador deixa al costat del PDF
    (src="file://.../img/<id>"); si no hi és, s'analitza el codi del generador."""
    ids = IM.totes()
    nom = art.split("/", 1)[1]
    cands = [nom, nom.replace("-prova.pdf", "-demostracio-assoliment.pdf").replace("-solucionari-prova.pdf", "-solucionari-demostracio.pdf")]
    us = json.load(open(IM.US)) if os.path.exists(IM.US) else {}
    for c in cands:
        if c in us: return {i: IM.hash_(i) for i in us[c]}
    for d in [os.path.join(HERE, "privat", "docs"), os.path.join(ROOT, "docs")]:
        for c in cands:
            h = os.path.join(d, c.replace(".pdf", ".html"))
            if os.path.exists(h):
                txt = open(h, encoding="utf-8", errors="ignore").read()
                pre = "file://" + IM.DIR + "/"
                us = sorted({u for u in re.findall(re.escape(pre) + r"([^\"')\s]+)", txt) if u in ids})
                return {i: IM.hash_(i) for i in us}
    g = x.get("generador") or ""
    fonts = [gen_path(g.split()[0])] if g.endswith(".py") else []
    if x.get("tipus") in ("pdf-public", "pdf-professorat") and "annex" in art:
        fonts = [os.path.join(HERE, "generadors", f) for f in ("gen_annexos.py", "gen_annex_extra.py", "annex_samples.py")]
    txt = "".join(open(f, encoding="utf-8").read() for f in fonts if os.path.exists(f))
    return {i: IM.hash_(i) for i in IM.usades_per(txt, ids)} if txt else {}


def fix_suggestion(name, orfes):
    m = re.match(r"^(sda\d-\d\d)-", name)
    return [o for o in orfes if m and o.startswith(m.group(1) + "-")]


def main():
    a = sys.argv[1:]
    bf = a[a.index("--bucket") + 1] if "--bucket" in a else os.path.join(C, "generat", "bucket-professorat.json")
    A, orfes, docs_orfes, tp = compute(bf)
    for k, x in A.items():
        if x["tipus"].startswith("pdf"): x["imatges"] = imatges_de(k, x)
    if "--registra-imatges" in a:
        # només afegeix o actualitza el hash de les imatges al registre, sense marcar res més com a regenerat
        D = json.load(open(REG)); n = 0
        for k, x in A.items():
            if "imatges" in x and k in D["artefactes"]:
                D["artefactes"][k]["imatges"] = x["imatges"]; n += 1
        json.dump(D, open(REG, "w"), ensure_ascii=False, indent=1, sort_keys=True)
        print(f"Imatges registrades per a {n} artefactes"); return
    if "--registra" in a:
        json.dump({"nota": "Generat per tools/3r/artefactes.py --registra. Registra l'estat actual com a generat.", "artefactes": A},
                  open(REG, "w"), ensure_ascii=False, indent=1, sort_keys=True)
        print(f"Registrats {len(A)} artefactes a contingut/3r/artefactes.json")
    if "--check" in a or "--registra" not in a:
        R = json.load(open(REG))["artefactes"] if os.path.exists(REG) else {}
        stale, falta, manual, nous = [], [], [], []
        for k, x in sorted(A.items()):
            r = R.get(k)
            if x.get("hash") is None: falta.append(k)
            if not r: nous.append(k); continue
            motius = []
            if r["empremta"] != x["empremta"]:
                motius += sorted(set(x["depen_de"]) ^ set(r["depen_de"])) or ["definició al YAML modificada"]
            if r.get("imatges") is not None and x.get("imatges") is not None and r["imatges"] != x["imatges"]:
                canv = sorted(i for i in set(r["imatges"]) | set(x["imatges"]) if r["imatges"].get(i) != x["imatges"].get(i))
                motius = [f"imatge img/{i} canviada" for i in canv] + motius
            if not motius and r.get("generador_hash") and x.get("generador_hash") and r["generador_hash"] != x["generador_hash"]:
                motius = [f"generador {x['generador']} modificat"]
            if motius:
                stale.append((k, motius))
            elif r.get("hash") != x["hash"] and x.get("hash") is not None: manual.append(k)
        for k, x in A.items():
            if x.get("coherent_amb_full_md") is False and k not in [s[0] for s in stale]:
                stale.append((k, ["les evidències del YAML no coincideixen amb la taula de full.md"]))
        print(f"Artefactes: {len(A)} · al registre: {len(R)}")
        for k, ch in stale: print(f"  CAL REGENERAR  {k}" + (f"  ({', '.join(ch[:6])}{'…' if len(ch) > 6 else ''})" if ch else ""))
        for k in manual: print(f"  MODIFICAT FORA DEL REGISTRE  {k} (fes --registra si és correcte)")
        for k in nous: print(f"  NOU (no registrat)  {k}")
        for k in falta:
            sug = fix_suggestion(k.split("/", 1)[1], orfes) if k.startswith("professorat/") else []
            print(f"  FALTA  {k}  ← enllaçat per {A[k].get('document')}" + (f" · al bucket hi ha: {', '.join(sug)}" if sug else " · no hi ha cap fitxer equivalent: cal generar-lo"))
        if orfes: print(f"  Al bucket sense cap enllaç: {', '.join(orfes)}")
        if docs_orfes: print(f"  A docs/ sense cap document: {', '.join(docs_orfes)}")
        if not (stale or manual or falta): print("  Tot al dia.")
        if "--check" in a and (stale or falta): sys.exit(1)


if __name__ == "__main__":
    main()
