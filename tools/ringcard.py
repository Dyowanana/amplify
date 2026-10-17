#!/usr/bin/env python3
"""P023-type habit ring card: one flat pale card, a glowing centre figure, a thin 2-line question and a ring of labelled
items. Text, pictograms and the app tile are drawn in code; generated art is cut out (from white, from chroma green, or as
a glow) and given a deliberately mixed finish so the ring reads as a collected collage, not one AI render style.

Usage:
  ringcard.py <spec.json> [--out DIR]

Spec (paths are relative to the spec file; boxes are % of the frame [x, y, w, h] from the top-left):
  {"canvas": [1080, 1350], "bg": "#ebf1ea", "ink": "#111111", "name": "board",
   "title": {"lines": ["why does today", "feel x?"], "y": 63,   # or "gap_below_centre": -3 (% under the figure's box)
 "size": 5.8, "weight": 300, "handle": "@account"},
   "label_size": 3.1, "label_weight": 300,
   "centre": {"art": "raw/art/figure.png", "box": [...], "cut": "glow", "crop_bottom": 0.85},
   "items": [
     {"art": "raw/art/x.png", "box": [...], "cut": "white|green", "finish": "stock|film|flash|none", "label": "two\nlines",
      "label_y": optional top of the label in % (lines a row up), "align": "center|bottom"},
     {"logo": "raw/brand/logo.png", "box": [...], "label": "…"},             # a real app icon, rounded like a home-screen tile
     {"picto": "battery|bell_off|terminal|check|bed", "box": [...], "label": "…"}, # flat black icon-font style glyphs
   ],
   "versions": [{"name": "slide2", "bg": "#ffffff"}, …]}   # optional: same board, another card colour per version
Writes DIR/<name>.png and DIR/records/<name>.json (visual data model, boxes measured from the drawn pixels).
"""
import argparse
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

import portable

FONTS = Path(__file__).resolve().parent.parent / "assets" / "fonts"
SANS = portable.font("/System/Library/Fonts/HelveticaNeue.ttc", "Inter-VF.ttf")
MONO = FONTS / "DejaVuSansMono.ttf"
SANS_NAME = "Helvetica Neue Light look (Inter 300, tight tracking)"
S = 2  # supersampling
BANNED = "—–:;"


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


class Ring:
    def __init__(self, spec_dir, spec):
        self.dir = spec_dir
        self.W, self.H = spec.get("canvas", [1080, 1350])
        self.bg, self.ink = spec.get("bg", "#ebf1ea"), spec.get("ink", "#111111")
        self.img = Image.new("RGBA", (self.W * S, self.H * S), hex_rgb(self.bg) + (255,))
        self.d = ImageDraw.Draw(self.img)
        self.layers, self.texts = [], []
        self.rng = np.random.default_rng(7)

    def px(self, b):
        return (b[0] * self.W / 100 * S, b[1] * self.H / 100 * S, (b[0] + b[2]) * self.W / 100 * S, (b[1] + b[3]) * self.H / 100 * S)

    def pct(self, bb):
        return [round(bb[0] / S / self.W * 100, 1), round(bb[1] / S / self.H * 100, 1),
                round((bb[2] - bb[0]) / S / self.W * 100, 1), round((bb[3] - bb[1]) / S / self.H * 100, 1)]

    def font(self, size_pct, weight):
        return portable.weighted(SANS, int(round(size_pct / 100 * self.H * S)), weight)

    # ---- text: tight negative tracking like the source's light grotesk
    def tracked(self, cx, top, s, fnt, fill, track=-0.035):
        adv = [self.d.textlength(c, font=fnt) + track * fnt.size for c in s]
        w = sum(adv) - track * fnt.size
        x = cx - w / 2
        x0 = x
        for c, a in zip(s, adv):
            self.d.text((x, top), c, font=fnt, fill=hex_rgb(fill), anchor="la")
            x += a
        asc, desc = fnt.getmetrics()
        return (x0, top + asc * 0.28, x0 + w, top + asc + desc * 0.25)

    def lines(self, cx, top, lines, size, weight, fill, lead=1.0, track=-0.035):
        fnt = self.font(size, weight)
        bbs, y = [], top
        for ln in lines:
            bbs.append(self.tracked(cx, y, ln, fnt, fill, track))
            y += fnt.size * lead
        return (min(b[0] for b in bbs), min(b[1] for b in bbs), max(b[2] for b in bbs), max(b[3] for b in bbs))

    def note_text(self, text, bb, role, size, fill, weight_name="Light"):
        for ch in BANNED:
            if ch in text:
                raise SystemExit(f"banned punctuation {ch!r} in {text!r}")
        self.texts.append({"text": text, "origin": "overlay", "role": role, "pattern": "item-label" if role == "label" else "center-block",
                           "box": self.pct(bb), "align": "center", "font": f"{SANS_NAME} {weight_name}", "size_pct": size,
                           "case": "lowercase", "fill": fill, "stroke": "none", "under": "negative-space"})

    # ---- art
    def paste(self, rgba, box, align="center"):
        """Fit an RGBA array inside box (keep aspect) and alpha-composite it. Returns the placed pixel box."""
        bx0, by0, bx1, by1 = self.px(box)
        h, w = rgba.shape[:2]
        k = min((bx1 - bx0) / w, (by1 - by0) / h)
        nw, nh = max(int(w * k), 1), max(int(h * k), 1)
        im = Image.fromarray(rgba, "RGBA").resize((nw, nh), Image.LANCZOS)
        x = int(bx0 + (bx1 - bx0 - nw) / 2)
        y = int(by1 - nh) if align == "bottom" else int(by0 + (by1 - by0 - nh) / 2)
        self.img.alpha_composite(im, (x, y))
        return (x, y, x + nw, y + nh)


def crop_to_alpha(rgba, pad=4):
    ys, xs = np.where(rgba[..., 3] > 8)
    return rgba[max(ys.min() - pad, 0): ys.max() + pad + 1, max(xs.min() - pad, 0): xs.max() + pad + 1]


def cut_white(bgr):
    """Background = near-white pixels reachable from the border. Feathered 1 px, eroded 1 px against the white halo."""
    h, w = bgr.shape[:2]
    near = ((bgr.min(axis=2) > 236) & (bgr.max(axis=2).astype(int) - bgr.min(axis=2) < 14)).astype(np.uint8)
    n, lab = cv2.connectedComponents(near, connectivity=4)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bgmask = np.isin(lab, list(border))
    fg = (~bgmask).astype(np.uint8)
    fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(fg, 8)
    if n > 1:
        big = stats[1:, cv2.CC_STAT_AREA].max()
        fg = np.isin(lab, [i for i in range(1, n) if stats[i, cv2.CC_STAT_AREA] >= 0.01 * big]).astype(np.uint8)
    fg = cv2.erode(fg, np.ones((3, 3), np.uint8))
    a = cv2.GaussianBlur(fg.astype(np.float32), (3, 3), 0)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    return crop_to_alpha(np.dstack([rgb, (a * 255).astype(np.uint8)]))


def cut_green(bgr):
    """Chroma key in colour with spill suppression on the edge."""
    im = bgr.astype(np.int16)
    b, g, r = im[..., 0], im[..., 1], im[..., 2]
    green = (g - np.maximum(r, b) > 30) & (g > 80)
    fg = (~green).astype(np.uint8)
    fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(fg, 8)
    big = stats[1:, cv2.CC_STAT_AREA].max()
    fg = np.isin(lab, [i for i in range(1, n) if stats[i, cv2.CC_STAT_AREA] >= 0.004 * big]).astype(np.uint8)
    fg = cv2.erode(fg, np.ones((3, 3), np.uint8))
    a = cv2.GaussianBlur(fg.astype(np.float32), (5, 5), 0)
    g2 = np.minimum(g, np.maximum(r, b) + 8)  # despill
    rgb = np.dstack([r, g2, b]).clip(0, 255).astype(np.uint8)
    return crop_to_alpha(np.dstack([rgb, (a * 255).astype(np.uint8)]))


def cut_glow(bgr, gain=2.2):
    """A light figure on white: alpha from how far each pixel is from white, colour un-premultiplied, plus a soft white
    halo so the core still reads as light on a tinted card."""
    bgr = cv2.copyMakeBorder(bgr, 90, 90, 90, 90, cv2.BORDER_CONSTANT, value=(255, 255, 255))  # room for the halo to fade out
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB).astype(np.float32)
    dist = np.clip((255 - rgb.min(axis=2) - 10) / 245, 0, 1)  # the generator's white is not quite 255: no faint white box
    a = np.clip(dist * gain, 0, 1)
    col = 255 - (255 - rgb) / np.maximum(a[..., None], 1e-3)
    col = np.clip(col, 0, 255)
    # the white core is opaque light (it must glow on a coloured card too): fill the figure's silhouette, then a soft halo
    sil = (dist > 0.06).astype(np.uint8)
    sil = cv2.morphologyEx(sil, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    n, lab = cv2.connectedComponents(1 - sil, connectivity=4)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    sil = np.where((lab > 0) & ~np.isin(lab, list(border)), 1, sil).astype(np.float32)
    body = cv2.GaussianBlur(sil, (0, 0), 3)
    halo = cv2.GaussianBlur(sil, (0, 0), 18) * 0.6
    a2 = np.maximum(a, np.maximum(body * 0.92, halo))
    col = col * (a / np.maximum(a2, 1e-3))[..., None] + 255 * (1 - a / np.maximum(a2, 1e-3))[..., None]
    return crop_to_alpha(np.dstack([col.astype(np.uint8), (a2 * 255).astype(np.uint8)]), pad=0)


def finish(rgba, kind, rng):
    """Vary the finish per item so the ring looks collected from different sources."""
    if kind in (None, "none"):
        return rgba
    rgb, a = rgba[..., :3], rgba[..., 3]
    h, w = rgb.shape[:2]
    if kind == "stock":  # a resized web image: a touch soft, mild JPEG
        k, q, noise, sat = 0.55, 70, 2.0, 1.0
    elif kind == "flash":  # an old digital-camera meme photo
        k, q, noise, sat = 0.32, 38, 5.0, 1.08
    else:  # "film": an old movie still, DVD-frame soft, warm, grain
        k, q, noise, sat = 0.38, 42, 8.0, 0.82
    small = cv2.resize(rgb, (max(int(w * k), 1), max(int(h * k), 1)), interpolation=cv2.INTER_AREA)
    ok, enc = cv2.imencode(".jpg", cv2.cvtColor(small, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, q])
    small = cv2.cvtColor(cv2.imdecode(enc, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
    out = cv2.resize(small, (w, h), interpolation=cv2.INTER_CUBIC).astype(np.float32)
    grey = out.mean(axis=2, keepdims=True)
    out = grey + (out - grey) * sat
    if kind == "film":
        out = out * np.array([1.04, 1.0, 0.92]) + 4
        x = out / 255
        out = (x * x * (3 - 2 * x)) * 0.6 * 255 + out * 0.4
    out = out + rng.normal(0, noise, out.shape)
    return np.dstack([np.clip(out, 0, 255).astype(np.uint8), a])


def app_tile(path, side):
    im = Image.open(path).convert("RGBA").resize((side, side), Image.LANCZOS)
    m = Image.new("L", (side, side), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, side - 1, side - 1), radius=int(side * 0.225), fill=255)
    im.putalpha(m)
    edge = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    ImageDraw.Draw(edge).rounded_rectangle((0, 0, side - 1, side - 1), radius=int(side * 0.225), outline=(0, 0, 0, 34), width=max(side // 90, 2))
    im.alpha_composite(edge)
    return np.asarray(im)


# ---- pictograms (flat black, the look of an icon font; one red prohibition sign)
def picto(kind, side, ink=(17, 17, 17)):
    im = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    s = side
    K = ink + (255,)
    if kind == "battery":
        d.rounded_rectangle((s * .04, s * .26, s * .86, s * .74), radius=s * .09, fill=K)
        d.rounded_rectangle((s * .86, s * .40, s * .96, s * .60), radius=s * .03, fill=K)
        bolt = [(s * .50, s * .30), (s * .32, s * .53), (s * .45, s * .53), (s * .39, s * .70), (s * .60, s * .45), (s * .47, s * .45), (s * .55, s * .30)]
        d.polygon(bolt, fill=(255, 255, 255, 255))
    elif kind == "bell_off":
        cx = s * .5
        d.pieslice((cx - s * .26, s * .20, cx + s * .26, s * .62), 180, 360, fill=K)
        d.rectangle((cx - s * .26, s * .41, cx + s * .26, s * .62), fill=K)
        d.polygon([(cx - s * .26, s * .60), (cx + s * .26, s * .60), (cx + s * .34, s * .70), (cx - s * .34, s * .70)], fill=K)
        d.ellipse((cx - s * .07, s * .69, cx + s * .07, s * .80), fill=K)
        d.ellipse((cx - s * .045, s * .14, cx + s * .045, s * .23), fill=K)
        red, w = (226, 30, 36, 255), int(s * .085)
        d.ellipse((s * .05, s * .05, s * .95, s * .95), outline=red, width=w)
        c, r = s * .5, s * .45 - w / 2
        d.line((c - r * .707, c - r * .707, c + r * .707, c + r * .707), fill=red, width=w)
    elif kind == "terminal":
        w = int(s * .055)
        d.rounded_rectangle((s * .06, s * .06, s * .94, s * .94), radius=s * .12, outline=K, width=w, fill=(255, 255, 255, 255))
        f = portable.weighted(MONO, int(s * .36), 700)
        d.text((s * .5, s * .52), ">_", font=f, fill=K, anchor="mm")
    elif kind == "check":
        d.ellipse((s * .06, s * .06, s * .94, s * .94), fill=K)
        d.line([(s * .29, s * .52), (s * .44, s * .67), (s * .72, s * .37)], fill=(255, 255, 255, 255), width=int(s * .09), joint="curve")
    elif kind == "bed":  # side view: headboard on the left, mattress, pillow, two legs
        d.rounded_rectangle((s * .04, s * .22, s * .14, s * .80), radius=s * .03, fill=K)
        d.rounded_rectangle((s * .04, s * .52, s * .96, s * .70), radius=s * .03, fill=K)
        d.rounded_rectangle((s * .18, s * .38, s * .40, s * .50), radius=s * .05, fill=K)
        d.rounded_rectangle((s * .43, s * .40, s * .96, s * .52), radius=s * .04, fill=K)
        d.rectangle((s * .86, s * .70, s * .95, s * .80), fill=K)
    else:
        raise SystemExit(f"unknown pictogram {kind}")
    return np.asarray(im)


PICTO_NOTE = {"battery": "flat black battery with a white bolt", "bell_off": "black bell under a red prohibition sign",
              "terminal": "outlined tile with a >_ prompt, element-tile style", "check": "black circle with a white tick",
              "bed": "flat black bed, side view"}


def render(spec_dir, spec, out):
    rc = Ring(spec_dir, spec)
    lsize, lweight = spec.get("label_size", 3.1), spec.get("label_weight", 300)
    c = spec.get("centre")
    centre_bb = None
    if c:
        bgr = cv2.imread(str(spec_dir / c["art"]))
        if c.get("crop_bottom"):
            bgr = bgr[: int(bgr.shape[0] * c["crop_bottom"])]
        bb = centre_bb = rc.paste(cut_glow(bgr, c.get("gain", 2.2)), c["box"])
        rc.layers.append({"type": "centre-image", "box": rc.pct(bb), "note": c.get("note", "glowing figure")})
    for it in spec["items"]:
        x0, y0, x1, y1 = rc.px(it["box"])
        side = int(min(x1 - x0, y1 - y0))
        if "logo" in it:
            arr, typ, note = app_tile(spec_dir / it["logo"], side), "app-icon", "the brand's real app icon, rounded tile"
        elif "picto" in it:
            arr, typ, note = crop_to_alpha(picto(it["picto"], side), pad=0), "pictogram", "drawn in code: " + PICTO_NOTE[it["picto"]]
        else:
            bgr = cv2.imread(str(spec_dir / it["art"]))
            arr = cut_green(bgr) if it.get("cut") == "green" else cut_white(bgr)
            arr = finish(arr, it.get("finish", "stock"), rc.rng)
            typ = "meme-cutout" if it.get("cut") == "green" else "photo-cutout"
            note = it.get("note", Path(it["art"]).stem)
        bb = rc.paste(arr, it["box"], it.get("align", "center"))
        rc.layers.append({"type": typ, "box": rc.pct(bb), "note": note})
        if it.get("label"):
            ln = it["label"].split("\n")
            ltop = it["label_y"] / 100 * rc.H * S if "label_y" in it else bb[3] + it.get("label_gap", 0.6) / 100 * rc.H * S
            lb = rc.lines((bb[0] + bb[2]) / 2, ltop, ln, lsize, lweight, rc.ink, lead=0.98)
            rc.note_text(" ".join(ln), lb, "label", lsize, rc.ink)
    t = spec["title"]
    fnt_px = t.get("size", 5.8) / 100 * rc.H * S
    if "gap_below_centre" in t and centre_bb:  # the title sits right under the drawn figure (its halo may overlap)
        top = centre_bb[3] + t["gap_below_centre"] / 100 * rc.H * S
    else:
        top = t.get("y", 62) / 100 * rc.H * S
    tb = rc.lines(rc.W * S / 2, top, t["lines"], t.get("size", 5.8), t.get("weight", 300), rc.ink, lead=t.get("lead", 0.98), track=-0.045)
    rc.note_text("\n".join(t["lines"]), tb, "hook", t.get("size", 5.8), rc.ink)
    if t.get("handle"):
        hb = rc.lines(rc.W * S / 2, tb[3] + fnt_px * 0.1, [t["handle"]], 1.6, 400, "#9a9a9a", track=-0.01)
        rc.note_text(t["handle"], hb, "watermark", 1.6, "#9a9a9a", "Regular")
    name = spec.get("name", "board")
    final = rc.img.convert("RGB").resize((rc.W, rc.H), Image.LANCZOS)
    final.save(out / f"{name}.png")
    rec = {"n": 1, "role": "hook", "class": "other:habit-ring-card", "confidence": "high",
           "frame": {"canvas": f"4:5 portrait, {rc.W}x{rc.H}",
                     "layers": [{"type": "background", "box": [0, 0, 100, 100], "note": f"flat card {rc.bg}"}] + rc.layers},
           "text_blocks": rc.texts}
    (out / "records").mkdir(parents=True, exist_ok=True)
    (out / "records" / f"{name}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{name}.png  ({len(spec['items'])} ring items)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    out = args.out or args.spec.parent / "output"
    out.mkdir(parents=True, exist_ok=True)
    for v in spec.get("versions") or [{}]:  # a version changes only the card colour and the file name
        render(args.spec.parent, {**spec, **v}, out)


if __name__ == "__main__":
    main()
