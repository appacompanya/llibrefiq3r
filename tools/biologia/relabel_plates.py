#!/usr/bin/env python3
"""Cobreix els rètols anglesos (traços) de les làmines i hi escriu el català."""
from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

from PIL import Image

ART = Path(__file__).resolve().parent / "art"
PLATES = Path("/tmp/plates")
OCR = Path("/tmp/ocr")
OCR.mkdir(exist_ok=True)

# Paraules que, si l'OCR encara les llegeix després, cal repassar.
ENGLISH = re.compile(
    r"\b(prophase|metaphase|anaphase|telophase|cytokinesis|nucleus|nucleolus|"
    r"membrane|vacuole|chloroplast|cytoplasm|extracellular|hydrophobic|hydrophilic|"
    r"cristae|matrix|granules|ribosome|envelope|golgi|starch|thylakoid|cleavage|"
    r"centriole|centrosome|homologous|chromatids|crossing|equator|spindle|"
    r"microtubule|chiasma|plasma|tonoplast|peroxisome|plasmodesmata|filamentous|"
    r"cytoskeleton|glycoprotein|glycolipid|cholesterol|phospholipid|peripheral|"
    r"integral|synthase|intermembrane|deoxyribonucleic|endoplasmic|reticulum|"
    r"mitochondrion|rough|smooth|outer|inner)\b",
    re.I,
)


def svg_size(name: str) -> tuple[float, float]:
    t = (ART / name).read_text(encoding="utf-8", errors="replace")
    vb = re.search(r'viewBox="\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)"', t)
    if vb:
        return float(vb.group(3)), float(vb.group(4))
    w = float(re.search(r'\bwidth="([\d.]+)', t).group(1))
    h = float(re.search(r'\bheight="([\d.]+)', t).group(1))
    return w, h


def ocr_words(png: Path, psm: str = "11") -> list[dict]:
    stem = png.stem + "w"
    subprocess.check_call(
        ["tesseract", str(png), str(OCR / stem), "-l", "eng", "--psm", psm, "tsv"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    rows = list(csv.DictReader(open(OCR / f"{stem}.tsv"), delimiter="\t"))
    out = []
    for r in rows:
        text = r["text"].strip()
        if len(text) < 2:
            continue
        try:
            conf = float(r["conf"])
        except ValueError:
            continue
        if conf < 40:
            continue
        w, h = int(r["width"]), int(r["height"])
        if w > 420 or h > 80 or w < 8:
            continue
        out.append(
            {
                "x": int(r["left"]),
                "y": int(r["top"]),
                "w": w,
                "h": h,
                "t": text,
            }
        )
    return out


def cluster(words: list[dict], gap: int = 14) -> list[dict]:
    words = sorted(words, key=lambda w: (w["y"], w["x"]))
    phrases: list[dict] = []
    for w in words:
        cy = w["y"] + w["h"] / 2
        placed = False
        for p in phrases:
            pc = p["y"] + p["h"] / 2
            gap_x = w["x"] - (p["x"] + p["w"])
            if abs(cy - pc) < max(w["h"], p["h"]) * 0.55 and -4 <= gap_x <= gap:
                nx = min(p["x"], w["x"])
                ny = min(p["y"], w["y"])
                nr = max(p["x"] + p["w"], w["x"] + w["w"])
                nb = max(p["y"] + p["h"], w["y"] + w["h"])
                p["x"], p["y"], p["w"], p["h"] = nx, ny, nr - nx, nb - ny
                p["t"] = (p["t"] + " " + w["t"]).strip()
                placed = True
                break
        if not placed:
            phrases.append(dict(w))
    return phrases


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _overlaps(a, b) -> bool:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    ix = max(0, min(ax + aw, bx + bw) - max(ax, bx))
    iy = max(0, min(ay + ah, by + bh) - max(ay, by))
    inter = ix * iy
    if inter <= 0:
        return False
    return inter / max(1.0, min(aw * ah, bw * bh)) > 0.25


def overlay_phrases(name: str, mapping: list[tuple[re.Pattern[str], str]], psm: str = "11", gap: int = 22) -> str:
    png = PLATES / name.replace(".svg", ".png")
    im = Image.open(png)
    pw, ph = im.size
    sw, sh = svg_size(name)
    sx, sy = sw / pw, sh / ph
    parts = ['<g id="ca-labels" font-family="DejaVu Sans, Liberation Sans, sans-serif">']
    used = 0
    placed: list[tuple[float, float, float, float]] = []
    for p in cluster(ocr_words(png, psm), gap=gap):
        key = re.sub(r"\s+", " ", p["t"]).strip()
        ca = None
        for rx, repl in mapping:
            if rx.search(key):
                ca = repl
                break
        if ca is None:
            continue
        x = p["x"] * sx
        y = p["y"] * sy
        w = p["w"] * sx
        h = p["h"] * sy
        # El català sol ser més llarg: eixamplem cap a la dreta sense sortir del dibuix.
        est = max(w * 1.05, len(ca) * h * 0.52)
        est = min(max(est, w), sw - x - 2)
        pad = max(1.2, h * 0.18)
        box = (x - pad, y - pad, est + 2 * pad, h + 2 * pad)
        if any(_overlaps(box, old) for old in placed):
            continue
        placed.append(box)
        parts.append(
            f'<rect x="{box[0]:.1f}" y="{box[1]:.1f}" width="{box[2]:.1f}" height="{box[3]:.1f}" fill="#ffffff"/>'
        )
        if ca:
            fs = max(8, h * 0.82)
            parts.append(
                f'<text x="{x:.1f}" y="{y+h*0.82:.1f}" font-size="{fs:.1f}" fill="#1b1f24">{esc(ca)}</text>'
            )
        used += 1
    parts.append("</g>")
    print(f"{name}: {used} rètols coberts")
    return "".join(parts)


def append(name: str, snippet: str) -> None:
    p = ART / name
    t = p.read_text(encoding="utf-8")
    t = re.sub(r'<g id="ca-labels".*?</g>\s*(?=</svg>)', "", t, flags=re.S)
    if "</svg>" not in t:
        raise SystemExit(f"sense </svg> a {name}")
    t = t.replace("</svg>", snippet + "</svg>", 1)
    p.write_text(t, encoding="utf-8")


PLANT = [
    (re.compile(r"filamentous|cytoskeleton", re.I), "citoesquelet"),
    (re.compile(r"plasmodesmata", re.I), "plasmodesmes"),
    (re.compile(r"small membranous", re.I), "vesícules petites"),
    (re.compile(r"^vesicles$", re.I), "vesícules"),
    (re.compile(r"plasma membrane", re.I), "membrana plasmàtica"),
    (re.compile(r"cell wall", re.I), "paret cel·lular"),
    (re.compile(r"chloroplast", re.I), "cloroplast"),
    (re.compile(r"thylakoid", re.I), "membrana del tilacoide"),
    (re.compile(r"starch", re.I), "grànul de midó"),
    (re.compile(r"^smooth$", re.I), "reticle llis"),
    (re.compile(r"^rough$", re.I), "reticle rugós"),
    (re.compile(r"endoplasmic", re.I), ""),
    (re.compile(r"^reticulum$", re.I), ""),
    (re.compile(r"^vacuole$", re.I), "vacúol"),
    (re.compile(r"tonoplast", re.I), "tonoplast"),
    (re.compile(r"ribosome", re.I), "ribosomes"),
    (re.compile(r"mitochondr", re.I), "mitocondri"),
    (re.compile(r"peroxisome", re.I), "peroxisoma"),
    (re.compile(r"cytoplasm", re.I), "citoplasma"),
    (re.compile(r"^nucleus$", re.I), "nucli"),
    (re.compile(r"nuclear pore", re.I), "porus nuclear"),
    (re.compile(r"golgi vesicles", re.I), "vesícules de Golgi"),
    (re.compile(r"nuclear envelope", re.I), "embolcall nuclear"),
    (re.compile(r"nucleolus", re.I), "nuclèol"),
    (re.compile(r"golgi body", re.I), "aparell de Golgi"),
    (re.compile(r"golgi apparatus|\(golgi", re.I), ""),
]

# El reticle llis és a la dreta; el rugós, més al centre. Es desambigua per la x.
def plant_mapping_dynamic(png: Path):
    return PLANT


MITO = [
    (re.compile(r"synthase|ATP", re.I), "ATP-sintasa"),
    (re.compile(r"intermembrane", re.I), "espai intermembranós"),
    (re.compile(r"^matrix", re.I), "matriu"),
    (re.compile(r"crista", re.I), "crestes"),
    (re.compile(r"ribosome", re.I), "ribosoma"),
    (re.compile(r"granule", re.I), "grànuls"),
    (re.compile(r"inner", re.I), "membrana interna"),
    (re.compile(r"outer", re.I), "membrana externa"),
    (re.compile(r"deoxyribo|DNA|\(DNA\)", re.I), "DNA"),
]

MEMBRANE = [
    (re.compile(r"extracellular", re.I), "medi extracel·lular"),
    (re.compile(r"hydrophilic", re.I), "cap hidròfil"),
    (re.compile(r"^head$", re.I), ""),
    (re.compile(r"glycoprot", re.I), "glicoproteïna"),
    (re.compile(r"globular", re.I), "proteïna globular"),
    (re.compile(r"phospholipid", re.I), "bicapa de fosfolípids"),
    (re.compile(r"cholesterol", re.I), "colesterol"),
    (re.compile(r"integral", re.I), "proteïna integral"),
    (re.compile(r"glycolipid", re.I), "glicolípid"),
    (re.compile(r"alpha|helix|hèlix", re.I), "proteïna (hèlix α)"),
    (re.compile(r"peripher", re.I), "proteïna perifèrica"),
    (re.compile(r"hydrophobic|tail", re.I), "cues hidrofòbiques"),
    (re.compile(r"filament|cytoskeleton", re.I), "filaments del citoesquelet"),
    (re.compile(r"cytoplasm", re.I), "citoplasma"),
    (re.compile(r"^prot$", re.I), "proteïna"),
]


def meiosis_overlay() -> str:
    name = "fig-2.7.svg"
    png = PLATES / "fig-2.7.png"
    im = Image.open(png)
    pw, ph = im.size
    sw, sh = svg_size(name)
    sx, sy = sw / pw, sh / ph
    parts = ['<g id="ca-labels" font-family="DejaVu Sans, Liberation Sans, sans-serif">']
    titles = [
        (105.259, "Profase I", None, "#510000"),
        (448.141, "Metafase I", None, "#510000"),
        (790.63, "Anafase I", None, "#510000"),
        (1133.618, "Telofase I", "i citocinesi", "#510000"),
        (1475.418, "Profase II", None, "#7D0000"),
        (1818.317, "Metafase II", None, "#7D0000"),
        (2159.318, "Anafase II", None, "#7D0000"),
        (2499.717, "Telofase II", "i citocinesi", "#7D0000"),
    ]
    for x, a, b, col in titles:
        parts.append(f'<rect x="{x:.2f}" y="27.94" width="261.68" height="77.04" fill="{col}"/>')
        if b:
            parts.append(
                f'<text x="{x+130.8:.1f}" y="58" text-anchor="middle" font-size="26" fill="#ffffff" font-weight="700">{esc(a)}</text>'
            )
            parts.append(
                f'<text x="{x+130.8:.1f}" y="88" text-anchor="middle" font-size="20" fill="#ffffff">{esc(b)}</text>'
            )
        else:
            parts.append(
                f'<text x="{x+130.8:.1f}" y="74" text-anchor="middle" font-size="28" fill="#ffffff" font-weight="700">{esc(a)}</text>'
            )
    # Peus en anglès: només es tapa la caixa de les paraules, no la cèl·lula.
    # (x0, x1, y0, y1 en píxels del PNG a 4200 px d'ample, línies en català)
    caps = [
        (40, 680, 900, 1050, ["Els cromosomes es condensen", "i l'embolcall es desfa.", "Hi ha entrecreuament."]),
        (690, 1120, 900, 1050, ["Els parells d'homòlegs", "van a l'equador."]),
        (1140, 1680, 900, 1040, ["Els homòlegs se separen", "cap als pols."]),
        (1700, 2150, 900, 1060, ["Arriben als pols.", "El citoplasma es divideix."]),
        (2150, 2700, 590, 720, ["Es forma un fus nou", "al voltant dels cromosomes."]),
        (2700, 3200, 590, 720, ["S'alineen a l'equador."]),
        (3200, 3720, 580, 760, ["Els centròmers es divideixen.", "Les cromàtides van als pols."]),
        (3700, 4180, 580, 760, ["Es forma l'embolcall.", "El citoplasma es divideix."]),
    ]
    words = ocr_words(png, "6")
    for x0, x1, y0, y1, lines in caps:
        inside = [
            w for w in words
            if x0 <= w["x"] + w["w"] / 2 <= x1 and y0 <= w["y"] <= y1
        ]
        if not inside:
            continue
        for w in inside:
            parts.append(
                f'<rect x="{w["x"]*sx-1:.1f}" y="{w["y"]*sy-1:.1f}" width="{w["w"]*sx+3:.1f}" height="{w["h"]*sy+2:.1f}" fill="#ffffff"/>'
            )
        ax = min(w["x"] for w in inside) * sx
        ay = min(w["y"] for w in inside) * sy
        fs = 13
        for k, line in enumerate(lines):
            parts.append(
                f'<text x="{ax:.1f}" y="{ay+fs+k*(fs+3):.1f}" font-size="{fs}" fill="#1b1f24">{esc(line)}</text>'
            )
    callouts = [
        (re.compile(r"cleavage", re.I), "solc de segmentació"),
        (re.compile(r"centriole", re.I), "centríols"),
        (re.compile(r"centrosome", re.I), "centrosoma"),
        (re.compile(r"centromere", re.I), "els centròmers es divideixen"),
        (re.compile(r"homologous", re.I), "cromosomes homòlegs"),
        (re.compile(r"nuclear envelope", re.I), "embolcall nuclear"),
        (re.compile(r"fragment", re.I), "fragment"),
        (re.compile(r"chromatid", re.I), "cromàtides germanes"),
        (re.compile(r"microtubule", re.I), "microtúbul"),
        (re.compile(r"chiasm", re.I), "quiasma"),
        (re.compile(r"kinetochore", re.I), "cinetocor"),
        (re.compile(r"\bwith\b", re.I), ""),
        (re.compile(r"^sister$", re.I), ""),
    ]
    def in_cap(px, py):
        for x0, x1, y0, y1, _lines in caps:
            if x0 <= px <= x1 and y0 <= py <= y1:
                return True
        return False

    for p in cluster(ocr_words(png, "6"), gap=18):
        if p["y"] > 880 or in_cap(p["x"], p["y"]):
            continue
        ca = None
        hit = False
        for rx, repl in callouts:
            if rx.search(p["t"]):
                ca = repl
                hit = True
                break
        if not hit:
            continue
        x, y, w, h = p["x"] * sx, p["y"] * sy, p["w"] * sx, p["h"] * sy
        est = max(w, len(ca) * h * 0.52) if ca else w
        parts.append(f'<rect x="{x-1:.1f}" y="{y-1:.1f}" width="{est+4:.1f}" height="{h+3:.1f}" fill="#ffffff"/>')
        if ca:
            parts.append(
                f'<text x="{x:.1f}" y="{y+h*0.8:.1f}" font-size="{max(9,h*0.8):.1f}" fill="#1b1f24">{esc(ca)}</text>'
            )
    # «(with kinetochore)» queda sota el llindar de confiança de l'OCR.
    parts.append('<rect x="520" y="208" width="130" height="34" fill="#ffffff"/>')
    parts.append('<text x="526" y="230" font-size="15" fill="#1b1f24">cinetocor</text>')
    parts.append("</g>")
    return "".join(parts)


def main() -> None:
    jobs = [
        ("fig-2.3b.svg", PLANT, "11", 18),
        ("fig-2.4.svg", MITO, "11", 40),
        ("fig-2.2.svg", MEMBRANE, "11", 22),
    ]
    for name, mapping, psm, gap in jobs:
        append(name, overlay_phrases(name, mapping, psm, gap))
    append("fig-2.7.svg", meiosis_overlay())
    print("ok")


if __name__ == "__main__":
    main()
