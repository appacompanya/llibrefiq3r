"""Descobreix les convocatòries a la carpeta de fonts i en treu els exercicis (retalls d'enunciat i de pauta)."""
import re
from pathlib import Path

import pymupdf
from segmenta import segment, lines, neteja
import tempfile
CACHE = Path(tempfile.gettempdir()) / "quim_net"
CACHE.mkdir(exist_ok=True)


def net(path):
    path = Path(path)
    out = CACHE / path.name
    if not out.exists() or out.stat().st_mtime < path.stat().st_mtime:
        neteja(str(path), str(out))
    return out

CONV = {"j": "Juny", "o": "Juny", "s": "Setembre", "e": "Setembre"}


def serie_of(doc, pages=range(0, 2)):
    for p in pages:
        if p < doc.page_count:
            m = re.search(r"S[èeÈE]RIE\s*(\d)|Sèrie\s*(\d)", doc[p].get_text(), re.I)
            if m:
                return int(m.group(1) or m.group(2))
    return 0


def pauta_start(doc):
    for i, p in enumerate(doc):
        if re.search(r"Criteri específic|Pautes de correcció|criteris de correcció", p.get_text(), re.I) and i > 0:
            return i
    return None


H_ENUN_25 = re.compile(r"^Exercici (\d)\s*$")
H_PAUTA_25 = re.compile(r"^(?:(?:Exercici|Pregunta|PREGUNTA|Problema|PROBLEMA|Qüestió|QÜESTIÓ)\s*|(?=[1-7]\.\s+[A-ZÀÈÉÍÒÓÚÇ]{3}))([1-7])(?:[a-d.)]|\s|$)")
H_ENUN_24 = re.compile(r"^([1-7])\.(\s+\S|\s*$)")


def _ex(enun_path, enun_pages, h_enun, pauta_path, pauta_pages, h_pauta, nom_fmt):
    enun_path = net(enun_path)
    de = pymupdf.open(enun_path)
    segs = segment(de, enun_pages, h_enun, lambda m: int(m.group(1)))
    sols = {}
    if pauta_path:
        pauta_path = net(pauta_path)
        dp = pymupdf.open(pauta_path)
        for k, t, clips, text in segment(dp, pauta_pages, h_pauta, lambda m: int(m.group(1))):
            sols[k] = ([(str(pauta_path), p, r) for p, r in clips], text)
    out = []
    for k, t, clips, text in segs:
        s = sols.get(k, ([], ""))
        out.append({"num": k, "nom": nom_fmt(k), "clips": [(str(enun_path), p, r) for p, r in clips], "text": text,
                    "sol": s[0], "sol_text": s[1]})
    return out


def cover_pages(doc):
    """Portades de cada sèrie dins d'un fitxer d'enunciats: {pàgina: sèrie}."""
    out = {}
    for i, p in enumerate(doc):
        t = p.get_text()
        top = [l[4] for l in lines(p) if l[0] < 260]
        ser = [re.match(r"^Sèrie\s*(\d)\s*$", x) for x in top]
        ser = [m for m in ser if m]
        if ser and any(re.match(r"^Proves d.accés a la universitat", x, re.I) for x in top):
            out[i] = int(ser[0].group(1))
    return out


def pauta_series(doc, first=0):
    """Inici de cada sèrie dins d'un fitxer de pautes: {pàgina: sèrie}."""
    out = {}
    for i in range(first, doc.page_count):
        for l in lines(doc[i])[:8]:
            m = re.match(r"^S[ÈèEe](?:RIE|IRE)\s*(\d)\s*$", l[4], re.I)
            if m:
                out[i] = int(m.group(1)); break
    return out


def ranges(starts, n):
    ks = sorted(starts)
    return {starts[k]: list(range(k, (ks[i + 1] if i + 1 < len(ks) else n))) for i, k in enumerate(ks)}


def _put(d, kind, f):
    """Si hi ha dues còpies del mateix document, es queda la que té més pàgines (la completa)."""
    if kind not in d or pymupdf.open(f).page_count > pymupdf.open(d[kind]).page_count:
        d[kind] = f


def convocatories(src: Path):
    files = {}
    for f in src.rglob("*.pdf"):
        files.setdefault(f.name.split("__")[-1].lower(), f)
    by = {}
    for name, f in files.items():
        m = re.search(r"pau_quim(\d\d)([jsoe])([lpt]?)(_tei)?\.pdf$", name, re.I)
        m2 = re.search(r"quimica-catalunya-(juny|setembre)-(20\d\d)-(enunciats|solucions)\.pdf$", name, re.I)
        m3 = re.search(r"pau_quimica_(20\d\d)_(juny|setembre)_(enunciat|solucio)\.pdf$", name, re.I)
        if m:
            yy, c, kind, tei = m.groups()
            _put(by.setdefault((int(yy), c.lower(), bool(tei)), {}), kind.lower() or "x", f)
        elif m2 or m3:
            if m2:
                cv, yr, k = m2.groups()
            else:
                yr, cv, k = m3.groups()
            key = (int(yr) - 2000, cv.lower()[0], False)
            kind = "l" if k.lower().startswith("enunciat") else "p"
            _put(by.setdefault(key, {}), kind, f)
    out = []
    for (yy, c, tei), d in sorted(by.items()):
        year = 2000 + yy
        if "x" in d:  # enunciat i pauta en un sol fitxer (2026)
            doc = pymupdf.open(d["x"]); ps = pauta_start(doc)
            lpath, ppath, lpages_all, ppages_first = d["x"], d["x"], ps, ps
        else:
            if "l" not in d:
                continue
            lpath = d["l"]; ppath = d.get("p") or d.get("t")
            lpages_all = pymupdf.open(lpath).page_count; ppages_first = 0
        dl = pymupdf.open(lpath)
        covers = {k: v for k, v in cover_pages(dl).items() if k < lpages_all}
        if not covers:
            covers = {0: serie_of(dl)}
        lr = ranges(covers, lpages_all)
        pr = {}
        if ppath:
            dp = pymupdf.open(ppath)
            ps_ = pauta_series(dp, ppages_first)
            if not ps_:
                ps_ = {ppages_first: next(iter(lr))}
            pr = ranges(ps_, dp.page_count)
        if yy >= 25:
            h_en, fmt = H_ENUN_25, (lambda k: f"Exercici {k}")
        else:
            h_en, fmt = H_ENUN_24, (lambda k: f"Qüestió {k}")
        for serie, pages in lr.items():
            pp = pr.get(serie) or (list(pr.values())[0] if len(pr) == 1 and len(lr) == 1 else [])
            out.append({"any": year, "conv": ("Juliol" if year == 2020 and c in "jo" else CONV[c]), "serie": serie,
                        "exercicis": (lambda lpath=lpath, pages=pages, ppath=ppath, pp=pp, h_en=h_en, fmt=fmt:
                                      _ex(lpath, pages, h_en, ppath if pp else None, pp, H_PAUTA_25, fmt))})
    return out
