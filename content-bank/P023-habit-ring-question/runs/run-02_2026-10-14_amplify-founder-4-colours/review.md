# Review · P023 run-02

## 7-point format check
Same as run-01, except for the ring: 4 top and 5 per side with no bottom row (the owner's choice), and the title above the figure. Structure, hook, item mix, pacing (31 words), text style, audio and arc all match the pillar.

## Checks (numbers from code)
- `originality.py`: raw word overlap 24%, content words 18% (under 30%). Longest shared run is 4 words ("why does today feel") and hook overlap is 80%. Both are the trend's formula phrase, kept on purpose. "sleep" is now a shared word ("7h+ sleep" in the source, "8h+ sleep" here), as the owner asked.
- Image hash: 11 bits for sage and white, 25 bits for blue and orange (near-duplicate is 10 or less). Sage and white only just pass. Their dhash is close to the source because a pale card with a 5-per-side ring has the source's skeleton; phash is 32, so they don't look alike.
- `caption.py check`: PASS (soft, 289 characters, disclosure last).
- Text contrast (`measure.py check --record`): sage 16.5, white 18.9, blue 10.0, orange 8.0, all good (4.5+).
- On the blue and orange cards the glow's white core is now drawn opaque (`ringcard.py` fills the figure's silhouette), so it still glows instead of showing the card colour through.

## Brand
Same as run-01: the real Amplify logo file, a claim from the allowed list, nothing from `never_say`, no other brand marks.

## Tester ratings
Pending.

## Owner verdict
Pending.
