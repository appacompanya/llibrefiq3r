"""Full de ruta comú a totes les SdA: 10 sessions repartides en 2 pàgines (5 per pàgina)."""
import gen_sda1 as G

EXTRA = """
@page{margin:13mm 14mm 13mm}
.list{display:grid;gap:3mm}
.c{border:1pt solid var(--ink);border-radius:3mm;padding:2.4mm 3mm;display:grid;grid-template-columns:42mm 1fr;gap:1.5mm 4mm;height:42.5mm;break-inside:avoid}
.t{grid-column:1/-1;display:flex;align-items:center;gap:2.5mm}
.t .b{width:7.5mm;height:7.5mm;border-radius:50%;background:var(--acc);color:#fff;font-weight:700;font-size:11pt;display:grid;place-items:center;flex:none}
.t h3{margin:0;font-size:12pt;flex:1;line-height:1.1}
.t .tag{font-size:9.5pt;font-weight:700;color:var(--acc);background:var(--tint);border-radius:1.4mm;padding:.5mm 2.2mm}
.t .ck{width:5.5mm;height:5.5mm;border:1.2pt solid var(--ink);border-radius:1mm;flex:none}
.im{display:flex;align-items:center;justify-content:center;height:34mm}
.im img{max-width:42mm;max-height:34mm;object-fit:contain}
.ph{width:38mm;height:30mm;border:1pt dashed #b9bec4;border-radius:2mm;display:grid;place-items:center;font-size:8.5pt;color:#8a9097;text-align:center}
.w{display:grid;grid-template-columns:1fr 1fr;gap:0 5mm;align-content:start}
.w .col{display:grid;gap:0;align-content:start}
.lb{font-size:9.5pt;font-weight:700}
.w .l{height:7mm}
.head{margin-bottom:3mm}
.q2{font-size:11pt;margin:.5mm 0 0;font-weight:400;color:var(--ink)}
.foot{display:flex;justify-content:space-between;font-size:9pt;color:var(--muted);margin-top:3mm}
.p2h{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2.2pt solid var(--acc);padding-bottom:2mm;margin-bottom:3mm}
.p2h .kick{margin:0}
"""

def build(question, sess, imgfn):
    n, title = G.SDA["n"], G.SDA["title"]
    half = (len(sess) + 1) // 2
    nl = 4 if half <= 5 else 3
    if half <= 5:
        extra = EXTRA
    elif half == 6:
        extra = EXTRA + ".c{height:37.6mm;padding:1.8mm 3mm}.im{height:27mm}.im img{max-height:27mm;max-width:38mm}.ph{height:25mm}.w .l{height:6.2mm}.t h3{font-size:11pt}"
    else:
        extra = EXTRA + (".list{gap:2.4mm}.head{margin-bottom:2mm}.c{height:32.6mm;padding:1.5mm 3mm;gap:1mm 4mm}.im{height:23mm}"
                         ".im img{max-height:23mm;max-width:36mm}.ph{height:21mm;width:34mm}.w .l{height:5.5mm}.t h3{font-size:10.5pt}"
                         ".t .b{width:6.5mm;height:6.5mm;font-size:10pt}.lb{font-size:9pt}")
    def card(k, t, tag):
        l1 = "He corregit" if k == len(sess) else "Avui he fet"
        l2 = "Com m'ha anat" if k == len(sess) - 1 else "He après"
        src = imgfn(k)
        pic = f'<img src="{src}" alt="">' if src else '<div class="ph">Il·lustració<br>pendent</div>'
        return (f'<div class="c"><div class="t"><span class="b">{k}</span><h3>{t}</h3><span class="tag">{tag}</span><span class="ck"></span></div>'
                f'<div class="im">{pic}</div><div class="w"><div class="col"><div class="lb">{l1}</div>{G.lines(nl)}</div>'
                f'<div class="col"><div class="lb">{l2}</div>{G.lines(nl)}</div></div></div>')
    p1 = "".join(card(*s) for s in sess[:half])
    p2 = "".join(card(*s) for s in sess[half:])
    body = (f'<div class="head"><div><div class="kick">Física i química · 3r ESO · SdA {n} · Full de ruta</div><h1>{title}</h1>'
            f'<p class="q2">{question}</p></div><div class="who"><span>Nom <i></i></span><span>Grup <i></i></span></div></div>'
            f'<div class="list">{p1}</div>'
            f'<div class="pb"></div><div class="p2h"><div class="kick">SdA {n} · {title} · Full de ruta (continuació)</div></div>'
            f'<div class="list">{p2}</div><div class="foot"><span>Marca la casella quan acabis cada sessió.</span><span>L\'etiqueta de color t\'indica què has de lliurar o fer a casa.</span></div>')
    return G.page(body, extra), True
