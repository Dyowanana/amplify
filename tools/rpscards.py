#!/usr/bin/env python3
"""P022-type rock paper scissors carousel renderer: two cut-out hands meeting from the left and right edges on a flat
textured card, a challenge cover and one round per slide (the losing gesture on the left with its line above it, the
gesture that beats it on the right with its line under it). Text, background, grid, mark and cursor are drawn in code.

Usage:
  rpscards.py <spec.json> [--out DIR]

Spec (paths are relative to the spec file):
  {"canvas": [1080, 1350],
   "theme": {"bg": "#0E1A24", "ink": "#FFFFFF", "accent": "#FF7A00", "muted": "#A3AEB4", "grid": 0.035, "grain": 5},
   "mark": {"logo": "raw/brand/logo.png", "handle": "withamplify.ai"},     # top-left mark, "NN / NN" counter top-right
   "art_scale": 0.3,                           # hand art px -> canvas px (one scale for every hand so sizes stay true)
   "cuff_min": 6,                              # % of the width the hoodie cuff stays inside the frame (moves a long hand in)
   "gap": 9,                                   # % of the width between the two fingertips
   "hands": {"rock": {"left": "raw/hands/left_rock.png", "right": {"path": "…", "flip": true, "zoom": 1.2}}, "paper": {…}, "scissors": {…}},
   "slides": [{"role": "hook", "left": "rock", "right": "scissors", "hands_y": 70,
               "lines": ["rock, paper,", "scissors, shoot"], "edition": "startup founder edition", "play": "swipe to play"},
              {"role": "round", "left": "rock", "right": "paper", "hands_y": 52,
               "lose": "shipping another feature", "win": "marketing the product you already built"}]}

Hands: generated on flat chroma green, the forearm cut by the frame edge it enters from. The green is keyed (soft edge,
green spill pulled down to max(r, b), specks dropped, holes filled) and the art is placed so its fingertip lands at
50 -/+ gap/2 % and the hand's centre at hands_y %; the arm runs off the canvas edge. "flip" mirrors an image that came out
facing the wrong way. Rounds must follow the game (the right gesture beats the left one); the tool stops otherwise.
Type: headline Barlow Condensed SemiBold (thickened), the edition line in the accent colour and sheared like an italic,
labels Inter ExtraBold, mark Inter Bold letter-spaced. Lowercase, no dashes, colons or semicolons (checked).
Writes DIR/slideN.png and DIR/records/slideN.json (visual data model, boxes from the drawn pixels).
"""
import argparse
import json
from itertools import combinations
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

import portable
from cards import Card, S, hex_rgb

FONTS = Path(__file__).resolve().parent.parent / "assets" / "fonts"
THEME = {"bg": "#0E1A24", "ink": "#FFFFFF", "accent": "#FF7A00", "muted": "#A3AEB4", "grid": 0.035, "grain": 5}
BEATS = {"paper": "rock", "scissors": "paper", "rock": "scissors"}


def check_text(s):
    bad = [c for c in "—–;:" if c in s]
    if bad:
        raise SystemExit(f"banned punctuation {bad} in: {s!r}")
    if s != s.lower():
        raise SystemExit(f"text must be lowercase: {s!r}")


def font_cap(path, cap_px, weight=None):
    """A font sized so a capital H is cap_px tall."""
    size = cap_px / 0.7
    for _ in range(3):
        f = portable.weighted(path, int(round(size)), weight) if weight else ImageFont.truetype(str(path), int(round(size)))
        b = f.getbbox("H")
        size *= cap_px / max(b[3] - b[1], 1)
    return portable.weighted(path, int(round(size)), weight) if weight else ImageFont.truetype(str(path), int(round(size)))


# ---------------------------------------------------------------- hands
def key_hand(path, flip=False):
    """RGBA cut-out of a hand on chroma green, cropped to the hand (the cut forearm stays on its image edge)."""
    im = cv2.cvtColor(cv2.imread(str(path)), cv2.COLOR_BGR2RGB).astype(np.float32)
    if flip:
        im = im[:, ::-1].copy()
    r, g, b = im[..., 0], im[..., 1], im[..., 2]
    d = g - np.maximum(r, b)
    alpha = np.clip(1 - (d - 10) / 30, 0, 1)
    core = (alpha > 0.5).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(core, 8)
    keep = np.zeros_like(core)
    if n > 1:
        big = stats[1:, cv2.CC_STAT_AREA].max()
        for i in range(1, n):
            if stats[i, cv2.CC_STAT_AREA] >= 0.01 * big:
                keep[lab == i] = 1
    n, lab = cv2.connectedComponents((1 - keep).astype(np.uint8), connectivity=4)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    holes = (lab > 0) & ~np.isin(lab, list(border)) & (d < 25)
    keep[holes] = 1
    alpha = np.where(holes, 1, alpha) * cv2.dilate(keep, np.ones((5, 5), np.uint8))
    alpha = cv2.GaussianBlur(alpha.astype(np.float32), (0, 0), 1.0)
    alpha = np.clip((alpha - 0.2) / 0.7, 0, 1)
    g2 = np.minimum(g, np.maximum(r, b) + 4)  # pull the green spill out of edges and hair
    rgb = np.dstack([r, g2, b])
    ys, xs = np.where(alpha > 0.05)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    out = np.dstack([rgb, alpha * 255])[y0:y1, x0:x1]
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")


def hand_center_y(a, side):
    """Vertical centre of the hand itself: the 35% of the cut-out nearest the fingertip."""
    al = np.asarray(a)[..., 3] > 128
    w = al.shape[1]
    cols = al[:, int(w * 0.65):] if side == "left" else al[:, : int(w * 0.35)]
    ys = np.where(cols.any(axis=1))[0]
    return (ys.min() + ys.max()) / 2, ys.min(), ys.max()


def cuff_x(a, side):
    """Inner edge of the hoodie cuff (and any band at the wrist) in the cut-out, in its own px: the sleeve is the
    low-colour part (charcoal or light grey), skin always carries some colour."""
    px = np.asarray(a).astype(np.int16)
    rgb, al = px[..., :3], px[..., 3]
    sleeve = (al > 128) & (rgb.max(axis=2) - rgb.min(axis=2) < 24)
    xs = np.where(sleeve)[1]
    if len(xs) < 50:
        return 0 if side == "left" else a.width
    return np.percentile(xs, 98) if side == "left" else np.percentile(xs, 2)


def place_hand(card, base, art, side, scale, gap, hands_y, cuff_min):
    W, H = card.W * S, card.H * S
    a = art.resize((int(art.width * scale * S), int(art.height * scale * S)), Image.LANCZOS)
    cy, top, bot = hand_center_y(a, side)
    tip_x = (50 - gap / 2 if side == "left" else 50 + gap / 2) / 100 * W
    # keep the hoodie cuff in frame: at least cuff_min % of the width between the frame edge and the cuff
    c = cuff_x(a, side)
    if side == "left":
        need = cuff_min / 100 * W + (a.width - c)
        if need > tip_x:
            print(f"  note: left hand moved in by {(need - tip_x) / W * 100:.1f}% to keep the cuff in frame")
            tip_x = need
    else:
        need = W - cuff_min / 100 * W - c
        if need < tip_x:
            print(f"  note: right hand moved in by {(tip_x - need) / W * 100:.1f}% to keep the cuff in frame")
            tip_x = need
    x = int(round(tip_x - a.width)) if side == "left" else int(round(tip_x))
    y = int(round(hands_y / 100 * H - cy))
    if (side == "left" and x > 0) or (side == "right" and x + a.width < W):
        print(f"  warning: the {side} forearm ends inside the frame; raise art_scale")
    # soft contact shadow, then the hand
    sh = Image.new("L", a.size, 0)
    sh.paste(a.getchannel("A").point(lambda v: int(v * 0.35)))
    sh = sh.filter(ImageFilter.GaussianBlur(14 * S))
    base.paste(Image.new("RGB", a.size, (0, 0, 0)), (x, y + 10 * S), sh)
    base.paste(a, (x, y), a)
    box = card.to_pct((max(x, 0), y + top, min(x + a.width, W), y + bot))
    return box, (max(x, 0), y + top, min(x + a.width, W), y + bot)


# ---------------------------------------------------------------- background and marks
def background(card, t, seed):
    W, H = card.W * S, card.H * S
    rng = np.random.default_rng(seed)
    base = np.array(hex_rgb(t["bg"]), np.float32)
    n1 = cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 0.8 * S)
    n2 = cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 3.0 * S)
    tex = (n1 / n1.std() * 0.6 + n2 / n2.std() * 0.4) * t["grain"]
    img = base[None, None, :] + tex[..., None]
    step = W / 9
    lines = np.zeros((H, W), np.float32)
    for i in range(1, 9):
        lines[:, int(i * step): int(i * step) + S] = 1
    for j in range(1, int(H / step) + 1):
        lines[int(j * step): int(j * step) + S, :] = 1
    img = img * (1 - lines[..., None] * t["grid"]) + 255 * lines[..., None] * t["grid"]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))


def logo_cutout(path, h_px):
    im = np.asarray(Image.open(path).convert("RGB")).astype(np.float32)
    bg = np.median(np.concatenate([im[:8].reshape(-1, 3), im[-8:].reshape(-1, 3)]), axis=0)
    dist = np.abs(im - bg).max(axis=2)
    a = np.clip((dist - 12) / 40, 0, 1)
    ys, xs = np.where(a > 0.1)
    rgba = np.dstack([im, a * 255])[ys.min(): ys.max() + 1, xs.min(): xs.max() + 1]
    lg = Image.fromarray(rgba.astype(np.uint8), "RGBA")
    return lg.resize((int(lg.width * h_px / lg.height), int(h_px)), Image.LANCZOS)


def spaced(d, xy, s, f, fill, track):
    x, y = xy
    x0 = x
    for ch in s:
        d.text((x, y), ch, font=f, fill=fill, anchor="ls")
        x += f.getlength(ch) + track
    return (x0, y - f.getbbox("H")[3] + f.getbbox("H")[1], x - track, y)


def marks(card, base, spec, n, total):
    d = ImageDraw.Draw(base)
    m = spec.get("mark", {})
    ink, muted = card.t["ink"], card.t["muted"]
    f = font_cap(FONTS / "Inter-VF.ttf", card.hpx(1.15) * S, 700)
    x, y = card.wpx(5.2) * S, card.hpx(5.6) * S
    if m.get("logo"):
        lg = logo_cutout(card.dir / m["logo"], card.hpx(2.6) * S)
        base.paste(lg, (int(x), int(y - lg.height * 0.82)), lg)
        lx = x
        x += lg.width + card.wpx(1.6) * S
        card.note_layer("mark", card.to_pct((lx, y - lg.height * 0.82, lx + lg.width, y + lg.height * 0.18)), "the brand's chevron mark (real logo file), top-left")
    if m.get("handle"):
        bb = spaced(d, (x, y), m["handle"], f, hex_rgb(ink), 0.16 * f.size)
        card.note_text(m["handle"], bb, "watermark", "corner-mark", "left", "Inter Bold, tracked", 1.15, "lowercase", ink, "negative-space", origin="mark")
    cnt = f"{n:02d} / {total:02d}"
    fx = font_cap(FONTS / "Inter-VF.ttf", card.hpx(1.15) * S, 500)
    wdt = sum(fx.getlength(c) + 0.1 * fx.size for c in cnt) - 0.1 * fx.size
    bb = spaced(d, (card.wpx(94.8) * S - wdt, y), cnt, fx, hex_rgb(muted), 0.1 * fx.size)
    card.note_text(cnt, bb, "counter", "corner-mark", "right", "Inter Medium", 1.15, "digits", muted, "negative-space", origin="mark")


def wrap(text, f, max_px):
    """Fewest lines that fit max_px, with the breaks chosen so the lines are as even as possible (no lone last word)."""
    out = []
    for para in text.split("\n"):
        words, best = para.split(), None
        for n in range(1, len(words) + 1):
            for cuts in combinations(range(1, len(words)), n - 1):
                idx = (0,) + cuts + (len(words),)
                lines = [" ".join(words[idx[i]:idx[i + 1]]) for i in range(n)]
                widest = max(f.getlength(ln) for ln in lines)
                if widest <= max_px and (best is None or widest < best[0]):
                    best = (widest, lines)
            if best:
                break
        out += best[1] if best else [para]
    return out


def label(card, d, text, f, fill, anchor_x, align, y, grow, pitch):
    """Draw wrapped lines; grow 'up' puts the last line's baseline at y, 'down' puts the first cap top at y."""
    lines = wrap(text, f, card.wpx(44) * S)
    cap = f.getbbox("H")[3] - f.getbbox("H")[1]
    base0 = y - (len(lines) - 1) * pitch if grow == "up" else y + cap
    boxes = []
    for i, ln in enumerate(lines):
        by = base0 + i * pitch
        anc = {"center": "ms", "right": "rs", "left": "ls"}[align]
        d.text((anchor_x, by), ln, font=f, fill=hex_rgb(fill), anchor=anc)
        boxes.append(d.textbbox((anchor_x, by), ln, font=f, anchor=anc))
    return (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))


def cursor(d, x, y, h, fill, outline):
    """Classic pointer arrow, tip at (x, y)."""
    u = h / 16
    pts = [(0, 0), (0, 13), (3.4, 10), (5.8, 15.4), (8, 14.4), (5.7, 9.2), (10, 9.2)]
    d.polygon([(x + px * u, y + py * u) for px, py in pts], fill=fill, outline=outline, width=max(int(u * 1.1), 1))


# ---------------------------------------------------------------- slides
def render(card, spec, s, n, total, hands):
    t = card.t
    base = background(card, t, seed=n)
    marks(card, base, spec, n, total)
    scale, gap, cm = spec.get("art_scale", 0.3), spec.get("gap", 9), spec.get("cuff_min", 6)
    lbox, lpx = place_hand(card, base, hands[(s["left"], "left")], "left", scale, gap, s["hands_y"], cm)
    rbox, rpx = place_hand(card, base, hands[(s["right"], "right")], "right", scale, gap, s["hands_y"], cm)
    card.note_layer("hand cut-out (left)", lbox, f"{s['left']} from the left edge, {spec.get('players', {}).get('left', 'player 1')}")
    card.note_layer("hand cut-out (right)", rbox, f"{s['right']} from the right edge, {spec.get('players', {}).get('right', 'player 2')}")
    d = ImageDraw.Draw(base)
    W = card.W * S
    if s.get("role") == "hook":
        f = font_cap(FONTS / "BarlowCondensed-SemiBold.ttf", card.hpx(s.get("cap", 7.6)) * S)
        pitch = card.hpx(s.get("cap", 7.6) * 1.32) * S
        y = card.hpx(s.get("head_y", 15)) * S + (f.getbbox("H")[3] - f.getbbox("H")[1])
        boxes = []
        for ln in s["lines"]:
            check_text(ln)
            d.text((W / 2, y), ln, font=f, fill=hex_rgb(t["ink"]), anchor="ms", stroke_width=int(0.014 * f.size), stroke_fill=hex_rgb(t["ink"]))
            boxes.append(d.textbbox((W / 2, y), ln, font=f, anchor="ms", stroke_width=int(0.014 * f.size)))
            y += pitch
        last = boxes[-1]
        # text caret right after the last word (cap height, sitting on the baseline), and a pointer resting on that word
        sw = int(0.014 * f.size)
        base_y = y - pitch
        cap = f.getbbox("H")[3] - f.getbbox("H")[1]
        ln = s["lines"][-1]
        word = ln.split()[-1]
        line_x0 = W / 2 - f.getlength(ln) / 2
        wx0 = line_x0 + f.getlength(ln[: len(ln) - len(word)])
        wx1 = line_x0 + f.getlength(ln) + sw
        cx0 = wx1 + card.wpx(1.0) * S
        caret = (cx0, base_y - cap * 1.02, cx0 + card.wpx(0.8) * S, base_y + cap * 0.06)
        d.rectangle(caret, fill=hex_rgb(t["accent"]))
        card.note_layer("ui motif", card.to_pct(caret), "text caret after the headline, as if it is being typed (coder take on the source's edit-menu motif)")
        tip = (wx0 + (wx1 - wx0) * 0.62, base_y - cap * 0.4)
        cursor(d, tip[0], tip[1], card.hpx(6.4) * S, t.get("pointer", "#39BEF8"), hex_rgb(t["bg"]))
        card.note_layer("ui motif", card.to_pct((tip[0], tip[1], tip[0] + card.hpx(4.0) * S, tip[1] + card.hpx(6.4) * S)), "pointer resting on the last word")
        hb = (min(b[0] for b in boxes), boxes[0][1], max(b[2] for b in boxes), last[3])
        card.note_text("\n".join(s["lines"]), hb, "hook", "top-headline", "center", "Barlow Condensed SemiBold, thickened", s.get("cap", 7.6), "lowercase", t["ink"], "negative-space")
        if s.get("edition"):
            check_text(s["edition"])
            fe = font_cap(FONTS / "BarlowCondensed-SemiBold.ttf", card.hpx(3.6) * S)
            layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
            ld = ImageDraw.Draw(layer)
            ey = y - pitch + card.hpx(7.2) * S
            ld.text((W / 2, ey), s["edition"], font=fe, fill=hex_rgb(t["accent"]) + (255,), anchor="ms", stroke_width=int(0.012 * fe.size), stroke_fill=hex_rgb(t["accent"]) + (255,))
            eb = ld.textbbox((W / 2, ey), s["edition"], font=fe, anchor="ms")
            k = 0.2  # italic shear around the baseline
            layer = layer.transform(layer.size, Image.AFFINE, (1, k, -k * ey, 0, 1, 0), Image.BICUBIC)
            base.paste(layer, (0, 0), layer)
            card.note_text(s["edition"], (eb[0] - k * (ey - eb[1]), eb[1], eb[2], eb[3]), "subheading", "center-line", "center", "Barlow Condensed SemiBold, sheared italic", 3.6, "lowercase", t["accent"], "negative-space")
            y = ey + card.hpx(5.4) * S
        if s.get("play"):
            check_text(s["play"])
            fp = font_cap(FONTS / "Inter-VF.ttf", card.hpx(2.2) * S, 300)
            tw = fp.getlength(s["play"])
            aw = card.wpx(24) * S
            x0 = W / 2 - (tw + card.wpx(2.5) * S + aw) / 2
            py = card.hpx(s.get("play_y", 50)) * S
            d.text((x0, py), s["play"], font=fp, fill=hex_rgb(t["ink"]), anchor="ls")
            pb = d.textbbox((x0, py), s["play"], font=fp, anchor="ls")
            ay = py - (fp.getbbox("H")[3] - fp.getbbox("H")[1]) / 2
            ax0, ax1 = pb[2] + card.wpx(2.5) * S, pb[2] + card.wpx(2.5) * S + aw
            d.line((ax0, ay, ax1, ay), fill=hex_rgb(t["ink"]), width=int(1.6 * S))
            d.line((ax1 - 10 * S, ay - 7 * S, ax1, ay, ax1 - 10 * S, ay + 7 * S), fill=hex_rgb(t["ink"]), width=int(1.6 * S), joint="curve")
            card.note_text(s["play"], (pb[0], pb[1], ax1, pb[3]), "cta", "label + arrow", "left", "Inter Light", 2.2, "lowercase", t["ink"], "negative-space")
    else:
        if BEATS[s["right"]] != s["left"]:
            raise SystemExit(f"slide {n}: {s['right']} does not beat {s['left']}; the right hand must win")
        check_text(s["lose"]), check_text(s["win"])
        cap = s.get("label_cap", 2.6)
        f = font_cap(FONTS / "Inter-VF.ttf", card.hpx(cap) * S, 800)
        pitch = card.hpx(cap * 1.55) * S
        lose_x = (lpx[0] + lpx[2]) / 2 if lpx[2] - lpx[0] < W * 0.5 else W * 0.25
        lose_x = max(lose_x, card.wpx(5.2) * S + card.wpx(22) * S)
        lb = label(card, d, s["lose"], f, t["ink"], lose_x, "center", lpx[1] - card.hpx(3.2) * S, "up", pitch)
        card.note_text(s["lose"], lb, "myth", "label above the left hand", "center", "Inter ExtraBold", cap, "lowercase", t["ink"], "negative-space")
        rb = label(card, d, s["win"], f, t["accent"], card.wpx(94.8) * S, "right", rpx[3] + card.hpx(3.4) * S, "down", pitch)
        card.note_text(s["win"], rb, "truth", "label below the right hand", "right", "Inter ExtraBold", cap, "lowercase", t["accent"], "negative-space")
    card.img = base
    card.d = ImageDraw.Draw(base)
    return [lbox[0], min(lbox[1], rbox[1]), 100, max(lbox[1] + lbox[3], rbox[1] + rbox[3]) - min(lbox[1], rbox[1])]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    out = args.out or args.spec.parent / "output"
    (out / "records").mkdir(parents=True, exist_ok=True)
    hands = {}
    for g, sides in spec["hands"].items():
        for side, v in sides.items():
            v = {"path": v} if isinstance(v, str) else v
            art = key_hand(args.spec.parent / v["path"], v.get("flip", False))
            z = v.get("zoom", 1.0)  # evens out hand size when a generation framed the hand closer or wider
            hands[(g, side)] = art.resize((int(art.width * z), int(art.height * z)), Image.LANCZOS) if z != 1.0 else art
    total = len(spec["slides"])
    for i, s in enumerate(spec["slides"], 1):
        card = Card(args.spec.parent, spec.get("canvas", [1080, 1350]), {**THEME, **spec.get("theme", {})})
        subject = render(card, spec, s, i, total, hands)
        card.finish(out / f"slide{i}.png")
        rec = {"n": i, "role": s.get("role", "round"), "class": "other:hand-gesture-duel-card", "confidence": "high",
               "frame": {"canvas": f"4:5 portrait, {card.W}x{card.H}",
                         "layers": [{"type": "background", "box": [0, 0, 100, 100], "note": f"flat {card.t['bg']} with a fine felt grain and a faint 9-column grid"}] + card.layers,
                         "composition": {"subject_box": [round(v, 1) for v in subject]}},
               "text_blocks": card.texts}
        (out / "records" / f"slide{i}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"slide{i}.png  ({len(card.texts)} text blocks)")


if __name__ == "__main__":
    main()
