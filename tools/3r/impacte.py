"""Graf d'impacte de 3r: què queda afectat quan canvia una peça, i què es pot fer.

La font única és contingut/3r/*.yaml. Aquest mòdul no regenera PDF ni crida
artefactes.py --registra (això amagaria la deriva dels fulls no regenerats).

L'únic pas que «actua» executa és:

  python3 tools/3r/build_dades.py --aplica-html --estricte

Escriu el web (index.html, digital/index.html, digital/profe.html),
digital/js/dades-generades.js, contingut/3r/generat/mapa_ce.json i uids.json.

La resta queda PENDENT MANUAL. Els generadors de SdA (gen_detectius, gen_sda1,
gen_mobil, gen_hidrogen, gen_cel, gen_energia, mn_ampl, mn_adapt) no són al git
i el kit de referència és anterior al mapa de CE, a la SdA 6 de 8 sessions i
als GS/MG. Els que sí són al repo i importen gen_sda1 (gen_curs, gen_annexos,
mn_recup, gen_multinivell, …) tampoc s'executen. build_fitxes_auto.py està
aturat: no escriu la fitxa publicada.

Ús:
  python3 tools/3r/impacte.py consulta REF
  python3 tools/3r/impacte.py actua REF
  python3 tools/3r/impacte.py comprova
  python3 tools/3r/artefactes.py --impacte REF
  python3 tools/3r/artefactes.py --actua REF

REF pot ser un uid (d5f5, s5.difu, s5.difu.x2, 2.3, CE2), una sessió
(sessio:5:7 o «sda5 sessio 7»), una SdA (sda5), un camí
(contingut/3r/sda/sda5.yaml, tools/3r/dades/full.md, docs/….pdf, img/….png)
o mapa_ce. --json imprimeix el pla. --complet no abrevia les llistes.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
C = os.path.join(ROOT, "contingut", "3r")
sys.path.insert(0, HERE)
import artefactes as ART
import build_dades as B

PAS_WEB = "build_dades"
WEB_FITXERS = (
    "index.html",
    "digital/index.html",
    "digital/profe.html",
    "digital/js/dades-generades.js",
)
MOTIU_PRIVAT = (
    "no és al git (tools/3r/privat). El kit de referència (18/10/2026) és anterior "
    "al mapa de CE, a la SdA 6 de 8 sessions i als GS/MG de la SdA 5. No s'executa."
)
IMPORTA_PRIVAT = {
    "gen_curs.py": "importa gen_sda1.py",
    "gen_annexos.py": "importa gen_sda1.py i llegeix full.md i sdas.json, no el YAML",
    "mn_recup.py": "importa gen_sda1.py; el text de les CE hi és copiat, no surt del YAML",
    "gen_multinivell.py": "importa gen_sda1.py, mn_ampl.py i mn_adapt.py",
    "gen_llibre.py": "importa gen_sda1.py",
    "gen_recursos.py": "importa gen_curs.py i gen_sda1.py",
    "mn_common.py": "importa gen_sda1.py",
    "annex_fitxes.py": "importa gen_sda1.py",
    "ruta.py": "importa gen_sda1.py",
    "gen_calendari.py": "llegeix annex_groups.json (G/M/L), no el booleà mitja del YAML",
    "gen_annex_extra.py": "no llegeix contingut/3r/*.yaml",
    "gen_anims.py": "escriu sim-*.html dins de tools/3r/generadors/, no les còpies publicades de l'arrel",
    "build_prog_final.py": "edita el Word de la programació; no és un pas segur",
    "build_fitxes_auto.py": "reconstrueix les fitxes des dels generadors privats i està aturat: no escriu digital/js/fitxes-auto.js",
    "build_web.py": "camí antic: reescriuria la web des de template.html",
    "build_site.py": "camí antic, retirat",
    "build_digital.py": "camí antic de 3r, retirat",
    "build_profe_digital.py": "camí antic, retirat",
    "export_links.js": "camí antic, retirat",
}


class Graf:
    def __init__(self):
        self.nodes = {}
        self.afecta = {}
        self.revisa = {}
        self.conte = {}
        self.usa = {}
        self.alias = {}

    def node(self, id_, **kw):
        self.nodes[id_] = {"id": id_, "estat": "info", "motiu": "", "comanda": None, "nota": "", "curt": id_, **kw}
        self.afecta.setdefault(id_, [])
        self.revisa.setdefault(id_, [])
        self.usa.setdefault(id_, [])
        self.alias.setdefault(id_, [id_])
        return self.nodes[id_]

    def aresta(self, a, b):
        if b not in self.nodes or a not in self.nodes:
            raise KeyError((a, b))
        if b not in self.afecta[a]:
            self.afecta[a].append(b)

    def revisio(self, a, b):
        if b not in self.nodes or a not in self.nodes:
            raise KeyError((a, b))
        if b not in self.revisa[a]:
            self.revisa[a].append(b)

    def ali(self, nom, id_):
        lst = self.alias.setdefault(nom, [])
        if id_ not in lst:
            lst.append(id_)


def comanda_build_dades():
    return [sys.executable, os.path.join(HERE, "build_dades.py"), "--aplica-html", "--estricte"]


def format_cmd(cmd):
    show = list(cmd)
    if os.path.basename(show[0]).startswith("python"):
        show[0] = "python3"
    if len(show) > 1 and os.path.isabs(show[1]):
        show[1] = os.path.relpath(show[1], ROOT)
    return " ".join(show)


def base_generador(g):
    if not g:
        return ""
    return g.split()[0]


def motiu_generador(generador):
    base = base_generador(generador)
    if not base:
        return "No hi ha generador conegut. PENDENT MANUAL."
    if base in ART.PRIVAT:
        return f"{base} {MOTIU_PRIVAT}"
    if "fitxes.js" in generador:
        return "La fitxa és a digital/js/fitxes.js, escrita a mà. No hi ha generador segur."
    if base in IMPORTA_PRIVAT:
        return f"{base} és al repo però {IMPORTA_PRIVAT[base]}. PENDENT MANUAL. No s'executa."
    if base.endswith(".py") or base.endswith(".js"):
        return f"{base} no és un pas segur (l'únic executable és build_dades.py). PENDENT MANUAL."
    return f"{generador} PENDENT MANUAL. No s'executa."


def _rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def construeix(bucket_file):
    cur, com, sdas = B.load()
    _out, docs = B.build(cur, com, sdas)
    A, orfes, docs_orfes, _tp = ART.compute(bucket_file)
    g = Graf()

    def N(id_, **kw):
        return g.node(id_, **kw)

    N("sortida:web", tipus="sortida", curt="web", etiqueta="Web (D, L, SDAS, EVAL, CRIT_NAMES)",
      font=", ".join(WEB_FITXERS), estat="aplica", comanda=PAS_WEB,
      motiu="Blocs de les tres pàgines i digital/js/dades-generades.js. El navegador no carrega dades-generades.js: --aplica-html el copia a les pàgines.")
    N("sortida:mapa_ce", tipus="sortida", curt="mapa_ce", etiqueta="Mapa SdA → evidències → criteris → CE",
      font="contingut/3r/generat/mapa_ce.json", estat="aplica", comanda=PAS_WEB,
      motiu="El torna a escriure build_dades.py. No s'edita a mà.")
    N("sortida:uids", tipus="sortida", curt="uids", etiqueta="Índex d'uid",
      font="contingut/3r/generat/uids.json", estat="aplica", comanda=PAS_WEB,
      motiu="El torna a escriure build_dades.py. No s'edita a mà.")
    N("sortida:calendari", tipus="sortida", curt="calendari", etiqueta="Calendari horitzontal",
      font="tools/3r/generadors/gen_calendari.py", estat="manual",
      motiu=motiu_generador("gen_calendari.py"))

    def font(path, etiqueta):
        fid = "font:" + path
        N(fid, tipus="font", curt=os.path.basename(path), etiqueta=etiqueta, font=path, estat="info",
          motiu="Fitxer font. El que cal regenerar és a les conseqüències.")
        g.ali(path, fid)
        g.ali(os.path.basename(path), fid)
        return fid

    fcur = font("contingut/3r/curriculum.yaml", "Currículum (CE i criteris)")
    fcom = font("contingut/3r/comuns.yaml", "Documents de curs i enllaços")
    fmd = font("tools/3r/dades/full.md", "Text de la programació")
    g.nodes[fmd]["motiu"] = "Còpia per als annexos i les taules 10-11. El web no la llegeix. No es reescriu des del YAML."
    g.nodes[fmd]["estat"] = "manual"
    fjson = font("tools/3r/dades/sdas.json", "Còpia de títols, reptes i sessions per als annexos")
    g.nodes[fjson]["motiu"] = (
        "La llegeix gen_annexos.py. El web llegeix el YAML. No es reescriu sola: a les SdA 1–4 el JSON té el camp half "
        "i el YAML encara no té el booleà mitja."
    )
    g.nodes[fjson]["estat"] = "manual"
    fgrp = font("tools/3r/generadors/annex_groups.json", "Cadena G/M/L del calendari")
    g.nodes[fgrp]["motiu"] = (
        "G = grup sencer, M = mig grup, L = laboratori en mig grup. El YAML només té mitja (GS/MG) a les SdA 5 i 6, "
        "i no distingeix L de M. No es recalcula sola."
    )
    g.nodes[fgrp]["estat"] = "manual"
    g.ali("mapa_ce", "sortida:mapa_ce")
    g.ali("mapa_ce.json", "sortida:mapa_ce")
    g.ali("contingut/3r/generat/mapa_ce.json", "sortida:mapa_ce")
    g.ali("uids.json", "sortida:uids")
    g.ali("contingut/3r/generat/uids.json", "sortida:uids")
    for f in WEB_FITXERS:
        g.ali(f, "sortida:web")

    for ce in cur["competencies"]:
        cid = f"ce:{ce['id']}"
        N(cid, tipus="ce", curt=ce["id"], etiqueta=ce["id"], font="contingut/3r/curriculum.yaml")
        g.ali(ce["id"], cid)
        g.ali(ce["id"].lower(), cid)
        g.aresta(fcur, cid)
        g.conte[cid] = []
        for c in ce["criteris"]:
            qid = f"criteri:{c['id']}"
            N(qid, tipus="criteri", curt=c["id"], etiqueta=f"{c['id']} {c['nom_curt']}", font="contingut/3r/curriculum.yaml")
            g.ali(c["id"], qid)
            g.ali(f"crit.{c['id']}", qid)
            g.ali(f"criteri:{c['id']}", qid)
            g.conte[cid].append(qid)
            g.aresta(fcur, qid)
            g.aresta(qid, "sortida:web")
            g.aresta(qid, "sortida:mapa_ce")
            g.aresta(qid, "sortida:uids")
            g.revisio(qid, fmd)

    arts = {}
    for k, meta in A.items():
        aid = f"artefacte:{k}"
        motiu = motiu_generador(meta.get("generador") or "")
        if meta.get("tipus") == "programacio":
            motiu = (
                "La taula surt de les evidències del YAML i s'ha de llegir igual a full.md. "
                "build_prog_final.py no s'executa. Un canvi només de text o de nom curt no altera els ids; "
                "sí que ho fa moure un criteri d'ítem."
            )
        curt = k
        N(aid, tipus="artefacte", curt=curt, etiqueta=k, font=k, estat="manual", motiu=motiu,
          clase=meta.get("tipus") or "", generador=meta.get("generador") or "", document=meta.get("document"),
          nota=meta.get("nota") or "")
        g.ali(k, aid)
        base = k.split("/", 1)[-1]
        g.ali(base, aid)
        if base.endswith(".pdf"):
            g.ali(base[:-4] + ".html", aid)
        arts[k] = aid

    annex_ids = [arts[k] for k in A if k.endswith("programacio-annexos.pdf")]
    taula_ids = [arts[k] for k in A if k.startswith("programacio/")]
    for aid in annex_ids:
        g.nodes[aid]["motiu"] = motiu_generador("gen_annexos.py")

    def arts_de(uid):
        return [aid for k, aid in arts.items() if A[k].get("document") == uid]

    rubric = {}
    owner = {}
    for s in sdas:
        for k in s["documents"]:
            owner[k] = s["sda"]
    for k, d in docs.items():
        if k.endswith("rub") or "rubri" in (d.get("fitxer") or ""):
            if k in owner:
                rubric.setdefault(owner[k], []).append(k)

    ce_doc = {}
    for n in range(1, 7):
        if f"dcR{n}" in docs:
            ce_doc[f"CE{n}"] = f"dcR{n}"

    for s in sdas:
        n = s["sda"]
        sid = f"sda:{n}"
        fsda = font(f"contingut/3r/sda/sda{n}.yaml", f"SdA {n}")
        N(sid, tipus="sda", curt=f"SdA {n}", etiqueta=f"SdA {n} · {s['titol']}", font=f"contingut/3r/sda/sda{n}.yaml")
        g.ali(f"sda{n}", sid)
        g.ali(f"SdA {n}", sid)
        g.ali(f"SdA{n}", sid)
        g.ali(str(n), sid)
        g.aresta(fsda, sid)
        for dest in ("sortida:web", "sortida:mapa_ce", "sortida:uids", "sortida:calendari"):
            g.aresta(sid, dest)
        for aid in taula_ids + annex_ids:
            g.aresta(sid, aid)
        g.revisio(sid, fmd)
        g.revisio(sid, fjson)
        g.revisio(sid, fgrp)
        for ce in s.get("ce_aprovades") or []:
            if f"ce:{ce}" in g.nodes:
                g.usa[f"ce:{ce}"].append(sid)

        sessions = []
        for i, ses in enumerate(s["sessions"], 1):
            grup = None
            if "mitja" in ses:
                grup = "MG" if ses["mitja"] else "GS"
            qid = f"sessio:{n}:{i}"
            et = f"Sessió {i} · {ses.get('titol') or ''}" + (f" · {grup}" if grup else "")
            refs = list(ses.get("docs") or []) + list(ses.get("docs_professorat") or [])
            N(qid, tipus="sessio", curt=f"sessió {i}" + (f" {grup}" if grup else ""), etiqueta=et,
              font=f"contingut/3r/sda/sda{n}.yaml", grup=grup, refs=refs, sda=n)
            g.ali(qid, qid)
            g.ali(f"sda{n} sessio {i}", qid)
            g.ali(f"SdA {n} sessió {i}", qid)
            sessions.append(qid)
            g.aresta(sid, qid)
            g.aresta(qid, "sortida:web")
            g.aresta(qid, "sortida:calendari")
            for aid in annex_ids:
                g.aresta(qid, aid)
            g.revisio(qid, fmd)
            g.revisio(qid, fjson)
            g.revisio(qid, fgrp)

        blocs = []
        for i, b in enumerate(s.get("professorat") or [], 1):
            bid = f"bloc:{n}:{i}"
            refs = list(b.get("docs") or [])
            N(bid, tipus="bloc", curt=b.get("bloc") or f"bloc {i}", etiqueta=f"Professorat · {b.get('bloc') or i}",
              font=f"contingut/3r/sda/sda{n}.yaml", refs=refs, sda=n)
            blocs.append(bid)
            g.aresta(sid, bid)
            g.aresta(bid, "sortida:web")

        documents = []
        for k in s["documents"]:
            documents.append(f"document:{k}")
        evidencies = []
        for e in s["evidencies"]:
            evidencies.append(f"evidencia:{e['uid']}")
        g.conte[sid] = sessions + blocs + documents + evidencies

    for k, d in docs.items():
        did = f"document:{k}"
        on = "bucket professorat" if d.get("professorat") else "docs/ (alumnat)"
        N(did, tipus="document", curt=k, etiqueta=f"{k} · {d.get('titol') or ''}", font=d.get("fitxer") or "",
          on=on, sda=owner.get(k))
        g.ali(k, did)
        g.ali(f"document:{k}", did)
        pregs = []
        for p in d.get("digital", {}).get("preguntes") or []:
            pid = f"pregunta:{p['uid']}"
            N(pid, tipus="pregunta", curt=p["uid"], etiqueta=p.get("etiqueta") or p["uid"], font=k)
            g.ali(p["uid"], pid)
            pregs.append(pid)
            g.aresta(pid, "sortida:uids")
            camps = []
            for c in p.get("camps") or []:
                if c == p["uid"]:
                    continue
                cid = f"camp:{c}"
                if cid not in g.nodes:
                    N(cid, tipus="camp", curt=c, etiqueta=c, font=k)
                    g.ali(c, cid)
                camps.append(cid)
                g.aresta(cid, pid)
            g.conte[pid] = camps
        g.conte[did] = pregs
        dests = arts_de(k)
        for aid in dests:
            g.aresta(did, aid)
            for pid in pregs:
                g.aresta(pid, aid)
        g.aresta(did, "sortida:web")
        g.aresta(did, "sortida:uids")
        if k in com.get("documents", {}):
            g.aresta(fcom, did)
        if k in owner:
            g.aresta(f"sda:{owner[k]}", did)

    for k, meta in A.items():
        if meta.get("tipus") != "fitxa-digital":
            continue
        doc = meta.get("document")
        for key, aid in arts.items():
            if A[key].get("document") == doc and str(A[key].get("tipus", "")).startswith("pdf"):
                g.aresta(aid, arts[k])

    # Enllaços i referències de sessió / bloc / evidència (ara que els documents existeixen).
    for ek, ev in (com.get("enllacos") or {}).items():
        eid = f"enllac:{ek}"
        N(eid, tipus="enllac", curt=ek, etiqueta=ev.get("l") or ek, font="contingut/3r/comuns.yaml")
        g.ali(ek, eid)
        g.aresta(eid, "sortida:web")
        g.aresta(fcom, eid)
    g.aresta(fcom, "sortida:web")

    for s in sdas:
        n = s["sda"]
        for i, ses in enumerate(s["sessions"], 1):
            qid = f"sessio:{n}:{i}"
            for dk in list(ses.get("docs") or []) + list(ses.get("docs_professorat") or []):
                did = f"document:{dk}"
                if did in g.nodes:
                    g.usa[did].append(qid)
            for ek in ses.get("enllacos") or []:
                eid = f"enllac:{ek}"
                if eid in g.nodes:
                    g.usa[eid].append(qid)
        for i, b in enumerate(s.get("professorat") or [], 1):
            bid = f"bloc:{n}:{i}"
            for dk in b.get("docs") or []:
                did = f"document:{dk}"
                if did in g.nodes:
                    g.usa[did].append(bid)
        rubs = [f"document:{k}" for k in rubric.get(n, []) if f"document:{k}" in g.nodes]
        for e in s["evidencies"]:
            eid = f"evidencia:{e['uid']}"
            N(eid, tipus="evidencia", curt=e["uid"], etiqueta=e.get("titol") or e["uid"],
              font=f"contingut/3r/sda/sda{n}.yaml", sda=n)
            g.ali(e["uid"], eid)
            g.aresta(f"sda:{n}", eid)
            items = []
            for it in e["items"]:
                iid = f"item:{it['uid']}"
                N(iid, tipus="item", curt=it["uid"], etiqueta=it.get("titol") or it["uid"],
                  font=f"contingut/3r/sda/sda{n}.yaml", criteris=list(it.get("criteris") or []), sda=n)
                g.ali(it["uid"], iid)
                items.append(iid)
                g.aresta(iid, eid)
                for c in it.get("criteris") or []:
                    qid = f"criteri:{c}"
                    if qid in g.nodes:
                        g.aresta(qid, iid)
                        g.usa[qid].append(iid)
            g.conte[eid] = items
            for dk in e.get("instruments") or []:
                did = f"document:{dk}"
                if did in g.nodes:
                    g.usa[did].append(eid)
                    g.aresta(eid, did)
                    g.aresta(did, "sortida:mapa_ce")
            for did in rubs:
                g.aresta(eid, did)
                if eid not in g.usa[did]:
                    g.usa[did].append(eid)
            for dest in ("sortida:web", "sortida:mapa_ce", "sortida:uids"):
                g.aresta(eid, dest)
            for aid in taula_ids + annex_ids:
                g.aresta(eid, aid)
            g.revisio(eid, fmd)

    for ce, dk in ce_doc.items():
        cid = f"ce:{ce}"
        did = f"document:{dk}"
        if cid in g.nodes and did in g.nodes:
            g.aresta(cid, did)
            g.usa[did].append(cid)
    for cid, node in list(g.nodes.items()):
        if node["tipus"] == "ce":
            g.aresta(cid, "sortida:mapa_ce")
            for aid in annex_ids:
                g.aresta(cid, aid)
            g.revisio(cid, fmd)

    for aid in annex_ids:
        g.aresta(fmd, aid)
        g.aresta(fjson, aid)
    for aid in taula_ids:
        g.aresta(fmd, aid)
    g.aresta(fgrp, "sortida:calendari")

    per_img = {k: set() for k in A}
    us_path = os.path.join(C, "generat", "imatges-us.json")
    if os.path.exists(us_path):
        us = json.load(open(us_path))
        for k in A:
            for i in us.get(k.split("/", 1)[-1], []):
                per_img[k].add(i)
    if os.path.exists(ART.REG):
        reg = json.load(open(ART.REG)).get("artefactes", {})
        for k, meta in reg.items():
            if k in per_img:
                per_img[k].update((meta.get("imatges") or {}))
    vistes = set(ART.IM.totes())
    for ids in per_img.values():
        vistes.update(ids)
    for img in sorted(vistes):
        iid = f"imatge:{img}"
        N(iid, tipus="imatge", curt=img, etiqueta=img, font=f"img/{img}", estat="info",
          motiu="El web enllaça img/ directament i es veu nova sense regenerar HTML. Els PDF que la porten queden pendents.")
        g.ali(img, iid)
        g.ali(f"img/{img}", iid)
        for k, ids in per_img.items():
            if img in ids:
                g.aresta(iid, arts[k])

    for nom in orfes:
        oid = f"orf:professorat/{nom}"
        N(oid, tipus="orfe", curt=nom, etiqueta=nom, font="bucket professorat", estat="manual",
          motiu="És al bucket i cap document del YAML l'enllaça. No es regenera des d'aquí.")
        g.ali(nom, oid)
    for nom in docs_orfes:
        oid = f"orf:docs/{nom}"
        if oid in g.nodes:
            continue
        N(oid, tipus="orfe", curt=nom, etiqueta=nom, font=f"docs/{nom}", estat="manual",
          motiu="És a docs/ i cap document del YAML l'enllaça.")
        g.ali(nom, oid)
        g.ali(f"docs/{nom}", oid)

    g.annex_ids = annex_ids
    g.taula_ids = taula_ids
    return g


_CACHE = {}


def graf(bucket=None):
    bf = bucket or os.path.join(C, "generat", "bucket-professorat.json")
    if bf not in _CACHE:
        _CACHE[bf] = construeix(bf)
    return _CACHE[bf]


def normalitza(ref):
    s = re.sub(r"\s+", " ", ref.strip())
    if s.startswith(ROOT + "/"):
        s = s[len(ROOT) + 1:]
    s = s.replace("\\", "/")
    m = re.fullmatch(r"(?i)sda\s*(\d)\s+sessi[oó]\s+(\d+)", s)
    if m:
        return f"sessio:{int(m.group(1))}:{int(m.group(2))}"
    m = re.fullmatch(r"(?i)sdas?\s*(\d)", s)
    if m:
        return f"sda:{int(m.group(1))}"
    m = re.fullmatch(r"(?i)ce\s*(\d)", s)
    if m:
        return f"CE{m.group(1)}"
    return s


def resol(g, ref):
    ref = normalitza(ref)
    if not ref:
        return []
    if ref in g.nodes and not ref.startswith("font:") and g.alias.get(ref) == [ref]:
        return [ref]
    if ref in g.nodes and ref not in g.alias:
        return [ref]
    hits = list(g.alias.get(ref, []))
    if ref in g.nodes and ref not in hits:
        hits.insert(0, ref)
    # Un nom de fitxer ha d'apuntar a l'artefacte, no al document que el comparteix per casualitat.
    if "/" in ref or ref.endswith((".pdf", ".html", ".md", ".yaml", ".json", ".png", ".jpg", ".svg", ".webp")):
        arts = [h for h in hits if h.startswith("artefacte:") or h.startswith("font:") or h.startswith("sortida:") or h.startswith("imatge:") or h.startswith("orf:")]
        if arts:
            hits = arts
    # uid de peça abans que un àlies curt ambigu: si hi ha una peça amb aquest id, queda.
    peces = [h for h in hits if h.split(":", 1)[0] in ("document", "evidencia", "item", "pregunta", "camp", "criteri", "ce", "sessio", "sda")]
    if peces and not ref.startswith(("docs/", "professorat/", "img/", "digital/")):
        hits = peces
    # «5» és la SdA 5, no una coincidència accidental.
    if re.fullmatch(r"[1-6]", ref):
        hits = [f"sda:{ref}"] if f"sda:{ref}" in g.nodes else hits
    # Desambiguació: el mateix PDF al bucket i a docs/.
    return list(dict.fromkeys(hits))


def tanca(g, origins):
    parent = {o: None for o in origins}
    q = list(origins)
    i = 0
    while i < len(q):
        a = q[i]
        i += 1
        for b in g.afecta.get(a, []):
            if b in parent:
                continue
            parent[b] = a
            q.append(b)
    rparent = {}
    revisio = []
    for a in q:
        for b in g.revisa.get(a, []):
            if b in parent or b in rparent:
                continue
            rparent[b] = a
            revisio.append(b)
    return q, parent, revisio, rparent


def cami(parent, id_):
    out = []
    vist = set()
    while id_ and id_ not in vist:
        vist.add(id_)
        out.append(id_)
        id_ = parent.get(id_)
    return list(reversed(out))


def pla(g, ref):
    ids = resol(g, ref)
    if not ids:
        return None
    ordre, parent, revisio, rparent = tanca(g, ids)
    consequencies = [g.nodes[i] for i in ordre if i not in ids] + [g.nodes[i] for i in revisio]
    parent_tot = dict(parent)
    parent_tot.update(rparent)
    return {
        "consulta": ref,
        "origen": [g.nodes[i] for i in ids],
        "consequencies": consequencies,
        "parent": parent_tot,
        "passos": passos_de(consequencies),
    }


def passos_de(nodes):
    if any(n.get("comanda") == PAS_WEB for n in nodes):
        return [comanda_build_dades()]
    return []


def _limita(seq, complet, n=12):
    if complet or len(seq) <= n:
        return seq, []
    return seq[:n], seq[n:]


def cadenes(p):
    gnodes = {n["id"]: n for n in p["origen"] + p["consequencies"]}
    origen = p["origen"][0]
    linies = []
    if origen["tipus"] == "sessio":
        docs = origen.get("refs") or []
        grup = f" ({origen['grup']})" if origen.get("grup") else ""
        linies.append(
            f"Si toco {origen['id']}{grup} → web (SDAS, amb el grup GS/MG) → {format_cmd(comanda_build_dades())}"
        )
        if docs:
            linies.append(
                "Els PDF d'aquests documents no es regeneren: el text del full no surt del YAML de la sessió: "
                + ", ".join(docs)
            )
        manuals = [n for n in p["consequencies"] if n["estat"] == "manual"]
        if manuals:
            linies.append("Còpies i annexos → PENDENT MANUAL (" + ", ".join(n["curt"] for n in manuals[:6]) + ")")
        return linies
    manuals = [n for n in p["consequencies"] if n["estat"] == "manual" and n["tipus"] == "artefacte" and str(n.get("clase", "")).startswith("pdf")]
    escollit = None
    for n in manuals:
        cam = cami(p["parent"], n["id"])
        if any(x.split(":", 1)[0] in ("item", "document", "evidencia") for x in cam):
            if escollit is None or len(cam) > len(escollit[0]):
                escollit = (cam, n)
    if escollit is None and manuals:
        n = manuals[0]
        escollit = (cami(p["parent"], n["id"]), n)
    if escollit:
        cam, n = escollit
        noms = []
        for i in cam:
            node = gnodes.get(i) or {"curt": i}
            noms.append(node.get("curt") or i)
        linies.append("Si toco " + " → ".join(noms) + " → PENDENT MANUAL")
    if p["passos"]:
        linies.append("Pas segur: " + format_cmd(p["passos"][0]))
    elif not linies:
        linies.append(f"Si toco {origen['curt']}: cap pas automàtic.")
    return linies


def _render(g, p, complet=False):
    o = p["origen"]
    L = []
    if len(o) == 1:
        n = o[0]
        L.append(f"{n['etiqueta']}  [{n['id']}]")
        if n.get("font"):
            L.append(f"Font: {n['font']}")
        if n.get("grup"):
            L.append(f"Grup: {n['grup']} ({'mig grup' if n['grup'] == 'MG' else 'grup sencer'})")
        if n.get("motiu") and n["tipus"] in ("imatge", "font", "orfe", "sortida", "artefacte"):
            L.append(n["motiu"])
        if n["tipus"] == "artefacte" and n.get("document"):
            L.append(f"Document: {n['document']}")
        conte = g.conte.get(n["id"]) or []
        if conte:
            et = [g.nodes[i]["curt"] for i in conte if i in g.nodes]
            mostra, resta = _limita(et, complet, 16)
            L.append("Conté: " + ", ".join(mostra) + (f" … i {len(resta)} més" if resta else ""))
        usa = [g.nodes[i]["curt"] for i in g.usa.get(n["id"], []) if i in g.nodes and i not in {x["id"] for x in p["consequencies"]}]
        if n["tipus"] == "document":
            # Les evidències i les sessions que el citen no són conseqüències.
            usa = [g.nodes[i]["curt"] for i in g.usa.get(n["id"], []) if i in g.nodes]
        if usa:
            mostra, resta = _limita(usa, complet, 12)
            L.append("El fan servir: " + ", ".join(mostra) + (f" … i {len(resta)} més" if resta else ""))
        if n["tipus"] == "sessio" and n.get("refs"):
            L.append("Documents de la sessió (el PDF no es regenera): " + ", ".join(n["refs"]))
    else:
        L.append("Coincideix amb:")
        for n in o:
            L.append(f"  {n['id']}  {n['etiqueta']}")
    L.append("")
    for ln in cadenes(p):
        L.append(ln)
    L.append("")
    aplica = [n for n in p["consequencies"] if n["estat"] == "aplica"]
    manual = [n for n in p["consequencies"] if n["estat"] == "manual"]
    info = [n for n in p["consequencies"] if n["estat"] == "info" and n["tipus"] not in ("pregunta", "camp")]
    pregs = [n for n in p["consequencies"] if n["tipus"] in ("pregunta", "camp")]
    if aplica:
        L.append(f"Pas segur · {format_cmd(p['passos'][0])}")
        for n in aplica:
            L.append(f"  {n['etiqueta']}  →  {n['font']}")
        L.append("")
    if info:
        L.append(f"Cadena ({len(info)})")
        mostra, resta = _limita(info, complet, 18)
        for n in mostra:
            L.append(f"  {n['id']}  {n['etiqueta']}")
        if resta:
            L.append(f"  … i {len(resta)} més (--complet)")
        L.append("")
    if pregs:
        L.append(f"Preguntes i camps afectats: {len(pregs)}" + ("" if complet else " (--complet per llistar-los)"))
        if complet:
            for n in pregs:
                L.append(f"  {n['id']}")
        L.append("")
    if manual:
        L.append(f"PENDENT MANUAL ({len(manual)})")
        grups = {}
        ordre = []
        for n in manual:
            grups.setdefault(n["motiu"], [])
            if n["motiu"] not in ordre:
                ordre.append(n["motiu"])
            grups[n["motiu"]].append(n)
        for motiu in ordre:
            L.append(f"  {motiu}")
            nodes = grups[motiu]
            mostra, resta = _limita(nodes, complet, 24)
            for n in mostra:
                nota = f"  ({n['nota']})" if n.get("nota") else ""
                L.append(f"    {n['font'] or n['id']}{nota}")
            if resta:
                L.append(f"    … i {len(resta)} més (--complet)")
        L.append("")
    if not (aplica or manual or info or pregs):
        L.append("Cap conseqüència derivada.")
        L.append("")
    L.append("No es fa artefactes.py --registra: un PDF no regenerat ha de continuar sortint com a deriva.")
    return "\n".join(L)


def executa(passos):
    for cmd in passos:
        print("\nExecuto: " + format_cmd(cmd))
        r = subprocess.run(cmd, cwd=ROOT)
        if r.returncode != 0:
            print(f"El pas segur ha fallat (codi {r.returncode}). No s'ha fet --registra.")
            return r.returncode
    return 0


def comprova(g):
    err = []

    def need(cond, msg):
        if not cond:
            err.append(msg)

    def ids(p):
        return {n["id"] for n in p["consequencies"]}

    p = pla(g, "2.3")
    need(p is not None, "no resol 2.3")
    c = ids(p)
    need("item:s5.difu.x2" in c, "2.3 ha d'afectar l'ítem s5.difu.x2")
    need("evidencia:s5.difu" in c, "2.3 ha d'afectar l'evidència s5.difu")
    need("document:d5f5" in c, "2.3 ha d'arribar al document d5f5")
    need(any(i.endswith("sda5-07-fitxa-5-difusio-i-gradient.pdf") for i in c), "falta el PDF de la fitxa 5")
    need(any(i.endswith("sda5-14-rubriques.pdf") for i in c), "la rúbrica de la SdA 5 ha de sortir (no és un instrument, però imprimeix els criteris)")
    need(all(n["estat"] == "manual" for n in p["consequencies"] if n["tipus"] == "artefacte"), "cap artefacte no és executable")
    cmd = p["passos"][0] if p["passos"] else []
    need(cmd[-2:] == ["--aplica-html", "--estricte"] and str(cmd[1] if len(cmd) > 1 else "").endswith("build_dades.py"), "el pas segur és build_dades")
    need(all("registra" not in " ".join(cmd) for cmd in p["passos"]), "actua no registra")
    need(all(os.path.basename(x) not in ART.PRIVAT for cmd in p["passos"] for x in cmd), "no s'executa cap generador privat")
    cam = None
    for n in p["consequencies"]:
        if n["id"].endswith("sda5-07-fitxa-5-difusio-i-gradient.pdf"):
            cam = cami(p["parent"], n["id"])
    need(cam and "item:s5.difu.x2" in cam and "document:d5f5" in cam, "la cadena fins al PDF passa per l'ítem i el document")

    s = pla(g, "sessio:5:7")
    need(s["origen"][0].get("grup") == "GS", "la sessió 7 de la SdA 5 és GS")
    need("sortida:web" in ids(s), "la sessió actualitza el web")
    need(not any(i.endswith("sda5-07-fitxa-5-difusio-i-gradient.pdf") for i in ids(s)), "la sessió no regenera el PDF de la fitxa")
    need("d5f5" in (s["origen"][0].get("refs") or []), "la sessió 7 referencia d5f5")
    need(any(n["id"].endswith("full.md") for n in s["consequencies"]), "cal revisar full.md")
    need(any(n["id"].endswith("annex_groups.json") for n in s["consequencies"]), "cal revisar annex_groups.json")
    need(any(i.endswith("programacio-annexos.pdf") for i in ids(s)), "els annexos queden pendents")

    s12 = pla(g, "sda5 sessio 12")
    need(s12 and s12["origen"][0].get("grup") == "MG", "la sessió 12 de la SdA 5 és MG")

    f = pla(g, "full.md")
    need("sortida:web" not in ids(f), "full.md no mou el web")
    need(any(i.endswith("programacio-annexos.pdf") for i in ids(f)), "full.md afecta els annexos")

    img = pla(g, "img/sda1-s1.png")
    need(any("sda1-01-full-de-ruta.pdf" in i for i in ids(img)), "la imatge afecta el full de ruta")
    need("sortida:web" not in ids(img), "una imatge no regenera l'HTML")
    need(img["passos"] == [], "una imatge no dispara build_dades")

    ce = pla(g, "CE2")
    need("criteri:2.3" not in ids(ce), "canviar el text de la CE no recalcula cada criteri")
    need("criteri:2.3" in (g.conte.get("ce:CE2") or []), "CE2 conté el criteri 2.3")
    need(any(i.endswith("curs-07-recuperacio-ce2.pdf") or "dcR2" in i for i in ids(ce)), "CE2 afecta la recuperació")

    amb = resol(g, "programacio-annexos.pdf")
    need(len(amb) >= 2, "el mateix annex viu a docs/ i al bucket")

    # Cap pas segur pot anomenar un generador privat, ni comprova ni actua.
    for node in g.nodes.values():
        if node.get("comanda") == PAS_WEB and node["estat"] != "aplica":
            err.append(f"{node['id']} té comanda però no és aplica")
        if node["estat"] == "aplica" and node.get("comanda") != PAS_WEB:
            err.append(f"{node['id']} aplica sense la comanda permesa")
    if err:
        for e in err:
            print("FALLA:", e)
        return 1
    print(f"Comprovació del graf: ok ({len(g.nodes)} nodes, {sum(len(v) for v in g.afecta.values())} arestes)")
    return 0


US = """\
Ús:
  python3 tools/3r/impacte.py consulta REF [--json] [--complet]
  python3 tools/3r/impacte.py actua REF [--json] [--complet]
  python3 tools/3r/impacte.py comprova
  python3 tools/3r/artefactes.py --impacte REF
  python3 tools/3r/artefactes.py --actua REF

REF: 2.3, CE2, sda5, sessio:5:7, «sda5 sessio 7», d5f5, s5.difu, un camí YAML,
full.md, mapa_ce, docs/….pdf, professorat/….pdf o img/….png.

actua només executa build_dades.py --aplica-html --estricte, i només si el canvi
arriba al web, al mapa o als uid. Els PDF queden PENDENT MANUAL. No fa --registra.
"""


def parse(argv):
    a = list(argv)
    flags = {"json": "--json" in a, "complet": "--complet" in a}
    bucket = None
    if "--bucket" in a:
        i = a.index("--bucket")
        if i + 1 >= len(a):
            return None, flags, "Falta el fitxer després de --bucket"
        bucket = a[i + 1]
        del a[i:i + 2]
    a = [x for x in a if x not in ("--json", "--complet")]
    if not a or a[0] in ("-h", "--help", "ajuda"):
        return None, flags, US
    if a[0] in ("consulta", "actua", "comprova"):
        cmd, ref = a[0], " ".join(a[1:]).strip()
    else:
        cmd, ref = "consulta", " ".join(a).strip()
    flags["bucket"] = bucket
    flags["cmd"] = cmd
    flags["ref"] = ref
    if cmd != "comprova" and not ref:
        return None, flags, US + "\nFalta REF.\n"
    return True, flags, None


def main(argv=None):
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except (AttributeError, OSError):
        pass
    ok, flags, err = parse(list(sys.argv[1:] if argv is None else argv))
    if not ok:
        if err == US:
            sys.stdout.write(US)
            return 0
        sys.stderr.write(err if err.endswith("\n") else err + "\n")
        return 2
    g = graf(flags.get("bucket"))
    if flags["cmd"] == "comprova":
        return comprova(g)
    p = pla(g, flags["ref"])
    if p is None:
        sys.stderr.write(f"No trobo «{flags['ref']}».\nExemples: 2.3, CE5, sda5, sessio:5:7, d5f5, contingut/3r/sda/sda5.yaml, full.md, img/sda1-s1.png\n")
        return 2
    if flags["json"]:
        out = {
            "consulta": flags["ref"],
            "origen": p["origen"],
            "resum": cadenes(p),
            "passos_segurs": [format_cmd(c) for c in p["passos"]],
            "pendent_manual": [n["id"] for n in p["consequencies"] if n["estat"] == "manual"],
            "aplica": [n["id"] for n in p["consequencies"] if n["estat"] == "aplica"],
            "cadena": [n["id"] for n in p["consequencies"] if n["estat"] == "info"],
            "nota": "No es fa artefactes.py --registra.",
        }
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        print(_render(g, p, flags["complet"]))
    if flags["cmd"] == "actua":
        code = executa(p["passos"])
        manuals = [n for n in p["consequencies"] if n["estat"] == "manual"]
        if code == 0 and not p["passos"]:
            print("\nCap pas segur per executar.")
        if manuals:
            print(f"\nPENDENT MANUAL: {len(manuals)} peces. No s'han executat ni s'ha fet --registra.")
        return code
    return 0


def des_de_artefactes(a):
    """Entrada de artefactes.py --impacte / --actua / --comprova. Ignora --registra."""
    cmd = "actua" if "--actua" in a else ("comprova" if "--comprova" in a else "consulta")
    rest = [x for x in a if x not in ("--impacte", "--actua", "--comprova", "--registra", "--registra-imatges", "--check")]
    return main([cmd] + rest)


if __name__ == "__main__":
    sys.exit(main())
