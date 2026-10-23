/* Llibre digital de l'alumne: accés amb codi, fitxes interactives i lliurament de fotos */
(function () {
  "use strict";
  const S = window.FQStore, F = window.FITXES || {};
  const $ = (s, r = document) => r.querySelector(s);
  const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  let settings = { auto_calc: true }, me = null, wsKey = null, wsBack = null, wsFromNav = false, cur = null;
  const LEVEL = window.FQ_LEVEL || "3r";

  /* ---------- accés ---------- */
  function showLogin(msg) {
    let el = $("#fqLogin");
    if (!el) { el = document.createElement("div"); el.id = "fqLogin"; el.className = "login"; document.body.appendChild(el); }
    el.innerHTML = `<img class="login-bg" src="../img/portada.webp" alt="Quatre alumnes fent experiments al laboratori de ciències">
    <form class="card" id="fqLoginForm" autocomplete="off">
      <div class="login-head"><span class="fq-tile" aria-hidden="true"><b>Fq</b></span><div><div class="eyebrow">${LEVEL} d'ESO · Llibre digital</div>
      <h1>Física i química per entendre el món</h1></div></div>
      <label for="fqCode">Escriu el teu codi d'accés</label>
      <input id="fqCode" name="code" placeholder="XXXX-XXXX" maxlength="9" autocapitalize="characters" spellcheck="false" required>
      <p class="err" id="fqErr">${esc(msg || "")}</p>
      <button class="btn" type="submit">Entra</button>
      ${S.mode === "demo" ? `<p class="demo"><b>Mode demostració.</b> Prova amb el codi ${LEVEL === "2n" ? "<b>DEMO-2001</b> o DEMO-2002" : LEVEL === "4t" ? "<b>DEMO-4001</b> o DEMO-4002" : "<b>DEMO-0001</b>, DEMO-0002 o DEMO-0003"}. Les respostes només es desen en aquest navegador.</p>` : `<p class="demo">El codi te'l dona el professor. Si l'has perdut, demana-li'n un de nou.</p>`}
    </form>`;
    el.hidden = false;
    $("#fqCode").addEventListener("input", (e) => { let v = e.target.value.toUpperCase().replace(/[^A-Z0-9]/g, ""); if (v.length > 4) v = v.slice(0, 4) + "-" + v.slice(4, 8); e.target.value = v; });
    $("#fqLoginForm").addEventListener("submit", async (e) => {
      e.preventDefault(); const b = e.target.querySelector("button"); b.disabled = true; $("#fqErr").textContent = "";
      try { me = await S.signInStudent($("#fqCode").value); await afterLogin(); }
      catch (err) { $("#fqErr").textContent = "Aquest codi no és correcte. Revisa'l i torna-ho a provar."; }
      finally { b.disabled = false; }
    });
    setTimeout(() => $("#fqCode") && $("#fqCode").focus(), 50);
  }
  async function afterLogin() {
    // un alumne d'un curs d'un altre nivell va al seu llibre
    try {
      const lv = S.myLevel ? await S.myLevel() : null;
      if (lv && lv !== LEVEL) {
        const url = lv === "3r" ? "/digital/" : `/${lv}/digital/`;
        await S.signOut(); me = null;
        showLogin(""); $("#fqErr").innerHTML = `Aquest codi és d'un curs de ${lv} d'ESO. Entra al teu llibre: <a href="${url}">llibrefiq3r.cat${url}</a>`;
        return;
      }
    } catch {}
    const el = $("#fqLogin"); if (el) el.hidden = true;
    try { settings = { auto_calc: true, ...(await S.getSettings()) }; } catch {}
    renderUserBar();
    window.dispatchEvent(new HashChangeEvent("hashchange"));
  }
  function renderUserBar() {
    let bar = $("#fqUser");
    if (!bar) { bar = document.createElement("div"); bar.id = "fqUser"; bar.className = "userbar"; $(".wrap").prepend(bar); }
    bar.innerHTML = `${S.mode === "demo" ? '<span class="demo-flag">Demostració</span>' : ""}<span>Hola, <b>${esc(me.display_name || "")}</b></span><button type="button" id="fqOut">Surt</button>`;
    $("#fqOut").onclick = async () => { await S.signOut(); me = null; location.hash = "#inici"; showLogin(); };
  }

  /* ---------- vista de fitxa ---------- */
  function ensureView() {
    if ($("#wsHost")) return;
    const sec = $("#vWs");
    sec.innerHTML = `<div class="wsbar"><button type="button" class="btn ghost" id="wsBack"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10 3L5 8l5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span id="wsBackL">Torna</span></button>
      <div class="vtitle"><span><span class="vk" id="wsKick"></span></span><b id="wsName"></b></div>
      <span class="wsstat" id="wsStat"></span><a class="btn ghost" id="wsPdf">Versió en PDF</a><button type="button" class="btn" id="wsSubmit">Lliura la fitxa</button></div>
      <div class="wsnote" id="wsNote" hidden></div><div id="wsHost"></div>`;
    $("#wsBack").onclick = () => { if (wsFromNav) history.back(); else location.hash = wsBack || "inici"; };
    $("#wsSubmit").onclick = submitWs;
  }
  const sdaOf = (k) => { const m = /^d(\d)/.exec(k); return m ? +m[1] : (F[k] && F[k].sda) || 0; };
  const fmtDate = (d) => d ? new Date(d).toLocaleString("ca-ES", { day: "numeric", month: "long", hour: "2-digit", minute: "2-digit" }) : "";

  async function openWs(k, fromNav, prevHash) {
    ensureView(); wsKey = k;
    if (prevHash !== undefined) { wsFromNav = !!fromNav && !!prevHash; wsBack = prevHash || ("sda" + sdaOf(k)); }
    const spec = F[k]; const n = sdaOf(k); const s = (window.SDAS || []).find((x) => x.n === n);
    document.documentElement.style.setProperty("--acc", s ? `var(${s.c})` : "var(--s6)");
    $("#wsKick").textContent = s ? `SdA ${n} · ${s.title}` : "";
    $("#wsName").textContent = spec.title;
    $("#wsBackL").textContent = (wsBack || "").startsWith("sda") ? `Torna a la SdA ${wsBack.slice(3)}` : "Torna";
    $("#wsPdf").href = "#doc-" + k;
    $("#wsHost").innerHTML = '<div class="spin" role="status" aria-label="Carregant la fitxa"></div>';
    const [answers, sub] = await Promise.all([S.loadResponses(k), S.getSubmission(k)]);
    const fbAll = sub.status !== "draft" ? await S.myFeedback(k).catch(() => []) : [];
    const auto = fbAll.filter((r) => String(r.item_id).startsWith("auto:"));
    const fb = sub.status === "returned" ? fbAll.filter((r) => !String(r.item_id).startsWith("auto:")) : [];
    const ro = sub.status === "submitted" || sub.status === "returned";
    const st = $("#wsStat"); st.className = "wsstat" + (sub.status === "submitted" ? " sub" : sub.status === "returned" ? " ret" : "");
    st.textContent = sub.status === "submitted" ? "Lliurada" : sub.status === "returned" ? "Corregida" : "Esborrany";
    $("#wsSubmit").hidden = ro; $("#wsSubmit").dataset.confirm = ""; $("#wsSubmit").textContent = "Lliura la fitxa";
    const note = $("#wsNote");
    if (sub.status === "submitted") { note.hidden = false; note.innerHTML = `Has lliurat aquesta fitxa${sub.submitted_at ? " el " + esc(fmtDate(sub.submitted_at)) : ""}. Ja no la pots modificar. ${auto.length ? "A sota de cada pregunta tens la <b>correcció automàtica</b>. " : ""}Quan el professor la revisi, hi veuràs també els seus comentaris.`; }
    else if (sub.status === "returned") { note.hidden = false; note.innerHTML = `<b>El professor t'ha retornat la fitxa corregida.</b> Llegeix els comentaris de cada apartat.`; }
    else { note.hidden = false; note.innerHTML = `Les respostes es desen soles mentre escrius. ${settings.auto_calc && (spec.html || JSON.stringify(spec.blocks).match(/"type":"(chain|sci|math)"/)) ? "Els càlculs es fan automàticament perquè puguis comprovar-los." : ""} Quan acabis, prem <b>Lliura la fitxa</b>.`; }
    cur = window.FQFitxa.render($("#wsHost"), k, {
      answers, readonly: ro, autoCalc: !!settings.auto_calc, photos: sub.photos || [], feedback: fb,
      photoUrl: (p) => S.photoUrl(p),
      onSave: async (id, val) => { st.textContent = "Desant…"; st.className = "wsstat"; try { await S.saveResponse(k, id, val); st.textContent = "Desat"; st.className = "wsstat saved"; } catch (e) { st.textContent = "No s'ha pogut desar"; st.className = "wsstat"; } },
      onPhoto: async (item, file) => { st.textContent = "Pujant la foto…"; try { await S.addPhoto(k, item, await shrink(file)); await openWs(k); } catch (e) { st.textContent = "No s'ha pogut pujar la foto"; } },
      onRemovePhoto: async (path) => { await S.removePhoto(k, path); await openWs(k); },
    });
    if (auto.length) window.FQFitxa.showAuto($("#wsHost"), auto);
    else if (sub.status === "submitted" && !autoTried[k]) { autoTried[k] = 1; runAuto(k).then((ok) => ok && wsKey === k && openWs(k)); }
  }
  const autoTried = {};
  /* correcció automàtica en lliurar la fitxa */
  async function runAuto(k) {
    const spec = F[k]; if (!spec) return false;
    const st = $("#wsStat"); const prev = st ? st.textContent : "";
    if (st) { st.textContent = "Corregint…"; st.className = "wsstat"; }
    try {
      const answers = await S.loadResponses(k);
      const items = window.FQFitxa.buildItems(spec, answers);
      await S.autoCorrect(k, spec.title, sdaOf(k), items);
      return true;
    } catch (e) { if (st) st.textContent = prev; return false; }
  }
  async function submitWs() {
    const b = $("#wsSubmit");
    if (b.dataset.confirm !== "1") { b.dataset.confirm = "1"; b.textContent = "Segur? Clica de nou per lliurar"; return; }
    b.disabled = true;
    try {
      await S.submit(wsKey); const k = wsKey; autoTried[k] = 1;
      b.textContent = "Corregint la fitxa…";
      await runAuto(k);
      await openWs(k); window.scrollTo(0, 0);
    } catch { b.textContent = "No s'ha pogut lliurar. Torna-ho a provar."; }
    finally { b.disabled = false; }
  }
  /* redueix les fotos a 1600 px (JPEG) abans de pujar-les */
  function shrink(file) {
    return new Promise((res) => {
      const img = new Image(); const url = URL.createObjectURL(file);
      img.onload = () => { const k = Math.min(1, 1600 / Math.max(img.width, img.height)); const c = document.createElement("canvas"); c.width = Math.round(img.width * k); c.height = Math.round(img.height * k);
        c.getContext("2d").drawImage(img, 0, 0, c.width, c.height); c.toBlob((b) => { URL.revokeObjectURL(url); res(b ? new File([b], "foto.jpg", { type: "image/jpeg" }) : file); }, "image/jpeg", 0.85); };
      img.onerror = () => res(file); img.src = url;
    });
  }

  /* ---------- lliurament de foto per a fitxes en PDF ---------- */
  async function photoPanel(k) {
    let p = $("#docPhotos");
    if (!p) { p = document.createElement("div"); p.id = "docPhotos"; p.className = "wsnote"; $("#vDoc .vbar").after(p); }
    if (!me || F[k] || (window.D && window.D[k] && window.D[k].t)) { p.hidden = true; return; }
    p.hidden = false; p.innerHTML = "Carregant…";
    const sub = await S.getSubmission(k); const ro = sub.status !== "draft";
    const imgs = await Promise.all((sub.photos || []).map(async (x) => `<span class="ph" data-path="${esc(x.path)}"><img alt="Foto lliurada" src="${esc(await S.photoUrl(x.path))}">${ro ? "" : '<button type="button" class="ph-x" aria-label="Treu la foto">×</button>'}</span>`));
    p.innerHTML = `<div style="display:grid;gap:8px"><b>Lliura aquest full fet a mà</b><span class="muted">Fes una foto de cada pàgina i lliura-la al professor.${sub.status === "submitted" ? " <b>Ja l'has lliurat.</b>" : sub.status === "returned" ? " <b>Corregit.</b>" : ""}</span>
      <div class="ws-photos">${imgs.join("")}${ro ? "" : `<label class="ws-cam"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 6.5h3l1.5-2h5L14 6.5h3v9.5H3z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="10" cy="11" r="3" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><span>Afegeix una foto</span><input type="file" accept="image/*" capture="environment" hidden id="docPhotoIn"></label>`}</div>
      ${!ro && (sub.photos || []).length ? '<div><button type="button" class="btn" id="docSubmit">Lliura les fotos</button></div>' : ""}</div>`;
    const inp = $("#docPhotoIn"); if (inp) inp.onchange = async () => { const f = inp.files[0]; if (!f) return; p.querySelector("b").textContent = "Pujant la foto…"; await S.addPhoto(k, "full", await shrink(f)); photoPanel(k); };
    p.querySelectorAll(".ph-x").forEach((x) => x.onclick = async () => { await S.removePhoto(k, x.closest(".ph").dataset.path); photoPanel(k); });
    const sb = $("#docSubmit"); if (sb) sb.onclick = async () => { if (sb.dataset.c !== "1") { sb.dataset.c = "1"; sb.textContent = "Segur? Clica de nou"; return; } await S.submit(k); photoPanel(k); };
  }

  /* ---------- rutes ---------- */
  let lastHash = location.hash.slice(1);
  window.FQRoute = function (h) {
    const m = /^fitxa-(\w+)$/.exec(h);
    if (!m || !F[m[1]]) return false;
    if (!me) return true;
    const prev = lastHash && !lastHash.startsWith("fitxa-") ? lastHash : null;
    window.FQShowView("ws");
    openWs(m[1], true, prev);
    return true;
  };
  window.addEventListener("hashchange", () => {
    const h = location.hash.slice(1);
    const d = /^doc-(\w+)$/.exec(h); if (d && me) photoPanel(d[1]);
    lastHash = h;
  });

  (async function start() {
    try { me = await S.init(); } catch { me = null; }
    if (!me) showLogin(); else await afterLogin();
  })();
})();
