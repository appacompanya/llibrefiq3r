// Converteix pàgines HTML en PDF amb Chromium (com els generadors del llibre de 3r).
// Ús: node render.js feines.json   ·  feines.json = [{"html": "...", "pdf": "...", "footer": "<div>…</div>"}]
const fs = require("fs");
const path = require("path");
function playwright() {
  for (const p of ["playwright", "/opt/node22/lib/node_modules/playwright"]) {
    try { return require(p); } catch (e) { /* següent */ }
  }
  throw new Error("Cal Playwright (npm i playwright)");
}
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
  const { chromium } = playwright();
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const j of jobs) {
    await page.goto("file://" + path.resolve(j.html));
    await page.waitForFunction('document.body.dataset.math === "ok"', null, { timeout: 15000 });
    await page.evaluate("document.fonts.ready");
    await page.waitForTimeout(150);
    await page.pdf({ path: j.pdf, format: "A4", printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: true, headerTemplate: "<div></div>", footerTemplate: j.footer });
  }
  await browser.close();
})();
