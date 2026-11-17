// Genera iniciaciofisica/iniciacio-fisica.pdf a partir de iniciaciofisica/llibre.html.
// Ús: node tools/iniciaciofisica/pdf.js
const { execFileSync } = require("child_process");
const path = require("path");
const root = path.resolve(__dirname, "..", "..");
const html = "file://" + path.join(root, "iniciaciofisica", "llibre.html");
const pdf = path.join(root, "iniciaciofisica", "iniciacio-fisica.pdf");
const chrome = process.env.CHROME || "google-chrome";
execFileSync(chrome, [
  "--headless", "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage",
  "--user-data-dir=/tmp/chrome-iniciacio-pdf",
  "--no-pdf-header-footer",
  "--virtual-time-budget=90000",
  "--print-to-pdf=" + pdf,
  html,
], { stdio: "inherit" });
console.log(pdf);
