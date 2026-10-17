# P018 · run 01 · Willow · "every freckle here is fake"

**Mode:** brand (Willow's full profile). Caption style **none** (no brand file for Amplify exists yet; see the end). Pillar = format: 6 slides, a hook macro, one ordinary selfie, three silent skin macros, a CTA macro. Persona = the face, freckles, moles, iris, wardrobe and her Bristol street.

## How pillar and persona combine
- The source's red hood becomes Willow's rust-orange chunky knit jumper (her own wardrobe, "errands and out" #4): the colour accent at the edges of the macros that ties the slides into one shoot.
- The source's porch becomes her terraced street on an overcast afternoon (her place, flat grey light like the source's shade).
- Macro order changed and built around her signature details: eye with amber flecks (hook) → selfie → lips → nose bump in profile → the two cheek moles → forehead and one brow (CTA). The source went lips → selfie → eye → nose → cheek → brows.

## Hook options (mechanic: reveal-by-claim, experience + disbelief)
Overlap measured in code against every word of the source post (hook and caption).
| Option | Overlap |
|---|---|
| **A (used)** `every freckle here is **fake**` | 20% (shares "is"), content words 0% |
| B `this is **ai**` | 100%: the formula phrase itself (trend wording, allowed by the skill rule) |
| C `not one freckle here is **real**` | 50% raw / 25% content ("not", "is", "real" are in the source caption), so "review" |

## Slides
| # | Role | Visual | Text (drawn in code, `overlay.py --style clean`) |
|---|------|--------|------|
| 1 | Hook | Extreme macro of her right eye: amber-flecked brown iris, window reflection, lashes, freckles under the eye, brow tail at the top | `every freckle here is **fake**`, one line, in the under-eye shadow just below the lashes (contrast 3.33) |
| 2 | Context | Selfie (term 1, no phone in shot), her terraced street, overcast, rust jumper, tucking hair behind her left ear, calm direct look | none |
| 3 | Proof | Extreme macro of her lips, relaxed and slightly parted, dry lines, lip balm sheen, peach fuzz above | none |
| 4 | Proof | Nose in profile from below: the bump, pores, freckles, redness at the nostril, eye soft at the top | none |
| 5 | Proof | Her left cheek almost abstract: pores, freckles, peach fuzz in side light, the two small moles, a hair strand, rust knit soft at the bottom | none |
| 6 | CTA | Forehead and one brow, hairline at the top, jumper pulled up over her nose | `would she fool **you** / be honest` (the first CTA, `comment yes or no`, shared 62% of its words with the source and failed) |

## Caption (`caption.json` → `caption.txt`, style none)
Manifesto in the pillar's voice (claim → why skin reads as real → what a render smooths away → what actually matters → question, ending `real or not, tell me in the comments 👇`). No hashtags (the source used none). `caption.py check`: PASS.

## Posting
- TikTok **AI-generated content label ON** (Willow is fictional, and the post is about that).
- Sound: pick a trending instrumental beat in TikTok (the source used "Thewayyouare", BYDKA BEATS).
- Time: the source posted on a Tuesday at 23:00 Manila time (15:00 UTC); one post is not evidence of a best time.

## Production
1. Refs on every image: `personas/willow/refs/real_face.png`, `sheet_real.png`; macros add `closeups/skin_macro.jpg` + `light/window_soft.jpg`; the selfie adds `rooms/street.jpg` + `light/overcast_street.jpg`.
2. Nano Banana Pro (`nbp`, 2K, 9:16), prompts in `raw/prompts.py` (identity lines + realism lines + macro framing + shot; every prompt ends "no text, no letters, no numbers, no logos").
3. v2 macro prompts (`prompt2`) say what is NOT in the frame, which fixed the half-face framing of v1. Look at every image at full size (plastic skin, repeated pores, extra moles, wrong eye colour).
4. `raw/compose.py`: 9:16 crop (lips 0.72, nose and cheek 0.86 of the still, no upscaling), exposure matched to the source's measured brightness (slides 1, 2, 5), then `overlay.py --phone 0.5 --style clean`, text on slides 1 and 6.
5. Slide records → `originality.py`.

## For an Amplify-branded version
There is no `brands/amplify.md`, so this run sells nothing (style none). The source's own CTA is a comment keyword for an AI-influencer offer; with a brand file the CTA slide becomes `comment **[keyword]** …` and the caption a soft or hard sell.
