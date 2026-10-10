# P019 run-01 · founder essentials · 5 outfit versions (no brand)

Made for the Amplify account, caption style **none** (no brand, logo or link anywhere). Format from P019 (@nicodunlap "Builder Essentials"); no persona file (a starter-pack board has no person in it).

## How it maps to the source
| Slot | Source | This run |
|---|---|---|
| Title | "Builder Essentials" | **founder essentials** (lowercase, owner rule) |
| Outfit (varies) | black hoodie, black shorts | top, bottom and shoes per version (below) |
| Work tool | branded laptop | silver laptop, no logo |
| Fuel | espresso, branded mineral water | iced oat latte, frosted sparkling water with no label |
| Gear | keyboard, branded fitness band | over-ear headphones, round smartwatch |
| Grind widget | an AI tool's "need more usage" top-up modal | code-drawn "you've hit your usage limit" modal, wait it out vs upgrade plan |
| Middle widget | an AI coding tool's app icon | code-drawn phone notification "new payment / you received $49.00" |
| Dream widget | MRR +343.8% chart | code-drawn mrr +212.6%, $8,940.12, rising green line |
| Layout | outfit stacked on the left | outfit stacked on the **right** (mirrored, see review) |

## Hook (mechanic labelled)
"founder essentials". Mechanic: **identity starter pack**. "essentials" is the trend's formula word, kept word for word; "founder" is new.

## The 5 versions (only the outfit changes)
| File | For | Top | Bottom | Shoes |
|---|---|---|---|---|
| `output/guy-1_knit-and-trousers.png` | guys | oatmeal chunky crewneck knit | charcoal drawstring trousers | white leather low tops |
| `output/guy-2_fleece-and-shorts.png` | guys | dusty blue half-zip fleece | stone chino shorts | grey suede runners |
| `output/girl-1_sweatshirt-and-flares.png` | girls | heather grey oversized sweatshirt | black flared yoga leggings | chunky cream dad sneakers |
| `output/girl-2_white-shirt-and-jeans.png` | girls | white oversized button-down | light wash wide-leg jeans | black ballet flats |
| `output/girl-3_sage-knit-set.png` | girls | sage ribbed knit cardigan | matching sage wide-leg pants | fluffy cream shearling slides |

All five side by side: `all_5_versions.jpg`.

## Caption (none) · `caption.txt`
tag the founder who owns every single thing on here 😭

#founder #buildinpublic #startuplife #indiehacker

## Posting
- Photo mode, one image per post, a trending sound picked in TikTok. Switch on TikTok's AI-generated label (the items are AI images).
- Post as a set a day or more apart, or test a guy and a girl version on the same day to see which audience saves more.

## Production
20 items with `kie.py image --model gpt25s --resolution 1K --aspect 1:1` (prompts in `raw/art/objects.tsv`), 3 redone (see review). Board: `tools/flatlay.py spec.json` (new renderer: title and the three widgets drawn in code, items multiply-blended on white).

## Cost
138 credits ($0.69): 23 GPT Image 2.5 Sunburst calls at 6 credits. Itemised in `costs.json`.
