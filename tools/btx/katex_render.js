// Renderitza amb KaTeX (mateixa versió que btx/assets/katex.css) una llista JSON [[tex, display], ...] llegida de stdin.
const path = require("path");
const dir = process.env.KATEX_DIR || path.join(__dirname, "node_modules");
const katex = require(require.resolve("katex", { paths: [dir, __dirname] }));
let inp = "";
process.stdin.on("data", (d) => (inp += d));
process.stdin.on("end", () => {
  const out = JSON.parse(inp).map(([tex, disp]) => {
    try { return katex.renderToString(tex, { displayMode: !!disp, output: "html", throwOnError: true, strict: "ignore" }); }
    catch (e) { console.error("KaTeX: " + e.message + "\n  a: " + tex); process.exitCode = 1; return "ERR"; }
  });
  process.stdout.write(JSON.stringify(out));
});
