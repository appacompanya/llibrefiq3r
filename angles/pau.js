/* Exàmens PAU d'Anglès per blocs (adaptat dels exercicis PAU de Física i Biologia):
   blocs, quaderns i llista d'exàmens amb àudio a partir d'exercicis.json (generat per tools/angles-pau/build.py) */
(function () {
  "use strict";
  var $ = function (s) { return document.querySelector(s); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); };
  var norm = function (s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/·/g, "."); };
  var COLORS = { listening: "var(--s4)", reading: "var(--s1)", writing: "var(--s2)" };
  var ICON = { listening: "L", reading: "R", writing: "W" };
  var D, CH = {}, rows = [], shown = 0, PAGE = 30;
  var nf = function (n, a, b) { return n + " " + (n === 1 ? a : b); };
  var mmss = function (s) { return s ? Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0") : ""; };

  function tiles(kind) {
    return D.capitols.map(function (c) {
      var f = kind === "e" ? c.enunciats : c.solucions, p = kind === "e" ? c.pagines_enunciats : c.pagines_solucions;
      var n = kind === "e" ? c.exercicis : c.solucions_n;
      return '<div class="chw" style="--c:' + COLORS[c.slug] + ';--np:1"><span class="chpics" aria-hidden="true"><img src="img/' + c.slug + '_thumb.webp" alt="" loading="lazy" decoding="async" width="600" height="400"></span>' +
        '<a class="ch" data-pdf="' + esc(f) + '" href="' + esc(f) + '" target="_blank" rel="noopener"><span class="n">' + ICON[c.slug] + '</span><span><b>' + esc(c.titol) + "</b><span>" +
        esc(c.sub) + " · " + nf(n, "examen", "exàmens") + " · " + nf(p, "pàgina", "pàgines") + "</span></span></a></div>";
    }).join("");
  }
  function label(x) {
    return "PAU " + x.any + " · " + x.conv + (x.tei ? " (TEI)" : "") + (x.serie ? " · Sèrie " + x.serie : "");
  }
  function opt(sel, vals) { sel.insertAdjacentHTML("beforeend", vals.map(function (v) { return '<option value="' + esc(v[0]) + '">' + esc(v[1]) + "</option>"; }).join("")); }

  function filter() {
    var q = norm($("#fq").value.trim()), c = $("#fc").value, s = $("#fs").value, a = $("#fa").value, v = $("#fv").value;
    var words = q ? q.split(/\s+/) : [];
    rows = D.exercicis.filter(function (x) {
      if (s && x.model !== s) return false;
      if (a && String(x.any) !== a) return false;
      if (v && x.conv !== v) return false;
      for (var i = 0; i < words.length; i++) if (x._h.indexOf(words[i]) < 0) return false;
      return true;
    });
    if (!$("#fo").checked) rows = rows.slice().reverse();
    $("#count").textContent = nf(rows.length, "examen", "exàmens") + (rows.length !== D.exercicis.length ? " de " + D.exercicis.length : "");
    var p = new URLSearchParams();
    if (c) p.set("bloc", c); if (s) p.set("model", s); if (a) p.set("any", a); if (v) p.set("conv", v); if (q) p.set("q", $("#fq").value.trim());
    var qs = p.toString();
    history.replaceState(null, "", (qs ? "?" + qs : location.pathname) + location.hash);
    shown = 0; $("#list").innerHTML = ""; render();
  }
  function blocBtns(x, b) {
    var c = CH[b], pp = x.p[b], h = "";
    if (!pp || !pp.e) return "";
    h += '<span class="grp">';
    h += '<a class="btn" style="--acc:' + COLORS[b] + '" data-pdf="' + esc(c.enunciats) + '" data-page="' + pp.e + '" href="' + esc(c.enunciats) + "#page=" + pp.e + '" target="_blank" rel="noopener">' + c.titol + " <small>pàg. " + pp.e + "</small></a>";
    if (pp.s) h += '<a class="btn ghost" data-pdf="' + esc(c.solucions) + '" data-page="' + pp.s + '" href="' + esc(c.solucions) + "#page=" + pp.s + '" target="_blank" rel="noopener">Solució <small>pàg. ' + pp.s + "</small></a>";
    return h + "</span>";
  }
  function render() {
    var c = $("#fc").value;
    var blocs = c ? [c] : ["listening", "reading", "writing"];
    var next = rows.slice(shown, shown + PAGE);
    if (!rows.length) $("#list").innerHTML = '<div class="empty">Cap examen amb aquests filtres.</div>';
    $("#list").insertAdjacentHTML("beforeend", next.map(function (x) {
      var col = c ? COLORS[c] : "var(--s4)";
      var chips = "";
      if (x.lt && (!c || c === "listening")) chips += '<span class="chip" title="Listening">Listening: ' + esc(x.lt) + "</span>";
      if (x.rt && (!c || c === "reading")) chips += '<span class="chip" title="Reading">Reading: ' + esc(x.rt) + "</span>";
      var acts = "";
      if (x.a && (!c || c === "listening")) acts += '<button type="button" class="btn" style="--acc:var(--s4)" data-audio="' + esc(x.a) + '" aria-expanded="false">▶ Àudio <small>' + mmss(x.dur) + "</small></button>";
      acts += blocs.map(function (b) { return blocBtns(x, b); }).join("");
      return '<article class="ex" style="--c:' + col + '" id="ex-' + esc(x.id) + '"><div><div class="t">' + esc(label(x)) + '</div><div class="m"><span class="capn">' + esc(x.model) + "</span>" + chips + "</div></div>" +
        '<div class="acts">' + acts + "</div></article>";
    }).join(""));
    shown += next.length;
    $("#more").hidden = shown >= rows.length;
    window.BtxPDF.apply($("#list"));
  }
  function modeNote() { $("#modeNote").textContent = window.BtxPDF.mode() === "mobil" ? "(PDF adaptats a pantalla petita)" : ""; }

  /* Àudio: un sol reproductor a la vegada, dins la fitxa de l'examen */
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-audio]");
    if (!b) return;
    var art = b.closest(".ex"), cur = art.querySelector("audio");
    document.querySelectorAll(".ex audio").forEach(function (a) {
      if (a !== cur) { a.pause(); a.remove(); }
    });
    document.querySelectorAll("[data-audio][aria-expanded=true]").forEach(function (x) { if (x !== b) { x.setAttribute("aria-expanded", "false"); x.firstChild.nodeValue = "▶ Àudio "; } });
    if (cur) { cur.pause(); cur.remove(); b.setAttribute("aria-expanded", "false"); b.firstChild.nodeValue = "▶ Àudio "; return; }
    var au = document.createElement("audio");
    au.controls = true; au.preload = "metadata"; au.src = b.getAttribute("data-audio");
    art.appendChild(au);
    b.setAttribute("aria-expanded", "true"); b.firstChild.nodeValue = "✕ Tanca l'àudio ";
    var p = au.play(); if (p && p.catch) p.catch(function () {});
  });

  fetch("exercicis.json").then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); }).then(function (d) {
    D = d; D.capitols.forEach(function (c) { CH[c.slug] = c; });
    D.exercicis.forEach(function (x) { x._h = norm([label(x), x.lt, x.rt, x.model].join(" ")); });
    $("#lead").textContent = "Els " + D.meta.total + " exàmens d'anglès de les PAU de Catalunya (" + D.meta.anys[0] + "–" + D.meta.anys[1] + "), separats en tres blocs: Listening, Reading i Writing. Tots els listenings tenen l'àudio. Els enunciats i el solucionari són documents separats.";
    $("#qeMeta").textContent = "Els tres blocs en un sol PDF · " + D.meta.pagines_quadern_enunciats + " pàgines";
    $("#qsMeta").textContent = "Totes les solucions en un sol PDF · " + D.meta.pagines_quadern_solucions + " pàgines";
    $("#chE").innerHTML = tiles("e"); $("#chS").innerHTML = tiles("s");
    opt($("#fc"), D.capitols.map(function (c) { return [c.slug, c.titol]; }));
    opt($("#fs"), [["Model actual", "Model actual (2025–)"], ["Model anterior", "Model anterior (fins al 2024)"]]);
    var anys = {}; D.exercicis.forEach(function (x) { anys[x.any] = 1; });
    opt($("#fa"), Object.keys(anys).sort().reverse().map(function (y) { return [y, y]; }));
    opt($("#fv"), [["Juny", "Juny"], ["Setembre", "Setembre"]]);
    var p = new URLSearchParams(location.search);
    if (CH[p.get("bloc")]) $("#fc").value = p.get("bloc");
    if (p.get("model")) $("#fs").value = p.get("model");
    if (p.get("any")) $("#fa").value = p.get("any");
    if (p.get("conv")) $("#fv").value = p.get("conv");
    if (p.get("q")) $("#fq").value = p.get("q");
    ["#fq", "#fc", "#fs", "#fa", "#fv", "#fo"].forEach(function (s) { $(s).addEventListener(s === "#fq" ? "input" : "change", filter); });
    $("#fr").addEventListener("click", function () { $("#f").reset(); filter(); });
    $("#more").addEventListener("click", render);
    filter(); window.BtxPDF.apply(); modeNote();
    if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
  }).catch(function (e) {
    $("#list").innerHTML = '<div class="empty">No s\'ha pogut carregar la llista d\'exàmens (' + esc(e.message) + ").</div>";
  });
  document.addEventListener("click", function (e) { if (e.target.closest && e.target.closest("[data-pdfmode]")) setTimeout(modeNote, 0); });
})();
