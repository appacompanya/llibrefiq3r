#!/usr/bin/env python3
"""Genera biologia/biologia-teoria.pdf a partir de biologia/teoria.html (Chrome).

Mateix paper que tools/btx/pdf_teoria.js: el HTML llarg de teoria, amb fons i marges.
Ús: python3 tools/biologia/pdf_teoria.py
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "biologia" / "teoria.html"
OUT = ROOT / "biologia" / "biologia-teoria.pdf"


def main() -> None:
    if not HTML.is_file():
        raise SystemExit("Falta biologia/teoria.html. Executeu abans tools/biologia/build.py")
    cmd = [
        "google-chrome",
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--user-data-dir=/tmp/biologia-pdf-chrome",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUT}",
        HTML.as_uri(),
    ]
    proc = subprocess.Popen(cmd)
    try:
        proc.wait(timeout=180)
    except subprocess.TimeoutExpired:
        proc.kill()
    if not OUT.is_file() or OUT.stat().st_size < 10000:
        raise SystemExit("El PDF no s'ha generat")
    print(f"PDF: {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
