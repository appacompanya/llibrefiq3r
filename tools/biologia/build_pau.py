#!/usr/bin/env python3
"""Genera biologia/pau/: quaderns de la PAU sencers i per blocs (ordinador i mòbil) i exercicis.json.

Ús: python3 tools/biologia/build_pau.py quadern_enunciats.pdf quadern_solucions.pdf
"""
import json, re, shutil, sys
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "biologia" / "pau"
SRC_E, SRC_S = Path(sys.argv[1]), Path(sys.argv[2])

BLOCS = [  # (slug, títol tal com surt al quadern, tema del llibre)
    ("biomolecules-cellula", "Biomolècules i cèl·lula", ["biomolecules", "cellula"]),
    ("metabolisme", "Metabolisme", ["metabolisme"]),
    ("genetica", "Genètica i herència", ["genetica"]),
    ("genetica-molecular", "Genètica molecular i biotecnologia", ["genetica-molecular"]),
    ("evolucio-ecologia", "Evolució i ecologia", ["evolucio"]),
    ("microbiologia", "Microbiologia", ["microbiologia"]),
    ("immunologia", "Immunologia", ["immunologia"]),
]


def chapters(doc):
    toc = doc.get_toc()
    ch = [(t[1], t[2]) for t in toc if t[0] == 1 and re.match(r"\d\.", t[1])]
    ends = [t[2] for t in toc if t[0] == 1]
    res = []
    for i, (title, p) in enumerate(ch):
        nxt = [e for e in ends if e > p]
        res.append((title, p, (min(nxt) - 1) if nxt else len(doc)))
    exs = [(t[1], t[2]) for t in toc if t[0] == 2]
    return res, exs


def subdoc(doc, a, b, path, mobile=False):
    out = fitz.open()
    out.insert_pdf(doc, from_page=a - 1, to_page=b - 1)
    toc = [[lvl, t, p - a + 1] for lvl, t, p in doc.get_toc() if a <= p <= b and lvl == 2]
    if mobile:
        crop(out)
    if toc:
        out.set_toc([[1, t, p] for _, t, p in toc])
    out.save(path, garbage=4, deflate=True)
    return len(out)


def crop(doc):
    """Versió per a mòbil: retalla els marges en blanc de cada pàgina (la numeració no canvia)."""
    for p in doc:
        r = fitz.Rect()
        for b in p.get_text("blocks"):
            r |= fitz.Rect(b[:4])
        for d in p.get_drawings():
            if d["rect"].width < p.rect.width * 0.98:
                r |= d["rect"]
        for img in p.get_images(full=True):
            for ir in p.get_image_rects(img[0]):
                r |= ir
        if r.is_empty or r.width < 50:
            continue
        r = fitz.Rect(r.x0 - 8, r.y0 - 8, r.x1 + 8, r.y1 + 8) & p.rect
        p.set_cropbox(r)


def tags(doc, title, page):
    p = doc[page - 1]
    lines = ["".join(s["text"] for s in l["spans"]) for b in p.get_text("dict")["blocks"] for l in b.get("lines", [])]
    num = title.split(" · ")[0].strip()
    for i, s in enumerate(lines):
        if s.startswith(num + " ") and i + 1 < len(lines):
            t = lines[i + 1]
            if " · " in t:
                return [x.strip() for x in t.split(" · ", 1)[1].split(";") if x.strip()]
    return []


def annex_types(doc):
    """Subtipus de cada bloc segons l'annex del quadern d'enunciats."""
    toc = doc.get_toc()
    ann = [t[2] for t in toc if t[0] == 1 and t[1].startswith("Annex")]
    if not ann:
        return {}
    txt = "\n".join(doc[i].get_text() for i in range(ann[0] - 1, len(doc)))
    res, cur = {}, None
    for line in txt.splitlines():
        line = line.strip()
        m = re.match(r"^(.*?)\s+\(\d+ exercicis\)$", line)
        if m:
            cur = m.group(1); res[cur] = []; continue
        if cur and line and not re.match(r"^('\d\d|\d+|·|Subtipus|Total)$", line) and not line.startswith("Annex"):
            res[cur].append(line)
    return res


def main():
    (OUT / "mobil").mkdir(parents=True, exist_ok=True)
    de, ds = fitz.open(SRC_E), fitz.open(SRC_S)
    che, exe = chapters(de)
    chs, exs = chapters(ds)
    types = annex_types(de)
    type2bloc = {}
    for bt, lst in types.items():
        for x in lst:
            type2bloc.setdefault(x, bt)
    title2slug = {t: s for s, t, _ in BLOCS}
    fast = "--json" in sys.argv
    for name, src in (() if fast else (("quadern_enunciats", SRC_E), ("quadern_solucions", SRC_S))):
        shutil.copy2(src, OUT / f"{name}.pdf")
        d = fitz.open(src); crop(d); d.save(OUT / "mobil" / f"{name}_mobil.pdf", garbage=4, deflate=True)
    caps, rows = [], []
    sol_by_num = {t.split(" · ")[0].strip(): p for t, p in exs}
    for i, (slug, btitle, temes) in enumerate(BLOCS):
        (te, ae, be), (ts, as_, bs) = che[i], chs[i]
        assert btitle in te and btitle in ts, (te, ts)
        if fast:
            ne, ns = be - ae + 1, bs - as_ + 1
        else:
            ne = subdoc(de, ae, be, OUT / f"enunciats_{slug}.pdf")
            subdoc(de, ae, be, OUT / "mobil" / f"enunciats_{slug}_mobil.pdf", mobile=True)
            ns = subdoc(ds, as_, bs, OUT / f"solucions_{slug}.pdf")
            subdoc(ds, as_, bs, OUT / "mobil" / f"solucions_{slug}_mobil.pdf", mobile=True)
        n_ex = 0
        for t, p in exe:
            if not (ae <= p <= be):
                continue
            n_ex += 1
            num = t.split(" · ")[0].strip()
            m = re.search(r"·\s*(\d{4})\s*–\s*(\w+)\s*–\s*Sèrie\s*(\d+)\s*–\s*(.+)$", t)
            sub = tags(de, t, p)
            cap2 = None
            for x in sub:
                b = type2bloc.get(x)
                if b and b != btitle and b in title2slug:
                    cap2 = title2slug[b]; break
            ps = sol_by_num.get(num)
            rows.append({"ex": int(num.split()[1]), "id": num, "any": int(m.group(1)) if m else None, "conv": m.group(2) if m else "",
                         "serie": int(m.group(3)) if m else None, "exercici": m.group(4).strip() if m else t, "model": False,
                         "cap": slug, "cap2": cap2, "sub": sub, "e": f"enunciats_{slug}.pdf", "pe": p - ae + 1,
                         "s": f"solucions_{slug}.pdf", "ps": (ps - as_ + 1) if ps else 1, "qe": p, "qs": ps or 1, "ue": None, "us": None})
        mb = lambda f: round((OUT / f).stat().st_size / 1e6, 1)
        caps.append({"n": i + 1, "slug": slug, "titol": btitle, "temes": temes, "exercicis": n_ex,
                     "tambe": 0, "enunciats": f"enunciats_{slug}.pdf", "solucions": f"solucions_{slug}.pdf",
                     "enunciats_mobil": f"mobil/enunciats_{slug}_mobil.pdf", "solucions_mobil": f"mobil/solucions_{slug}_mobil.pdf",
                     "pagines_enunciats": ne, "pagines_solucions": ns, "mb_enunciats": mb(f"enunciats_{slug}.pdf"), "mb_solucions": mb(f"solucions_{slug}.pdf"),
                     "index": f"./?cap={slug}#index"})
    for c in caps:
        c["tambe"] = sum(1 for r in rows if r["cap2"] == c["slug"])
    anys = [r["any"] for r in rows if r["any"]]
    meta = {"quadern_enunciats": "quadern_enunciats.pdf", "quadern_solucions": "quadern_solucions.pdf",
            "pagines_quadern_enunciats": len(de), "pagines_quadern_solucions": len(ds), "total": len(rows), "anys": [min(anys), max(anys)]}
    json.dump({"meta": meta, "capitols": caps, "exercicis": rows}, open(OUT / "exercicis.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(len(rows), "exercicis;", [(c["slug"], c["exercicis"]) for c in caps])


if __name__ == "__main__":
    main()
