"""Genera el formulari (1 pàgina) i el glossari del curs (alumnat)."""
import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..", "lib"))
import imatges as IM
import os, sys
import gen_curs as GC
from gen_sda1 import page
from playwright.sync_api import sync_playwright

OUT = GC.OUT
COL = {1: "#2F8F95", 2: "#E0782F", 3: "#6C5CC9", 4: "#3F9A5A", 5: "#D14B66", 6: "#2F6DB5"}
TIT = {1: "Detectius de la matèria", 2: "El desodorant kamikaze", 3: "Què hi ha dins del meu mòbil?", 4: "Un cotxe que només allibera aigua?", 5: "Cèl·lules a la caça dels patògens", 6: "L'energia del nostre institut"}

F = {
    1: [(r"d = \dfrac{m}{V}", "densitat (g/cm³, kg/m³)"), (r"1\ \mathrm{mL} = 1\ \mathrm{cm^3}", "volum"), (r"1\ \mathrm{dm^3} = 1\ \mathrm{L}", "volum"), (r"1\ \mathrm{m^3} = 1000\ \mathrm{L}", "volum"), (r"a\cdot10^{n},\ 1 \le a < 10", "notació científica"),
        (r"E_a = |x - x_{\mathrm{ref}}|", "error absolut"), (r"E_r = \dfrac{E_a}{x_{\mathrm{ref}}}\cdot100", "error relatiu (%)"), (r"c = \dfrac{m_{\mathrm{solut}}}{V_{\mathrm{dissolució}}}", "concentració (g/L)")],
    2: [(r"p_1\,V_1 = p_2\,V_2", "Boyle-Mariotte (T constant)"), (r"\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}", "Charles (p constant)"), (r"\dfrac{p_1}{T_1} = \dfrac{p_2}{T_2}", "Gay-Lussac (V constant)"),
        (r"T\,(\mathrm{K}) = T\,(^{\circ}\mathrm{C}) + 273", "escala absoluta"), (r"V = \tfrac{4}{3}\,\pi\,r^{3}", "volum de l'esfera"), (r"P = 2\,\pi\,r", "perímetre")],
    3: [(r"A = Z + N", "nombre màssic"), (r"e^{-} = Z - q", "electrons d'un ió de càrrega q"), (r"\mathrm{Li \rightarrow Li^{+} + e^{-}}", "oxidació a la bateria")],
    4: [(r"\textstyle\sum m_{\mathrm{reactius}} = \sum m_{\mathrm{productes}}", "conservació de la massa"), (r"\dfrac{m_A}{m_B} = \text{constant}", "proporcions definides"), (r"M = \textstyle\sum m_{\text{atòmiques}}", "massa molecular (u)"), (r"V = \pi\,r^{2}\,h", "volum d'un cilindre")],
    5: [(r"v = \dfrac{\Delta x}{\Delta t}", "velocitat"), (r"x = x_0 + v\,t", "MRU"), (r"a = \dfrac{\Delta v}{\Delta t}", "acceleració"), (r"v = v_0 + a\,t", "MRUA"),
        (r"x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^{2}", "MRUA"), (r"F = m\,a", "2a llei de Newton"), (r"P = m\,g,\ g = 9{,}8\ \mathrm{m/s^2}", "pes"), (r"F = k\,\Delta x", "llei de Hooke"), (r"\mathrm{km/h} \div 3{,}6 = \mathrm{m/s}", "canvi d'unitats")],
    6: [(r"E = P\,t", "energia consumida"), (r"1\ \mathrm{kWh} = 3{,}6\cdot10^{6}\ \mathrm{J}", "kilowatt hora"), (r"\eta = \dfrac{E_{\text{útil}}}{E_{\text{consumida}}}\cdot100", "rendiment (%)"),
        (r"P = V\,I", "potència elèctrica"), (r"\text{cost} = E\,(\mathrm{kWh})\cdot\text{preu}", "cost")],
}

def formulari():
    b = GC.head("Formulari del curs", intro="El pots fer servir a classe, a casa i a les activitats de demostració d\x27assoliment. Recorda: escriu sempre les dades, la fórmula, el càlcul i el resultat amb unitats.")
    b += "<div class='grid'>"
    for n in range(1, 7):
        rows = "".join(f"<tr><td class='f'>\\({f}\\)</td><td class='d'>{d}</td></tr>" for f, d in F[n])
        b += f"<div class='card' style='--c:{COL[n]}'><div class='ct'>SdA {n} · {TIT[n]}</div><table>{rows}</table></div>"
    b += "</div>"
    b += "<p class='small' style='margin-top:2mm'><b>Prefixos:</b> giga, G = 10⁹ · mega, M = 10⁶ · quilo, k = 10³ · hecto, h = 10² · deca, da = 10 · deci, d = 10⁻¹ · centi, c = 10⁻² · mil·li, m = 10⁻³ · micro, µ = 10⁻⁶ · nano, n = 10⁻⁹</p>"
    css = ("@page{size:A4;margin:11mm 14mm 11mm}.grid{display:grid;grid-template-columns:1fr 1fr;gap:3mm}.card{border:1.4pt solid var(--c);border-radius:2.5mm;padding:2mm 3mm;break-inside:avoid}"
           ".ct{font-weight:700;color:var(--c);font-size:10.5pt;margin-bottom:1mm}.card table{margin:0;font-size:9.5pt}.card td{border:none;border-bottom:.5pt solid #e3e6ea;padding:1mm 1mm}.card td.f{width:60%}.card td.d{color:#5d646d;font-size:9pt}")
    return page(b, css), True

G = {
    1: [("magnitud", "propietat d'un cos, una substància o un fenomen que es pot mesurar i expressar amb un nombre i una unitat", "(physical) quantity"),
        ("unitat de mesura", "valor d'una magnitud, fixat per convenció, amb què es comparen els altres de la mateixa magnitud", "unit of measurement"),
        ("densitat", "massa per unitat de volum d'una substància (kg/m³, g/cm³)", "density"),
        ("notació científica", "manera d'escriure un nombre com a·10ⁿ, amb 1 ≤ a < 10", "scientific notation"),
        ("error relatiu", "quocient entre l'error absolut i el valor de referència; sovint s'expressa en %", "relative error"),
        ("substància pura", "matèria amb una composició fixa i unes propietats característiques (densitat, punt de fusió…)", "pure substance"),
        ("mescla", "matèria formada per dues o més substàncies que conserven les seves propietats", "mixture"),
        ("dissolució", "mescla homogènia d'un o més soluts en un dissolvent", "solution"),
        ("decantació", "separació, per diferència de densitat, de dos líquids no miscibles o d'un sòlid sedimentat i un líquid", "decantation"),
        ("filtració", "separació d'un sòlid insoluble d'un líquid fent-los passar per un filtre", "filtration"),
        ("cromatografia", "separació dels components d'una mescla perquè un dissolvent els arrossega a velocitats diferents per un suport", "chromatography"),
        ("pictograma de perill", "símbol normalitzat que indica el perill d'un producte químic", "hazard pictogram")],
    2: [("partícula", "component molt petit de la matèria (àtom, molècula o ió) que es mou constantment", "particle"),
        ("pressió", "força perpendicular per unitat de superfície (Pa); en un gas, la causen els xocs de les partícules", "pressure"),
        ("temperatura", "magnitud relacionada amb l'energia cinètica mitjana de les partícules", "temperature"),
        ("kelvin", "unitat de temperatura del SI; 0 K = −273,15 °C (zero absolut)", "kelvin"),
        ("estat d'agregació", "forma en què es presenta la matèria: sòlid, líquid o gas", "state of matter"),
        ("punt de fusió", "temperatura a què una substància pura passa de sòlid a líquid, a una pressió determinada", "melting point"),
        ("punt d'ebullició", "temperatura a què una substància pura bull, a una pressió determinada", "boiling point"),
        ("vaporització", "pas de líquid a gas: per evaporació (a la superfície) o per ebullició (a tot el líquid)", "vaporisation"),
        ("condensació", "pas de gas a líquid", "condensation"),
        ("corba d'escalfament", "gràfica temperatura–temps d'una substància que s'escalfa", "heating curve")],
    3: [("àtom", "partícula formada per un nucli (protons i neutrons) i electrons; unitat més petita d'un element químic", "atom"),
        ("protó", "partícula del nucli amb càrrega positiva", "proton"),
        ("neutró", "partícula del nucli sense càrrega", "neutron"),
        ("electró", "partícula amb càrrega negativa que es mou al voltant del nucli", "electron"),
        ("nombre atòmic (Z)", "nombre de protons del nucli; identifica l'element", "atomic number"),
        ("isòtops", "àtoms d'un mateix element (igual Z) amb un nombre diferent de neutrons", "isotopes"),
        ("ió", "àtom o grup d'àtoms amb càrrega perquè ha guanyat o perdut electrons", "ion"),
        ("grup", "columna de la taula periòdica", "group"),
        ("període", "fila de la taula periòdica", "period"),
        ("enllaç químic", "unió entre àtoms (iònic, covalent o metàl·lic)", "chemical bond"),
        ("matèria primera crítica", "matèria primera de gran importància econòmica amb un risc alt de problemes de subministrament (llista de la UE)", "critical raw material")],
    4: [("reacció química", "procés en què unes substàncies (reactius) es transformen en unes altres (productes)", "chemical reaction"),
        ("reactiu", "substància que es consumeix en una reacció", "reactant"),
        ("producte", "substància que es forma en una reacció", "product"),
        ("equació química", "representació d'una reacció amb fórmules i coeficients", "chemical equation"),
        ("coeficient estequiomètric", "nombre davant d'una fórmula que ajusta l'equació", "stoichiometric coefficient"),
        ("sistema tancat", "sistema que intercanvia energia però no matèria amb l'entorn", "closed system"),
        ("reacció exotèrmica", "reacció que allibera energia a l'entorn", "exothermic reaction"),
        ("reacció endotèrmica", "reacció que absorbeix energia de l'entorn", "endothermic reaction"),
        ("electròlisi", "descomposició d'una substància amb corrent elèctric", "electrolysis"),
        ("combustió", "reacció ràpida d'un combustible amb oxigen que allibera energia", "combustion"),
        ("velocitat de reacció", "rapidesa amb què es consumeixen els reactius o es formen els productes", "rate of reaction")],
    5: [("posició", "lloc on és un cos respecte d'un origen", "position"),
        ("desplaçament", "canvi de posició entre dos instants (en línia recta, amb sentit)", "displacement"),
        ("trajectòria", "línia que descriu un cos en moure's", "trajectory, path"),
        ("velocitat", "desplaçament per unitat de temps (m/s)", "velocity"),
        ("acceleració", "variació de la velocitat per unitat de temps (m/s²)", "acceleration"),
        ("MRU / MRUA", "moviment rectilini uniforme / moviment rectilini uniformement accelerat", "uniform linear motion / uniformly accelerated linear motion"),
        ("força", "interacció que pot canviar l'estat de moviment d'un cos o deformar-lo (N)", "force"),
        ("inèrcia", "tendència d'un cos a mantenir el seu estat de repòs o de moviment", "inertia"),
        ("constant elàstica", "força per unitat d'allargament d'una molla (N/m)", "spring constant"),
        ("gradient", "variació d'una magnitud d'un punt a un altre de l'espai", "gradient"),
        ("quimiotaxi", "moviment d'una cèl·lula orientat per un gradient de concentració d'una substància", "chemotaxis")],
    6: [("energia", "capacitat d'un sistema de produir canvis (J, kWh)", "energy"),
        ("potència", "energia transformada per unitat de temps (W)", "power"),
        ("quilowatt hora", "energia que transforma un aparell d'1 kW en 1 h (1 kWh = 3,6·10⁶ J)", "kilowatt-hour"),
        ("rendiment", "percentatge de l'energia consumida que es converteix en energia útil", "efficiency"),
        ("consum en espera", "energia que consumeix un aparell apagat o en espera però endollat (consum fantasma)", "standby power consumption"),
        ("circuit en sèrie", "aparells connectats un darrere l'altre, pels quals passa el mateix corrent", "series circuit"),
        ("circuit en paral·lel", "aparells connectats a la mateixa tensió, de manera independent", "parallel circuit"),
        ("alternador", "generador que transforma energia cinètica de rotació en energia elèctrica de corrent altern", "alternator"),
        ("font d'energia renovable", "font d'energia que es regenera de manera natural i no s'esgota a escala humana", "renewable energy source"),
        ("matriu energètica", "combinació de fonts d'energia que fa servir un territori; en electricitat, el percentatge de cada font en la generació", "energy mix")],
}

def glossari():
    b = GC.head("Glossari del curs", intro="Paraules clau de cada SdA. A l'última columna pots afegir-hi les teves anotacions: un exemple, un dibuix, la traducció o allò que t'ajudi a recordar-la.")
    for n in range(1, 7):
        rows = "".join(f"<tr><td><b>{w}</b></td><td>{d}</td><td><i>{e}</i></td><td></td></tr>" for w, d, e in G[n])
        b += (f"<h2 style='color:{COL[n]}'><span class='k' style='background:{COL[n]}'>{n}</span> {TIT[n]}</h2>"
              f"<table><tr><th style='width:20%'>Paraula</th><th>Definició</th><th style='width:20%'>English</th><th style='width:16%'>Anotacions de l'estudiant</th></tr>{rows}</table>")
    css = "@page{size:A4;margin:13mm 14mm 13mm}table{font-size:8.6pt;line-height:1.25}th,td{padding:.7mm 1.5mm}h2{font-size:11.5pt;margin:2.4mm 0 .8mm}"
    return page(b, css), True

DOCS = [("curs-04-formulari.pdf", formulari), ("curs-05-glossari.pdf", glossari)]

if __name__ == "__main__":
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for fn, f in DOCS:
            html, _ = f()
            path = os.path.join(OUT, fn.replace(".pdf", ".html")); open(path, "w", encoding="utf-8").write(html)
            pg.goto("file://" + path); pg.wait_for_function('document.body.dataset.math==="ok"', timeout=8000); pg.wait_for_timeout(300)
            pg.pdf(path=os.path.join(OUT, fn), format="A4", print_background=True, prefer_css_page_size=True, display_header_footer=True, header_template="<div></div>", footer_template=GC.FOOT)
            os.remove(path); print("ok", fn)
        br.close()
