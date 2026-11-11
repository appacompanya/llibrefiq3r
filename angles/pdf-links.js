/* Enllaços a PDF: a mòbil (pantalla tàctil i estreta, o navegador de mòbil) s'obre la versió mobil/<nom>_mobil.pdf,
   que té la mateixa numeració de pàgines. Ús: <a data-pdf="quadern_enunciats.pdf" data-page="12">, camí relatiu a la pàgina.
   L'usuari ho pot canviar amb BtxPDF.set("mobil"|"ordinador") (es desa al navegador). */
(function () {
  "use strict";
  var KEY = "btx-pdf";
  function auto() {
    var coarse = window.matchMedia && matchMedia("(pointer:coarse)").matches;
    var narrow = window.matchMedia && matchMedia("(max-width: 900px)").matches;
    var ua = /Android|iPhone|iPod|Mobi|Opera Mini|IEMobile/i.test(navigator.userAgent || "");
    return (coarse && narrow) || ua;
  }
  function mode() {
    var v = null;
    try { v = localStorage.getItem(KEY); } catch (e) {}
    return v === "mobil" || v === "ordinador" ? v : (auto() ? "mobil" : "ordinador");
  }
  function href(file, page, m) {
    var u = (m || mode()) === "mobil" ? file.replace(/([^\/]+)\.pdf$/, "mobil/$1_mobil.pdf") : file;
    return page ? u + "#page=" + page : u;
  }
  function apply(root) {
    var m = mode();
    document.documentElement.setAttribute("data-pdf", m);
    var els = (root || document).querySelectorAll("a[data-pdf]");
    for (var i = 0; i < els.length; i++) els[i].href = href(els[i].getAttribute("data-pdf"), els[i].getAttribute("data-page"), m);
    var bs = document.querySelectorAll("[data-pdfmode]");
    for (var j = 0; j < bs.length; j++) bs[j].setAttribute("aria-pressed", String(bs[j].getAttribute("data-pdfmode") === m));
  }
  function set(m) { try { localStorage.setItem(KEY, m); } catch (e) {} apply(); }
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-pdfmode]");
    if (b) set(b.getAttribute("data-pdfmode"));
  });
  window.BtxPDF = { mode: mode, href: href, apply: apply, set: set, auto: auto };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { apply(); });
  else apply();
})();
