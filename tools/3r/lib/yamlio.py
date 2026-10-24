"""Llegeix i desa els YAML de contingut/3r conservant la capçalera de comentaris i el format."""
import yaml


class Dumper(yaml.SafeDumper):
    pass


def _str(d, s):
    if "\n" in s:
        return d.represent_scalar("tag:yaml.org,2002:str", s, style="|")
    return d.represent_scalar("tag:yaml.org,2002:str", s)


Dumper.add_representer(str, _str)


def load(path):
    txt = open(path).read()
    head = "".join(l for l in txt.splitlines(True) if l.startswith("#") and txt.startswith(l[:1]))
    head = ""
    for l in txt.splitlines(True):
        if l.startswith("#"): head += l
        else: break
    return yaml.safe_load(txt), head


def save(path, obj, head=""):
    with open(path, "w") as f:
        f.write(head)
        yaml.dump(obj, f, Dumper=Dumper, allow_unicode=True, sort_keys=False, width=1000)
