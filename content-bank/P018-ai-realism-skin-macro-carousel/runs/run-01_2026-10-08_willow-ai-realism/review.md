# Review · P018 run 01 · Willow · "every freckle here is fake"

## 7-point format check (against the pillar)
| Point | Pillar | This run | Match |
|---|---|---|---|
| Structure | 6 slides: hook macro → selfie → 3 silent macros → CTA macro | same, with new features (eye → selfie → lips → nose → cheek → brow) | yes |
| Hook | reveal-by-claim over the most convincing macro, one bold word | `every freckle here is **fake**` over the eye macro | yes |
| Camera & motion | humans: selfie (term 1) + extreme phone macros, flat daylight | same; overcast street selfie, window-light macros | yes |
| Pacing | text on 2 of 6 slides only | text on slides 1 and 6 only | yes |
| Text overlay | clean white geometric sans, light + one bold word, centred on the subject, no box/outline | Inter 300 + 700, centred on the subject, faint shadow (`overlay.py --style clean`, new) | yes (font is the closest local match to Montserrat) |
| Audio | trending instrumental | chosen in TikTok at posting | n/a until posting |
| Arc | claim → whole person → escalating proof → action | same | yes |

## Measured checks
- **Originality** (`output/originality.json`): **PASS**. Hook overlap 20% (shares "is"). Slide 1 raw overlap 20%, slide 6 17% ("you"), content-word overlap 0% on every slide, longest shared run 1 word. Closest image to any source slide is 22 bits away (near-duplicate threshold 10). New person (Willow), new outfit (rust knit, not a red hood), new place (Bristol street, her window), new macro order.
- **Caption** (`caption_check.json`): **PASS**, style none, 495 characters, 0 hashtags, no banned punctuation, no capitals.
- **Text boxes** (`output/records/check_slide1`, `check_slide6`): 0 box problems. Contrast 3.33 (slide 1) and 3.21 (slide 6), in the source's own range (3.14 to 4.08). Slide 1's text touches the uncalibrated right-button zone by 7.1% (a hint only).
- **Tone against the source** (`output/visual_vs_source.json`, both at 1080×1920): brightness within 2.5 points on slides 1, 3, 4, 5 (slide 1 was 61.9 and was brought to 51 in code), saturation within 8 points. Ours is sharper (sharpness 88 to 466 vs 63 to 207) and grainier (noise 0.7 to 2.3 vs 0.2 to 0.3): the source is a softened, recompressed upload. Left that way on purpose, since the texture is the point; TikTok's own compression will soften it.

## What was rejected (kept in `raw/rejected/`)
- v1 eye, lips, nose: half-face close-ups, not macros. Fix: the prompt now says what is **not** in the frame ("the nose, the mouth and the edge of the face are not in the frame").
- v2 temple: two brows and two eyes on one side, hair drawn grey. Replaced by a single brow and forehead shot.
- v1 cheek was stopped mid-run (billed, not downloaded).

## Look by eye (every image at full size)
- Identity holds: warm brown iris with amber flecks, freckles across the nose and cheeks, gold hoop, dark wavy hair. No extra dark spots.
- Slide 4 has a small raised spot on the nose bridge, and the lower cheek mole on slide 5 is slightly raised where the persona file says flat. Both read as real skin. Re-roll if you want strict persona consistency.
- Slide 6: she has the jumper pulled up over her nose. It reads as a natural candid gesture and isn't in the source.

## Models used
Nano Banana Pro (`nbp`, 2K, 9:16) only. 11 calls, **198 credits ($0.99)**. All on the approved list.

## Known limits
- One source post, so the pillar is Low confidence.
- No Amplify brand file, so the post sells nothing (caption none). A branded version needs `brands/amplify.md` (claims, CTA keyword, never-say list).
- Turn on TikTok's AI-generated label when posting.

## Tester ratings
Pending.

## Owner verdict
Pending.
