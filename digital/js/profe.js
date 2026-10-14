/* Zona del professorat de la versió digital */
(function () {
  "use strict";
  const S = window.FQStore, F = window.FITXES || {}, DOCS = window.DOCS || {}, FX = window.FQFitxa;
  const app = document.getElementById("app");
  const $ = (s, r = document) => r.querySelector(s);
  const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  const LV = ["NA", "AS", "AN", "AE"];
  const STATUS = { draft: ["Esborrany", "draft"], submitted: ["Lliurada", "sub"], returned: ["Retornada", "ret"] };
  let tab = "fitxes", students = [], subs = [], respKeys = [], settings = {}, curWs = null, curStu = null;
  const toast = (t) => { const el = $("#toast"); el.textContent = t; el.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => (el.hidden = true), 3500); };
  const titleOf = (k) => (F[k] && F[k].title) || (DOCS[k] && `SdA ${DOCS[k].sda} · ${DOCS[k].l}`) || k;
  const sdaOf = (k) => (F[k] && F[k].sda) || (DOCS[k] && DOCS[k].sda) || 0;

  /* ---------- accés ---------- */
  function loginView(msg) {
    app.innerHTML = `<form class="card login" id="lf"><div class="eyebrow">Física i química · 3r d'ESO</div><h1>Zona del professorat</h1>
      ${S.mode === "demo" ? `<p class="note"><b>Mode demostració.</b> Les dades es guarden només en aquest navegador. Entra directament.</p>` :
      `<label class="f">Correu<input type="email" id="le" autocomplete="username" required></label><label class="f">Contrasenya<input type="password" id="lp" autocomplete="current-password" required></label>`}
      <p class="err" id="lerr">${esc(msg || "")}</p><button class="btn" type="submit">Entra</button></form>`;
    $("#lf").onsubmit = async (e) => {
      e.preventDefault();
      try { await S.signInTeacher(S.mode === "demo" ? "" : $("#le").value, S.mode === "demo" ? "" : $("#lp").value); await boot(); }
      catch (err) { $("#lerr").textContent = err.message === "not_teacher" ? "Aquest compte no és de professorat." : "Correu o contrasenya incorrectes."; }
    };
  }
  async function boot() {
    [students, subs, respKeys, settings] = await Promise.all([S.listStudents(), S.listSubmissions(), S.listResponseKeys(), S.getSettings()]);
    shell();
  }
  function shell() {
    app.innerHTML = `<header class="top"><div><div class="eyebrow">Física i química per entendre el món · ${S.mode === "demo" ? "demostració" : "llibre digital"}</div><h1>Zona del professorat</h1></div>
      <div class="row noprint"><a class="btn ghost" href="./" target="_blank" rel="noopener">Obre el llibre de l'alumnat</a><button class="btn ghost" id="out">Surt</button></div></header>
      <nav class="tabs noprint" role="tablist">${[["fitxes", "Fitxes i lliuraments"], ["alumnat", "Alumnat i codis"], ["ajustos", "Ajustos"]].map(([k, l]) => `<button role="tab" data-tab="${k}" aria-selected="${tab === k}">${l}</button>`).join("")}</nav>
      <main id="main"></main>`;
    $("#out").onclick = async () => { await S.signOut(); loginView(); };
    app.querySelectorAll("[data-tab]").forEach((b) => (b.onclick = () => { tab = b.dataset.tab; curWs = null; curStu = null; shell(); }));
    ({ fitxes: fitxesView, alumnat: alumnatView, ajustos: ajustosView })[tab]();
  }

  /* ---------- ajustos ---------- */
  function ajustosView() {
    $("#main").innerHTML = `<section class="card"><h2>Ajudes a l'alumnat</h2>
      <label class="switch"><input type="checkbox" id="ac"${settings.auto_calc !== false ? " checked" : ""}> Càlcul automàtic a les fitxes</label>
      <p class="note">Si està activat, quan l'alumne escriu números o factors de conversió, la fitxa li mostra el resultat del càlcul i si cada factor val 1. Desactiva-ho per a les activitats d'avaluació.</p></section>
      <section class="card"><h2>Correcció assistida</h2><p class="note">El botó «Proposta automàtica» de cada lliurament demana una proposta de nivell i comentari per a cada apartat. La proposta no la veu l'alumne: la revises, la modifiques si cal i decideixes quan retornar la fitxa.${S.mode === "demo" ? " En mode demostració, la proposta es basa només en la comprovació automàtica." : ""}</p></section>`;
    $("#ac").onchange = async (e) => { try { await S.setSetting("auto_calc", e.target.checked); settings.auto_calc = e.target.checked; toast(e.target.checked ? "Càlcul automàtic activat." : "Càlcul automàtic desactivat."); } catch { toast("No s'ha pogut desar."); } };
  }

  /* ---------- alumnat ---------- */
  function alumnatView(created) {
    const grups = [...new Set(students.map((s) => s.grup).filter(Boolean))];
    $("#main").innerHTML = `<div class="grid2"><section class="card noprint"><h2>Afegeix alumnat</h2>
        <label class="f">Noms (un per línia)<textarea id="names" rows="8" placeholder="Nom Cognom"></textarea></label>
        <label class="f">Grup<input id="grup" list="grups" placeholder="3r A"><datalist id="grups">${grups.map((g) => `<option value="${esc(g)}">`).join("")}</datalist></label>
        <div class="row"><button class="btn" id="add">Crea els comptes</button></div>
        <p class="note">Cada alumne rep un codi d'accés de 8 caràcters. Amb aquest codi entra al llibre digital des de qualsevol dispositiu.</p></section>
      <section class="card"><div class="row" style="justify-content:space-between"><h2>Alumnat (${students.length})</h2><div class="row noprint"><button class="btn ghost" id="csv">Descarrega els codis (CSV)</button><button class="btn ghost" id="prn">Imprimeix targetes</button></div></div>
        ${created && created.length ? `<p class="note" style="color:var(--ok)"><b>Comptes creats:</b> ${created.length}. Ja els tens a la llista.</p>` : ""}
        <div class="tscroll"><table class="t"><thead><tr><th>Nom</th><th>Grup</th><th>Codi</th><th class="noprint"></th></tr></thead><tbody>
        ${students.map((s) => `<tr data-id="${s.id}"><td>${esc(s.display_name)}</td><td>${esc(s.grup)}</td><td><code class="c">${esc(s.code || "—")}</code></td><td class="noprint"><div class="row"><button class="btn ghost" data-reset>Codi nou</button><button class="btn danger" data-del>Esborra</button></div></td></tr>`).join("") || `<tr><td colspan="4" class="note">Encara no hi ha alumnat. Afegeix-lo amb el formulari.</td></tr>`}
        </tbody></table></div></section></div>
      <section class="codes" id="cards" hidden>${students.map((s) => `<div class="codecard"><span>Física i química · 3r d'ESO · llibre digital</span><b>${esc(s.display_name)}</b><code>${esc(s.code || "")}</code><span>${esc(location.origin + location.pathname.replace(/profe\.html$/, ""))}</span></div>`).join("")}</section>`;
    $("#add").onclick = async () => {
      const names = $("#names").value.split("\n").map((x) => x.trim()).filter(Boolean); if (!names.length) return;
      const b = $("#add"); b.disabled = true; b.textContent = "Creant…";
      try { const out = await S.createStudents(names, $("#grup").value.trim()); students = await S.listStudents(); alumnatView(out); }
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
      const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv" })); a.download = "codis-alumnat-fq3.csv"; a.click();
    };
    $("#prn").onclick = () => { $("#cards").hidden = false; window.print(); setTimeout(() => ($("#cards").hidden = true), 500); };
  }

  /* ---------- fitxes i lliuraments ---------- */
  function fitxesView() {
    if (curWs && curStu) return reviewView();
    const keys = new Set([...Object.keys(F), ...subs.map((s) => s.worksheet_id), ...respKeys.map((r) => r.worksheet_id)]);
    const list = [...keys].sort((a, b) => sdaOf(a) - sdaOf(b) || a.localeCompare(b, undefined, { numeric: true }));
    if (!curWs) curWs = list[0] || null;
    const subOf = (sid) => subs.find((s) => s.student_id === sid && s.worksheet_id === curWs);
    const started = (sid) => respKeys.some((r) => r.student_id === sid && r.worksheet_id === curWs);
    const counts = (k) => { const ss = subs.filter((s) => s.worksheet_id === k); return { sub: ss.filter((s) => s.status === "submitted").length, ret: ss.filter((s) => s.status === "returned").length }; };
    $("#main").innerHTML = `<div class="grid2"><section class="card"><h2>Fitxes</h2><div class="tscroll"><table class="t"><thead><tr><th>Fitxa</th><th>Per corregir</th><th>Retornades</th></tr></thead><tbody>
        ${list.map((k) => { const c = counts(k); return `<tr class="click" data-ws="${k}"${k === curWs ? ' style="background:var(--chip)"' : ""}><td>${F[k] ? '<span class="pill">digital</span> ' : '<span class="pill">foto</span> '}${esc(titleOf(k))}</td><td>${c.sub ? `<span class="pill sub">${c.sub}</span>` : "—"}</td><td>${c.ret || "—"}</td></tr>`; }).join("") || '<tr><td colspan="3" class="note">Encara no hi ha cap fitxa.</td></tr>'}
        </tbody></table></div></section>
      <section class="card">${curWs ? `<h2>${esc(titleOf(curWs))}</h2><div class="tscroll"><table class="t"><thead><tr><th>Alumne/a</th><th>Grup</th><th>Estat</th><th>Lliurada</th></tr></thead><tbody>
        ${students.map((s) => { const sb = subOf(s.id); const st = sb ? STATUS[sb.status] : started(s.id) ? STATUS.draft : null;
          return `<tr class="click" data-stu="${s.id}"><td>${esc(s.display_name)}</td><td>${esc(s.grup)}</td><td>${st ? `<span class="pill ${st[1]}">${st[0]}</span>` : '<span class="note">Sense començar</span>'}</td><td>${sb && sb.submitted_at ? new Date(sb.submitted_at).toLocaleDateString("ca-ES") : ""}</td></tr>`; }).join("") || '<tr><td colspan="4" class="note">Encara no hi ha alumnat.</td></tr>'}
        </tbody></table></div>` : '<p class="note">Tria una fitxa.</p>'}</section></div>`;
    $("#main").querySelectorAll("[data-ws]").forEach((r) => (r.onclick = () => { curWs = r.dataset.ws; fitxesView(); }));
    $("#main").querySelectorAll("[data-stu]").forEach((r) => (r.onclick = () => { curStu = r.dataset.stu; reviewView(); window.scrollTo(0, 0); }));
  }

  function answerText(it, a) {
    if (!a) return "(sense resposta)";
    const U = window.FQUnits;
    switch (it.type) {
      case "text": case "number": return a.text || "";
      case "sci": return `${a.m || "?"}·10^${a.e || "?"}`;
      case "math": return `${a.latex || ""} → ${a.m || "?"}·10^${a.e || "?"}`;
      case "chain": return `${it.start.v} ${it.start.u} ${(a.factors || []).map((f) => `· (${f.nv} ${f.nu})/(${f.dv} ${f.du})`).join(" ")} = ${a.v || "?"} ${a.u || ""}`;
      case "tf": return it.statements.map((s, i) => `${i + 1}: ${(a.ans || {})[i] === true ? "T" : (a.ans || {})[i] === false ? "F" : "?"} ${(a.corr || {})[i] || ""}`).join(" | ");
      case "table": return it.rows.map((r, ri) => r.label + ": " + r.cells.map((c, ci) => (a.cells || {})[`r${ri}c${ci}`] || "—").join(" / ")).join(" | ");
      default: return JSON.stringify(a);
    }
  }

  async function reviewView() {
    const stu = students.find((s) => s.id === curStu); const k = curWs; const spec = F[k];
    $("#main").innerHTML = '<div class="spin"></div>';
    const [answers, sub, fbRows] = await Promise.all([S.loadResponses(k, curStu), S.getSubmission(k, curStu), S.feedbackFor(curStu, k)]);
    const fb = Object.fromEntries(fbRows.map((r) => [r.item_id, r]));
    const st = STATUS[sub.status] || STATUS.draft;
    $("#main").innerHTML = `<div class="revhead"><button class="btn ghost" id="back">← Llista</button><h2>${esc(stu ? stu.display_name : "")} · ${esc(titleOf(k))}</h2><span class="pill ${st[1]}">${st[0]}</span>
      <button class="btn ghost" id="ai">Proposta automàtica</button><button class="btn ghost" id="save">Desa</button><button class="btn" id="ret">Retorna a l'alumne</button>${sub.status !== "draft" ? '<button class="btn ghost" id="reopen">Deixa-la modificar</button>' : ""}</div>
      <div id="rev"></div>`;
    $("#back").onclick = () => { curStu = null; fitxesView(); };
    const host = $("#rev");
    if (spec) {
      FX.render(host, k, { answers, readonly: true, autoCalc: true, showCheck: true, photos: sub.photos || [], photoUrl: (p) => S.photoUrl(p) });
    } else {
      const imgs = await Promise.all((sub.photos || []).map(async (p) => `<a href="${esc(await S.photoUrl(p.path))}" target="_blank" rel="noopener"><img src="${esc(await S.photoUrl(p.path))}" alt="Foto lliurada" style="max-width:100%;border-radius:10px;border:1px solid var(--line)"></a>`));
      host.innerHTML = `<div class="ws"><section class="ws-block"><b>Fotos lliurades</b>${imgs.join("") || '<p class="note">Sense fotos.</p>'}</section></div>`;
    }
    // editors de retroacció
    const targets = spec ? [...FX.allItems(spec).filter((it) => !it.parent).map((it) => it.id), ...spec.blocks.filter((b) => b.type === "group").map((b) => b.id)] : [];
    const editor = (id, label) => { const f = fb[id] || {}; return `<div class="fbed" data-fb="${id}"><b>${esc(label)}</b><div class="lvs">${LV.map((l) => `<button type="button" data-lv="${l}" class="${f.level === l ? "on" : ""}">${l}</button>`).join("")}</div>
      <textarea rows="2" placeholder="Comentari per a l'alumne">${esc(f.comment || "")}</textarea>${f.proposal_level || f.proposal_note ? `<div class="prop">Proposta: <b>${esc(f.proposal_level || "")}</b> ${esc(f.proposal_note || "")}<button type="button" data-accept>Fes-la servir</button></div>` : ""}</div>`; };
    targets.forEach((id) => {
      const el = host.querySelector(`.ws-block[data-block="${id}"]`) || host.querySelector(`.ws-item[data-item="${id}"]`)?.closest(".ws-block");
      if (el) el.insertAdjacentHTML("beforeend", editor(id, "Valoració de l'apartat " + id));
    });
    host.insertAdjacentHTML("beforeend", `<div class="ws" style="margin-top:14px"><section class="ws-block">${editor("_global", "Valoració global de la fitxa")}</section></div>`);
    host.addEventListener("click", (e) => {
      const b = e.target.closest("[data-lv]"); if (b) { const box = b.closest(".fbed"); const was = b.classList.contains("on"); box.querySelectorAll("[data-lv]").forEach((x) => x.classList.remove("on")); if (!was) b.classList.add("on"); return; }
      const acc = e.target.closest("[data-accept]"); if (acc) { const box = acc.closest(".fbed"); const f = fb[box.dataset.fb] || {}; box.querySelectorAll("[data-lv]").forEach((x) => x.classList.toggle("on", x.dataset.lv === f.proposal_level)); box.querySelector("textarea").value = f.proposal_note || ""; }
    });
    const collect = () => [...host.querySelectorAll(".fbed")].map((box) => ({ item_id: box.dataset.fb, level: box.querySelector("[data-lv].on")?.dataset.lv || null, comment: box.querySelector("textarea").value.trim() }));
    $("#save").onclick = async () => { try { await S.saveFeedback(curStu, k, collect()); toast("Valoració desada (l'alumne encara no la veu)."); } catch (e) { toast("Error: " + e.message); } };
    $("#ret").onclick = async (e) => {
      const b = e.target; if (b.dataset.c !== "1") { b.dataset.c = "1"; b.textContent = "Segur? L'alumne veurà els comentaris"; return; }
      try { await S.saveFeedback(curStu, k, collect()); await S.release(curStu, k); subs = await S.listSubmissions(); toast("Fitxa retornada."); reviewView(); } catch (er) { toast("Error: " + er.message); }
    };
    const ro = $("#reopen"); if (ro) ro.onclick = async () => { await S.reopen(curStu, k); subs = await S.listSubmissions(); toast("L'alumne ja pot tornar a modificar la fitxa."); reviewView(); };
    $("#ai").onclick = async () => {
      if (!spec) { toast("Les fitxes en foto les has de valorar tu."); return; }
      const b = $("#ai"); b.disabled = true; b.textContent = "Preparant la proposta…";
      const strip = (h) => String(h || "").replace(/<[^>]+>/g, "");
      const expOf = (it) => typeof it.expected === "object" ? `${it.expected.v} ${it.expected.u}` : (it.expected || "");
      const items = spec.blocks.filter((b) => b.id).map((b) => {
        if (b.type !== "group") { const r = FX.checkItem(b, answers[b.id]); return { id: b.id, prompt: strip(b.prompt), expected: expOf(b) || (b.type === "table" ? "taula: valors de referència" : ""), criteria: b.criteria || "", answer: answerText(b, answers[b.id]), auto: r.ok === null ? null : (r.detail ? `${r.ok ? "correcte" : "incorrecte"} (${r.detail})` : r.ok), score: r.score ?? (r.ok === null ? null : r.ok ? 1 : 0) }; }
        const parts = b.items.map((it) => ({ it, r: FX.checkItem(it, answers[it.id]) }));
        const checked = parts.filter((x) => x.r.ok !== null); const good = checked.filter((x) => x.r.ok).length;
        return { id: b.id, prompt: strip(b.prompt) + " " + b.items.map((it) => it.label).join(" · "), expected: b.items.map((it) => `${it.label}: ${expOf(it)}`).join(" · "), criteria: b.items.map((it) => it.criteria).filter(Boolean).join(" "),
          answer: b.items.map((it) => `${it.label}: ${answerText(it, answers[it.id])}`).join(" | "), auto: checked.length ? `${good}/${checked.length} apartats correctes` : null, score: checked.length ? good / checked.length : null };
      });
      try {
        if (S.mode === "demo") {
          const lvOf = (sc) => sc == null ? null : sc >= 0.95 ? "AE" : sc >= 0.75 ? "AN" : sc >= 0.5 ? "AS" : "NA";
          const rows = items.map((x) => ({ item_id: x.id, proposal_level: lvOf(x.score), proposal_note: x.score == null ? "Cal revisar-ho manualment." : x.score >= 0.95 ? "Correcte." : `Comprovació automàtica: ${x.auto}. Revisa els apartats marcats.` }));
          await S.saveFeedback(curStu, k, rows.map((r) => ({ ...r })));
        } else { await S.proposeAI(curStu, k, items); }
        toast("Proposta preparada. Revisa-la abans de retornar."); reviewView();
      } catch (e) { toast(e.message === "missing_api_key" ? "Falta configurar la clau de correcció al servidor." : "No s'ha pogut fer la proposta: " + e.message); b.disabled = false; b.textContent = "Proposta automàtica"; }
    };
  }

  (async () => { let me = null; try { me = await S.init(); } catch {} if (me && me.role === "teacher") await boot(); else loginView(); })();
})();
