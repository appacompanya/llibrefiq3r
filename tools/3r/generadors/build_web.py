"""Retirat. No reconstrueixis la web de 3r des de template.html.

template.html és una còpia anterior del llibre. Aquest script escrivia index.html
i profe.html a partir d'aquesta còpia i podia substituir la web publicada.

Font única: contingut/3r/*.yaml
Pipeline actual:
  python3 tools/3r/build_dades.py --aplica-html --estricte

Això regenera digital/js/dades-generades.js i copia els blocs D, L, SDAS,
EVAL i CRIT_NAMES dins de index.html, digital/index.html i digital/profe.html.

dades-generades.js no el carrega el navegador. És la foto intermèdia.
Sense --aplica-html, les pàgines queden amb els blocs vells.
"""
import sys

sys.stderr.write(
    "Aturat: build_web.py sobreescriuria la web amb tools/3r/generadors/template.html, que és una còpia vella.\n"
    "Usa la font YAML i el pipeline actual:\n"
    "  python3 tools/3r/build_dades.py --aplica-html --estricte\n"
    "dades-generades.js es genera però no es carrega al navegador: --aplica-html el copia dins les pàgines.\n"
)
sys.exit(1)
