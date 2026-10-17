---
id: P023
name: Habit ring question
status: draft
type: slideshow
visual_class: other:habit-ring-card
confidence: Low
sources:
- '7685559890898881800'
creators:
- mentalapp
created: '2026-10-14'
updated: '2026-10-14'
summary: A single-image "why does today feel <state>?" card, a glowing centre figure and a thin 2-line question ringed by 14 labelled cut-outs (photo objects, meme cut-outs, flat pictograms) that list the habits behind the good day, with the brand's own app icon slipped in as one habit labelled "(check bio)".
---

# P023 – Habit ring question

## 1. Source
- https://www.tiktok.com/@mentalapp/photo/7685559890898881800 (@mentalapp, posted 2026-09-15, collected 2026-10-14). One photo-mode slide. `fetch.py` only got the audio; the slide was saved from the public post page.

## 2. Summary
A single-image "why does today feel <state>?" card: a glowing centre figure and a thin 2-line question, ringed by 14 labelled cut-outs that list the habits behind the good day. The brand's own app icon is one of the habits, labelled with what it does + "(check bio)".

## 3. Best for
- A niche's "perfect day" (founders, students, gym people, creators): recognition and saves come from "i do that" and "i should do that".
- A soft product plug: the product is one habit among 14, never the subject.
- Not for explaining anything; each item is 1 to 3 words.

## 4. Structure
1 slide, 4:5.

| Zone | What sits there |
|---|---|
| Centre | A glowing, ethereal figure (the "state"), with the 2-line question under it and a small grey handle line |
| Top row (4) | Habits, left to right; one is a meme cut-out |
| Left column (3), right column (3) | Habits |
| Bottom row (4) | The brand's app icon first (bottom-left), then habits; one is a meme cut-out |

Item mix (that mix is the look, keep it): about 6 photo objects (food, drink, nature, gear), 2 meme cut-outs (a weird creature, a film-still person), 4 flat black pictograms (an icon-font look, one with a red prohibition sign), 1 element-tile style text icon or similar, 1 app icon.

## 5. Product slot
Bottom-left. The brand's real app icon or logo (never generated), label `<what the product does>` on line 1 and `(check bio)` on line 2. The caption points to the bio. No other brand mention on the card.

## 6. Proof device
None.

## 7. Series structure
Single post. Repeats well per identity or per state ("feel unreal", "feel so productive").

## 8. Video timing (videos only)
n/a.

## 9. Hook formula(s)
- `why does today feel <state>?` Mechanic: **mystery recipe**. The question sells a feeling and the ring is the secret recipe; the viewer checks which habits they already have.
- "why does today feel" is the trend phrase and may stay word for word; the state word must be new.
- Evidence: source title "why does today / feel unreal?".

## 10. Slide text rules
- Title 2 lines, 4 to 6 words, ends with "?". Labels 1 to 3 words, 1 or 2 lines, numbers welcome ("0", "10k", "7h+"). Product label ends "(check bio)".
- All lowercase (real brand names keep capitals), no dashes, colons or semicolons, no emoji on the card.

## 11. Visual style
- Canvas 1080 x 1350, flat pale sage #ebf1ea.
- Type: one thin neo-grotesk for everything (Helvetica Neue Light look; Inter at weight 300 with tight tracking), near-black #111. Title about 6% per line, tight leading, centred at y 60 to 66. Labels about 3.3% (cap-to-baseline), centred under each item. Handle 1.6% grey #9a9a9a under the title.
- Ring boxes in the source (% of frame, items): top row y 2 to 15 at x 5, 32, 58, 80 (w 15 to 18); left column x 6 to 22 at y 27, 46, 65; right column x 79 to 95 at y 27, 48, 67; bottom row y 82 to 93 at x 7, 31, 56, 80. Labels sit 1% under each item.
- Don't keep those exact columns: on a flat pale card they land inside the near-duplicate line on dhash. Re-space the ring (run-01: 5 top, 2 + 2 sides, 5 bottom) and run `originality.py`.
- Centre figure box about [38, 22, 26, 32]: a translucent glowing person, a single cold colour.
- Items look collected, not generated: sharp stock-photo objects, low-res film-still meme people and creatures, crisp icon-font pictograms. Avoid a uniform AI render style across items.
- Renderer: `tools/ringcard.py`.

## 12. Caption formula and hashtag pattern
- One deadpan line that refuses to explain and points to the bio (source: "the reason is, check bio instead"), then 5 hashtags (brand-ish, niche trend word, mood, routine, broad topic).

## 13. Performance context
394,400 views, 46,300 likes, 12,479 saves (3.2%), 1,893 shares (0.5%), 85 comments (post.json, 2026-10-14). For reference only.

## 14. Do / Don't
- Do: mix photo, meme and pictogram items; keep the deadpan numbers; make the brand slot look like every other item.
- Do: draw pictograms and the app tile in code; generate photo objects and meme people separately (people on green, film grade), prompts ending "no text, no letters, no numbers, no logos".
- Don't: copy the source's habits word for word, its glowing figure's pose and colour, or its meme characters. Never use a real meme photo or a known cartoon character (fictional film-still people only).

## 15. Confidence
Low: one post. The ring layout and item mix are clear; how much the meme items drive the saves is a guess.

## Evidence: format fingerprint
Nearest pillar is P019 layout B (4 of 7: structure, camera and motion, pacing, audio), but the hook mechanic differs. See `content-bank/_sources/mentalapp/grouping.md`.

## Runs
| Run | Topic | Verdict |
|---|---|---|
| [run-01](runs/run-01_2026-10-14_amplify-founder-vibe-coder-day/) | founder and vibe coder day, Amplify logo in the brand slot, soft caption | pending |
| [run-02](runs/run-02_2026-10-14_amplify-founder-4-colours/) | run-01 reworked: 4 top, 5 per side, 8h+ sleep for the duck, title above the figure; sage, white, blue and orange cards | pending |
| [run-03](runs/run-03_2026-10-14_amplify-founder-full-ring-4-co/) | full ring (4 top, 3 per side, 4 bottom), title right under the figure; sage, white, blue and orange cards | pending |
