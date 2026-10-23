/* Zona del professorat de la versió digital */
(function () {
  "use strict";
  const S = window.FQStore, F = window.FITXES || {}, DOCS = window.DOCS || {}, FX = window.FQFitxa;
  let app = document.getElementById("app");
  const EMBED = !!window.FQ_EMBED;
  const $ = (s, r = document) => r.querySelector(s);
  const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  const LV = ["NA", "AS", "AN", "AE"];
  const STATUS = { draft: ["Esborrany", "draft"], submitted: ["Lliurada", "sub"], returned: ["Retornada", "ret"] };
  let tab = "revisar", students = [], subs = [], respKeys = [], settings = {}, curWs = null, curStu = null, curSda = null, fbAll = [], errAll = [], segStu = null, courses = [], queue = null;
  const toast = (t) => { const el = $("#toast"); el.textContent = t; el.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => (el.hidden = true), 3500); };
  const titleOf = (k) => (F[k] && F[k].title) || (DOCS[k] && `SdA ${DOCS[k].sda} · ${DOCS[k].l}`) || k;
  const sdaOf = (k) => (F[k] && F[k].sda) || (DOCS[k] && DOCS[k].sda) || 0;
  const DOCENT_URL = window.FQ_DOCENT_URL || "../docent/";
  const curName = () => (courses.find((c) => c.id === S.curCourse()) || {}).name || "";
  /* lliuraments que el docent encara no ha revisat (ja corregits per la IA o pendents), del més antic al més nou */
  const pending = () => subs.filter((x) => x.status === "submitted" && x.review !== "done")
    .sort((a, b) => String(a.submitted_at || "").localeCompare(String(b.submitted_at || "")));

  /* ---------- accés ---------- */
  function loginView(msg) {
    app.innerHTML = `<form class="card login" id="lf"><div class="eyebrow">Física i química · ${LEVEL} d'ESO</div><h1>Zona del professorat</h1>
      ${S.mode === "demo" ? `<p class="note"><b>Mode demostració.</b> Les dades es guarden només en aquest navegador.</p><label class="f">Usuari<input id="le" required></label><label class="f">Contrasenya<input type="password" id="lp" required></label>` :
      `<label class="f">Usuari<input id="le" autocomplete="username" required></label><label class="f">Contrasenya<input type="password" id="lp" autocomplete="current-password" required></label>`}
      <p class="err" id="lerr">${esc(msg || "")}</p><button class="btn" type="submit">Entra</button></form>`;
    $("#lf").onsubmit = async (e) => {
      e.preventDefault();
      try { await S.signInTeacher($("#le").value, $("#lp").value); await boot(); }
      catch (err) { $("#lerr").textContent = err.message === "not_teacher" ? "Aquest compte no és de professorat." : "Usuari o contrasenya incorrectes."; }
    };
  }
  /* cada llibre digital treballa amb els cursos del seu nivell (3r per defecte; 2n posa window.FQ_LEVEL) */
  const LEVEL = window.FQ_LEVEL || "3r";
  async function loadCourses() {
    courses = (await S.listCourses()).filter((c) => c.level === LEVEL);
    if (!courses.some((c) => c.id === S.curCourse())) S.setCourse(courses[0] ? courses[0].id : null);
  }
  async function loadData() {
    const sids = new Set((students = await S.listStudents()).map((s) => s.id));
    const [sb, rk, st] = await Promise.all([S.listSubmissions(), S.listResponseKeys(), S.getSettings()]);
    subs = sb.filter((x) => sids.has(x.student_id)); respKeys = rk.filter((x) => sids.has(x.student_id)); settings = st;
    await loadSeg();
  }
  async function boot() {
    await loadCourses();
    if (S.curCourse()) await loadData(); else { students = []; subs = []; respKeys = []; settings = {}; }
    shell();
  }
  function shell() {
    const cur = S.curCourse(); const nq = pending().length; const me = S.me() || {};
    const courseSel = courses.length ? `<label class="cursel">Curs <select id="curs">${courses.map((c) => `<option value="${c.id}"${c.id === cur ? " selected" : ""}>${esc(c.name)}${me.role === "admin" && c.teacher_id !== me.id ? ` · ${esc(c.teacher_name)}` : ""}</option>`).join("")}</select></label>` : "";
    app.innerHTML = `<header class="top dtop"><div><div class="eyebrow">Zona del professorat · ${S.mode === "demo" ? "demostració" : "llibre digital"} · ${esc(me.display_name || "")}</div><h2 class="dh">Llibre digital de l'alumnat</h2></div>
      <div class="row noprint">${courseSel}<a class="btn ghost" href="${DOCENT_URL}">Els meus cursos</a>${EMBED ? '<a class="btn ghost" href="#inici">← Portada del professorat</a>' : ""}<a class="btn ghost" href="./" target="_blank" rel="noopener">Obre el llibre de l'alumnat</a>${EMBED ? "" : '<button class="btn ghost" id="out">Surt</button>'}</div></header>
      ${cur ? `<nav class="tabs noprint" role="tablist">${[["revisar", `Per revisar${nq ? ` <span class="qn">${nq}</span>` : ""}`], ["fitxes", "Fitxes i lliuraments"], ["seguiment", "Seguiment de l'alumnat"], ["alumnat", "Alumnat i codis"], ["ajustos", "Ajustos"]].map(([k, l]) => `<button role="tab" data-tab="${k}" aria-selected="${tab === k}">${l}</button>`).join("")}</nav>
      <main id="main"></main>` : `<section class="card"><h2>Encara no tens cap curs de ${LEVEL} d'ESO</h2><p class="note">Crea'l a <a href="${DOCENT_URL}">Els meus cursos</a>: tria el nivell, posa-li nom i afegeix-hi l'alumnat.</p></section>`}`;
    if ($("#out")) $("#out").onclick = async () => { await S.signOut(); loginView(); };
    if ($("#curs")) $("#curs").onchange = async (e) => { S.setCourse(e.target.value); curWs = null; curStu = null; queue = null; $("#main").innerHTML = '<div class="spin"></div>'; await loadData(); shell(); };
    if (!cur) return;
    app.querySelectorAll("[data-tab]").forEach((b) => (b.onclick = () => { tab = b.dataset.tab; curWs = null; curStu = null; queue = null; shell(); }));
    ({ revisar: queueView, fitxes: fitxesView, seguiment: segView, alumnat: alumnatView, ajustos: ajustosView })[tab]();
  }

  /* ---------- ajustos ---------- */
  function ajustosView() {
    $("#main").innerHTML = `<section class="card"><h2>Ajudes a l'alumnat de ${esc(curName())}</h2>
      <label class="switch"><input type="checkbox" id="ac"${settings.auto_calc !== false ? " checked" : ""}> Càlcul automàtic a les fitxes</label>
      <p class="note">Si està activat, quan l'alumne escriu números o factors de conversió, la fitxa li mostra el resultat del càlcul i si cada factor val 1. Desactiva-ho per a les activitats d'avaluació. Aquest ajust només afecta aquest curs.</p></section>
      <section class="card" id="pdfp" hidden></section>
      <section class="card"><h2>Correcció automàtica</h2><p class="note">Quan l'alumne lliura una fitxa digital, rep de seguida la correcció de cada pregunta (nivell i comentari breu):</p>
        <ul class="note"><li>Els càlculs, les taules i les preguntes tancades es corregeixen sols, sense IA.</li><li>Les respostes raonades les corregeix una IA econòmica (OpenAI gpt-5.4-nano) amb els solucionaris del professorat.</li><li>Els dibuixos en foto també els mira la IA, en baixa resolució perquè costi poc.</li><li>També valora l'ortografia en català i en corregeix algun exemple a l'alumne.</li><li>Indici de text copiat d'una IA: la IA en valora l'estil i el llibre compta els caràcters que l'alumne ha enganxat a cada resposta. Només ho veus tu, a «Per revisar». És un indici per comprovar, no una prova.</li><li>L'alumne veu de seguida la correcció de tota la fitxa. Totes les fitxes corregides van a <b>Per revisar</b>, per si vols comprovar-les; les preguntes on la IA dubta surten marcades. Les fitxes en paper les valores tu.</li></ul>
        <p class="note">Tu reps la mateixa valoració com a proposta a cada apartat: la pots canviar i decideixes quan retornar la fitxa amb la teva valoració. Els errors es classifiquen per tipus a «Seguiment de l'alumnat».${S.mode === "demo" ? " En mode demostració, la correcció es basa només en la comprovació automàtica dels càlculs." : ""}</p>
        <p class="note" id="usage"></p></section>`;
    S.usage().then((u) => { const el = $("#usage"); if (el && S.mode !== "demo") el.innerHTML = `Despesa aproximada de la IA aquest mes (tots els cursos): <b>${(u.usd || 0).toLocaleString("ca-ES", { style: "currency", currency: "USD", maximumFractionDigits: 2 })}</b> en ${u.calls || 0} correccions.`; }).catch(() => {});
    if (window.fqTeacherFiles && S.mode !== "demo") pdfPanel();
    $("#ac").onchange = async (e) => { try { await S.setSetting("auto_calc", e.target.checked); settings.auto_calc = e.target.checked; toast(e.target.checked ? "Càlcul automàtic activat." : "Càlcul automàtic desactivat."); } catch { toast("No s'ha pogut desar."); } };
  }

  async function pdfPanel() {
    const box = $("#pdfp"); box.hidden = false;
    const need = window.fqTeacherFiles(); const have = new Set(await window.fqListUploaded());
    const missing = need.filter((f) => !have.has(f));
    box.innerHTML = `<h2>PDF del professorat</h2><p class="note">Les proves, els solucionaris i les adaptacions es guarden en un espai privat que només pot obrir el professorat. ${missing.length ? `En falten <b>${missing.length}</b> de ${need.length}.` : `Hi són tots (${need.length}).`}</p>
      <label class="btn ghost" style="justify-self:start">Puja PDF del professorat<input type="file" accept="application/pdf" multiple hidden id="pdfin"></label>
      ${missing.length ? `<details><summary class="note">Quins falten?</summary><p class="note">${missing.map(esc).join("<br>")}</p></details>` : ""}`;
    $("#pdfin").onchange = async (e) => {
      const files = [...e.target.files].filter((f) => need.includes(f.name)); let ok = 0;
      for (const f of files) { try { await window.fqUpload(f); ok++; toast(`Pujant… ${ok}/${files.length}`); } catch (er) { toast("Error amb " + f.name + ": " + er.message); } }
      toast(`${ok} fitxers pujats.`); pdfPanel();
    };
  }

  /* ---------- alumnat ---------- */
  function alumnatView(created) {
    $("#main").innerHTML = `<div class="grid2"><section class="card noprint"><h2>Afegeix alumnat a ${esc(curName())}</h2>
        <label class="f">Noms (un per línia)<textarea id="names" rows="8" placeholder="Nom Cognom"></textarea></label>
        <div class="row"><button class="btn" id="add">Crea els comptes</button></div>
        <p class="note">Cada alumne rep un codi d'accés de 8 caràcters. Amb aquest codi entra al llibre digital des de qualsevol dispositiu.</p></section>
      <section class="card"><div class="row" style="justify-content:space-between"><h2>Alumnat de ${esc(curName())} (${students.length})</h2><div class="row noprint"><button class="btn ghost" id="csv">Descarrega els codis (CSV)</button><button class="btn ghost" id="prn">Imprimeix targetes</button></div></div>
        ${created && created.length ? `<p class="note" style="color:var(--ok)"><b>Comptes creats:</b> ${created.length}. Ja els tens a la llista.</p>` : ""}
        <div class="tscroll"><table class="t"><thead><tr><th>Nom</th><th>Grup</th><th>Codi</th><th class="noprint"></th></tr></thead><tbody>
        ${students.map((s) => `<tr data-id="${s.id}"><td>${esc(s.display_name)}</td><td>${esc(s.grup)}</td><td><code class="c">${esc(s.code || "—")}</code></td><td class="noprint"><div class="row"><button class="btn ghost" data-reset>Codi nou</button><button class="btn danger" data-del>Esborra</button></div></td></tr>`).join("") || `<tr><td colspan="4" class="note">Encara no hi ha alumnat. Afegeix-lo amb el formulari.</td></tr>`}
        </tbody></table></div></section></div>
      <section class="codes" id="cards" hidden>${students.map((s) => `<div class="codecard"><span>Física i química · ${LEVEL} d'ESO · llibre digital</span><b>${esc(s.display_name)}</b><code>${esc(s.code || "")}</code><span>${esc(location.origin + location.pathname.replace(/profe\.html$/, ""))}</span></div>`).join("")}</section>`;
    $("#add").onclick = async () => {
      const names = $("#names").value.split("\n").map((x) => x.trim()).filter(Boolean); if (!names.length) return;
      const b = $("#add"); b.disabled = true; b.textContent = "Creant…";
      try { const out = await S.createStudents(names); students = await S.listStudents(); alumnatView(out); }
      catch (e) { toast("No s'han pogut crear els comptes: " + e.message); b.disabled = false; b.textContent = "Crea els comptes"; }
    };
    $("#main").querySelectorAll("[data-reset]").forEach((b) => (b.onclick = async () => {
      const id = b.closest("tr").dataset.id; if (b.dataset.c !== "1") { b.dataset.c = "1"; b.textContent = "Segur? El codi antic deixarà de funcionar"; return; }
      try { await S.resetCode(id); students = await S.listStudents(); alumnatView(); toast("Codi nou creat."); } catch (e) { toast("Error: " + e.message); }
    }));
    $("#main").querySelectorAll("[data-del]").forEach((b) => (b.onclick = async () => {
      const id = b.closest("tr").dataset.id; if (b.dataset.c !== "1") { b.dataset.c = "1"; b.textContent = "Segur? S'esborren totes les respostes"; return; }
      try { await S.deleteStudent(id); students = await S.listStudents(); alumnatView(); toast("Alumne esborrat."); } catch (e) { toast("Error: " + e.message); }
    }));
    $("#csv").onclick = () => {
      const rows = [["Nom", "Grup", "Codi"], ...students.map((s) => [s.display_name, s.grup, s.code || ""])];
      const csv = "﻿" + rows.map((r) => r.map((v) => `"${String(v).replace(/"/g, '""')}"`).join(";")).join("\r\n");
      const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv" })); a.download = `codis-alumnat-${curName().replace(/[^\w-]+/g, "-")}.csv`; a.click();
    };
    $("#prn").onclick = () => { $("#cards").hidden = false; window.print(); setTimeout(() => ($("#cards").hidden = true), 500); };
  }

  /* ---------- fitxes i lliuraments ---------- */
  function fitxesView() {
    if (curWs && curStu) return reviewView();
    const keys = new Set([...Object.keys(F), ...subs.map((s) => s.worksheet_id), ...respKeys.map((r) => r.worksheet_id)]);
    const all = [...keys].sort((a, b) => sdaOf(a) - sdaOf(b) || a.localeCompare(b, undefined, { numeric: true }));
    const sdas = [...new Set(all.map(sdaOf))].sort((a, b) => a - b);
    if (curSda === null || !sdas.includes(curSda)) {
      const pend = subs.find((s) => s.status === "submitted"); curSda = pend ? sdaOf(pend.worksheet_id) : (sdas.find((n) => n > 0) ?? sdas[0] ?? 1);
    }
    const list = all.filter((k) => sdaOf(k) === curSda);
    if (!curWs || !list.includes(curWs)) curWs = list[0] || null;
    const N = students.length;
    const subOf = (sid) => subs.find((s) => s.student_id === sid && s.worksheet_id === curWs);
    const started = (sid) => respKeys.some((r) => r.student_id === sid && r.worksheet_id === curWs);
    const counts = (k) => { const ss = subs.filter((s) => s.worksheet_id === k); return { sub: ss.filter((s) => s.status === "submitted").length, ret: ss.filter((s) => s.status === "returned").length }; };
    const sdaPend = (n) => subs.filter((s) => s.status === "submitted" && sdaOf(s.worksheet_id) === n).length;
    const sdaName = (n) => { const x = (window.SDAS || []).find((y) => y.n === n); return n ? `SdA ${n}` + (x ? ` · ${x.title}` : "") : "Tot el curs"; };
    $("#main").innerHTML = `<nav class="sdachips" aria-label="Situacions d'aprenentatge">${sdas.map((n) => `<button type="button" data-sda="${n}" class="${n === curSda ? "on" : ""}" style="--c:var(--s${n || 6})">${n ? "SdA " + n : "Curs"}${sdaPend(n) ? `<span class="dot">${sdaPend(n)}</span>` : ""}</button>`).join("")}</nav>
      <div class="grid2"><section class="card"><h2>${esc(sdaName(curSda))}</h2><div class="tscroll"><table class="t"><thead><tr><th>Fitxa</th><th>Lliurades</th><th>Per revisar</th><th>Retornades</th></tr></thead><tbody>
        ${list.map((k) => { const c = counts(k); const done = c.sub + c.ret; return `<tr class="click" data-ws="${k}"${k === curWs ? ' style="background:var(--chip)"' : ""}><td>${F[k] ? '<span class="pill">digital</span> ' : '<span class="pill">foto</span> '}${esc(titleOf(k))}</td><td><b>${done}</b>/${N}<div class="bar"><i style="width:${N ? Math.round(100 * done / N) : 0}%"></i></div></td><td>${c.sub ? `<span class="pill sub">${c.sub}</span>` : "—"}</td><td>${c.ret || "—"}</td></tr>`; }).join("") || '<tr><td colspan="4" class="note">Aquesta SdA no té fitxes digitals.</td></tr>'}
        </tbody></table></div></section>
      <section class="card">${curWs ? `<h2>${esc(titleOf(curWs))}</h2><p class="note">Lliurades: <b>${counts(curWs).sub + counts(curWs).ret}/${N}</b></p><div class="tscroll"><table class="t"><thead><tr><th>Alumne/a</th><th>Grup</th><th>Estat</th><th>Nivell</th><th>Lliurada</th></tr></thead><tbody>
        ${students.map((s) => { const sb = subOf(s.id); const st = sb ? STATUS[sb.status] : started(s.id) ? STATUS.draft : null;
          return `<tr class="click" data-stu="${s.id}"><td>${esc(s.display_name)}</td><td>${esc(s.grup)}</td><td>${st ? `<span class="pill ${st[1]}">${st[0]}</span>` : '<span class="note">Sense començar</span>'}</td><td>${levelHtml(s.id, curWs, true)}</td><td>${sb && sb.submitted_at ? new Date(sb.submitted_at).toLocaleDateString("ca-ES") : ""}</td></tr>`; }).join("") || '<tr><td colspan="5" class="note">Encara no hi ha alumnat.</td></tr>'}
        </tbody></table></div>` : '<p class="note">Tria una fitxa.</p>'}</section></div>`;
    $("#main").querySelectorAll("[data-sda]").forEach((b) => (b.onclick = () => { curSda = +b.dataset.sda; curWs = null; fitxesView(); }));
    $("#main").querySelectorAll("[data-ws]").forEach((r) => (r.onclick = () => { curWs = r.dataset.ws; fitxesView(); }));
    $("#main").querySelectorAll("[data-stu]").forEach((r) => (r.onclick = () => { curStu = r.dataset.stu; reviewView(); window.scrollTo(0, 0); }));
  }

  /* ---------- per revisar: fitxes ja corregides per la IA que el docent pot comprovar una a una ---------- */
  const qKey = (x) => x.student_id + "|" + x.worksheet_id;
  /* preguntes amb indici de text copiat d'una IA (estil del text segons la IA i caràcters enganxats); només ho veu el docent */
  const iaSusp = (sid, ws) => ((errAll.find((e) => e.student_id === sid && e.worksheet_id === ws) || {}).items || [])
    .filter((it) => it.ia === "alta" || (it.ia === "mitjana" && (it.enganxat || 0) >= 40) || (it.enganxat || 0) >= 150);
  function queueView() {
    if (curWs && curStu) return reviewView();
    const list = pending(); queue = list.map(qKey);
    const nameOf = (sid) => (students.find((s) => s.id === sid) || {}).display_name || "";
    const why = (x) => { const n = (x.review_items || []).length;
      if (!F[x.worksheet_id]) return ["Fitxa en paper: valora-la tu", "sub"];
      if (!x.review) return ["Encara sense correcció", "sub"];
      return n ? [`Corregida · la IA dubta en ${n === 1 ? "1 pregunta" : n + " preguntes"}`, "sub"] : ["Corregida per la IA", "ret"]; };
    const lvOfWs = (x) => levelHtml(x.student_id, x.worksheet_id);
    $("#main").innerHTML = `<section class="card"><div class="row" style="justify-content:space-between"><h2>Per revisar (${list.length})</h2>${list.length ? '<button class="btn" id="qstart">Comença per la primera</button>' : ""}</div>
      <p class="note">Quan l'alumnat lliura una fitxa, la IA la corregeix sencera i l'alumne en veu el resultat de seguida. Aquí pots mirar què ha posat cada alumne i comprovar que la IA no s'ha equivocat. Si tot és correcte, prem <b>Bé, següent</b>; si vols canviar alguna cosa, posa-hi el teu nivell o comentari i prem <b>Retorna amb canvis</b>. Les preguntes on la IA dubta surten marcades en groc.</p>
      ${list.length ? `<div class="tscroll"><table class="t"><thead><tr><th>Alumne/a</th><th>Fitxa</th><th>Nivell</th><th>Estat</th><th>Lliurada</th></tr></thead><tbody>
        ${list.map((x, i) => { const [w, c] = why(x); const ia = iaSusp(x.student_id, x.worksheet_id).length; return `<tr class="click" data-q="${i}"><td>${esc(nameOf(x.student_id))}</td><td>${esc(titleOf(x.worksheet_id))}</td><td>${lvOfWs(x)}</td><td><span class="pill ${c}">${esc(w)}</span>${ia ? ` <span class="pill ia" title="Possible text copiat d'una IA">Possible IA en ${ia === 1 ? "1 pregunta" : ia + " preguntes"}</span>` : ""}</td><td>${x.submitted_at ? new Date(x.submitted_at).toLocaleDateString("ca-ES") : ""}</td></tr>`; }).join("")}
        </tbody></table></div>` : '<p class="note" style="color:var(--ok)"><b>Ho tens tot revisat.</b> Quan l\'alumnat lliuri fitxes noves, apareixeran aquí.</p>'}</section>`;
    const open = (i) => { const [sid, ws] = queue[i].split("|"); curStu = sid; curWs = ws; reviewView(); window.scrollTo(0, 0); };
    $("#main").querySelectorAll("[data-q]").forEach((r) => (r.onclick = () => open(+r.dataset.q)));
    if ($("#qstart")) $("#qstart").onclick = () => open(0);
  }

  async function reviewView() {
    const stu = students.find((s) => s.id === curStu); const k = curWs; const spec = F[k];
    const inQ = tab === "revisar" && queue && queue.includes(curStu + "|" + k);
    const qi = inQ ? queue.indexOf(curStu + "|" + k) : -1;
    const go = (i) => { if (i < 0 || i >= queue.length) { curStu = null; curWs = null; queueView(); return; } [curStu, curWs] = queue[i].split("|"); reviewView(); window.scrollTo(0, 0); };
    $("#main").innerHTML = '<div class="spin"></div>';
    const [answers, sub, fbRows] = await Promise.all([S.loadResponses(k, curStu), S.getSubmission(k, curStu), S.feedbackFor(curStu, k)]);
    const autoRows = fbRows.filter((r) => String(r.item_id).startsWith("auto:"));
    const fb = Object.fromEntries(fbRows.filter((r) => !String(r.item_id).startsWith("auto:")).map((r) => [r.item_id, r]));
    const st = STATUS[sub.status] || STATUS.draft;
    $("#main").innerHTML = `<div class="revhead"><button class="btn ghost" id="back">← ${inQ ? "Per revisar" : "Llista"}</button>${inQ ? `<span class="qnav"><button class="btn ghost" id="qprev"${qi > 0 ? "" : " disabled"} aria-label="Anterior">←</button><b>${qi + 1} de ${queue.length}</b><button class="btn ghost" id="qnext"${qi < queue.length - 1 ? "" : " disabled"} aria-label="Següent">→</button></span>` : ""}<h2>${esc(stu ? stu.display_name : "")} · ${esc(titleOf(k))}</h2><span class="pill ${st[1]}">${st[0]}</span>
      <button class="btn ghost" id="ai">${autoRows.length ? "Torna a corregir automàticament" : "Correcció automàtica"}</button><button class="btn ghost" id="save">Desa</button>${inQ ? '<button class="btn" id="ok">Bé, següent</button>' : ""}<button class="btn${inQ ? " ghost" : ""}" id="ret">${inQ ? "Retorna amb canvis" : "Retorna a l'alumne"}</button>${sub.status !== "draft" ? '<button class="btn ghost" id="reopen">Deixa-la modificar</button>' : ""}</div>
      <div id="rev"></div>`;
    $("#back").onclick = () => { curStu = null; curWs = null; inQ ? queueView() : fitxesView(); };
    if (inQ) { $("#qprev").onclick = () => go(qi - 1); $("#qnext").onclick = () => go(qi + 1); }
    const host = $("#rev");
    if (spec) {
      FX.render(host, k, { answers, readonly: true, autoCalc: true, showCheck: true, photos: sub.photos || [], photoUrl: (p) => S.photoUrl(p) });
      if (autoRows.length) FX.showAuto(host, autoRows);
    } else {
      const imgs = await Promise.all((sub.photos || []).map(async (p) => `<a href="${esc(await S.photoUrl(p.path))}" target="_blank" rel="noopener"><img src="${esc(await S.photoUrl(p.path))}" alt="Foto lliurada" style="max-width:100%;border-radius:10px;border:1px solid var(--line)"></a>`));
      host.innerHTML = `<div class="ws"><section class="ws-block"><b>Fotos lliurades</b>${imgs.join("") || '<p class="note">Sense fotos.</p>'}</section></div>`;
    }
    // editors de retroacció
    const targets = spec && spec.html ? Object.keys(spec.qs) : spec ? [...FX.allItems(spec).filter((it) => !it.parent).map((it) => it.id), ...spec.blocks.filter((b) => b.type === "group").map((b) => b.id)] : [];
    const editor = (id, label) => { const f = fb[id] || {}; return `<div class="fbed" data-fb="${id}"><b>${esc(label)}</b><div class="lvs">${LV.map((l) => `<button type="button" data-lv="${l}" class="${f.level === l ? "on" : ""}">${l}</button>`).join("")}</div>
      <textarea rows="2" placeholder="Comentari per a l'alumne">${esc(f.comment || "")}</textarea>${f.proposal_level || f.proposal_note ? `<div class="prop">Proposta automàtica: <b>${esc(f.proposal_level || "")}</b> ${esc(f.proposal_note || "")}<button type="button" data-accept>Fes-la servir</button></div>` : ""}</div>`; };
    targets.forEach((id) => {
      const el = host.querySelector(`[data-qblock="${CSS.escape(id)}"]`) || host.querySelector(`.ws-block[data-block="${id}"]`) || host.querySelector(`.ws-item[data-item="${id}"]`)?.closest(".ws-block");
      if (el) el.insertAdjacentHTML("beforeend", editor(id, id === "diana" ? "Valoració de la diana" : (spec.html ? "Valoració de la pregunta " : "Valoració de l'apartat ") + id));
    });
    host.insertAdjacentHTML("beforeend", `<div class="ws" style="margin-top:14px"><section class="ws-block">${editor("_global", "Valoració global de la fitxa")}</section></div>`);
    // preguntes que la correcció automàtica ha deixat per al docent
    const need = (sub.review_items || []).map(String); let first = null;
    need.forEach((id) => { const box = host.querySelector(`.fbed[data-fb="${CSS.escape(id)}"]`); if (!box) return; box.classList.add("need"); box.insertAdjacentHTML("afterbegin", '<span class="needtag">La IA dubta</span>'); first = first || box; });
    iaSusp(curStu, k).forEach((it) => { const box = host.querySelector(`.fbed[data-fb="${CSS.escape(String(it.id))}"]`); if (!box) return; box.classList.add("need"); box.insertAdjacentHTML("afterbegin", `<span class="needtag ia">Possible text d'IA${it.ia ? ` · estil ${esc(it.ia)}` : ""}${it.enganxat ? ` · ${it.enganxat} caràcters enganxats` : ""}</span>`); first = first || box; });
    if (first && inQ) setTimeout(() => first.scrollIntoView({ block: "center", behavior: "smooth" }), 150);
    host.addEventListener("click", (e) => {
      const b = e.target.closest("[data-lv]"); if (b) { const box = b.closest(".fbed"); const was = b.classList.contains("on"); box.querySelectorAll("[data-lv]").forEach((x) => x.classList.remove("on")); if (!was) b.classList.add("on"); return; }
      const acc = e.target.closest("[data-accept]"); if (acc) { const box = acc.closest(".fbed"); const f = fb[box.dataset.fb] || {}; box.querySelectorAll("[data-lv]").forEach((x) => x.classList.toggle("on", x.dataset.lv === f.proposal_level)); box.querySelector("textarea").value = f.proposal_note || ""; }
    });
    const collect = () => [...host.querySelectorAll(".fbed")].map((box) => ({ item_id: box.dataset.fb, level: box.querySelector("[data-lv].on")?.dataset.lv || null, comment: box.querySelector("textarea").value.trim() }));
    $("#save").onclick = async () => { try { await S.saveFeedback(curStu, k, collect()); toast("Valoració desada (l'alumne encara no la veu)."); } catch (e) { toast("Error: " + e.message); } };
    $("#ret").onclick = async (e) => {
      const b = e.target; if (b.dataset.c !== "1") { b.dataset.c = "1"; b.textContent = "Segur? L'alumne veurà els comentaris"; return; }
      try {
        await S.saveFeedback(curStu, k, collect()); await S.release(curStu, k); await refreshSubs(); await loadSeg(); toast("Fitxa retornada.");
        if (inQ) { queue.splice(qi, 1); go(qi); } else reviewView();
      } catch (er) { toast("Error: " + er.message); }
    };
    // revisada sense canvis: l'alumne es queda amb la correcció de la IA
    if ($("#ok")) $("#ok").onclick = async () => { try { await S.markReviewed(curStu, k); await refreshSubs(); toast("Revisada."); queue.splice(qi, 1); go(qi); } catch (er) { toast("Error: " + er.message); } };
    const ro = $("#reopen"); if (ro) ro.onclick = async () => { await S.reopen(curStu, k); await refreshSubs(); await loadSeg(); toast("L'alumne ja pot tornar a modificar la fitxa."); if (inQ) { queue.splice(qi, 1); go(qi); } else reviewView(); };
    $("#ai").onclick = async () => {
      if (!spec) { toast("Les fitxes en foto les has de valorar tu."); return; }
      const b = $("#ai"); b.disabled = true; b.textContent = "Corregint…";
      try {
        await S.autoCorrect(k, spec.title, sdaOf(k), FX.buildItems(spec, answers), curStu);
        await refreshSubs(); await loadSeg(); toast("Correcció automàtica feta. Revisa les propostes abans de retornar."); reviewView();
      } catch (e) { toast(e.message === "missing_api_key" ? "Falta configurar la clau de correcció al servidor." : "No s'ha pogut corregir: " + e.message); b.disabled = false; b.textContent = "Correcció automàtica"; }
    };
  }

  async function refreshSubs() { const sids = new Set(students.map((x) => x.id)); subs = (await S.listSubmissions()).filter((x) => sids.has(x.student_id)); }

  /* ---------- seguiment de l'alumnat: nivells, tipus d'error i progrés ---------- */
  const LVN = { NA: 1, AS: 2, AN: 3, AE: 4 };
  const LVNAME = { NA: "No assolit", AS: "Satisfactori", AN: "Notable", AE: "Excel·lent" };
  const lvFrom = (v) => v == null ? null : LV[Math.min(3, Math.max(0, Math.round(v) - 1))];
  const chip = (l, extra) => l ? `<span class="lvchip lv-${l}" title="${esc(LVNAME[l] + (extra ? " · " + extra : ""))}">${l}</span>` : '<span class="lvchip lv-none">–</span>';
  const ERRN = { conceptual: "Conceptual", "càlcul": "Càlcul", unitats: "Unitats", "notació": "Notació i xifres", procediment: "Procediment", enunciat: "Comprensió de l'enunciat", "expressió": "Expressió científica", ortografia: "Ortografia", incompleta: "Incompleta" };
  const avg = (a) => a.length ? a.reduce((x, y) => x + y, 0) / a.length : null;
  async function loadSeg() { try { [fbAll, errAll] = await Promise.all([S.allFeedback(), S.errorsAll()]); } catch { fbAll = []; errAll = []; } }
  /* nivell d'una fitxa: valoració del professor si n'hi ha; si no, la correcció automàtica */
  function wsLevel(sid, ws) {
    const rows = fbAll.filter((r) => r.student_id === sid && r.worksheet_id === ws);
    const g = rows.find((r) => r.item_id === "_global" && r.level);
    if (g) return { lv: g.level, v: LVN[g.level], src: "prof" };
    const teach = rows.filter((r) => !r.item_id.startsWith("auto:") && r.item_id !== "_global" && r.level).map((r) => LVN[r.level]);
    if (teach.length) { const v = avg(teach); return { lv: lvFrom(v), v, src: "prof" }; }
    const au = rows.filter((r) => r.item_id.startsWith("auto:") && r.item_id !== "auto:_global" && r.level).map((r) => LVN[r.level]);
    if (au.length) { const v = avg(au); return { lv: lvFrom(v), v, src: "auto" }; }
    return null;
  }  /* nivell si les preguntes amb indici d'IA compten com a NA (null si no n'hi ha cap) */
  function wsLevelIA(sid, ws) {
    const sus = new Set(iaSusp(sid, ws).map((it) => String(it.id))); if (!sus.size) return null;
    const rows = fbAll.filter((r) => r.student_id === sid && r.worksheet_id === ws);
    const teach = Object.fromEntries(rows.filter((r) => !r.item_id.startsWith("auto:") && r.item_id !== "_global" && r.level).map((r) => [r.item_id, r.level]));
    const vals = rows.filter((r) => r.item_id.startsWith("auto:") && r.item_id !== "auto:_global").map((r) => { const id = r.item_id.slice(5); const l = teach[id] || r.level; return sus.has(id) ? 1 : l ? LVN[l] : null; }).filter((v) => v != null);
    return vals.length ? lvFrom(avg(vals)) : null;
  }
  /* qualificació de la fitxa + avís d'IA + qualificació si les preguntes amb IA són NA */
  function levelHtml(sid, ws, src) {
    const L = wsLevel(sid, ws); if (!L) return "";
    const li = wsLevelIA(sid, ws);
    return chip(L.lv) + (src ? `<span class="src">${L.src === "auto" ? "auto" : "prof."}</span>` : "") + (li ? ` <span class="pill ia" title="Possible text copiat d'una IA (${iaSusp(sid, ws).length === 1 ? "1 pregunta" : iaSusp(sid, ws).length + " preguntes"})">IA</span> <span class="iaalt" title="Nivell si les preguntes amb indici d'IA compten com a NA">amb NA: ${chip(li)}</span>` : "");
  }

  function stuSummary(sid) {
    const per = {};
    for (const ws of Object.keys(F)) {
      const n = sdaOf(ws); const p = per[n] = per[n] || { sda: n, total: 0, lliurades: 0, vals: [], ws: [], errors: {} };
      p.total++;
      const sb = subs.find((x) => x.student_id === sid && x.worksheet_id === ws);
      if (sb && sb.status !== "draft") p.lliurades++;
      const L = wsLevel(sid, ws); if (L) p.vals.push(L.v);
      p.ws.push({ ws, status: sb ? sb.status : respKeys.some((r) => r.student_id === sid && r.worksheet_id === ws) ? "draft" : null, L });
    }
    errAll.filter((e) => e.student_id === sid && F[e.worksheet_id]).forEach((e) => { const p = per[e.sda || sdaOf(e.worksheet_id)]; if (!p) return; (e.items || []).forEach((it) => (it.errors || []).forEach((x) => (p.errors[x] = (p.errors[x] || 0) + 1))); });
    return Object.values(per).sort((a, b) => a.sda - b.sda).map((p) => ({ ...p, mitjana: avg(p.vals) }));
  }
  const sdaTitle = (n) => { const x = (window.SDAS || []).find((y) => y.n === n); return x ? x.title : ""; };

  function progressSvg(sm, groupMean) {
    const pts = sm.filter((p) => p.sda > 0);
    if (!pts.length) return "";
    const W = 560, H = 190, L = 92, R = 16, T = 14, B = 30;
    const x = (i) => L + (pts.length === 1 ? (W - L - R) / 2 : i * (W - L - R) / (pts.length - 1));
    const y = (v) => T + (4 - v) / 3 * (H - T - B);
    let g = "";
    LV.forEach((l, i) => { const yy = y(i + 1); g += `<line x1="${L}" x2="${W - R}" y1="${yy}" y2="${yy}" class="gl"/><text x="${L - 8}" y="${yy + 4}" text-anchor="end" class="ax">${l} · ${LVNAME[l]}</text>`; });
    pts.forEach((p, i) => { g += `<text x="${x(i)}" y="${H - 8}" text-anchor="middle" class="ax">SdA ${p.sda}</text>`; });
    const line = (vals, cls) => { const P = vals.map((v, i) => v == null ? null : `${x(i).toFixed(1)},${y(v).toFixed(1)}`).filter(Boolean); return P.length > 1 ? `<polyline points="${P.join(" ")}" class="${cls}"/>` : ""; };
    g += line(pts.map((p) => groupMean[p.sda] ?? null), "pl grp");
    g += line(pts.map((p) => p.mitjana), "pl stu");
    pts.forEach((p, i) => { if (groupMean[p.sda] != null) g += `<circle cx="${x(i)}" cy="${y(groupMean[p.sda])}" r="3.5" class="pt grp"/>`; if (p.mitjana != null) g += `<circle cx="${x(i)}" cy="${y(p.mitjana)}" r="5.5" class="pt stu"><title>SdA ${p.sda}: ${p.mitjana.toFixed(2)}</title></circle>`; });
    return `<svg class="segchart" viewBox="0 0 ${W} ${H}" role="img" aria-label="Evolució del nivell mitjà per SdA">${g}</svg>
      <p class="legend"><span class="k stu"></span>Alumne/a <span class="k grp"></span>Mitjana del grup</p>`;
  }

  function segView() {
    if (!students.length) { $("#main").innerHTML = '<section class="card"><p class="note">Encara no hi ha alumnat. Crea els comptes a «Alumnat i codis».</p></section>'; return; }
    if (!segStu || !students.some((s) => s.id === segStu)) segStu = students[0].id;
    const sdas = [...new Set(Object.keys(F).map(sdaOf))].filter((n) => n > 0).sort((a, b) => a - b);
    const sums = Object.fromEntries(students.map((s) => [s.id, stuSummary(s.id)]));
    const groupMean = Object.fromEntries(sdas.map((n) => [n, avg(students.map((s) => (sums[s.id].find((p) => p.sda === n) || {}).mitjana).filter((v) => v != null))]));
    const glob = (sid) => avg(sums[sid].map((p) => p.mitjana).filter((v) => v != null));
    const stu = students.find((s) => s.id === segStu); const sm = sums[segStu];
    const errTot = {}; sm.forEach((p) => Object.entries(p.errors).forEach(([e, c]) => (errTot[e] = (errTot[e] || 0) + c)));
    const errKeys = Object.keys(ERRN).filter((e) => errTot[e]);
    const maxE = Math.max(1, ...sm.flatMap((p) => Object.values(p.errors)));
    const errTable = errKeys.length ? `<div class="tscroll"><table class="t errt"><thead><tr><th>Tipus d'error</th>${sdas.map((n) => `<th>SdA ${n}</th>`).join("")}<th>Total</th></tr></thead><tbody>
      ${errKeys.sort((a, b) => errTot[b] - errTot[a]).map((e) => `<tr><td>${esc(ERRN[e])}</td>${sdas.map((n) => { const c = ((sm.find((p) => p.sda === n) || {}).errors || {})[e] || 0; return `<td style="--h:${(c / maxE).toFixed(2)}">${c || ""}</td>`; }).join("")}<td><b>${errTot[e]}</b></td></tr>`).join("")}</tbody></table></div>`
      : `<p class="note">Encara no hi ha errors classificats. Es classifiquen automàticament quan l'alumne lliura una fitxa digital.</p>`;
    const wsList = sm.filter((p) => p.sda > 0 || p.lliurades).map((p) => `<details class="segsda"${p.lliurades ? " open" : ""}><summary><b>SdA ${p.sda}</b> <span class="note">${esc(sdaTitle(p.sda))}</span><span class="sp"></span>${p.lliurades}/${p.total} lliurades ${chip(lvFrom(p.mitjana))}</summary>
      <table class="t"><tbody>${p.ws.filter((w) => w.status).map((w) => { const st = w.status ? STATUS[w.status] : null; return `<tr${w.status ? ` class="click" data-open="${w.ws}"` : ""}><td>${esc(titleOf(w.ws))}</td><td>${st ? `<span class="pill ${st[1]}">${st[0]}</span>` : '<span class="note">Sense començar</span>'}</td><td>${w.L ? levelHtml(segStu, w.ws, true) : ""}</td><td>${w.status ? '<span class="lnk">Respostes →</span>' : ""}</td></tr>`; }).join("")}</tbody></table>${(() => { const ns = p.ws.filter((w) => !w.status); return ns.length ? `<p class="note">Sense començar (${ns.length}): ${ns.map((w) => esc(titleOf(w.ws))).join(" · ")}</p>` : ""; })()}</details>`).join("");
    const lliurades = sm.reduce((a, p) => a + p.lliurades, 0);
    $("#main").innerHTML = `<div class="seggrid"><section class="card"><h2>Grup</h2><div class="tscroll"><table class="t segtab"><thead><tr><th>Alumne/a</th>${sdas.map((n) => `<th title="${esc(sdaTitle(n))}">${n}</th>`).join("")}<th>Mitjana</th></tr></thead><tbody>
        ${students.map((s) => `<tr class="click${s.id === segStu ? " on" : ""}" data-seg="${s.id}"><td>${esc(s.display_name)}</td>${sdas.map((n) => `<td>${chip(lvFrom((sums[s.id].find((p) => p.sda === n) || {}).mitjana))}</td>`).join("")}<td>${chip(lvFrom(glob(s.id)))}</td></tr>`).join("")}
        </tbody></table></div><p class="note">Nivell mitjà de les fitxes digitals de cada SdA. Si has retornat la fitxa, compta la teva valoració; si no, la correcció automàtica.</p></section>
      <section class="card segmain"><div class="row" style="justify-content:space-between"><h2>${esc(stu.display_name)}</h2><span class="note">${esc(stu.grup || "")} · ${lliurades} fitxes lliurades</span></div>
        <h3>Progrés d'una SdA a la següent</h3>${progressSvg(sm, groupMean) || '<p class="note">Sense dades.</p>'}
        <h3>Tipus d'error detectats</h3>${errTable}
        <h3>Informe de la IA</h3><div id="inf"><p class="note">Carregant…</p></div>
        <h3>Fitxes</h3>${wsList}</section></div>`;
    $("#main").querySelectorAll("[data-seg]").forEach((r) => (r.onclick = () => { segStu = r.dataset.seg; segView(); }));
    $("#main").querySelectorAll("[data-open]").forEach((r) => (r.onclick = () => { curWs = r.dataset.open; curSda = sdaOf(curWs); curStu = segStu; tab = "fitxes"; shell(); window.scrollTo(0, 0); }));
    renderInforme(stu, sm, errTot, lliurades);
  }

  async function renderInforme(stu, sm, errTot, lliurades) {
    const box = $("#inf"); if (!box) return;
    let rec = null; try { rec = await S.getInforme(stu.id); } catch {}
    if (segStu !== stu.id) return;
    const li = (a) => (a || []).length ? `<ul>${a.map((x) => `<li>${esc(x)}</li>`).join("")}</ul>` : "";
    box.innerHTML = (rec ? `<div class="inf"><p>${esc(rec.resum || "")}</p>${rec.fortaleses && rec.fortaleses.length ? `<b>Fortaleses</b>${li(rec.fortaleses)}` : ""}${rec.errors && rec.errors.length ? `<b>Errors recurrents</b>${li(rec.errors)}` : ""}${rec.progres ? `<b>Progrés</b><p>${esc(rec.progres)}</p>` : ""}${rec.propostes && rec.propostes.length ? `<b>Propostes</b>${li(rec.propostes)}` : ""}<p class="note">Generat el ${new Date(rec.at).toLocaleString("ca-ES", { day: "numeric", month: "long", hour: "2-digit", minute: "2-digit" })}. Només el veu el professorat.</p></div>`
      : `<p class="note">La IA analitza les fitxes lliurades, els tipus d'error i l'evolució entre SdA, i proposa com ajudar l'alumne. L'informe només el veus tu.</p>`)
      + `<button class="btn ghost" id="mkinf"${lliurades ? "" : " disabled"}>${rec ? "Actualitza l'informe" : "Genera l'informe"}</button>`;
    const b = $("#mkinf"); if (!b) return;
    b.onclick = async () => {
      b.disabled = true; b.textContent = "Analitzant…";
      // no s'envia el nom de l'alumne: només les dades acadèmiques
      const data = { lliurades, errors: errTot, sdas: sm.filter((p) => p.lliurades).map((p) => ({ sda: p.sda, titol: sdaTitle(p.sda), lliurades: p.lliurades, total: p.total, mitjana: p.mitjana == null ? null : +p.mitjana.toFixed(2), nivell: lvFrom(p.mitjana), errors: p.errors,
        fitxes: p.ws.filter((w) => w.L).map((w) => ({ fitxa: titleOf(w.ws), nivell: w.L.lv, origen: w.L.src, comentari: ((errAll.find((e) => e.student_id === stu.id && e.worksheet_id === w.ws) || {}).global || "").slice(0, 300) })) })) };
      try { await S.makeInforme(stu.id, data); renderInforme(stu, sm, errTot, lliurades); }
      catch (e) { toast("No s'ha pogut fer l'informe: " + e.message); b.disabled = false; b.textContent = "Genera l'informe"; }
    };
  }

  /* dades per al registre d'avaluació de cada SdA (profe.html) */
  window.FQDigitalData = {
    async load() { if (!courses.length) await loadCourses(); if (!students.length && S.curCourse()) await loadData(); return students; },
    sda(sid, n) { const p = stuSummary(sid).find((x) => x.sda === n); return p ? { lv: lvFrom(p.mitjana), mitjana: p.mitjana, lliurades: p.lliurades, total: p.total, ws: p.ws.map((w) => ({ ...w, title: titleOf(w.ws) })) } : null; },
    open(sid, ws) { curWs = ws; curSda = sdaOf(ws); curStu = sid; tab = "fitxes"; const mounted = !!$("#main"); location.hash = "#digital"; if (mounted) setTimeout(() => { shell(); window.scrollTo(0, 0); }, 50); },
  };

  window.FQDigital = { mount(el) { app = el; boot(); } };
  // si la portada del professorat ja ha arrencat abans que es carregués aquest fitxer, munta ara el llibre digital
  if (EMBED && window.FQ_READY && location.hash === "#digital" && typeof window.route === "function") window.route();
  if (!EMBED) (async () => { let me = null; try { me = await S.init(); } catch {} if (S.isStaff(me)) await boot(); else loginView(); })();
})();
