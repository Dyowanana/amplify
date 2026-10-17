# P022 learnings

Feedback from runs, turned into general rules.

## From run-01 (owner feedback, 2026-10-14)
- **Two players, two looks.** The hands are two different people: different skin tone, sleeve colour and accessory per side. Generate one anchor per side and use it as the reference only for that side's other gestures.
- **Paper shows the palm, fingers slightly apart.** Palm toward the camera, a small visible gap between every finger, thumb open. A palm-down paper reads as wrong. Ask for a clean palm (one take came out with blister-like spots).
- **The cover's UI motif sits on the headline.** A thin text caret right after the last word and the pointer resting on that word, as in the source. Not a block with a gap.
- **Even out sizes in code.** Generations frame hands at different distances; measure wrist thickness just past the cuff and set `zoom` per hand so both players match.
- **Show the sleeves.** Keep each cuff at least 8% inside the frame (`cuff_min`), scaling the hands down rather than losing the sleeve.
