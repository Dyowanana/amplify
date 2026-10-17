---
id: P020
name: Founder notes with meme cutouts
status: draft
type: slideshow
visual_class: other:meme-cutout-text-card
confidence: Low
sources:
- '7678443671007530262'
creators:
- founderscale
created: '2026-10-13'
updated: '2026-10-13'
summary: A 7-slide founder-lessons carousel on plain warm grey cards, a bold lowercase heading and short monospace paragraphs over a black and white meme-energy cutout of a person, moving from a pov reality-check hook through "the game changed", numbers, the main lesson and a next step to a first-person conclusion with a bio-link CTA.
---

# P020 – Founder notes with meme cutouts

## 1. Source
- https://www.tiktok.com/@founderscale/photo/7678443671007530262 (@founderscale, posted 2026-08-26, collected 2026-10-13). 7 photo-mode slides, 1080 x 1350. Slides saved from the public post page (`fetch.py` got the sound only).

## 2. Summary
A 7-slide founder-lessons carousel on plain warm grey cards, a bold lowercase heading and short monospace paragraphs over a black and white meme-energy cutout of a person, moving from a pov reality-check hook through "the game changed", numbers, the main lesson and a next step to a first-person conclusion with a bio-link CTA.

## 3. Best for
- Founder, builder, creator and marketing advice where the audience saves posts (save rate 3.7% on the source).
- A product the author uses themselves: the post reads like private notes, so a first-person tool mention fits.
- Not for visual products or anything that needs a demo; it's a text post.

## 4. Structure
7 slides.

| # | Role | What happens | Text on screen (pattern) |
|---|------|--------------|---------------------------|
| 1 | Hook | One bold line, swipe arrow bottom right, a deadpan cutout bottom left | `pov <a builder's reality in <year>>` |
| 2 | The game changed | What used to be the advantage, and why it isn't now | heading + 3 short paragraphs |
| 3 | Proof | One numbers block or one concrete observation the author can back up (source in brackets) | heading + 3 to 4 short paragraphs |
| 4 | Main lesson | The order that works, with a soft bio-link line in brackets | heading + 4 paragraphs + `(link in bio …)` |
| 5 | Second lesson | A reframe of a fear or a habit | heading + 3 to 5 short paragraphs |
| 6 | Next step | One concrete action, often naming one tool | heading + 3 to 4 paragraphs |
| 7 | Conclusion | Centred recap, "i do this myself" credibility line, CTA | heading + 3 to 4 centred paragraphs |

## 5. Product slot
In the text, first person, as one of the author's own tools: a bracketed `(link in bio …)` line at the end of the main lesson (slide 4), a named tool in the next step (slide 6), and the CTA on the conclusion (slide 7). No logo, no screenshot.

## 6. Proof device
One numbers slide with the source named in brackets, and a first-person founder line on the conclusion. Every number must be true and sourced (a public report, or the author's own measured data).

## 7. Series structure
Single post; the source teases a follow-up on slide 6 ("in my next post …").

## 8. Video timing (videos only)
n/a.

## 9. Hook formula(s)
- `pov: reality of building a <thing> <year>`. Mechanic: **reality check aimed at a builder identity** (insider gap). "pov" is the trend word and stays; the owner's rule removes the colon (`pov <…>`). Everything after it must be new.
- Same register: `pov you <did the builder thing> and <the painful reality>`.

## 10. Slide text rules
- Heading 2 to 4 words, body 45 to 75 words in 3 to 5 paragraphs, hard line breaks at about 40 to 45 characters, a blank line between paragraphs.
- Short declaratives, calm insider voice, first and second person. No hype words, no emoji.
- Lowercase (owner rule); brand names keep their capitals. No dashes, colons or semicolons (the source uses "pov:" and an em dash; replications drop both). Brackets and full stops are fine.

## 11. Visual style
- Class: other:meme-cutout-text-card.
- Canvas 1080 x 1350, flat warm light grey #e4e3df, no texture.
- Heading: bold grotesk, #111; the source's Roboto Bold measures 2.9% of frame height, Inter Bold matches it at 2.7%. Body: monospace (DejaVu Sans Mono in `assets/fonts` for Space Mono), #111, 1.95%, line pitch 2.3%.
- Left layout (slides 1 to 6): text left-aligned at x 12.5 to 13.5%, heading at y 11 to 19%, body starting 6 to 8% below it. Centre layout (conclusion): heading and body centred on the frame.
- Cutout: one person per slide, black and white, waist up, cropped by the bottom edge (sometimes the left edge), thick white sticker outline (about 1.3% of the width), height 26 to 51% of the frame. Cover and conclusion in a coarse halftone dot screen, the rest plain grainy black and white. Each person has a strong meme pose that tags the slide's mood (deadpan, pointing, scheming, relaxed, dancing, focused).
- Swipe arrow (thin black right arrow) bottom right of the cover only.
- **Owner rules (2026-10-13):** body-slide cutouts fill the bottom width with no blank corner (`memecards.py` fill mode, the default); the cover keeps art left and the arrow in the free corner. People look like classic 90s/2000s film stills, not clean AI renders: the film-still prompt in run-02/run-03 `raw/art/prompts.tsv`, generated at 3:2 with arms and props spread wide, plus `"grade": "film"`.
- Renderer: `tools/memecards.py` (text and arrow drawn in code; people generated on green, keyed, halftoned and outlined in code).

## 12. Caption formula and hashtag pattern
- One line that restates the hook as advice ("read this before you …"), then 5 hashtags: role (developer), topic (saas), growth, a second role, fyp.

## 13. Performance context
27,200 views, 1,424 likes, 1,016 saves (3.7%), 118 shares (0.4%), 14 comments. For reference only.

## 14. Do / Don't
- Do: keep each paragraph one idea; make slide 3 a real number or a measured observation.
- Do: generate original people (`kie.py image --model gpt25s`), on a flat green background, prompts ending "no text, no letters, no numbers, no logos".
- Don't: use film stills or any real person's likeness (the source cuts out recognisable actors); don't redraw a famous scene's costume and pose.
- Don't: copy the source's stats, tool or wording.

## 15. Confidence
Low: one post from one account.

## Evidence: format fingerprint
New format; nearest pillar is P006 at 2 of 7. See `content-bank/_sources/founderscale/grouping.md`.

## Runs
| Run | Topic | Verdict |
|---|---|---|
| [run-01](runs/run-01_2026-10-13_amplify-distribution-is-the-ga/) | Amplify, distribution is the game, soft sell | owner: people look AI, empty bottom corners (2026-10-13); re-rendered with the fill layout, first render kept in `raw/output_v1/` |
| [run-02](runs/run-02_2026-10-13_amplify-same-text-classic-phot/) | run-01 text, butter-yellow card, classic film-still people on slides 2, 4, 5, 7, cutouts fill the bottom | pending |
| [run-03](runs/run-03_2026-10-13_amplify-closer-to-source-text/) | source hook and slide 2 title copied on request, new body, all new classic people | pending |
| [run-04](runs/run-04_2026-10-13_amplify-closer-to-source-retro/) | run-03 in retro orange #ee7f3b | pending |
