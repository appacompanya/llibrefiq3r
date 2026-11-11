#!/usr/bin/env python3
"""Recull d'exercicis de la PAU de Química (Catalunya, 2011–2026): quadern d'enunciats i quadern de solucions.

Ús: python3 tools/quimica-pau/build.py <carpeta_fonts> <carpeta_sortida>
Les fonts són els PDF oficials (enunciats i pautes de correcció) que baixa l'acció «Química PAU · fonts».
"""
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pymupdf
from segmenta import segment, lines
from classifica import BLOCS, NOMS, classify
from munta import Book, _txt, MX, W, BLUE, MUTED, INK
from fonts import convocatories

SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)


def main():
    items = []
    for c in convocatories(SRC):
        exs = c["exercicis"]()
        for e in exs:
            e.update({k: c[k] for k in ("any", "conv", "serie")})
            items.append(e)
    # classificació
    for e in items:
        e["bloc"], e["extra"] = classify(e["text"] + "\n" + e.get("sol_text", "")[:1500])
    order = {k: i for i, (k, _) in enumerate(BLOCS)}
    conv_ord = {"Juny": 0, "Setembre": 1}
    items.sort(key=lambda e: (order[e["bloc"]], -e["any"], conv_ord.get(e["conv"], 2), e["serie"], e["num"]))
    for i, e in enumerate(items, 1):
        e["n"] = i

    def label(e):
        s = f"Ex. {e['n']}  ·  {e['any']} – {e['conv']} – Sèrie {e['serie']} – {e['nom']}"
        return s

    def tags(e):
        t = NOMS[e["bloc"]]
        if e["extra"]:
            t += "  ·  també: " + ", ".join(NOMS[x] for x in e["extra"])
        return t

    counts = {k: sum(1 for e in items if e["bloc"] == k) for k, _ in BLOCS}
    for kind in ("enunciats", "solucions"):
        title = "Química PAU Catalunya"
        sub = f"Quadern {'d’enunciats' if kind == 'enunciats' else 'de solucions'} 2011–2026"
        b = Book(f"{title} – {sub}", sub)
        # portada
        b.new_page()
        p = b.page
        _txt(p, 0, 300, title, 26, True, align=1, width=595)
        _txt(p, 0, 332, sub, 20, True, align=1, width=595)
        y = 400
        _txt(p, 70, y, f"{len(items)} exercicis de Química de les PAU de Catalunya, del 2011 al 2026.", 10.5); y += 15
        _txt(p, 70, y, "Ordenats per blocs. El número Ex. N és el mateix als dos quaderns (enunciats i solucions).", 10.5); y += 15
        if kind == "solucions":
            _txt(p, 70, y, "Solucions: criteris de correcció oficials de cada convocatòria.", 10.5); y += 15
        y += 12
        for i, (k, nom) in enumerate(BLOCS, 1):
            _txt(p, 70, y, f"{i}. {nom}  ({counts[k]})", 10.5); y += 15
        y += 14
        for s in ("Fonts: exàmens i criteris de correcció oficials de les PAU de Química (Generalitat de Catalunya).",
                  "Un exercici amb apartats de més d’un bloc va al bloc dominant; la línia gris diu quins altres toca.",
                  "Fins al 2019 l’alumne triava entre opcions; des del 2020 hi ha preguntes a escollir. Tot hi és."):
            _txt(p, 70, y, s, 8.5, color=MUTED); y += 12
        cur = None
        for e in items:
            if e["bloc"] != cur:
                cur = e["bloc"]
                b.bloc_band(f"Bloc {order[cur] + 1}. {NOMS[cur]}  ({counts[cur]} exercicis)")
            b.ex_header(label(e), tags(e))
            b.toc.append((e, b.doc.page_count))
            clips = e["clips"] if kind == "enunciats" else e.get("sol", [])
            if not clips:
                _txt(b.page, MX + 6, b.y + 10, "(No hi ha criteris de correcció publicats per a aquest exercici.)", 9, color=MUTED)
                b.y += 22
            for (path, pno, rect) in clips:
                b.clip(path, pno, rect)
            b.y += 10
        # índex
        b.bloc = "Índex"
        b.new_page()
        _txt(b.page, MX, b.y + 12, "Índex d’exercicis", 14, True); b.y += 26
        cur = None
        for e, pg in b.toc:
            if e["bloc"] != cur:
                cur = e["bloc"]
                b.space(30)
                _txt(b.page, MX, b.y + 12, f"Bloc {order[cur] + 1}. {NOMS[cur]}  ({counts[cur]} exercicis)", 9.5, True, BLUE); b.y += 18
            b.space(11)
            s = f"Ex. {e['n']}  ·  {e['any']} – {e['conv']} – Sèrie {e['serie']} – {e['nom']}"
            if e["extra"]:
                s += "  [+ " + ", ".join(NOMS[x] for x in e["extra"]) + "]"
            _txt(b.page, MX + 6, b.y + 8, s[:118], 7.5)
            _txt(b.page, MX + W - 20, b.y + 8, str(pg), 7.5)
            b.y += 10.5
        b.number_pages()
        name = "quadern_enunciats.pdf" if kind == "enunciats" else "quadern_solucions.pdf"
        b.save(OUT / name)
        print(name, b.doc.page_count, "pàgines")
    json.dump([{k: e[k] for k in ("n", "any", "conv", "serie", "nom", "bloc", "extra")} for e in items],
              open(OUT / "exercicis.json", "w"), ensure_ascii=False, indent=0)
    print(len(items), "exercicis;", counts)


if __name__ == "__main__":
    main()
