#!/usr/bin/env python3
"""Busca a l'arxiu de la Wayback Machine els PDF de Química de la PAU que la Generalitat ja no enllaça (2011–2023) i els baixa.

S'executa a GitHub Actions. Escriu a <out>/wb/ els PDF i <out>/wb/llista.tsv.
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "fonts") / "wb"
OUT.mkdir(parents=True, exist_ok=True)
PREFIXES = [
    "universitats.gencat.cat/web/.content/",
    "universitatsirecerca.gencat.cat/web/.content/",
    "www20.gencat.cat/docs/",
    "www.gencat.cat/economia/ur/",
    "www10.gencat.cat/",
]
UA = {"User-Agent": "Mozilla/5.0 (llibrefiq3r; recull PAU Química per a ús educatiu)"}


def get(url, tries=4):
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
                return r.read()
        except Exception as e:
            err = e
            time.sleep(5 * (k + 1))
    raise err


found = {}
log = open(OUT / "cdx.txt", "w")
for pre in PREFIXES:
    q = ("https://web.archive.org/cdx/search/cdx?url=" + urllib.parse.quote(pre + "*", safe="*/:.")
         + "&output=json&fl=timestamp,original,mimetype,statuscode&filter=statuscode:200"
         + "&filter=original:" + urllib.parse.quote("(?i).*qu[ií]m.*\\.pdf.*") + "&collapse=urlkey&limit=5000")
    try:
        rows = json.loads(get(q) or b"[]")
    except Exception as e:
        log.write(f"ERR\t{pre}\t{e}\n"); continue
    log.write(f"OK\t{pre}\t{len(rows)}\n")
    for ts, orig, mt, st in rows[1:]:
        key = re.sub(r"^https?://", "", orig).split("?")[0].lower()
        if key not in found or ts > found[key][0]:
            found[key] = (ts, orig)
    time.sleep(2)
log.close()

with open(OUT / "llista.tsv", "w") as f:
    for key, (ts, orig) in sorted(found.items()):
        name = re.sub(r"[^A-Za-z0-9._-]+", "__", key.split("/web/.content/")[-1].split("/docs/")[-1])[-150:]
        try:
            body = get(f"https://web.archive.org/web/{ts}id_/{orig}")
            if not body.startswith(b"%PDF"):
                raise ValueError("no és PDF")
            (OUT / name).write_bytes(body)
            f.write(f"{name}\t{len(body)}\t{orig}\t{ts}\n")
        except Exception as e:
            f.write(f"ERR\t0\t{orig}\t{e}\n")
        f.flush()
        time.sleep(1.5)
print(len(found), "PDF trobats a l'arxiu")
