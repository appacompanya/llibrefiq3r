/* Adaptacions de les fitxes per perfil (NESE). El perfil l'assigna el docent des de «Alumnat i codis».
   FQAdapt.apply(host, clau, perfils, {mode}) s'aplica després de FQFitxa.render.
   Dades: window.FQ_ADAPT (digital/js/adaptacions-dades.js, generat de contingut/3r/adaptacions.yaml).
   Criteris: document «Adaptacions del llibre digital: criteris per perfil». Mai no es treu cap pregunta avaluable. */
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
.ad-dis .ws,.ad-dis .ws *{font-family:"Atkinson Hyperlegible",Verdana,sans-serif!important}
.ad-dis .ws{font-size:1.12em;line-height:1.8;letter-spacing:.02em;word-spacing:.08em}
.ad-dis .ws p,.ad-dis .ws .q,.ad-dis .ws .tip,.ad-dis .ws td{text-align:left!important}
.ad-dis .ws b{font-weight:700}
.ad-tts{display:inline-flex;align-items:center;gap:4px;border:1px solid var(--line);background:var(--surface);color:var(--fg);border-radius:999px;padding:2px 10px;font:inherit;font-size:.8rem;cursor:pointer;margin:4px 0}
.ad-tts[aria-pressed=true]{background:var(--acc);color:#fff;border-color:var(--acc)}
.ad-card{border:1.5px solid var(--acc);border-radius:12px;padding:10px 14px;margin:8px 0;background:color-mix(in srgb,var(--acc) 6%,var(--surface))}
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
.ad-paper .ws-block{margin-bottom:28px}.ad-draw{border:1.5px dashed var(--line);border-radius:10px;min-height:60mm;color:var(--muted);padding:6px 10px;font-size:.85rem}.ad-paper .ad-steps li{margin-bottom:6px}
@media print{.wsnote,.ad-tts,.ad-nav,.ad-calc,.ad-noprint,.ad-pista{display:none!important}.ad-gl{border:0;font-weight:700}}`;
    document.head.appendChild(st);
  }

  /* ---------- peces comunes ---------- */
  const questions = (host) => [...host.querySelectorAll("[data-qblock], .ws > section.ws-block")];
  const qid = (sec) => sec.dataset.qblock || sec.dataset.block || ((sec.querySelector(".ws-item") || {}).dataset || {}).item || "";
  const promptEl = (sec) => sec.querySelector(":scope > .q > div, :scope .ws-q > div");
  /* lloc on s'afegeixen les ajudes: just després de l'enunciat, a l'amplada de la pregunta */
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
  function glossari(host, k, paper) {
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
    if (list.length) ws.prepend(card("Paraules clau d'aquesta fitxa", `<table class="ad-gltab"><thead><tr><th>Català</th><th>Castellà</th><th>Anglès</th>${paper ? "<th>La meva llengua</th>" : ""}</tr></thead><tbody>${list.map((w) => `<tr><td><b>${esc(w.ca)}</b></td><td>${esc(w.es)}</td><td>${esc(w.en)}</td>${paper ? "<td></td>" : ""}</tr>`).join("")}</tbody></table>`));
    if (paper) return;
    let pop = null;
    host.addEventListener("click", (e) => {
      const b = e.target.closest(".ad-gl");
      if (pop) { pop.remove(); pop = null; }
      if (!b) return;
      const w = words[+b.dataset.g]; const r = b.getBoundingClientRect();
      pop = document.createElement("div"); pop.className = "ad-pop"; pop.setAttribute("role", "dialog");
      pop.innerHTML = `<b>${esc(w.ca)}</b>${esc(w.def)}<div class="tr">Castellà: ${esc(w.es)} · Anglès: ${esc(w.en)}</div>`;
      pop.append(speakBtn(`${w.ca}. ${w.def}`));
      document.body.appendChild(pop);
      pop.style.left = Math.max(8, Math.min(r.left + G.scrollX, G.scrollX + document.documentElement.clientWidth - pop.offsetWidth - 8)) + "px";
      pop.style.top = r.bottom + G.scrollY + 6 + "px";
    });
  }

  /* ---------- versió escrita a mà (continguts bàsics, nouvingut, TEA, discalcúlia): continguts afegits per pregunta ---------- */
  function variants(host, k, perfils) {
    const ws = host.querySelector(".ws"); if (!ws) return;
    perfils.forEach((p) => {
      const v = variant(k, p); if (!v) return;
      if (v.abans) ws.prepend(card(v.abans_titol || "Abans de començar", v.abans));
      const Q = v.preguntes || {};
      questions(host).forEach((sec) => {
        const x = Q[qid(sec)]; if (!x) return;
        const p0 = afterQ(sec);
        if (x.exemple) p0.after(card("Exemple resolt", x.exemple));
        if (x.passos) p0.after(card("Fes-ho per passos", `<ol class="ad-steps">${x.passos.map((s) => `<li>${s}</li>`).join("")}</ol>`));
        if (x.frases) p0.after(card("Frases que t'ajuden", `<ul>${x.frases.map((s) => `<li>${s}</li>`).join("")}</ul>${x.paraules ? `<p><b>Paraules:</b> ${x.paraules.map(esc).join(" · ")}</p>` : ""}`));
        if (x.model) p0.after(card("Com ha de ser la resposta", x.model));
        if (x.pistes) {
          const c = card("Necessites ajuda?", "");
          x.pistes.forEach((t, i) => { const b = document.createElement("button"); b.type = "button"; b.className = "btn ghost ad-pista"; b.textContent = `Pista ${i + 1}`; b.disabled = i > 0;
            b.onclick = () => { b.disabled = true; const d = document.createElement("div"); d.className = "ad-pistatxt"; d.innerHTML = t; c.append(d); const nx = c.querySelectorAll(".ad-pista")[i + 1]; if (nx) nx.disabled = false; }; c.append(b); });
          p0.after(c);
        }
      });
    });
  }

  /* ---------- discalcúlia: taula de passos i calculadora a les preguntes de càlcul ---------- */
  const isCalc = (sec) => !!sec.querySelector(".work, .wl-math, .ws-math, .ws-chain, input[inputmode=decimal]") && /\d/.test(plain(promptEl(sec) || sec));
  function discalculia(host, paper) {
    let any = false;
    questions(host).forEach((sec) => {
      if (!isCalc(sec)) return; any = true;
      const p0 = afterQ(sec);
      p0.after(card("Taula de passos", `<ol class="ad-steps"><li><b>Dades:</b> escriu cada dada amb la seva unitat.</li><li><b>Fórmula:</b> quina fórmula fas servir?</li><li><b>Substitueix:</b> posa els números a la fórmula.</li><li><b>Opera:</b> fes el càlcul${paper ? " amb la calculadora" : " (pots fer servir la calculadora)"}.</li><li><b>Resultat:</b> escriu el número amb la unitat. Té sentit?</li></ol>`));
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

  function apply(host, k, perfils, opts = {}) {
    const P = effective(k, perfils); if (!P.length || !host) return [];
    css();
    const paper = opts.mode === "paper";
    host.classList.toggle("ad-paper", paper);
    if (paper) host.querySelectorAll(".muted").forEach((m) => { if (/sense foto/.test(m.textContent)) m.outerHTML = '<div class="ad-draw">Dibuixa-ho aquí</div>'; });
    if (P.includes("dislexia")) host.classList.add("ad-dis");
    variants(host, k, P);
    if (P.includes("discalculia")) discalculia(host, paper);
    if (P.includes("nouvingut")) glossari(host, k, paper);
    if (!paper && (P.includes("dislexia") || P.includes("nouvingut"))) tts(host);
    if (P.includes("tea")) tea(host, k, paper);
    if (P.includes("tdah")) tdah(host, paper);
    return P;
  }

  G.FQAdapt = { apply, effective };
})(window);
