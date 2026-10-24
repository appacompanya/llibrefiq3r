/* ===== Avaluació (només zona del professorat) ===== */
const LV = ["NA","AS","AN","AE"];
const LVN = {NA:1, AS:2, AN:3, AE:4};
const NOTA = {NA:3, AS:5.5, AN:7.5, AE:9.5};
const LVNAME = {NA:"No assolit", AS:"Satisfactori", AN:"Notable", AE:"Excel·lent"};
const EVAL = {
 1: [
  {id:"prova", l:"Prova escrita (sessions 9 i 10)", w:35, items:[
    {id:"p1", l:"Ex. 1 · La xeringa tapada", c:["1.1","1.2"]},
    {id:"p2", l:"Ex. 2 · La bomba de la bicicleta", c:["3.2"]},
    {id:"p3", l:"Ex. 3 · El globus del congelador", c:["3.2"]},
    {id:"p4", l:"Ex. 4 · La laca al costat de l'estufa", c:["1.2","3.2","5.3"]},
    {id:"p5", l:"Ex. 5 · La corba d'escalfament", c:["1.1","2.5","3.2"]},
    {id:"p6", l:"Ex. 6 · L'Everest", c:["1.3"]}]},
  {id:"inf", l:"Informe de pràctica", w:20, items:[
    {id:"i1", l:"Hipòtesi", c:["2.1"], d:{AE:"Clara, comprovable i justificada amb el model", AN:"Clara i comprovable", AS:"Poc concreta", NA:"Sense hipòtesi"}},
    {id:"i2", l:"Dades i unitats", c:["3.2"], d:{AE:"Taules completes, unitats correctes, mitjanes i kelvin quan cal", AN:"Taules completes amb algun error menor d'unitats", AS:"Taules incompletes o errors d'unitats", NA:"Dades absents o sense unitats"}},
    {id:"i3", l:"Gràfica", c:["2.5"], d:{AE:"Eixos amb magnitud i unitats, escala adequada, títol i tram d'ebullició identificat", AN:"Correcta amb algun element que falta", AS:"Errors d'escala o d'eixos", NA:"Sense gràfica o il·legible"}},
    {id:"i4", l:"Interpretació", c:["2.3"], d:{AE:"Interpreta amb el model, compara amb la predicció i comenta les fonts d'error", AN:"Interpreta els resultats amb el model", AS:"Descriu els resultats sense interpretar-los", NA:"No interpreta els resultats"}},
    {id:"i5", l:"Seguretat", c:["3.3"], d:{AE:"Identifica els riscos de la pràctica i les normes aplicades", AN:"Esmenta les normes aplicades", AS:"Esmenta alguna norma de manera genèrica", NA:"No esmenta la seguretat"}}]},
  {id:"video", l:"Vídeo per a 1r d'ESO", w:20, items:[
    {id:"v1", l:"Explicació científica", c:["1.3"], d:{AE:"Explica el fenomen amb el model i relaciona bé pressió, volum i temperatura", AN:"Explica el fenomen amb el model, amb alguna imprecisió menor", AS:"Fa servir el model de manera parcial", NA:"No fa servir el model o és incorrecta"}},
    {id:"v2", l:"Adaptació al públic", c:["4.1"], d:{AE:"Llenguatge clar, exemples propers i suport visual", AN:"Llenguatge clar i algun suport visual", AS:"Massa tècnic o poc suport visual", NA:"No s'entén per a un alumne de 1r"}},
    {id:"v3", l:"Vida quotidiana i salut", c:["5.3"], d:{AE:"Relaciona el fenomen amb situacions quotidianes i en dedueix consells de seguretat", AN:"Relaciona el fenomen amb situacions quotidianes", AS:"Esmenta la situació sense desenvolupar-la", NA:"No hi ha relació amb la vida quotidiana"}},
    {id:"v4", l:"Treball en equip", c:["2.4"], d:{AE:"Tots participen i compleixen el seu rol", AN:"Participen tots, amb alguna desigualtat", AS:"La càrrega recau en una part del grup", NA:"Un sol membre fa la feina"}},
    {id:"v5", l:"Qualitat tècnica", c:[], d:{AE:"Imatge i so clars, 2–3 min, muntatge cuidat", AN:"Imatge i so correctes, durada adequada", AS:"Problemes de so o d'imatge, o durada inadequada", NA:"No es pot seguir el vídeo"}}]},
  {id:"expl", l:"Explicació final del repte", w:15, items:[
    {id:"e1", l:"Ús del model", c:["1.2"], d:{AE:"Explica l'augment de pressió amb el moviment i els xocs de les partícules; el dibuix ho representa bé", AN:"Explicació correcta, dibuix amb alguna imprecisió", AS:"Explicació parcial o dibuix que no la representa", NA:"Sense model o incorrecta"}},
    {id:"e2", l:"Detecció dels propis errors", c:[], d:{AE:"Identifica tots els errors del dibuix inicial i explica per què ho eren", AN:"Identifica la majoria d'errors", AS:"Identifica algun error sense explicar-lo", NA:"No identifica els errors"}},
    {id:"e3", l:"Salut i seguretat", c:["5.3"], d:{AE:"Justifica l'avís de l'etiqueta i proposa consells concrets", AN:"Justifica l'avís de l'etiqueta", AS:"Esmenta el perill sense justificar-lo", NA:"No ho relaciona amb la seguretat"}}]},
  {id:"fit", l:"Fitxes i observació a l'aula", w:10, items:[
    {id:"f1", l:"Fitxa 1 · Model cineticomolecular", c:["1.1"]},
    {id:"f2", l:"Fitxa 2 · Lleis dels gasos", c:["3.2"]},
    {id:"f3", l:"Línia del temps de la teoria cinètica (sessió 4)", c:["6.1"]},
    {id:"f4", l:"Normes de seguretat al laboratori (observació)", c:["3.3"]}]}
 ]
};
const CRIT_NAMES = {"1.1":"Analitzar conceptes i processos","1.2":"Explicar fenòmens amb teories","1.3":"Aplicar-ho a problemes reals","2.1":"Formular hipòtesis","2.3":"Experimentar i interpretar","2.4":"Col·laborar","2.5":"Comunicar resultats","3.2":"Unitats i eines matemàtiques","3.3":"Seguretat al laboratori","4.1":"Comunicar amb entorns digitals","5.3":"Ciència, salut i sostenibilitat","6.1":"Perspectiva històrica"};
const EXAMPLE_NAMES = ["Alumne/a 01 (exemple)","Alumne/a 02 (exemple)","Alumne/a 03 (exemple)","Alumne/a 04 (exemple)","Alumne/a 05 (exemple)","Alumne/a 06 (exemple)"];

const AV = {ready:false, persistent:false, students:[], marks:{}, sel:null, sda:1};
let ST = null; // {db, uid}
const saveTimers = {};

function critList(n){ const s = new Set(); EVAL[n].forEach(i => i.items.forEach(it => it.c.forEach(c => s.add(c)))); return [...s].sort((a,b)=>parseFloat(a)-parseFloat(b) || a.localeCompare(b,undefined,{numeric:true})); }
function lvFromAvg(v){ if (v==null) return null; return LV[Math.min(3, Math.max(0, Math.round(v)-1))]; }
function summary(n, sid){
  const m = (AV.marks[sid]||{});
  const crit = {}, inst = {};
  let wsum = 0, nsum = 0;
  EVAL[n].forEach(ins => {
    const vals = [];
    ins.items.forEach(it => { const l = m[it.id]; if (!l) return; vals.push(LVN[l]); it.c.forEach(c => (crit[c] = crit[c] || []).push(LVN[l])); });
    if (vals.length){ const avg = vals.reduce((a,b)=>a+b,0)/vals.length; inst[ins.id] = {lv:lvFromAvg(avg), done:vals.length, total:ins.items.length}; wsum += ins.w; nsum += ins.w * NOTA[lvFromAvg(avg)]; }
  });
  const critLv = {}; Object.entries(crit).forEach(([c,v]) => critLv[c] = lvFromAvg(v.reduce((a,b)=>a+b,0)/v.length));
  const complete = EVAL[n].every(ins => ins.items.every(it => m[it.id]));
  return {crit:critLv, inst, nota: wsum ? nsum/wsum : null, complete};
}
const chip = l => l ? `<span class="lv lv-${l}" title="${LVNAME[l]}">${l}</span>` : `<span class="lv lv-none">–</span>`;

async function initStore(){
  try {
    if (!(window.claude && window.claude.use)) throw 0;
    const [db, user] = await Promise.all([window.claude.use("db"), window.claude.use("user")]);
    const uid = user ? await user.id() : null;
    if (!db || !uid) throw 0;
    ST = {db, uid};
    const cls = await db.doc(`data/users/${uid}/fq3-classe`).get();
    AV.students = (cls.exists && Array.isArray(cls.data().students)) ? cls.data().students.map(s => ({id:String(s.id), name:String(s.name)})) : [];
    const ev = await db.doc(`data/users/${uid}/fq3-classe`).collection("aval").get();
    ev.docs.forEach(d => { const b = d.data(); if (b && b.sid && b.marks) AV.marks[b.sid] = Object.assign({}, b.marks); });
    AV.persistent = true;
  } catch(e) { ST = null; AV.persistent = false; }
  AV.ready = true;
  if (AV.students.length && !AV.sel) AV.sel = AV.students[0].id;
  renderAval();
}
async function saveStudents(){
  if (!ST) return;
  try { await ST.db.doc(`data/users/${ST.uid}/fq3-classe`).set({students: AV.students}); }
  catch(e) { toast("No s'ha pogut desar la llista d'alumnes."); }
}
function saveMarks(sid){
  if (!ST) return;
  clearTimeout(saveTimers[sid]);
  saveTimers[sid] = setTimeout(async () => {
    try { await ST.db.doc(`data/users/${ST.uid}/fq3-classe`).collection("aval").doc(`sda${AV.sda}-${sid}`).set({sda:AV.sda, sid, marks: AV.marks[sid] || {}}); }
    catch(e) { toast("No s'ha pogut desar l'avaluació. Torna-ho a provar."); }
  }, 700);
}

function renderAval(){
  const host = document.getElementById("aval"); if (!host) return;
  const n = AV.sda;
  if (!AV.ready){ host.innerHTML = `<p class="note">Carregant l'avaluació…</p>`; return; }
  const crits = critList(n);
  const note = AV.persistent ? "Les dades es desen al teu compte i només les veus tu." : "No es poden desar dades en aquesta vista: el que marquis es perdrà en tancar la pàgina.";
  const list = AV.students.map(s => `<button type="button" class="stu${s.id===AV.sel?' on':''}" data-stu="${s.id}"><span>${esc(s.name)}</span>${(() => { const r = summary(n, s.id); return r.nota!=null ? `<b>${r.nota.toFixed(1)}</b>` : ""; })()}</button>`).join("");
  const empty = !AV.students.length ? `<p class="note">Encara no hi ha alumnat. Afegeix la llista del grup o prova l'eina amb alumnat d'exemple.</p><button type="button" class="btn ghost" id="avexample">Carrega alumnat d'exemple</button>` : "";
  let main = "";
  const st = AV.students.find(s => s.id === AV.sel);
  if (st){
    const m = AV.marks[st.id] || {};
    const r = summary(n, st.id);
    const insHtml = EVAL[n].map(ins => {
      const rows = ins.items.map(it => `<tr><th scope="row"><span class="asp">${esc(it.l)}</span>${it.c.length?`<span class="cr">${it.c.join(" · ")}</span>`:`<span class="cr">competència transversal</span>`}</th>${LV.slice().reverse().map(l => `<td><button type="button" class="cell-lv${m[it.id]===l?' on lv-'+l:''}" data-item="${it.id}" data-lv="${l}" aria-pressed="${m[it.id]===l}"><b>${l}</b>${it.d?`<span>${esc(it.d[l])}</span>`:`<span>${LVNAME[l]}</span>`}</button></td>`).join("")}</tr>`).join("");
      const ir = r.inst[ins.id];
      return `<details class="ins" open><summary><span>${esc(ins.l)}</span><span class="w">pes ${ins.w} %</span>${ir?chip(ir.lv)+`<span class="w">${ir.done}/${ir.total}</span>`:chip(null)}</summary>
        <div class="tscroll"><table class="rub"><thead><tr><th>Aspecte</th><th>AE</th><th>AN</th><th>AS</th><th>NA</th></tr></thead><tbody>${rows}</tbody></table></div></details>`;
    }).join("");
    const critHtml = crits.map(c => `<div class="crit"><span class="cc">${c}</span><span class="cn">${esc(CRIT_NAMES[c]||"")}</span>${chip(r.crit[c])}</div>`).join("");
    main = `<div class="avhead"><h4>${esc(st.name)}</h4><div class="nota">${r.nota!=null?`<b>${r.nota.toFixed(1)}</b><span>nota orientativa${r.complete?"":" · avaluació en curs"}</span>`:`<span>Sense avaluar</span>`}</div>
      <div class="acts"><button type="button" class="btn ghost" id="avclear">Esborra les marques</button><button type="button" class="btn ghost" id="avremove">Treu de la llista</button></div></div>
      <p class="note">Clica el nivell assolit a cada aspecte. Torna-hi a clicar per desmarcar-lo.</p>
      ${insHtml}
      <h4 class="sub">Criteris d'avaluació de ${esc(st.name)}</h4><div class="crits">${critHtml}</div>`;
  } else if (AV.students.length) {
    main = `<p class="note">Tria un alumne de la llista.</p>`;
  }
  const grid = AV.students.length ? `<div class="tscroll"><table class="grp"><thead><tr><th>Alumne/a</th>${crits.map(c=>`<th title="${esc(CRIT_NAMES[c]||"")}">${c}</th>`).join("")}<th>Nota</th></tr></thead><tbody>${AV.students.map(s => { const r = summary(n, s.id); return `<tr><th scope="row">${esc(s.name)}</th>${crits.map(c=>`<td>${chip(r.crit[c])}</td>`).join("")}<td class="nt">${r.nota!=null?r.nota.toFixed(1):"–"}</td></tr>`; }).join("")}</tbody></table></div>
    <div class="acts"><button type="button" class="btn" id="avcsv">${ICON_DL}Descarrega el resum (CSV)</button></div>` : "";
  host.innerHTML = `<h3 class="sec">Avaluació de la SdA ${n}</h3>
    <p class="note">${note} Els nivells de cada criteri són la mitjana dels aspectes on apareix. La nota orientativa pondera els instruments (prova 35 %, informe 20 %, vídeo 20 %, explicació 15 %, fitxes 10 %) amb NA = 3, AS = 5,5, AN = 7,5 i AE = 9,5.</p>
    <div class="avgrid"><aside class="stulist"><div class="stus">${list}</div>${empty}
      <label for="avnames" class="lbl">Afegeix alumnat (un nom per línia)</label><textarea id="avnames" rows="4" placeholder="Nom Cognom"></textarea><button type="button" class="btn ghost" id="avadd">Afegeix</button></aside>
      <div class="avmain">${main}</div></div>
    ${AV.students.length?`<h4 class="sub">Resum del grup</h4>`:""}${grid}`;
}
function addStudents(names){
  const fresh = names.map(s => s.trim()).filter(Boolean).filter(nm => !AV.students.some(s => s.name === nm)).map(nm => ({id: Date.now().toString(36) + Math.random().toString(36).slice(2,6), name: nm.slice(0,80)}));
  if (!fresh.length) return;
  AV.students = AV.students.concat(fresh);
  if (!AV.sel) AV.sel = fresh[0].id;
  saveStudents(); renderAval();
}
async function exportCsv(){
  const n = AV.sda, crits = critList(n);
  const head = ["Alumne/a", ...crits.map(c => "Criteri " + c), ...EVAL[n].map(i => i.l), "Nota orientativa"];
  const rows = AV.students.map(s => { const r = summary(n, s.id); return [s.name, ...crits.map(c => r.crit[c]||""), ...EVAL[n].map(i => (r.inst[i.id]||{}).lv||""), r.nota!=null ? r.nota.toFixed(1).replace(".",",") : ""]; });
  const csv = "﻿" + [head, ...rows].map(r => r.map(v => `"${String(v).replace(/"/g,'""')}"`).join(";")).join("\r\n");
  const dl = await getDownloads();
  if (!dl) { toast("Per descarregar, obre aquesta pàgina des de claude.ai."); return; }
  try { await dl.save({filename:`avaluacio-sda${n}.csv`, data:csv}); toast("Resum descarregat."); }
  catch(e){ toast(e && e.code==="declined" ? "Descàrrega cancel·lada." : "No s'ha pogut descarregar."); }
}
document.addEventListener("click", e => {
  const host = document.getElementById("aval"); if (!host || !host.contains(e.target)) return;
  const stu = e.target.closest("[data-stu]"); if (stu){ AV.sel = stu.dataset.stu; renderAval(); return; }
  const cell = e.target.closest(".cell-lv");
  if (cell && AV.sel){
    const m = AV.marks[AV.sel] = Object.assign({}, AV.marks[AV.sel]);
    const {item, lv} = cell.dataset;
    if (m[item] === lv) delete m[item]; else m[item] = lv;
    const y = window.scrollY; renderAval(); window.scrollTo(0, y); saveMarks(AV.sel); return;
  }
  if (e.target.id === "avadd"){ const t = document.getElementById("avnames"); addStudents(t.value.split("\n")); return; }
  if (e.target.id === "avexample"){ addStudents(EXAMPLE_NAMES); return; }
  if (e.target.id === "avcsv"){ exportCsv(); return; }
  if (e.target.id === "avclear" && AV.sel){ AV.marks[AV.sel] = {}; saveMarks(AV.sel); renderAval(); return; }
  if (e.target.id === "avremove" && AV.sel){
    const b = e.target; if (b.dataset.confirm !== "1"){ b.dataset.confirm = "1"; b.textContent = "Clica de nou per confirmar"; return; }
    const sid = AV.sel; AV.students = AV.students.filter(s => s.id !== sid); delete AV.marks[sid];
    if (ST) ST.db.doc(`data/users/${ST.uid}/fq3-classe`).collection("aval").doc(`sda${AV.sda}-${sid}`).delete().catch(()=>{});
    AV.sel = AV.students.length ? AV.students[0].id : null; saveStudents(); renderAval();
  }
});
