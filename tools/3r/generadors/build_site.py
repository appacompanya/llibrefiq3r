"""Retirat. L'antic build_site.py refeia una web estàtica a partir de la sortida de build_web.py.

No el facis servir per publicar el llibre. La web viva és l'arrel del repositori
(index.html, digital/) i surt de contingut/3r/*.yaml:

  python3 tools/3r/build_dades.py --aplica-html --estricte
"""
import sys

sys.stderr.write(
    "Aturat: build_site.py és el camí antic (build_web.py → web estàtica) i no s'ha d'usar per publicar.\n"
    "Usa: python3 tools/3r/build_dades.py --aplica-html --estricte\n"
)
sys.exit(1)
