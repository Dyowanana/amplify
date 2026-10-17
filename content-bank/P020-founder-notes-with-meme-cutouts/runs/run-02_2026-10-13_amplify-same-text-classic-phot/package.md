# P020 · run 02 · amplify same text classic photos

Same text and caption as run-01. Changes from the owner's feedback (2026-10-13):
- **New card colour:** butter yellow #efe1b4 (was warm grey #e4e3df).
- **Classic meme-style people on slides 2, 4, 5 and 7.** The owner said run-01's people "look like ai" and asked for real meme photos. Real meme photos are real people (actors in film stills), which the owner rules forbid ("fictional people only"). So these are new generated people prompted as black and white 90s/2000s comedy film stills, with exaggerated meme expressions and period props. In code they get a film grade (old DVD-frame softness, a contrast S-curve, JPEG grit, grain). Slides 1, 3 and 6 reuse run-01's art with the same grade.
- **No awkward empty space at the bottom** (owner rule, 2026-10-13). Cutouts fill the width from just under the text to the bottom edge (`memecards.py` fill mode). The cover keeps the source's layout: art left, swipe arrow bottom right.

| # | Heading | Person |
|---|---|---|
| 1 | pov you launched and got zero signups | run-01 hoodie guy at a laptop, halftone |
| 2 | shipping is the easy part | heavyset office worker on a beige CRT monitor, cheesy double thumbs up (new) |
| 3 | distribution is the game | run-01 man tapping his temple |
| 4 | let ai make the content | man in a Hawaiian shirt and sunglasses on a beach lounger, laptop on his belly, drink (new) |
| 5 | post twice a day | woman in a boxy blazer shouting, a flip phone held up in each hand (new) |
| 6 | kill what flops | run-01 man tossing a crumpled paper |
| 7 | the short version | woman in a 90s power suit spread back in an executive chair, halftone (new) |

Caption: same as run-01 (`caption.txt`, soft, PASS).

Production: 4 × `kie.py image --model gpt25s --resolution 2K --aspect 3:2`, prompts in `raw/art/prompts.tsv` (40 credits, $0.20), all first take. Render: `tools/memecards.py spec.json`.
Posting: as run-01 (photo carousel, a trending low-key track, the AI label and commercial content toggle on).
