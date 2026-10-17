#!/usr/bin/env python3
"""P020-type founder-notes carousel renderer: a flat card, a bold heading and monospace paragraphs drawn in code, and one
black and white cut-out person per slide with a white sticker outline (cards.py's Card for text and records).

Usage:
  memecards.py <spec.json> [--out DIR]

Spec (paths are relative to the spec file):
  {"canvas": [1080, 1350], "theme": {"bg": "#e4e3df", "ink": "#111111"},
   "slides": [{"role": "hook", "layout": "left|center",
               "heading": "…", "heading_y": 24,            # top of the heading in % of the frame height
               "body": ["line one\\nline two", "next paragraph"],   # paragraphs, \\n is a hard line break
               "body_gap": 6,                              # % between the heading top and the first body line top
               "cutout": {"art": "raw/art/s1.png", "box": [x, y, w, h], "halftone": true, "align": "left|center|right", "crop_bottom": 0.88, "crop_x": [0.2, 1],
                          "fit": "fill", "top_gap": 3, "max_cut": 0.35, "grade": "film", "note": "who is in it"},
               "arrow": true}]}                            # swipe arrow bottom right (cover)

Type (P020 §11): heading Inter Bold at 2.7% (Inter runs larger than the source's Roboto at 2.9%) of the frame height; body DejaVu Sans Mono (assets/fonts, stands in for
Space Mono) at 1.95% with a 2.3% line pitch and one empty line between paragraphs; left layout at x 12.8%, centre layout
centred on the frame. Text is lowercase by the owner's rule (brand names keep their capitals); no dashes, colons or semicolons.

Cut-outs: art is generated on a flat chroma green. The green is keyed out, holes are filled, the person turns grayscale
(levels stretched), optionally into a 45° halftone dot screen, and gets a white outline 1.3% of the frame width. The
cut-out is fitted inside its box (keeping its aspect) and sits on the box's bottom edge; a box that reaches the frame's
bottom or left edge crops it there, as in the source.
fit "fill" (the default since 2026-10-13, owner rule: no awkward empty space at the bottom): the cut-out covers its box,
anchored at the box top and centred on the person, and the frame edges crop the overflow (at most max_cut of the person's
height is cut at the bottom). With no "box", the box spans the full width from top_gap % under the last text line to the
bottom. "contain" keeps the old fit-inside behaviour.
grade "film": the classic movie-still finish (softened like an old DVD frame, a contrast S-curve, JPEG grit, heavy grain),
so generated people read as old film stills rather than clean AI renders.
Writes DIR/slideN.png and DIR/records/slideN.json (visual data model, boxes measured from the drawn pixels).
"""
import argparse
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import portable
from cards import Card, S, hex_rgb

FONTS = Path(__file__).resolve().parent.parent / "assets" / "fonts"
HEAD_PCT, BODY_PCT, PITCH_PCT, LEFT_X = 2.7, 1.95, 2.3, 12.8
THEME = {"bg": "#e4e3df", "ink": "#111111"}


def check_text(s):
    bad = [c for c in "—–;:" if c in s]
    if bad:
        raise SystemExit(f"banned punctuation {bad} in: {s!r}")


def key_person(path, crop_bottom=None, crop_x=None):
    """Cut the person out of a flat green background. Returns (gray uint8, mask float 0..1), cropped to the person.
    crop_bottom: keep only the top fraction of the art (drops a desk or floor that would end in a hard cut).
    crop_x: [left, right] fractions of the art width to keep (drops a wide prop so the person can be bigger; place the
    cut side against the frame edge)."""
    im = cv2.imread(str(path)).astype(np.int16)
    if crop_bottom:
        im = im[: int(im.shape[0] * crop_bottom)]
    if crop_x:
        im = im[:, int(im.shape[1] * crop_x[0]): int(im.shape[1] * crop_x[1])]
    b, g, r = im[..., 0], im[..., 1], im[..., 2]
    green = (g - np.maximum(r, b) > 28) & (g > 70)
    person = (~green).astype(np.uint8)
    person = cv2.morphologyEx(person, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(person, 8)
    keep = np.zeros_like(person)
    big = stats[1:, cv2.CC_STAT_AREA].max() if n > 1 else 0
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] >= 0.004 * big:
            keep[lab == i] = 1
    # fill holes: anything not reachable from the border through background is the person
    n, lab = cv2.connectedComponents((1 - keep).astype(np.uint8), connectivity=4)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    holes = (lab > 0) & ~np.isin(lab, list(border))
    keep = np.where(holes & ~green, 1, keep).astype(np.uint8)  # enclosed green (a gap under an arm) stays out
    ys, xs = np.where(keep > 0)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    gray = cv2.cvtColor(im.astype(np.uint8), cv2.COLOR_BGR2GRAY)[y0:y1, x0:x1]
    m = keep[y0:y1, x0:x1].astype(np.float32)
    m = cv2.GaussianBlur(m, (3, 3), 0)
    vals = gray[m > 0.5]
    lo, hi = np.percentile(vals, 1.5), np.percentile(vals, 98.5)
    gray = np.clip((gray.astype(np.float32) - lo) / max(hi - lo, 1) * 255, 0, 255).astype(np.uint8)
    return gray, m


def halftone(gray, cell):
    """45° amplitude-modulated dot screen: black dots on white, dot area follows the darkness."""
    h, w = gray.shape
    dark = 1 - cv2.blur(gray, (int(cell), int(cell))).astype(np.float32) / 255
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    c, s = np.cos(np.pi / 4), np.sin(np.pi / 4)
    u, v = xx * c + yy * s, -xx * s + yy * c
    du = (u / cell - np.round(u / cell)) * cell
    dv = (v / cell - np.round(v / cell)) * cell
    dist = np.sqrt(du ** 2 + dv ** 2)
    radius = np.sqrt(np.clip(dark, 0, 1)) * cell * 0.62
    ink = np.clip(radius - dist + 0.5, 0, 1)  # one pixel of anti-aliasing
    return (255 * (1 - ink)).astype(np.uint8)


def film(gray, rng):
    """Old movie-still finish: DVD-frame softness, an S-curve, JPEG grit and grain."""
    h, w = gray.shape
    small = cv2.resize(gray, (max(w * 2 // 5, 1), max(h * 2 // 5, 1)), interpolation=cv2.INTER_AREA)
    ok, enc = cv2.imencode(".jpg", small, [cv2.IMWRITE_JPEG_QUALITY, 45])
    small = cv2.imdecode(enc, cv2.IMREAD_GRAYSCALE)
    g = cv2.resize(small, (w, h), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
    g = g * g * (3 - 2 * g)  # smoothstep S-curve: crushed blacks, bright highlights
    g = g * 255 + rng.normal(0, 11, g.shape)
    return np.clip(g, 0, 255).astype(np.uint8)


def place_cutout(card, cut, slide_n, text_bottom):
    gray, m = key_person(card.dir / cut["art"], cut.get("crop_bottom"), cut.get("crop_x"))
    box = cut.get("box") or [0, text_bottom + cut.get("top_gap", 3), 100, 100 - text_bottom - cut.get("top_gap", 3)]
    bx, by, bw, bh = [card.wpx(box[0]) * S, card.hpx(box[1]) * S, card.wpx(box[2]) * S, card.hpx(box[3]) * S]
    h, w = gray.shape
    fill = cut.get("fit", "fill") == "fill"
    k = min(bw / w, bh / h)
    if fill:
        k = min(max(bw / w, bh / h), bh / (h * (1 - cut.get("max_cut", 0.35))))
    nw, nh = int(round(w * k)), int(round(h * k))
    gray = cv2.resize(gray, (nw, nh), interpolation=cv2.INTER_AREA if k < 1 else cv2.INTER_CUBIC)
    m = cv2.resize(m, (nw, nh), interpolation=cv2.INTER_LINEAR)
    rng = np.random.default_rng(slide_n)
    if cut.get("grade") == "film":
        gray = film(gray, rng)
    if cut.get("halftone"):
        # dots darken a print: lift the mid-tones first so faces stay readable (dark suits otherwise go solid)
        gray = (255 * (gray.astype(np.float32) / 255) ** cut.get("halftone_gamma", 0.6)).astype(np.uint8)
        gray = halftone(gray, cell=card.W * S * 0.0085)
    elif cut.get("grade") != "film":
        gray = np.clip(gray.astype(np.float32) + rng.normal(0, 7, gray.shape), 0, 255).astype(np.uint8)
    align = cut.get("align", "center" if fill else "left")
    if fill and align == "center":  # centre the person's mass, never leave a gap at a side the art could cover
        cx = float((m.sum(axis=0) * np.arange(nw)).sum() / max(m.sum(), 1))
        x = int(bx + bw / 2 - cx)
        x = int(min(max(x, bx + bw - nw), bx)) if nw >= bw else int(min(max(x, bx), bx + bw - nw))
    else:
        x = int(bx if align == "left" else bx + (bw - nw) / 2 if align == "center" else bx + bw - nw)
    y = int(by if fill and nh > bh else by + bh - nh)
    # white sticker outline: dilate the mask, round its corners
    r = int(card.W * S * 0.013)
    pad = r + 4
    mp = np.pad(m, pad)
    outline = cv2.dilate((mp > 0.5).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1)))
    outline = cv2.GaussianBlur(outline.astype(np.float32), (0, 0), r * 0.25)
    outline = np.clip((outline - 0.5) * 4 + 0.5, 0, 1)
    gp = np.pad(gray, pad, constant_values=255).astype(np.float32)
    canvas = np.asarray(card.img).astype(np.float32).copy()
    H, W = canvas.shape[:2]
    X0, Y0 = x - pad, y - pad
    cx0, cy0, cx1, cy1 = max(X0, 0), max(Y0, 0), min(X0 + mp.shape[1], W), min(Y0 + mp.shape[0], H)
    sl = (slice(cy0 - Y0, cy1 - Y0), slice(cx0 - X0, cx1 - X0))
    region = canvas[cy0:cy1, cx0:cx1]
    o, a, g = outline[sl][..., None], mp[sl][..., None], gp[sl][..., None]
    region = region * (1 - o) + 255 * o
    region = region * (1 - a) + g * a
    canvas[cy0:cy1, cx0:cx1] = region
    card.img = Image.fromarray(np.clip(canvas, 0, 255).astype(np.uint8))
    card.d = ImageDraw.Draw(card.img)
    box = card.to_pct((max(x - r, 0), max(y - r, 0), min(x + nw + r, W), min(y + nh, H)))
    card.note_layer("cutout", box, (cut.get("note", "person") + ("; halftone dot screen" if cut.get("halftone") else "; grainy black and white")
                                    + "; white sticker outline; generated on green, keyed in code"))
    return box


def arrow(card):
    W, H = card.W * S, card.H * S
    x0, x1, y = W * 0.82, W * 0.932, H * 0.94
    lw = int(W * 0.0042)
    card.d.line((x0, y, x1, y), fill=hex_rgb(card.t["ink"]), width=lw)
    head = W * 0.026
    card.d.line((x1 - head, y - head, x1 + lw * 0.3, y + lw * 0.3), fill=hex_rgb(card.t["ink"]), width=lw)
    card.d.line((x1 - head, y + head, x1 + lw * 0.3, y - lw * 0.3), fill=hex_rgb(card.t["ink"]), width=lw)
    card.note_layer("arrow", card.to_pct((x0, y - head, x1, y + head)), "thin black swipe arrow")


def render(card, s, n):
    head_f = portable.weighted(FONTS / "Inter-VF.ttf", int(card.hpx(HEAD_PCT) * S), 700)
    body_f = ImageFont.truetype(str(FONTS / "DejaVuSansMono.ttf"), int(card.hpx(BODY_PCT) * S))
    center = s.get("layout", "left") == "center"
    W = card.W * S
    x = W / 2 if center else card.wpx(LEFT_X) * S
    anchor = "ma" if center else "la"
    check_text(s["heading"])
    y = card.hpx(s["heading_y"]) * S
    bb = card.d.textbbox((x, y), s["heading"], font=head_f, anchor=anchor)
    card.d.text((x, y), s["heading"], font=head_f, fill=hex_rgb(card.t["ink"]), anchor=anchor)
    card.note_text(s["heading"], bb, "hook" if s.get("role") == "hook" else "headline", "top-headline", "center" if center else "left",
                   "Inter Bold", HEAD_PCT, "lowercase", card.t["ink"], "negative-space")
    if s.get("body"):
        y = card.hpx(s["heading_y"] + s.get("body_gap", 6)) * S
        pitch = card.hpx(PITCH_PCT) * S
        top, boxes = y, []
        for p_i, para in enumerate(s["body"]):
            for line in para.split("\n"):
                check_text(line)
                card.d.text((x, y), line, font=body_f, fill=hex_rgb(card.t["ink"]), anchor=anchor)
                boxes.append(card.d.textbbox((x, y), line, font=body_f, anchor=anchor))
                y += pitch
            y += pitch
        bb = (min(b[0] for b in boxes), top, max(b[2] for b in boxes), max(b[3] for b in boxes))
        card.note_text("\n\n".join(s["body"]), bb, "body", "stacked-paragraphs", "center" if center else "left",
                       "DejaVu Sans Mono (Space Mono stand-in)", BODY_PCT, "lowercase", card.t["ink"], "negative-space")
    text_bottom = bb[3] / S / card.H * 100  # bottom of the body (or the heading when there is no body)
    subject = place_cutout(card, s["cutout"], n, text_bottom) if s.get("cutout") else None
    if s.get("arrow"):
        arrow(card)
    return subject


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    out = args.out or args.spec.parent / "output"
    (out / "records").mkdir(parents=True, exist_ok=True)
    for i, s in enumerate(spec["slides"], 1):
        card = Card(args.spec.parent, spec.get("canvas", [1080, 1350]), {**THEME, **spec.get("theme", {})})
        subject = render(card, s, i)
        card.finish(out / f"slide{i}.png")
        rec = {"n": i, "role": s.get("role", "body"), "class": "other:meme-cutout-text-card", "confidence": "high",
               "frame": {"canvas": f"4:5 portrait, {card.W}x{card.H}",
                         "layers": [{"type": "background", "box": [0, 0, 100, 100], "note": f"flat card colour {card.t['bg']}"}] + card.layers,
                         "composition": {"subject_box": subject}},
               "text_blocks": card.texts}
        (out / "records" / f"slide{i}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"slide{i}.png  ({len(card.texts)} text blocks)")


if __name__ == "__main__":
    main()
