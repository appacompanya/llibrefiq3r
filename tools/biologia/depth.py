"""Text afegit a cada secció perquè el dossier sigui un llibre, no un resum."""
from __future__ import annotations

import re

from amplia import MORE

# Inserit just després del títol de la secció.
EXTRA = {}

EXTRA["cel-s2"] = """
<h4>Procariota i eucariota, costat a costat</h4>
<table><thead><tr><th></th><th>Procariota</th><th>Eucariota</th></tr></thead><tbody>
<tr><td>Nucli</td><td>no: DNA al nucleoide</td><td>sí, amb embolcall i porus</td></tr>
<tr><td>DNA</td><td>circular, un cromosoma principal</td><td>lineal, diversos cromosomes, amb histones</td></tr>
<tr><td>Orgànuls amb membrana</td><td>no</td><td>sí (mitocondri, reticle, Golgi…)</td></tr>
<tr><td>Ribosomes</td><td>70S</td><td>80S al citosol; 70S a mitocondris i cloroplasts</td></tr>
<tr><td>Paret</td><td>peptidoglicà (bacteris); sense, en arqueus</td><td>cel·lulosa, quitina o cap (animals)</td></tr>
<tr><td>Divisió</td><td>bipartició</td><td>mitosi; meiosi per als gàmetes</td></tr>
</tbody></table>
<p>Un bacteri de 2 µm i una cèl·lula hepàtica de 20 µm no es diferencien només per la mida. La cèl·lula eucariota compartimenta: la cadena respiratòria no neda pel citosol, és a la membrana interna del mitocondri. Per això les preguntes de la PAU que demanen «on» són preguntes de biologia cel·lular, no un detall opcional.</p>
<div class="box ex"><div class="lead">Exemple resolt</div><p>Una cèl·lula té DNA circular, ribosomes 70S i paret sense peptidoglicà. És un bacteri?</p><p>No necessàriament. Encaixa amb un arqueu: procariota, però sense peptidoglicà. Un bacteri típic sí que en porta. Els mitocondris també tenen DNA circular i ribosomes 70S, però no són cèl·lules lliures ni tenen paret.</p></div>
"""

EXTRA["cel-s5"] = """
<h4>Cèl·lula animal i cèl·lula vegetal</h4>
<table><thead><tr><th></th><th>Animal</th><th>Vegetal</th></tr></thead><tbody>
<tr><td>Paret</td><td>no</td><td>sí, de cel·lulosa, per fora de la membrana</td></tr>
<tr><td>Cloroplasts</td><td>no</td><td>sí, a les cèl·lules fotosintètiques</td></tr>
<tr><td>Vacúol</td><td>petits, si n’hi ha</td><td>un de gran, amb turgència</td></tr>
<tr><td>Centríols</td><td>sí</td><td>no, i el fus es munta igualment</td></tr>
<tr><td>Lisosomes</td><td>evidents</td><td>menys habituals; el vacúol fa part d’aquest paper</td></tr>
<tr><td>Nutrició</td><td>heteròtrofa</td><td>autòtrofa si hi ha cloroplasts</td></tr>
</tbody></table>
<p>El nucli, el reticle, el Golgi, els mitocondris i els ribosomes 80S són comuns. El reticle rugós fabrica proteïnes que aniran a la secreció o a la membrana; el llis, lípids i destoxificació. El Golgi madura i classifica. Confondre Golgi i reticle és un error de dibuix: el reticle és una xarxa contínua amb el nucli; el Golgi és una pila de sacs separada.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Una micrografia mostra una cèl·lula amb paret, un vacúol que ocupa gran part del volum i orgànuls verds amb membranes internes apilades. És animal o vegetal? On és el Calvin?</p><p>Vegetal. Els orgànuls verds són cloroplasts. El Calvin és a l’estroma, no als tilacoides.</p></div>
"""

EXTRA["cel-s7"] = """
<p>Convé fixar què es veu a cada fase, perquè la PAU ho demana sobre un esquema. A la interfase el nucli sembla homogeni: el DNA ja s’ha replicat a la fase S, però les cromàtides encara no es distingeixen. A la profase es condensen. A la prometafase desapareix l’embolcall i els microtúbuls enganxen el cinetocor. A la metafase tots els centròmers són al pla equatorial. A l’anafase cada pol rep una cromàtide de cada cromosoma, que a partir d’ara ja compta com un cromosoma. A la telofase es refan dos nuclis. La citocinesi no és una fase de la mitosi en sentit estricte, però és el que parteix el citoplasma.</p>
"""

EXTRA["cel-s8"] = """
<h4>Mitosi i meiosi</h4>
<table><thead><tr><th></th><th>Mitosi</th><th>Meiosi</th></tr></thead><tbody>
<tr><td>Nombre de divisions</td><td>1</td><td>2</td></tr>
<tr><td>Entrecreuament</td><td>no</td><td>sí, a la profase I</td></tr>
<tr><td>Què se separa a la primera anafase</td><td>cromàtides germanes</td><td>cromosomes homòlegs</td></tr>
<tr><td>Cèl·lules que en surten</td><td>2, diploides, idèntiques</td><td>4, haploides, diferents</td></tr>
<tr><td>Funció</td><td>créixer, renovar, reproduir-se sense gàmetes</td><td>fer gàmetes o espores i generar variació</td></tr>
</tbody></table>
<p>Si l’esquema mostra parelles de cromosomes (un de cada color, per exemple) que se separen encara amb dues cromàtides, és anafase I. Si mostra cromàtides soltes marxant cap als pols, pot ser anafase de mitosi o anafase II. El context (si abans hi ha hagut aparellament) ho decideix.</p>
<div class="box ex"><div class="lead">Exemple resolt</div><p>Una cèl·lula 2n = 8 entra en meiosi. Quants cromosomes hi ha a cada pol al final de l’anafase I, i quants a cada gàmeta al final de la meiosi II?</p><p>A l’anafase I cada pol rep 4 cromosomes (n = 4), encara duplicats. Després de la meiosi II, cada nucli té 4 cromosomes d’una sola cromàtide.</p></div>
"""

EXTRA["gen-s1"] = """
<h4>DNA i RNA</h4>
<table><thead><tr><th></th><th>DNA</th><th>RNA</th></tr></thead><tbody>
<tr><td>Sucre</td><td>desoxiribosa</td><td>ribosa</td></tr>
<tr><td>Bases</td><td>A, T, G, C</td><td>A, U, G, C</td></tr>
<tr><td>Cadenes</td><td>dues, antiparal·leles</td><td>normalment una</td></tr>
<tr><td>On, en un eucariota</td><td>nucli, mitocondri, cloroplast</td><td>se’n fa al nucli i es tradueix al citosol</td></tr>
<tr><td>Funció</td><td>guardar la informació</td><td>expressar-la (RNAm, RNAt, RNAr)</td></tr>
</tbody></table>
"""

EXTRA["gen-s2"] = """
<h4>Replicació procariota i eucariota</h4>
<table><thead><tr><th></th><th>Procariota</th><th>Eucariota</th></tr></thead><tbody>
<tr><td>Origens</td><td>una</td><td>moltes</td></tr>
<tr><td>Qui allarga</td><td>DNA-polimerasa III</td><td>diverses polimerases</td></tr>
<tr><td>Qui treu l’encebador</td><td>DNA-polimerasa I</td><td>maquinària equivalent</td></tr>
<tr><td>Extrems</td><td>el cromosoma és circular</td><td>telòmers; la telomerasa els allarga en algunes cèl·lules</td></tr>
<tr><td>Comú</td><td colspan="2">semiconservativa, síntesi només 5′→3′, cadena líder i retardada, helicasa, primasa, ligasa, SSB</td></tr>
</tbody></table>
<div class="box ex"><div class="lead">Exemple resolt</div><p>Per què la cadena retardada no es pot fer d’una sola tirada, en el mateix sentit que avança la forquilla?</p><p>Perquè la polimerasa només afegeix nucleòtids a un extrem 3′. Al motlle que queda orientat al revés, l’única manera d’avançar amb la forquilla és anar fent fragments cap enrere, cadascun amb el seu encebador.</p></div>
"""

EXTRA["gen-s3"] = """
<h4>Transcripció: procariotes i eucariotes</h4>
<table><thead><tr><th></th><th>Procariota</th><th>Eucariota</th></tr></thead><tbody>
<tr><td>Enzim de l’RNAm</td><td>una RNA-polimerasa, amb factor σ</td><td>RNA-polimerasa II</td></tr>
<tr><td>On</td><td>citoplasma (no hi ha nucli)</td><td>nucli</td></tr>
<tr><td>Maduració</td><td>no: es pot traduir de seguida</td><td>cap 5′, cua poli-A, eliminació d’introns</td></tr>
<tr><td>RNAm</td><td>sovint policistrònic (operó)</td><td>monocistrònic</td></tr>
</tbody></table>
<p>En els dos casos el motlle es llegeix 3′→5′ i l’RNA creix 5′→3′. La cadena codificant no es llegeix: l’RNA s’hi assembla, amb U en lloc de T.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Motlle 3′–TAC GGA TTA ACT–5′. Escriviu l’RNAm i digueu on comença i on s’atura la traducció si AUG és inici, UAA és parada, GGA és Gly i UUA és Leu. La taula de l’examen us donaria aquests codons.</p><p>RNAm 5′–AUG CCU AAU UGA–3′. Comença a AUG (Met) i s’atura a UGA, que no es tradueix. Entre mig, CCU i AAU. El motlle començava per TAC, que és l’AUG: no cal inventar un marc diferent.</p></div>
"""

EXTRA["imm-s2"] = """
<h4>Innata i específica</h4>
<table><thead><tr><th></th><th>Innata</th><th>Específica</th></tr></thead><tbody>
<tr><td>Especificitat</td><td>patrons generals</td><td>un antigen concret</td></tr>
<tr><td>Memòria</td><td>no</td><td>sí</td></tr>
<tr><td>Temps</td><td>minuts o hores</td><td>dies la primera vegada</td></tr>
<tr><td>Cèl·lules clau</td><td>neutròfils, macròfags, dendrítiques, NK, mastòcits</td><td>limfòcits T i B</td></tr>
<tr><td>Molècules</td><td>complement, histamina</td><td>anticossos, receptors T i B</td></tr>
</tbody></table>
"""

EXTRA["imm-s3"] = """
<h4>Limfòcits B i T</h4>
<table><thead><tr><th></th><th>B</th><th>T col·laborador (CD4)</th><th>T citotòxic (CD8)</th></tr></thead><tbody>
<tr><td>Reconeix</td><td>antigen sencer</td><td>pèptid + MHC II</td><td>pèptid + MHC I</td></tr>
<tr><td>Efecte</td><td>esdevé plasmàtica i fa anticossos</td><td>activa B i macròfags</td><td>mata la cèl·lula infectada</td></tr>
<tr><td>Branca</td><td>humoral</td><td>cel·lular (ajuda)</td><td>cel·lular</td></tr>
</tbody></table>
<p>Els T col·laboradors no secreten anticossos. Si un text ho diu, és una errada. Qui secreta anticossos és la cèl·lula plasmàtica.</p>
"""

EXTRA["mic-s6"] = """
<h4>Cicle lític i cicle lisogènic</h4>
<table><thead><tr><th></th><th>Lític</th><th>Lisogènic</th></tr></thead><tbody>
<tr><td>El genoma víric</td><td>es replica a part</td><td>s’integra (pròfag) i es copia amb el bacteri</td></tr>
<tr><td>La cèl·lula</td><td>es trenca i allibera virus</td><td>continua viva fins a la inducció</td></tr>
<tr><td>Quan es veu</td><td>infecció productiva</td><td>latència; després pot passar al lític</td></tr>
</tbody></table>
<p>Un retrovirus com el VIH fa un pas de més: l’RNA es copia a DNA (retrotranscriptasa) i aquest DNA s’integra. No és un bacteriòfag, però el principi d’integració s’assembla al lisogènic.</p>
"""

EXTRA["evo-s3"] = """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>En una població, el 16 % dels individus expressen un caràcter recessiu. Suposeu Hardy-Weinberg. Quina és la freqüència de l’al·lel recessiu i quina la de portadors?</p><p>q² = 0,16, q = 0,4. p = 0,6. Portadors 2pq = 2·0,6·0,4 = 0,48, és a dir un 48 %. No és el 16 %.</p></div>
<p>Si la població és petita, la deriva pot canviar p d’una generació a l’altra encara que ningú no es reprodueixi millor. Un coll d’ampolla i un efecte fundador són dos casos de deriva, no de selecció.</p>
"""

EXTRA["met-s4"] = """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Per què, sense oxigen, s’atura el cicle de Krebs encara que el Krebs no faci servir O₂ directament?</p><p>Perquè el NADH i el FADH₂ no es poden reoxidar a la cadena si l’oxigen no accepta els electrons. Sense NAD⁺ i FAD lliures, el Krebs no pot continuar. La fermentació existeix precisament per reoxidar el NADH sense cadena.</p></div>
"""

EXTRA["men-s4"] = """
<div class="box ex"><div class="lead">Exemple resolt</div><p>Un home hemofílic i una dona sana no portadora tenen una filla. Quina probabilitat té aquesta filla de ser hemofílica? I de ser portadora?</p><p>El pare li passa el seu X (Xʰ) i la mare un X sa (Xᴴ). La filla és XᴴXʰ: no és hemofílica (calen dos al·lels) i sí que és portadora. Probabilitat d’afectada: 0. De portadora: 1, en aquest encreuament.</p></div>
"""

EXTRA["dis-s2"] = """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Un grup mesura la velocitat d’un enzim a pH 7 i a pH 4, però al pH 4 també ha canviat la temperatura. Es pot concloure que el pH és la causa?</p><p>No. S’han canviat dues variables. Cal repetir-ho amb la temperatura fixa i un control a pH 7, amb rèpliques.</p></div>
"""


EXTRA["bio-s2"] = """
<h4>Reserva i estructura no són el mateix enllaç</h4>
<table><thead><tr><th>Polisacàrid</th><th>Enllaç</th><th>On</th><th>Funció</th></tr></thead><tbody>
<tr><td>Amilosa</td><td>α(1→4)</td><td>midó vegetal</td><td>reserva</td></tr>
<tr><td>Amilopectina i glicogen</td><td>α(1→4) i ramificacions α(1→6)</td><td>plantes / animals i fongs</td><td>reserva; el glicogen és més ramificat</td></tr>
<tr><td>Cel·lulosa</td><td>β(1→4)</td><td>paret vegetal</td><td>estructura</td></tr>
</tbody></table>
<p>La maltosa és el disacàrid de dues glucoses amb α(1→4). La sacarosa uneix glucosa i fructosa pels dos carbonis anomèrics (α1→β2) i per això no redueix. La lactosa és galactosa β(1→4) glucosa i sí que redueix. A la prova n’hi ha prou amb decidir el grup i, si l’enunciat dona l’enllaç, la funció.</p>
<div class="box ex"><div class="lead">Exemple resolt</div><p>Una cadena de glucoses amb enllaços β(1→4) es pot fer servir com a reserva muscular?</p><p>No. És cel·lulosa. La reserva animal és el glicogen, amb enllaços α. Els enzims que trenquen l’α no trenquen el β.</p></div>
"""

EXTRA["bio-s5"] = """
<p>Quan llegiu un gràfic, mireu primer si les corbes arriben al mateix sostre. Si la corba amb inhibidor assoleix la mateixa V<sub>max</sub> però més tard, l’inhibidor és competitiu: ocupa el centre actiu i el substrat el desplaça. Si el sostre baixa i no es recupera, no és competitiu. La temperatura té un òptim; per damunt, la proteïna es desnaturalitza i la velocitat cau. Això no és una inhibició competitiva.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Un enzim digestiu treballa a pH 2 i deixa de fer-ho a pH 8. N’hi ha prou per dir que s’ha desnaturalitzat?</p><p>No del tot. A pH 8 pot estar fora de l’òptim i recuperar-se si es torna a pH 2. La desnaturalització implica pèrdua del plegament, sovint irreversible. L’enunciat només diu que a pH 8 no treballa. La pepsina té l’òptim àcid: a pH 8 no és el seu medi.</p></div>
"""

EXTRA["met-s8"] = """
<h4>Fotosíntesi i respiració</h4>
<table><thead><tr><th></th><th>Fotosíntesi oxigènica</th><th>Respiració aeròbica</th></tr></thead><tbody>
<tr><td>On, en una planta</td><td>cloroplast</td><td>citosol (glucòlisi) i mitocondri</td></tr>
<tr><td>Energia</td><td>llum</td><td>energia química del combustible</td></tr>
<tr><td>Gasos</td><td>entra CO₂, surt O₂</td><td>entra O₂, surt CO₂</td></tr>
<tr><td>L’aigua</td><td>es trenca (fotòlisi) i dona l’O₂</td><td>es forma a la cadena</td></tr>
<tr><td>Coenzim reduït</td><td>NADPH</td><td>NADH i FADH₂</td></tr>
</tbody></table>
<p>No són la mateixa via al revés. Una planta respira de dia i de nit. De dia, a la llum, la fotosíntesi sol superar la respiració i el balanç net és d’entrada de CO₂.</p>
"""

EXTRA["men-s3"] = """
<p>El 9:3:3:1 només val si els dos gens són independents i hi ha dominància completa a tots dos. Si el recompte s’aparta d’això i els parentals són majoria, els gens estan lligats. La distància en centimorgans és el percentatge de recombinants. Un 50 % vol dir que es comporten com si no estiguessin lligats: o són lluny al mateix cromosoma, o són a cromosomes diferents.</p>
<div class="box ex"><div class="lead">Exemple resolt</div><p>Encreuament prova: 430 parentals i 70 recombinants. Estan lligats? A quina distància?</p><p>70/500 = 0,14. Sí que estan lligats, a 14 cM. Si haguessin estat independents, els quatre tipus haurien sortit prop del 25 % cadascun.</p></div>
"""

EXTRA["mic-s1"] = """
<h4>Bacteris i arqueus</h4>
<table><thead><tr><th></th><th>Bacteris</th><th>Arqueus</th></tr></thead><tbody>
<tr><td>Organització</td><td>procariota</td><td>procariota</td></tr>
<tr><td>Paret</td><td>peptidoglicà</td><td>sense peptidoglicà</td></tr>
<tr><td>Lípids de membrana</td><td>enllaços èster</td><td>enllaços èter</td></tr>
<tr><td>Parentiu</td><td>domini Bacteria</td><td>més propers als eucariotes en la maquinària genètica</td></tr>
</tbody></table>
<p>Dir «bacteri» per a qualsevol procariota és l’error. Els arqueus no es tenyeixen com un Gram clàssic de manual, perquè la tinció mira el peptidoglicà.</p>
"""

EXTRA["imm-s5"] = """
<p>La taula de les quatre combinacions es pregunta gairebé cada any, amb un cas. La vacuna és activa i artificial. El sèrum és passiu i artificial. La infecció és activa i natural. Els anticossos de la mare són passius i naturals. Només l’activa deixa memòria, perquè només llavors el propi sistema ha seleccionat clons.</p>
"""

EXTRA["evo-s1"] = """
<p>Una prova sola no «demostra» l’evolució com si fos un experiment d’un dia. El que es demana és relacionar-ne dues: per exemple, que els ossos de l’extremitat anterior són homòlegs i que les seqüències del gen corresponent també s’assemblen més entre parents propers. La convergència explica per què una ala d’ocell i una ala d’insecte no són un argument de parentiu.</p>
"""

EXTRA["dis-s3"] = """
<p>Quan el gràfic té dos eixos, escriviu la conclusió amb les unitats que s’hi veuen. Si la corba puja i després cau, no digueu que «sempre puja». Si compareu dues espècies amb un sol individu, la conclusió màxima és que aquells dos exemplars difereixen, no que les espècies senceres ho facin. La millora és afegir rèpliques biològiques.</p>
<div class="box ex"><div class="lead">Exemple resolt</div><p>Un text diu que la glucòlisi ocorre a la matriu mitocondrial i rendeix 38 ATP. Quines errades hi ha?</p><p>La glucòlisi és al citosol i el balanç net són 2 ATP i 2 NADH. Els 30–32 ATP (o 36–38 en el conveni escolar) són el total de la respiració aeròbica completa, no el de la glucòlisi.</p></div>
"""

def deepen(html: str) -> str:
    blocks: dict[str, str] = {}
    for src in (EXTRA, MORE):
        for sid, extra in src.items():
            blocks[sid] = blocks.get(sid, "") + "\n" + extra
    for sid, extra in blocks.items():
        token = f'<section id="{sid}"'
        i = html.find(token)
        if i < 0:
            continue
        j = html.find("</section>", i)
        if j < 0:
            raise SystemExit(f"depth: secció {sid} sense tancament")
        html = html[:j] + extra + html[j:]
    return html
