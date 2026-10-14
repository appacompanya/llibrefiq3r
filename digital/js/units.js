/* Unitats i càlcul: àlgebra d'unitats (factors de conversió) i avaluació d'expressions LaTeX senzilles. */
(function (G) {
  "use strict";
  // magnituds base: L (longitud, m), M (massa, kg), T (temps, s), Th (temperatura, K), N (quantitat, mol), I (corrent, A)
  const BASE = {
    m:   { f: 1, d: { L: 1 } },
    g:   { f: 1e-3, d: { M: 1 } },
    s:   { f: 1, d: { T: 1 } },
    min: { f: 60, d: { T: 1 }, noPrefix: true },
    h:   { f: 3600, d: { T: 1 }, noPrefix: true },
    dia: { f: 86400, d: { T: 1 }, noPrefix: true },
    L:   { f: 1e-3, d: { L: 3 } },
    l:   { f: 1e-3, d: { L: 3 } },
    t:   { f: 1000, d: { M: 1 }, noPrefix: true },
    K:   { f: 1, d: { Th: 1 } },
    mol: { f: 1, d: { N: 1 } },
    N:   { f: 1, d: { M: 1, L: 1, T: -2 } },
    J:   { f: 1, d: { M: 1, L: 2, T: -2 } },
    W:   { f: 1, d: { M: 1, L: 2, T: -3 } },
    Wh:  { f: 3600, d: { M: 1, L: 2, T: -2 } },
    Pa:  { f: 1, d: { M: 1, L: -1, T: -2 } },
    atm: { f: 101325, d: { M: 1, L: -1, T: -2 }, noPrefix: true },
    A:   { f: 1, d: { I: 1 } },
    V:   { f: 1, d: { M: 1, L: 2, T: -3, I: -1 } },
    Hz:  { f: 1, d: { T: -1 } },
    "€": { f: 1, d: { EUR: 1 }, noPrefix: true },
  };
  const PREFIX = { G: 1e9, M: 1e6, k: 1e3, h: 1e2, da: 1e1, d: 1e-1, c: 1e-2, m: 1e-3, "µ": 1e-6, u: 1e-6, n: 1e-9 };
  const SUP = { "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-" };

  function token(sym) {
    if (BASE[sym]) return { sym, f: BASE[sym].f, d: BASE[sym].d };
    for (const p of Object.keys(PREFIX).sort((a, b) => b.length - a.length)) {
      if (sym.startsWith(p)) {
        const b = sym.slice(p.length);
        if (BASE[b] && !BASE[b].noPrefix) return { sym, f: PREFIX[p] * BASE[b].f, d: BASE[b].d };
      }
    }
    return null;
  }

  /** Converteix una unitat escrita ("km/h", "kg/m^3", "g·cm⁻³", "mL/s") en {terms:{sym:exp}, ok} */
  function parseUnit(str) {
    let s = String(str || "").trim().replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+/g, (m) => "^" + [...m].map((c) => SUP[c]).join(""));
    s = s.replace(/\\mathrm\{([^}]*)\}/g, "$1").replace(/\\cdot|·|\*|×/g, " ").replace(/\\,|~/g, " ").replace(/\{|\}/g, "");
    s = s.replace(/\bμ/g, "µ");
    const terms = {}; let ok = true;
    if (!s) return { terms, ok: true, empty: true };
    const parts = s.split("/");
    parts.forEach((part, i) => {
      const sign = i === 0 ? 1 : -1;
      part.trim().split(/\s+/).filter(Boolean).forEach((t) => {
        const m = t.match(/^([A-Za-zµ€]+)(?:\^?(-?\d+))?$/);
        if (!m || !token(m[1])) { ok = false; return; }
        const e = (m[2] ? parseInt(m[2], 10) : 1) * sign;
        terms[m[1]] = (terms[m[1]] || 0) + e;
      });
    });
    return { terms, ok };
  }

  function mul(a, b, k = 1) { const r = { ...a }; for (const [s, e] of Object.entries(b)) { r[s] = (r[s] || 0) + k * e; if (!r[s]) delete r[s]; } return r; }
  function siFactor(terms) { let f = 1; for (const [s, e] of Object.entries(terms)) f *= Math.pow(token(s).f, e); return f; }
  function dims(terms) { const d = {}; for (const [s, e] of Object.entries(terms)) for (const [k, v] of Object.entries(token(s).d)) { d[k] = (d[k] || 0) + v * e; if (!d[k]) delete d[k]; } return d; }
  function sameDims(a, b) { const da = dims(a), db = dims(b); const ks = new Set([...Object.keys(da), ...Object.keys(db)]); for (const k of ks) if ((da[k] || 0) !== (db[k] || 0)) return false; return true; }

  const supStr = (n) => String(n).split("").map((c) => ({ "-": "⁻", 0: "⁰", 1: "¹", 2: "²", 3: "³", 4: "⁴", 5: "⁵", 6: "⁶", 7: "⁷", 8: "⁸", 9: "⁹" })[c]).join("");
  function formatUnit(terms) {
    const num = [], den = [];
    for (const [s, e] of Object.entries(terms)) {
      if (e > 0) num.push(s + (e !== 1 ? supStr(e) : ""));
      if (e < 0) den.push(s + (e !== -1 ? supStr(-e) : ""));
    }
    if (!num.length && !den.length) return "";
    return (num.join("·") || "1") + (den.length ? "/" + (den.length > 1 ? den.join("·") : den[0]) : "");
  }

  /** nombre en català: "1,2", "1.2", "1,2·10^3", "1,2e3" */
  function parseNum(v) {
    if (typeof v === "number") return v;
    let s = String(v || "").trim().replace(/\s/g, "").replace(/−/g, "-");
    if (!s) return NaN;
    s = s.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+/g, (m) => "^" + [...m].map((c) => SUP[c]).join(""));
    const sci = s.match(/^([-+]?[\d.,]+)(?:[·*x×]10\^?\(?([-+]?\d+)\)?|e([-+]?\d+))?$/i);
    if (!sci) return NaN;
    let mant = sci[1];
    if (mant.includes(",")) mant = mant.replace(/\./g, "").replace(",", ".");
    const n = parseFloat(mant); const ex = sci[2] ?? sci[3];
    return ex != null ? n * Math.pow(10, parseInt(ex, 10)) : n;
  }

  function fmt(n, sig = 4) {
    if (!isFinite(n)) return "—";
    if (n === 0) return "0";
    const a = Math.abs(n);
    if (a >= 1e6 || a < 1e-3) {
      const e = Math.floor(Math.log10(a)); const m = n / Math.pow(10, e);
      return (+m.toPrecision(sig)).toString().replace(".", ",") + "·10" + supStr(e);
    }
    let t = String(+n.toPrecision(Math.max(sig, Math.floor(Math.log10(a)) + 1)));
    const [ip, fp] = t.split(".");
    const ipf = ip.replace(/\B(?=(\d{3})+(?!\d))/g, "\u2009");
    return fp ? ipf + "," + fp : ipf;
  }

  /** Cadena de factors: start {v,u}, factors [{nv,nu,dv,du}] -> {value, terms, unitStr, factorChecks, cancelled} */
  function chain(start, factors) {
    const s0 = parseUnit(start.u); let value = parseNum(start.v); let terms = s0.terms; let ok = s0.ok && isFinite(value);
    const checks = []; const all = [{ ...s0.terms }];
    for (const f of factors) {
      const nu = parseUnit(f.nu), du = parseUnit(f.du); const nv = parseNum(f.nv), dv = parseNum(f.dv);
      if (!nu.ok || !du.ok || !isFinite(nv) || !isFinite(dv) || dv === 0) { checks.push("incomplete"); ok = false; continue; }
      value = value * nv / dv; terms = mul(mul(terms, nu.terms), du.terms, -1);
      const isOne = sameDims(nu.terms, du.terms) && Math.abs(nv * siFactor(nu.terms) - dv * siFactor(du.terms)) <= 1e-6 * Math.abs(dv * siFactor(du.terms));
      checks.push(isOne ? "one" : (sameDims(nu.terms, du.terms) ? "notone" : "dims"));
    }
    return { ok, value, terms, unitStr: formatUnit(terms), checks };
  }

  /** compara una quantitat amb l'esperada (mateixa magnitud i valor dins de la tolerància relativa) */
  function sameQuantity(v, u, expV, expU, tol = 0.02, strict = false) {
    const a = parseUnit(u), b = parseUnit(expU); const x = parseNum(v), y = parseNum(expV);
    if (!a.ok || !b.ok || !isFinite(x) || !isFinite(y)) return { ok: false, reason: "format" };
    if (!sameDims(a.terms, b.terms)) return { ok: false, reason: "unit" };
    const xs = x * siFactor(a.terms), ys = y * siFactor(b.terms);
    const good = Math.abs(xs - ys) <= tol * Math.abs(ys) + 1e-12;
    const exactUnit = formatUnit(a.terms) === formatUnit(b.terms);
    if (strict && !exactUnit) return { ok: false, reason: "unit" };
    return { ok: good, reason: good ? (exactUnit ? "" : "unitat equivalent") : "value" };
  }

  /** Avalua LaTeX numèric senzill (\frac, \cdot, \times, ^, parèntesis, \sqrt, coma decimal) */
  function evalLatex(tex) {
    let s = String(tex || "");
    s = s.replace(/\\left|\\right|\\displaystyle/g, "").replace(/\\dfrac|\\tfrac/g, "\\frac").replace(/\\,|\\ |~/g, "")
      .replace(/\{,\}/g, ".").replace(/(\d),(\d)/g, "$1.$2").replace(/\\cdot|\\times/g, "*").replace(/÷|\\div/g, "/")
      .replace(/\\mathrm\{[^}]*\}|\\text\{[^}]*\}/g, "").replace(/\s+/g, "");
    let i = 0;
    const peek = () => s[i];
    function group() { if (peek() === "{") { i++; const v = expr(); if (s[i] === "}") i++; return v; } return atom(); }
    function atom() {
      if (s.startsWith("\\frac", i)) { i += 5; const a = group(); const b = group(); return a / b; }
      if (s.startsWith("\\sqrt", i)) { i += 5; return Math.sqrt(group()); }
      if (s.startsWith("\\pi", i)) { i += 3; return Math.PI; }
      if (peek() === "(" || peek() === "[") { i++; const v = expr(); if (s[i] === ")" || s[i] === "]") i++; return v; }
      if (peek() === "{") return group();
      const m = s.slice(i).match(/^\d+(\.\d+)?|^\.\d+/);
      if (m) { i += m[0].length; return parseFloat(m[0]); }
      throw new Error("syntax");
    }
    function power() { let b = atom(); while (peek() === "^") { i++; const e = peek() === "{" ? group() : atom(); b = Math.pow(b, e); } return b; }
    function unary() { if (peek() === "-") { i++; return -unary(); } if (peek() === "+") { i++; return unary(); } return power(); }
    function term() {
      let v = unary();
      for (;;) {
        if (peek() === "*") { i++; v *= unary(); }
        else if (peek() === "/") { i++; v /= unary(); }
        else if (peek() && /[\d(\\{]/.test(peek()) && !s.startsWith("\\right", i)) { v *= unary(); }
        else break;
      }
      return v;
    }
    function expr() { let v = term(); while (peek() === "+" || peek() === "-") { const op = s[i++]; const t = term(); v = op === "+" ? v + t : v - t; } return v; }
    try { if (!s) return NaN; const v = expr(); return i >= s.length ? v : NaN; } catch { return NaN; }
  }

  G.FQUnits = { parseUnit, parseNum, formatUnit, chain, sameQuantity, evalLatex, fmt, sameDims, siFactor };
})(window);
