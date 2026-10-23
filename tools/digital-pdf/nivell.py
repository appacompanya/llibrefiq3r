"""Nivell que es construeix (2n o 4t): variable d'entorn FQ_NIVELL o primer argument «2n» / «4t»."""
import os, sys
NIVELLS = ("2n", "4t")
LEVEL = os.environ.get("FQ_NIVELL", "")
for a in list(sys.argv[1:]):
    if a in NIVELLS:
        LEVEL = a; sys.argv.remove(a)
if LEVEL not in NIVELLS:
    raise SystemExit("Indica el nivell: 2n o 4t (p. ex. python3 build.py 4t)")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
TMP = os.path.join(HERE, "_html", LEVEL)          # HTML intermedi
IMGPFX = "n" + LEVEL[0]                            # prefix de les imatges: n2…, n4…
