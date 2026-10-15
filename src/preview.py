#!/usr/bin/env python3
"""Render the layout sheets used by the README and by Discord posts.

    python3 src/preview.py

Writes assets/preview/page_*.png (xl_page_*.png for the XL) and one overview per
profile: overview.png (15 keys), overview-xl.png. Keys the plugin paints are shown as
it draws them once paired, with no state yet (a combined key unlit, a value as a
dash); animated keys on their first frame.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build as BLD    # noqa: E402
import layout as L     # noqa: E402
import tactical as T   # noqa: E402

OUT = os.path.join(BLD.ROOT, "assets", "preview")
TILE, GAP, PAD, HEAD = 150, 10, 22, 54
BG = (10, 13, 17)
EMPTY = (6, 8, 10)
RULE = (40, 46, 52)


def rgb(colour):
    return tuple(int(colour[i:i + 2], 16) for i in (1, 3, 5))


def page_sheet(lay, page_key):
    page = lay["pages"][page_key]
    cols, rows = lay["cols"], lay["rows"]
    w = PAD * 2 + cols * TILE + (cols - 1) * GAP
    h = PAD * 2 + rows * TILE + (rows - 1) * GAP + HEAD
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join(T.FONTS, "chakra_petch_bold.ttf"), 26)
    d.text((PAD, PAD + 6), lay["titles"][page_key].upper(), font=font, fill=rgb(T.INK))
    top = PAD + HEAD
    d.line([(PAD, top - 14), (w - PAD, top - 14)], fill=RULE, width=2)
    for r in range(rows):
        for c in range(cols):
            x, y = PAD + c * (TILE + GAP), top + r * (TILE + GAP)
            btn = page["keys"].get((c, r))
            if btn is None:
                d.rectangle([x, y, x + TILE - 1, y + TILE - 1], fill=EMPTY, outline=RULE, width=2)
            else:
                im.paste(T.to_image(BLD.face(btn), TILE), (x, y))
    return im


def board(sheets, cols):
    rows = (len(sheets) + cols - 1) // cols
    w = sheets[0].width * cols + GAP * (cols + 1)
    h = sheets[0].height * rows + GAP * (rows + 1)
    out = Image.new("RGB", (w, h), (4, 6, 8))
    for i, s in enumerate(sheets):
        out.paste(s, (GAP + (i % cols) * (s.width + GAP), GAP + (i // cols) * (s.height + GAP)))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    for old in os.listdir(OUT):
        os.remove(os.path.join(OUT, old))
    for lay in L.LAYOUTS:
        sheets = []
        for key in lay["order"]:
            im = page_sheet(lay, key)
            im.save(os.path.join(OUT, f"{lay['slug']}page_{key}.png"), optimize=True)
            sheets.append(im)
        name = "overview.png" if lay["key"] == "15" else f"overview-{lay['key']}.png"
        board(sheets, 2).save(os.path.join(OUT, name), optimize=True)
        print(f"{lay['name']} : {len(sheets)} planches + {name}")


if __name__ == "__main__":
    main()
