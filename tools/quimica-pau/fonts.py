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
H_PAUTA_25 = re.compile(r"^(?:Exercici|Pregunta|Problema|Qüestió) (\d)(?:[a-d.]|\s|$)")
H_ENUN_24 = re.compile(r"^([1-7])\.\s+\S")


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


def convocatories(src: Path):
    files = {f.name: f for f in src.rglob("*.pdf")}
    out = []
    by = {}
    for name, f in files.items():
        m = re.search(r"pau_quim(\d\d)([jsoe])([lpt]?)(_tei)?\.pdf$", name, re.I)
        if m:
            yy, c, kind, tei = m.groups()
            by.setdefault((int(yy), c.lower(), bool(tei)), {})[kind.lower() or "x"] = f
    for (yy, c, tei), d in sorted(by.items()):
        year = 2000 + yy
        if yy >= 24:
            if "x" in d:  # enunciat i pauta en un sol fitxer (2026)
                doc = pymupdf.open(d["x"]); ps = pauta_start(doc)
                el, ep = (d["x"], list(range(1, ps))), (d["x"], list(range(ps, doc.page_count)))
            else:
                if "l" not in d:
                    continue
                pk = d.get("p") or d.get("t")
                doc = pymupdf.open(d["l"])
                el = (d["l"], list(range(1, doc.page_count)))
                ep = (pk, list(range(0, pymupdf.open(pk).page_count))) if pk else (None, [])
            serie = serie_of(pymupdf.open(el[0]))
            h_en = H_ENUN_24 if yy == 24 else H_ENUN_25
            fmt = (lambda k: f"Qüestió {k}") if yy == 24 else (lambda k: f"Exercici {k}")
            out.append({"any": year, "conv": CONV[c], "serie": serie,
                        "exercicis": (lambda el=el, ep=ep, h_en=h_en, fmt=fmt:
                                      _ex(el[0], el[1], h_en, ep[0], ep[1], H_PAUTA_25, fmt))})
    return out
