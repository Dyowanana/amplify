"""Upper-body crops of the people (the source's people icons are cropped, not full body) and a screen-first laptop."""
import sys
from PIL import Image
run = sys.argv[1]
cut = f"{run}/raw/art/cut"
def crop_top(name, frac, out):
    im = Image.open(f"{cut}/{name}.png").convert("RGB")
    im.crop((0, 0, im.width, int(im.height * frac))).save(f"{cut}/{out}.png")
crop_top("ugc", 0.50, "ugc_crop")
crop_top("guru", 0.47, "guru_crop")
crop_top("trench", 0.52, "trench_crop")
crop_top("skeleton", 0.80, "skeleton_crop")
crop_top("laptop_shopify", 0.70, "laptop_shopify_crop")
