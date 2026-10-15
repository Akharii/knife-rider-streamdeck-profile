"""Keys drawn in the Farline companion's Tactical style.

Port of the plugin's `src/render.ts` + `src/palette.ts` (Farline companion v0.1.0, MIT,
github.com/david-digitis/Farline-companion), so the keys this profile draws itself (folders,
Back, the native hotkeys) sit next to the plugin's keys without a seam:
no frame, a large Material Symbols Sharp pictogram, everything in ink, the accent only on
a state (the plugin's job), no glow, no gradient, no rounded corner.

Every key is an SVG (144 x 144, the Stream Deck's @2x key) rasterised by resvg with the
game's own fonts (src/fonts/, never shipped). Animations are drawn in ink only: mint is the
plugin's colour for "ON", and an animation must never look like a state.
"""
import io
import math
import os
import re

import resvg_py
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
SYMBOLS = os.path.join(HERE, "symbols")

SIZE = 144
CUT = 16
NUM_FONT = "Chakra Petch, Bahnschrift, sans-serif"
LABEL_FONT = "DM Mono, Consolas, monospace"

# --- palette (the game's UiTokens, as the plugin copies them) -----------------
BG = "#0f1419"
INK = "#ece8e1"
INK_DIM = "#ece8e199"
INK_OFF = "#ece8e161"
INK_TRACK = "#ece8e11f"
MINT = "#3ee6b4"
CORAL = "#ff5e5b"
BLUE = "#8fb8ff"


def fill(colour, attr="fill"):
    """#rrggbb as is; #rrggbbaa split into #rrggbb + opacity (Qt reads 8 digits as #aarrggbb)."""
    if len(colour) != 9:
        return f'{attr}="{colour}"'
    alpha = round(int(colour[7:], 16) / 255, 2)
    return f'{attr}="{colour[:7]}" {attr}-opacity="{alpha}"'


def escape(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


# --- glyphs ---------------------------------------------------------------------
_paths = {}


def symbol_file(symbol, filled=False):
    return os.path.join(SYMBOLS, f"{symbol}-fill.svg" if filled else f"{symbol}.svg")


def path_of(symbol, filled=False):
    name = (symbol, filled)
    if name not in _paths:
        with open(symbol_file(symbol, filled), encoding="utf-8") as fh:
            m = re.search(r'\sd="([^"]+)"', fh.read())
        if m is None:
            raise ValueError(f"no path in {symbol_file(symbol, filled)}")
        _paths[name] = m.group(1)
    return _paths[name]


def glyph(symbol, filled, x, y, size, colour, extra=""):
    """A 960-unit Material Symbol (top at y = -960) drawn `size` px square at (x, y)."""
    k = size / 960
    return (f'<path transform="translate({x} {y + size}) scale({k})" {fill(colour)} {extra}'
            f'd="{path_of(symbol, filled)}"/>')


# --- text -------------------------------------------------------------------------
def text(x, y, size, colour, body, num=False, anchor="middle"):
    font = (f'font-family="{NUM_FONT}" font-weight="700"' if num
            else f'font-family="{LABEL_FONT}" font-weight="400"')
    return (f'<text x="{x}" y="{y}" {font} font-size="{size}" {fill(colour)} '
            f'text-anchor="{anchor}">{escape(body)}</text>')


def wrap(label, width=11, lines=3):
    out, line = [], ""
    for word in label.split():
        nxt = word if line == "" else f"{line} {word}"
        if len(nxt) <= width or line == "":
            line = nxt
        else:
            out.append(line)
            line = word
    if line:
        out.append(line)
    if len(out) > lines:
        out = out[:lines]
        out[-1] = out[-1][:width - 1] + "…"
    return [l if len(l) <= width else l[:width - 1] + "…" for l in out]


def caption(label):
    """A label as a key prints it: capitals, without what is in brackets."""
    return re.sub(r"\s*\([^)]*\)", "", label).upper()


def block(lines, mid, size, step, colour):
    top = mid - ((len(lines) - 1) * step) / 2 + size * 0.35
    return "".join(text(72, top + i * step, size, colour, l) for i, l in enumerate(lines))


def ground():
    return f'<rect width="{SIZE}" height="{SIZE}" fill="{BG}"/>'


def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" '
            f'viewBox="0 0 {SIZE} {SIZE}">{body}</svg>')


# --- keys ---------------------------------------------------------------------------
def command_body(label, symbol=None, filled=False):
    """The plugin's commandKey: pictogram large, label below (or the label alone)."""
    words = caption(label)
    if symbol is None:
        return block(wrap(words, 11, 3), 72, 15, 21, INK)
    lines = wrap(words, 15, 2)
    return (glyph(symbol, filled, 40, 14 if len(lines) > 1 else 20, 64, INK)
            + block(lines, 112 if len(lines) > 1 else 116, 12, 15, INK_DIM))


def command_key(label, symbol=None, filled=False):
    return svg(ground() + command_body(label, symbol, filled))


def hotkey_key(label, symbol, key, filled=False, tag=None):
    """A native Hotkey: the plugin's command face, plus the keyboard key it types (top
    right) and, for an action the game wants held, its tag (top left). Both sit above the
    pictogram's top edge (y = 14)."""
    corner = text(134, 12, 10, INK_DIM, key, anchor="end")
    if tag:
        corner += text(10, 12, 10, INK_DIM, tag, anchor="start")
    return svg(ground() + command_body(label, symbol, filled) + corner)


def value_key(label, symbol=None, filled=False):
    """The plugin's valueKey with no value yet: what its keys show before the game speaks."""
    head = (glyph(symbol, filled, 14, 14, 22, INK_DIM)
            + text(42, 31, 12, INK_DIM, (wrap(caption(label), 12, 1) or [""])[0], anchor="start")
            if symbol else text(72, 30, 12, INK_DIM, (wrap(caption(label), 16, 1) or [""])[0]))
    return svg(ground() + head + text(72, 96, 52, INK_DIM, "—", num=True))


CHEVRONS = "".join(f"M{x} 92L{x + 5} 97L{x} 102" for x in (60, 70, 80))


def _nav_mark():
    return f'<path d="{CHEVRONS}" fill="none" stroke="{MINT}" stroke-width="2"/>'


def nav_body(symbol, label=None, folder=False, filled=False, picture=None):
    """The plugin's navKey (pictogram, and for a folder the mint >>> of the game's panel
    titles), plus the folder's name drawn below (this profile draws its own titles)."""
    pic = picture if picture is not None else glyph(symbol, filled, 44, 18, 56, INK)
    name = text(72, 126, 13, INK, caption(label)) if label else ""
    return pic + (_nav_mark() if folder else "") + name


def nav_key(symbol, label=None, folder=False, filled=False):
    return svg(ground() + nav_body(symbol, label, folder, filled))


# --- animations (ink only, see module docstring) ---------------------------------
FRAMES = 24
FRAME_MS = 70


def _ring(cx, cy, r, colour, width=2):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" {fill(colour, "stroke")} stroke-width="{width}"/>'


def _alpha(colour, a):
    """INK at opacity `a` (0..1) as #rrggbbaa."""
    return f"{colour[:7]}{max(0, min(255, round(a * 255))):02x}"


def anim_pulse(symbol, label, t):
    """Combat: a ring leaves the pictogram and fades."""
    r = 30 + 12 * t                 # stays inside the key: its top at y = 4
    ring = _ring(72, 46, r, _alpha(INK, 0.5 * (1 - t)))
    return svg(ground() + ring + nav_body(symbol, label, folder=True))


def anim_radar(symbol, label, t):
    """Ciblage: a sweep turns around the pictogram, its trail fading behind it."""
    cx, cy, r = 72, 46, 34
    out = _ring(cx, cy, r, INK_TRACK)
    for i in range(8):
        a = 2 * math.pi * (t - i * 0.025) - math.pi / 2
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        out += (f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" '
                f'{fill(_alpha(INK, 0.5 * (1 - i / 8)), "stroke")} stroke-width="2"/>')
    pic = glyph(symbol, False, 58, 32, 28, INK)
    return svg(ground() + out + nav_body(symbol, label, folder=True, picture=pic))


def anim_thrust(symbol, label, t):
    """Vol: exhaust streaks run down from the pictogram."""
    out = ""
    for x, phase in ((60, 0.0), (72, 0.33), (84, 0.66)):
        p = (t + phase) % 1
        y = 70 + 14 * p
        out += (f'<line x1="{x}" y1="{y:.1f}" x2="{x}" y2="{y + 6:.1f}" '
                f'{fill(_alpha(INK, 0.6 * (1 - p)), "stroke")} stroke-width="2"/>')
    pic = glyph(symbol, False, 46, 14, 52, INK)
    return svg(ground() + out + nav_body(symbol, label, folder=True, picture=pic))


def anim_turbine(symbol, label, t):
    """Vaisseau: a turbine turns, the pictogram at its hub."""
    cx, cy, r = 72, 46, 32
    out = _ring(cx, cy, r, INK_TRACK)
    for i in range(6):
        a = 2 * math.pi * (t / 3 + i / 6)
        x1, y1 = cx + 20 * math.cos(a), cy + 20 * math.sin(a)
        x2, y2 = cx + (r - 3) * math.cos(a + 0.35), cy + (r - 3) * math.sin(a + 0.35)
        out += (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                f'{fill(INK_DIM, "stroke")} stroke-width="2"/>')
    pic = glyph(symbol, False, 60, 34, 24, INK)
    return svg(ground() + out + nav_body(symbol, label, folder=True, picture=pic))


def anim_scan(symbol, label, t):
    """Tablette: a scanline sweeps the pictogram, top to bottom."""
    y = 16 + 60 * t
    line = (f'<rect x="36" y="{y:.1f}" width="72" height="2" {fill(INK_DIM)}/>'
            f'<rect x="36" y="{y - 8:.1f}" width="72" height="8" {fill(_alpha(INK, 0.06))}/>')
    return svg(ground() + nav_body(symbol, label, folder=True) + line)


def anim_flares(symbol, label, key, t):
    """Leurres (a native key): sparks fall from both sides of the pictogram and fade."""
    out = ""
    for x, dx, phase in ((48, -10, 0.0), (96, 10, 0.5), (60, -6, 0.25), (84, 6, 0.75)):
        p = (t + phase) % 1
        out += (f'<circle cx="{x + dx * p:.1f}" cy="{64 + 24 * p:.1f}" r="{2.5 - 1.2 * p:.1f}" '
                f'{fill(_alpha(INK, 0.8 * (1 - p)))}/>')
    face = hotkey_key(label, symbol, key)
    return face.replace("</svg>", out + "</svg>")


ANIMS = {"pulse": anim_pulse, "radar": anim_radar, "thrust": anim_thrust,
         "turbine": anim_turbine, "scan": anim_scan}


# --- rasterising ---------------------------------------------------------------
def png_bytes(svg_text, size=288):
    return bytes(resvg_py.svg_to_bytes(svg_string=svg_text, width=size, height=size,
                                       font_dirs=[FONTS], skip_system_fonts=True))


def to_image(svg_text, size=288):
    return Image.open(io.BytesIO(png_bytes(svg_text, size))).convert("RGB")


def save_png(svg_text, path, size=288):
    to_image(svg_text, size).save(path, optimize=True)


def save_gif(frames_svg, path, size=144):
    """An animated key as Stream Deck plays it from a profile: 144 px, looping."""
    frames = [to_image(f, size) for f in frames_svg]
    pal = frames[0].quantize(colors=64, method=Image.Quantize.MEDIANCUT)
    q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
    q[0].save(path, save_all=True, append_images=q[1:], duration=FRAME_MS, loop=0,
              optimize=False, disposal=1)
