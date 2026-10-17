# Review · P023 run-01

## 7-point format check
| Point | Source | Ours | Match |
|---|---|---|---|
| Structure | 1 slide, 14 labelled items ringed round a glowing figure and a 2-line question, brand app as one item | same, ring re-spaced as 5 top, 2 + 2 sides, 5 bottom | yes |
| Hook | why does today feel unreal? | why does today feel illegal? | yes (mechanic and formula phrase) |
| Camera and motion | designed card, mixed photo, meme and pictogram cut-outs | same mix | yes |
| Pacing | about 30 words | 32 words | yes |
| Text overlay | thin grotesk, lowercase, black, centred labels | Inter 300, tight tracking, lowercase | yes |
| Audio | music bed | music bed, picked in TikTok | yes |
| Arc | curiosity, then the recipe, brand as one habit, caption to bio | same | yes |

## Checks (numbers from code)
- `originality.py`: raw word overlap 22% (under 30%), content words 15%. Longest shared run is 4 words ("why does today feel") and hook overlap is 80%. Both come from the trend's formula phrase, kept on purpose (skill rule: the formula phrase may stay, the state word is new). Lower-overlap hooks are in `package.md`. Image hash distance 24 bits (pass; near-duplicate is 10 or less).
- The first layout (the source's 4-column rows) scored 4 bits on dhash, a near-duplicate. Re-spaced to 5-column top and bottom rows: 24.
- `caption.py check`: PASS (soft, 289 characters, 5 hashtags, disclosure last).
- `measure.py check --record`: every text block has contrast 16.5 (good). Boxes in `raw/boxcheck/slide1_boxcheck.jpg` sit on their elements.
- Punctuation: no dashes, colons or semicolons on the card ("lofi" instead of "lo-fi").

## Brand
- Amplify's real logo file, not generated. The label "automated content" stays within the allowed claims (makes posts in formats that work). Nothing about posting or scheduling for you; nothing from `never_say`.
- No real brand marks: the laptop has a plain lid, the keyboard has blank keys, the matcha cup and headphones are unbranded.
- The meme man and the cat are generated, not real meme photos (likeness rule). The source's cartoon character and meme photo are not used.

## Known limits
- No handle under the title (the brand file has none yet).
- Confidence Low: one source post.

## Tester ratings
Pending.

## Owner verdict
Pending.
