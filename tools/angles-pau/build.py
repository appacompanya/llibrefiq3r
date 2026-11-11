#!/usr/bin/env python3
"""Genera angles/ (PAU d'anglès per blocs) a partir de les fonts baixades per fonts.py (branca fonts-pau-angles).

Escriu:
  angles/enunciats_{listening,reading,writing}.pdf, solucions_*.pdf, quadern_enunciats.pdf, quadern_solucions.pdf
  angles/mobil/*_mobil.pdf   (marges retallats; mateixa numeració de pàgines)
  angles/audio/AAAA-conv-sN.mp3   (mono, 48 kbps)
  angles/exercicis.json
Ús: python3 tools/angles-pau/build.py /camí/a/fonts-pau-angles
"""
import json, re, subprocess, sys, unicodedata
from pathlib import Path
import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).parent))
from segmenta import exam_series, key_series  # noqa: E402

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/claude/fonts-angles") / "dropbox"
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "angles"
ANYS = range(2026, 2010, -1)
CONVS = [("june", "Juny", False), ("june_tei", "Juny", True), ("sept", "Setembre", False)]
BLOCS = [("listening", "Listening", "Comprensió oral · 3 punts"),
         ("reading", "Reading", "Comprensió escrita · 3 punts"),
         ("writing", "Writing", "Expressió escrita · 4 punts")]


def words(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return set(w for w in re.findall(r"[a-z0-9]+", s) if len(w) > 2 or w.isdigit()) - {"the", "and", "with", "interview", "conversation", "mp3"}


def sim(a, b):
    a, b = words(a), words(b)
    return len(a & b) / max(1, min(len(a), len(b)))


def nice(t):
    if not t:
        return None
    t = re.sub(r"[“”\"]", "", t).strip(" .")
    if t.isupper():
        small = {"a", "an", "the", "of", "in", "on", "at", "to", "for", "and", "or", "with", "is", "are", "as", "by", "from", "your", "you"}
        out = []
        for i, w in enumerate(t.lower().split()):
            out.append(w if (i and w in small) else w[:1].upper() + w[1:])
        t = " ".join(out)
        t = re.sub(r"\b(Us|Uk|Ai|Bbc|Usa|U\.s\.)\b", lambda m: m.group(1).upper(), t)
    return t


def reading_title(T, pages):
    for p in pages[:2]:
        for l in (x.strip() for x in T[p].splitlines()):
            if len(l) > 10 and l.isupper() and not re.match(r"(PART|SÈRIE|QUESTIONS|PROVES)", l) and not re.search(r"\d\s*$", l):
                return l
    return None


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


FONT = fitz.Font("hebo")


def label_page(page, text):
    """Etiqueta discreta a dalt a la dreta de la primera pàgina de cada examen."""
    w = page.rect.width
    tw = FONT.text_length(text, fontsize=8.5)
    box = fitz.Rect(w - tw - 34, 8, w - 18, 24)
    page.draw_rect(box, color=None, fill=(0.11, 0.16, 0.23), overlay=True)
    tw_ = fitz.TextWriter(page.rect, color=(1, 1, 1))
    tw_.append((box.x0 + 8, box.y1 - 4.8), text, font=FONT, fontsize=8.5)
    tw_.write_text(page, overlay=True)


def main():
    audios = sorted((SRC / "audios").glob("*.mp3"))
    items = []
    for y in ANYS:
        yy = f"{y % 100:02d}"
        for code, conv, tei in CONVS:
            ef = SRC / "examens" / f"pau_angl{yy}{code}.pdf"
            if not ef.exists():
                continue
            kf = next(iter(sorted((SRC / "solucions").glob(f"pau_angl{yy}{code}[_-]key.pdf"))), None)
            ed, ET, ES = exam_series(ef)
            kd, KT, KS = key_series(kf) if kf else (None, [], [])
            pref = ("june" if code.startswith("june") else "sept") + yy
            cand = [a for a in audios if re.match(rf"{pref}(?:_tei)?\b|{pref}[\s\-_]", a.stem)]
            cand = [a for a in cand if ("_tei" in a.stem) == tei]
            used = set()
            for si, s in enumerate(ES):
                lt = s.get("listening_title")
                # pauta: per títol del listening; si no n'hi ha, per ordre
                ks = None
                if KS:
                    best = max(KS, key=lambda k: sim(lt, k.get("listening_title")))
                    if sim(lt, best.get("listening_title")) >= 0.5:
                        ks = best
                    elif len(KS) == len(ES):
                        ks = KS[si]
                # àudio: per paraules del títol
                au = None
                if cand:
                    best = max(cand, key=lambda a: sim(lt, re.sub(r"^(june|sept)\d+(_tei)?", "", a.stem)))
                    if sim(lt, re.sub(r"^(june|sept)\d+(_tei)?", "", best.stem)) >= 0.34 or (len(cand) == 1 and len(ES) == 1):
                        au = best
                if au in used:
                    au = None
                if au:
                    used.add(au)
                items.append({
                    "any": y, "conv": conv, "tei": tei, "serie": s.get("serie"), "ed": ed, "ET": ET, "ep": s["pages"],
                    "kd": kd, "kp": ks["pages"] if ks else {},
                    "lt": nice(lt or (ks or {}).get("listening_title")), "rt": nice(reading_title(ET, s["pages"].get("reading", []))),
                    "audio_src": au,
                })
    print(len(items), "exàmens")

    (OUT / "mobil").mkdir(parents=True, exist_ok=True)
    (OUT / "audio").mkdir(exist_ok=True)
    for old in list(OUT.glob("*.pdf")) + list((OUT / "mobil").glob("*.pdf")):
        old.unlink()

    # àudios
    for it in items:
        it["slug"] = f"{it['any']}-{it['conv'].lower()}{'-tei' if it['tei'] else ''}-s{it['serie'] or 0}"
        if it["audio_src"]:
            dst = OUT / "audio" / f"{it['slug']}.mp3"
            if not dst.exists():
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(it["audio_src"]), "-ac", "1", "-ar", "22050", "-b:a", "48k", "-map_metadata", "-1", str(dst)], check=True)
            it["a"] = f"audio/{dst.name}"
            dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(dst)], capture_output=True, text=True).stdout
            it["dur"] = round(float(dur or 0))
        else:
            it["a"] = None

    def lab(it):
        return f"PAU {it['any']} · {it['conv']}{' (TEI)' if it['tei'] else ''}" + (f" · Sèrie {it['serie']}" if it["serie"] else "")

    caps, quad = [], {"e": fitz.open(), "s": fitz.open()}
    qtoc = {"e": [], "s": []}
    for n, (b, titol, sub) in enumerate(BLOCS, 1):
        docs = {"e": fitz.open(), "s": fitz.open()}
        toc = {"e": [], "s": []}
        cnt = {"e": 0, "s": 0}
        for it in items:
            for k, src, pages in (("e", it["ed"], it["ep"].get(b, [])), ("s", it["kd"], it["kp"].get(b, []))):
                if not pages or src is None:
                    it[f"{b}_{k}"] = None
                    continue
                start = len(docs[k]) + 1
                for p in pages:
                    docs[k].insert_pdf(src, from_page=p, to_page=p)
                label_page(docs[k][start - 1], f"{titol} · {lab(it)}")
                it[f"{b}_{k}"] = start
                cnt[k] += 1
                name = lab(it) + (f" · {it['lt']}" if b == "listening" and it["lt"] else f" · {it['rt']}" if b == "reading" and it["rt"] else "")
                toc[k].append([1, name, start])
        c = {"n": n, "slug": b, "titol": titol, "sub": sub, "exercicis": cnt["e"], "solucions_n": cnt["s"]}
        for k, pre in (("e", "enunciats"), ("s", "solucions")):
            d = docs[k]
            d.set_toc(toc[k])
            fn = f"{pre}_{b}.pdf"
            d.save(OUT / fn, garbage=4, deflate=True)
            m = fitz.open(OUT / fn); crop(m); m.save(OUT / "mobil" / f"{pre}_{b}_mobil.pdf", garbage=4, deflate=True)
            off = len(quad[k])
            quad[k].insert_pdf(d)
            qtoc[k].append([1, f"{n}. {titol}", off + 1])
            qtoc[k] += [[2, t, p + off] for _, t, p in toc[k]]
            c[pre] = fn
            c[f"pagines_{pre}"] = len(d)
            c[f"mb_{pre}"] = round((OUT / fn).stat().st_size / 1e6, 1)
            for it in items:
                if it.get(f"{b}_{k}"):
                    it[f"{b}_q{k}"] = it[f"{b}_{k}"] + off
        caps.append(c)
    for k, pre in (("e", "enunciats"), ("s", "solucions")):
        quad[k].set_toc(qtoc[k])
        quad[k].save(OUT / f"quadern_{pre}.pdf", garbage=4, deflate=True)
        m = fitz.open(OUT / f"quadern_{pre}.pdf"); crop(m); m.save(OUT / "mobil" / f"quadern_{pre}_mobil.pdf", garbage=4, deflate=True)

    ex = []
    for i, it in enumerate(items, 1):
        ex.append({
            "ex": i, "id": it["slug"], "any": it["any"], "conv": it["conv"], "tei": it["tei"], "serie": it["serie"],
            "model": "Model actual" if it["any"] >= 2025 else "Model anterior",
            "lt": it["lt"], "rt": it["rt"], "a": it["a"], "dur": it.get("dur"),
            "p": {b: {"e": it.get(f"{b}_e"), "s": it.get(f"{b}_s")} for b, _, _ in BLOCS},
        })
    data = {"meta": {"quadern_enunciats": "quadern_enunciats.pdf", "quadern_solucions": "quadern_solucions.pdf",
                     "pagines_quadern_enunciats": len(quad["e"]), "pagines_quadern_solucions": len(quad["s"]),
                     "total": len(ex), "audios": sum(1 for x in ex if x["a"]), "anys": [min(ANYS), max(ANYS)]},
            "capitols": caps, "exercicis": ex}
    (OUT / "exercicis.json").write_text(json.dumps(data, ensure_ascii=False, indent=0), encoding="utf-8")
    for it in items:
        miss = [b for b, _, _ in BLOCS if not it.get(f"{b}_s")]
        print(f"{it['slug']:24} L={it['lt']!s:45.45} R={it['rt']!s:35.35} àudio={'sí' if it['a'] else 'NO'} sense pauta={','.join(miss) or '-'}")


if __name__ == "__main__":
    main()
