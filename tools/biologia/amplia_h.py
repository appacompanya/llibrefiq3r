"""Tercera capa: balanços i problemes llargs, els que la PAU puntua pas a pas."""

MORE = {}

def P(sid, html):
    MORE[sid] = html

P("met-s4", """
<h4>Un balanç sencer, amb els dos convenis</h4>
<p>Es parteix d’una glucosa. Glucòlisi, al citosol: es paguen 2 ATP, se’n cobren 4, net 2 ATP, i queden 2 NADH i 2 piruvats. Cada piruvat, a la matriu, dona un acetil-CoA, un NADH i un CO₂. Dues vegades: 2 NADH i 2 CO₂. Cada acetil-CoA fa una volta de Krebs: 3 NADH, 1 FADH₂, 1 GTP i 2 CO₂. Dues voltes: 6 NADH, 2 FADH₂, 2 GTP i 4 CO₂. El CO₂ total és 6, que és el de la glucosa. El GTP es compta com a ATP.</p>
<p>Conveni actual, P/O 2,5 per NADH i 1,5 per FADH₂. Els 2 NADH de la glucòlisi, si la llançadora és la del malat-aspartat, compten com a NADH matricials: 2 × 2,5 = 5. Si és la del glicerol-fosfat, compten com a FADH₂: 2 × 1,5 = 3. Els 2 NADH del pont: 5. Els 6 del Krebs: 15. Els 2 FADH₂: 3. Més 2 ATP de la glucòlisi i 2 del GTP. Total 32 o 30. Aquest és el 30–32.</p>
<p>Conveni escolar, 3 i 2. Els mateixos NADH matricials donen 3, els FADH₂ donen 2. Els 8 NADH de dins (2 del pont i 6 del Krebs) donen 24. Els 2 FADH₂ donen 4. Els 2 NADH citosòlics donen 6 o 4 segons la llançadora. Més 4 de substrat. Total 38 o 36. Quan l’enunciat diu «calculeu segons el conveni de 3 i 2», es fa així i es diu. Quan no ho diu, es pot donar el 30–32 i esmentar que el clàssic és 36–38.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Un NADH i un FADH₂ arriben a la cadena. Amb el conveni 2,5 i 1,5, quant ATP se’n fa, i per què el FADH₂ en fa menys si tots dos acaben a l’oxigen?</p><p>2,5 i 1,5. El FADH₂ entrega els electrons al complex II, no al I, i es bomba menys protons per aquell parell d’electrons. L’oxigen és el mateix acceptor; el que canvia és el tram de la cadena que es recorre. Per això no es pot dir «tots els coenzims reduïts valen igual».</p></div>
""")

P("met-s2", """
<p>Val la pena saber el balanç sense memoritzar els deu enzims. Glucosa a glucosa-6-fosfat gasta un ATP. Fructosa-6-fosfat a fructosa-1,6-bisfosfat en gasta un altre. Aquest segon pas és el principal punt de regulació: l’ATP el frena i l’AMP l’activa. La molècula de sis es parteix en dues de tres. A partir d’aquí es multiplica per dos. Cada triosa s’oxida (un NAD⁺ per triosa, dos per glucosa) i el fosfat que s’hi enganxa acaba a l’ATP. Dues vegades per triosa, quatre ATP bruts, dos nets. El producte és piruvat, no etanol ni lactat: això ja és fermentació, un pas de més.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Una cèl·lula transforma 5 glucoses per glucòlisi i després fermenta a lactat. Quants ATP nets, quants NADH queden acumulats i quants lactats?</p><p>10 ATP nets. Cap NADH acumulat: la fermentació els ha tornat a NAD⁺, i aquest és el motiu de fer-la. 10 lactats, perquè cada glucosa dona 2 piruvats i cada piruvat un lactat. Si l’enunciat hagués dit «només glucòlisi, amb oxigen», els NADH serien 10 i no hi hauria lactat.</p></div>
""")

P("met-s8", """
<p>El balanç del Calvin es demana per CO₂ o per glucosa, i no s’han de barrejar. Per un CO₂: la rubisco el fixa, surten dues molècules de tres carbonis, i reduir-les i regenerar la ribulosa costa 2 NADPH i 3 ATP. Per sis CO₂, que són els d’una glucosa, 12 NADPH i 18 ATP. Aquests no surten del mitocondri. Surten de la fase lluminosa. L’aigua es trenca al fotosistema II, a la banda del lumen. L’oxigen que se’n va és el de l’aigua. Els protons queden al lumen, tornen a l’estroma per l’ATP-sintasa, i el NADPH es forma a l’estroma, al final del fotosistema I. El Calvin, que gasta les dues coses, és a l’estroma. Si es diu que el Calvin és al tilacoide, el balanç de protons queda al revés.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Una planta fixa 12 CO₂. Quants NADPH i quants ATP gasta el Calvin, i quants O₂ ha hagut de desprendre la fase lluminosa si la relació és la de la fotosíntesi oxigènica, un O₂ per cada dos aigua, amb sis O₂ per glucosa?</p><p>12 CO₂ són dues glucoses. NADPH: 12 × 2 = 24. ATP: 12 × 3 = 36. O₂: dues glucoses, 12 O₂. El CO₂ no és la font de l’O₂; la relació 1:1 entre CO₂ fixat i O₂ desprès és el balanç global, no el mecanisme. El mecanisme continua essent la fotòlisi.</p></div>
""")

P("bio-s6", """
<p>Un problema de composició es resol sempre en el mateix ordre, i només si el DNA és de doble cadena. Es escriu A = T i G = C. Si donen un percentatge, el de la parella és el mateix, i el que queda es parteix per la meitat entre l’altra parella. La comprovació és que els quatre sumin 100. Si donen una cadena sola, o un RNA, no es fa aquest càlcul: es diu que no es pot, i això ja és la resposta.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Cadena 5′–ATCCG–3′ d’un DNA. Escriviu la complementària en 5′→3′, i l’RNAm si aquesta cadena fos la codificant.</p><p>La complementària, antiparal·lela, és 3′–TAGGC–5′, que en el sentit 5′→3′ s’escriu 5′–GGCTA–3′. Si la cadena donada és la codificant, l’RNAm s’hi assembla: 5′–AUCCG–3′. Si fos el motlle, l’RNAm seria el complement amb U: 5′–CGGAU–3′. La pregunta decideix quin dels dos papers té la cadena. No es pot contestar sense llegir la paraula «codificant» o «motlle».</p></div>
""")

P("cel-s8", """
<p>El recompte de la meiosi es fa per fases, no de memòria. S’escriu 2n. A la profase I es formen n bivalents. A l’anafase I cada pol rep n cromosomes de dues cromàtides. No hi ha S. A l’anafase II cada un d’aquests cromosomes se separa en dues cromàtides, i cada pol en rep n d’una sola peça. Al final, quatre nuclis, cadascun amb n cromosomes. Si en algun pas el nombre es dobla sense una anafase, el recompte està malament.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>2n = 46. Quants bivalents a la profase I, quants cromosomes a un nucli al final de la telofase I, i quants a un gàmeta al final de la meiosi II?</p><p>23 bivalents. Al final de la telofase I, 23 cromosomes, encara amb dues cromàtides cadascun: el DNA d’aquell nucli és 2C, no 1C. Al gàmeta, 23 cromosomes d’una cromàtide, 1C. La fecundació torna a 46. Dir 23 parells al gàmeta és tornar al 2n.</p></div>
""")

P("men-s3", """
<p>La distància es calcula només amb un encreuament prova, on es veu el genotip de cada descendent. Es sumen els dos tipus recombinants, es divideix pel total i es multiplica per 100. Els parentals són els dos grups grans. Si els quatre grups són semblants, no hi ha lligament i no es dona una distància: es diu que són independents o tan lluny que no es distingeixen.</p>
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Dades: 610, 590, 45, 55. Calculeu la distància i digueu quins són els parentals.</p><p>Total 1.300. Els parentals són 610 i 590. Els recombinants, 45 i 55, sumen 100. 100/1.300 = 0,0769. Distància 7,7 cM, que es pot deixar en 7,7 o en 8 segons les xifres significatives de l’enunciat. No es calcula 610/1.300: això és la freqüència d’un parental, no la distància.</p></div>
""")

P("men-s4", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Una dona sana filla d’un pare hemofílic i d’una mare no portadora es casa amb un home sa. Quina probabilitat té un fill home de la parella de ser hemofílic?</p><p>La dona és portadora obligada: el pare li ha passat el seu únic X, que és l’afectat, i la mare un X sa. Amb un home sa, cada fill home té ½ de rebre l’X afectat. Una filla no serà hemofílica: el pare sa li dona un X sa. La probabilitat que es demana, la del fill home, és ½, no ¼, perquè el sexe ja està fixat a l’enunciat. Si demanés «un fill qualsevol, sense saber el sexe», seria ¼: ½ de ser home i ½ de rebre l’al·lel.</p></div>
""")

P("men-s5", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Dos heterozigots per a dos gens independents, AaBb × AaBb. Quina probabilitat té un fill de ser aabb? I de tenir almenys un fenotip dominant?</p><p>aabb és ¼ × ¼ = 1/16. Almenys un fenotip dominant és tot el que no és el doble recessiu: 1 − 1/16 = 15/16. No és 9/16: això és només el doble dominant. «Almenys un» inclou els 9/16, els 3/16 i els 3/16. Fer el producte i restar de 1 és més curt que sumar tres fraccions, i dona el mateix.</p></div>
""")

P("evo-s3", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>El 36 % dels individus són homozigots recessius. La població està en equilibri. Quin percentatge són heterozigots?</p><p>q² = 0,36, q = 0,6, p = 0,4. Heterozigots 2pq = 2 × 0,4 × 0,6 = 0,48, un 48 %. Homozigots dominants p² = 0,16, un 16 %. Comprovació: 16 + 48 + 36 = 100. El 36 % no és la freqüència de l’al·lel: és la del genotip. L’al·lel és 0,6, més alt, perquè també és a la meitat dels heterozigots.</p></div>
<p>Quan l’enunciat dona el percentatge d’afectats d’un recessiu, el primer pas és sempre l’arrel, no dividir per dos. Dividir el 36 % per dos i dir que els portadors són el 18 % és l’error de no fer servir el binomi.</p>
""")

P("gen-s3", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>RNAm 5′–AUG UUC UAA GGG–3′. La taula diu que UUC és Phe i GGG és Gly. Quina proteïna se’n fa, i per què la glicina no hi és?</p><p>Met–Phe. UAA és parada i el ribosoma se’n va. GGG és a continuació i no es llegeix. Una parada al mig no es «salta». Si l’enunciat hagués posat UUC i GGG abans de la parada, la glicina hi seria. L’ordre és el que mana, no la llista d’aminoàcids que algú veu a la taula.</p></div>
<p>El marc es fixa a l’AUG. Si es comença un nucleòtid abans, AUG desapareix i la lectura és una altra proteïna, o cap. Per això una inserció d’una base és greu: no canvia una lletra, canvia totes les de després.</p>
""")

P("gen-s6", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Una substitució canvia UUU (Phe) per UUC (Phe). Una deleció treu la primera U. Compareu l’efecte sobre la proteïna, sabent que el triplet següent era GGA (Gly) i que, desplaçat, el nou triplet pot ser un altre.</p><p>La substitució és silenciosa: l’aminoàcid no canvia, el marc tampoc. La deleció treu una base i tot el que ve després es llegeix en un marc diferent. Encara que el primer aminoàcid afectat es pogués salvar, la resta de la cadena no. La deleció és la mutació greu. No es puntua igual una substitució sinònima i un canvi de marc.</p></div>
""")

P("imm-s5", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Un nadó té IgG de la mare, que anirà baixant, i als dos mesos se’l vacuna. Dibuixeu amb paraules les dues corbes: la de l’IgG materna i la de la resposta del nadó. Quina és passiva i quina deixa memòria?</p><p>L’IgG materna baixa en setmanes, sense un segon pic: és passiva natural, i el nadó no ha fet clons. La vacuna, al cap d’uns dies, fa un pic propi, més lent la primera vegada, i deixa memòria: és activa artificial. Si més endavant hi ha un record, el pic del nen serà més ràpid. Les dues corbes no s’han de sumar com si fossin la mateixa resposta.</p></div>
""")

P("mic-s6", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Compareu, en quatre files, el cicle lític i el lisogènic: on és el genoma, què fa la cèl·lula, si es produeixen virions de seguida, i com es passa de l’un a l’altre.</p><p>Lític: el genoma es replica a part, la cèl·lula acaba lisant-se, els virions surten de seguida, i no cal cap inducció perquè ja és el cicle productiu. Lisogènic: el genoma integrat (pròfag, si és un bacteri), la cèl·lula viu i es divideix, no hi ha virions mentre dura la latència, i un senyal d’estrès indueix el pas al lític. No són dos virus diferents. Són dos programes del mateix virus, quan el virus els té tots dos.</p></div>
""")

P("cel-s4", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Tres casos. A: O₂ entra sense proteïna. B: glucosa entra a favor de gradient amb una proteïna, sense ATP. C: Na⁺ surt contra de gradient gastant ATP. Poseu el nom de cada transport i digueu quin es pararia primer si no hi hagués ATP, i quin no se’n ressentiria.</p><p>A és difusió simple. B, difusió facilitada. C, transport actiu primari. Sense ATP es para C de seguida. B continua mentre duri el gradient de glucosa. A no depèn ni de proteïna ni d’ATP. A la llarga, els gradients que mantenen algunes difusions facilitades els ha creat una bomba, i també cauran; però el que es para de manera directa és l’actiu.</p></div>
""")

P("bio-s5", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Sense inhibidor, la V<sub>max</sub> és 100 i la K<sub>m</sub> és 5 mmol/L. Amb un inhibidor, la V<sub>max</sub> continua essent 100 i la concentració que dona velocitat 50 passa a 20 mmol/L. De quin tipus és, i què ha passat amb l’afinitat aparent?</p><p>Competitiu. La K<sub>m</sub> aparent ha passat de 5 a 20, quatre vegades més alta: cal més substrat per arribar a la meitat de la velocitat, que és la definició operativa de menys afinitat aparent. La V<sub>max</sub> no ha canviat, de manera que a substrat molt alt el fàrmac es desplaça. Si la V<sub>max</sub> hagués baixat a 40, no seria competitiu.</p></div>
""")

P("dis-s3", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Un gràfic mostra la velocitat d’un enzim a cinc pH: 2, 4, 6, 8 i 10. Els valors són 10, 40, 90, 30 i 5. On és l’òptim, i per què no es diu que «com més alt és el pH, més lenta és la reacció»?</p><p>L’òptim, d’aquests punts, és pH 6. La frase és falsa perquè de 2 a 6 la velocitat puja. Només baixa a partir de l’òptim. Una frase vàlida és: hi ha un òptim a pH 6 i la velocitat cau a banda i banda. Extrapol·lar a pH 12 no es pot fer amb aquestes dades.</p></div>
""")

P("gen-s8", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Es parteix de 4 molècules i es fan 10 cicles de PCR, amb eficiència del 100 %. Quantes còpies del tram hi ha al final? Per què el resultat no és 4 × 10?</p><p>Cada cicle dobla. 4 × 2¹⁰ = 4 × 1.024 = 4.096. Multiplicar per 10 seria un creixement lineal, que no és el de la PCR. El creixement és exponencial mentre hi ha encebadors, nucleòtids i polimerasa activa. Quan un d’aquests s’acaba, la corba s’aplana i el 4.096 teòric no s’assoleix.</p></div>
""")

P("mic-s3", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Un sòl perd nitrat cap a l’atmosfera en condicions d’anòxia. Quin procés bacterià és, i per què no és la fixació, que també toca el N₂?</p><p>És la desnitrificació: nitrat a N₂. La fixació va en sentit contrari, de N₂ a amoníac, i la fan organismes amb nitrogenasa, sovint en simbiosi i amb un cost gran d’ATP. La desnitrificació la fan altres bacteris quan no hi ha oxigen i fan servir el nitrat com a acceptor. El mateix gas, dos sentits, dos grups de microorganismes.</p></div>
""")

P("evo-s2", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>En una població de polls, un insecticida mata el 99 %. Al cap de dos anys, el mateix producte mata el 20 %. Proposeu l’explicació seleccionista i descarteu la lamarckiana en una frase.</p><p>El 1 % que va sobreviure portava, ja abans, una variant heretable de resistència. Els seus fills són la població actual, i per això el producte ja no funciona. No és que cada poll hagi desenvolupat resistència en resposta al verí i l’hagi llegada. Si fos així, la resistència apareixeria igual en una població sense variació prèvia, i no és el que s’observa.</p></div>
""")

P("imm-s3", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Una cèl·lula infectada per un virus deixa de mostrar MHC I. Quina cèl·lula de la innata la pot matar precisament per això, i quina de l’específica la mataria si el MHC I sí que mostrés el pèptid?</p><p>Sense MHC I, la cèl·lula NK, que interpreta l’absència com un senyal de perill. Si el MHC I mostra el pèptid, el T citotòxic CD8 la reconeix i la mata. Són dues vies cap a un resultat semblant, amb receptors diferents. La NK no és específica d’antigen. El CD8 sí.</p></div>
""")

P("bio-s2", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Es donen tres polisacàrids de glucosa. Un no el digerim, un és la reserva de les plantes i un és la reserva del múscul. Poseu el nom, l’enllaç decisiu i el compartiment o el teixit.</p><p>El que no digerim és la cel·lulosa, β(1→4), a la paret vegetal. La reserva de les plantes és el midó (amilosa i amilopectina), α(1→4) i, en l’amilopectina, ramificacions α(1→6), als plastidis. La reserva del múscul és el glicogen, els mateixos enllaços amb més ramificacions, al citosol. El fet de ser glucosa no decideix la funció. La decideix l’enllaç i el lloc.</p></div>
""")

P("cel-s5", """
<div class="box pau"><div class="lead">Mini-PAU resolt</div><p>Ompliu el lloc, en una cèl·lula vegetal: fotòlisi, Calvin, Krebs, cadena respiratòria, síntesi de proteïnes de secreció.</p><p>Fotòlisi: lumen del tilacoide, al fotosistema II. Calvin: estroma. Krebs: matriu del mitocondri. Cadena respiratòria: membrana interna del mitocondri. Proteïnes de secreció: es comencen al reticle rugós i es maduren al Golgi. Cap d’aquests llocs no es pot intercanviar. El mitocondri no fa el Calvin i el cloroplast no fa el Krebs.</p></div>
""")
