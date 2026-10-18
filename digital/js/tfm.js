/* Eines interactives de les fitxes digitals:
   - [data-widget="tfm"]: microscòpia de forces de tracció (superposar les làmines A i B, alinear les creus i mesurar desplaçaments).
   - svg[data-ruler]: regle sobre una figura (mides en mm del full imprès a escala 100 %). */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const el = (n, a = {}, p) => { const e = document.createElementNS(NS, n); for (const k in a) e.setAttribute(k, a[k]); if (p) p.appendChild(e); return e; };
  const fmt = (v) => v.toFixed(1).replace(".", ",");
  const ptIn = (svg, ev) => { const p = svg.createSVGPoint(); p.x = ev.clientX; p.y = ev.clientY; return p.matrixTransform(svg.getScreenCTM().inverse()); };

  // ---- regle i fletxes persistents sobre un svg (unitats = mm) ----
  function rulerLayer(svg, opts = {}) {
    const layer = el("g", { class: "fq-ruler" }, svg);
    const marks = [];
    let cur = null, on = true, color = "#F27C29";
    const snap = opts.snap || (() => null);
    const label = (x1, y1, x2, y2, g) => {
      const L = Math.hypot(x2 - x1, y2 - y1);
      const t = el("text", { x: (x1 + x2) / 2 + 1.5, y: (y1 + y2) / 2 - 1.5, "font-size": 3.4, "font-weight": 700, fill: color, stroke: "#fff", "stroke-width": .7, "paint-order": "stroke" }, g);
      t.textContent = fmt(L) + " mm"; return L;
    };
    const draw = (g, x1, y1, x2, y2) => {
      g.innerHTML = "";
      const a = Math.atan2(y2 - y1, x2 - x1), h = 1.8;
      el("line", { x1, y1, x2, y2, stroke: color, "stroke-width": .55, "stroke-linecap": "round" }, g);
      el("path", { d: `M${x2} ${y2} L${x2 - h * Math.cos(a - .45)} ${y2 - h * Math.sin(a - .45)} M${x2} ${y2} L${x2 - h * Math.cos(a + .45)} ${y2 - h * Math.sin(a + .45)}`, stroke: color, "stroke-width": .55, fill: "none", "stroke-linecap": "round" }, g);
      return label(x1, y1, x2, y2, g);
    };
    const pick = (ev) => { const p = ptIn(svg, ev); const s = snap(p.x, p.y); return s || { x: p.x, y: p.y }; };
    svg.addEventListener("pointerdown", (ev) => {
      if (!on) return; ev.preventDefault();
      const p = pick(ev); cur = { x1: p.x, y1: p.y, g: el("g", {}, layer) };
      svg.setPointerCapture(ev.pointerId);
    });
    svg.addEventListener("pointermove", (ev) => { if (!cur) return; const p = pick(ev); cur.L = draw(cur.g, cur.x1, cur.y1, p.x, p.y); });
    svg.addEventListener("pointerup", () => {
      if (!cur) return;
      if (!cur.L || cur.L < 0.4) cur.g.remove(); else { marks.push(cur.L); opts.onMark && opts.onMark(marks); }
      cur = null;
    });
    return {
      set on(v) { on = v; svg.style.cursor = v ? "crosshair" : ""; }, get on() { return on; },
      set color(c) { color = c; },
      clear() { layer.innerHTML = ""; marks.length = 0; opts.onMark && opts.onMark(marks); },
      marks,
    };
  }

  const css = `
  .fq-tool{border:1px solid #d8dde3;border-radius:12px;background:#fff;padding:12px;margin:12px 0}
  .fq-tool h4{margin:0 0 6px;font-size:15px}
  .fq-tool .bar{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:8px 0}
  .fq-tool button{font:inherit;font-size:13px;border:1px solid #c9ccd1;background:#f6f7f9;border-radius:999px;padding:5px 11px;cursor:pointer}
  .fq-tool button.on{background:#CE4555;border-color:#CE4555;color:#fff}
  .fq-tool label{font-size:13px;display:inline-flex;gap:5px;align-items:center}
  .fq-tool .stage{overflow:auto;border-radius:8px;max-height:78vh;touch-action:none}
  .fq-tool .stage svg{display:block;user-select:none;-webkit-user-select:none}
  .fq-tool .msg{font-size:13px;color:#5d646d;min-height:1.3em}
  .fq-tool .msg.ok{color:#1d7a46;font-weight:600}
  .fq-tool .log{font-size:13px;margin-top:6px;color:#1f2328}`;
  function addCss() { if (document.getElementById("fq-tool-css")) return; const s = document.createElement("style"); s.id = "fq-tool-css"; s.textContent = css; document.head.appendChild(s); }

  // ---- microscòpia de forces de tracció ----
  function tfm(host) {
    if (host.dataset.ready) return; host.dataset.ready = 1; addCss();
    const C = JSON.parse(host.dataset.cfg);
    const SC = C.sc, W = 40 * SC, GREEN = "#3DDC84", MAG = "#E040C8";
    host.className = "fq-tool";
    host.innerHTML = `<h4>Laboratori virtual · Superposa les làmines</h4>
      <div class="msg">La làmina A (verda) és el gel en repòs. La làmina B (magenta) és el mateix camp amb la cèl·lula enganxada. Arrossega la làmina B fins que les quatre creus coincideixin.</div>
      <div class="bar">
        <button data-a="move" class="on">✋ Mou la làmina B</button>
        <button data-a="ruler">📏 Regle i fletxes</button>
        <button data-a="clear">Esborra les fletxes</button>
        <button data-a="zoom">🔍 Amplia</button>
        <label><input type="checkbox" data-a="showA" checked> Làmina A</label>
        <label><input type="checkbox" data-a="showB" checked> Làmina B</label>
        <label>Transparència B <input type="range" min="20" max="100" value="85" data-a="op"></label>
      </div>
      <div class="stage"></div>
      <div class="msg" data-m></div>
      <div class="log" data-log></div>
      <div class="msg">El regle mesura en mil·límetres de la làmina impresa (escala 100 %). Fes clic damunt d'una boleta verda i arrossega fins a la mateixa boleta magenta: la fletxa s'enganxa al centre de les boletes. Mesura també la barra d'escala per passar de mm a µm.</div>`;
    const stage = host.querySelector(".stage");
    const svg = el("svg", { viewBox: `-6 -6 ${W + 12} ${W + 12}`, width: "100%" }, stage);
    el("style", {}, svg).textContent = "text{font-family:Atkinson Hyperlegible,Verdana,sans-serif}";
    const cross = (g, cx, cy, ink) => el("path", { d: `M${cx - 3} ${cy} H${cx + 3} M${cx} ${cy - 3} V${cy + 3}`, stroke: ink, "stroke-width": .5 }, g);
    const bead = (g, x, y, r, col) => { el("circle", { cx: x, cy: y, r: r * 2, fill: col, opacity: .28 }, g); el("circle", { cx: x, cy: y, r, fill: col }, g); };
    const corners = [[4, 4], [W - 4, 4], [4, W - 4], [W - 4, W - 4]];
    // làmina A
    const gA = el("g", {}, svg);
    el("rect", { x: 0, y: 0, width: W, height: W, fill: "#10151c" }, gA);
    corners.forEach(([x, y]) => cross(gA, x, y, "#fff"));
    C.field.forEach(([x, y]) => bead(gA, x * SC, y * SC, 1.0, GREEN));
    const snapPts = [];
    C.field.forEach(([x, y]) => snapPts.push([x * SC, y * SC]));
    for (const n in C.marked) { const [x, y] = C.marked[n]; bead(gA, x * SC, y * SC, 1.2, GREEN); snapPts.push([x * SC, y * SC]); const t = el("text", { x: x * SC + 2.6, y: y * SC - 2.2, "font-size": 3.6, "font-weight": 700, fill: "#fff" }, gA); t.textContent = n; }
    const bx = W - 4 - 10 * SC;
    el("line", { x1: bx, y1: W - 6, x2: W - 4, y2: W - 6, stroke: "#fff", "stroke-width": 1 }, gA);
    const tA = el("text", { x: bx + 5 * SC, y: W - 8, "text-anchor": "middle", "font-size": 3.6, "font-weight": 700, fill: "#fff" }, gA); tA.textContent = "10 µm";
    snapPts.push([bx, W - 6], [W - 4, W - 6]);
    // làmina B (acetat)
    const gB = el("g", { style: "cursor:grab" }, svg);
    const gBi = el("g", { style: "mix-blend-mode:screen" }, gB);
    el("rect", { x: 0, y: 0, width: W, height: W, fill: "rgba(255,255,255,0.001)", stroke: MAG, "stroke-width": .6 }, gBi);
    corners.forEach(([x, y]) => cross(gBi, x, y, MAG));
    C.field.forEach(([x, y]) => bead(gBi, x * SC, y * SC, 1.0, MAG));
    const cx = C.cell[0] * SC, cy = C.cell[1] * SC, a = C.cell[2] * SC, b2 = C.cell[3] * SC;
    el("path", { d: `M${cx - a} ${cy} C ${cx - a} ${cy - b2}, ${cx + a} ${cy - b2}, ${cx + a} ${cy} C ${cx + a} ${cy + b2}, ${cx - a} ${cy + b2}, ${cx - a} ${cy} Z`, fill: "none", stroke: MAG, "stroke-width": .7, "stroke-dasharray": "2 1.2" }, gBi);
    const tc = el("text", { x: cx, y: cy + 1.5, "text-anchor": "middle", "font-size": 3.6, fill: MAG }, gBi); tc.textContent = "contorn de la cèl·lula";
    const after = [];
    for (const n in C.marked) { const [x, y, dx, dy] = C.marked[n]; const px = (x + dx) * SC, py = (y + dy) * SC; bead(gBi, px, py, 1.2, MAG); after.push([px, py]); const t = el("text", { x: px + 2.6, y: py - 2.2, "font-size": 3.6, "font-weight": 700, fill: MAG }, gBi); t.textContent = n; }
    let off = { x: 23, y: -15 };
    const place = () => gB.setAttribute("transform", `translate(${off.x} ${off.y})`);
    place();
    const msg = host.querySelector("[data-m]"), log = host.querySelector("[data-log]");
    const aligned = () => Math.hypot(off.x, off.y) < 0.01;
    const status = () => {
      if (aligned()) { msg.className = "msg ok"; msg.textContent = "✓ Creus alineades. On les boletes coincideixen, el verd i el magenta es veuen blancs. Quines boletes no coincideixen? Ara fes servir el regle."; }
      else { msg.className = "msg"; msg.textContent = `Les creus encara no coincideixen (desfasament ${fmt(Math.hypot(off.x, off.y))} mm).`; }
    };
    status();
    // arrossegar B
    let drag = null, mode = "move";
    gB.addEventListener("pointerdown", (ev) => { if (mode !== "move") return; ev.preventDefault(); ev.stopPropagation(); const p = ptIn(svg, ev); drag = { x: p.x - off.x, y: p.y - off.y }; gB.setPointerCapture(ev.pointerId); gB.style.cursor = "grabbing"; });
    gB.addEventListener("pointermove", (ev) => { if (!drag) return; const p = ptIn(svg, ev); off = { x: p.x - drag.x, y: p.y - drag.y }; if (Math.hypot(off.x, off.y) < 1.6) off = { x: 0, y: 0 }; place(); status(); });
    gB.addEventListener("pointerup", () => { drag = null; gB.style.cursor = "grab"; });
    // regle (per sobre de tot)
    const ruler = rulerLayer(svg, {
      snap: (x, y) => {
        let best = null, bd = 2.6;
        const cand = snapPts.concat(aligned() ? after : after.map(([px, py]) => [px + off.x, py + off.y]));
        for (const [px, py] of cand) { const d = Math.hypot(px - x, py - y); if (d < bd) { bd = d; best = { x: px, y: py }; } }
        return best;
      },
      onMark: (m) => { log.innerHTML = m.length ? "<b>Mesures:</b> " + m.map((L, i) => `${i + 1}) ${fmt(L)} mm`).join(" · ") : ""; },
    });
    ruler.on = false;
    const btn = (k) => host.querySelector(`[data-a="${k}"]`);
    const setMode = (m) => { mode = m; btn("move").classList.toggle("on", m === "move"); btn("ruler").classList.toggle("on", m === "ruler"); ruler.on = m === "ruler"; gB.style.pointerEvents = m === "move" ? "" : "none"; gB.style.cursor = m === "move" ? "grab" : ""; };
    btn("move").onclick = () => setMode("move");
    btn("ruler").onclick = () => setMode("ruler");
    btn("clear").onclick = () => ruler.clear();
    let z = false;
    btn("zoom").onclick = () => { z = !z; svg.setAttribute("width", z ? "220%" : "100%"); btn("zoom").textContent = z ? "🔍 Redueix" : "🔍 Amplia"; };
    btn("showA").onchange = (e) => { gA.style.display = e.target.checked ? "" : "none"; };
    btn("showB").onchange = (e) => { gB.style.display = e.target.checked ? "" : "none"; };
    btn("op").oninput = (e) => { gBi.style.opacity = e.target.value / 100; };
    gBi.style.opacity = .85;
    setMode("move");
  }

  // ---- regle genèric sobre figures ----
  function ruler(svg) {
    if (svg.dataset.ready) return; svg.dataset.ready = 1; addCss();
    const box = document.createElement("div"); box.className = "fq-tool";
    box.innerHTML = `<div class="bar"><button data-a="ruler">📏 Regle</button><button data-a="c2">Canvia el color</button><button data-a="clear">Esborra</button><button data-a="zoom">🔍 Amplia</button></div><div class="stage"></div><div class="log" data-log></div><div class="msg">Activa el regle, fes clic i arrossega: la mida surt en mil·límetres del full imprès (escala 100 %). Les línies es queden dibuixades.</div>`;
    svg.parentNode.insertBefore(box, svg);
    box.querySelector(".stage").appendChild(svg);
    const w0 = svg.getAttribute("width");
    svg.removeAttribute("height"); svg.setAttribute("width", "100%"); svg.style.maxWidth = "none";
    const log = box.querySelector("[data-log]");
    const r = rulerLayer(svg, { onMark: (m) => { log.innerHTML = m.length ? "<b>Mesures:</b> " + m.map((L, i) => `${i + 1}) ${fmt(L)} mm`).join(" · ") : ""; } });
    r.on = false;
    const b = (k) => box.querySelector(`[data-a="${k}"]`);
    b("ruler").onclick = () => { r.on = !r.on; b("ruler").classList.toggle("on", r.on); };
    const cols = ["#F27C29", "#2989E4", "#CE4555"]; let ci = 0;
    b("c2").onclick = () => { ci = (ci + 1) % cols.length; r.color = cols[ci]; b("c2").style.color = cols[ci]; };
    b("clear").onclick = () => r.clear();
    let z = false;
    b("zoom").onclick = () => { z = !z; svg.setAttribute("width", z ? "200%" : "100%"); b("zoom").textContent = z ? "🔍 Redueix" : "🔍 Amplia"; };
    void w0;
  }

  window.FQWidgets = (window.FQWidgets || []).concat([(host) => {
    host.querySelectorAll('[data-widget="tfm"]').forEach(tfm);
    host.querySelectorAll("svg[data-ruler]").forEach(ruler);
  }]);
})();
