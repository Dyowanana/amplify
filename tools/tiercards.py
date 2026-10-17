#!/usr/bin/env python3
"""P021-type tier list chart renderer: the table and every word drawn in code, cut-out icons multiply-blended on the card.

Usage:
  tiercards.py cut <sheet.png> --names a,b,c,… --out DIR [--min-area 0.004]
      Splits an icon sheet (separate objects on white) into one PNG per object: finds the objects as connected regions,
      orders them row by row, left to right, and saves DIR/<name>.png cropped to the object on white.
  tiercards.py render <spec.json> [--out DIR]

Spec (paths are relative to the spec file):
  {"canvas": [1080, 1350], "theme": {"bg": "#hex", "ink": "#hex"},
   "slides": [
     {"type": "cover", "top": "tier list of", "hero": "raw/art/hero.png", "topic": "marketing", "qualifier": "…",
      "corner_left": "growth", "corner_right": "raw/art/cut/magnet.png"},
     {"type": "chart", "title": "…", "cta": "…", "handle": "optional",
      "tiers": [{"letter": "S", "tagline": "…", "color": "#hex", "items": [{"art": "…", "label": "…"} | {"glyph": "?", "label": "…"}]}, …],
      "f": {same as one tier: drawn after a plus sign, apart from the table}}]}

Layout (P021 §11, measured on the source at 1080x1350): table x 7.6% to 85.4%, letter column to 22%, five rows from 17.5% to
73.2%, a plus sign at about 76%, the F row 78.9% to 90%. One thin grotesque for everything (Inter at weight 300 stands in for
Helvetica Neue Light), slightly tightened like the source. Rows with fewer than 4 items spread them over equal slots.
Headings and labels are lowercase by the owner's rule; no dashes, colons or semicolons (checked here, the render stops).
Writes DIR/slideN.png and DIR/records/slideN.json (visual data model, boxes measured from the drawn pixels).
"""
import argparse
import json
import re
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

import portable
from cards import Card, S, hex_rgb

FONTS = Path(__file__).resolve().parent.parent / "assets" / "fonts"
SANS, SANS_NAME = FONTS / "Inter-VF.ttf", "Inter Light (Helvetica Neue Light stand-in)"
THEME = {"bg": "#edf2eb", "ink": "#111111", "line": "#111111"}
TRACK = -0.035  # letter spacing as a share of the font size; the source's headline face is set tight
BANNED = re.compile(r"[—–:;]")


def font(card, size_pct, weight=None):
    """Inter: display optical size and weight 250 for headings (closer to Helvetica Neue Light), text cut at 300 for small type."""
    big = size_pct >= 4
    f = portable.weighted(SANS, int(round(card.hpx(size_pct) * S)), weight or (250 if big else 300))
    f.set_variation_by_axes([32 if big else 14, weight or (250 if big else 300)])  # axes: optical size, weight
    return f


def tracked_len(card, s, f, track=TRACK):
    return sum(card.d.textlength(ch, font=f) for ch in s) + track * f.size * (len(s) - 1)


def draw_tracked(card, x, y, s, f, fill, anchor="l", track=TRACK):
    """Draw s with tightened letter spacing; x is the left edge (anchor l), the centre (m) or the right edge (r), y the baseline."""
    w = tracked_len(card, s, f, track)
    x = x - w / 2 if anchor == "m" else x - w if anchor == "r" else x
    boxes = []
    for ch in s:
        boxes.append(card.d.textbbox((x, y), ch, font=f, anchor="ls"))
        card.d.text((x, y), ch, font=f, fill=hex_rgb(fill), anchor="ls")
        x += card.d.textlength(ch, font=f) + track * f.size
    boxes = [b for b in boxes if b[2] > b[0]]
    return (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))


def line(card, x0, y0, x1, y1, width_px, fill):
    card.d.line([(x0, y0), (x1, y1)], fill=hex_rgb(fill), width=max(1, int(round(width_px * S))))


def place(card, rel, box_pct, anchor="bottom"):
    art, _ = card.load_art(rel)
    return card.place_art(art, box_pct, align="bottom-center" if anchor == "bottom" else "center")[0]


# ---------------------------------------------------------------- cover
def growth_glyph(card, box_pct, ink):
    """Black line drawing with round end nodes (the source's corner molecule, redrawn as a rising chart line)."""
    x, y, w, h = [card.wpx(box_pct[0]) * S, card.hpx(box_pct[1]) * S, card.wpx(box_pct[2]) * S, card.hpx(box_pct[3]) * S]
    pts = [(0.05, 0.92), (0.30, 0.55), (0.52, 0.72), (0.95, 0.10)]
    pts = [(x + px * w, y + py * h) for px, py in pts]
    lw = card.hpx(0.62) * S
    card.d.line(pts, fill=hex_rgb(ink), width=int(lw), joint="curve")
    r = card.hpx(1.25) * S
    for i, (px, py) in enumerate(pts):
        if i in (0, len(pts) - 1):
            card.d.ellipse((px - r, py - r, px + r, py + r), fill=hex_rgb(card.t["bg"]), outline=hex_rgb(ink), width=int(lw))
    return (x - r, y - r, x + w + r, y + h + r)


def slide_cover(card, s):
    t = card.t
    f_top, f_topic, f_qual = font(card, 12.6), font(card, 10.8), font(card, 6.9)
    bb = draw_tracked(card, card.W * S / 2, card.hpx(21.7) * S, s["top"], f_top, t["ink"], "m")
    card.note_text(s["top"], bb, "hook", "top-headline", "center", SANS_NAME, 12.6, "lowercase", t["ink"], "negative-space")
    hb = place(card, s["hero"], s.get("hero_box", [17, 24.5, 66, 37]), anchor="center")
    card.note_layer("hero cut-out", card.to_pct(hb), "false-colour scan of the topic's core object, thin white outline")
    bb = draw_tracked(card, card.W * S / 2, card.hpx(69.6) * S, s["topic"], f_topic, t["ink"], "m")
    card.note_text(s["topic"], bb, "headline", "center-block", "center", SANS_NAME, 10.8, "lowercase", t["ink"], "negative-space")
    bb = draw_tracked(card, card.W * S / 2, card.hpx(75.8) * S, s["qualifier"], f_qual, t["ink"], "m")
    card.note_text(s["qualifier"], bb, "subheading", "center-block", "center", SANS_NAME, 6.9, "lowercase", t["ink"], "negative-space")
    if s.get("corner_left") == "growth":
        gb = growth_glyph(card, [11, 84, 31, 10.5], t["ink"])
        card.note_layer("line glyph", card.to_pct(gb), "black rising chart line with round end nodes, bottom-left")
    if s.get("corner_right"):
        cb = place(card, s["corner_right"], [70, 82.5, 15, 13])
        card.note_layer("3D icon", card.to_pct(cb), "glossy 3D object, bottom-right")
    return {"summary": f"cover: {s['top']} {s['topic']} {s['qualifier']}", "subject_box": card.to_pct(hb)}


# ---------------------------------------------------------------- chart
X0, XL, X1 = 7.6, 22.0, 85.4
ROW_TOP, ROW_H, F_TOP = 17.5, 11.14, 78.9


def tier_row(card, tier, top, f_letter, f_tag, f_label):
    t = card.t
    bot = top + ROW_H
    px = lambda v, axis: (card.wpx(v) if axis == "x" else card.hpx(v)) * S
    card.d.rectangle((px(X0, "x"), px(top, "y"), px(XL, "x"), px(bot, "y")), fill=hex_rgb(tier["color"]))
    lb = draw_tracked(card, px((X0 + XL) / 2, "x"), px(top + ROW_H * 0.60, "y"), tier["letter"], f_letter, t["ink"], "m", track=0)
    card.note_text(tier["letter"], lb, "label", "tier letter", "center", SANS_NAME, 5.0, "caps", t["ink"], "colour cell")
    tag_lines = tier["tagline"].split(" / ")
    if len(tag_lines) == 1 and tracked_len(card, tag_lines[0], f_tag, -0.02) > card.wpx(XL - X0 - 1.2) * S and ", " in tag_lines[0]:
        a, b = tag_lines[0].split(", ", 1)
        tag_lines = [a + ",", b]
    y = bot - 0.95 - (len(tag_lines) - 1) * 1.45
    for tl in tag_lines:
        tb = draw_tracked(card, px((X0 + XL) / 2, "x"), px(y, "y"), tl, f_tag, t["ink"], "m", track=-0.02)
        card.note_text(tl, tb, "body", "tier tagline", "center", SANS_NAME, 1.5, "lowercase", t["ink"], "colour cell")
        y += 1.45
    items = tier["items"]
    slot = (X1 - XL) / max(len(items), 4) if len(items) >= 4 else (X1 - XL) / len(items)
    boxes = []
    for i, it in enumerate(items):
        cx = XL + slot * (i + 0.5)
        lines = it["label"].split(" / ")
        if len(lines) == 1 and tracked_len(card, lines[0], f_label, -0.03) > card.wpx(slot * 0.96) * S and " " in lines[0]:
            words = lines[0].split()  # wrap to two lines, as balanced as the words allow
            k = min(range(1, len(words)), key=lambda j: abs(len(" ".join(words[:j])) - len(" ".join(words[j:]))))
            lines = [" ".join(words[:k]), " ".join(words[k:])]
        label_top = bot - 1.0 - 2.2 * len(lines)
        if it.get("glyph"):
            gf = font(card, 8.2, 250)
            gb = draw_tracked(card, px(cx, "x"), px(label_top - 0.2, "y"), it["glyph"], gf, t["ink"], "m", track=0)
            boxes.append(gb)
        else:
            boxes.append(place(card, it["art"], [cx - slot * 0.42, top + 0.8, slot * 0.84, label_top - top - 0.8 + it.get("overlap", 0)]))
        y = label_top + 1.9
        for ln in lines:
            bb = draw_tracked(card, px(cx, "x"), px(y, "y"), ln, f_label, t["ink"], "m", track=-0.03)
            card.note_text(ln, bb, "label", "grid-labels", "center", SANS_NAME, 2.45, "lowercase", t["ink"], "negative-space")
            y += 2.2
    return boxes


def table_lines(card, top, bot, rows):
    lw = 1.6
    for k in range(rows + 1):
        y = card.hpx(top + (bot - top) * k / rows) * S
        line(card, card.wpx(X0) * S, y, card.wpx(X1) * S, y, lw, card.t["line"])
    for xv in (X0, XL, X1):
        line(card, card.wpx(xv) * S, card.hpx(top) * S, card.wpx(xv) * S, card.hpx(bot) * S, lw, card.t["line"])


def slide_chart(card, s):
    t = card.t
    f_title, f_letter, f_tag, f_label = font(card, 7.6), font(card, 5.0), font(card, 1.35), font(card, 2.3)
    bb = draw_tracked(card, card.wpx(10.2) * S, card.hpx(12.2) * S, s["title"], f_title, t["ink"])
    card.note_text(s["title"], bb, "hook", "top-headline", "left", SANS_NAME, 7.6, "lowercase", t["ink"], "negative-space")
    icons = []
    for k, tier in enumerate(s["tiers"]):
        icons += tier_row(card, tier, ROW_TOP + k * ROW_H, f_letter, f_tag, f_label)
    table_lines(card, ROW_TOP, ROW_TOP + ROW_H * len(s["tiers"]), len(s["tiers"]))
    card.note_layer("tier table", [X0, ROW_TOP, X1 - X0, ROW_H * len(s["tiers"])], "coloured letter cells, hairline black grid")
    if s.get("f"):
        cx, cy, arm = card.wpx(14.8) * S, card.hpx(76.0) * S, card.hpx(1.75) * S
        line(card, cx - arm, cy, cx + arm, cy, 3.2, t["ink"])
        line(card, cx, cy - arm, cx, cy + arm, 3.2, t["ink"])
        card.note_layer("plus glyph", card.to_pct((cx - arm, cy - arm, cx + arm, cy + arm)), "black plus between the table and the F row")
        icons += tier_row(card, s["f"], F_TOP, f_letter, f_tag, f_label)
        table_lines(card, F_TOP, F_TOP + ROW_H, 1)
        card.note_layer("F row", [X0, F_TOP, X1 - X0, ROW_H], "separate bottom row")
    if s.get("cta"):
        fc = font(card, 4.9)
        bb = draw_tracked(card, card.wpx(11) * S, card.hpx(96.6) * S, s["cta"], fc, t["ink"])
        card.note_text(s["cta"], bb, "cta", "bottom-left", "left", SANS_NAME, 4.9, "lowercase", t["ink"], "negative-space")
    if s.get("handle"):
        fh = font(card, 2.2)
        bb = draw_tracked(card, card.wpx(85.4) * S, card.hpx(96.2) * S, s["handle"], fh, t["ink"], "r", track=-0.02)
        card.note_text(s["handle"], bb, "watermark", "corner-mark", "right", SANS_NAME, 2.2, "lowercase", t["ink"], "negative-space", origin="mark")
    card.note_layer("icons", card.to_pct((min(b[0] for b in icons), min(b[1] for b in icons), max(b[2] for b in icons), max(b[3] for b in icons))),
                    f"{len(icons)} cut-out icons: photoreal objects, glossy 3D icons and black glyphs, multiply-blended on the card")
    return {"summary": f"tier chart: {s['title']}", "subject_box": [X0, ROW_TOP, X1 - X0, F_TOP + ROW_H - ROW_TOP]}


SLIDES = {"cover": slide_cover, "chart": slide_chart}


def texts_of(spec):
    out = []
    for s in spec["slides"]:
        out += [s.get(k, "") for k in ("top", "topic", "qualifier", "title", "cta")]
        for tier in s.get("tiers", []) + ([s["f"]] if s.get("f") else []):
            out += [tier["tagline"]] + [it["label"] for it in tier["items"]]
    return [x for x in out if x]


def render(args):
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    bad = [x for x in texts_of(spec) if BANNED.search(x)]
    if bad:
        sys.exit(f"banned punctuation (dash, colon, semicolon) in: {bad}")
    out = args.out or args.spec.parent / "output"
    (out / "records").mkdir(parents=True, exist_ok=True)
    for i, s in enumerate(spec["slides"], 1):
        card = Card(args.spec.parent, spec.get("canvas", [1080, 1350]), {**THEME, **spec.get("theme", {})})
        info = SLIDES[s["type"]](card, s)
        card.finish(out / f"slide{i}.png")
        rec = {"n": i, "role": "hook" if s["type"] == "cover" else "body", "class": "other:tier-chart-card", "confidence": "high",
               "summary": info["summary"],
               "frame": {"canvas": f"4:5 portrait, {card.W}x{card.H}",
                         "layers": [{"type": "background", "box": [0, 0, 100, 100], "note": f"flat card colour {card.t['bg']}"}] + card.layers,
                         "composition": {"subject_box": info["subject_box"]}},
               "text_blocks": card.texts}
        (out / "records" / f"slide{i}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"slide{i}.png  ({len(card.texts)} text blocks)")


def cut(args):
    im = cv2.imread(str(args.sheet))
    names = [n.strip() for n in args.names.split(",")]
    mask = (im.min(axis=2) < 236).astype(np.uint8)
    k = max(3, int(min(im.shape[:2]) * 0.02)) | 1
    grown = cv2.dilate(mask, np.ones((k, k), np.uint8))
    n, lab, stats, cent = cv2.connectedComponentsWithStats(grown)
    area_min = args.min_area * im.shape[0] * im.shape[1]
    objs = [(stats[i], cent[i]) for i in range(1, n) if stats[i][4] >= area_min]
    if len(objs) != len(names):
        sys.exit(f"found {len(objs)} objects, expected {len(names)}: adjust --min-area or check the sheet")
    # rows: cluster by centre y, then left to right
    objs.sort(key=lambda o: o[1][1])
    rows, cur = [], [objs[0]]
    for o in objs[1:]:
        if abs(o[1][1] - np.mean([c[1][1] for c in cur])) < im.shape[0] * 0.12:
            cur.append(o)
        else:
            rows.append(cur)
            cur = [o]
    rows.append(cur)
    ordered = [o for r in rows for o in sorted(r, key=lambda o: o[1][0])]
    args.out.mkdir(parents=True, exist_ok=True)
    pad = 12
    for name, (st, _) in zip(names, ordered):
        x, y, w, h = st[:4]
        crop = np.full((h + 2 * pad, w + 2 * pad, 3), 255, np.uint8)
        crop[pad:pad + h, pad:pad + w] = im[y:y + h, x:x + w]
        cv2.imwrite(str(args.out / f"{name}.png"), crop)
        print(f"{name}.png  {w}x{h}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cut")
    c.add_argument("sheet", type=Path)
    c.add_argument("--names", required=True)
    c.add_argument("--out", type=Path, required=True)
    c.add_argument("--min-area", type=float, default=0.004)
    r = sub.add_parser("render")
    r.add_argument("spec", type=Path)
    r.add_argument("--out", type=Path)
    args = ap.parse_args()
    cut(args) if args.cmd == "cut" else render(args)


if __name__ == "__main__":
    main()
