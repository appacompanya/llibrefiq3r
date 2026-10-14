/* Fitxes digitals. La clau és la mateixa que al llibre (D). Les fitxes que no hi són s'obren en PDF
   i l'alumne pot lliurar-ne una foto. "expected" i "criteria" només els fa servir la zona del professorat. */
window.FITXES = {

d1f1: {
  title: "Fitxa 1 · Magnituds, unitats i notació científica", sda: 1,
  intro: "Sessió 2. Acaba-la a casa i lliura-la a la sessió 3.",
  blocks: [
    { type: "tip", html: "<b>Recorda.</b> Una <b>magnitud</b> és una propietat que es pot mesurar i expressar amb un nombre i una unitat. Les <b>fonamentals</b> es defineixen per si mateixes (longitud, massa, temps, temperatura…); les <b>derivades</b> s'obtenen a partir de les fonamentals (superfície, volum, velocitat, densitat…). Equivalència clau: 1 mL = 1 cm³ i 1 L = 1 dm³." },
    { id: "1", type: "table", prompt: "<b>Fonamental o derivada?</b> Classifica aquestes magnituds i escriu la unitat del SI de cadascuna.",
      cols: ["Magnitud", "Fonamental o derivada", "Unitat del SI (nom i símbol)"],
      rows: [["Massa","F","quilogram (kg)"],["Volum","D","metre cúbic (m³)"],["Temps","F","segon (s)"],["Densitat","D","quilogram per metre cúbic (kg/m³)"],["Longitud","F","metre (m)"],["Velocitat","D","metre per segon (m/s)"],["Temperatura","F","kelvin (K)"],["Superfície","D","metre quadrat (m²)"]]
        .map(([m, fd, u]) => ({ label: m, cells: [{ type: "select", options: ["Fonamental", "Derivada"], expected: fd === "F" ? "Fonamental" : "Derivada" }, { type: "text", expected: u }] })) },
    { id: "2", type: "table", prompt: "<b>Els prefixos.</b> Completa la taula amb el símbol, l'equivalència respecte de la unitat i la potència de 10.",
      cols: ["Prefix", "Símbol", "Equivalència", "Potència de 10"],
      rows: [["kilo","k","1000","10^3"],["hecto","h","100","10^2"],["deca","da","10","10^1"],["deci","d","0,1","10^-1"],["centi","c","0,01","10^-2"],["mil·li","m","0,001","10^-3"],["micro","µ","0,000001","10^-6"],["nano","n","0,000000001","10^-9"]]
        .map(([p, s, e, w]) => ({ label: p, cells: [{ type: "text", expected: s, small: true }, { type: "number", expected: e }, { type: "pow10", expected: w }] })) },
    { id: "3", type: "group", prompt: "<b>Conversions simples.</b> Fes aquests canvis d'unitats amb un factor de conversió. Escriu el factor i el resultat amb la unitat.",
      items: [["a","2,5","kg","g","2500"],["b","350","mg","g","0,35"],["c","1,2","m","cm","120"],["d","750","mL","L","0,75"],["e","0,25","L","cm³","250"],["f","3","dm³","mL","3000"],["g","45","cm³","mL","45"],["h","2","m³","L","2000"]]
        .map(([k, v, u, to, r]) => ({ id: "3" + k, type: "chain", label: `${k}) ${v} ${u} → ${to}`, start: { v, u, fixed: true }, target: to, expected: { v: r, u: to, strict: true } })) },
    { type: "h", text: "Notació científica" },
    { type: "tip", html: "Per escriure nombres molt grans o molt petits fem servir la <b>notació científica</b>: \\(a \\cdot 10^{n}\\), amb \\(1 \\le a < 10\\). Si el nombre és més gran que 1, l'exponent és positiu: \\(25\\,000 = 2{,}5 \\cdot 10^{4}\\). Si és més petit que 1, és negatiu: \\(0{,}0003 = 3 \\cdot 10^{-4}\\). Per multiplicar se sumen els exponents i per dividir es resten." },
    { id: "4", type: "group", prompt: "<b>Escriu en notació científica.</b>",
      items: [["a","300 000 000 m/s (velocitat de la llum)","3·10^8"],["b","0,000 07 m (gruix d'un cabell)","7·10^-5"],["c","6 371 000 m (radi de la Terra)","6,371·10^6"],["d","0,000 000 000 1 m (mida d'un àtom)","1·10^-10"],["e","150 000 000 km (distància de la Terra al Sol)","1,5·10^8"],["f","0,0025 kg (massa d'un clip)","2,5·10^-3"]]
        .map(([k, t, e]) => ({ id: "4" + k, type: "sci", label: `${k}) ${t}`, expected: e })) },
    { id: "5", type: "group", prompt: "<b>Escriu en forma decimal.</b>",
      items: [["a","4,2·10³ g","4200"],["b","7,5·10⁻⁶ m","0,0000075"],["c","1,0·10⁻³ L","0,001"],["d","9,46·10¹⁵ m (un any llum)","9460000000000000"]]
        .map(([k, t, e]) => ({ id: "5" + k, type: "number", label: `${k}) ${t}`, expected: e })) },
    { id: "6", type: "group", prompt: "<b>Opera</b> i dona el resultat en notació científica. Escriu l'operació amb l'editor (fes servir el botó de fracció i el de ·10ⁿ).",
      items: [["a","(3·10⁴)·(2·10⁻⁶)","6·10^-2"],["b","(8·10⁻³) / (4·10²)","2·10^-5"],["c","(1,5·10⁸)·(4·10³)","6·10^11"],["d","(6·10⁻²) / (3·10⁻⁵)","2·10^3"]]
        .map(([k, t, e]) => ({ id: "6" + k, type: "math", label: `${k}) ${t}`, expected: e, answerSci: true })) },
    { id: "7", type: "text", lines: 4, prompt: "<b>Ordre de magnitud.</b> Ordena de més petit a més gran i escriu-los en metres i en notació científica: un àtom (0,1 nm), un glòbul vermell (7,5 µm), una formiga (3 mm), un gra de sorra (0,5 mm) i un bacteri (1 µm).",
      expected: "Àtom 1·10⁻¹⁰ m < bacteri 1·10⁻⁶ m < glòbul vermell 7,5·10⁻⁶ m < gra de sorra 5·10⁻⁴ m < formiga 3·10⁻³ m",
      criteria: "Ordre correcte i les cinc mides en metres amb notació científica correcta." },
  ],
},

d1f2: {
  title: "Fitxa 2 · Factors de conversió", sda: 1,
  intro: "Sessió 3. Els exercicis 1–4 es fan a classe. La part B és per a casa i es lliura a la sessió 4.",
  blocks: [
    { type: "tip", html: "<b>Mètode dels factors de conversió.</b> Multipliquem la quantitat per fraccions que valen 1 (numerador i denominador són la mateixa quantitat en unitats diferents), de manera que les unitats que no volem se simplifiquen: \\[ 72\\ \\frac{\\mathrm{km}}{\\mathrm{h}} \\cdot \\frac{1000\\ \\mathrm{m}}{1\\ \\mathrm{km}} \\cdot \\frac{1\\ \\mathrm{h}}{3600\\ \\mathrm{s}} = 20\\ \\frac{\\mathrm{m}}{\\mathrm{s}} \\]" },
    { type: "h", text: "A · Factors de conversió encadenats" },
    { id: "1", type: "group", prompt: "<b>Densitats.</b>",
      items: [["a","1,2","g/mL","kg/m³","1200"],["b","0,79","g/cm³","kg/m³","790"],["c","2700","kg/m³","g/cm³","2,7"],["d","1,93·10^4","kg/m³","g/cm³","19,3"]]
        .map(([k, v, u, to, r]) => ({ id: "1" + k, type: "chain", label: `${k}) ${v.replace("·10^4", "·10⁴")} ${u} → ${to}${k === "d" ? " (densitat de l'or)" : ""}`, start: { v, u, fixed: true }, target: to, expected: { v: r, u: to, strict: true } })) },
    { id: "2", type: "group", prompt: "<b>Velocitats.</b>",
      items: [{ id: "2a", type: "chain", label: "a) 90 km/h → m/s", start: { v: "90", u: "km/h", fixed: true }, target: "m/s", expected: { v: "25", u: "m/s", strict: true } },
              { id: "2b", type: "chain", label: "b) 15 m/s → km/h", start: { v: "15", u: "m/s", fixed: true }, target: "km/h", expected: { v: "54", u: "km/h", strict: true } }] },
    { id: "3", type: "group", prompt: "<b>Concentracions.</b>",
      items: [{ id: "3a", type: "chain", label: "a) 5 g/L → mg/mL", start: { v: "5", u: "g/L", fixed: true }, target: "mg/mL", expected: { v: "5", u: "mg/mL", strict: true } },
              { id: "3b", type: "chain", label: "b) 250 mg/L → g/m³", start: { v: "250", u: "mg/L", fixed: true }, target: "g/m³", expected: { v: "250", u: "g/m³", strict: true } }] },
    { id: "4", type: "chain", prompt: "<b>Cabal.</b> Una aixeta aboca 0,5 L/min. Expressa-ho en mL/s.", start: { v: "0,5", u: "L/min", fixed: true }, target: "mL/s", expected: { v: "8,33", u: "mL/s", strict: true } },
    { type: "h", text: "B · Per a casa: cerca de densitats de referència" },
    { id: "B", type: "table", prompt: "Busca la densitat a 20 °C de cada substància en <b>fonts fiables</b> (manuals de dades, webs d'universitats o d'organismes oficials) i cita sempre la font.",
      cols: ["Substància", "Densitat (g/cm³)", "Font (autor o organització, títol, adreça web i data de consulta)"],
      rows: [["Aigua","0,998"],["Dissolució de clorur de sodi al 10 % en massa","1,07"],["Dissolució de sacarosa al 18 % en massa","1,07"],["Oli de gira-sol","0,92"],["Etanol","0,789"],["Dissolució de sulfat de coure(II) al 10 % en massa","1,11"],["Ferro","7,87"],["Alumini","2,70"]]
        .map(([s, d]) => ({ label: s, cells: [{ type: "number", expected: d, tol: 0.03 }, { type: "text", wide: true }] })) },
    { id: "5", type: "text", lines: 4, prompt: "<b>Fiabilitat.</b> Has trobat valors diferents per a una mateixa substància? Per què creus que passa? Quina font consideres més fiable i per què?",
      criteria: "Reconeix que la densitat depèn de la temperatura, la concentració o la puresa; justifica la fiabilitat amb criteris (autoria experta, institució, data, coincidència amb altres fonts)." },
  ],
},

d1ellen: {
  title: "Reading: the woman who tested the water", sda: 1,
  intro: "Lectura per a casa després de la sessió 6. El debat es fa a la sessió 7. Llegeix el text (o escolta'l), consulta el glossari i respon les preguntes.",
  blocks: [
    { type: "reading", title: "Ellen Swallow Richards (1842–1911)", lang: "en-GB", audio: "audio/ellen.mp3", img: "../img/sda1-ellen.png",
      paras: [
        "Ellen Swallow was born in 1842 in Massachusetts, in the United States. As a girl, she loved science. At that time, very few universities accepted women. Ellen studied at Vassar, a college for women. Then, in 1870, she asked to study chemistry at the Massachusetts Institute of Technology (MIT). MIT accepted her as “an experiment”. She was the first woman at MIT, and in 1873 she finished her degree in chemistry.",
        "In the 1880s, many towns in Massachusetts were growing very fast. People drank water from rivers, lakes and wells, but some of this water was dirty. Waste water from houses and factories went into the rivers, and many people got ill.",
        "In 1887, the government of Massachusetts asked Ellen and her team for help. For two years, they analysed more than 20,000 samples of water from all over the state. In the laboratory, they measured the amount of chloride in each sample. Chloride comes from salts, like sodium chloride, the salt we use in the kitchen. Clean water far from the sea has only a small, normal amount of chloride. When a sample had more chloride than normal, it was a sign of pollution from waste water.",
        "Ellen made a map with the normal values for the whole state: the “Normal Chlorine Map”. Thanks to this work, Massachusetts created the first water-quality standards in the United States, and a city built one of the first modern plants to clean waste water.",
        "Today, scientists still use Ellen's idea: to know if water is clean, we compare a sample with a reference."],
      glossary: "sample = mostra · waste water = aigües residuals · well = pou · to get ill = emmalaltir · amount = quantitat · pollution = contaminació · standard = norma, valor de referència · plant = planta (instal·lació) · to clean = netejar, depurar" },
    { type: "h", text: "A · Reading comprehension" },
    { id: "1", type: "tf", prompt: "<b>True or false?</b> Correct the false sentences.",
      statements: [["Ellen studied at MIT before she studied at Vassar.", false, "She studied at Vassar first, and then at MIT."], ["In 1870, it was easy for women to study at university.", false, "Very few universities accepted women."], ["Ellen and her team analysed more than 20,000 water samples.", true], ["A high amount of chloride was a sign of pollution.", true], ["Ellen's work helped to create the first water-quality standards in the USA.", true]] },
    { id: "2", type: "group", prompt: "<b>Answer in English with short sentences.</b>",
      items: [["a","Why did many people get ill in Massachusetts in the 1880s?","Because they drank dirty water: waste water from houses and factories went into the rivers."],["b","What did Ellen measure in each water sample?","The amount of chloride."],["c","What is the “Normal Chlorine Map”?","A map with the normal values of chloride for the whole state."]]
        .map(([k, q, e]) => ({ id: "2" + k, type: "text", lines: 2, label: `${k}) ${q}`, expected: e })) },
    { type: "h", text: "B · La ciència del text" },
    { id: "3", type: "text", lines: 3, prompt: "<b>L'ió clorur.</b> D'on prové el clorur de l'aigua? Quin pot del nostre repte en conté? Com el vam detectar a la sessió 5?", criteria: "Prové de sals com el clorur de sodi; el pot de NaCl; el detectem perquè la dissolució condueix el corrent (ions)." },
    { id: "4", type: "text", lines: 3, prompt: "<b>Mostra i referència.</b> Ellen comparava cada mostra amb un valor normal. Quan nosaltres hem fet el mateix en aquesta SdA? Posa'n un exemple.", criteria: "Exemple: comparar la densitat mesurada amb el valor de referència i calcular l'error." },
    { id: "5", type: "text", lines: 3, prompt: "<b>Aigua i salut.</b> Per què és important que hi hagi normes de qualitat de l'aigua de l'aixeta? Busca d'on prové l'aigua de l'aixeta de Barcelona i cita la font.", criteria: "Relaciona normes de qualitat i salut; origen (Ter, Llobregat, aqüífers, dessalinitzadora) amb font citada." },
    { type: "h", text: "C · Per al debat de la sessió 7" },
    { id: "6", type: "text", lines: 4, prompt: "<b>Una científica poc coneguda.</b> El treball d'Ellen va millorar la salut de milions de persones, però avui poca gent en coneix el nom. Escriu dues possibles raons a partir del text i del context de l'època.", criteria: "Proposa raons basades en el text i el context (poques dones a la universitat, reconeixement desigual, «experiment»)." },
  ],
},

};
