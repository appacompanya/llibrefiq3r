"""Munta els quaderns (enunciats i solucions) a partir dels retalls dels exercicis."""
import pymupdf

A4 = pymupdf.paper_rect("a4")
MX, MT, MB = 40, 46, 50
W = A4.width - 2 * MX
BLUE = (0.16, 0.33, 0.58)
GREY = (0.93, 0.94, 0.95)
INK = (0.12, 0.12, 0.14)
MUTED = (0.42, 0.44, 0.48)
FD = "/usr/share/fonts/opentype/inter/"
FONTS = {False: ("inter", FD + "Inter-Regular.otf"), True: ("intersb", FD + "Inter-SemiBold.otf")}
_FOBJ = {k: pymupdf.Font(fontfile=v[1]) for k, v in FONTS.items()}


def _txt(page, x, y, s, size=9, bold=False, color=INK, align=0, width=None):
    name, path = FONTS[bold]
    if align == 1 and width:
        x = x + (width - _FOBJ[bold].text_length(s, fontsize=size)) / 2
    page.insert_text((x, y), s, fontsize=size, fontname=name, fontfile=path, color=color)


class Book:
    def __init__(self, title, subtitle):
        self.doc = pymupdf.open()
        self.title, self.subtitle = title, subtitle
        self.page = None
        self.y = 0
        self.bloc = ""
        self.srcs = {}
        self.toc = []  # (ex_num, label, bloc, page_no)

    def src(self, path):
        if path not in self.srcs:
            self.srcs[path] = pymupdf.open(path)
        return self.srcs[path]

    def new_page(self):
        self.page = self.doc.new_page(width=A4.width, height=A4.height)
        if self.bloc:
            _txt(self.page, MX, 28, self.bloc, 7.5, color=MUTED)
        self.y = MT

    def space(self, h):
        if self.page is None or self.y + h > A4.height - MB:
            self.new_page()

    def bloc_band(self, label):
        self.bloc = label.split("  (")[0]
        self.new_page()
        self.page.draw_rect(pymupdf.Rect(MX, self.y, MX + W, self.y + 24), color=None, fill=BLUE)
        _txt(self.page, MX + 8, self.y + 16.5, label, 12, True, (1, 1, 1))
        self.y += 34

    def ex_header(self, label, tags):
        self.space(70)
        self.page.draw_rect(pymupdf.Rect(MX, self.y, MX + W, self.y + 17), color=None, fill=GREY)
        _txt(self.page, MX + 6, self.y + 12, label, 9.5, True)
        self.y += 21
        if tags:
            _txt(self.page, MX + 6, self.y + 7, tags, 7.5, color=MUTED)
            self.y += 12
        self.y += 2

    def clip(self, path, pno, rect, maxscale=0.92):
        """Enganxa un retall vectorial; si no hi cap, el parteix entre pàgines."""
        src = self.src(path)
        scale = min(maxscale, W / rect.width)
        r = pymupdf.Rect(rect)
        while r.height > 1:
            avail = (A4.height - MB - self.y) / scale
            if avail < 40:
                self.new_page(); continue
            if r.height <= avail:
                part = r
            else:
                cut = self._cut(src[pno], r, r.y0 + avail)
                if cut <= r.y0 + 20:
                    if self.y > MT + 5:
                        self.new_page(); continue
                    cut = r.y0 + avail
                part = pymupdf.Rect(r.x0, r.y0, r.x1, cut)
            dst = pymupdf.Rect(MX, self.y, MX + part.width * scale, self.y + part.height * scale)
            self.page.show_pdf_page(dst, src, pno, clip=part)
            self.y += part.height * scale + 4
            r = pymupdf.Rect(r.x0, part.y1, r.x1, r.y1)
            if r.height > 1:
                self.new_page()

    @staticmethod
    def _cut(page, r, ymax):
        """Millor punt de tall (entre línies de text i sense partir dibuixos) per sota de ymax."""
        blocks = [pymupdf.Rect(b[:4]) for b in page.get_text("blocks", clip=r)]
        blocks += [d["rect"] for d in page.get_drawings() if d["rect"].intersects(r) and d["rect"].height > 3]
        blocks += [pymupdf.Rect(i["bbox"]) for i in page.get_image_info() if pymupdf.Rect(i["bbox"]).intersects(r)]
        y = ymax
        for _ in range(60):
            hit = [b for b in blocks if b.y0 < y < b.y1]
            if not hit:
                return y
            y = min(b.y0 for b in hit) - 1
            if y <= r.y0 + 20:
                break
        # si no hi ha cap tall net (dibuix molt alt), es talla entre línies de text
        lines = sorted(b[3] for b in page.get_text("blocks", clip=pymupdf.Rect(r.x0, r.y0, r.x1, ymax)))
        return (lines[-1] + 1) if lines else ymax

    def number_pages(self, first=1):
        for i, p in enumerate(self.doc):
            if i >= first:
                _txt(p, 0, A4.height - 24, f"– {i + 1} –", 8, color=MUTED, align=1, width=A4.width)

    def save(self, path):
        self.doc.set_metadata({"title": self.title, "author": "llibrefiq3r.cat", "subject": self.subtitle})
        self.doc.save(path, garbage=4, deflate=True)
