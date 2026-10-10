---
id: P019
name: Essentials flat-lay
status: approved
type: slideshow
visual_class: other:essentials-flatlay
confidence: Low
sources:
- '7670706992230485261'
creators:
- nicodunlap
created: '2026-10-10'
updated: '2026-10-10'
summary: A single-image starter pack where a two-word "<identity> essentials" title sits over a white flat-lay of cut-out items, an outfit stacked on the left and gadgets, drinks and two or three in-joke app widgets around it, so viewers tag the people who are that identity.
---

# P019 – Essentials flat-lay

## 1. Source
- https://www.tiktok.com/@nicodunlap/photo/7670706992230485261 (@nicodunlap, posted 2026-08-06, collected 2026-10-10). One photo-mode slide.

## 2. Summary
A single-image starter pack where a two-word "<identity> essentials" title sits over a white flat-lay of cut-out items, an outfit stacked on the left and gadgets, drinks and two or three in-joke app widgets around it, so viewers tag the people who are that identity.

## 3. Best for
- Identity and lifestyle content for a niche audience (founders, builders, creators, students, gym people, nurses, remote workers). Saves and shares come from "this is literally me" and tagging.
- Variant series: the same board with only the outfit swapped (his and hers versions, seasons, cities) is cheap to make and posts as a set.
- Not for how-to, claims or anything that needs explaining. There is one line of designed text.

## 4. Structure
1 slide.

| # | Role | What happens | Text on screen (pattern, not the source's words) |
|---|------|--------------|---------------------------------------------------|
| 1 | Hook + payload | Title over a white board of 10 to 13 cut-out items. Outfit (top over bottom, footwear under) on the left as the anchor; 4 to 6 lifestyle objects and 2 to 3 app widgets in two loose columns on the right | `<identity> essentials` |

Item slots (fill all of them):
- **Outfit** (varies per version): top, bottom, footwear. The only slots that say who the person is.
- **Work tool**: laptop or equivalent (unbranded).
- **Fuel**: one hot or iced drink, one bottled drink.
- **Gear**: 1 to 2 objects of the identity (headphones, a wearable, a keyboard).
- **In-joke widgets**: 2 to 3 small app UI snippets drawn in code. One shows the grind (a usage limit, a top-up, a deploy log), one shows the dream outcome going up (revenue, followers). These carry the humour.

## 5. Product slot
None in the source (real brands only appear as props). For a brand run, the product takes one gear or widget slot as a real screenshot or a real product photo (never generated), and the caption carries the sell.

## 6. Proof device
App widgets as in-joke proof of the lifestyle (a usage top-up, a revenue chart). Draw them in code with invented, plausible numbers. Never copy a real app's UI or a real brand's icon.

## 7. Series structure
Single post. Works as a set of variants: same board, outfit swapped, posted a day or more apart.

## 8. Video timing (videos only)
n/a.

## 9. Hook formula(s)
- `<identity> essentials` (mechanic: **identity starter pack**, the viewer checks whether they belong). "essentials" is the trend word and stays word for word; the identity word must be new.
- Variants in the same register: `<identity> starter pack`, `<identity> uniform`.
- The pack is the real hook. The joke widgets must read in under a second.
- Evidence: the source title is "Builder Essentials".

## 10. Slide text rules
- Title only, 2 to 3 words, lowercase (owner rule; the source uses Title Case). No dashes, colons or semicolons.
- Widget text: short UI phrases in lowercase, numbers allowed, at most 6 words per line.
- No emoji on the board.

## 11. Visual style
- Class: other:essentials-flatlay (designed card made of product cut-outs + UI snippets).
- Canvas 1080 x 1350 (4:5), flat white #ffffff.
- Title: bold grotesk sans (Inter Bold for SF Pro Display Bold), near-black #111, centred, top-headline box about [17, 8, 66, 6].
- Items: realistic catalogue packshots, isolated on white, no visible shadows, mostly monochrome (black, grey, white, oatmeal) with one or two colour accents. Items never overlap; gutters 2 to 4% of the frame.
- Layout boxes (% of frame, from the source): outfit top [5, 18, 40, 37], bottom [10, 56, 30, 24], footwear [10, 82, 32, 12]; middle column work tool [42, 19, 28, 14], widget [52, 36, 40, 13], widget or object [50, 53, 18, 15], widget [50, 70, 20, 12], object [49, 84, 24, 10]; right column drink [75, 18, 19, 14], gear [76, 54, 20, 19], bottle [80, 76, 12, 19].
- The outfit column can sit on either side. Run-01 mirrors the source (outfit on the right) so the board stays well clear of the source on the image hash; keep that unless the items are very different in tone from the source's.
- Fixed across variants: title, layout, every non-outfit item. Varies: the outfit (and the identity word for a new identity).
- Renderer: `tools/flatlay.py` (title and widgets drawn in code, art multiply-blended on white).

## 12. Caption formula and hashtag pattern
- Source caption is hashtags only: 4 tags (tool, identity, aspiration, place).
- Write: an optional 1-line lowercase in-joke or tag ask, then 4 to 5 hashtags (identity, aspiration, niche tool or habit, a broad one).

## 13. Performance context
431,300 views, 52,100 likes, 10,949 saves (2.5%), 3,413 shares (0.8%), 165 comments. For reference only.

## 14. Do / Don't
- Do: keep the board airy and the items monochrome; make the outfit clearly the biggest thing; make the widgets the punchline.
- Do: generate each item separately on white (`kie.py image --model gpt25s --resolution 1K --aspect 1:1`), prompts ending "no text, no letters, no numbers, no logos".
- Don't: copy the source's brands (laptop logo, AI tool icon and modal, wearable, mineral water, designer waistband) or its widget text and numbers.
- Don't: draw any brand logo; don't put text in a generated image.

## 15. Confidence
Low: one source post. The layout and slots are clear; how far the joke widgets drive the saves is a guess.

## Evidence: format fingerprint
One post, so no comparison. Nearest existing pillar is P017 (object grid): it matches on camera and motion (cut-outs on a light card) and audio only (2 of 7). See `content-bank/_sources/nicodunlap/grouping.md`.

## Runs
| Run | Topic | Verdict |
|---|---|---|
| [run-01](runs/run-01_2026-10-10_founder-essentials-5-outfits/) | founder essentials, 2 guy and 3 girl outfits, no brand | pending |
