"""Hiperenllaços de la programació cap al llibre web i el llibre digital."""
import json, re, copy
from prog_edit import *

B = "https://llibrefiq3r.cat/"
LJ = json.load(open("links.json"))
D, LL, SD = LJ["D"], LJ["L"], LJ["SDAS"]
DIG = set(json.load(open("fitxes_keys.json")))


def sess_of(n, k):
    for i, x in enumerate(SD[n - 1]["sessions"]):
        if k in x["d"] + x["dt"]:
            return i + 1
    return None


def url_doc(k, n=None):
    if D[k].get("t"):   # material del professorat: no és públic, enllaça la sessió
        s = sess_of(n, k) if n else None
        return B + (f"#sda{n}-s{s}" if s else f"#sda{n}" if n else "")
    return B + "#doc-" + k


def url_l(k):
    return LL[k]["u"] if LL[k]["u"].startswith("http") else B + LL[k]["u"]


def split_run(doc, r, segs):
    """Substitueix el run r per diversos runs; segs = [(text, url|None)]."""
    prev = r
    for txt, url in segs:
        nr = copy.deepcopy(r)
        for x in list(nr):
            if x.tag != W + 'rPr':
                nr.remove(x)
        t = nr.makeelement(W + 't', {}); t.text = txt
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); nr.append(t)
        prev.addnext(nr)
        node = wrap_run_link(doc, nr, url) if url else nr
        prev = node
    r.getparent().remove(r)


def link_regex(doc, p, rx, urlf):
    n = 0
    for _ in range(20):
        done = False
        for r in list(p.iter(W + 'r')):
            if r.getparent().tag == W + 'hyperlink':
                continue
            t = r.find(W + 't')
            if t is None or not t.text:
                continue
            m = re.search(rx, t.text)
            if not m:
                continue
            u = urlf(m)
            if not u:
                continue
            s = t.text
            segs = [(s[:m.start()], None), (m.group(0), u), (s[m.end():], None)]
            split_run(doc, r, [x for x in segs if x[0]])
            n += 1; done = True
            break
        if not done:
            break
    return n


# fulls de cada SdA: text de la llista «Fulls: …» amb [text|clau]
FULLS = {
 1: "[full de ruta|d1ruta], [registre del detectiu|d1reg], [seguretat|d1seg], [fitxa 1|d1f1], [fitxa 2|d1f2], fulls de laboratori ([densitat|d1dens], [proves|d1prov], [separació|d1sep], [cromatografia|d1crom]), [lectura en anglès|d1ellen], [guió de l'informe|d1inf], [rúbriques|d1rub], [activitat de demostració|d1prova], [diana|d1diana] i [mapa conceptual|d1mapa].",
 2: "[full de ruta|ruta], [full del repte|repte], laboratoris ([globus|lab] i [corba d'escalfament|labc]), [fitxa 1|f1], [fitxa 2|f2], [guió de l'informe|inf] i [del vídeo|video], [rúbriques|rub], [coavaluació dels vídeos|d2coav], [activitat de demostració|prova], [diana|diana] i [mapa conceptual|mapa].",
 3: "[full de ruta|d3ruta], fitxes [1|d3f1], [2|d3f2], [3|d3f3], [4|d3f4] i [5|d3f5], [laboratori|d3lab], [dossier|d3dos], [pla de campanya|d3camp], [rúbriques|d3rub], [activitat de demostració|d3prova], [diana|d3diana] i [mapa conceptual|d3mapa].",
 4: "[full de ruta|d4ruta], [full del repte|d4repte], laboratoris ([massa|d4lab1], [hidrogen|d4lab2], [electròlisi|d4lab3]), fitxes [1|d4f1], [2|d4f2] i [3|d4f3], [dossier|d4dos], [rúbriques|d4rub], [activitat de demostració|d4prova], [diana|d4diana] i [mapa conceptual|d4mapa].",
 5: "[full de ruta|d5ruta], [full del repte|d5repte], fitxes [1|d5f1], [2|d5f2], [3|d5f3], [4|d5f4], [5|d5f5], [6|d5f6q] i [7|d5f6], [problemes|d5prob], [laboratori de Hooke|d5hooke], [full de forces cel·lulars|d5tfm], [làmines A i B|d5lam], [rúbriques|d5rub], [activitat de demostració|d5prova], [diana|d5diana] i [mapa conceptual|d5mapa].",
 6: "[full de ruta|d6ruta], [full del repte|d6repte], [fitxa 1|d6f1], [fitxa 2|d6f2], [laboratori de consum|d6lab], [pla d'estalvi i debat|d6pla], [rúbriques|d6rub], [activitat de demostració|d6prova], [diana|d6diana] i [mapa conceptual|d6mapa].",
}
# recursos externs dins del paràgraf «Recursos:» (text que ja hi és → clau de L)
EXT = {
 1: [],
 2: [("«Propietats dels gasos»", "gasprop"), ("«Estats de la matèria»", "states")],
 3: [("«Dispersió de Rutherford»", "rutherford"), ("«Construeix un àtom»", "buildatom"), ("«La bateria de liti per dins»", "simbat")],
 4: [("simulació PhET", "ajust"), ("TMB", "tmbh2")],
 5: [("Vídeo de Rogers", "rogers"), ("cicatrització", "ferida"), ("metàstasi", "metastasi"), ("«Difusió»", "difusio")],
 6: [("plantilla d'inventari", "inv"), ("dades de Red Eléctrica", "reecat"), ("«Kit de construcció de circuits»", "circuits")],
}
PRE = {  # textos afegits a la part de material per citar també els simuladors que hi falten
 1: (r"claus de ferro, tres retoladors negres i paper de filtre\.", "claus de ferro, tres retoladors negres i paper de filtre; simulacions PhET «Densitat» i «Sucre i sal».",
     [("«Densitat»", "density"), ("«Sucre i sal»", "sugarsalt")]),
 2: (r"simulacions PhET «Propietats", "simulador propi de gasos i simulacions PhET «Propietats", [("simulador propi de gasos", "simgas")]),
 3: (r"«La bateria de liti per dins»,", "«La bateria de liti per dins», [taula periòdica interactiva],", []),
}


def parse_items(s, n):
    segs = []
    for part in re.split(r"(\[[^\]]+\])", s):
        if part.startswith("["):
            txt, k = part[1:-1].split("|")
            segs.append((txt, url_doc(k, n)))
        elif part:
            segs.append((part, None))
    return segs


def apply(doc):
    body = doc.element.body
    cnt = {"sessions": 0, "fulls": 0, "ext": 0, "altres": 0}
    # 1) capçaleres de sessió de les taules (cap. 4 i 6)
    sda = 0
    for tbl in body.iter(W + 'tbl'):
        for tr in tbl.findall(W + 'tr'):
            tcs = tr.findall(W + 'tc')
            if len(tcs) != 1:
                continue
            p = tcs[0].find(W + 'p')
            if p is None:
                continue
            t = ptext(p)
            m = re.match(r"Sessió (\d+) · [^\t]+\t", t)
            if not m:
                continue
            k = int(m.group(1))
            if k == 0:
                url = B + "#doc-dc0"
            else:
                if k == 1:
                    sda += 1
                url = B + f"#sda{sda}-s{k}"
            r = p.find(W + 'r')
            if r is not None and "\t" not in (ptext(r)):
                wrap_run_link(doc, r, url); cnt["sessions"] += 1
                c = r.find(W + 'rPr/' + W + 'color')
                if c is not None:
                    c.set(W + 'val', 'FFFFFF')   # capçalera fosca: enllaç en blanc i subratllat
    # 2) paràgrafs «Recursos:» del capítol 6
    n = 0
    for p in list(body.iter(W + 'p')):
        t = ptext(p)
        if not t.startswith("Recursos:"):
            continue
        n += 1
        if n in PRE:
            rx, new, ls = PRE[n]
            if n == 3:
                sub_in_par(p, rx, "«La bateria de liti per dins», taula periòdica interactiva,")
                ls = [("taula periòdica interactiva", "ptable")]
            else:
                sub_in_par(p, rx, new)
            for ph, k in ls:
                cnt["ext"] += link_phrase(doc, p, ph, url_l(k))
        # llista de fulls
        sub_in_par(p, r"Fulls: .*$", "Fulls: " + "@@FULLS@@")
        for r in p.iter(W + 'r'):
            tt = r.find(W + 't')
            if tt is not None and tt.text and "@@FULLS@@" in tt.text:
                a, b = tt.text.split("@@FULLS@@")
                segs = ([(a, None)] if a else []) + parse_items(FULLS[n], n) + ([(b, None)] if b.strip() else [])
                split_run(doc, r, segs); cnt["fulls"] += 1
                break
        for ph, k in EXT[n]:
            cnt["ext"] += link_phrase(doc, p, ph, url_l(k))
    # 3) taula de segona oportunitat i altres referències «SdA N, sessió K»
    for p in body.iter(W + 'p'):
        cnt["altres"] += link_regex(doc, p, r"SdA ([1-6]), sessió (\d+)", lambda m: B + f"#sda{m.group(1)}-s{m.group(2)}")
    # 4) tasques de recuperació per CE
    p = find_par(doc, "Tasques de recuperació per CE.")
    for i in range(1, 7):
        cnt["altres"] += link_phrase(doc, p, f"CE{i}:", B + f"#doc-dcR{i}")
    # 5) sessió 0 i tancament
    p = find_par(doc, "La primera i l'última sessió del curs")
    cnt["altres"] += link_phrase(doc, p, "la sessió 0", B + "#doc-dc0")
    cnt["altres"] += link_phrase(doc, p, "la de tancament", B + "#doc-dcT")
    # 6) annexos en document a part
    p = find_par(doc, "Els annexos (10 fulls")
    cnt["altres"] += link_phrase(doc, p, "document a part", B + "docs/programacio-annexos.pdf")
    # 7) exemples de la tipologia d'activitats i fets discrepants: (SdA N) → pàgina de la SdA
    for start in ("Fets discrepants.",):
        p = find_par(doc, start)
        for _ in range(8):
            if not link_regex(doc, p, r"SdA ([1-6])\)", lambda m: B + f"#sda{m.group(1)}"):
                break
            cnt["altres"] += 1
    return cnt


# ---------------------------------------------------------------- enllaços dins de les taules (fitxes, fulls, dossiers…)
def sda_docs(n):
    ks = []
    for x in SD[n - 1]["sessions"]:
        for k in x["d"] + x["dt"]:
            if k not in ks:
                ks.append(k)
    return ks


def find_key(n, pred):
    for k in sda_docs(n):
        if pred(k, D[k]["l"]):
            return k
    return None


def sess_doc(n, s, pred):
    if not s:
        return None
    x = SD[n - 1]["sessions"][s - 1]
    for k in x["d"] + x["dt"]:
        if pred(k, D[k]["l"]):
            return k
    return None


def demo_session(n):
    for i, x in enumerate(SD[n - 1]["sessions"], 1):
        if any("prova" in k for k in x["dt"]):
            return i
    return None


ADAPT = {("1", "Dislèxia"): "d1adap", ("2", "Alumnat nouvingut"): "d2adap", ("2", "Retard en l'aprenentatge"): "d2bas",
         ("3", "Altes capacitats"): "d3amp", ("4", "Dificultats en el càlcul (discalcúlia)"): "d4adap", ("5", "TDAH"): "d5adap",
         ("6", "Trastorn de l'espectre autista"): "d6adap"}
LECT = {"1": ("«The woman who tested the water»", B + "#doc-d1ellen"), "2": ("Notícia d'un aerosol", B + "#doc-repte"),
        "3": ("Notícies d'incendis", B + "#doc-d3dos"), "4": ("Notícia sobre els autobusos d'hidrogen de TMB", None),
        "5": ("Text divulgatiu sobre la febre", B + "#doc-d5f6q"), "6": ("Mária Telkes i la casa solar de Dover", None)}


def link_tables(doc):
    body = doc.element.body
    n = 0; cnt = 0; miss = []
    for el in body.iterchildren():
        if el.tag == W + 'p':
            t = ptext(el)
            m = re.match(r"6\.([1-6])(\.| )", t)
            st = el.find(W + 'pPr/' + W + 'pStyle')
            if m and st is not None and st.get(W + 'val', '').startswith('Heading'):
                n = int(m.group(1))
            mb = re.match(r"SITUACIÓ D'APRENENTATGE (\d)", t)
            if mb:
                n = int(mb.group(1))
            if t.startswith("7."):
                n = 0
            continue
        if el.tag != W + 'tbl':
            continue
        mb = re.match(r"SITUACIÓ D'APRENENTATGE (\d)", ptext(el))
        if mb:
            n = int(mb.group(1)); continue
        rows = el.findall(W + 'tr')
        hdr = [ptext(c) for c in rows[0].findall(W + 'tc')] if rows else []
        # Taula 29 (lectures) i taula 65 (materials adaptats)
        if hdr[:3] == ["SdA", "Lectura", "On es fa"]:
            for tr in rows[1:]:
                tcs = tr.findall(W + 'tc'); k = ptext(tcs[0]).strip()
                ph, u = LECT.get(k, (None, None))
                if k == "4": u = url_l("tmbh2")
                if k == "6": u = url_l("telkes")
                if ph and u:
                    for p in tcs[1].findall(W + 'p'):
                        cnt += link_phrase(doc, p, ph, u)
            continue
        if hdr[:3] == ["SdA", "Perfil", "Material adaptat d'exemple"]:
            for tr in rows[1:]:
                tcs = tr.findall(W + 'tc')
                k = ADAPT.get((ptext(tcs[0]).strip(), ptext(tcs[1]).strip()))
                if k:
                    ph = ptext(tcs[2]).strip()
                    for p in tcs[2].findall(W + 'p'):
                        cnt += link_phrase(doc, p, ph, B + "digital/profe.html#doc-" + k)
            continue
        if not n:
            continue
        sess = None
        for tr in rows:
            tcs = tr.findall(W + 'tc')
            if len(tcs) == 1:
                m = re.match(r"Sessió (\d+) · ", ptext(tcs[0]))
                if m:
                    sess = int(m.group(1))
                continue
            if hdr and hdr[0] == "Codi" and len(hdr) == 6:
                cols = {5}
            elif hdr and hdr[0] == "Codi" and hdr[-1].startswith("Evidències"):
                cols = {len(hdr) - 1}
            elif hdr and hdr[0] == "Instrument":
                cols = {0}
            else:
                cols = set()
            for ci, tc in enumerate(tcs):
                if ci not in cols:
                    continue
                for p in tc.findall(W + 'p'):
                    t = ptext(p)
                    LAB = {1: "d1dens", 3: "d3lab", 5: "d5hooke", 6: "d6lab"}
                    rules = [
                        (r"\b[Ff]itxa (\d)\b", lambda m: find_key(n, lambda k, l: l.startswith(f"Fitxa {m.group(1)}"))),
                        (r"\bFull de laboratori de Lavoisier\b", lambda m: "d4lab1" if n == 4 else None),
                        (r"\bFull de laboratori de l'electròlisi\b", lambda m: "d4lab3" if n == 4 else None),
                        (r"\b[Ff]ulls? de laboratori\b|\b[Ll]aboratori\b", lambda m: (sess_doc(n, sess, lambda k, l: "aboratori" in l) if sess else LAB.get(n))),
                        (r"\b[Ff]ull del repte\b", lambda m: find_key(n, lambda k, l: l == "Full del repte")),
                        (r"\b[Dd]ossier\b", lambda m: find_key(n, lambda k, l: l.startswith("Dossier"))),
                        (r"\b[Dd]iana\b", lambda m: find_key(n, lambda k, l: l.startswith("Diana"))),
                        (r"\b[Mm]apa conceptual\b", lambda m: find_key(n, lambda k, l: l.startswith("Mapa conceptual"))),
                        (r"\bFull de seguretat\b", lambda m: "d1seg" if n == 1 else None),
                        (r"\b[Rr]egistre\b", lambda m: "d1reg" if n == 1 else None),
                        (r"\bFull de proves\b", lambda m: "d1prov" if n == 1 else None),
                        (r"\bFull de cromatografia\b", lambda m: "d1crom" if n == 1 else None),
                        (r"\bInforme del grup i protocol\b|\bInforme i protocol\b|\binforme\b", lambda m: "d1inf" if n == 1 else None),
                        (r"\bLectura\b", lambda m: "d1ellen" if n == 1 else None),
                        (r"\bPla de campanya\b|\bCampanya i punt de recollida\b", lambda m: "d3camp" if n == 3 else None),
                        (r"\bFull de forces cel·lulars\b|\b[Ff]ull de forces\b", lambda m: "d5tfm" if n == 5 else None),
                        (r"\b[Pp]roblemes\b", lambda m: "d5prob" if n == 5 else None),
                        (r"\bGràfiques del patinet\b", lambda m: "d5f3" if n == 5 else None),
                        (r"\bLa febre i la migració\b", lambda m: "d5f6q" if n == 5 else None),
                        (r"\b[Pp]la d'estalvi\b", lambda m: "d6pla" if n == 6 else None),
                        (r"\bCerca d'informació\b", lambda m: "d6f2" if n == 6 else None),
                        (r"\bDebat\b", lambda m: "d6pla" if n == 6 else None),
                        (r"\bFull de càlcul\b", lambda m: "@inv" if n == 6 else None),
                        (r"\bVídeo per a 1r d'ESO\b|\bVídeo\b|\bGuió\b", lambda m: "video" if n == 2 else None),
                        (r"\bExplicació final\b", lambda m: "repte" if n == 2 else None),
                        (r"\bDossier i resposta del grup\b|\bResposta del grup\b", lambda m: "d4dos" if n == 4 else None),
                        (r"\b[Aa]ctivitat de demostració\b", lambda m: "@demo"),
                    ]
                    got = False
                    for rx, f in rules:
                        for _ in range(6):
                            # primera coincidència encara no enllaçada
                            free = "".join((r.find(W + 't').text or "") for r in p.iter(W + 'r') if r.getparent().tag != W + 'hyperlink' and r.find(W + 't') is not None)
                            mm = re.search(rx, free)
                            if not mm:
                                break
                            k = f(mm)
                            if not k:
                                break
                            u = B + f"#sda{n}-s{demo_session(n)}" if k == "@demo" else (url_l("inv") if k == "@inv" else url_doc(k, n))
                            if not link_phrase(doc, p, mm.group(0), u):
                                break
                            cnt += 1; got = True
                    if not got and re.search(r"\b(Fitxa|Full|Dossier|Diana|Laboratori)\b", t) and len(t) < 160:
                        miss.append((n, sess, t[:90]))
    return cnt, miss
