import sys
from PIL import Image
R = sys.argv[1]
ims = [Image.open(f'{R}/output/slide{i}.png').convert('RGB').resize((432, 540)) for i in range(1, 8)]
sh = Image.new('RGB', (432 * 4, 540 * 2), 'white')
for i, im in enumerate(ims):
    sh.paste(im, ((i % 4) * 432, (i // 4) * 540))
sh.save(f'{R}/raw/_render_sheet.jpg', quality=88)
