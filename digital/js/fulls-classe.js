/* Fulls d'una sessió per a tota la classe (zona del professorat, profe.html).
   Genera un sol document per imprimir o desar en PDF amb, per a cada full de la sessió:
   - tantes còpies del full original com alumnes no tenen cap adaptació que afecti aquell full;
   - una còpia adaptada per a cada alumne amb adaptació (amb el seu nom imprès, sense el nom del perfil).
   L'alumnat i les adaptacions són els del curs actiu (FQDigitalData / FQStore).
   Per a impressió a doble cara: si una còpia acaba en pàgina senar, s'afegeix una pàgina en blanc
   perquè la següent comenci sempre per davant. */
(function (G) {
  "use strict";
  const esc = (s) => String(s ?? "").replace(/&/g, "&").replace(/</g, "<").replace(/>/g, ">").replace(/"/g, """);
  const NAMES = { dislexia: "dislèxia", nouvingut: "nouvingut", basics: "continguts bàsics", discalculia: "discalcúlia", tdah: "TDAH", tea: "TEA" };
  const AD = () => G.FQAdapt, F = () => G.FITXES || {};
  const imgCache = {};

  function css() {
    if (document.getElementById("fccss")) return;
    const st = document.createElement("style"); st.id = "fccss";
    st.textContent = `
#fcPrint{position:absolute;left:-10000px;top:0;width:210mm;background:#fff;color:#1f2328}
#fcPrint .fc-pg{width:210mm;break-after:page;page-break-after:always}
#fcPrint .fc-pg img{display:block;width:210mm;height:auto}
#fcPrint .fc-pg:last-child{break-after:auto;page-break-after:auto}
#fcPrint .ws-block,#fcPrint [data-qblock],#fcPrint .ad-card,#fcPrint tr{break-inside:avoid}
#fcPrint .fc-ad{padding:12mm 14mm 10mm;box-sizing:border-box}
#fcPrint .fc-hd{display:flex;justify-content:space-between;gap:12px;border-bottom:1.5px solid #1f2328;padding-bottom:4px;margin-bottom:8px;font-size:11pt}
#fcPrint .fc-hd b{font-size:13pt}
#fcPrint .ws-actions,#fcPrint .wsnote,#fcPrint button.ad-tts,#fcPrint .ad-nav,#fcPrint .ad-calc,#fcPrint .ad-noprint{display:none!important}
#fcDlg{border:1px solid var(--line);border-radius:16px;padding:20px 22px;width:min(560px,94vw);background:var(--surface);color:var(--fg)}
#fcDlg::backdrop{background:rgba(0,0,0,.35)}
#fcDlg h3{margin:0 0 6px;font-family:var(--font-display,inherit)}
#fcDlg ul{margin:6px 0 12px;padding-left:1.2em;display:grid;gap:4px}
#fcDlg .acts{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end}
@media print{@page{size:A4;margin:0}
 body.fc-printing>*:not(#fcPrint){display:none!important}
 body.fc-printing{background:#fff!important}
 body.fc-printing #fcPrint{position:static;left:auto;width:auto}}`;
    document.head.appendChild(st);
  }

  /* pàgines del PDF original com a imatges (es reutilitzen per a totes les còpies) */
  async function pdfImages(f) {
    if (imgCache[f]) return imgCache[f];
    const u = await G.fqDocUrl(f);
    const pdf = await G.pdfjsLib.getDocument({ url: u, isEvalSupported: false }).promise;
    const out = [];
    for (let i = 1; i <= pdf.numPages; i++) {
      const page = await pdf.getPage(i); const vp = page.getViewport({ scale: 2.2 });
      const c = document.createElement("canvas"); c.width = Math.round(vp.width); c.height = Math.round(vp.height);
      const ctx = c.getContext("2d"); ctx.fillStyle = "#fff"; ctx.fillRect(0, 0, c.width, c.height);
      await page.render({ canvasContext: ctx, viewport: vp }).promise;
      out.push(c.toDataURL("image/jpeg", 0.9));
    }
    return (imgCache[f] = out);
  }

  /* agrupa l'alumnat per a un full: original o adaptació efectiva (+ llengua si és nouvingut) */
  function groups(k, students) {
    const orig = [], ad = [];
    students.forEach((s) => {
      const P = F()[k] && AD() ? AD().effective(k, s.adaptacions || []) : [];
      if (!P.length) orig.push(s); else ad.push({ s, P });
    });
    return { orig, ad };
  }

  function adaptedCopy(k, st, P, meta) {
    const pg = document.createElement("div"); pg.className = "fc-pg fc-ad";
    pg.innerHTML = `<div class="fc-hd"><span><b>${esc(meta.title)}</b><br>${esc(meta.kick)}</span><span>Nom: <b>${esc(st.display_name || "")}</b><br>Data: ____________</span></div><div class="fc-host"></div>`;
    const host = pg.querySelector(".fc-host");
    G.FQFitxa.render(host, k, { answers: {}, readonly: true, autoCalc: false, photos: [], feedback: [], photoUrl: async () => "" });
    AD().apply(host, k, st.adaptacions || [], { mode: "paper", idioma: st.adapt_idioma || null, off: [] });
    return pg;
  }

  /* Afegeix una pàgina en blanc (per alinear a doble cara quan el nombre de pàgines és imparell) */
  function addBlank(pr) {
    const blank = document.createElement("div");
    blank.className = "fc-pg";
    pr.appendChild(blank);
  }

  async function open(o) {
    css();
    let dlg = document.getElementById("fcDlg");
    if (!dlg) { dlg = document.createElement("dialog"); dlg.id = "fcDlg"; document.body.appendChild(dlg); }
    dlg.innerHTML = `<h3>Fulls per a la classe</h3><p class="note">Preparant els fulls…</p>`;
    dlg.showModal();
    let students = [];
    try { if (G.FQDigitalData) await G.FQDigitalData.load(); students = G.FQStore && G.FQStore.curCourse() ? await G.FQStore.listStudents() : []; } catch (e) { students = []; } /* llista fresca: les adaptacions poden haver canviat */
    students = (students || []).filter((s) => !s.role || s.role === "student");
    if (!students.length) {
      dlg.innerHTML = `<h3>Fulls per a la classe</h3><p>No hi ha cap curs amb alumnat. Entra a la zona del professorat, tria el curs i torna-ho a provar.</p><div class="acts"><button class="btn" data-x>D'acord</button></div>`;
      dlg.querySelector("[data-x]").onclick = () => dlg.close(); return;
    }
    let pr = document.getElementById("fcPrint"); if (pr) pr.remove();
    pr = document.createElement("div"); pr.id = "fcPrint"; document.body.appendChild(pr);
    const lines = []; let pages = 0;
    try {
      for (const d of o.docs) {
        const { orig, ad } = groups(d.k, students);
        const meta = { title: (F()[d.k] && F()[d.k].title) || d.l, kick: `Física i química · 3r d'ESO · SdA ${o.sda.n} · ${o.sda.title}` };
        if (orig.length) {
          const imgs = await pdfImages(d.f);
          const n = imgs.length;
          for (let c = 0; c < orig.length; c++) {
            imgs.forEach((src) => {
              const pg = document.createElement("div");
              pg.className = "fc-pg";
              pg.innerHTML = `<img src="${src}" alt="">`;
              pr.appendChild(pg);
              pages++;
            });
            // Si el nombre de pàgines és imparell, afegeix una pàgina en blanc per a doble cara
            if (n % 2 === 1) {
              addBlank(pr);
              pages++;
            }
          }
        }
        const byProf = {};
        ad.forEach(({ s, P }) => {
          pr.appendChild(adaptedCopy(d.k, s, P, meta));
          pages++;
          // Les adaptades actualment ocupen 1 pàgina (imparell) → farciment
          // (si en el futur poden ocupar més, caldria comptar les pàgines reals generades)
          addBlank(pr);
          pages++;

          const lab = P.map((p) => (p === "nouvingut" && s.adapt_idioma ? `${NAMES[p]} (${(((G.FQ_ADAPT || {}).llengues || []).find((l) => l.codi === s.adapt_idioma) || {}).nom || s.adapt_idioma})` : NAMES[p] || p)).join(" + ");
          (byProf[lab] = byProf[lab] || []).push(s.display_name || "");
        });
        const noVar = !F()[d.k] && students.some((s) => (s.adaptacions || []).length);
        lines.push(`<li><b>${esc(d.l)}</b>: ${orig.length} còpi${orig.length === 1 ? "a" : "es"} del full original${Object.entries(byProf).map(([lab, ns]) => ` · ${ns.length} adaptad${ns.length === 1 ? "a" : "es"} (${esc(lab)}: ${esc(ns.join(", "))})`).join("")}${noVar ? ' <span class="note">(aquest full no té versió adaptada: tothom rep l\\'original)</span>' : ""}</li>`);
      }
    } catch (e) {
      console.error("fulls-classe", e);
      dlg.innerHTML = `<h3>Fulls per a la classe</h3><p>No s'han pogut preparar els fulls. Torna-ho a provar.</p><div class="acts"><button class="btn" data-x>D'acord</button></div>`;
      dlg.querySelector("[data-x]").onclick = () => dlg.close(); pr.remove(); return;
    }
    setTimeout(() => { try { if (G.MathLive && G.MathLive.renderMathInElement) G.MathLive.renderMathInElement(pr); } catch {} }, 300);
    dlg.innerHTML = `<h3>Fulls per a la classe · sessió ${o.ses + 1}</h3>
      <p class="note">${students.length} alumnes del curs. Cada alumne amb adaptació rep la seva còpia amb el nom imprès (el full no diu quina adaptació és).</p>
      <ul>${lines.join("")}</ul>
      <p class="note">Al diàleg d'impressió pots imprimir-ho directament o triar «Desa com a PDF». S'han afegit pàgines en blanc quan calia per a impressió a doble cara.</p>
      <div class="acts"><button class="btn ghost" data-x>Tanca</button><button class="btn" data-p>Imprimeix o desa en PDF</button></div>`;
    dlg.querySelector("[data-x]").onclick = () => { dlg.close(); pr.remove(); };
    dlg.querySelector("[data-p]").onclick = () => {
      dlg.close(); document.body.classList.add("fc-printing");
      const done = () => { document.body.classList.remove("fc-printing"); pr.remove(); G.removeEventListener("afterprint", done); };
      G.addEventListener("afterprint", done);
      setTimeout(() => G.print(), 400);
    };
  }

  G.FQFullsClasse = { open, groups };
})(window);
