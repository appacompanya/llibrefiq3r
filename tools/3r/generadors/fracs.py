import re
def fr(a,b):
    st=lambda x: x[1:-1] if x.startswith("(") and x.endswith(")") and x.count("(")==1 else x
    return f'<span class="fr"><span>{st(a)}</span><span>{st(b)}</span></span>'
SPECIAL=[("massa de solut (g) / volum de dissolució (L)",fr("massa de solut (g)","volum de dissolució (L)")),("massa de solut / massa de dissolució · 100",fr("massa de solut","massa de dissolució")+" · 100"),
 ("massa de solut / volum",fr("massa de solut","volum")),("mida a la imatge / augments",fr("mida a la imatge","augments")),("E<sub>a</sub> / valor de referència · 100",fr("E<sub>a</sub>","valor de referència")+" · 100"),("(canvi de l'eix vertical) / (canvi de l'eix horitzontal)",fr("canvi de l'eix vertical","canvi de l'eix horitzontal")),
 ("en kW (W / 1 000)","en kW (divideix els watts entre 1 000)"),("(V final − V inicial) / V inicial",fr("V final − V inicial","V inicial")),("4/3 ·",fr("4","3")+" ·"),
 ("error absolut / referència · 100",fr("error absolut","referència")+" · 100"),("llum / elèctrica · 100",fr("llum","elèctrica")+" · 100"),("3 / 8 · 100",fr("3","8")+" · 100"),
 ("energia útil / energia consumida · 100",fr("energia útil","energia consumida")+" · 100"),
 ("11 kg · 132 / 44",fr("11 · 132","44")),("17 · 10⁻⁶ m / 60 s",fr("17 · 10⁻⁶ m","60 s")),("40 000 mg / 1000 mL",fr("40 000 mg","1000 mL")),
 ("P (W) · hores / 1000",fr("P (W) · hores","1000")),("Wh → / 1000","Wh → "+fr("…","1000")),
 ("· 100 bombetes · 6 h · 175 dies / 1000 = … kWh.",fr("… · 100 bombetes · 6 h · 175 dies","1000")+" = … kWh."),
 ("Potència en espera d'una pissarra · 30 · 18 h · 365 / 1000","Potència en espera d'una pissarra: "+fr("P · 30 · 18 h · 365","1000")),
 ("P₂ = P₁ · V₁ / V₂ · V₂ = P₁ · V₁ / P₂","P₂ = "+fr("P₁ · V₁","V₂")+" i V₂ = "+fr("P₁ · V₁","P₂")),
 ("P freda = 1,55 · T freda / T ambient","P freda = "+fr("1,55 · T freda","T ambient")),("m = c · V · V = m / c","m = c · V i V = "+fr("m","c")),
 ("Passa a kg: / 1000","Passa a kg: "+fr("…","1000")),("massa de solut / volum (en L)",fr("massa de solut","volum (en L)")),("massa pesada / 0,1 L",fr("massa pesada","0,1 L")),
 ("volum en 1 min / gotes en 1 min",fr("volum en 1 min","gotes en 1 min")),("volum en 1 min / gotes",fr("volum en 1 min","gotes")),
 ("volum gran / volum petit",fr("volum gran","volum petit")),("volum A / volum B",fr("volum A","volum B")),("volum del tub A / volum del tub B",fr("volum del tub A","volum del tub B")),
 ("… / T ambient",fr("…","T ambient")),("litres a l'any / 175",fr("litres a l'any","175")),("Litres a l'any / 175",fr("Litres a l'any","175")),
 ("36 km/h / 3,6",fr("36 km/h","3,6")),("50 km/h / 3,6",fr("50 km/h","3,6")),("18 km/h / 3,6",fr("18 km/h","3,6")),("mida a la imatge / mida real",fr("mida a la imatge","mida real")),
 ("mida al dibuix (µm) / 7,5",fr("mida al dibuix (µm)","7,5")),("mida al dibuix / augments",fr("mida al dibuix","augments")),("mida al dibuix (en µm) / mida real (µm)",fr("mida al dibuix (en µm)","mida real (µm)")),
 ("energia útil / energia consumida",fr("energia útil","energia consumida")),("camí total / 5 min",fr("camí total","5 min")),("desplaçament / 5 min",fr("desplaçament","5 min")),
 ("(canvi de v) / (canvi de t)",fr("canvi de v","canvi de t")),("(canvi de concentració) / (distància)",fr("canvi de concentració","distància")),("Δconcentració / Δdistància",fr("Δconcentració","Δdistància")),
 ("120 µm / rapidesa (µm/min)",fr("120 µm","rapidesa (µm/min)")),("120 µm / velocitat",fr("120 µm","velocitat")),("distància total / temps total",fr("distància total","temps total")),
 ("300 m / 80 s",fr("300 m","80 s")),("9,8 · 10⁻³ N entre aquesta suma","9,8 · 10⁻³ N entre aquesta suma"),
 ("(velocitat a 39 °C − velocitat a 35 °C) / (39 − 35)",fr("velocitat a 39 °C − velocitat a 35 °C","39 − 35")),("(36 − 18) · 10 · 6 · 175 / 1000",fr("(36 − 18) · 10 · 6 · 175","1000")),
 ("pressió × amplada","pressió × amplada")]
MW={"massa","volum","densitat","suma","residu","velocitat","alumnes","gotes","augments","camí","desplaçament","rapidesa","concentració","temps","distància","Δx","Δt","Δv","pendent","m","V","d","c","F","k","E","P","t","v","a","T₁","T₂","V₁","V₂","P₁","P₂"}
TOK=r'(?:\([^()]+\)|[^\s/()<>]+)'; OPER=rf'{TOK}(?: · {TOK})*'
RX=re.compile(rf'({OPER}) / ({OPER})')
def ok(x): return bool(re.search(r'[0-9…]',x)) or x.strip("().,") in MW or any(w in MW for w in re.split(r' · ',x))
FAC=re.compile(r'\((\d[\d ,]*\s?[^\s/()<>]+) / (\d[\d ,]*\s?[^\s/()<>]+)\)')
def conv(s):
    if " / " not in s and "4/3" not in s and not re.search(r'(^|: )/ ',s): return s
    for a,b in SPECIAL: s=s.replace(a,b)
    s=FAC.sub(lambda m: fr(m.group(1),m.group(2)),s)
    s=re.sub(r'(\d) (\d{3})(?!\d)',lambda m:m.group(1)+"\u00a0"+m.group(2),s)
    def rep(m):
        a,b=m.group(1),m.group(2)
        if not (ok(a) or ok(b)): return m.group(0)
        tail=""
        while b and b[-1] in ".,;:" : tail=b[-1]+tail; b=b[:-1]
        if b.endswith(" · 100"): b=b[:-6]; tail=" · 100"+tail
        return fr(a,b)+tail
    prev=None
    while prev!=s: prev=s; s=RX.sub(rep,s)
    s=re.sub(r'(^|: )/ ([0-9][0-9 ,]*[0-9]|[0-9]+)',lambda m:m.group(1)+fr("…",m.group(2)),s)
    return s
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str): return conv(o)
    return o
