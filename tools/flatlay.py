#!/usr/bin/env python3
"""P019-type essentials flat-lay renderer: one white board, a title drawn in code, cut-out item art multiply-blended on the
card (cards.py's Card), and small app widgets drawn in code (the image model never draws text or UI).

Usage:
  flatlay.py <spec.json> [--out DIR]

Spec (paths are relative to the spec file):
  {"canvas": [1080, 1350], "theme": {"bg": "#ffffff", "ink": "#111111"},
   "title": "founder essentials",       # or a centre block: {"lines": ["peak", "creator", "purchases"], "y": 47, "size": 6.2,
                                          #  "weight": 800, "sub": "guy edition", "sub_size": 2.3}
   "label_size": 2.2,                     # optional, item labels in % of frame height
   "items": [{"art": "raw/art/x.png", "box": [x, y, w, h], "align": "center|left|bottom-center", "note": "…",
              "label": "optional 1 to 2 line label just under the drawn item, a newline breaks it", "label_y": optional top of the label in %},
             {"type": "text", "lines": [".com", ".co", ".io"], "box": […], "label": "…"},   # a text stack used as an item
             {"type": "icon", "glyph": "ai", "fill": "#hex", "box": […], "label": "…"},     # a code-drawn app icon
             …],
   "widgets": [{"type": "limit|payment|revenue", "box": [x, y, w, h], …texts, see below}],
   "versions": [{"name": "guy-1", "items": [{"art": …, "box": …}, …]}, …]}
Top-level items and widgets are on every version; a version adds its own items (the outfit) and may override "title".
With no versions, one board.

Widgets (all text lowercase, no dashes, colons or semicolons; numbers allowed):
  limit    dark modal: "title", "sub", two tiles "left" (grey) and "right" (blue outline, the upsell)
  payment  light phone notification: green app square with "$", "title", "time", "body"
  revenue  "label" + green "change" pill, big "value", a rising line chart over a flat grey one

Layout boxes are % of the frame [x, y, w, h] from the top-left (P019 §11). Items fit inside their box, keeping their aspect.
Writes DIR/<name>.png and DIR/records/<name>.json (visual data model, boxes measured from the drawn pixels).
"""
import argparse
import json
from pathlib import Path

import numpy as np

import portable
from cards import Card, S, hex_rgb

FONTS = Path(__file__).resolve().parent.parent / "assets" / "fonts"
SANS = portable.font("/System/Library/Fonts/SFNS.ttf", "Inter-VF.ttf")
SANS_NAME = "SF Pro Display (Inter on Windows)"
THEME = {"bg": "#ffffff", "ink": "#111111"}


def f(card, size_pct, weight):
    return portable.weighted(SANS, int(round(card.hpx(size_pct) * S)), weight)


def box_px(card, b):
    return card.wpx(b[0]) * S, card.hpx(b[1]) * S, card.wpx(b[0] + b[2]) * S, card.hpx(b[1] + b[3]) * S


def draw_title(card, title):
    if isinstance(title, str):
        fnt = f(card, 6.0, 700)
        bb = card.text((card.W * S / 2, card.hpx(11) * S), title, fnt, card.t["ink"], anchor="mm")
        card.note_text(title, bb, "hook", "top-headline", "center", f"{SANS_NAME} Bold", 6.0, "lowercase", card.t["ink"], "negative-space")
        return
    # centre block (the ring layout): stacked heavy lines with tight leading, then a grey subline
    size, lines = title.get("size", 6.2), title["lines"]
    fnt = f(card, size, title.get("weight", 800))
    lh = card.hpx(size) * S * 1.02
    y = card.hpx(title.get("y", 47)) * S - lh * (len(lines) - 1) / 2
    bbs = []
    for ln in lines:
        bbs.append(card.text((card.W * S / 2, y), ln, fnt, card.t["ink"], anchor="mm"))
        y += lh
    bb = (min(b[0] for b in bbs), min(b[1] for b in bbs), max(b[2] for b in bbs), max(b[3] for b in bbs))
    card.note_text("\n".join(lines), bb, "hook", "center-block", "center", f"{SANS_NAME} Heavy", size, "lowercase", card.t["ink"], "negative-space")
    if title.get("sub"):
        ss = title.get("sub_size", 2.3)
        sb = card.text((card.W * S / 2, bb[3] + card.hpx(ss) * S * 0.9), title["sub"], f(card, ss, 600), "#555555", anchor="mt")
        card.note_text(title["sub"], sb, "subheading", "center-block", "center", f"{SANS_NAME} Semibold", ss, "lowercase", "#555555", "negative-space")


def draw_label(card, it, size, placed):
    """1 to 2 centred lines just under the drawn item (placed: its pixel box at S), or at label_y."""
    x0, y0, x1, y1 = placed
    fnt = f(card, size, 600)
    y = card.hpx(it["label_y"]) * S if "label_y" in it else y1 + card.hpx(1.0) * S
    bbs = []
    for ln in it["label"].split("\n"):
        bbs.append(card.text(((x0 + x1) / 2, y), ln, fnt, card.t["ink"], anchor="mt"))
        y += fnt.size * 1.12
    bb = (min(b[0] for b in bbs), min(b[1] for b in bbs), max(b[2] for b in bbs), max(b[3] for b in bbs))
    card.note_text(it["label"].replace("\n", " "), bb, "label", "item-label", "center", f"{SANS_NAME} Semibold", size, "lowercase",
                   card.t["ink"], "negative-space")


def text_item(card, it):
    """A short stack of heavy words used as an item (e.g. domain endings), sized to fill the box."""
    x0, y0, x1, y1 = box_px(card, it["box"])
    lines = it["lines"]
    size = it.get("size", (y1 - y0) / S / card.H * 100 / len(lines) / 1.05)
    fnt = f(card, size, 800)
    widest = max(card.d.textlength(ln, font=fnt) for ln in lines)
    if widest > x1 - x0:
        size *= (x1 - x0) / widest
        fnt = f(card, size, 800)
    lh = card.hpx(size) * S * 1.05
    y = (y0 + y1) / 2 - lh * (len(lines) - 1) / 2
    for ln in lines:
        card.text(((x0 + x1) / 2, y), ln, fnt, card.t["ink"], anchor="mm")
        y += lh
    card.note_text(" ".join(lines), (x0, y0, x1, y1), "item", "text-item", "center", f"{SANS_NAME} Heavy", size, "lowercase", card.t["ink"], "negative-space")
    return (x0, y0, x1, y1)


def icon_item(card, it):
    """A code-drawn app icon: rounded square in one colour with a short white glyph (never a real app's icon)."""
    x0, y0, x1, y1 = box_px(card, it["box"])
    side = min(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    b = (cx - side / 2, cy - side / 2, cx + side / 2, cy + side / 2)
    card.rrect(b, side * 0.23, it.get("fill", "#111111"))
    card.text((cx, cy), it["glyph"], portable.weighted(SANS, int(side * 0.42), 800), "#ffffff", anchor="mm")
    return b


def w_limit(card, w):
    x0, y0, x1, y1 = box_px(card, w["box"])
    r, pad = 22 * S, 24 * S
    card.rrect((x0, y0, x1, y1), r, "#1c1c1e")
    t = card.text((x0 + pad, y0 + pad), w["title"], f(card, 1.75, 600), "#ffffff", anchor="lt")
    s = card.text((x0 + pad, t[3] + 8 * S), w["sub"], f(card, 1.3, 400), "#9a9aa0", anchor="lt")
    ty0, ty1 = s[3] + 16 * S, y1 - pad
    gap = 12 * S
    mid = (x0 + x1) / 2
    for (tx0, tx1), label, key in (((x0 + pad, mid - gap / 2), w["left"], "left"), ((mid + gap / 2, x1 - pad), w["right"], "right")):
        upsell = key == "right"
        card.rrect((tx0, ty0, tx1, ty1), 14 * S, "#3b82f6" if upsell else "#2c2c2e")
        if upsell:
            card.rrect((tx0 + 3 * S, ty0 + 3 * S, tx1 - 3 * S, ty1 - 3 * S), 12 * S, "#14223d")
        card.text(((tx0 + tx1) / 2, (ty0 + ty1) / 2), label, f(card, 1.45, 600), "#ffffff" if upsell else "#c7c7cc", anchor="mm")
    text = f"{w['title']} / {w['sub']} / {w['left']} / {w['right']}"
    card.note_text(text, (x0, y0, x1, y1), "joke-prop", "ui-snippet", "left", SANS_NAME, 1.75, "lowercase", "#ffffff", "dark ui card", origin="in-image-ui")
    return "dark usage-limit modal with a wait tile and an upgrade tile"


def w_payment(card, w):
    x0, y0, x1, y1 = box_px(card, w["box"])
    pad = 20 * S
    card.rrect((x0, y0, x1, y1), 24 * S, "#f0f0f3")
    icon = (y1 - y0) - 2 * pad
    icon = min(icon, 62 * S)
    iy = (y0 + y1) / 2 - icon / 2
    card.rrect((x0 + pad, iy, x0 + pad + icon, iy + icon), icon * 0.24, "#22c55e")
    card.text((x0 + pad + icon / 2, iy + icon / 2), "$", f(card, 2.6, 700), "#ffffff", anchor="mm")
    tx = x0 + pad + icon + 16 * S
    t = card.text((tx, iy + 2 * S), w["title"], f(card, 1.5, 600), "#111111", anchor="lt")
    card.text((x1 - pad, iy + 2 * S), w["time"], f(card, 1.2, 400), "#8e8e93", anchor="rt")
    card.text((tx, t[3] + 8 * S), w["body"], f(card, 1.4, 400), "#3a3a3c", anchor="lt")
    card.note_text(f"{w['title']} / {w['time']} / {w['body']}", (x0, y0, x1, y1), "joke-prop", "ui-snippet", "left", SANS_NAME, 1.5,
                   "lowercase", "#111111", "light ui card", origin="in-image-ui")
    return "light phone notification of a new payment"


def w_revenue(card, w):
    x0, y0, x1, y1 = box_px(card, w["box"])
    lab = card.text((x0, y0), w["label"], f(card, 1.6, 500), "#3a3a3c", anchor="lt")
    pf = f(card, 1.35, 600)
    pw = card.d.textlength(w["change"], font=pf)
    px0, ph = lab[2] + 12 * S, lab[3] - lab[1] + 10 * S
    card.rrect((px0, lab[1] - 5 * S, px0 + pw + 18 * S, lab[1] - 5 * S + ph), 8 * S, "#dcfce7")
    card.text((px0 + 9 * S, (lab[1] + lab[3]) / 2), w["change"], pf, "#15803d", anchor="lm")
    v = card.text((x0, lab[3] + 14 * S), w["value"], f(card, 3.0, 500), "#111111", anchor="lt")
    cy0, cy1 = v[3] + 18 * S, y1
    xs = np.linspace(x0, x1, 40)
    base = cy1 - (cy1 - cy0) * 0.12  # both lines start together; the green one pulls away
    rise = base - (base - cy0) * (np.linspace(0, 1, 40) ** 1.8) + np.sin(np.linspace(0, 9, 40)) * 2 * S * np.linspace(0, 1, 40)
    flat = base + np.sin(np.linspace(0, 5, 40)) * 2 * S
    card.d.line(list(zip(xs, flat)), fill=hex_rgb("#c7c7cc"), width=3 * S, joint="curve")
    card.d.line(list(zip(xs, rise)), fill=hex_rgb("#16a34a"), width=4 * S, joint="curve")
    card.note_text(f"{w['label']} {w['change']} / {w['value']}", (x0, y0, x1, v[3]), "joke-prop", "ui-snippet", "left", SANS_NAME, 3.0,
                   "lowercase", "#111111", "white", origin="in-image-ui")
    return "revenue widget, green change pill, big figure, rising line chart"


WIDGETS = {"limit": w_limit, "payment": w_payment, "revenue": w_revenue}


def render(spec_dir, spec, items, out, name):
    card = Card(spec_dir, spec.get("canvas", [1080, 1350]), {**THEME, **spec.get("theme", {})})
    draw_title(card, spec["title"])
    placed = []
    for it in items:
        kind = it.get("type", "art")
        if kind == "text":
            bb = text_item(card, it)
        elif kind == "icon":
            bb = icon_item(card, it)
        else:
            art, _ = card.load_art(it["art"])
            bb, _ = card.place_art(art, it["box"], it.get("align", "center"))
        box = card.to_pct(bb)
        card.note_layer({"text": "text-item", "icon": "app-icon"}.get(kind, "product-cutout"), box, it.get("note", Path(it.get("art", kind)).stem))
        placed.append(box)
        if it.get("label"):
            draw_label(card, it, spec.get("label_size", 2.2), bb)
    for w in spec.get("widgets", []):
        note = WIDGETS[w["type"]](card, w)
        card.note_layer("ui-snippet", w["box"], f"drawn in code: {note}")
        placed.append(w["box"])
    card.finish(out / f"{name}.png")
    sx0 = min(b[0] for b in placed); sy0 = min(b[1] for b in placed)
    sx1 = max(b[0] + b[2] for b in placed); sy1 = max(b[1] + b[3] for b in placed)
    rec = {"n": 1, "role": "hook", "class": "other:essentials-flatlay", "confidence": "high", "version": name,
           "frame": {"canvas": f"4:5 portrait, {card.W}x{card.H}",
                     "layers": [{"type": "background", "box": [0, 0, 100, 100], "note": f"flat card colour {card.t['bg']}"}] + card.layers,
                     "composition": {"subject_box": [round(sx0, 1), round(sy0, 1), round(sx1 - sx0, 1), round(sy1 - sy0, 1)]}},
           "text_blocks": card.texts}
    (out / "records" / f"{name}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{name}.png  ({len(items)} items, {len(spec.get('widgets', []))} widgets)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    out = args.out or args.spec.parent / "output"
    (out / "records").mkdir(parents=True, exist_ok=True)
    for v in spec.get("versions") or [{"name": "board", "items": []}]:
        vspec = {**spec, "title": v.get("title", spec.get("title"))}  # a version may change the title (e.g. the edition line)
        render(args.spec.parent, vspec, spec.get("items", []) + v["items"], out, v["name"])


if __name__ == "__main__":
    main()
