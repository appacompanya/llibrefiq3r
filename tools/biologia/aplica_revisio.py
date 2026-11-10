#!/usr/bin/env python3
"""Aplica tools/biologia/revisio.py al text extret i escriu contingut/biologia/teoria-revisat.json."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import revisio

ROOT = Path(__file__).resolve().parents[2]
els = json.load(open(ROOT / "contingut/biologia/teoria-extret.json", encoding="utf-8"))


for i, e in enumerate(els):
    e["oid"] = str(i)
BY = {e["oid"]: e for e in els}


def get(path):
    parts = path.split(".")
    cur = BY[parts[0]]
    parent, idx = None, None
    for p in parts[1:]:
        parent, idx = cur["children"], int(p)
        cur = cur["children"][idx]
    return cur, parent, idx


def field(e):
    return "html" if "html" in e else ("caption" if "caption" in e else None)


errors = []
for c in list(revisio.C) + list(getattr(revisio, "F", [])):
    kind, path = c[0], c[1]
    try:
        e, parent, idx = get(path)
    except (IndexError, KeyError):
        errors.append(f"camí inexistent {path}"); continue
    if kind == "sub":
        old, new = c[2], c[3]
        if e["t"] == "table":
            done = False
            for row in [e["head"]] + e["rows"]:
                for i, cell in enumerate(row):
                    plain = re.sub("<[^>]+>", "", cell)
                    if " | " in old:
                        a, b = old.split(" | "); na, nb = new.split(" | ")
                        if a in plain and i + 1 < len(row) and re.sub("<[^>]+>", "", row[i + 1]) == b:
                            row[i] = na; row[i + 1] = nb; done = True
                    elif old in cell:
                        row[i] = cell.replace(old, new); done = True
            if not done:
                errors.append(f"no trobat a la taula {path}: {old[:50]}")
            continue
        f = field(e)
        h = e.get(f, "")
        if old in h:
            e[f] = h.replace(old, new)
        else:
            hp = re.sub(r"<sub>(.*?)</sub>", r"_\1", h)
            if old in hp:
                e[f] = re.sub(r"_(\w+)", r"<sub>\1</sub>", hp.replace(old, new))
            else:
                errors.append(f"no trobat {path}: {old[:60]}")
    elif kind == "set":
        e[field(e)] = c[2]
    elif kind == "del":
        e["_del"] = True
    elif kind == "rep":
        e.clear(); e.update(c[2]); e["oid"] = path
    elif kind == "ins":      # abans de l'element
        e.setdefault("_before", []).append(c[2])
    elif kind == "after":    # després de l'element
        e.setdefault("_after", []).append(c[2])


def expand(lst):
    out = []
    for e in lst:
        out += e.pop("_before", [])
        after = e.pop("_after", [])
        if "children" in e:
            e["children"] = expand(e["children"])
        if not e.get("_del"):
            out.append(e)
        out += after
    return out


els = expand(els)


def glob(h):
    for a, b in revisio.GLOBAL:
        h = re.sub(a, b, h)
    return h


def walk(e):
    for k in ("html", "caption"):
        if k in e:
            e[k] = glob(e[k])
    if e["t"] == "table":
        e["head"] = [glob(x) for x in e["head"]]
        e["rows"] = [[glob(x) for x in r] for r in e["rows"]]
    for c in e.get("children", []):
        walk(c)


for e in els:
    walk(e)
json.dump(els, open(ROOT / "contingut/biologia/teoria-revisat.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(els), "elements;", len(errors), "errors")
for x in errors:
    print(" -", x)
