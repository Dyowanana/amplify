# Review · P017 run-01 · Willow × Bolt Pharmacy

## 7-point format check (against P017)
| Point | Match | Note |
|---|---|---|
| Structure | ✔ | 5 slides: hook grid → swap grid → fix grid → explainer with plug → photo closer (the pillar's 5-slide variant) |
| Hook | ✔ | serif problem headline with italic payoff + grey reframing sub over a 6-object grid; mechanic: reassuring reframe |
| Camera & motion | ✔ | flat tinted card, photoreal cut-outs with soft shadows; warm lifestyle photo closer |
| Pacing | ✔ | 13 to 14 short text items per grid; explainer 58 words; closer 2 lines |
| Text overlay | ✔ | Playfair Display + italic payoff, Inter labels and grey reasons, explainer with accent dots; colours swapped to Bolt's |
| Audio | n/a | music to be picked in TikTok |
| Arc | ✔ (changed on purpose) | recognition → reassurance → swaps → habits → mechanism → service line → calm closer; the testimonial and body-outcome payoff are replaced (see below) |

## Measured checks
- `originality.py`: **PASS**. Raw word overlap per slide 22 / 24 / 23 / 24 / 27% (all under 30%), content-word overlap 11 to 15%, longest shared run 3 words ("water not fat", the pillar's reframe formula). Hook overlap 25% (only "why"). Images: closest source slide 11 bits on a 64-bit hash (near-duplicate is 10 or less).
  - The image hash started at 9 to 10 bits on three slides: light cards in the same grid layout hash close even with no source pixels. Fixed by enlarging the objects, reordering slides 1 and 2 and moving the explainer text lower; the margin is still thin (11 bits), so re-run the check after any edit.
- `caption.py check` (hard, brands/boltpharmacy.md): **PASS**, 434 characters, 5 hashtags, disclosure last. The first ~100 characters before "more" carry the hook, not the brand.
- `measure.py check --record` on all 5 slides: 0 box problems. Contrast: headings 15.2:1, labels 15.2:1, grey reasons 5.0:1 (after darkening from 3.8:1), photo headline 10.1:1, photo subline 16.3:1.
- `doctor.py` after adding `tools/gridcards.py`: 0 failed; the P006 test render is unchanged ("close", as before).

## Brand and compliance
- No medicine names, no pens or packs, no weight or body-outcome claims, no before/after, no "lose weight" wording; `never_say` list clear (checked by `caption.py`).
- Claims used are only from the brand file's allowed list: online eligibility check, no in-person appointment, UK clinicians review every case.
- The source's first-person testimonial ("the app kept me going") was replaced with a factual service line: a fictional person can't vouch for a regulated healthcare service.
- The source's joke "tips" (comment bait) were left out; every tip here is true and general. Physiology lines kept deliberately soft ("usually", "throws off", "shift"): salt, carbohydrate storage, alcohol, muscle repair, the menstrual cycle and long sitting all affect short-term water weight.
- **Real, regulated brand:** the caption and slides need Bolt Pharmacy's own compliance sign-off before posting (ASA/CAP, MHRA). These checks are word-level only, not a legal review.

## Known limits
- The closer is a single AI photo of Willow (one take). Side by side with `refs/real_face.png`: hair, freckles, gold hoops, slightly uneven teeth and the moles on her left cheek match; in the full laugh her face reads a little longer and older than the reference. Fine at phone size; a second take is about $0.09 if the owner wants a closer match.
- "uk" is lowercase on the slides and in the caption to follow the lowercase rule; change to "UK" if the brand prefers.
- `gridcards.py` is new (not on the owner's machine yet): `manifest.py compare` will list it as an extra tool until the owner adds it.

## Verdict
Pending the owner's review. Tester ratings: pending.
