/* Panell del docent per assignar l'adaptació (NESE) d'un alumne. Es fa servir a «Els meus cursos» (docent/)
   i a la zona del professorat de cada llibre (profe.js). Desa amb FQStore.setAdaptacions. */
(function (G) {
  "use strict";
  const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  const NAMES = { dislexia: "Dislèxia", nouvingut: "Nouvingut", basics: "Continguts bàsics", discalculia: "Discalcúlia", tdah: "TDAH", tea: "TEA" };
  const HELP = { dislexia: "Lletra d'alta llegibilitat, interlineat ampli i lectura en veu alta.", nouvingut: "Glossari amb traducció a la seva llengua, lectura en veu alta i frases model.", basics: "Exemples resolts, preguntes per passos i pistes. Només el docent el pot treure.", discalculia: "Taula de passos i calculadora a les preguntes de càlcul.", tdah: "Una pregunta per pantalla, progrés, temporitzador i pauses.", tea: "Guia anticipada de la fitxa i instruccions literals." };
  let langs = null;
  function loadLangs() {
    if (G.FQ_ADAPT) return Promise.resolve((langs = G.FQ_ADAPT.llengues || []));
    if (langs) return Promise.resolve(langs);
    return new Promise((res) => { const sc = document.createElement("script"); sc.src = "/digital/js/adaptacions-dades.js"; sc.onload = () => res((langs = (G.FQ_ADAPT || {}).llengues || [])); sc.onerror = () => res((langs = [])); document.head.appendChild(sc); });
  }
  const langName = (c) => ((langs || []).find((l) => l.codi === c) || {}).nom || c;
  const label = (a, lang) => (a && a.length ? a.map((k) => (k === "nouvingut" && lang ? `${NAMES[k]} (${langName(lang).toLowerCase()})` : NAMES[k] || k)).join(" · ") : "Sense adaptació");
  function css() {
    if (document.getElementById("adpcss")) return; const st = document.createElement("style"); st.id = "adpcss";
    st.textContent = ".adbtn{white-space:nowrap;font-size:.82rem}.adpanel{border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:grid;gap:10px;margin:4px 0}.adpanel legend{font-weight:700;padding:0 6px}.adgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:8px}.adopt{display:flex;gap:8px;align-items:flex-start;border:1px solid var(--line);border-radius:10px;padding:8px 10px;cursor:pointer}.adopt small{display:block;color:var(--muted);font-size:.78rem;line-height:1.3}.adopt input{margin-top:3px}.adlang{display:grid;gap:4px;max-width:520px}.adlang select{font:inherit;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:var(--surface,#fff);color:var(--fg)}";
    document.head.appendChild(st);
  }
  /* obre (o tanca) el panell sota la fila de l'alumne */
  async function open(btn, s, { colspan = 5, toast = () => {}, scope = document } = {}) {
    css(); await loadLangs();
    const S = G.FQStore; const tr = btn.closest("tr");
    const was = tr.nextElementSibling && tr.nextElementSibling.classList.contains("adrow");
    scope.querySelectorAll(".adrow").forEach((r) => r.remove()); scope.querySelectorAll("[data-adapt]").forEach((x) => x.setAttribute("aria-expanded", "false"));
    if (was) return;
    btn.setAttribute("aria-expanded", "true");
    const cur = new Set(s.adaptacions || []);
    const row = document.createElement("tr"); row.className = "adrow noprint";
    row.innerHTML = `<td colspan="${colspan}"><fieldset class="adpanel"><legend>Adaptació de les fitxes de ${esc(s.display_name || "")}</legend>
      <p class="note">Les fitxes del llibre digital se li carregaran sempre amb aquesta adaptació, en digital i en paper, fins que la canviïs. Es poden combinar. Si una fitxa ja és adient per a un perfil, rep l'original. L'alumne no veu el nom del perfil.</p>
      <div class="adgrid">${(S.ADAPT || Object.keys(NAMES)).map((k) => `<label class="adopt"><input type="checkbox" value="${k}"${cur.has(k) ? " checked" : ""}><span><b>${NAMES[k]}</b><small>${HELP[k]}</small></span></label>`).join("")}</div>
      <label class="adlang"${cur.has("nouvingut") ? "" : " hidden"}><b>Llengua de l'alumne</b><select data-adlang><option value="">Tria la llengua…</option>${(langs || []).map((l) => `<option value="${l.codi}"${s.adapt_idioma === l.codi ? " selected" : ""}>${esc(l.nom)} · ${esc(l.paisos)}</option>`).join("")}</select><small class="note">El glossari de cada fitxa sortirà amb la traducció en aquesta llengua o amb un enllaç al traductor.</small></label>
      <p class="note">L'alumne pot desactivar les ajudes que no li calguin. Continguts bàsics només el pots treure tu.</p>
      <div class="row"><button type="button" class="btn" data-adsave>Desa</button><button type="button" class="btn ghost" data-adnone>Treu l'adaptació</button><button type="button" class="btn ghost" data-adclose>Tanca</button></div></fieldset></td>`;
    tr.after(row);
    const nv = row.querySelector('input[value="nouvingut"]'), lg = row.querySelector(".adlang");
    nv.onchange = () => { lg.hidden = !nv.checked; };
    const close = () => { row.remove(); btn.setAttribute("aria-expanded", "false"); };
    const save = async (list) => {
      const lang = row.querySelector("[data-adlang]").value || null;
      if (list.includes("nouvingut") && !lang) { toast("Tria la llengua de l'alumne nouvingut."); row.querySelector("[data-adlang]").focus(); return; }
      try { await S.setAdaptacions(s.id, list, lang); s.adaptacions = list; s.adapt_idioma = list.includes("nouvingut") ? lang : null; btn.textContent = label(list, s.adapt_idioma); close(); toast(list.length ? "Adaptació desada." : "Adaptació treta."); }
      catch (e) { toast("No s'ha pogut desar: " + e.message); }
    };
    row.querySelector("[data-adsave]").onclick = () => save([...row.querySelectorAll(".adgrid input:checked")].map((x) => x.value));
    row.querySelector("[data-adnone]").onclick = () => save([]);
    row.querySelector("[data-adclose]").onclick = close;
  }
  G.FQAdaptUI = { open, label, loadLangs, NAMES };
})(window);
