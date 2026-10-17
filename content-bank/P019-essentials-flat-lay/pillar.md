---
id: P019
name: Essentials flat-lay
status: approved
type: slideshow
visual_class: other:essentials-flatlay
confidence: Medium
sources:
- '7670706992230485261'
- '7665200692289752333'
creators:
- nicodunlap
created: '2026-10-10'
updated: '2026-10-10'
summary: A single-image identity starter pack on white, either an "<identity> essentials" flat-lay (outfit stacked on one side, gadgets and in-joke app widgets around it) or a "peak <identity> purchases" ring of labelled items around a centre title, so viewers tag the people who are that identity.
---

# P019 – Essentials flat-lay

## 1. Source
- https://www.tiktok.com/@nicodunlap/photo/7670706992230485261 (@nicodunlap, posted 2026-08-06, collected 2026-10-10). One photo-mode slide. Layout A, flat-lay.
- https://www.tiktok.com/@nicodunlap/photo/7665200692289752333 (@nicodunlap, collected 2026-10-10). One photo-mode slide. Layout B, ring.

## 2. Summary
A single-image identity starter pack on white, either an "<identity> essentials" flat-lay (outfit stacked on one side, gadgets and in-joke app widgets around it) or a "peak <identity> purchases" ring of labelled items around a centre title, so viewers tag the people who are that identity.

## 3. Best for
- Identity and lifestyle content for a niche audience (founders, builders, creators, students, gym people, nurses, remote workers). Saves and shares come from "this is literally me" and tagging.
- Variant series: the same board with only the outfit swapped (his and hers versions, seasons, cities) is cheap to make and posts as a set.
- Not for how-to, claims or anything that needs explaining. There is one line of designed text.

## 4. Structure
1 slide.

| # | Role | What happens | Text on screen (pattern, not the source's words) |
|---|------|--------------|---------------------------------------------------|
| 1 | Hook + payload | Title over a white board of 10 to 13 cut-out items. Outfit (top over bottom, footwear under) on the left as the anchor; 4 to 6 lifestyle objects and 2 to 3 app widgets in two loose columns on the right | `<identity> essentials` |

| 1 (layout B) | Hook + payload | Centre title block (3 stacked lines + a grey `<tribe> edition` subline) ringed by 8 labelled items: 3 top, 1 left, 1 right, 3 bottom | `peak <identity> purchases` / `<tribe> edition`, and a 1 to 2 line label under each item |

Layout B slots: work tool, headphones, a text item (e.g. domain endings), two app icons (left and right, the product goes in one of them), fitness (gym gear, or pilates for a women's version), mic, desk. Labels are the object in plain words, sometimes with a joke adjective ("unused domains").

Layout A item slots (fill all of them):
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
- `<identity> essentials` (layout A) and `peak <identity> purchases` + `<tribe> edition` (layout B). Mechanic: **identity starter pack**, the viewer checks whether they belong.
- "essentials", "peak … purchases" and "edition" are the trend words and stay word for word; the identity word must be new.
- Variants in the same register: `<identity> starter pack`, `<identity> uniform`.
- The pack is the real hook. The joke widgets must read in under a second.
- Evidence: the source titles are "Builder Essentials" and "peak solopreneur purchases / builder edition".

## 10. Slide text rules
- Layout A: title only, 2 to 3 words. Layout B: 3-word title, 2-word edition line, 8 labels of 1 to 4 words. All lowercase (owner rule; the sources' labels use Title Case), real brand names keep their capitals. No dashes, colons or semicolons.
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
- Layout B (% of frame): centre title at y 47, 3 lines at 6% with tight leading, Inter Heavy (SF Pro Heavy look), grey #555 edition line at 2.3% under it. Ring boxes: text item [10, 14, 16, 12], work tool [36, 10, 28, 16], headphones [72, 11.5, 20, 15.5], left icon [4, 42, 16, 12], right icon [82, 43, 13, 10.5], fitness [7, 63, 25, 16], mic [40, 64, 20, 20], desk [66, 65.5, 28, 15]; labels Inter Semibold 2.2%, centred 1% under each box.
- Renderer: `tools/flatlay.py` (title, labels, text items, app icons and widgets drawn in code, art multiply-blended on white; a version can override the title).

## 12. Caption formula and hashtag pattern
- Source captions are hashtags only: 4 to 5 tags (identity, meme or aspiration, money, tool, place or trend).
- Write: an optional 1-line lowercase in-joke or tag ask, then 4 to 5 hashtags (identity, aspiration, niche tool or habit, a broad one).

## 13. Performance context
- Layout A: 431,300 views, 52,100 likes, 10,949 saves (2.5%), 3,413 shares (0.8%), 165 comments.
- Layout B: 84,900 views, 9,975 likes, 2,540 saves (3.0%), 441 shares (0.5%), 34 comments.
For reference only.

## 14. Do / Don't
- Do: keep the board airy and the items monochrome; make the outfit clearly the biggest thing; make the widgets the punchline.
- Do: generate each item separately on white (`kie.py image --model gpt25s --resolution 1K --aspect 1:1`), prompts ending "no text, no letters, no numbers, no logos".
- Don't: copy the source's brands (laptop logo, AI tool icon and modal, wearable, mineral water, designer waistband) or its widget text and numbers.
- Don't: draw any brand logo; don't put text in a generated image.

## 15. Confidence
Medium: two posts from one account, two layouts of the same idea. The slots are clear; how far the joke items drive the saves is a guess.

## Evidence: format fingerprint
The two posts match on 6 of 7 (structure, hook, camera and motion, pacing, audio, arc); text overlay differs (one title vs a centre block with item labels). Nearest other pillar is P017 (2 of 7). See `content-bank/_sources/nicodunlap/grouping.md`.

## Runs
| Run | Topic | Verdict |
|---|---|---|
| [run-01](runs/run-01_2026-10-10_founder-essentials-5-outfits/) | founder essentials, 2 guy and 3 girl outfits, no brand | pending |
| [run-02](runs/run-02_2026-10-10_creator-purchases-5-versions-a/) | layout B, peak creator purchases, Amplify logo, 2 guy and 3 girl versions, no caption | pending |
