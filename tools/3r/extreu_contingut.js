/* Extracció única (fase 1, 24/10/2026): llegeix les dades escrites a mà a les pàgines publicades
   (digital/profe.html, digital/index.html, index.html, digital/js/fitxes*.js) i en treu un JSON intermedi
   que extreu_contingut.py converteix en contingut/3r/*.yaml. No modifica res.
   Ús: node tools/3r/extreu_contingut.js > /tmp/extret.json */
const path = require("path");
const grab = require("./lib/jsliteral.js");
const ROOT = path.resolve(__dirname, "..", "..");
const P = (f) => path.join(ROOT, f);
const out = {};
for (const n of ["D", "L", "SDAS", "EVAL", "CRIT_NAMES"]) out[n] = grab(P("digital/profe.html"), n).val;
out.L_arrel = grab(P("index.html"), "L").val;
global.window = {};
require(P("digital/js/fitxes.js"));
const manual = new Set(Object.keys(window.FITXES));
require(P("digital/js/fitxes-auto.js"));
const strip = (h) => String(h || "").replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ").replace(/\s+/g, " ").trim();
const short = (s, n = 90) => (s.length > n ? s.slice(0, n - 1).trimEnd() + "…" : s);
out.FITXES = {};
for (const [ws, f] of Object.entries(window.FITXES)) {
  const pq = [];
  if (manual.has(ws)) {
    for (const b of f.blocks) {
      if (!b.id) continue;
      const camps = b.type === "group" ? b.items.map((x) => String(x.id)) : [String(b.id)];
      pq.push({ id: String(b.id), tipus: b.type, etiqueta: short(strip(b.prompt || b.title || "")), camps });
    }
  } else {
    const byq = {};
    for (const [fid, fl] of Object.entries(f.fields || {})) (byq[String(fl.q)] = byq[String(fl.q)] || []).push(fid);
    const qs = f.qs || {};
    const ids = [...new Set([...Object.keys(qs), ...Object.keys(byq)])];
    for (const q of ids) pq.push({ id: q, tipus: "auto", etiqueta: short(strip(qs[q] || "")), camps: byq[q] || [] });
  }
  out.FITXES[ws] = { origen: manual.has(ws) ? "manual" : "auto", sda: f.sda, titol: f.title, preguntes: pq };
}
process.stdout.write(JSON.stringify(out));
