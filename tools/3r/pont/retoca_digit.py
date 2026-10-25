# retoca_digit.py IN OUT "context|idx|new" ...  : substitueix el caràcter idx de cada aparició de context per new
import os, sys, pymupdf
S = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts") + "/"  # Atkinson Hyperlegible (OFL)
d = pymupdf.open(sys.argv[1]); jobs = [a.split("|") for a in sys.argv[3:]]
done = {j[0]: 0 for j in jobs}
for p in d:
    ins = []
    for blk in p.get_text("rawdict")["blocks"]:
        for l in blk.get("lines", []):
            for s in l["spans"]:
                txt = "".join(c["c"] for c in s["chars"])
                for ctx, idx, new in jobs:
                    st = txt.find(ctx)
                    while st >= 0:
                        c = s["chars"][st + int(idx)]
                        r = pymupdf.Rect(c["bbox"]); r.x0 += 0.6; r.x1 -= 0.6; r.y0 += 1; r.y1 -= 1
                        p.add_redact_annot(r, fill=False)
                        ins.append((c["origin"], new, s["font"], s["size"], s["color"]))
                        done[ctx] += 1; st = txt.find(ctx, st + 1)
    if ins:
        p.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE, text=pymupdf.PDF_REDACT_TEXT_REMOVE)
        for (x, y), new, font, size, col in ins:
            bold = "Bol" in font
            p.insert_font(fontname="AHB" if bold else "AHR", fontfile=S + ("AH-700.ttf" if bold else "AH-400.ttf"))
            p.insert_text((x, y), new, fontname="AHB" if bold else "AHR", fontsize=size, color=tuple(((col >> k) & 255) / 255 for k in (16, 8, 0)))
print(done)
d.save(sys.argv[2], garbage=3, deflate=True)
