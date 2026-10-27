#!/usr/bin/env python3
"""Uneix la portada actual (pàgina 1 de btx/fisica-II-teoria.pdf) amb el PDF nou generat per pdf_teoria.js."""
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT / "btx" / "fisica-II-teoria.pdf"
NOU = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "btx" / "_teoria_sense_portada.pdf"
w = PdfWriter()
w.add_page(PdfReader(PDF).pages[0])
for pg in PdfReader(NOU).pages:
    w.add_page(pg)
w.add_metadata({"/Title": "Física II (teoria)"})
tmp = PDF.with_suffix(".tmp.pdf")
w.write(tmp)
tmp.replace(PDF)
NOU.unlink()
print(f"{PDF}: {len(w.pages)} pàgines")
