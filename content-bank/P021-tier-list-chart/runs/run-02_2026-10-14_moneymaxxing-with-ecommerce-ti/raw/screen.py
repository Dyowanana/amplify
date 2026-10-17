"""Put the real shopify.com screenshot (their own command-centre card, no people, no other brands) on the generated laptop's green screen."""
import sys
import numpy as np
from PIL import Image, ImageFilter
run = sys.argv[1]
lap = np.array(Image.open(f"{run}/raw/art/cut/laptop.png").convert("RGB")).astype(int)
r, g, b = lap[..., 0], lap[..., 1], lap[..., 2]
green = (g > 150) & (g - np.maximum(r, b) > 60)
ys, xs = np.where(green)
x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
W, H = x1 - x0, y1 - y0
full = Image.open(f"{run}/raw/web/shopify_full.png").convert("RGB")
card = full.crop((1090, 4900, 1852, 5596))
bg = card.getpixel((8, 8))
s = H / card.height
card = card.resize((int(card.width * s), H), Image.LANCZOS)
screen = Image.new("RGB", (W, H), bg)
screen.paste(card, ((W - card.width) // 2, 0))
out = Image.fromarray(lap.astype(np.uint8))
mask = Image.fromarray((green * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3))
full_screen = Image.new("RGB", out.size)
full_screen.paste(screen, (x0, y0))
out.paste(full_screen, (0, 0), mask)
out.save(f"{run}/raw/art/cut/laptop_shopify.png")
print("screen", x0, y0, W, H, "green px", int(green.sum()))
