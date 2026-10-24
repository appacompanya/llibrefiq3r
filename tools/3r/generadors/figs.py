"""Suports visuals afegits als fulls de l'alumnat (etiquetes, pictogrames i esquemes de muntatge)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
import sys; sys.path.insert(0, os.path.join(ROOT, "..", "lib"))
import imatges as IM  # una sola còpia de cada imatge, a img/ de l'arrel
IMG = lambda n: IM.uri(n)
GHS = lambda c: IM.uri(f"ghs/ghs{c:02d}.png")

T = 'font-family="AH,Verdana,sans-serif" fill="#1f2328"'
INK = "#1f2328"
GLASS = "#5d646d"
WATER = "#cfe6f7"


def fig(svg, caption, width="120mm"):
    return (f'<figure style="margin:2mm auto 3mm;text-align:center;break-inside:avoid">'
            f'<div style="width:{width};max-width:100%;margin:0 auto">{svg}</div>'
            f'<figcaption style="font-size:8.5pt;color:#5d646d;margin-top:1mm">{caption}</figcaption></figure>')


# ---------- SdA 2 · etiqueta de l'esprai ----------
def etiqueta_esprai():
    p = ("Manteniu-lo lluny de la calor, de les superfícies calentes, de les espurnes, de les flames obertes i de qualsevol altra font d'ignició. No fumeu.",
         "No el ruixeu sobre una flama oberta ni sobre cap altra font d'ignició.",
         "No el perforeu ni el cremeu, ni tan sols quan ja s'hagi acabat.",
         "Protegiu-lo de la llum del sol. No l'exposeu a temperatures superiors a 50 °C.",
         "Manteniu-lo fora de l'abast dels infants.")
    li = "".join(f"<li style='margin:0 0 .6mm'>{x}</li>" for x in p)
    return (
        '<div style="display:flex;gap:4mm;align-items:center;justify-content:center;margin:2mm 0 3mm;break-inside:avoid">'
        f'<img src="{IMG("sda2-esprai.jpg")}" alt="Esprai desodorant" style="width:22mm;height:auto">'
        '<div style="border:1.2pt solid #1f2328;border-radius:2mm;padding:2.5mm 3.5mm;max-width:128mm;font-size:8.6pt;line-height:1.3;background:#fff;text-align:left">'
        '<div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:.8pt solid #b9bec4;padding-bottom:1mm;margin-bottom:1.5mm">'
        '<b style="font-size:11pt;letter-spacing:.04em">FRESC 48 h</b><span>Desodorant en esprai · 200 mL</span></div>'
        f'<div style="display:flex;gap:3mm;align-items:center;margin-bottom:1.2mm"><img src="{GHS(2)}" alt="Pictograma de perill" style="width:15mm;height:15mm">'
        '<div><b style="font-size:10.5pt">PERILL</b><br>Aerosol extremadament inflamable.<br>Recipient a pressió: pot rebentar si s\'escalfa.</div></div>'
        f'<ul style="margin:0 0 1.2mm;padding-left:4.5mm">{li}</ul>'
        '<div style="color:#5d646d">Composició: butà, isobutà i propà (gasos propel·lents), alcohol, perfum.</div>'
        '</div></div>'
        '<p class="small" style="text-align:center;margin-top:-1mm">Etiqueta de l\'esprai (marca inventada; avisos reals del Reglament CLP de la UE)</p>')


# ---------- SdA 1 · pictogrames ----------
def picto(*codes, size="13mm"):
    return "".join(f'<img src="{GHS(c)}" alt="Pictograma GHS{c:02d}" style="width:{size};height:{size};vertical-align:middle;margin:0 1mm 0 0">' for c in codes)


def picto_ref():
    cells = "".join(
        f'<div style="text-align:center"><img src="{GHS(c)}" alt="GHS{c:02d}" style="width:15mm;height:15mm;display:block;margin:0 auto"><span style="font-size:8pt;color:#5d646d">GHS{c:02d}</span></div>'
        for c in range(1, 10))
    return ('<div style="display:grid;grid-template-columns:repeat(9,1fr);gap:1.5mm;margin:1.5mm 0 3mm;break-inside:avoid">' + cells + '</div>')


GHS_INFO = [
    (1, "Explosiu", "Pot explotar per la calor, un cop o el fregament.", "Lluny de la calor; no el colpegis."),
    (2, "Inflamable", "S'encén molt fàcilment (líquid, gas o aerosol).", "Lluny de flames, espurnes i fonts de calor."),
    (3, "Comburent", "Aporta oxigen i fa que altres materials cremin més.", "Lluny de combustibles (paper, fusta, alcohol)."),
    (4, "Gas a pressió", "Recipient amb gas comprimit: pot rebentar si s'escalfa.", "No l'escalfis ni el perforis."),
    (5, "Corrosiu", "Crema la pell i els ulls i ataca els metalls.", "Guants i ulleres; si toca la pell, molta aigua."),
    (6, "Toxicitat aguda", "Pot ser mortal en quantitats petites.", "No l'ingereixis ni l'inhalis; guants."),
    (7, "Nociu o irritant", "Irrita la pell, els ulls o les vies respiratòries; nociu si s'ingereix.", "Guants i ulleres; ventila l'espai."),
    (8, "Perill greu per a la salut", "Danys a llarg termini (càncer, òrgans, al·lèrgies respiratòries).", "Evita'n el contacte i la inhalació."),
    (9, "Perillós per al medi ambient", "Tòxic per als organismes aquàtics.", "No el llencis a l'aigüera: als residus."),
]


def picto_table(cols=3, size="12mm"):
    """Taula de referència dels nou pictogrames de perill (Reglament CLP)."""
    cells = "".join(
        f'<div style="display:flex;gap:2mm;align-items:flex-start;border:0.6pt solid #d8dde3;border-radius:2mm;padding:1.4mm;break-inside:avoid">'
        f'<img src="{GHS(c)}" alt="Pictograma GHS{c:02d}" style="width:{size};height:{size};flex:none">'
        f'<div style="font-size:8pt;line-height:1.25"><b>GHS{c:02d} · {n}</b><br>{m}<br><i>{pr}</i></div></div>'
        for c, n, m, pr in GHS_INFO)
    return (f'<div class="tip" style="padding:2mm 2.5mm"><b>Els pictogrames de perill</b> (Reglament CLP de la UE). Són rombes vermells amb un símbol negre. Cada producte perillós els porta a l\'etiqueta, amb una paraula d\'avís (<b>Perill</b> o <b>Atenció</b>).'
            f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:1.6mm;margin-top:1.6mm">{cells}</div></div>')


# ---------- SdA 1 · muntatge de conductivitat ----------
def circuit_conductivitat():
    s = f'''<svg viewBox="0 0 320 175" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
<g fill="none" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round">
<path d="M131 72 V54 H40 V22 H96"/><path d="M104 22 H202"/><path d="M218 22 H280 V54 H169 V72"/>
<line x1="104" y1="10" x2="104" y2="34" stroke-width="2"/><line x1="96" y1="15" x2="96" y2="29" stroke-width="4"/>
<path d="M202 13 L218 22 L202 31 Z" fill="#ffe08a"/><line x1="218" y1="13" x2="218" y2="31" stroke-width="2"/>
<path d="M212 9 l7 -7 m-4 0 h4 v4 M220 12 l7 -7 m-4 0 h4 v4" stroke-width="1.1"/>
</g>
<path d="M100 92 V162 Q100 168 106 168 H194 Q200 168 200 162 V92" fill="none" stroke="{GLASS}" stroke-width="1.6"/>
<path d="M101.5 110 H198.5 V162 Q198.5 166.5 194 166.5 H106 Q101.5 166.5 101.5 162 Z" fill="{WATER}"/>
<rect x="127" y="66" width="8" height="84" rx="1.5" fill="#3c3f44"/><rect x="165" y="66" width="8" height="84" rx="1.5" fill="#3c3f44"/>
<g {T} font-size="9.5">
<text x="100" y="45" text-anchor="middle">pila de 9 V</text><text x="88" y="12" font-size="10" font-weight="700">−</text><text x="108" y="12" font-size="10" font-weight="700">+</text>
<text x="210" y="45" text-anchor="middle">LED</text>
<text x="208" y="96">elèctrodes de grafit</text><path d="M206 93 H176" stroke="{GLASS}" stroke-width=".8"/>
<text x="208" y="107" font-size="8.5" fill="#5d646d">(no es toquen)</text>
<text x="150" y="158" text-anchor="middle" fill="#2f5d86">líquid del pot</text>
</g></svg>'''
    return fig(s, "Comprovador de conductivitat: si el líquid condueix, el circuit es tanca i el LED s\'encén", "105mm")


# ---------- SdA 1 · cromatografia ----------
def cromatografia():
    cm = 12  # 1 cm = 12 px
    bot = 170
    water = bot - cm          # 1 cm d'aigua
    strip_b = bot - 6         # la tira entra 0,5 cm a l'aigua
    spot = strip_b - int(1.5 * cm)
    s = f'''<svg viewBox="0 0 330 190" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
<path d="M90 45 V{bot-6} Q90 {bot} 96 {bot} H174 Q180 {bot} 180 {bot-6} V45" fill="none" stroke="{GLASS}" stroke-width="1.6"/>
<path d="M91.5 {water} H178.5 V{bot-6} Q178.5 {bot-1.5} 174 {bot-1.5} H96 Q91.5 {bot-1.5} 91.5 {bot-6} Z" fill="{WATER}"/>
<rect x="70" y="36" width="130" height="7" rx="3.5" fill="#e9b949" stroke="{INK}" stroke-width="1"/>
<path d="M200 36 l14 3.5 l-14 3.5 Z" fill="#f3d9a4" stroke="{INK}" stroke-width="1"/>
<rect x="124" y="40" width="22" height="{strip_b-40}" fill="#fff" stroke="{INK}" stroke-width="1.1"/>
<path d="M124 52 q11 4 22 0" fill="none" stroke="{INK}" stroke-width="1"/>
<circle cx="135" cy="{spot}" r="4" fill="#1f2328"/>
<line x1="119" y1="{spot}" x2="151" y2="{spot}" stroke="{GLASS}" stroke-width=".7" stroke-dasharray="2 2"/>
<g stroke="{INK}" stroke-width=".9" fill="none">
<path d="M196 {spot} V{strip_b}"/><path d="M193 {spot} H199 M193 {strip_b} H199"/>
<path d="M60 {water} V{bot}"/><path d="M57 {water} H63 M57 {bot} H63"/>
</g>
<g {T} font-size="9.5">
<text x="205" y="{(spot+strip_b)//2+3}">1,5 cm</text>
<text x="56" y="{(water+bot)//2+3}" text-anchor="end">1 cm d'aigua</text>
<text x="222" y="42">llapis (subjecta la tira)</text>
<text x="222" y="90">tira de paper de filtre</text><path d="M220 87 H148" stroke="{GLASS}" stroke-width=".8"/>
<text x="222" y="{spot-14}">taca de tinta</text><path d="M220 {spot-17} L141 {spot-3}" stroke="{GLASS}" stroke-width=".8"/>
<text x="222" y="{spot-3}" font-size="8.5" fill="#5d646d">(per sobre de l'aigua)</text>
</g></svg>'''
    return fig(s, "Muntatge de la cromatografia en paper (esquema a escala aproximada)", "100mm")


# ---------- SdA 2 · globus sobre l'aigua calenta ----------
def globus_calent():
    s = f'''<svg viewBox="0 0 330 215" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
<rect x="70" y="182" width="150" height="18" rx="3" fill="#8b9096" stroke="{INK}" stroke-width="1.2"/>
<rect x="95" y="177" width="100" height="6" fill="#5d646d"/>
<circle cx="205" cy="191" r="5" fill="#3c3f44"/>
<path d="M100 92 L96 86 M100 92 V171 Q100 177 106 177 H184 Q190 177 190 171 V92" fill="none" stroke="{GLASS}" stroke-width="1.6"/>
<path d="M101.5 100 H188.5 V171 Q188.5 175.5 184 175.5 H106 Q101.5 175.5 101.5 171 Z" fill="#f6c9b5"/>
<g stroke="#e0782f" stroke-width="1" fill="none" opacity=".7"><path d="M120 165 q4 -6 0 -12 q-4 -6 0 -12"/><path d="M145 165 q4 -6 0 -12 q-4 -6 0 -12"/><path d="M170 165 q4 -6 0 -12 q-4 -6 0 -12"/></g>
<ellipse cx="145" cy="58" rx="44" ry="47" fill="#e5533d" stroke="{INK}" stroke-width="1.3"/>
<ellipse cx="130" cy="38" rx="9" ry="13" fill="#fff" opacity=".35"/>
<path d="M141 13 l4 -6 l4 6 Z" fill="#c2412f" stroke="{INK}" stroke-width="1"/>
<ellipse cx="145" cy="58" rx="47" ry="9" fill="none" stroke="#1f2328" stroke-width="1" stroke-dasharray="3 2.5"/>
<line x1="230" y1="20" x2="230" y2="182" stroke="#8b9096" stroke-width="4"/>
<rect x="182" y="84" width="52" height="6" rx="2" fill="#8b9096"/>
<rect x="178" y="80" width="5" height="88" rx="2.5" fill="#fff" stroke="{INK}" stroke-width="1"/>
<circle cx="180.5" cy="168" r="4" fill="#e5533d" stroke="{INK}" stroke-width="1"/>
<g {T} font-size="9.5">
<text x="246" y="62">perímetre a la zona</text><text x="246" y="73">més ampla</text><path d="M244 62 H193" stroke="{GLASS}" stroke-width=".8"/>
<text x="246" y="125">termòmetre</text><path d="M244 122 H184" stroke="{GLASS}" stroke-width=".8"/>
<text x="10" y="140">aigua calenta</text><text x="10" y="151">(≈ 70 °C)</text><path d="M58 143 H106" stroke="{GLASS}" stroke-width=".8"/>
<text x="232" y="196">placa calefactora</text><path d="M230 192 H221" stroke="{GLASS}" stroke-width=".8"/>
<text x="10" y="100">el globus toca</text><text x="10" y="111">l'aigua</text><path d="M48 103 L118 101" stroke="{GLASS}" stroke-width=".8"/>
</g></svg>'''
    return fig(s, "Globus damunt del vas de precipitats de 600 mL amb aigua calenta", "100mm")


# ---------- SdA 4 · sistema tancat ----------
def sistema_tancat():
    s = f'''<svg viewBox="0 0 330 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
<rect x="60" y="188" width="150" height="24" rx="4" fill="#c8ccd1" stroke="{INK}" stroke-width="1.2"/>
<rect x="85" y="194" width="62" height="12" rx="2" fill="#5d646d"/><circle cx="170" cy="200" r="4" fill="#8b9096"/><circle cx="188" cy="200" r="4" fill="#8b9096"/>
<rect x="70" y="182" width="130" height="7" rx="2" fill="#aeb3b9" stroke="{INK}" stroke-width="1"/>
<path d="M120 30 V48 Q100 56 100 78 V176 Q100 182 106 182 H164 Q170 182 170 176 V78 Q170 56 150 48 V30 Z" fill="#eef6fb" stroke="{GLASS}" stroke-width="1.5"/>
<rect x="116" y="16" width="38" height="16" rx="2" fill="#4a7bb0" stroke="{INK}" stroke-width="1.1"/>
<g stroke="#2f5d86" stroke-width="1"><line x1="122" y1="18" x2="122" y2="30"/><line x1="129" y1="18" x2="129" y2="30"/><line x1="136" y1="18" x2="136" y2="30"/><line x1="143" y1="18" x2="143" y2="30"/><line x1="150" y1="18" x2="150" y2="30"/></g>
<path d="M101.5 172 H168.5 V176 Q168.5 180.5 164 180.5 H106 Q101.5 180.5 101.5 176 Z" fill="#f0dca0"/>
<g transform="rotate(-9 136 130)">
<path d="M128 92 V164 Q128 172 136 172 Q144 172 144 164 V92" fill="#fff" stroke="{INK}" stroke-width="1.2"/>
<path d="M129.2 150 H142.8 V164 Q142.8 170.8 136 170.8 Q129.2 170.8 129.2 164 Z" fill="#f4f4f4" stroke="#aaa" stroke-width=".6"/>
</g>
<g {T} font-size="9.5">
<text x="182" y="27">tap de rosca</text><path d="M180 24 H156" stroke="{GLASS}" stroke-width=".8"/>
<text x="182" y="110">ampolla de plàstic de 500 mL</text><path d="M180 107 H170" stroke="{GLASS}" stroke-width=".8"/>
<text x="182" y="145">tub d'assaig dret amb el</text><text x="182" y="156">bicarbonat (≈ 1 g)</text><path d="M180 148 L143 156" stroke="{GLASS}" stroke-width=".8"/>
<text x="10" y="168">20 mL de vinagre</text><path d="M88 170 L106 176" stroke="{GLASS}" stroke-width=".8"/>
<text x="218" y="203">balança digital</text>
</g></svg>'''
    return fig(s, "Sistema tancat: el bicarbonat no toca el vinagre fins que inclinem l'ampolla tapada", "100mm")


# ---------- SdA 4 · obtenim hidrogen ----------
def tub_hidrogen():
    tube = lambda x, y, h, inv=False: (f'<path d="M{x} {y} V{y+h-8} Q{x} {y+h} {x+8} {y+h} Q{x+16} {y+h} {x+16} {y+h-8} V{y}" fill="#fff" stroke="{INK}" stroke-width="1.2"/>' if not inv else
                                       f'<path d="M{x} {y+h} V{y+8} Q{x} {y} {x+8} {y} Q{x+16} {y} {x+16} {y+8} V{y+h}" fill="#fff" stroke="{INK}" stroke-width="1.2"/>')
    s = f'''<svg viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
<rect x="40" y="150" width="90" height="8" fill="#c8ccd1" stroke="{INK}" stroke-width="1"/>
{tube(77, 98, 92)}
<path d="M78.2 150 H91.8 V182 Q91.8 188.8 85 188.8 Q78.2 188.8 78.2 182 Z" fill="{WATER}"/>
<rect x="81" y="170" width="2.5" height="14" fill="#9aa1a8" transform="rotate(15 82 177)"/>
<g fill="#fff" stroke="#2f5d86" stroke-width=".7"><circle cx="86" cy="165" r="1.6"/><circle cx="83" cy="158" r="1.3"/><circle cx="88" cy="153" r="1.2"/></g>
<g transform="rotate(-7 85 96)">{tube(77, 14, 82, inv=True)}</g>
<g {T} font-size="9.5">
<text x="104" y="45">tub sec boca avall</text><text x="104" y="56">(recull l'hidrogen)</text><path d="M102 48 H95" stroke="{GLASS}" stroke-width=".8"/>
<text x="104" y="176">10 mL d'HCl 1 M</text><text x="104" y="187">+ 2 cm de magnesi</text><path d="M102 177 H93" stroke="{GLASS}" stroke-width=".8"/>
<text x="85" y="12" text-anchor="middle" font-weight="700">1</text><text x="255" y="12" text-anchor="middle" font-weight="700">2</text>
</g>
<line x1="185" y1="10" x2="185" y2="195" stroke="#d6d9dd" stroke-width="1" stroke-dasharray="3 3"/>
{tube(247, 30, 82, inv=True)}
<path d="M255 135 q-9 -12 -2 -22 q2 8 7 3 q3 10 -5 19 Z" fill="#f0a24a" stroke="#c2412f" stroke-width="1"/>
<rect x="249" y="135" width="12" height="40" rx="2" fill="#8b9096"/>
<g {T} font-size="9.5">
<text x="270" y="70">sense girar-lo,</text><text x="270" y="81">a la flama</text>
<text x="270" y="140">flama (la sosté</text><text x="270" y="151">el professor)</text>
</g></svg>'''
    return fig(s, "1) Recollim el gas en un tub boca avall. 2) Apropem el tub, sense girar-lo, a la flama.", "105mm")


# ---------- SdA 6 · etiqueta del carregador ----------
def etiqueta_carregador():
    return ('<div style="display:flex;justify-content:center;margin:1.5mm 0 3mm;break-inside:avoid"><div style="background:#2b2e33;color:#e8eaed;border-radius:3mm;padding:3mm 4.5mm;font-size:8.6pt;line-height:1.45;font-family:Verdana,sans-serif;min-width:95mm">'
            '<div style="font-weight:700;letter-spacing:.05em;margin-bottom:1mm">AC ADAPTER · ADAPTADOR DE CORRENT · 65 W</div>'
            '<div>INPUT (entrada): 100–240 V ~ 50–60 Hz 1,5 A</div>'
            '<div><b>OUTPUT (sortida): 20 V ⎓ 3,25 A</b> · 15 V ⎓ 3 A · 5 V ⎓ 3 A</div>'
            '<div style="color:#9aa1a8;font-size:7.6pt;margin-top:1mm">~ corrent altern · ⎓ corrent continu</div></div></div>'
            '<p class="small" style="text-align:center;margin-top:-1.5mm">Exemple d\'etiqueta d\'un carregador de portàtil</p>')
