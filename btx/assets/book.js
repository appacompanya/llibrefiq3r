/* Llibre de Física · navegació: calaix lateral, scroll-spy, progrés de lectura i botó per tornar a dalt. Sense dependències. */
(function () {
  "use strict";
  var body = document.body, menu = document.querySelector(".menu"), side = document.getElementById("side");
  function drawer(open) {
    body.classList.toggle("drawer", open);
    if (menu) menu.setAttribute("aria-expanded", String(open));
    if (open && side) { var a = side.querySelector("a[aria-current],.active,a"); if (a) a.focus({ preventScroll: true }); }
  }
  if (menu) menu.addEventListener("click", function () { drawer(!body.classList.contains("drawer")); });
  var scrim = document.querySelector(".scrim"); if (scrim) scrim.addEventListener("click", function () { drawer(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && body.classList.contains("drawer")) { drawer(false); if (menu) menu.focus(); } });
  if (side) side.addEventListener("click", function (e) { if (e.target.closest("a") && window.matchMedia("(max-width:1080px)").matches) drawer(false); });

  // scroll-spy dels subtemes de la pàgina actual
  var links = side ? Array.prototype.slice.call(side.querySelectorAll('.toc li.cur ol a[href*="#"]')) : [];
  var items = links.map(function (a) { var id = a.getAttribute("href").split("#")[1]; return { a: a, el: document.getElementById(id) }; }).filter(function (x) { return x.el; });
  var crumb = document.getElementById("crumb-sub"), bar = document.querySelector(".progress"), top = document.querySelector(".totop");
  var current = null, ticking = false;
  function update() {
    ticking = false;
    var y = window.scrollY, h = document.documentElement.scrollHeight - window.innerHeight;
    if (bar) bar.style.transform = "scaleX(" + (h > 0 ? Math.min(1, y / h) : 0) + ")";
    if (top) top.classList.toggle("on", y > 900);
    var line = 120, act = null;
    for (var i = 0; i < items.length; i++) { if (items[i].el.getBoundingClientRect().top - line <= 0) act = items[i]; else break; }
    if (act !== current) {
      if (current) current.a.classList.remove("active");
      current = act;
      if (act) { act.a.classList.add("active"); var r = act.a.getBoundingClientRect(), sr = side.getBoundingClientRect(); if (r.top < sr.top + 60 || r.bottom > sr.bottom - 20) act.a.scrollIntoView({ block: "nearest" }); }
      if (crumb) { crumb.textContent = act ? act.a.getAttribute("data-short") : ""; crumb.hidden = !act; if (crumb.previousElementSibling) crumb.previousElementSibling.hidden = !act; }
    }
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; setTimeout(update, 60); } }, { passive: true });
  window.addEventListener("resize", update);
  update();
})();
