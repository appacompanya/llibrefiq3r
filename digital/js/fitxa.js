/* Motor de fitxes interactives */
(function (G) {
  "use strict";
  const U = G.FQUnits;
  const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const UNITS = ["m", "cm", "mm", "km", "µm", "nm", "g", "kg", "mg", "t", "L", "mL", "cL", "dL", "cm³", "dm³", "m³", "s", "min", "h", "m/s", "km/h", "g/mL", "g/cm³", "kg/m³", "g/L", "mg/mL", "mg/L", "g/m³", "mL/s", "L/min", "N", "J", "W", "kWh", "Pa", "K", "mol"];
  const ICON = {
    cam: '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 6.5h3l1.5-2h5L14 6.5h3v9.5H3z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="10" cy="11" r="3" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>',
    x: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    play: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3.5v9l7-4.5z" fill="currentColor"/></svg>',
    pause: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3.5h2v9H5zM9 3.5h2v9H9z" fill="currentColor"/></svg>',
  };
  let unitListAdded = false;
  function ensureUnitList() {
    if (unitListAdded) return; unitListAdded = true;
    const dl = document.createElement("datalist"); dl.id = "fq-units"; dl.innerHTML = UNITS.map((u) => `<option value="${u}">`).join(""); document.body.appendChild(dl);
  }
  /* Unitats compostes com a fracció apilada (g/L -> g sobre L), també dins de les fórmules */
  const UT = "(?:[kKhdcmµμnMG]?(?:g|L|l|m|s|h|min|mol|J|W|N|Pa|atm|bar|K|A|V|Ω|Wh|cal|M)|°C|€)(?:[²³⁻¹]+)?";
  const UP = UT + "(?:·" + UT + ")*";
  const TXT_RE = new RegExp("(^|[^\\w/·.])(" + UP + ")/(\\(" + UP + "\\)|" + UP + ")(?![\\w/²³])", "g");
  const MU = "[A-Za-zµμ°Ω]+(?:\\^\\{?-?\\d\\}?)?", MP = MU + "(?:\\s*\\\\cdot\\s*" + MU + ")*";
  const MATH_RE = new RegExp("\\\\mathrm\\{\\s*(" + MP + ")\\s*/\\s*(\\(\\s*" + MP + "\\s*\\)|" + MP + ")\\s*\\}", "g");
  const unp = (b) => (b[0] === "(" && b[b.length - 1] === ")" ? b.slice(1, -1).trim() : b.trim());
  function fracUnits(root) {
    const skip = "svg,script,style,textarea,input,select,option,math-field,.uf,.ML__latex,.katex,[contenteditable]";
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (n.parentElement && n.parentElement.closest(skip) ? NodeFilter.FILTER_REJECT : /\//.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP) });
    const nodes = []; while (w.nextNode()) nodes.push(w.currentNode);
    nodes.forEach((n) => {
      const parts = n.nodeValue.split(/(\\\(.*?\\\)|\\\[.*?\\\])/s);
      let changed = false;
      const html = parts.map((p) => {
        if (/^\\[\(\[]/.test(p)) { const q = p.replace(MATH_RE, (m, a, b) => "\\dfrac{\\mathrm{" + a.trim() + "}}{\\mathrm{" + unp(b) + "}}"); if (q !== p) changed = true; return esc(q); }
        return p.split(/(\s+)/).map((wd) => {
          if (!wd.includes("/") || /:\/\/|www\./.test(wd)) return esc(wd);
          let out = "", last = 0; TXT_RE.lastIndex = 0; let m;
          while ((m = TXT_RE.exec(wd))) { changed = true; out += esc(wd.slice(last, m.index)) + esc(m[1]) + `<span class="uf"><span>${esc(m[2])}</span><span>${esc(unp(m[3]))}</span></span>`; last = m.index + m[0].length; }
          return out + esc(wd.slice(last));
        }).join("");
      }).join("");
      if (!changed) return;
      const t = document.createElement("template"); t.innerHTML = html; n.replaceWith(t.content);
    });
  }
  /* MathLive interpreta el símbol que segueix \longrightarrow com a etiqueta de la fletxa: es canvia per una fletxa simple */
  function fixArrows(root) {
    const RE = /\\long(right|left|leftright)arrow(\{\})?/g;
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (n.nodeValue.includes("\\long") ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP) });
    const ns = []; while (w.nextNode()) ns.push(w.currentNode);
    ns.forEach((n) => { n.nodeValue = n.nodeValue.replace(RE, (m, d) => "\\;\\" + d + "arrow\\;"); });
  }
  const typeset = (el) => { try { fixArrows(el); } catch {} try { fracUnits(el); } catch {} try { if (G.MathLive && G.MathLive.renderMathInElement) G.MathLive.renderMathInElement(el); } catch {} };
  G.FQFracUnits = fracUnits;

  /* ---------- comprovació automàtica (per a la zona del professorat) ---------- */
  function cellOk(cell, val) {
    if (cell.expected == null || cell.expected === "") return null;
    const v = String(val ?? "").trim(); if (!v) return false;
    if (cell.type === "select") return v === cell.expected;
    if (cell.type === "number") { const a = U.parseNum(v), b = U.parseNum(cell.expected); return isFinite(a) && Math.abs(a - b) <= (cell.tol ?? 0.01) * Math.abs(b) + 1e-12; }
    if (cell.type === "pow10") { const m = String(cell.expected).match(/-?\d+$/); return m && v.replace(/\s/g, "").replace("−", "-") === m[0]; }
    const norm = (s) => s.toLowerCase().replace(/[()\s]/g, "").replace(/³/g, "3").replace(/²/g, "2");
    if (cell.small) return norm(v) === norm(cell.expected) || (cell.expected === "µ" && /^(µ|u|μ)$/i.test(v));
    const sym = (cell.expected.match(/\(([^)]+)\)/) || [])[1];
    return sym ? norm(v).includes(norm(sym)) : norm(v) === norm(cell.expected);
  }
  function sciVal(a) { if (!a) return NaN; return U.parseNum(a.m) * Math.pow(10, parseInt(String(a.e ?? "").replace("−", "-"), 10)); }
  function checkItem(it, ans) {
    if (!ans) return { ok: it.expected != null || it.type === "table" || it.type === "tf" ? false : null };
    switch (it.type) {
      case "chain": { const r = U.sameQuantity(ans.v, ans.u, it.expected.v, it.expected.u, 0.02, it.expected.strict); const c = U.chain(it.start, ans.factors || []); return { ok: r.ok, detail: r.reason, factorsOk: c.checks.every((x) => x === "one") && (ans.factors || []).length > 0 }; }
      case "sci": { const v = sciVal(ans), e = U.parseNum(it.expected); const mant = Math.abs(U.parseNum(ans.m)); return { ok: isFinite(v) && Math.abs(v - e) <= 1e-6 * Math.abs(e), detail: mant >= 10 || mant < 1 ? "mantissa fora de [1,10)" : "" }; }
      case "number": { const a = U.parseNum(ans.text), b = U.parseNum(it.expected); return { ok: isFinite(a) && Math.abs(a - b) <= 1e-6 * Math.abs(b) }; }
      case "math": { const v = sciVal(ans), e = U.parseNum(it.expected); return { ok: isFinite(v) && Math.abs(v - e) <= 1e-6 * Math.abs(e) }; }
      case "table": { let tot = 0, good = 0; it.rows.forEach((r, ri) => r.cells.forEach((c, ci) => { const o = cellOk(c, (ans.cells || {})[`r${ri}c${ci}`]); if (o !== null) { tot++; if (o) good++; } })); return { ok: tot ? good === tot : null, score: tot ? good / tot : null, detail: tot ? `${good}/${tot}` : "" }; }
      case "tf": { let good = 0; it.statements.forEach((s, i) => { if ((ans.ans || {})[i] === s[1]) good++; }); return { ok: good === it.statements.length, detail: `${good}/${it.statements.length}` }; }
      default: return { ok: null };
    }
  }
  function allItems(spec) { const out = []; spec.blocks.forEach((b) => { if (b.type === "group") b.items.forEach((x) => out.push({ ...x, parent: b })); else if (b.id) out.push(b); }); return out; }

  /* ---------- representació ---------- */
  /* text enganxat a cada resposta (només la mida): ajuda el docent a detectar respostes copiades d'una IA */
  function trackPaste(host, answers, save, keyOf) {
    host.addEventListener("paste", (e) => {
      const k = keyOf(e.target); if (!k) return;
      const n = ((e.clipboardData && e.clipboardData.getData("text")) || "").trim().length; if (n < 20) return;
      const p = { ...(answers._paste || {}) }; p[k] = (p[k] || 0) + n; save("_paste", p);
    });
  }
  function render(host, key, opts) {
    ensureUnitList();
    const spec = G.FITXES[key];
    if (spec.html) return renderHtml(host, key, opts); const st = { answers: { ...(opts.answers || {}) }, auto: !!opts.autoCalc, ro: !!opts.readonly };
    const photosByItem = {}; (opts.photos || []).forEach((p) => (photosByItem[p.item || "full"] = photosByItem[p.item || "full"] || []).push(p));
    const fb = {}; (opts.feedback || []).forEach((f) => (fb[f.item_id] = f));
    const dis = st.ro ? " disabled" : "";
    const timers = {};
    function set(id, val) { st.answers[id] = val; if (st.ro) return; clearTimeout(timers[id]); timers[id] = setTimeout(() => opts.onSave && opts.onSave(id, val), 600); }

    const fbHtml = (id) => { const f = fb[id]; if (!f || (!f.level && !f.comment)) return ""; return `<div class="ws-fb">${f.level ? `<span class="lvchip lv-${f.level}">${f.level}</span>` : ""}<span>${esc(f.comment || "")}</span></div>`; };
    const checkHtml = (it) => { if (!opts.showCheck) return ""; const r = checkItem(it, st.answers[it.id]); if (r.ok === null) return ""; return `<span class="ws-chk ${r.ok ? "ok" : "ko"}" title="Comprovació automàtica">${r.ok ? "✓" : "✗"}${r.detail ? " " + esc(r.detail) : ""}</span>`; };
    const photoBtn = (id) => (st.ro && !(photosByItem[id] || []).length) ? "" : `<div class="ws-photos" data-photos="${id}">${(photosByItem[id] || []).map((p) => `<span class="ph" data-path="${esc(p.path)}"><img alt="Foto adjunta" data-src="${esc(p.path)}">${st.ro ? "" : `<button type="button" class="ph-x" aria-label="Treu la foto">${ICON.x}</button>`}</span>`).join("")}${st.ro ? "" : `<label class="ws-cam">${ICON.cam}<span>Afegeix una foto</span><input type="file" accept="image/*" capture="environment" data-photo-item="${id}" hidden></label>`}</div>`;

    function widget(it) {
      const a = st.answers[it.id] || {};
      switch (it.type) {
        case "text": return `<textarea class="ws-text" rows="${it.lines || 3}" data-k="text"${dis}>${esc(a.text || "")}</textarea>`;
        case "number": return `<input class="ws-in num" inputmode="decimal" data-k="text" value="${esc(a.text || "")}" placeholder="valor"${dis}>`;
        case "sci": return `<span class="ws-sci"><input class="ws-in m" inputmode="decimal" data-k="m" value="${esc(a.m || "")}" placeholder="a"${dis}><span>· 10</span><input class="ws-in e sup" inputmode="numeric" data-k="e" value="${esc(a.e || "")}" placeholder="n"${dis}></span><output class="ws-calc" data-calc></output>`;
        case "math": return `<div class="ws-math"><div class="mtools">${st.ro ? "" : '<button type="button" data-ins="\\frac{#@}{#?}" title="Fracció">a/b</button><button type="button" data-ins="\\cdot 10^{#?}" title="Potència de 10">·10ⁿ</button><button type="button" data-ins="#@^{#?}" title="Potència">xⁿ</button><button type="button" data-ins="\\cdot" title="Per">·</button><button type="button" data-ins="\\left(#?\\right)" title="Parèntesis">( )</button><button type="button" data-ins="\\sqrt{#?}" title="Arrel">√</button>'}</div>
          <math-field class="mf" math-virtual-keyboard-policy="manual"${st.ro ? " read-only" : ""}>${esc(a.latex || "")}</math-field><output class="ws-calc" data-calc></output></div>
          <div class="ws-res"><span>Resultat:</span><span class="ws-sci"><input class="ws-in m" inputmode="decimal" data-k="m" value="${esc(a.m || "")}" placeholder="a"${dis}><span>· 10</span><input class="ws-in e sup" inputmode="numeric" data-k="e" value="${esc(a.e || "")}" placeholder="n"${dis}></span></div>`;
        case "chain": {
          const fs = a.factors && a.factors.length ? a.factors : [{ nv: "", nu: "", dv: "", du: "" }];
          return `<div class="ws-chain"><span class="q0">${esc(it.start.v.replace("·10^4", "·10⁴"))} <b>${esc(it.start.u)}</b></span>${fs.map((f, i) => `<span class="dot">·</span><span class="frac" data-f="${i}"><span class="fn"><input class="ws-in v" inputmode="decimal" data-fk="nv" value="${esc(f.nv)}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-fk="nu" value="${esc(f.nu)}" placeholder="unitat"${dis}></span><span class="fd"><input class="ws-in v" inputmode="decimal" data-fk="dv" value="${esc(f.dv)}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-fk="du" value="${esc(f.du)}" placeholder="unitat"${dis}></span>${st.ro ? "" : `<button type="button" class="fx" data-del="${i}" aria-label="Treu el factor">${ICON.x}</button>`}<i class="fchk" data-fchk="${i}"></i></span>`).join("")}${st.ro ? "" : '<button type="button" class="addf" data-add>+ factor</button>'}
            <span class="eq">=</span><span class="ws-final"><input class="ws-in v" inputmode="decimal" data-k="v" value="${esc(a.v || "")}" placeholder="resultat"${dis}><input class="ws-in u" list="fq-units" data-k="u" value="${esc(a.u || "")}" placeholder="${esc(it.target)}"${dis}></span></div><output class="ws-calc" data-calc></output>`;
        }
        case "tf": return `<table class="ws-tab"><thead><tr><th>Sentence</th><th>T / F</th><th>Correction</th></tr></thead><tbody>${it.statements.map((s, i) => `<tr><td>${esc(s[0])}</td><td class="tf"><label><input type="radio" name="tf-${it.id}-${i}" value="T" data-tf="${i}"${(a.ans || {})[i] === true ? " checked" : ""}${dis}>T</label><label><input type="radio" name="tf-${it.id}-${i}" value="F" data-tf="${i}"${(a.ans || {})[i] === false ? " checked" : ""}${dis}>F</label></td><td><input class="ws-in w" data-corr="${i}" value="${esc((a.corr || {})[i] || "")}"${dis}></td></tr>`).join("")}</tbody></table>`;
        case "table": return `<div class="ws-scroll"><table class="ws-tab"><thead><tr>${it.cols.map((c) => `<th>${esc(c)}</th>`).join("")}</tr></thead><tbody>${it.rows.map((r, ri) => `<tr><th scope="row">${esc(r.label)}</th>${r.cells.map((c, ci) => { const v = (a.cells || {})[`r${ri}c${ci}`] || ""; const k = `r${ri}c${ci}`;
            const ok = opts.showCheck ? cellOk(c, v) : null; const cls = ok === null ? "" : ok ? " ok" : " ko";
            if (c.type === "select") return `<td class="${cls}"><select class="ws-in" data-cell="${k}"${dis}><option value=""></option>${c.options.map((o) => `<option${o === v ? " selected" : ""}>${esc(o)}</option>`).join("")}</select></td>`;
            if (c.type === "pow10") return `<td class="${cls}"><span class="ws-sci">10<input class="ws-in e sup" inputmode="numeric" data-cell="${k}" value="${esc(v)}" placeholder="n"${dis}></span></td>`;
            return `<td class="${cls}"><input class="ws-in${c.small ? " s" : ""}${c.wide ? " w" : ""}" ${c.type === "number" ? 'inputmode="decimal"' : ""} data-cell="${k}" value="${esc(v)}"${dis}></td>`; }).join("")}</tr>`).join("")}</tbody></table></div>`;
        default: return "";
      }
    }
    function itemHtml(it, numbered) {
      const head = it.label ? `<div class="ws-lbl">${esc(it.label)}</div>` : (it.prompt ? `<div class="ws-q">${numbered ? `<span class="ws-n">${esc(it.id)}</span>` : ""}<div>${it.prompt}</div></div>` : "");
      return `<div class="ws-item" data-item="${it.id}" data-type="${it.type}">${head}${widget(it)}${checkHtml(it)}${opts.showCheck && (it.expected || it.criteria) && ["text"].includes(it.type) ? `<details class="ws-exp"><summary>Resposta model</summary>${esc(it.expected || "")}${it.criteria ? `<div class="crit">${esc(it.criteria)}</div>` : ""}</details>` : ""}${fbHtml(it.id)}</div>`;
    }
    let html = `<div class="ws">`;
    spec.blocks.forEach((b) => {
      if (b.type === "tip") html += `<div class="ws-tip">${b.html}</div>`;
      else if (b.type === "h") html += `<h3 class="ws-h">${esc(b.text)}</h3>`;
      else if (b.type === "reading") html += `<div class="ws-read" lang="${b.lang || "en"}"><div class="rhead"><b>${esc(b.title)}</b><button type="button" class="btn ws-tts" data-tts>${ICON.play}<span>Escolta el text</span></button></div><div class="rbody"><div>${b.paras.map((p) => `<p>${esc(p)}</p>`).join("")}</div>${b.img ? `<img src="${esc(b.img)}" alt="">` : ""}</div><p class="gl"><b>Glossary:</b> ${esc(b.glossary || "")}</p></div>`;
      else if (b.type === "group") html += `<section class="ws-block" data-block="${b.id}"><div class="ws-q"><span class="ws-n">${esc(b.id)}</span><div>${b.prompt}</div></div><div class="ws-sub">${b.items.map((x) => itemHtml(x, false)).join("")}</div>${b.photo ? photoBtn(b.id) : ""}${fbHtml(b.id)}</section>`;
      else html += `<section class="ws-block">${itemHtml(b, true)}${b.photo ? photoBtn(b.id) : ""}</section>`;
    });
    html += `${fbHtml("_global")}</div>`;
    host.innerHTML = html;
    typeset(host);
    try { (window.FQWidgets || []).forEach((fn) => fn(host)); } catch (e) { console.warn(e); }

    /* fotos: carrega miniatures */
    host.querySelectorAll("img[data-src]").forEach(async (img) => { try { img.src = await opts.photoUrl(img.dataset.src); } catch {} });

    /* càlculs */
    function calc(itemEl) {
      const it = itemById[itemEl.dataset.item]; const a = st.answers[it.id] || {}; const out = itemEl.querySelector("[data-calc]");
      if (it.type === "chain") {
        const c = U.chain(it.start, a.factors || []);
        itemEl.querySelectorAll("[data-fchk]").forEach((el, i) => { const k = c.checks[i]; el.className = "fchk" + (st.auto && k ? " " + k : ""); el.title = !st.auto ? "" : k === "one" ? "El factor val 1" : k === "notone" ? "Aquest factor no val 1: revisa l'equivalència" : k === "dims" ? "Les unitats de dalt i de baix no mesuren el mateix" : ""; });
        if (out) out.innerHTML = st.auto && c.ok && (a.factors || []).length ? `Càlcul: <b>${U.fmt(c.value)} ${esc(c.unitStr)}</b>` : "";
      } else if (it.type === "sci") {
        const v = sciVal(a); if (out) out.textContent = st.auto && isFinite(v) ? "= " + U.fmt(v, 6) : "";
      } else if (it.type === "math") {
        const v = U.evalLatex(a.latex); if (out) out.innerHTML = st.auto && isFinite(v) ? `= <b>${U.fmt(v, 6)}</b>` : "";
      }
    }
    const itemById = Object.fromEntries(allItems(spec).map((x) => [x.id, x]));
    host.querySelectorAll(".ws-item").forEach(calc);

    if (st.ro) return { answers: st.answers };

    trackPaste(host, st.answers, set, (t) => { const el = t.closest && t.closest(".ws-item"); return el && el.dataset.item; });
    host.addEventListener("input", (e) => {
      const itemEl = e.target.closest(".ws-item"); if (!itemEl) return; const id = itemEl.dataset.item; const it = itemById[id];
      const a = { ...(st.answers[id] || {}) };
      if (e.target.dataset.k) a[e.target.dataset.k] = e.target.value;
      if (e.target.dataset.cell) a.cells = { ...(a.cells || {}), [e.target.dataset.cell]: e.target.value };
      if (e.target.dataset.corr != null) a.corr = { ...(a.corr || {}), [e.target.dataset.corr]: e.target.value };
      if (e.target.dataset.fk) { const fi = +e.target.closest("[data-f]").dataset.f; const fs = (a.factors && a.factors.length ? a.factors : [{ nv: "", nu: "", dv: "", du: "" }]).map((f) => ({ ...f })); fs[fi][e.target.dataset.fk] = e.target.value; a.factors = fs; }
      if (e.target.tagName === "MATH-FIELD") a.latex = e.target.value;
      set(id, a); calc(itemEl);
    });
    host.addEventListener("change", (e) => {
      if (e.target.dataset.tf != null) { const itemEl = e.target.closest(".ws-item"); const id = itemEl.dataset.item; const a = { ...(st.answers[id] || {}) }; a.ans = { ...(a.ans || {}), [e.target.dataset.tf]: e.target.value === "T" }; set(id, a); }
      if (e.target.dataset.photoItem) { const f = e.target.files[0]; if (f) opts.onPhoto(e.target.dataset.photoItem, f); e.target.value = ""; }
    });
    host.addEventListener("click", (e) => {
      const ins = e.target.closest("[data-ins]"); if (ins) { const mf = ins.closest(".ws-math").querySelector("math-field"); mf.focus(); mf.executeCommand(["insert", ins.dataset.ins]); return; }
      const add = e.target.closest("[data-add]"), del = e.target.closest("[data-del]");
      if (add || del) {
        const itemEl = e.target.closest(".ws-item"); const id = itemEl.dataset.item; const it = itemById[id]; const a = { ...(st.answers[id] || {}) };
        let fs = (a.factors && a.factors.length ? a.factors : [{ nv: "", nu: "", dv: "", du: "" }]).map((f) => ({ ...f }));
        if (add) fs.push({ nv: "", nu: "", dv: "", du: "" }); else fs.splice(+del.dataset.del, 1);
        a.factors = fs; set(id, a);
        const tmp = document.createElement("div"); tmp.innerHTML = itemHtml(it, !it.label && !!it.prompt); itemEl.replaceWith(tmp.firstElementChild);
        const nel = host.querySelector(`.ws-item[data-item="${id}"]`); calc(nel); if (add) { const ins2 = nel.querySelectorAll("[data-f]"); ins2[ins2.length - 1].querySelector("input").focus(); }
        return;
      }
      const px = e.target.closest(".ph-x"); if (px) { opts.onRemovePhoto(px.closest(".ph").dataset.path); return; }
      const tts = e.target.closest("[data-tts]"); if (tts) speak(tts, spec.blocks.find((b) => b.type === "reading"));
    });
    return { answers: st.answers, setAuto(v) { st.auto = v; host.querySelectorAll(".ws-item").forEach(calc); } };
  }

  /* lectura en veu alta: fitxer d'àudio si existeix; si no, veu del navegador */
  let audio = null;
  async function speak(btn, b) {
    const label = btn.querySelector("span");
    const setPlaying = (p) => { btn.innerHTML = (p ? ICON.pause : ICON.play) + `<span>${p ? "Atura" : "Escolta el text"}</span>`; };
    if (audio && !audio.paused) { audio.pause(); setPlaying(false); return; }
    if (G.speechSynthesis && G.speechSynthesis.speaking) { G.speechSynthesis.cancel(); setPlaying(false); return; }
    if (b.audio) {
      try { const r = await fetch(b.audio, { method: "HEAD" }); if (r.ok) { audio = audio || new Audio(b.audio); audio.onended = () => setPlaying(false); await audio.play(); setPlaying(true); return; } } catch {}
    }
    if (!G.speechSynthesis) return;
    const u = new SpeechSynthesisUtterance([b.title, ...b.paras].join("\n\n")); u.lang = b.lang || "en-GB"; u.rate = 0.92;
    const v = G.speechSynthesis.getVoices().filter((x) => x.lang && x.lang.startsWith("en"));
    u.voice = v.find((x) => /natural|neural|google uk|sonia|libby|daniel/i.test(x.name)) || v.find((x) => x.lang === "en-GB") || v[0] || null;
    u.onend = () => setPlaying(false); G.speechSynthesis.speak(u); setPlaying(true);
  }


  /* ================= Pissarra: tota la pantalla per escriure i dibuixar a mà ================= */
  const Board = (function () {
    const COLS = ["#1f2328", "#2563eb", "#dc2626"];
    function drawStroke(c, st, k, ox = 0, oy = 0) {
      const P = st.p; if (!P || !P.length) return;
      c.strokeStyle = st.c; c.fillStyle = st.c; c.lineWidth = (st.w || 2.6) * k; c.lineCap = "round"; c.lineJoin = "round";
      const X = (i) => (P[i] - ox) * k, Y = (i) => (P[i + 1] - oy) * k;
      c.beginPath(); c.moveTo(X(0), Y(0));
      const L = P.length - 2;
      if (st.t === "l" || st.t === "a") { c.lineTo(X(L), Y(L)); c.stroke(); }
      else if (P.length === 2) { c.arc(X(0), Y(0), c.lineWidth / 2, 0, 7); c.fill(); return; }
      else { for (let i = 2; i < L; i += 2) { const mx = (X(i) + X(i + 2)) / 2, my = (Y(i) + Y(i + 2)) / 2; c.quadraticCurveTo(X(i), Y(i), mx, my); } c.lineTo(X(L), Y(L)); c.stroke(); }
      if (st.t === "a" && P.length >= 4) {
        const x1 = X(0), y1 = Y(0), x2 = X(L), y2 = Y(L), a = Math.atan2(y2 - y1, x2 - x1), h = Math.max(10 * k, c.lineWidth * 4);
        c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - h * Math.cos(a - 0.45), y2 - h * Math.sin(a - 0.45)); c.lineTo(x2 - h * Math.cos(a + 0.45), y2 - h * Math.sin(a + 0.45)); c.closePath(); c.fill();
      }
    }
    function bbox(strokes) {
      let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
      strokes.forEach((st) => { for (let i = 0; i < st.p.length; i += 2) { x0 = Math.min(x0, st.p[i]); x1 = Math.max(x1, st.p[i]); y0 = Math.min(y0, st.p[i + 1]); y1 = Math.max(y1, st.p[i + 1]); } });
      return isFinite(x0) ? [x0, y0, x1, y1] : null;
    }
    /* imatge retallada a la zona escrita, traç fosc sobre blanc, com a màxim 1200 px: llegible i lleugera */
    function exportPng(strokes) {
      const bb = bbox(strokes); if (!bb) return Promise.resolve(null);
      const pad = 18, w = bb[2] - bb[0] + 2 * pad, h = bb[3] - bb[1] + 2 * pad, k = Math.min(1.6, 1200 / Math.max(w, h));
      const cv = document.createElement("canvas"); cv.width = Math.max(1, Math.round(w * k)); cv.height = Math.max(1, Math.round(h * k));
      const c = cv.getContext("2d"); c.fillStyle = "#fff"; c.fillRect(0, 0, cv.width, cv.height);
      strokes.forEach((st) => drawStroke(c, st, k, bb[0] - pad, bb[1] - pad));
      return new Promise((res) => cv.toBlob((b) => res(b ? new File([b], "pissarra.png", { type: "image/png" }) : null), "image/png"));
    }
    function open({ data, title, onSave }) {
      const W0 = data && data.w ? data.w : null;
      let strokes = (data && data.s ? data.s : []).map((x) => ({ ...x, p: [...x.p] })); const redo = [];
      let tool = "pen", col = COLS[0], grid = data ? data.g !== 0 : true, penSeen = false;
      const ov = document.createElement("div"); ov.className = "pz"; ov.setAttribute("role", "dialog"); ov.setAttribute("aria-label", "Pissarra");
      // estils essencials en línia: la pissarra s'obre a pantalla completa encara que el full d'estils sigui antic (memòria cau) o el navegador no conegui «inset» (iPad antics)
      ov.style.cssText = "position:fixed;top:0;left:0;right:0;bottom:0;width:100%;height:" + window.innerHeight + "px;z-index:2147483000;background:#fff;display:flex;flex-direction:column;touch-action:none;-webkit-user-select:none;user-select:none";
      ov.innerHTML = `<div class="pz-bar">
        <div class="pz-g">${[["pen", "✏️", "Llapis"], ["arrow", "↗", "Fletxa (forces, vectors)"], ["line", "╱", "Línia recta"], ["erase", "⌫", "Goma: toca un traç per esborrar-lo"]].map(([t, i, l]) => `<button type="button" data-tool="${t}" title="${l}" aria-label="${l}">${i}</button>`).join("")}</div>
        <div class="pz-g">${COLS.map((c) => `<button type="button" class="sw" data-col="${c}" style="--c:${c}" aria-label="Color"></button>`).join("")}</div>
        <div class="pz-g"><button type="button" data-act="undo" title="Desfés" aria-label="Desfés">↶</button><button type="button" data-act="redo" title="Refés" aria-label="Refés">↷</button><button type="button" data-act="grid" title="Quadrícula" aria-label="Quadrícula">▦</button><button type="button" data-act="clear" title="Esborra-ho tot" aria-label="Esborra-ho tot">🗑</button></div>
        <span class="pz-t">${esc(title || "")}</span>
        <div class="pz-g end"><button type="button" class="pz-x" data-act="cancel">Cancel·la</button><button type="button" class="pz-ok" data-act="save">Desa</button></div></div>
        <div class="pz-c"><canvas></canvas></div>`;
      document.body.appendChild(ov); document.documentElement.classList.add("pz-on");
      // la pàgina de sota no es mou mentre s'escriu amb el dit (iPad: overflow:hidden no n'hi ha prou)
      const sy = window.scrollY, bs = document.body.style, prevBody = bs.cssText;
      bs.position = "fixed"; bs.top = -sy + "px"; bs.left = "0"; bs.right = "0"; bs.overflow = "hidden";
      const noScroll = (e) => { if (!e.target.closest || !e.target.closest(".pz-bar")) e.preventDefault(); };
      ov.addEventListener("touchmove", noScroll, { passive: false });
      ov.addEventListener("gesturestart", (e) => e.preventDefault());
      const host = ov.querySelector(".pz-c"), cv = ov.querySelector("canvas"), c = cv.getContext("2d");
      host.style.cssText = "flex:1 1 auto;position:relative;min-height:0;overflow:hidden;touch-action:none";
      cv.style.touchAction = "none"; cv.style.display = "block";
      const fit = () => { ov.style.height = window.innerHeight + "px"; };
      const onRs = () => { fit(); size(); };
      let k = 1, cur = null;
      function size() {
        const r = host.getBoundingClientRect(), dpr = window.devicePixelRatio || 1;
        cv.width = Math.round(r.width * dpr); cv.height = Math.round(r.height * dpr); cv.style.width = r.width + "px"; cv.style.height = r.height + "px";
        k = W0 ? r.width / W0 : 1; c.setTransform(dpr, 0, 0, dpr, 0, 0); paint();
      }
      function paint() {
        const r = host.getBoundingClientRect(); c.clearRect(0, 0, r.width, r.height);
        if (grid) { c.strokeStyle = "#e3e8ef"; c.lineWidth = 1; c.beginPath(); for (let x = 24; x < r.width; x += 24) { c.moveTo(x + .5, 0); c.lineTo(x + .5, r.height); } for (let y = 24; y < r.height; y += 24) { c.moveTo(0, y + .5); c.lineTo(r.width, y + .5); } c.stroke(); }
        strokes.forEach((st) => drawStroke(c, st, k)); if (cur) drawStroke(c, cur, k);
        ov.querySelectorAll("[data-tool]").forEach((b) => b.classList.toggle("on", b.dataset.tool === tool));
        ov.querySelectorAll("[data-col]").forEach((b) => b.classList.toggle("on", b.dataset.col === col));
        ov.querySelector('[data-act="grid"]').classList.toggle("on", grid);
      }
      const pt = (e) => { const r = cv.getBoundingClientRect(); return [Math.round((e.clientX - r.left) / k * 10) / 10, Math.round((e.clientY - r.top) / k * 10) / 10]; };
      function eraseAt(p) { const R = 12 / k; const n = strokes.length; strokes = strokes.filter((st) => { for (let i = 0; i < st.p.length; i += 2) if (Math.hypot(st.p[i] - p[0], st.p[i + 1] - p[1]) < R) return false; if (st.t !== "f" && st.p.length >= 4) { const [x1, y1] = st.p, x2 = st.p[st.p.length - 2], y2 = st.p[st.p.length - 1]; const L = Math.hypot(x2 - x1, y2 - y1) || 1; const t = Math.max(0, Math.min(1, ((p[0] - x1) * (x2 - x1) + (p[1] - y1) * (y2 - y1)) / (L * L))); if (Math.hypot(x1 + t * (x2 - x1) - p[0], y1 + t * (y2 - y1) - p[1]) < R) return false; } return true; }); if (strokes.length !== n) { redo.length = 0; paint(); } }
      cv.addEventListener("pointerdown", (e) => {
        if (e.pointerType === "pen") penSeen = true; else if (penSeen && e.pointerType === "touch") return; // el palmell no pinta si s'usa llapis
        cv.setPointerCapture(e.pointerId); const p = pt(e);
        if (tool === "erase") { eraseAt(p); cur = { erase: true }; return; }
        cur = { t: tool === "pen" ? "f" : tool === "arrow" ? "a" : "l", c: col, w: 2.6, p: [...p, ...(tool === "pen" ? [] : p)] }; paint();
      });
      cv.addEventListener("pointermove", (e) => {
        if (!cur) return; const p = pt(e);
        if (cur.erase) { eraseAt(p); return; }
        if (cur.t === "f") { const n = cur.p.length; if (Math.hypot(cur.p[n - 2] - p[0], cur.p[n - 1] - p[1]) >= 1.5 / k) cur.p.push(p[0], p[1]); }
        else { cur.p[2] = p[0]; cur.p[3] = p[1]; }
        paint();
      });
      const end = () => { if (cur && !cur.erase && cur.p.length >= 2) { strokes.push(cur); redo.length = 0; } cur = null; paint(); };
      cv.addEventListener("pointerup", end); cv.addEventListener("pointercancel", end);
      function close() { window.removeEventListener("resize", onRs); window.removeEventListener("orientationchange", onRs); document.documentElement.classList.remove("pz-on"); ov.remove(); bs.cssText = prevBody; window.scrollTo(0, sy); }
      ov.addEventListener("click", async (e) => {
        const b = e.target.closest("button"); if (!b) return;
        if (b.dataset.tool) { tool = b.dataset.tool; paint(); return; }
        if (b.dataset.col) { col = b.dataset.col; if (tool === "erase") tool = "pen"; paint(); return; }
        const a = b.dataset.act;
        if (a === "undo" && strokes.length) { redo.push(strokes.pop()); paint(); }
        if (a === "redo" && redo.length) { strokes.push(redo.pop()); paint(); }
        if (a === "grid") { grid = !grid; paint(); }
        if (a === "clear" && strokes.length) { if (b.dataset.sure === "1") { redo.push(...strokes.reverse()); strokes = []; b.dataset.sure = ""; b.textContent = "🗑"; paint(); } else { b.dataset.sure = "1"; b.textContent = "Segur?"; setTimeout(() => { b.dataset.sure = ""; b.textContent = "🗑"; }, 2500); } }
        if (a === "cancel") close();
        if (a === "save") {
          b.disabled = true; b.textContent = "Desant…";
          const r = host.getBoundingClientRect(); const w = W0 || Math.round(r.width);
          const out = { w, g: grid ? 1 : 0, s: strokes.map((st) => ({ t: st.t, c: st.c, w: st.w, p: st.p.map((v) => Math.round(v * 10) / 10) })) };
          try { await onSave(out, await exportPng(out.s)); close(); } catch (err) { b.disabled = false; b.textContent = "Desa"; console.warn(err); }
        }
      });
      window.addEventListener("resize", onRs); window.addEventListener("orientationchange", onRs); requestAnimationFrame(() => { fit(); size(); });
    }
    return { open, exportPng };
  })();
  G.FQBoard = Board;

  /* ================= Fitxes convertides dels fulls (spec.html) ================= */
  function workLineHtml(ln, i, ro) {
    const dis = ro ? " disabled" : "";
    const lab = ln.lab ? ` data-lab="${esc(ln.lab)}"` : "";
    const del = ro || ln.lab ? "" : `<button type="button" class="wl-x" data-wdel="${i}" aria-label="Treu aquesta línia">${ICON.x}</button>`;
    if (ln.t === "res") return `<div class="wl wl-res" data-wl="${i}"${lab}><span class="wl-tag">${esc(ln.lab || "Resultat")}</span><span class="ws-final"><input class="ws-in v" inputmode="decimal" data-rk="v" value="${esc(ln.v || "")}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-rk="u" value="${esc(ln.u || "")}" placeholder="${esc(ln.ut || "unitat")}"${dis}></span><span class="lchk" aria-live="polite"></span>${del}</div>`;
    if (ln.t === "math") return `<div class="wl wl-math" data-wl="${i}"${lab}><span class="wl-tag">${esc(ln.lab || "Equació")}</span><div class="mtools">${ro ? "" : '<button type="button" data-ins="\\frac{#@}{#?}" title="Fracció">a/b</button><button type="button" data-ins="\\cdot 10^{#?}" title="Potència de 10">·10ⁿ</button><button type="button" data-ins="#@^{#?}" title="Potència">xⁿ</button><button type="button" data-ins="\\cdot" title="Per">·</button><button type="button" data-ins="\\left(#?\\right)" title="Parèntesis">( )</button><button type="button" data-ins="\\sqrt{#?}" title="Arrel">√</button><button type="button" data-ins="\\Delta" title="Increment">Δ</button>'}</div><math-field class="mf" math-virtual-keyboard-policy="manual"${ro ? " read-only" : ""}>${esc(ln.v || "")}</math-field><output class="ws-calc" data-calc></output><span class="lchk" aria-live="polite"></span>${del}</div>`;
    if (ln.t === "chain") {
      const fs = ln.factors && ln.factors.length ? ln.factors : [{ nv: "", nu: "", dv: "", du: "" }];
      return `<div class="wl wl-chain" data-wl="${i}"${lab}${ln.rt ? ` data-rt="${esc(ln.rt)}"` : ""}><span class="wl-tag">${esc(ln.lab || "Factors de conversió")}</span><div class="ws-chain"><span class="ws-final"><input class="ws-in v" inputmode="decimal" data-ck="sv" value="${esc(ln.sv || "")}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-ck="su" value="${esc(ln.su || "")}" placeholder="unitat"${dis}></span>${fs.map((f, j) => `<span class="dot">·</span><span class="frac" data-f="${j}"><span class="fn"><input class="ws-in v" inputmode="decimal" data-fk="nv" value="${esc(f.nv)}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-fk="nu" value="${esc(f.nu)}" placeholder="unitat"${dis}></span><span class="fd"><input class="ws-in v" inputmode="decimal" data-fk="dv" value="${esc(f.dv)}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-fk="du" value="${esc(f.du)}" placeholder="unitat"${dis}></span>${ro ? "" : `<button type="button" class="fx" data-fdel="${j}" aria-label="Treu el factor">${ICON.x}</button>`}<i class="fchk" data-fchk="${j}"></i></span>`).join("")}${ro ? "" : '<button type="button" class="addf" data-fadd>+ factor</button>'}<span class="eq">=</span><span class="ws-final"><input class="ws-in v" inputmode="decimal" data-ck="rv" value="${esc(ln.rv || "")}" placeholder="resultat"${dis}><input class="ws-in u" list="fq-units" data-ck="ru" value="${esc(ln.ru || "")}" placeholder="${esc(ln.rt || "unitat")}"${dis}></span><span class="lchk" aria-live="polite"></span></div><output class="ws-calc" data-calc></output>${del}</div>`;
    }
    return `<div class="wl wl-text" data-wl="${i}"${lab}${ln.ph ? ` data-ph="${esc(ln.ph)}"` : ""}>${ln.lab ? `<span class="wl-tag">${esc(ln.lab)}</span>` : ""}<textarea class="ws-text" rows="${ln.rows || 2}" data-wt${ln.ph ? ` placeholder="${esc(ln.ph)}"` : ""}${dis}>${esc(ln.v || "")}</textarea>${i > 0 ? del : ""}</div>`;
  }
  let curPhotos = [];
  const boardHas = (a) => !!(a && a.board && a.board.s && a.board.s.length);
  function boardHtml(fid, a, ro) {
    const ph = curPhotos.filter((p) => p.item === fid);
    const prev = ph.length ? `<span class="bprev">${ph.map((p) => `<img alt="Pissarra" data-src="${esc(p.path)}">`).join("")}</span>` : "";
    if (ro) return prev ? `<div class="bwrap">${prev}</div>` : "";
    return `<div class="bwrap">${prev}<button type="button" class="bbtn" data-board="${fid}">${boardHas(a) ? "✏️ Continua a la pissarra" : "✏️ Pissarra: escriu i dibuixa a mà"}</button></div>`;
  }
  function workHtml(fid, f, a, ro) {
    const lines = a && a.lines && a.lines.length ? a.lines : (f.init && f.init.length ? f.init.map((x) => ({ ...x, factors: x.t === "chain" ? [{ nv: "", nu: "", dv: "", du: "" }] : undefined })) : [{ t: "text", v: "", rows: f.rows || 2 }]);
    if (ro && !(a && a.lines)) return `<div class="work ro" data-fid="${fid}"><div class="wl wl-text"><textarea class="ws-text" rows="${f.rows || 2}" disabled></textarea></div>${boardHtml(fid, a, ro)}</div>`;
    return `<div class="work${f.init ? " scaf" : ""}${f.sub ? " sub" : ""}" data-fid="${fid}">${lines.map((ln, i) => workLineHtml(ln, i, ro)).join("")}${ro || f.plain ? "" : `<div class="wadd"><button type="button" data-wadd="text">+ text</button><button type="button" data-wadd="math">+ equació</button><button type="button" data-wadd="chain">+ factors de conversió</button><button type="button" data-wadd="res">+ resultat</button></div>`}${f.plain ? "" : boardHtml(fid, a, ro)}</div>`;
  }
  function photoFieldHtml(fid, f, photos, ro) {
    const ps = photos.filter((p) => p.item === fid);
    if (ro && !ps.length) return `<span class="muted">(sense foto)</span>`;
    return `<div class="ws-photos" data-photos="${fid}">${ps.map((p) => `<span class="ph" data-path="${esc(p.path)}"><img alt="Foto adjunta" data-src="${esc(p.path)}">${ro ? "" : `<button type="button" class="ph-x" aria-label="Treu la foto">${ICON.x}</button>`}</span>`).join("")}${ro ? "" : `<label class="ws-cam">${ICON.cam}<span>${f.label && f.label.length < 40 ? "Foto: " + esc(f.label) : "Puja una foto del dibuix"}</span><input type="file" accept="image/*" capture="environment" data-photo-item="${fid}" hidden></label>`}</div>`;
  }
  function fieldHtml(fid, f, a, ro, photos) {
    const dis = ro ? " disabled" : "";
    switch (f.k) {
      case "work":
        if (f.legacy) { const has = a && (a.lines || []).some((l) => l.v || l.rv || l.sv || (l.factors || []).some((x) => x.nv || x.dv)); return has ? `<div class="legacy"><span class="wl-tag">La teva resposta anterior</span>${workHtml(fid, { ...f, plain: 1 }, a, ro)}</div>` : ""; }
        return workHtml(fid, f, a, ro);
      case "cell": if (f.opts) return `<select class="ws-in cellf" data-cf="${fid}"${dis}><option value=""></option>${f.opts.map((o) => `<option${a && a.v === o ? " selected" : ""}>${esc(o)}</option>`).join("")}</select>`;
        if (f.coef) return `<input class="ws-in coef" data-cf="${fid}" inputmode="numeric" maxlength="3" value="${esc((a && a.v) || "")}"${dis} aria-label="Coeficient" title="Coeficient (deixa-ho buit si és 1)">`;
        return `<input class="ws-in cellf${f.wide ? " wide" : ""}" data-cf="${fid}" value="${esc((a && a.v) || "")}"${f.ph ? ` placeholder="${esc(f.ph)}"` : ""}${dis} aria-label="Resposta">`;
      case "check": return `<input type="checkbox" class="chkf" data-cf="${fid}"${a && a.v ? " checked" : ""}${dis} aria-label="Marca">`;
      case "rate": return `<span class="ratef" data-rate="${fid}">${[1, 2, 3, 4].map((n) => `<label><input type="radio" name="r-${fid}" value="${n}" data-cf="${fid}"${a && +a.v === n ? " checked" : ""}${dis}>${n}</label>`).join("")}</span>`;
      case "photo": return photoFieldHtml(fid, f, photos, ro);
    }
    return "";
  }
  function drawRadar(host, spec, answers) {
    const el = host.querySelector("[data-radar]"); if (!el) return;
    const ids = Object.keys(spec.fields).filter((k) => spec.fields[k].k === "rate"); const n = ids.length; if (n < 3) return;
    const R = 120, C = 150, pt = (i, v) => { const a = -Math.PI / 2 + (2 * Math.PI * i) / n; return [C + Math.cos(a) * R * v / 4, C + Math.sin(a) * R * v / 4]; };
    let svg = `<svg viewBox="0 0 300 300" role="img" aria-label="Diana d'autoavaluació">`;
    for (let r = 1; r <= 4; r++) svg += `<polygon points="${ids.map((_, i) => pt(i, r).join(",")).join(" ")}" fill="none" stroke="var(--line)" stroke-width="1"/>`;
    ids.forEach((_, i) => { const [x, y] = pt(i, 4); svg += `<line x1="${C}" y1="${C}" x2="${x}" y2="${y}" stroke="var(--line)"/>`; const [lx, ly] = pt(i, 4.55); svg += `<text x="${lx}" y="${ly}" text-anchor="middle" dominant-baseline="middle" font-size="13" font-weight="700" fill="var(--fg)">${i + 1}</text>`; });
    const vals = ids.map((k) => +((answers[k] || {}).v || 0));
    if (vals.some((v) => v)) svg += `<polygon points="${vals.map((v, i) => pt(i, v).join(",")).join(" ")}" fill="color-mix(in srgb,var(--acc) 30%,transparent)" stroke="var(--acc)" stroke-width="2.5"/>` + vals.map((v, i) => v ? `<circle cx="${pt(i, v)[0]}" cy="${pt(i, v)[1]}" r="4.5" fill="var(--acc)"/>` : "").join("");
    el.innerHTML = svg + "</svg>";
  }
  function renderHtml(host, key, opts) {
    const spec = G.FITXES[key]; const ro = !!opts.readonly; const answers = { ...(opts.answers || {}) }; let auto = !!opts.autoCalc;
    const photos = opts.photos || []; curPhotos = photos; const fb = {}; (opts.feedback || []).forEach((f) => (fb[f.item_id] = f));
    const timers = {};
    const save = (fid, val) => { answers[fid] = val; if (ro) return; clearTimeout(timers[fid]); timers[fid] = setTimeout(() => opts.onSave && opts.onSave(fid, val), 600); };
    const wrap = document.createElement("div"); wrap.innerHTML = spec.html;
    wrap.querySelectorAll(".fld[data-fid]").forEach((el) => { const id = el.dataset.fid; const f = spec.fields[id]; if (!f) return; const t = document.createElement("span"); t.innerHTML = fieldHtml(id, f, answers[id], ro, photos); el.replaceWith(...t.childNodes); });
    wrap.querySelectorAll("[data-qblock]").forEach((b) => { const f = fb[b.dataset.qblock]; if (f && (f.level || f.comment)) b.insertAdjacentHTML("beforeend", `<div class="ws-fb">${f.level ? `<span class="lvchip lv-${f.level}">${f.level}</span>` : ""}<span>${esc(f.comment || "")}</span></div>`); });
    host.innerHTML = `<div class="ws wsh">${wrap.innerHTML}${fb._global && (fb._global.level || fb._global.comment) ? `<div class="ws-fb">${fb._global.level ? `<span class="lvchip lv-${fb._global.level}">${fb._global.level}</span>` : ""}<span>${esc(fb._global.comment || "")}</span></div>` : ""}</div>`;
    typeset(host);
    try { (window.FQWidgets || []).forEach((fn) => fn(host)); } catch (e) { console.warn(e); }
    host.querySelectorAll("img[data-src]").forEach(async (img) => { try { img.src = await opts.photoUrl(img.dataset.src); } catch {} });
    drawRadar(host, spec, answers);

    const keepBoard = (fid, v) => (answers[fid] && answers[fid].board ? { ...v, board: answers[fid].board } : v);
    const readWork = (w) => ({ lines: [...w.querySelectorAll(":scope > .wl")].map((l) => {
      const lab = l.dataset.lab ? { lab: l.dataset.lab } : {};
      if (l.classList.contains("wl-math")) return { t: "math", v: l.querySelector("math-field").value, ...lab };
      if (l.classList.contains("wl-res")) { const g = (k) => (l.querySelector(`[data-rk="${k}"]`) || {}).value || ""; const u = l.querySelector('[data-rk="u"]'); return { t: "res", v: g("v"), u: g("u"), ut: u && u.placeholder !== "unitat" ? u.placeholder : undefined, ...lab }; }
      if (l.classList.contains("wl-chain")) { const g = (k) => (l.querySelector(`[data-ck="${k}"]`) || {}).value || ""; return { t: "chain", sv: g("sv"), su: g("su"), rv: g("rv"), ru: g("ru"), rt: l.dataset.rt || undefined, ...lab, factors: [...l.querySelectorAll("[data-f]")].map((fr) => { const q = (k) => fr.querySelector(`[data-fk="${k}"]`).value; return { nv: q("nv"), nu: q("nu"), dv: q("dv"), du: q("du") }; }) }; }
      const ta = l.querySelector("textarea"); return { t: "text", v: ta.value, rows: +ta.getAttribute("rows") || 2, ph: l.dataset.ph || undefined, ...lab };
    }) });
    function calcLine(l) {
      const out = l.querySelector("[data-calc]"); if (!out) return;
      if (l.classList.contains("wl-math")) { const v = U.evalLatex(l.querySelector("math-field").value); out.innerHTML = auto && isFinite(v) ? `= <b>${U.fmt(v, 6)}</b>` : ""; return; }
      const g = (k) => (l.querySelector(`[data-ck="${k}"]`) || {}).value || "";
      const fs = [...l.querySelectorAll("[data-f]")].map((fr) => { const q = (k) => fr.querySelector(`[data-fk="${k}"]`).value; return { nv: q("nv"), nu: q("nu"), dv: q("dv"), du: q("du") }; });
      const c = U.chain({ v: g("sv"), u: g("su") }, fs);
      l.querySelectorAll("[data-fchk]").forEach((el, i) => { const k = c.checks[i]; el.className = "fchk" + (auto && k ? " " + k : ""); });
      out.innerHTML = auto && c.ok && fs.length ? `Càlcul: <b>${U.fmt(c.value)} ${esc(c.unitStr)}</b>` : "";
    }
    host.querySelectorAll(".wl-math, .wl-chain").forEach(calcLine);
    if (ro) return { answers };

    /* comprovació en directe del resultat i dels passos (al servidor) */
    const known = {}, ctimers = {};
    function liveCheck(w) {
      const fid = w.dataset.fid; if (!opts.onCheck || known[fid] === false) return;
      clearTimeout(ctimers[fid]); ctimers[fid] = setTimeout(async () => {
        const r = resultsOf(fid, readWork(w)); if (!r) { w.querySelectorAll(".lchk").forEach((x) => { x.className = "lchk"; x.textContent = ""; }); return; }
        let out; try { out = await opts.onCheck(fid, { res: r.res, steps: r.steps }); } catch { return; }
        if (!out || out.known === false) { known[fid] = false; return; }
        known[fid] = true;
        const mark = (el, ok) => { if (!el) return; el.className = "lchk" + (ok === true ? " ok" : ok === false ? " ko" : ""); el.textContent = ok === true ? "✓" : ok === false ? "✗" : ""; el.title = ok === true ? "Correcte" : ok === false ? "Revisa-ho" : ""; };
        const resEls = [...w.querySelectorAll(".wl-res"), ...w.querySelectorAll(".wl-chain")].filter((l) => l.classList.contains("wl-res") ? (l.querySelector('[data-rk="v"]') || {}).value : (l.querySelector('[data-ck="rv"]') || {}).value);
        resEls.forEach((l, i) => mark(l.querySelector(".lchk"), (out.res || [])[i]));
        [...w.querySelectorAll(".wl-math")].filter((l) => l.querySelector("math-field").value).forEach((l, i) => mark(l.querySelector(".lchk"), (out.steps || [])[i]));
      }, 900);
    }
    host.addEventListener("change", (e) => { const w = e.target.closest && e.target.closest(".work"); if (w) liveCheck(w); });
    host.addEventListener("focusout", (e) => { const w = e.target.closest && e.target.closest(".work"); if (w && (e.target.tagName === "MATH-FIELD" || e.target.closest(".wl-res, .wl-chain"))) liveCheck(w); });
    trackPaste(host, answers, save, (t) => { if (!t.closest) return null; const w = t.closest(".work"); if (w) return w.dataset.fid; const c = t.closest("[data-cf]"); return c && c.dataset.cf; });
    host.addEventListener("input", (e) => {
      const w = e.target.closest(".work");
      if (w) { const l = e.target.closest(".wl"); if (l) calcLine(l); save(w.dataset.fid, keepBoard(w.dataset.fid, readWork(w))); return; }
      const c = e.target.closest("[data-cf]"); if (c && c.type !== "radio" && c.type !== "checkbox") save(c.dataset.cf, { v: c.value });
    });
    host.addEventListener("change", (e) => {
      const c = e.target.closest("[data-cf]");
      if (c && c.type === "checkbox") save(c.dataset.cf, { v: c.checked });
      if (c && c.tagName === "SELECT") save(c.dataset.cf, { v: c.value });
      if (c && c.type === "radio") { save(c.dataset.cf, { v: +c.value }); drawRadar(host, spec, answers); }
      if (e.target.dataset.photoItem) { const f = e.target.files[0]; if (f) opts.onPhoto(e.target.dataset.photoItem, f); e.target.value = ""; }
    });
    host.addEventListener("click", (e) => {
      const ins = e.target.closest("[data-ins]"); if (ins) { const mf = ins.closest(".wl").querySelector("math-field"); mf.focus(); mf.executeCommand(["insert", ins.dataset.ins]); return; }
      const px = e.target.closest(".ph-x"); if (px) { opts.onRemovePhoto(px.closest(".ph").dataset.path); return; }
      const bb = e.target.closest("[data-board]");
      if (bb) {
        const fid = bb.dataset.board; const w0 = bb.closest(".work");
        const fq = (spec.fields && spec.fields[fid] || {}).q, qt = (spec.qs || {})[fq];
        try { Board.open({ data: (answers[fid] || {}).board, title: qt ? String(qt).replace(/<[^>]+>/g, "").replace(/^(.{0,150})\s.*$/s, "$1…") : spec.title, onSave: async (board, file) => {
          const val = { ...(w0 ? readWork(w0) : answers[fid] || {}), board }; answers[fid] = val; clearTimeout(timers[fid]);
          if (opts.onSave) await opts.onSave(fid, val);
          for (const p of photos.filter((x) => x.item === fid)) { try { await opts.onRemovePhoto(p.path); } catch {} }
          if (file && opts.onPhoto) await opts.onPhoto(fid, file);
        } }); } catch (err) { console.error(err); alert("No s'ha pogut obrir la pissarra. Torna-ho a provar o actualitza la pàgina."); }
        return;
      }
      const w = e.target.closest(".work"); if (!w) return;
      const st = readWork(w);
      const wa = e.target.closest("[data-wadd]"), wd = e.target.closest("[data-wdel]"), fa = e.target.closest("[data-fadd]"), fd = e.target.closest("[data-fdel]");
      if (!(wa || wd || fa || fd)) return;
      if (wa) st.lines.push(wa.dataset.wadd === "text" ? { t: "text", v: "", rows: 2 } : wa.dataset.wadd === "math" ? { t: "math", v: "" } : wa.dataset.wadd === "res" ? { t: "res", v: "", u: "" } : { t: "chain", factors: [{ nv: "", nu: "", dv: "", du: "" }] });
      if (wd) st.lines.splice(+wd.dataset.wdel, 1);
      const li = (fa || fd) ? +e.target.closest(".wl").dataset.wl : -1;
      if (fa) st.lines[li].factors.push({ nv: "", nu: "", dv: "", du: "" });
      if (fd) st.lines[li].factors.splice(+fd.dataset.fdel, 1);
      const t = document.createElement("div"); t.innerHTML = workHtml(w.dataset.fid, spec.fields[w.dataset.fid], st, false); const nw = t.firstElementChild; w.replaceWith(nw);
      nw.querySelectorAll(".wl-math, .wl-chain").forEach(calcLine); save(nw.dataset.fid, keepBoard(nw.dataset.fid, st));
      nw.querySelectorAll("img[data-src]").forEach(async (img) => { try { img.src = await opts.photoUrl(img.dataset.src); } catch {} });
      if (wa) { const last = nw.querySelectorAll(".wl"); const el = last[last.length - 1]; const f = el.querySelector("math-field, input, textarea"); if (f) setTimeout(() => f.focus(), 30); }
    });
    return { answers, setAuto(v) { auto = v; host.querySelectorAll(".wl-math, .wl-chain").forEach(calcLine); } };
  }
  function answerSummary(spec, fid, a) {
    const f = spec.fields[fid]; if (!a) return "";
    if (f.k === "work") return ((a.board && a.board.s && a.board.s.length) ? "[pissarra: dibuix adjunt] " : "") + (a.lines || []).map((l) => { const lb = l.lab ? l.lab + ": " : ""; const t = l.t === "math" ? (l.v ? `[${l.v}]` : "") : l.t === "res" ? (l.v ? `${l.v} ${l.u || ""}` : "") : l.t === "chain" ? ((l.factors || []).some((x) => x.nv || x.dv) || l.rv ? `${l.sv} ${l.su} ${(l.factors || []).map((x) => `·(${x.nv} ${x.nu})/(${x.dv} ${x.du})`).join(" ")} = ${l.rv} ${l.ru}` : "") : l.v; return t ? lb + t : ""; }).filter(Boolean).join(" | ");
    if (f.coef) return a.v ? `[${a.v}]` : "[ ]";
    if (f.k === "check") return a.v ? "[x]" : "[ ]";
    return String(a.v ?? "");
  }
  /* resultats (valor + unitat) i passos escrits a cada camp: es comproven al servidor */
  function resultsOf(fid, a) {
    if (!a || !a.lines) return null;
    const res = a.lines.filter((l) => l.t === "res" && l.v).map((l) => ({ v: l.v, u: l.u || "" }));
    a.lines.filter((l) => l.t === "chain" && l.rv).forEach((l) => res.push({ v: l.rv, u: l.ru || "" }));
    const steps = a.lines.filter((l) => l.t === "math" && l.v).map((l) => l.v);
    return res.length || steps.length ? { fid, res, steps } : null;
  }
  function htmlItems(spec, answers) {
    return Object.entries(spec.qs).map(([q, prompt]) => {
      const fids = Object.keys(spec.fields).filter((k) => spec.fields[k].q === q);
      const pids = fids.filter((k) => spec.fields[k].k === "photo" || boardHas(answers[k]));
      return { id: q, prompt, answer: fids.map((k) => answerSummary(spec, k, answers[k])).filter(Boolean).join(" · ") || "(sense resposta)", photos: pids.length, photo_ids: pids, results: fids.map((k) => resultsOf(k, answers[k])).filter(Boolean) };
    });
  }

  /* ---------- elements per a la correcció automàtica ---------- */
  function answerText(it, a) {
    if (!a) return "(sense resposta)";
    switch (it.type) {
      case "text": case "number": return a.text || "";
      case "sci": return `${a.m || "?"}·10^${a.e || "?"}`;
      case "math": return `${a.latex || ""} → ${a.m || "?"}·10^${a.e || "?"}`;
      case "chain": return `${it.start.v} ${it.start.u} ${(a.factors || []).map((f) => `· (${f.nv} ${f.nu})/(${f.dv} ${f.du})`).join(" ")} = ${a.v || "?"} ${a.u || ""}`;
      case "tf": return it.statements.map((st, i) => `${i + 1}: ${(a.ans || {})[i] === true ? "V" : (a.ans || {})[i] === false ? "F" : "?"} ${(a.corr || {})[i] || ""}`).join(" | ");
      case "table": return it.rows.map((r, ri) => r.label + ": " + r.cells.map((c, ci) => (a.cells || {})[`r${ri}c${ci}`] || "—").join(" / ")).join(" | ");
      default: return JSON.stringify(a);
    }
  }
  function buildItems(spec, answers) {
    const pz = (answers && answers._paste) || {}; const pasted = (ids) => ids.reduce((a, k) => a + (+pz[k] || 0), 0);
    const strip = (h) => String(h || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    const expOf = (it) => typeof it.expected === "object" ? `${it.expected.v} ${it.expected.u}` : (it.expected || "");
    if (spec.html) return htmlItems(spec, answers).map((x) => ({ id: x.id, prompt: x.prompt, expected: "", criteria: x.photos ? "La resposta inclou un dibuix o un càlcul fet a mà (foto o pissarra) que s'adjunta." : "", answer: x.answer, auto: null, score: null, photos: x.photos, photo_ids: x.photo_ids, results: x.results, pasted: pasted(Object.keys(spec.fields).filter((k) => spec.fields[k].q === x.id)) }));
    return spec.blocks.filter((b) => b.id).map((b) => {
      if (b.type !== "group") { const r = checkItem(b, answers[b.id]); return { pasted: pasted([b.id]), photos: b.photo ? 1 : 0, photo_ids: b.photo ? [b.id] : [], id: b.id, prompt: strip(b.prompt), expected: expOf(b), criteria: b.criteria || "", answer: answerText(b, answers[b.id]), auto: r.ok === null ? null : (r.detail ? `${r.ok ? "correcte" : "incorrecte"} (${r.detail})` : r.ok), score: r.score ?? (r.ok === null ? null : r.ok ? 1 : 0) }; }
      const parts = b.items.map((it) => ({ it, r: checkItem(it, answers[it.id]) }));
      const checked = parts.filter((x) => x.r.ok !== null); const good = checked.filter((x) => x.r.ok).length;
      return { pasted: pasted(b.items.map((it) => it.id)), photos: b.photo ? 1 : 0, photo_ids: b.photo ? [b.id] : [], id: b.id, prompt: strip(b.prompt) + " " + b.items.map((it) => it.label).join(" · "), expected: b.items.map((it) => `${it.label}: ${expOf(it)}`).join(" · "), criteria: b.items.map((it) => it.criteria).filter(Boolean).join(" "),
        answer: b.items.map((it) => `${it.label}: ${answerText(it, answers[it.id])}`).join(" | "), auto: checked.length ? `${good}/${checked.length} apartats correctes` : null, score: checked.length ? good / checked.length : null };
    });
  }
  /* mostra la correcció automàtica (files item_id = "auto:…") dins de la fitxa */
  function showAuto(host, rows) {
    const LVN = { NA: "No assolit", AS: "Satisfactori", AN: "Notable", AE: "Excel·lent" };
    const box = (r) => `<div class="ws-auto"><div class="ws-auto-h">Correcció automàtica${r.level ? ` <span class="lvchip lv-${r.level}" title="${LVN[r.level] || ""}">${r.level}</span>` : ""}</div>${r.comment ? `<p>${esc(r.comment)}</p>` : ""}</div>`;
    host.querySelectorAll(".ws-auto").forEach((e) => e.remove());
    let glob = null;
    (rows || []).forEach((r) => {
      const id = String(r.item_id).replace(/^auto:/, "");
      if (id === "_global") { glob = r; return; }
      const el = host.querySelector(`[data-qblock="${CSS.escape(id)}"]`) || host.querySelector(`.ws-block[data-block="${CSS.escape(id)}"]`) || host.querySelector(`.ws-item[data-item="${CSS.escape(id)}"]`);
      if (el) el.insertAdjacentHTML("beforeend", box(r));
    });
    const ws = host.querySelector(".ws"); if (glob && ws) ws.insertAdjacentHTML("afterbegin", `<section class="ws-block ws-auto-g">${box(glob).replace("Correcció automàtica", "Correcció automàtica de la fitxa")}</section>`);
  }

  const ML = "https://cdn.jsdelivr.net/npm/mathlive@0.105.3/";
  function mlSetup() { if (G.MathfieldElement) { try { G.MathfieldElement.fontsDirectory = ML + "fonts"; G.MathfieldElement.soundsDirectory = null; } catch {} } }
  mlSetup(); G.addEventListener("DOMContentLoaded", mlSetup); G.addEventListener("load", mlSetup);

  G.FQFitxa = { render, checkItem, allItems, sciVal, htmlItems, buildItems, answerText, showAuto };
})(window);
