/* Biologia: amplia les figures (SVG incrustat o imatge) en una capa a pantalla completa, amb desplaçament i zoom tàctil. */
(function () {
  "use strict";
  var css = ".fz{position:fixed;inset:0;z-index:1000;background:rgba(16,19,24,.9);overflow:auto;-webkit-overflow-scrolling:touch;padding:56px 12px 24px;cursor:zoom-out}" +
    ".fz .fz-in{background:#fff;border-radius:14px;padding:10px;margin:0 auto;width:max(100%,900px);max-width:1400px}" +
    ".fz svg,.fz img{display:block;width:100%;height:auto}" +
    ".fz p{color:#fff;font:600 .9rem/1.4 system-ui,sans-serif;max-width:70ch;margin:12px auto 0}" +
    ".fz-x{position:fixed;top:10px;right:10px;width:44px;height:44px;border-radius:50%;border:0;background:#fff;color:#1b1f24;font:700 26px/1 system-ui;cursor:pointer;z-index:1001}" +
    "figure .fig-in{cursor:zoom-in;position:relative}figure .fig-in::after{content:'⤢';position:absolute;right:8px;bottom:8px;width:26px;height:26px;border-radius:50%;background:#1b1f24;color:#fff;font:700 15px/26px system-ui;text-align:center;opacity:.75}" +
    "figure.map .fig-in::after{display:none}html.fz-open{overflow:hidden}@media print{figure .fig-in::after{display:none}}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  var box = null;
  function close() { if (box) { box.remove(); box = null; document.documentElement.classList.remove("fz-open"); } }
  document.addEventListener("click", function (e) {
    var fi = e.target.closest && e.target.closest("figure .fig-in");
    if (!fi || box) return;
    e.preventDefault(); e.stopPropagation();
    var fig = fi.parentNode, cap = fig.querySelector("figcaption");
    box = document.createElement("div"); box.className = "fz"; box.setAttribute("role", "dialog"); box.setAttribute("aria-modal", "true");
    var inner = document.createElement("div"); inner.className = "fz-in";
    var c = fi.querySelector("svg,img").cloneNode(true); c.removeAttribute("data-zoom"); inner.appendChild(c);
    box.appendChild(inner);
    if (cap) { var p = document.createElement("p"); p.textContent = cap.textContent; box.appendChild(p); }
    var x = document.createElement("button"); x.className = "fz-x"; x.type = "button"; x.setAttribute("aria-label", "Tanca"); x.textContent = "×"; box.appendChild(x);
    box.addEventListener("click", function (ev) { if (ev.target === box || ev.target === x) close(); });
    document.body.appendChild(box); document.documentElement.classList.add("fz-open"); x.focus();
  }, true);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
})();
