/* Problemes PAU: capítols i cercador d'exercicis a partir d'exercicis.json (generat per tools/btx-pau/build.py) */
(function () {
  "use strict";
  var $ = function (s) { return document.querySelector(s); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); };
  var norm = function (s) { return String(s).toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/·/g, "."); };
  var COLORS = ["--s1", "--s2", "--s3", "--s4", "--s5", "--s6"];
  var D, CH = {}, rows = [], shown = 0, PAGE = 60;
  var col = function (c) { return "var(" + COLORS[(c.n - 1) % COLORS.length] + ")"; };
  var nf = function (n, a, b) { return n + " " + (n === 1 ? a : b); };

  function chapterTiles(kind) {
    return D.capitols.map(function (c) {
      var f = kind === "e" ? c.enunciats : c.solucions, p = kind === "e" ? c.pagines_enunciats : c.pagines_solucions;
      return '<a class="ch" style="--c:' + col(c) + '" data-pdf="' + esc(f) + '" href="' + esc(f) + '" target="_blank" rel="noopener"><span class="n">' + c.n + '</span><span><b>' + esc(c.titol) + '</b><span>' +
        nf(c.exercicis, "exercici", "exercicis") + " · " + nf(p, "pàgina", "pàgines") + '</span></span></a>';
    }).join("");
  }
  function label(x) {
    if (x.model) return "Model de la Generalitat " + x.any + " · " + x.exercici;
    return "PAU " + x.any + " · " + x.conv + (x.serie !== "—" && x.serie != null ? " · Sèrie " + x.serie : "") + " · " + x.exercici;
  }
  function opt(sel, vals) { sel.insertAdjacentHTML("beforeend", vals.map(function (v) { return '<option value="' + esc(v[0]) + '">' + esc(v[1]) + "</option>"; }).join("")); }

  function filter() {
    var q = norm($("#fq").value.trim()), c = $("#fc").value, s = $("#fs").value, a = $("#fa").value, v = $("#fv").value, two = $("#f2").checked;
    var words = q ? q.split(/\s+/) : [];
    rows = D.exercicis.filter(function (x) {
      if (c && !(x.cap === c || (two && x.cap2 === c))) return false;
      if (s && x.sub.indexOf(s) < 0) return false;
      if (a && String(x.any) !== a) return false;
      if (v && x.conv !== v) return false;
      for (var i = 0; i < words.length; i++) if (x._h.indexOf(words[i]) < 0) return false;
      return true;
    });
    if ($("#fo").checked) rows = rows.slice().sort(function (p, r) { return r.any - p.any || p.ex - r.ex; });
    var subs = {};
    D.exercicis.forEach(function (x) { if (!c || x.cap === c || (two && x.cap2 === c)) x.sub.forEach(function (t) { subs[t] = 1; }); });
    Array.prototype.forEach.call($("#fs").options, function (o) { if (o.value) o.hidden = !subs[o.value]; });
    $("#count").textContent = nf(rows.length, "exercici", "exercicis") + (rows.length !== D.exercicis.length ? " de " + D.exercicis.length : "");
    var p = new URLSearchParams();
    if (c) p.set("cap", c); if (s) p.set("tipus", s); if (a) p.set("any", a); if (v) p.set("conv", v); if (q) p.set("q", $("#fq").value.trim());
    var qs = p.toString();
    history.replaceState(null, "", (qs ? "?" + qs : location.pathname) + location.hash);
    shown = 0; $("#list").innerHTML = ""; render();
  }
  function render() {
    var next = rows.slice(shown, shown + PAGE);
    if (!rows.length) $("#list").innerHTML = '<div class="empty">Cap exercici amb aquests filtres.</div>';
    $("#list").insertAdjacentHTML("beforeend", next.map(function (x) {
      var c = CH[x.cap], c2 = x.cap2 && CH[x.cap2];
      return '<article class="ex" style="--c:' + col(c) + '" id="ex-' + x.ex + '"><div><div class="t">' + esc(label(x)) + '</div><div class="m"><span class="capn">' + c.n + ". " + esc(c.titol) + "</span>" +
        (c2 ? '<span class="chip" title="També toca aquest capítol">+ ' + esc(c2.titol) + "</span>" : "") +
        x.sub.map(function (t) { return '<span class="chip">' + esc(t) + "</span>"; }).join("") +
        (x.ue ? '<span class="off">oficial: <a href="' + esc(x.ue) + '" target="_blank" rel="noopener">enunciat</a>' +
          (x.us && x.us !== x.ue ? ' · <a href="' + esc(x.us) + '" target="_blank" rel="noopener">solució</a>' : "") + "</span>" : "") + "</div></div>" +
        '<div class="acts"><a class="btn" data-pdf="' + esc(x.e) + '" data-page="' + x.pe + '" href="' + esc(x.e) + "#page=" + x.pe + '" target="_blank" rel="noopener">Enunciat <small>pàg. ' + x.pe + "</small></a>" +
        '<a class="btn ghost" data-pdf="' + esc(x.s) + '" data-page="' + x.ps + '" href="' + esc(x.s) + "#page=" + x.ps + '" target="_blank" rel="noopener">Veure solució <small>pàg. ' + x.ps + "</small></a></div></article>";
    }).join(""));
    shown += next.length;
    $("#more").hidden = shown >= rows.length;
    window.BtxPDF.apply($("#list"));
  }
  function modeNote() { $("#modeNote").textContent = window.BtxPDF.mode() === "mobil" ? "(PDF adaptats a pantalla petita)" : ""; }

  fetch("exercicis.json").then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); }).then(function (d) {
    D = d; D.capitols.forEach(function (c) { CH[c.slug] = c; });
    D.exercicis.forEach(function (x) { x._h = norm([label(x), CH[x.cap].titol, x.cap2 ? CH[x.cap2].titol : "", x.sub.join(" ")].join(" ")); });
    $("#lead").textContent = "Els " + D.meta.total + " exercicis de les PAU de Física de Catalunya (" + D.meta.anys[0] + "–" + D.meta.anys[1] + "), ordenats en " + (["", "un", "dos", "tres", "quatre", "cinc", "sis", "set", "vuit", "nou", "deu", "onze", "dotze"][D.capitols.length] || D.capitols.length) + " capítols. Els enunciats i el solucionari són documents separats.";
    $("#qeMeta").textContent = "Tots els capítols en un sol PDF · " + D.meta.pagines_quadern_enunciats + " pàgines";
    $("#qsMeta").textContent = "Totes les solucions en un sol PDF · " + D.meta.pagines_quadern_solucions + " pàgines";
    $("#chE").innerHTML = chapterTiles("e"); $("#chS").innerHTML = chapterTiles("s");
    opt($("#fc"), D.capitols.map(function (c) { return [c.slug, c.n + ". " + c.titol]; }));
    var subs = {}, anys = {}, convs = {};
    D.exercicis.forEach(function (x) { x.sub.forEach(function (t) { subs[t] = (subs[t] || 0) + 1; }); anys[x.any] = 1; convs[x.conv] = 1; });
    opt($("#fs"), Object.keys(subs).sort(function (a, b) { return a.localeCompare(b, "ca"); }).map(function (t) { return [t, t + " (" + subs[t] + ")"]; }));
    opt($("#fa"), Object.keys(anys).sort().reverse().map(function (y) { return [y, y]; }));
    opt($("#fv"), ["Juny", "Juliol", "Setembre", "Model"].filter(function (v) { return convs[v]; }).map(function (v) { return [v, v]; }));
    var p = new URLSearchParams(location.search);
    if (CH[p.get("cap")]) $("#fc").value = p.get("cap");
    if (p.get("tipus")) $("#fs").value = p.get("tipus");
    if (p.get("any")) $("#fa").value = p.get("any");
    if (p.get("conv")) $("#fv").value = p.get("conv");
    if (p.get("q")) $("#fq").value = p.get("q");
    ["#fq", "#fc", "#fs", "#fa", "#fv", "#f2", "#fo"].forEach(function (s) { $(s).addEventListener(s === "#fq" ? "input" : "change", filter); });
    $("#fr").addEventListener("click", function () { $("#f").reset(); filter(); });
    $("#more").addEventListener("click", render);
    filter(); window.BtxPDF.apply(); modeNote();
    if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
  }).catch(function (e) {
    $("#list").innerHTML = '<div class="empty">No s\'ha pogut carregar l\'índex d\'exercicis (' + esc(e.message) + ').</div>';
  });
  document.addEventListener("click", function (e) { if (e.target.closest && e.target.closest("[data-pdfmode]")) setTimeout(modeNote, 0); });
})();
