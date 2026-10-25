/* Adaptacions de les fitxes per perfil (NESE). El perfil l'assigna el docent des de «Alumnat i codis».
   FQAdapt.apply(host, clau, perfils, {mode}) s'aplica després de FQFitxa.render.
   Dades: window.FQ_ADAPT (digital/js/adaptacions-dades.js, generat de contingut/3r/adaptacions.yaml).
   Criteris: document «Adaptacions del llibre digital: criteris per perfil».
   Continguts bàsics rebaixa l'exigència: treu preguntes (treu) i redueix apartats (redueix). Aquestes preguntes no s'avaluen
   i el nivell màxim de l'alumne és AS (FQStore aplica el topall). Els altres perfils mai no treuen cap pregunta. */
(function (G) {
  "use strict";
  const A = () => G.FQ_ADAPT || { perfils: [], glossari: {}, fitxes: {} };
  const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const sdaOf = (k) => { const m = /^d(\d)/.exec(k); if (m) return +m[1]; const F = G.FITXES || {}; return (F[k] && F[k].sda) || 2; };

  /* perfils que s'apliquen a aquesta fitxa: els de l'alumne menys els marcats «no_cal» */
  function effective(k, perfils) {
    const dec = A().fitxes[k] || {};
    return (perfils || []).filter((p) => dec[p] !== "no_cal");
  }
  const variant = (k, p) => { const x = (A().fitxes[k] || {})[p]; return x && typeof x === "object" ? x : null; };

  function css() {
    if (document.getElementById("adcss")) return;
    const l = document.createElement("link"); l.rel = "stylesheet"; l.href = "https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap"; document.head.appendChild(l);
    const st = document.createElement("style"); st.id = "adcss";
    st.textContent = `
.ad-dis .ws,.ad-dis .ws *:not(.ML__latex *):not(math-field){font-family:"Atkinson Hyperlegible",Verdana,sans-serif!important}
.ad-dis .ws{box-sizing:border-box;max-width:100%;line-height:1.9;letter-spacing:.05em;word-spacing:.16em;background:#fdf8ea;color:#1f2328;border-radius:14px;padding:14px}
.ad-dis .ws :is(p,div,span,td,th,li,label,b,strong,em,i,a,textarea,input,select,output,h3,h4,small,button):not(.uf span):not(.ML__latex *):not(.katex *):not(.n){font-size:1.3rem!important;line-height:1.9!important}
.ad-dis .ws h2{font-size:1.5rem!important}
.ad-dis .ws p,.ad-dis .ws .q,.ad-dis .ws .tip,.ad-dis .ws td,.ad-dis .ws li{text-align:left!important}
.ad-dis .ws em,.ad-dis .ws i{font-style:normal!important;font-weight:700}
.ad-dis .ws textarea,.ad-dis .ws input{padding:8px 10px!important}
.ad-dis .ws .tip,.ad-dis .ws .ad-card,.ad-dis .ws-block{background:#fffdf6!important;color:#1f2328}
.ad-bas .ws :is(p,div,span,td,th,li,label,b,strong,em,i,a,textarea,input,select,output,h3,h4,small,button):not(.uf span):not(.ML__latex *):not(.katex *):not(.n){font-size:1.12rem!important;line-height:1.75!important}
.ad-bas .ws-block{padding-top:6px;padding-bottom:6px}
.ad-paper .ws :is(p,div,span,td,th,li,label,b,strong,em,i,a,textarea,input,select,output,h3,h4,small,button):not(.uf span):not(.ML__latex *):not(.katex *):not(.n){font-size:1.15rem!important}
.ad-paper.ad-dis .ws :is(p,div,span,td,th,li,label,b,strong,em,i,a,textarea,input,select,output,h3,h4,small,button):not(.uf span):not(.ML__latex *):not(.katex *):not(.n){font-size:1.35rem!important}
.ad-tts{display:inline-flex;align-items:center;gap:4px;border:1px solid var(--line);background:var(--surface);color:var(--fg);border-radius:999px;padding:2px 10px;font:inherit;font-size:.8rem;cursor:pointer;margin:4px 0}
.ad-tts[aria-pressed=true]{background:var(--acc);color:#fff;border-color:var(--acc)}
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;margin:0 .15em;line-height:1.15}.fr>span{padding:0 .2em}.fr>span+span{border-top:1.5px solid currentColor}
.ad-redueix{border-width:2.5px!important;background:color-mix(in srgb,var(--acc) 14%,var(--surface))!important}
.ad-card{box-sizing:border-box;max-width:100%;overflow-wrap:anywhere;border:1.5px solid var(--acc);border-radius:12px;padding:10px 14px;margin:8px 0;background:color-mix(in srgb,var(--acc) 6%,var(--surface))}
.ad-card h4{margin:0 0 6px;font-size:.95rem}
.ad-card ul,.ad-card ol{margin:4px 0 0;padding-left:1.3em}
.ad-gl{all:unset;cursor:pointer;border-bottom:2px dotted var(--acc);font-weight:600}
.ad-pop{position:absolute;z-index:50;max-width:320px;background:var(--surface);color:var(--fg);border:1.5px solid var(--acc);border-radius:10px;padding:10px 12px;box-shadow:0 8px 24px rgba(0,0,0,.18);font-size:.9rem;line-height:1.4}
.ad-pop b{display:block;margin-bottom:2px}.ad-pop .tr{color:var(--muted);margin-top:4px}
.ad-gltab{width:100%;border-collapse:collapse;font-size:.88rem}.ad-gltab td,.ad-gltab th{border:1px solid var(--line);padding:3px 6px;text-align:left}
.ad-pista{margin:4px 6px 0 0}.ad-pistatxt{margin:6px 0 0;padding:6px 10px;border-left:3px solid var(--acc);background:var(--surface)}
.ad-calc{position:fixed;right:16px;bottom:16px;z-index:60;background:var(--surface);border:1.5px solid var(--acc);border-radius:12px;padding:10px;box-shadow:0 8px 24px rgba(0,0,0,.2);display:grid;gap:6px;width:min(260px,calc(100vw - 32px))}
.ad-calc input{font:inherit;font-size:1.1rem;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--fg)}
.ad-calc .r{font-size:1.2rem;font-weight:700;min-height:1.4em}
.ad-tdah [data-adpage][hidden]{display:none!important}
.ad-nav{position:sticky;top:0;z-index:20;display:flex;flex-wrap:wrap;gap:8px;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:8px 10px;margin:6px 0}
.ad-nav .bar{flex:1 1 120px;height:8px;border-radius:99px;background:var(--chip);overflow:hidden}.ad-nav .bar i{display:block;height:100%;background:var(--acc)}
.ad-nav .tm{font-variant-numeric:tabular-nums;color:var(--muted);font-size:.85rem}
.ad-toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:70;background:var(--fg);color:var(--surface);border-radius:999px;padding:8px 16px;font-size:.9rem}
.ad-num{background:color-mix(in srgb,var(--acc) 18%,transparent);border-radius:4px;padding:0 3px;font-weight:700}.ad-paper .ws-block{margin-bottom:28px}.ad-draw{border:1.5px dashed var(--line);border-radius:10px;min-height:60mm;color:var(--muted);padding:6px 10px;font-size:.85rem}.ad-paper .ad-steps li{margin-bottom:6px}
@media print{html{font-size:12pt}.ad-paper .ws :is(p,div,span,td,th,li,label,b,strong,em,i,a,textarea,input,select,output,h3,h4,small,button):not(.uf span):not(.ML__latex *):not(.katex *):not(.n){font-size:13pt!important}.ad-paper.ad-dis .ws :is(p,div,span,td,th,li,label,b,strong,em,i,a,textarea,input,select,output,h3,h4,small,button):not(.uf span):not(.ML__latex *):not(.katex *):not(.n){font-size:15pt!important;line-height:1.9!important}.ad-paper textarea{min-height:28mm}.ad-dis .ws{background:none!important;padding:0}.wsnote,.ad-tts,.ad-nav,.ad-calc,.ad-noprint,.ad-pista{display:none!important}.ad-gl{border:0;font-weight:700}}`;
    document.head.appendChild(st);
  }

  /* ---------- peces comunes ---------- */
  const questions = (host) => [...host.querySelectorAll("[data-qblock], .ws > section.ws-block")].filter((q) => !q.classList.contains("ad-treu"));
  /* continguts bàsics: preguntes que no ha de fer i apartats reduïts */
  function treu(k, perfils) { if (!effective(k, perfils).includes("basics")) return []; const v = variant(k, "basics"); return ((v && v.treu) || []).map(String); }
  function redueix(k, perfils) { if (!effective(k, perfils).includes("basics")) return {}; const v = variant(k, "basics"); return (v && v.redueix) || {}; }
  const HINT_BAS = "Alumne amb adaptació de continguts bàsics: valora només el contingut bàsic de la pregunta, amb criteris rebaixats. El nivell màxim és AS (no posis mai AN ni AE).";
  /* ítems per a la correcció automàtica: sense les preguntes tretes i amb el criteri rebaixat */
  function forAuto(k, perfils, items) {
    if (!effective(k, perfils).includes("basics")) return items;
    const T = new Set(treu(k, perfils)); const R = redueix(k, perfils);
    return items.filter((it) => !T.has(String(it.id))).map((it) => ({ ...it, criteria: [it.criteria, R[it.id] ? "Només s'ha de fer: " + R[it.id].replace(/<[^>]+>/g, "") : "", HINT_BAS].filter(Boolean).join(" ") }));
  }
  function hideTreu(host, k, perfils) {
    const T = treu(k, perfils); const R = redueix(k, perfils);
    T.forEach((id) => {
      const el = host.querySelector(`[data-qblock="${CSS.escape(id)}"]`) || host.querySelector(`.ws-block[data-block="${CSS.escape(id)}"]`) || host.querySelector(`.ws-item[data-item="${CSS.escape(id)}"]`);
      if (el) { el.classList.add("ad-treu"); el.hidden = true; }
    });
    Object.entries(R).forEach(([id, txt]) => {
      const sec = host.querySelector(`[data-qblock="${CSS.escape(id)}"]`) || host.querySelector(`.ws-block[data-block="${CSS.escape(id)}"]`); if (!sec) return;
      const c = card("Què has de fer", txt, "ad-redueix"); const p = afterQ(sec); if (p && p !== sec) p.after(c); else sec.prepend(c);
    });
  }
  const qid = (sec) => sec.dataset.qblock || sec.dataset.block || ((sec.querySelector(".ws-item") || {}).dataset || {}).item || "";
  const promptEl = (sec) => sec.querySelector(":scope > .q > div, :scope .ws-q > div");
  /* lloc on s'afegeixen les ajudes: just després de l'enunciat, a l'amplada de la pregunta */
  /* insereix una ajuda just abans del primer camp de resposta de la pregunta (o, si no n'hi ha, després de l'enunciat) */
  function place(sec, node) {
    const f = sec.querySelector(".work, .ws-math, .ws-chain, .ws-scroll, table:not(.ad-gltab), textarea, select, input:not([type=checkbox]):not([type=radio]), .ws-photos");
    if (f && !f.closest(".ad-card")) { const anchor = f.closest(".ws-item") && f.closest(".ws-item") !== sec ? f.closest(".ws-item") : f; anchor.before(node); }
    else afterQ(sec).after(node);
  }
  const afterQ = (sec) => { const p = promptEl(sec); return (p && p.closest(".q, .ws-q")) || p || sec; };
  function plain(el) {
    if (!el) return "";
    const c = el.cloneNode(true);
    c.querySelectorAll("input,textarea,select,math-field,button,.work,.ws-photos,svg").forEach((x) => x.remove());
    return c.textContent.replace(/\s+/g, " ").trim();
  }
  function speakBtn(text) {
    const b = document.createElement("button"); b.type = "button"; b.className = "ad-tts ad-noprint"; b.setAttribute("aria-pressed", "false");
    b.innerHTML = "🔊 <span>Escolta</span>";
    b.onclick = () => {
      if (!G.speechSynthesis) return;
      if (G.speechSynthesis.speaking) { G.speechSynthesis.cancel(); document.querySelectorAll(".ad-tts[aria-pressed=true]").forEach((x) => x.setAttribute("aria-pressed", "false")); if (b.getAttribute("aria-pressed") === "true") return; }
      const u = new SpeechSynthesisUtterance(text); u.lang = "ca-ES"; u.rate = 0.92;
      const v = G.speechSynthesis.getVoices(); u.voice = v.find((x) => /^ca/i.test(x.lang)) || v.find((x) => /^es/i.test(x.lang)) || null;
      u.onend = () => b.setAttribute("aria-pressed", "false"); b.setAttribute("aria-pressed", "true"); G.speechSynthesis.speak(u);
    };
    return b;
  }
  function card(title, inner, cls = "") { const d = document.createElement("div"); d.className = "ad-card " + cls; d.innerHTML = `<h4>${title}</h4>${inner}`; return d; }
  function toast(t) { const d = document.createElement("div"); d.className = "ad-toast"; d.textContent = t; document.body.appendChild(d); setTimeout(() => d.remove(), 5000); }

  /* ---------- lectura en veu alta (dislèxia, nouvingut) ---------- */
  function tts(host) {
    const ws = host.querySelector(".ws"); if (!ws) return;
    ws.querySelectorAll(":scope > .tip, :scope > .ws-tip").forEach((t) => t.prepend(speakBtn(plain(t))));
    questions(host).forEach((sec) => { const p = promptEl(sec); if (p) p.prepend(speakBtn(plain(p))); });
  }

  /* ---------- glossari (nouvingut) ---------- */
  function glossari(host, k, paper, idioma) {
    const LL = (A().llengues || []).find((l) => l.codi === idioma) || null;
    const trOf = (w) => (LL && w.tr && w.tr[LL.codi]) || "";
    const gt = (w) => (LL && LL.traductor ? `https://translate.google.com/?sl=ca&tl=${encodeURIComponent(LL.traductor)}&text=${encodeURIComponent(w.ca)}&op=translate` : "");
    const dir = LL && LL.rtl ? ' dir="rtl"' : "";
    const words = A().glossari[String(sdaOf(k))] || []; if (!words.length) return;
    const ws = host.querySelector(".ws"); if (!ws) return;
    const found = new Set();
    const skip = "input,textarea,select,option,math-field,button,svg,script,style,.ML__latex,.ad-card,.ad-tts";
    const forms = [];
    words.forEach((w, i) => (w.formes || [w.ca]).forEach((f) => forms.push([f, i])));
    forms.sort((a, b) => b[0].length - a[0].length);
    const L = "a-zàáèéíïòóúüç·A-ZÀÁÈÉÍÏÒÓÚÜÇ";
    const re = new RegExp(`(^|[^${L}])(${forms.map(([f]) => f.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|")})(?![${L}])`, "i");
    const tw = document.createTreeWalker(ws, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (n.parentElement && n.parentElement.closest(skip) ? NodeFilter.FILTER_REJECT : n.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP) });
    const nodes = []; while (tw.nextNode()) nodes.push(tw.currentNode);
    nodes.forEach((n) => {
      let txt = n.nodeValue, m, frag = null, guard = 0;
      while ((m = re.exec(txt)) && guard++ < 20) {
        const hit = m[2]; const idx = (forms.find(([f]) => f.toLowerCase() === hit.toLowerCase()) || [])[1];
        if (idx == null || found.has(idx)) { // ja marcada: continua després
          frag = frag || document.createDocumentFragment(); frag.append(txt.slice(0, m.index + m[0].length)); txt = txt.slice(m.index + m[0].length); continue;
        }
        found.add(idx);
        frag = frag || document.createDocumentFragment();
        frag.append(txt.slice(0, m.index + m[1].length));
        const b = document.createElement("button"); b.type = "button"; b.className = "ad-gl"; b.dataset.g = idx; b.textContent = hit; frag.append(b);
        txt = txt.slice(m.index + m[0].length);
      }
      if (frag) { frag.append(txt); n.replaceWith(frag); }
    });
    const list = [...found].sort((a, b) => a - b).map((i) => words[i]);
    const showEs = !LL || LL.codi !== "es";
    const langCell = (w) => { const t = trOf(w); if (t) return `<td${dir}>${esc(t)}</td>`; const u = gt(w); return `<td>${u && !paper ? `<a href="${u}" target="_blank" rel="noopener">Tradueix ↗</a>` : ""}</td>`; };
    if (list.length) ws.prepend(card("Paraules clau d'aquesta fitxa", `<table class="ad-gltab"><thead><tr><th>Català</th>${LL ? `<th>${esc(LL.nom)}</th>` : "<th>La meva llengua</th>"}${showEs ? "<th>Castellà</th>" : ""}</tr></thead><tbody>${list.map((w) => `<tr><td><b>${esc(w.ca)}</b></td>${LL ? langCell(w) : "<td></td>"}${showEs ? `<td>${esc((w.tr || {}).es || "")}</td>` : ""}</tr>`).join("")}</tbody></table>${LL && !paper ? '<p class="note ad-noprint">Les traduccions les revisa l\'aula d\'acollida. Si no hi ha traducció, prem «Tradueix».</p>' : ""}`));
    if (paper) return;
    let pop = null;
    host.addEventListener("click", (e) => {
      const b = e.target.closest(".ad-gl");
      if (pop) { pop.remove(); pop = null; }
      if (!b) return;
      const w = words[+b.dataset.g]; const r = b.getBoundingClientRect();
      pop = document.createElement("div"); pop.className = "ad-pop"; pop.setAttribute("role", "dialog");
      const t = trOf(w), u = gt(w);
      pop.innerHTML = `<b>${esc(w.ca)}</b>${esc(w.def)}${LL ? `<div class="tr">${esc(LL.nom)}: ${t ? `<span${dir}>${esc(t)}</span>` : "—"}${u ? ` · <a href="${u}" target="_blank" rel="noopener">Tradueix ↗</a>` : ""}</div>` : ""}<div class="tr">Castellà: ${esc((w.tr || {}).es || "")}</div>`;
      pop.append(speakBtn(`${w.ca}. ${w.def}`));
      document.body.appendChild(pop);
      pop.style.left = Math.max(8, Math.min(r.left + G.scrollX, G.scrollX + document.documentElement.clientWidth - pop.offsetWidth - 8)) + "px";
      pop.style.top = r.bottom + G.scrollY + 6 + "px";
    });
  }

  /* ---------- versió escrita a mà (continguts bàsics, nouvingut, TEA, discalcúlia): continguts afegits per pregunta ---------- */
  function variants(host, k, perfils, paper) {
    const ws = host.querySelector(".ws"); if (!ws) return;
    perfils.forEach((p) => {
      const v = variant(k, p); if (!v) return;
      if (v.abans) ws.prepend(card(v.abans_titol || "Abans de començar", v.abans));
      const Q = v.preguntes || {};
      questions(host).forEach((sec) => {
        const x = Q[qid(sec)]; if (!x) return;
        const p0 = afterQ(sec);
        if (x.exemple) place(sec, card("Exemple resolt", x.exemple));
        if (x.passos) place(sec, card("Fes-ho per passos", `<ol class="ad-steps">${x.passos.map((s) => `<li>${s}</li>`).join("")}</ol>`));
        if (x.frases) place(sec, card("Frases que t'ajuden", `<ul>${x.frases.map((s) => `<li>${s}</li>`).join("")}</ul>${x.paraules ? `<p><b>Paraules:</b> ${x.paraules.map(esc).join(" · ")}</p>` : ""}`));
        if (x.model) place(sec, card("Com ha de ser la resposta", x.model));
        if (x.pistes && paper) place(sec, card("Pistes", `<ol class="ad-steps">${x.pistes.map((t) => `<li>${t}</li>`).join("")}</ol>`));
        else if (x.pistes) {
          const c = card("Necessites ajuda?", "");
          x.pistes.forEach((t, i) => { const b = document.createElement("button"); b.type = "button"; b.className = "btn ghost ad-pista"; b.textContent = `Pista ${i + 1}`; b.disabled = i > 0;
            b.onclick = () => { b.disabled = true; const d = document.createElement("div"); d.className = "ad-pistatxt"; d.innerHTML = t; c.append(d); const nx = c.querySelectorAll(".ad-pista")[i + 1]; if (nx) nx.disabled = false; }; c.append(b); });
          place(sec, c);
        }
      });
    });
  }


  /* ---------- continguts bàsics (automàtic): com respondre cada tipus de pregunta i vocabulari en català ---------- */
  const GUIA = [
    [/\b(calcula|quin volum|quina pressió|quina temperatura|quina massa|quant|a quina|quina velocitat|quina energia|quina distància)/i, "Fes-ho per passos", "<ol class=\"ad-steps\"><li>Escriu les <b>dades</b> amb les unitats.</li><li>Tria la <b>fórmula</b> (mira el formulari o la teoria de la fitxa).</li><li><b>Substitueix</b> els números a la fórmula.</li><li><b>Calcula</b>.</li><li>Escriu el <b>resultat amb la unitat</b>.</li></ol>"],
    [/\b(explica|justifica|per què|argumenta|raona)/i, "Com respondre", "<ol class=\"ad-steps\"><li>Digues <b>què passa</b>.</li><li>Digues <b>per què</b>, amb la idea principal del tema.</li><li>Fes servir una <b>paraula clau</b> de la fitxa.</li></ol><p>Pots començar així: «Passa que … perquè …».</p>"],
    [/\b(completa|omple)/i, "Com fer-ho", "<p>Mira l'exemple o la primera fila. Després fes el mateix a cada casella, d'una en una.</p>"],
    [/\b(dibuixa|representa|gràfica|fes un esquema)/i, "Com fer el dibuix o la gràfica", "<ol class=\"ad-steps\"><li>Posa el <b>nom</b> i la <b>unitat</b> a cada eix o a cada part.</li><li>Tria una <b>escala</b> que hi càpiga.</li><li>Marca els <b>punts</b> o dibuixa les parts.</li><li>Revisa que es pugui entendre.</li></ol>"],
    [/\b(compara|diferència|semblances)/i, "Com comparar", "<p>Digues en què <b>s'assemblen</b> i en què <b>es diferencien</b>. Pots començar així: «Els dos … però …».</p>"],
    [/\b(classifica|ordena|relaciona)/i, "Com fer-ho", "<p>Llegeix cada element i pensa a quin grup va. Fes-ho d'un en un i comprova-ho al final.</p>"],
  ];
  function basicsAuto(host, k) {
    const v = variant(k, "basics"); const Q = (v && v.preguntes) || {};
    questions(host).forEach((sec) => {
      if (Q[qid(sec)]) return;
      const t = plain(promptEl(sec) || sec); const g = GUIA.find(([re]) => re.test(t)); if (!g) return;
      place(sec, card(g[1], g[2], "ad-bascard"));
    });
  }
  function vocabCa(host, k) {
    const words = A().glossari[String(sdaOf(k))] || []; const ws = host.querySelector(".ws"); if (!ws || !words.length) return;
    const txt = ws.textContent.toLowerCase();
    const list = words.filter((w) => (w.formes || [w.ca]).some((f) => txt.includes(f.toLowerCase())));
    if (list.length) ws.prepend(card("Paraules que t'ajuden", `<ul>${list.map((w) => `<li><b>${esc(w.ca)}:</b> ${esc(w.def)}</li>`).join("")}</ul>`));
  }
  /* discalcúlia: ressalta les dades numèriques (número + unitat) de l'enunciat */
  function markNums(el) {
    if (!el) return;
    const re = /(−|-)?\d+(?:[.,]\d+)?(?:\s?(?:°C|K|atm|bar|mL|cm³|dm³|m³|L|km\/h|m\/s²|m\/s|kWh|km|cm|mm|µm|m|kg|mg|g|min|h|s|N|J|W|Pa|%))?/g;
    const tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (n.parentElement.closest("input,textarea,math-field,button,.ad-card,.ML__latex,.uf,.n") ? NodeFilter.FILTER_REJECT : /\d/.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP) });
    const ns = []; while (tw.nextNode()) ns.push(tw.currentNode);
    ns.forEach((n) => { const t = n.nodeValue; if (t.includes("\\(")) return; const h = esc(t).replace(re, (m) => `<span class="ad-num">${m}</span>`); if (h === esc(t)) return; const sp = document.createElement("span"); sp.innerHTML = h; n.replaceWith(...sp.childNodes); });
  }
  /* ---------- discalcúlia: taula de passos i calculadora a les preguntes de càlcul ---------- */
  const isCalc = (sec) => !!sec.querySelector(".work, .wl-math, .ws-math, .ws-chain, input[inputmode=decimal]") && /\d/.test(plain(promptEl(sec) || sec));
  function discalculia(host, paper, K) {
    let any = false;
    questions(host).forEach((sec) => {
      if (!isCalc(sec)) return; any = true;
      markNums(promptEl(sec));
      const vq = ((variant(K, "discalculia") || {}).preguntes || {})[qid(sec)] || ((variant(K, "basics") || {}).preguntes || {})[qid(sec)];
      if (vq && vq.passos) return;
      if ([...sec.querySelectorAll(".ad-bascard h4")].some((h) => h.textContent === "Fes-ho per passos")) return;
      place(sec, card("Taula de passos", `<ol class="ad-steps"><li><b>Dades:</b> escriu cada dada amb la seva unitat.</li><li><b>Fórmula:</b> quina fórmula fas servir?</li><li><b>Substitueix:</b> posa els números a la fórmula.</li><li><b>Opera:</b> fes el càlcul${paper ? " amb la calculadora" : " (pots fer servir la calculadora)"}.</li><li><b>Resultat:</b> escriu el número amb la unitat. Té sentit?</li></ol>`));
    });
    if (!any || paper || document.querySelector(".ad-calc-open")) return;
    const ws = host.querySelector(".ws");
    const b = document.createElement("button"); b.type = "button"; b.className = "btn ghost ad-calc-open ad-noprint"; b.textContent = "🧮 Calculadora";
    b.onclick = () => {
      let c = document.querySelector(".ad-calc"); if (c) { c.remove(); return; }
      c = document.createElement("div"); c.className = "ad-calc"; c.setAttribute("role", "dialog"); c.setAttribute("aria-label", "Calculadora");
      c.innerHTML = `<b>Calculadora</b><input aria-label="Operació" placeholder="p. ex. 0,25 * 20" inputmode="decimal"><div class="r" aria-live="polite"></div><small class="note">Fes servir + − * / i parèntesis. La coma i el punt són decimals.</small><button type="button" class="btn ghost">Tanca</button>`;
      const inp = c.querySelector("input"), out = c.querySelector(".r");
      inp.oninput = () => { const e = inp.value.replace(/,/g, ".").replace(/[×·]/g, "*").replace(/÷/g, "/").replace(/−/g, "-"); if (!/^[\d.+\-*/()\s^e]+$/.test(e)) { out.textContent = ""; return; } try { const v = Function(`"use strict";return (${e.replace(/\^/g, "**")})`)(); out.textContent = isFinite(v) ? "= " + String(+v.toPrecision(10)).replace(".", ",") : ""; } catch { out.textContent = ""; } };
      c.querySelector("button").onclick = () => c.remove(); document.body.appendChild(c); inp.focus();
    };
    if (ws) ws.prepend(b);
  }

  /* ---------- TDAH: una pregunta per pantalla, progrés, temporitzador i pauses ---------- */
  let tdahTimer = null;
  function tdah(host, paper) {
    if (paper) return;
    const qs = questions(host); if (qs.length < 2) return;
    host.classList.add("ad-tdah");
    qs.forEach((q, i) => (q.dataset.adpage = i));
    const nav = document.createElement("div"); nav.className = "ad-nav ad-noprint";
    nav.innerHTML = `<button type="button" class="btn ghost" data-adprev>← Anterior</button><span><b data-adn></b> de ${qs.length}</span><span class="bar"><i data-adbar></i></span><span class="tm" data-adtm>0:00</span><button type="button" class="btn" data-adnext>Següent →</button>`;
    const ws = host.querySelector(".ws"); ws.prepend(nav);
    let cur = 0;
    const show = (i) => { cur = Math.max(0, Math.min(qs.length - 1, i)); qs.forEach((q, j) => (q.hidden = j !== cur)); nav.querySelector("[data-adn]").textContent = `Pregunta ${cur + 1}`; nav.querySelector("[data-adbar]").style.width = ((cur + 1) / qs.length) * 100 + "%"; nav.querySelector("[data-adprev]").disabled = cur === 0; const nx = nav.querySelector("[data-adnext]"); nx.textContent = cur === qs.length - 1 ? "Has acabat ✓" : "Següent →"; nx.disabled = cur === qs.length - 1; nav.scrollIntoView({ block: "nearest" }); };
    nav.querySelector("[data-adprev]").onclick = () => show(cur - 1);
    nav.querySelector("[data-adnext]").onclick = () => show(cur + 1);
    show(0);
    clearInterval(tdahTimer); const t0 = Date.now(); let lastPause = 0;
    tdahTimer = setInterval(() => {
      if (!document.body.contains(nav)) { clearInterval(tdahTimer); return; }
      const s = Math.floor((Date.now() - t0) / 1000); nav.querySelector("[data-adtm]").textContent = `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
      if (s - lastPause >= 12 * 60) { lastPause = s; toast("Fes una pausa activa d'un minut: aixeca't, estira't i torna."); }
    }, 1000);
  }

  /* ---------- TEA: guia anticipada ---------- */
  function tea(host, k, paper) {
    const F = (G.FITXES || {})[k] || {}; const n = questions(host).length;
    const mins = /(\d+)\s*min/.exec(F.intro || ""); const ses = /Sessi[óo] (\d+)/.exec(F.intro || "");
    const ws = host.querySelector(".ws"); if (!ws) return;
    ws.prepend(card("Què passarà en aquesta fitxa", `<ul>
      <li><b>Què farem:</b> ${esc(F.title || "la fitxa")}${ses ? ` (sessió ${ses[1]})` : ""}.</li>
      <li><b>Quantes preguntes:</b> ${n || "les que veuràs a sota"}. Les fem en ordre, una darrere l'altra.</li>
      <li><b>Quant de temps:</b> ${mins ? mins[1] + " minuts" : "una sessió de classe"}. Si no l'acabes, la pots acabar a casa.</li>
      <li><b>Què he d'entregar:</b> ${paper ? "el full fet, al professor." : "quan acabis, prem el botó «Lliura la fitxa». Les respostes es desen soles."}</li>
      <li><b>Si necessito parar:</b> aixeca la targeta de pausa o avisa el professor.</li></ul>`));
  }

  /* ajudes que l'alumne pot desactivar; continguts bàsics no en té (només el docent el decideix) */
  const AJUDA_NOM = { lletra: "Lletra fàcil de llegir", veu: "Lectura en veu alta", glossari: "Paraules clau i traducció", passos: "Taula de passos i calculadora", pantalla: "Una pregunta per pantalla", guia: "Guia de la fitxa" };
  const AJUDA_PERFIL = { lletra: ["dislexia"], veu: ["dislexia", "nouvingut"], glossari: ["nouvingut"], passos: ["discalculia"], pantalla: ["tdah"], guia: ["tea"] };
  const PERFIL_AJUDA = { dislexia: "lletra", nouvingut: "glossari", discalculia: "passos", tdah: "pantalla", tea: "guia" };
  function aids(k, perfils) { const P = effective(k, perfils); return Object.keys(AJUDA_PERFIL).filter((a) => AJUDA_PERFIL[a].some((p) => P.includes(p))); }
  function apply(host, k, perfils, opts = {}) {
    const P = effective(k, perfils); if (!P.length || !host) return [];
    css();
    const paper = opts.mode === "paper";
    const off = new Set(opts.off || []);
    const on = (a) => aids(k, perfils).includes(a) && !off.has(a);
    host.classList.toggle("ad-paper", paper);
    if (paper) host.querySelectorAll(".muted").forEach((m) => { if (/sense foto/.test(m.textContent)) m.outerHTML = '<div class="ad-draw">Dibuixa-ho aquí</div>'; });
    if (on("lletra")) host.classList.add("ad-dis");
    if (P.includes("basics")) { hideTreu(host, k, perfils); host.classList.add("ad-bas"); basicsAuto(host, k); if (!on("glossari")) vocabCa(host, k); }
    variants(host, k, P.filter((p) => p === "basics" || !PERFIL_AJUDA[p] || on(PERFIL_AJUDA[p])), paper);
    if (on("passos")) discalculia(host, paper, k);
    if (on("glossari")) glossari(host, k, paper, opts.idioma);
    if (!paper && on("veu")) tts(host);
    if (on("guia")) tea(host, k, paper);
    if (on("pantalla")) tdah(host, paper);
    return P;
  }

  G.FQAdapt = { apply, effective, aids, AJUDA_NOM, treu, redueix, forAuto };
})(window);
