"""Format numèric del llibre: coma decimal i arrodoniment escolar (meitat cap amunt)."""
from decimal import Decimal, ROUND_HALF_UP

G = 9.8


def fmt(x, d=2):
    """Arrodoneix a d decimals i retorna el nombre amb coma decimal."""
    q = Decimal(10) ** -d
    r = Decimal(format(float(x), ".12f")).quantize(q, rounding=ROUND_HALF_UP)
    if d == 0:
        return str(int(r))
    return f"{r:.{d}f}".replace(".", ",")


def num(x, d=2):
    return fmt(x, d)
