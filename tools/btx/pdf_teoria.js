// Genera btx/fisica-II-teoria.pdf a partir de btx/teoria.html (Chromium de Playwright).
// Abans d'imprimir marca com a «keep» (no es parteixen) els requadres, taules i figures prou curts;
// els més llargs es poden partir, però el títol queda sempre enganxat al contingut que el segueix.
// La portada (pàgina 1) es copia del PDF anterior amb tools/btx/pdf_portada.py.
// Ús: node tools/btx/pdf_teoria.js [sortida.pdf]
const path = require("path");
const { chromium } = require("playwright");
const ROOT = path.resolve(__dirname, "..", "..");
const OUT = process.argv[2] || path.join(ROOT, "btx", "_teoria_sense_portada.pdf");
(async () => {
  const b = await chromium.launch();
  // amplada de la pàgina útil: A4 (210 mm) menys 2 × 15 mm de marge = 180 mm ≈ 680 px
  const p = await b.newPage({ viewport: { width: 680, height: 1000 } });
  await p.emulateMedia({ media: "print" });
  await p.goto("file://" + path.join(ROOT, "btx", "teoria.html"), { waitUntil: "load" });
  await p.evaluate(() => document.fonts.ready);
  const n = await p.evaluate(() => {
    const PAGE = 1000; // alçada útil aproximada d'una pàgina (267 mm) en px
    let k = 0;
    document.querySelectorAll(".box, table, figure").forEach((el) => {
      if (el.getBoundingClientRect().height < PAGE * 0.33) { el.classList.add("keep"); k++; }
    });
    // als requadres que es poden partir, el títol (.lead) i el primer paràgraf van junts
    document.querySelectorAll(".box:not(.keep) > .lead").forEach((lead) => {
      const nx = lead.nextElementSibling; if (!nx || nx.getBoundingClientRect().height > 220) return;
      const w = document.createElement("div"); w.style.breakInside = "avoid";
      lead.parentNode.insertBefore(w, lead); w.appendChild(lead); w.appendChild(nx);
    });
    return k;
  });
  await p.pdf({
    path: OUT, format: "A4", printBackground: true, displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate: '<div style="width:100%;font-size:7px;color:#666;padding:0 15mm;display:flex;justify-content:space-between;font-family:sans-serif"><span>Física II · Llibre de teoria</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: "14mm", bottom: "16mm", left: "15mm", right: "15mm" },
  });
  console.log(`PDF: ${OUT} (${n} blocs sense partir)`);
  await b.close();
})();
