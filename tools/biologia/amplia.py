"""Junta les ampliacions dels nou temes."""
from amplia_a import MORE as A
from amplia_b import MORE as B
from amplia_c import MORE as C
from amplia_d import MORE as D
from amplia_f import MORE as F
from amplia_g import MORE as G
from amplia_h import MORE as H

MORE = {}
for part in (A, B, C, D, F, G, H):
    for key, html in part.items():
        MORE[key] = MORE.get(key, "") + "\n" + html

