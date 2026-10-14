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
  const typeset = (el) => { try { if (G.MathLive && G.MathLive.renderMathInElement) G.MathLive.renderMathInElement(el); } catch {} };

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

  /* ================= Fitxes convertides dels fulls (spec.html) ================= */
  function workLineHtml(ln, i, ro) {
    const dis = ro ? " disabled" : "";
    const del = ro ? "" : `<button type="button" class="wl-x" data-wdel="${i}" aria-label="Treu aquesta línia">${ICON.x}</button>`;
    if (ln.t === "math") return `<div class="wl wl-math" data-wl="${i}"><span class="wl-tag">Equació</span><div class="mtools">${ro ? "" : '<button type="button" data-ins="\\frac{#@}{#?}" title="Fracció">a/b</button><button type="button" data-ins="\\cdot 10^{#?}" title="Potència de 10">·10ⁿ</button><button type="button" data-ins="#@^{#?}" title="Potència">xⁿ</button><button type="button" data-ins="\\cdot" title="Per">·</button><button type="button" data-ins="\\left(#?\\right)" title="Parèntesis">( )</button><button type="button" data-ins="\\sqrt{#?}" title="Arrel">√</button><button type="button" data-ins="\\Delta" title="Increment">Δ</button>'}</div><math-field class="mf" math-virtual-keyboard-policy="manual"${ro ? " read-only" : ""}>${esc(ln.v || "")}</math-field><output class="ws-calc" data-calc></output>${del}</div>`;
    if (ln.t === "chain") {
      const fs = ln.factors && ln.factors.length ? ln.factors : [{ nv: "", nu: "", dv: "", du: "" }];
      return `<div class="wl wl-chain" data-wl="${i}"><span class="wl-tag">Factors de conversió</span><div class="ws-chain"><span class="ws-final"><input class="ws-in v" inputmode="decimal" data-ck="sv" value="${esc(ln.sv || "")}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-ck="su" value="${esc(ln.su || "")}" placeholder="unitat"${dis}></span>${fs.map((f, j) => `<span class="dot">·</span><span class="frac" data-f="${j}"><span class="fn"><input class="ws-in v" inputmode="decimal" data-fk="nv" value="${esc(f.nv)}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-fk="nu" value="${esc(f.nu)}" placeholder="unitat"${dis}></span><span class="fd"><input class="ws-in v" inputmode="decimal" data-fk="dv" value="${esc(f.dv)}" placeholder="valor"${dis}><input class="ws-in u" list="fq-units" data-fk="du" value="${esc(f.du)}" placeholder="unitat"${dis}></span>${ro ? "" : `<button type="button" class="fx" data-fdel="${j}" aria-label="Treu el factor">${ICON.x}</button>`}<i class="fchk" data-fchk="${j}"></i></span>`).join("")}${ro ? "" : '<button type="button" class="addf" data-fadd>+ factor</button>'}<span class="eq">=</span><span class="ws-final"><input class="ws-in v" inputmode="decimal" data-ck="rv" value="${esc(ln.rv || "")}" placeholder="resultat"${dis}><input class="ws-in u" list="fq-units" data-ck="ru" value="${esc(ln.ru || "")}" placeholder="unitat"${dis}></span></div><output class="ws-calc" data-calc></output>${del}</div>`;
    }
    return `<div class="wl wl-text" data-wl="${i}"><textarea class="ws-text" rows="${ln.rows || 2}" data-wt${dis}>${esc(ln.v || "")}</textarea>${i > 0 ? del : ""}</div>`;
  }
  function workHtml(fid, f, a, ro) {
    const lines = a && a.lines && a.lines.length ? a.lines : [{ t: "text", v: "", rows: f.rows || 2 }];
    if (ro && !(a && a.lines)) return `<div class="work ro" data-fid="${fid}"><div class="wl wl-text"><textarea class="ws-text" rows="${f.rows || 2}" disabled></textarea></div></div>`;
    return `<div class="work" data-fid="${fid}">${lines.map((ln, i) => workLineHtml(ln, i, ro)).join("")}${ro || f.plain ? "" : `<div class="wadd"><button type="button" data-wadd="text">+ text</button><button type="button" data-wadd="math">+ equació</button><button type="button" data-wadd="chain">+ factors de conversió</button></div>`}</div>`;
  }
  function photoFieldHtml(fid, f, photos, ro) {
    const ps = photos.filter((p) => p.item === fid);
    if (ro && !ps.length) return `<span class="muted">(sense foto)</span>`;
    return `<div class="ws-photos" data-photos="${fid}">${ps.map((p) => `<span class="ph" data-path="${esc(p.path)}"><img alt="Foto adjunta" data-src="${esc(p.path)}">${ro ? "" : `<button type="button" class="ph-x" aria-label="Treu la foto">${ICON.x}</button>`}</span>`).join("")}${ro ? "" : `<label class="ws-cam">${ICON.cam}<span>${f.label && f.label.length < 40 ? "Foto: " + esc(f.label) : "Puja una foto del dibuix"}</span><input type="file" accept="image/*" capture="environment" data-photo-item="${fid}" hidden></label>`}</div>`;
  }
  function fieldHtml(fid, f, a, ro, photos) {
    const dis = ro ? " disabled" : "";
    switch (f.k) {
      case "work": return workHtml(fid, f, a, ro);
      case "cell": if (f.opts) return `<select class="ws-in cellf" data-cf="${fid}"${dis}><option value=""></option>${f.opts.map((o) => `<option${a && a.v === o ? " selected" : ""}>${esc(o)}</option>`).join("")}</select>`;
        return `<input class="ws-in cellf" data-cf="${fid}" value="${esc((a && a.v) || "")}"${dis} aria-label="Resposta">`;
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
    const photos = opts.photos || []; const fb = {}; (opts.feedback || []).forEach((f) => (fb[f.item_id] = f));
    const timers = {};
    const save = (fid, val) => { answers[fid] = val; if (ro) return; clearTimeout(timers[fid]); timers[fid] = setTimeout(() => opts.onSave && opts.onSave(fid, val), 600); };
    const wrap = document.createElement("div"); wrap.innerHTML = spec.html;
    wrap.querySelectorAll(".fld[data-fid]").forEach((el) => { const id = el.dataset.fid; const f = spec.fields[id]; if (!f) return; const t = document.createElement("span"); t.innerHTML = fieldHtml(id, f, answers[id], ro, photos); el.replaceWith(...t.childNodes); });
    wrap.querySelectorAll("[data-qblock]").forEach((b) => { const f = fb[b.dataset.qblock]; if (f && (f.level || f.comment)) b.insertAdjacentHTML("beforeend", `<div class="ws-fb">${f.level ? `<span class="lvchip lv-${f.level}">${f.level}</span>` : ""}<span>${esc(f.comment || "")}</span></div>`); });
    host.innerHTML = `<div class="ws wsh">${wrap.innerHTML}${fb._global && (fb._global.level || fb._global.comment) ? `<div class="ws-fb">${fb._global.level ? `<span class="lvchip lv-${fb._global.level}">${fb._global.level}</span>` : ""}<span>${esc(fb._global.comment || "")}</span></div>` : ""}</div>`;
    typeset(host);
    host.querySelectorAll("img[data-src]").forEach(async (img) => { try { img.src = await opts.photoUrl(img.dataset.src); } catch {} });
    drawRadar(host, spec, answers);

    const readWork = (w) => ({ lines: [...w.querySelectorAll(":scope > .wl")].map((l) => {
      if (l.classList.contains("wl-math")) return { t: "math", v: l.querySelector("math-field").value };
      if (l.classList.contains("wl-chain")) { const g = (k) => (l.querySelector(`[data-ck="${k}"]`) || {}).value || ""; return { t: "chain", sv: g("sv"), su: g("su"), rv: g("rv"), ru: g("ru"), factors: [...l.querySelectorAll("[data-f]")].map((fr) => { const q = (k) => fr.querySelector(`[data-fk="${k}"]`).value; return { nv: q("nv"), nu: q("nu"), dv: q("dv"), du: q("du") }; }) }; }
      const ta = l.querySelector("textarea"); return { t: "text", v: ta.value, rows: +ta.getAttribute("rows") || 2 };
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

    host.addEventListener("input", (e) => {
      const w = e.target.closest(".work");
      if (w) { const l = e.target.closest(".wl"); if (l) calcLine(l); save(w.dataset.fid, readWork(w)); return; }
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
      const w = e.target.closest(".work"); if (!w) return;
      const st = readWork(w);
      const wa = e.target.closest("[data-wadd]"), wd = e.target.closest("[data-wdel]"), fa = e.target.closest("[data-fadd]"), fd = e.target.closest("[data-fdel]");
      if (!(wa || wd || fa || fd)) return;
      if (wa) st.lines.push(wa.dataset.wadd === "text" ? { t: "text", v: "", rows: 2 } : wa.dataset.wadd === "math" ? { t: "math", v: "" } : { t: "chain", factors: [{ nv: "", nu: "", dv: "", du: "" }] });
      if (wd) st.lines.splice(+wd.dataset.wdel, 1);
      const li = (fa || fd) ? +e.target.closest(".wl").dataset.wl : -1;
      if (fa) st.lines[li].factors.push({ nv: "", nu: "", dv: "", du: "" });
      if (fd) st.lines[li].factors.splice(+fd.dataset.fdel, 1);
      const t = document.createElement("div"); t.innerHTML = workHtml(w.dataset.fid, spec.fields[w.dataset.fid], st, false); const nw = t.firstElementChild; w.replaceWith(nw);
      nw.querySelectorAll(".wl-math, .wl-chain").forEach(calcLine); save(nw.dataset.fid, st);
      if (wa) { const last = nw.querySelectorAll(".wl"); const el = last[last.length - 1]; const f = el.querySelector("math-field, input, textarea"); if (f) setTimeout(() => f.focus(), 30); }
    });
    return { answers, setAuto(v) { auto = v; host.querySelectorAll(".wl-math, .wl-chain").forEach(calcLine); } };
  }
  function answerSummary(spec, fid, a) {
    const f = spec.fields[fid]; if (!a) return "";
    if (f.k === "work") return (a.lines || []).map((l) => l.t === "math" ? `[${l.v}]` : l.t === "chain" ? `${l.sv} ${l.su} ${(l.factors || []).map((x) => `·(${x.nv} ${x.nu})/(${x.dv} ${x.du})`).join(" ")} = ${l.rv} ${l.ru}` : l.v).filter(Boolean).join(" | ");
    if (f.k === "check") return a.v ? "[x]" : "[ ]";
    return String(a.v ?? "");
  }
  function htmlItems(spec, answers) {
    return Object.entries(spec.qs).map(([q, prompt]) => {
      const fids = Object.keys(spec.fields).filter((k) => spec.fields[k].q === q);
      return { id: q, prompt, answer: fids.map((k) => answerSummary(spec, k, answers[k])).filter(Boolean).join(" · ") || "(sense resposta)", photos: fids.filter((k) => spec.fields[k].k === "photo").length };
    });
  }

  const ML = "https://cdn.jsdelivr.net/npm/mathlive@0.105.3/";
  function mlSetup() { if (G.MathfieldElement) { try { G.MathfieldElement.fontsDirectory = ML + "fonts"; G.MathfieldElement.soundsDirectory = null; } catch {} } }
  mlSetup(); G.addEventListener("DOMContentLoaded", mlSetup); G.addEventListener("load", mlSetup);

  G.FQFitxa = { render, checkItem, allItems, sciVal, htmlItems };
})(window);
