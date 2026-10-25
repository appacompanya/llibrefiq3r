#!/usr/bin/env python3
"""Anteposa la portada a btx/fisica-II-teoria.pdf.

Il·lustració: btx/assets/portada-fisica-II.png (sang complet, DIN A4).
Títol «Física II» a dalt; «Autor: Macià Esteve Pallarès Pallarès» a baix,
un 35% més petit que el crèdit de 18 pt (18 × 0,65 = 11,7 pt).

Si la primera pàgina ja és aquesta portada, la substitueix.
"""

from __future__ import annotations

import io
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "btx" / "assets" / "portada-fisica-II.png"
PDF = ROOT / "btx" / "fisica-II-teoria.pdf"
FONTS = ROOT / "btx" / "assets" / "fonts"

TITOL = "Física II"
AUTOR = "Autor: Macià Esteve Pallarès Pallarès"
# Crèdit inicial 18 pt; la línia d'autor aprovada és un 35% més petita.
AUTOR_PT = 18 * 0.65  # 11.7
TITOL_PT = 58


def _ttf(woff2: Path) -> bytes:
    font = TTFont(woff2)
    font.flavor = None
    buf = io.BytesIO()
    font.save(buf)
    return buf.getvalue()


def _fonts() -> tuple[bytes, bytes]:
    bric = _ttf(FONTS / "Bricolage-ExtraBold.woff2")
    atk = _ttf(FONTS / "Atkinson-Regular.woff2")
    if "Bricolage" not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(RLFont("Bricolage", io.BytesIO(bric)))
        pdfmetrics.registerFont(RLFont("Atkinson", io.BytesIO(atk)))
    return bric, atk


def _draw_line(c: canvas.Canvas, text: str, font: str, size: float, x: float, y: float, fill: Color, tracking: float) -> None:
    t = c.beginText()
    t.setTextOrigin(x, y)
    t.setFont(font, size)
    t.setCharSpace(tracking)
    t.setFillColor(fill)
    t.textOut(text)
    c.drawText(t)


def _background(pagesize: tuple[float, float], bric: bytes, atk: bytes) -> io.BytesIO:
    """Il·lustració a sang amb l'ombra del text ja integrada."""
    _, h = pagesize
    art = Image.open(ART).convert("RGB")
    th = max(1, round(art.width * h / w))
    art = art.resize((art.width, th), Image.Resampling.LANCZOS)
    px = th / h
    shadow = Image.new("RGBA", art.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow)
    fb = ImageFont.truetype(io.BytesIO(bric), max(1, round(TITOL_PT * px)))
    fa = ImageFont.truetype(io.BytesIO(atk), max(1, round(AUTOR_PT * px)))

    def blot(text: str, font: ImageFont.FreeTypeFont, baseline: float, tracking: float) -> None:
        advances = [font.getlength(ch) for ch in text]
        gap = tracking * px
        total = sum(advances) + gap * max(0, len(text) - 1)
        cx = (art.width - total) / 2
        cy = (h - baseline) / h * th
        for ch, adv in zip(text, advances):
            draw.text((cx, cy), ch, font=font, fill=(1, 4, 12, 220), anchor="ls")
            cx += adv + gap

    blot(TITOL, fb, h - h * 0.118, 0.4)
    blot(AUTOR, fa, h * 0.145, 0.25)
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=max(1.2, 1.3 * px)))
    base = art.convert("RGBA")
    base.alpha_composite(shadow)
    out = io.BytesIO()
    base.convert("RGB").save(out, format="JPEG", quality=92, optimize=True)
    out.seek(0)
    return out


def _draw_centered(c: canvas.Canvas, text: str, font: str, size: float, y: float, fill: Color, tracking: float = 0) -> None:
    width = c.stringWidth(text, font, size) + tracking * max(0, len(text) - 1)
    x = (float(c._pagesize[0]) - width) / 2
    _draw_line(c, text, font, size, x, y, fill, tracking)


def portada_pdf(pagesize: tuple[float, float]) -> bytes:
    bric, atk = _fonts()
    w, h = pagesize
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=pagesize)
    c.drawImage(ImageReader(_background(pagesize, bric, atk)), 0, 0, width=w, height=h, preserveAspectRatio=False, anchor="sw")
    # Franja fosca superior (el sol queda a l'esquerra i la galàxia a la dreta).
    _draw_centered(c, TITOL, "Bricolage", TITOL_PT, h - h * 0.118, Color(1, 0.99, 0.97), tracking=0.4)
    # Franja fosca sota la Terra, abans de la nebulosa de la dreta.
    _draw_centered(c, AUTOR, "Atkinson", AUTOR_PT, h * 0.145, Color(0.96, 0.97, 0.99), tracking=0.25)
    c.save()
    return buf.getvalue()


def _es_portada(page) -> bool:
    text = page.extract_text() or ""
    return AUTOR in text and "Índex" not in text


def main() -> None:
    if not ART.is_file():
        raise SystemExit(f"No hi ha la il·lustració: {ART}")
    if not PDF.is_file():
        raise SystemExit(f"No hi ha el PDF: {PDF}")
    orig = PdfReader(str(PDF))
    box = orig.pages[0].mediabox
    pagesize = (float(box.width), float(box.height))
    cover = PdfReader(io.BytesIO(portada_pdf(pagesize)))
    start = 1 if _es_portada(orig.pages[0]) else 0
    out = PdfWriter()
    out.add_page(cover.pages[0])
    for page in orig.pages[start:]:
        out.add_page(page)
    if orig.metadata:
        out.add_metadata({k: v for k, v in orig.metadata.items() if v})
    tmp = PDF.with_suffix(".pdf.tmp")
    with tmp.open("wb") as f:
        out.write(f)
    tmp.replace(PDF)
    print(f"{PDF.name}: {len(orig.pages)} → {len(out.pages)} pàgines ({pagesize[0]:.2f}×{pagesize[1]:.2f} pt)")


if __name__ == "__main__":
    main()
