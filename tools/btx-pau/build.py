#!/usr/bin/env python3
"""Genera btx/pau/ a partir de la carpeta de PAU de Física (per defecte /workspace/pau_fisica).

Copia els PDF (originals a btx/pau/, versions per a mòbil a btx/pau/mobil/) i escriu:
  btx/pau/exercicis.json      índex d'exercicis amb camins relatius a btx/pau/
Ús: python3 tools/btx-pau/build.py [carpeta_font]
"""
import json, re, shutil, subprocess, sys
from pathlib import Path

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "/workspace/pau_fisica")
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "btx" / "pau"
CHAPTERS = [
    ("mhs", "Moviment harmònic simple"),
    ("ones", "Moviment ondulatori"),
    ("fenomens-ondulatoris", "Fenòmens ondulatoris"),
    ("camp-gravitatori", "Camp gravitatori"),
    ("camp-electric", "Camp elèctric"),
    ("camp-magnetic", "Camp electromagnètic"),
    ("induccio", "Inducció electromagnètica"),
    ("quantica", "Física quàntica"),
    ("particules", "Física relativista, nuclear i de partícules"),  # la PAU ajunta relativitat i partícules en un capítol
    ("optica", "Òptica"),
]
SLUGS = [s for s, _ in CHAPTERS]


def pages(p: Path) -> int:
    out = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))


def find(name: str) -> Path:
    for c in (SRC / name, SRC / "per_bloc" / name, SRC / "per_bloc" / "mobil" / Path(name).name, SRC / Path(name).name):
        if c.exists():
            return c
    raise FileNotFoundError(name)


def main():
    data = json.load(open(SRC / "per_bloc" / "index_exercicis.json", encoding="utf-8"))
    (OUT / "mobil").mkdir(parents=True, exist_ok=True)
    files = {}  # nom relatiu a btx/pau -> font

    def reg(rel_src: str, mobile: bool) -> str:
        name = Path(rel_src).name
        rel = ("mobil/" if mobile else "") + name
        files[rel] = find(rel_src)
        return rel

    for q in ("quadern_enunciats.pdf", "quadern_solucions.pdf"):
        reg(q, False)
        reg(q.replace(".pdf", "_mobil.pdf"), True)
    for s in SLUGS:
        for k in ("enunciats", "solucions"):
            reg(f"per_bloc/{k}_{s}.pdf", False)
            reg(f"per_bloc/mobil/{k}_{s}_mobil.pdf", True)

    for old in list(OUT.glob("*.pdf")) + list((OUT / "mobil").glob("*.pdf")):
        if old.relative_to(OUT).as_posix() not in files:
            print("Esborrat (ja no és a la font):", old.relative_to(OUT))
            old.unlink()
    npages = {}
    for rel, src in files.items():
        dst = OUT / rel
        if not dst.exists() or dst.stat().st_size != src.stat().st_size or dst.stat().st_mtime < src.stat().st_mtime:
            shutil.copy2(src, dst)
        npages[rel] = pages(dst)
    for rel in files:
        if rel.startswith("mobil/"):
            orig = rel[6:].replace("_mobil.pdf", ".pdf")
            if npages[rel] != npages[orig]:
                raise SystemExit(f"Pàgines diferents: {rel} {npages[rel]} vs {orig} {npages[orig]}")

    rows, issues = [], []
    for x in data:
        if x["capitol_slug"] not in SLUGS:
            issues.append(f"ex {x['ex']}: capítol desconegut {x['capitol_slug']}")
            continue
        e = Path(x["fitxer_enunciat"]).name
        so = Path(x["fitxer_solucio"]).name
        for f, p in ((e, x["pagina_enunciat"]), (so, x["pagina_solucio"]),
                     ("quadern_enunciats.pdf", x["pagina_quadern_enunciats"]),
                     ("quadern_solucions.pdf", x["pagina_quadern_solucions"])):
            if not (1 <= p <= npages[f]):
                issues.append(f"ex {x['ex']}: pàgina {p} fora de {f} ({npages[f]})")
        rows.append({
            "ex": x["ex"], "id": x["id_estable"], "any": x["any"], "conv": x["convocatoria"],
            "serie": x["serie"], "exercici": x["exercici"], "model": x["model_generalitat"],
            "cap": x["capitol_slug"], "cap2": x["capitol_secundari"], "sub": x["subtipus"],
            "e": e, "pe": x["pagina_enunciat"], "s": so, "ps": x["pagina_solucio"],
            "qe": x["pagina_quadern_enunciats"], "qs": x["pagina_quadern_solucions"],
            "ue": x["url_enunciat_oficial"], "us": x["url_solucio_oficial"],
        })
    chapters = []
    for i, (s, t) in enumerate(CHAPTERS, 1):
        mine = [r for r in rows if r["cap"] == s]
        chapters.append({
            "n": i, "slug": s, "titol": t, "exercicis": len(mine),
            "tambe": sum(1 for r in rows if r["cap2"] == s),
            "enunciats": f"enunciats_{s}.pdf", "solucions": f"solucions_{s}.pdf",
            "enunciats_mobil": f"mobil/enunciats_{s}_mobil.pdf", "solucions_mobil": f"mobil/solucions_{s}_mobil.pdf",
            "pagines_enunciats": npages[f"enunciats_{s}.pdf"], "pagines_solucions": npages[f"solucions_{s}.pdf"],
            "mb_enunciats": round((OUT / f"enunciats_{s}.pdf").stat().st_size / 1e6, 1),
            "mb_solucions": round((OUT / f"solucions_{s}.pdf").stat().st_size / 1e6, 1),
            "index": f"./?cap={s}#index",
        })
    meta = {
        "quadern_enunciats": "quadern_enunciats.pdf", "quadern_solucions": "quadern_solucions.pdf",
        "pagines_quadern_enunciats": npages["quadern_enunciats.pdf"], "pagines_quadern_solucions": npages["quadern_solucions.pdf"],
        "total": len(rows), "anys": [min(r["any"] for r in rows), max(r["any"] for r in rows)],
    }
    json.dump({"meta": meta, "capitols": chapters, "exercicis": rows}, open(OUT / "exercicis.json", "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"))
    tot = sum((OUT / r).stat().st_size for r in files)
    big = [(r, (OUT / r).stat().st_size) for r in files if (OUT / r).stat().st_size > 50e6]
    print(f"{len(rows)} exercicis, {len(files)} PDF, {tot/1e6:.1f} MB")
    if big: print("ATENCIÓ fitxers > 50 MB:", big)
    if tot > 300e6: print("ATENCIÓ: més de 300 MB")
    for i in issues: print("PROBLEMA:", i)


if __name__ == "__main__":
    main()
