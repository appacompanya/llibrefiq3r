"""Retirat. Construïa digital/index.html a partir de la web estàtica antiga.

No és tools/digital-pdf/build_digital.py (aquest sí que reconstrueix 2n i 4t).
Per a 3r:

  python3 tools/3r/build_dades.py --aplica-html --estricte
"""
import sys

sys.stderr.write(
    "Aturat: tools/3r/generadors/build_digital.py és el camí antic de 3r.\n"
    "Usa: python3 tools/3r/build_dades.py --aplica-html --estricte\n"
    "El de 2n i 4t és un altre fitxer: tools/digital-pdf/build_digital.py\n"
)
sys.exit(1)
