# P020 learnings

Feedback from runs, turned into general rules.

## 2026-10-13 · owner feedback on run-01
- **People must look like classic meme film stills, not AI.** run-01's people (clean, evenly lit, posed on green) read as AI. What fixed it in run-02/run-03: prompt for a black and white still from a 1990s or early 2000s comedy film with hard light, grain, a candid exaggerated meme expression, and period wardrobe and props (CRT monitor, flip phones, Hawaiian shirt, power suit, tuxedo and chips). Then `"grade": "film"` in `memecards.py`. Real meme photos stay out (fictional people only).
- **No empty bottom corners.** A cutout placed bottom left with a blank bottom right looks awkward. Generate wide (3:2, arms and props spread), let `memecards.py` fill the width from just under the text, and let the frame edges crop the art. Only the cover keeps a free corner, for the swipe arrow.
- **Halftone on dark clothes goes solid.** Lift the mid-tones before the dot screen (`halftone_gamma` 0.6, the default).
- A different card colour (butter yellow #efe1b4) keeps the format; the black and white cutouts and white outline still read.
