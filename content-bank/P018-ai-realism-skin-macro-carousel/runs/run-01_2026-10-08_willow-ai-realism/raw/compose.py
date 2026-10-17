"""Crop each still to 9:16, then overlay.py: phone finish (light, the macros need their texture) + clean text on slides 1 and 6."""
import json, subprocess, sys
import numpy as np
from pathlib import Path
from PIL import Image
R = Path(__file__).resolve().parent.parent
PY = sys.executable
# measured brightness to match (source slides 1, 2, 5 measure 50.5, 38.8, 52.1; ours came out 61.9, 48.9, 56.3)
TARGET = {1: 51, 2: 44, 5: 52}


def expose(im, target):
    """Gamma so the mean brightness (0-100) lands on target: darkens the mid-tones, keeps the texture."""
    a = np.asarray(im, dtype=np.float32) / 255
    lo, hi = 0.5, 3.0
    for _ in range(30):
        g = (lo + hi) / 2
        m = (np.asarray(Image.fromarray((a ** g * 255).astype(np.uint8)).convert("L"), dtype=np.float32).mean() / 2.55)
        lo, hi = (g, hi) if m > target else (lo, g)
    return Image.fromarray(np.clip(a ** g * 255, 0, 255).astype(np.uint8))


# file, crop width as a share of the still (1.0 = full frame), crop centre (x, y), text, text y, size
SLIDES = [
    ("s1_eye.png",    1.00, (0.50, 0.50), "every freckle here is **fake**", 0.47, 0.032),
    ("s2_selfie.png", 1.00, (0.50, 0.50), None, 0, 0),
    ("s3_lips.png",   0.72, (0.42, 0.40), None, 0, 0),
    ("s4_nose.png",   0.86, (0.55, 0.45), None, 0, 0),
    ("s5_cheek.png",  0.86, (0.50, 0.42), None, 0, 0),
    ("s6_brow.png",   1.00, (0.50, 0.50), "would she fool **you**/be honest", 0.45, 0.031),
]
for n, (f, share, (cx, cy), text, ty, size) in enumerate(SLIDES, 1):
    im = Image.open(R / "raw" / f).convert("RGB")
    w = round(im.width * share); h = round(w * 16 / 9)
    if h > im.height: h = im.height; w = round(h * 9 / 16)
    left = min(max(0, round(im.width * cx - w / 2)), im.width - w)
    top = min(max(0, round(im.height * cy - h / 2)), im.height - h)
    crop = R / "raw" / "crops" / f"slide{n}.png"
    out = im.crop((left, top, left + w, top + h)).resize((1080, 1920), Image.LANCZOS)
    out = expose(out, TARGET[n]) if n in TARGET else out
    out.save(crop)
    cmd = [PY, "tools/overlay.py", str(crop), "--out", str(R / "output" / f"slide{n}.png"), "--phone", "0.5", "--style", "clean"]
    if text: cmd += ["--text", text, "--y", str(ty), "--size", str(size)]
    subprocess.run(cmd, check=True)
    print(n, f, f"crop {w}x{h} at {left},{top}")
