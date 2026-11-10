// Genera biologia/biologia-teoria.pdf a partir de biologia/teoria.html (tot el llibre en una pàgina).
// Ús: node tools/biologia/pdf_teoria.js
const path = require("path");
const { chromium } = require("playwright");
const ROOT = path.resolve(__dirname, "..", "..");
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || undefined });
  const p = await b.newPage({ viewport: { width: 680, height: 1000 } });
  await p.emulateMedia({ media: "print" });
  await p.goto("file://" + path.join(ROOT, "biologia", "teoria.html"), { waitUntil: "load" });
  await p.evaluate(() => document.fonts.ready);
  await p.evaluate(() => {
    document.querySelectorAll("details").forEach((d) => (d.open = true));
    document.querySelectorAll(".box, table, figure, ol.aut > li").forEach((el) => {
      if (el.getBoundingClientRect().height < 330) el.style.breakInside = "avoid";
    });
  });
  await p.pdf({
    path: path.join(ROOT, "biologia", "biologia-teoria.pdf"), format: "A4", printBackground: true, displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate: '<div style="width:100%;font-size:7px;color:#666;padding:0 15mm;display:flex;justify-content:space-between;font-family:sans-serif"><span>Biologia · 2n de Batxillerat · llibrefiq3r.cat/biologia</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: "14mm", bottom: "16mm", left: "15mm", right: "15mm" },
  });
  await b.close();
})();
