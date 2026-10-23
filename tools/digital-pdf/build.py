"""Regenera el llibre digital d'un nivell a partir dels PDF dels fulls: python3 build.py 2n|4t
1. pdf2html.py     PDF → HTML (i imatges de les figures a <nivell>/digital/fimg/)
2. build_fitxes.py HTML → fitxes interactives (<nivell>/digital/js/fitxes-auto.js)
3. build_digital.py llibre de l'alumnat i zona del professorat (<nivell>/digital/)
4. qa.py           avisos de possibles errors de conversió"""
import os, sys, glob, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from nivell import LEVEL, ROOT
for f in glob.glob(os.path.join(ROOT, LEVEL, "digital", "fimg", "*.webp")): os.remove(f)
env = dict(os.environ, FQ_NIVELL=LEVEL, PYTHONWARNINGS="ignore")
for step in ("pdf2html.py", "build_fitxes.py", "build_digital.py", "qa.py"):
    print("==", step, flush=True)
    r = subprocess.run([sys.executable, os.path.join(HERE, step)], env=env, capture_output=step == "pdf2html.py", text=True)
    if r.returncode: print(r.stdout or "", r.stderr or ""); raise SystemExit(f"{step} ha fallat")
