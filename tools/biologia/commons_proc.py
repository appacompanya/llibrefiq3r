#!/usr/bin/env python3
"""Prepara les il·lustracions de Wikimedia Commons per al llibre: tradueix les etiquetes al català,
ajusta el viewBox perquè no quedi res retallat i escriu biologia/img/<clau>.svg i biologia/img/commons.json
(autoria i llicència, que el llibre mostra al peu de cada figura).

Ús: python3 tools/biologia/commons_proc.py
"""
import json, re, html
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "tools/biologia/commons"
OUT = ROOT / "biologia/img"

# clau del llibre → (fitxer de Commons, traduccions {text original: text català})
SPEC = {
    "animal": ("Animal cell structure ca.svg", {"Aparell de golgi": "Aparell de Golgi", "Filaments d'actina": "Filaments d’actina", "Membrana": "Membrana"}),
    "membrana": ("Cell membrane detailed diagram ca.svg", {
        "Filaments de": "Filaments del", "citosequelet": "citoesquelet", "Caps hidrofílics": "Caps hidròfils", "Cues hidrofòbiques": "Cues hidròfobes",
        "(proteïna en alfa-hèlix)": "(hèlix α)", "(proteïna globular)": "(globular)"}),
    "dna_quimica": ("DNA chemical structure.svg", {
        "Phosphate-": "Esquelet de", "deoxyribose": "fosfat i", "backbone": "desoxiribosa", "Adenine": "Adenina", "Thymine": "Timina",
        "Guanine": "Guanina", "Cytosine": "Citosina", "3&#x2032; end": "extrem 3&#x2032;", "5&#x2032; end": "extrem 5&#x2032;"}),
}
CREDIT_FIX = {}


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def translate(svg, tr):
    def rep(m):
        t = m.group(1)
        key = t.strip()
        if key in tr:
            return ">" + t.replace(key, tr[key]) + "<"
        return m.group(0)
    return re.sub(r">([^<>]+)<", rep, svg)


def fit(page, path):
    """Calcula la capsa de tot el dibuix (inclosos els textos) i la posa com a viewBox."""
    page.goto("file://" + str(path))
    bb = page.evaluate("""() => { const s = document.querySelector('svg'); const b = s.getBBox(); return [b.x, b.y, b.width, b.height]; }""")
    return bb


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    meta = json.load(open(SRC / "commons.json", encoding="utf-8"))
    res = {}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": 1600, "height": 1200})
        for key, (fname, tr) in SPEC.items():
            m = meta.get(fname, {})
            if "file" not in m:
                print("falta", fname); continue
            svg = (SRC / m["file"]).read_text(encoding="utf-8")
            svg = translate(svg, tr)
            # en fitxers multilingües (<switch>), l'opció per defecte (sense systemLanguage) és la que hem traduït
            tmp = OUT / f"{key}.svg"
            tmp.write_text(svg, encoding="utf-8")
            x, y, w, h = fit(pg, tmp)
            pad = max(w, h) * 0.02
            vb = f'{x - pad:.1f} {y - pad:.1f} {w + 2 * pad:.1f} {h + 2 * pad:.1f}'
            svg = re.sub(r"<svg\b([^>]*)>", lambda mm: "<svg" + re.sub(r'\s(width|height|viewBox)="[^"]*"', "", mm.group(1)) + f' viewBox="{vb}" width="{w + 2*pad:.0f}" height="{h + 2*pad:.0f}">', svg, count=1)
            tmp.write_text(svg, encoding="utf-8")
            artist = re.sub(r"\s*\(talk.*?\)", "", strip_tags(html.unescape(m.get("artist", "")))).strip()
            lic = m.get("license", "")
            credit = f'Imatge: {artist}, <a href="{m.get("descurl")}" target="_blank" rel="noopener">Wikimedia Commons</a> ({lic}){", etiquetes traduïdes" if tr else ""}.'
            res[key] = {"file": f"{key}.svg", "w": round(w + 2 * pad), "h": round(h + 2 * pad), "credit": credit, "src": fname}
            print(key, vb, lic, artist)
        b.close()
    json.dump(res, open(OUT / "commons.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
