/* Amplia les portades: qualsevol element amb data-zoom="imatge.webp" obre la imatge gran en una capa.
   Es tanca amb un clic, la tecla Esc o el botó ×. Sense dependències; porta el seu propi CSS. */
(function () {
  "use strict";
  var css = ".lb{position:fixed;inset:0;z-index:1000;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;padding:max(14px,env(safe-area-inset-top)) 14px 14px;background:rgba(16,19,24,.86);cursor:zoom-out;opacity:0;transition:opacity .18s}" +
    ".lb.on{opacity:1}.lb img{display:block;max-width:min(1200px,100%);max-height:calc(100vh - 90px);max-height:calc(100dvh - 90px);width:auto;height:auto;border:4px solid #1b1f24;border-radius:16px;background:#fff;box-shadow:0 20px 60px rgba(0,0,0,.5)}" +
    ".lb p{margin:0;color:#fff;font:700 .95rem/1.3 system-ui,sans-serif;text-align:center;max-width:60ch}" +
    ".lb .lb-x{position:absolute;top:10px;right:10px;width:44px;height:44px;border-radius:50%;border:3px solid #1b1f24;background:#fff;color:#1b1f24;font:700 26px/1 system-ui,sans-serif;cursor:pointer}" +
    "html.lb-open{overflow:hidden}[data-zoom]{cursor:zoom-in}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  var box = null, last = null;
  function close() {
    if (!box) return;
    box.remove(); box = null; document.documentElement.classList.remove("lb-open");
    if (last) last.focus({ preventScroll: true });
  }
  function open(el) {
    close(); last = el;
    var alt = el.getAttribute("data-zoom-alt") || "";
    box = document.createElement("div");
    box.className = "lb"; box.setAttribute("role", "dialog"); box.setAttribute("aria-modal", "true"); box.setAttribute("aria-label", alt || "Imatge ampliada");
    var img = document.createElement("img"); img.src = el.getAttribute("data-zoom"); img.alt = alt;
    var x = document.createElement("button"); x.type = "button"; x.className = "lb-x"; x.setAttribute("aria-label", "Tanca"); x.textContent = "×";
    box.appendChild(img);
    if (alt) { var p = document.createElement("p"); p.textContent = alt; box.appendChild(p); }
    box.appendChild(x);
    box.addEventListener("click", close);
    document.body.appendChild(box); document.documentElement.classList.add("lb-open");
    requestAnimationFrame(function () { if (box) box.classList.add("on"); });
    x.focus({ preventScroll: true });
  }
  document.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest("[data-zoom]");
    if (el) { e.preventDefault(); e.stopPropagation(); open(el); }
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && box) { e.stopPropagation(); close(); } }, true);
})();
