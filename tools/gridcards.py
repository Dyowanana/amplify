#!/usr/bin/env python3
"""P017-type object grid carousel renderer: text drawn in code, object art multiply-blended on the card (cards.py's Card).

Usage:
  gridcards.py <spec.json> [--out DIR]

Spec (paths are relative to the spec file):
  {"canvas": [1080, 1350],
   "theme": {"bg": "#hex", "ink": "#hex", "accent": "#hex", "grey": "#hex", "photo_accent": "#hex"},
   "slides": [
     {"type": "grid", "heading": [["plain words ", ""], ["payoff words", "accent"]], "sub": "optional grey line",
      "items": [{"art": "raw/art/x.png", "label": "…", "reason": "…"}, … 6 items, row by row]},
     {"type": "explainer", "heading": [[…]], "paragraphs": ["…", "…"], "highlight": ["Brand Name"]},
     {"type": "photo", "photo": "raw/photo/x.png", "heading": [[…]], "sub": "…", "focus_y": 0.35}]}

Layouts (P017 §11, re-spaced for a full-bleed 1080x1350 card because the source cards sit inside TikTok's grey bars):
  grid       serif headline with the payoff in the accent italic, centred at 11%; grey subheading; 2 x 3 objects (column
             centres 18/50/82%, rows 20-45.5% and 56.5-82%) with a bold label and a grey reason under each.
  explainer  serif heading at about 30%, a three-dot accent divider, centred sans paragraphs; highlight words in accent bold.
  photo      the photo cover-cropped, phone_look() grain, a dark gradient on the lower 45%, white serif headline with the
             payoff in photo_accent italic at about 64%, white sans subline under it.
Headings and labels are lowercase by the owner's rule (brand names keep their capitals); no dashes, colons or semicolons.
Writes DIR/slideN.png and DIR/records/slideN.json (visual data model, boxes measured from the drawn pixels).
"""
import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageOps

import portable
from cards import Card, S, hex_rgb
from overlay import phone_look

FONTS = Path(__file__).resolve().parent.parent / "assets" / "fonts"
THEME = {"bg": "#faf8f4", "ink": "#1f1a17", "accent": "#d4508a", "grey": "#8a8580", "photo_accent": "#f2a7c3", "white": "#ffffff"}
SERIF, SERIF_IT, SANS = FONTS / "PlayfairDisplay-VF.ttf", FONTS / "PlayfairDisplay-Italic-VF.ttf", FONTS / "Inter-VF.ttf"
SERIF_NAME, SANS_NAME = "Playfair Display (Italic for the payoff)", "Inter"


def font(card, path, size_pct, weight):
    return portable.weighted(path, int(round(card.hpx(size_pct) * S)), weight)


def heading_lines(card, segs, size_pct, max_w_pct):
    """Segments [[text, style]] → lines of (text, font, colour_key). Fits on one line if it can, otherwise the plain part on
    line 1 and the payoff on line 2 (the source's wrap), and only then word-wraps."""
    plain, accent = font(card, SERIF, size_pct, 600), font(card, SERIF_IT, size_pct, 500)
    parts = [(t, accent if st == "accent" else plain, st or "ink") for t, st in segs]
    width = lambda line: sum(card.d.textlength(t, font=f) for t, f, _ in line)
    max_px = card.wpx(max_w_pct) * S
    if width(parts) <= max_px:
        return [parts]
    lines = []
    for p in parts:
        words, cur = p[0].split(), ""
        for w in words:
            trial = (cur + " " + w).strip()
            if card.d.textlength(trial, font=p[1]) > max_px and cur:
                lines.append([(cur, p[1], p[2])])
                cur = w
            else:
                cur = trial
        lines.append([(cur, p[1], p[2])])
    return lines


def draw_heading(card, segs, center_y_pct, size_pct, colours, max_w_pct=86, role="headline"):
    lines = heading_lines(card, segs, size_pct, max_w_pct)
    lh = card.hpx(size_pct) * S * 1.18
    y = card.hpx(center_y_pct) * S - lh * (len(lines) - 1) / 2
    boxes = []
    for line in lines:
        total = sum(card.d.textlength(t, font=f) for t, f, _ in line)
        x = card.W * S / 2 - total / 2
        for i, (t, f, key) in enumerate(line):
            txt = t if i == len(line) - 1 else t.rstrip() + " "
            bb = card.text((x, y), txt.strip(), f, colours[key], anchor="lm")
            boxes.append(bb)
            x += card.d.textlength(txt, font=f)
        y += lh
    bb = (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))
    text = " ".join(t for t, _ in segs).replace("  ", " ").strip()
    card.note_text(text, bb, role, "top-headline" if center_y_pct < 33 else "lower-third" if center_y_pct > 55 else "center-block",
                   "center", SERIF_NAME, size_pct, "lowercase", f"{colours['ink']} / {colours['accent']}", "negative-space")
    return bb


def centred_text(card, text, y_pct, fnt, fill, max_w_pct, cx_pct=50):
    lines, cur = [], ""
    for w in text.split():
        trial = (cur + " " + w).strip()
        if card.d.textlength(trial, font=fnt) > card.wpx(max_w_pct) * S and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    lines.append(cur)
    y, bbs = card.hpx(y_pct) * S, []
    for ln in lines:
        bbs.append(card.text((card.wpx(cx_pct) * S, y), ln, fnt, fill, anchor="mt"))
        y += fnt.size * 1.25
    return (min(b[0] for b in bbs), min(b[1] for b in bbs), max(b[2] for b in bbs), max(b[3] for b in bbs))


def slide_grid(card, s):
    t = card.t
    two_lines = len(heading_lines(card, s["heading"], 4.4, 86)) > 1
    hb = draw_heading(card, s["heading"], 8.6 if two_lines else 10.5, 4.4, {"ink": t["ink"], "accent": t["accent"]})
    if s.get("sub"):  # under the heading, pushed down when the heading wraps to two lines
        f = font(card, SANS, 1.75, 400)
        bb = centred_text(card, s["sub"], max(15.2, hb[3] / S / card.H * 100 + 1.2), f, t["grey"], 70)
        card.note_text(s["sub"], bb, "subheading", "top-headline", "center", SANS_NAME, 1.75, "lowercase", t["grey"], "negative-space")
    lab, rea = font(card, SANS, 2.1, 600), font(card, SANS, 1.6, 400)
    rows = [(20, 47.8), (56.5, 84.3)]
    placed = []
    for i, it in enumerate(s["items"]):
        r, c = divmod(i, 3)
        cx = (18, 50, 82)[c]
        art, _ = card.load_art(it["art"])
        box, _ = card.place_art(art, [cx - 14.5, rows[r][0], 29, 25.5])
        placed.append(box)
        lb = centred_text(card, it["label"], rows[r][1], lab, t["ink"], 30, cx)
        rb = centred_text(card, it["reason"], lb[3] / S / card.H * 100 + 0.7, rea, t["grey"], 30, cx)
        card.note_text(it["label"], lb, "label", "grid-labels", "center", SANS_NAME + " SemiBold", 2.1, "lowercase", t["ink"], "negative-space")
        card.note_text(it["reason"], rb, "body", "grid-labels", "center", SANS_NAME, 1.6, "lowercase", t["grey"], "negative-space")
    grid = card.to_pct((min(b[0] for b in placed), min(b[1] for b in placed), max(b[2] for b in placed), max(b[3] for b in placed)))
    card.note_layer("object cut-outs", grid, "6 photoreal object cut-outs in a 2 x 3 grid, multiply-blended on the card")
    return {"summary": "object grid: " + " ".join(x for x, _ in s["heading"]), "subject_box": grid}


def slide_explainer(card, s):
    t = card.t
    hb = draw_heading(card, s["heading"], s.get("heading_y", 27), 3.8, {"ink": t["ink"], "accent": t["accent"]})
    dot_y = hb[3] + card.hpx(2.2) * S
    for k in (-1, 0, 1):
        x, r = card.W * S / 2 + k * card.wpx(1.6) * S, card.hpx(0.22) * S
        card.d.ellipse((x - r, dot_y - r, x + r, dot_y + r), fill=hex_rgb(t["accent"]))
    reg, bold = font(card, SANS, 2.55, 400), font(card, SANS, 2.55, 700)
    hl = [[h] for h in s.get("highlight", [])]
    y, max_px, boxes = dot_y + card.hpx(3.0) * S, card.wpx(82) * S, []
    for para in s["paragraphs"]:
        for h in s.get("highlight", []):  # keep a highlighted name on one line
            para = para.replace(h, h.replace(" ", " "))
        words = para.split(" ")
        flags = [False] * len(words)
        for h in hl:
            for i in range(len(words) - len(h) + 1):
                if [w.strip(",.").replace(" ", " ") for w in words[i:i + len(h)]] == [" ".join(h)][:len(h)] or [w.strip(",.") for w in words[i:i + len(h)]] == h:
                    for j in range(i, i + len(h)):
                        flags[j] = True
        lines, cur = [], []
        for w, f in zip(words, flags):
            trial = cur + [(w, f)]
            if sum(card.d.textlength(x + " ", font=bold if b else reg) for x, b in trial) > max_px and cur:
                lines.append(cur)
                cur = [(w, f)]
            else:
                cur = trial
        lines.append(cur)
        for ln in lines:
            total = sum(card.d.textlength(x + " ", font=bold if b else reg) for x, b in ln) - card.d.textlength(" ", font=reg)
            x = card.W * S / 2 - total / 2
            for w, b in ln:
                boxes.append(card.text((x, y + reg.getmetrics()[0]), w, bold if b else reg, t["accent"] if b else t["ink"], anchor="ls"))
                x += card.d.textlength(w + " ", font=bold if b else reg)
            y += reg.size * 1.42
        y += card.hpx(1.4) * S
    bb = (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))
    card.note_text(" / ".join(s["paragraphs"]), bb, "body", "center-block", "center", SANS_NAME, 2.55, "lowercase",
                   f"{t['ink']}, highlight {t['accent']} bold", "negative-space")
    card.note_layer("divider", card.to_pct((card.W * S / 2 - card.wpx(2) * S, dot_y - 4, card.W * S / 2 + card.wpx(2) * S, dot_y + 4)), "three accent dots")
    return {"summary": "explainer: " + " ".join(x for x, _ in s["heading"]), "subject_box": card.to_pct(bb)}


def slide_photo(card, s):
    t = card.t
    im = Image.open(card.dir / s["photo"]).convert("RGB")
    im = ImageOps.fit(im, (card.W * S, card.H * S), Image.LANCZOS, centering=(0.5, s.get("focus_y", 0.4)))
    im = phone_look(im.resize((card.W, card.H), Image.LANCZOS), s.get("grain", 0.8)).resize((card.W * S, card.H * S), Image.LANCZOS)
    a = np.asarray(im, dtype=np.float32)
    ramp = np.clip((np.arange(card.H * S) / (card.H * S) - 0.5) / 0.38, 0, 1) ** 1.1 * 0.7
    a *= (1 - ramp)[:, None, None]
    card.img = Image.fromarray(a.astype(np.uint8))
    card.d = ImageDraw.Draw(card.img)
    card.note_layer("photo", [0, 0, 100, 100], "full-bleed lifestyle photo, phone_look grain")
    card.note_layer("dark gradient", [0, 52, 100, 48], "black gradient from 50% height to 70% darkness at 88%, behind the text")
    draw_heading(card, s["heading"], s.get("heading_y", 64), 4.4, {"ink": t["white"], "accent": t["photo_accent"]}, role="headline")
    if s.get("sub"):
        f = font(card, SANS, 1.9, 500)
        bb = centred_text(card, s["sub"], s.get("heading_y", 64) + 4.6, f, t["white"], 70)
        card.note_text(s["sub"], bb, "cta", "lower-third", "center", SANS_NAME, 1.9, "lowercase", t["white"], "body")
    return {"summary": "photo closer: " + " ".join(x for x, _ in s["heading"]), "subject_box": [10, 5, 80, 80]}


SLIDES = {"grid": slide_grid, "explainer": slide_explainer, "photo": slide_photo}


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
        info = SLIDES[s["type"]](card, s)
        card.finish(out / f"slide{i}.png")
        rec = {"n": i, "role": s.get("role", s["type"]), "class": "humans" if s["type"] == "photo" else "other:designed-card", "confidence": "high",
               "summary": info["summary"],
               "frame": {"canvas": f"4:5 portrait, {card.W}x{card.H}",
                         "layers": ([] if s["type"] == "photo" else [{"type": "background", "box": [0, 0, 100, 100], "note": f"flat card colour {card.t['bg']}"}]) + card.layers,
                         "composition": {"subject_box": info["subject_box"]}},
               "text_blocks": card.texts}
        (out / "records" / f"slide{i}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"slide{i}.png  ({len(card.texts)} text blocks)")


if __name__ == "__main__":
    main()
