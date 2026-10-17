# Review

## Format match (7 points)
1. **Structure:** cover + 6 rounds (source 5 slides). Match.
2. **Hook:** game call and edition line with a "swipe to play" arrow on a standoff. The source used a know-how challenge; this uses the trend's game call (the owner's line). Partial match, same mechanic family.
3. **Camera & motion:** two cut-out hands from opposite edges at one height, sleeve at each edge, flat textured card. Match.
4. **Pacing:** 3 to 6 words per side. Match.
5. **Text overlay:** bold grotesque, no box or outline, losing line above the left hand, winning line under the right hand, right-aligned. Match (lowercase by the owner's rule; tangerine winner by the brand).
6. **Audio:** carousel. Match.
7. **Arc:** belief vs. better move per round, the winner holds the lesson. Every round checked by the tool (the right gesture beats the left).

## Originality (`output/originality.json`)
Overall FAIL from slide 1 only: "rock paper scissors" (3 words) is the game's name, shared with the source caption. It's the trend wording the skill allows word for word. Slide 2 is in review at 33% raw overlap from "marketing / the / you", 14% content words. Slides 3 to 7 pass. Hook overlap 0%. Images: closest source slide is 22 bits away (near-duplicate at 10 or less), pass. New hands, sleeve, background, words and motif.

## Caption check
`caption.py check`: PASS, soft, 322 characters, 5 hashtags, disclosure last. The warning about capitals flags TikTok and Instagram (platform names, kept). Claims: only the brand file's "learns formats … makes new posts for your brand". No never-say words.

## Measured slide checks
`measure.py check --record` on all 7 (`output/checks/`). Boxes sit on their elements (looked at slide 2). Text contrast on navy: white about 17:1, tangerine #FF7A00 about 7:1, counter #A3AEB4 about 8:1.

## Models used
`nbp` (Nano Banana Pro) only, 13 calls, 234 credits ($1.17) including the revision. On the approved list.

## Looked at
Every hand image on a contact sheet (right scissors at full size: 5 fingers, thumb holding ring and little finger; left paper at full size after the blister take), every rendered slide on a sheet, slides 1, 3 and 6 at full size, and the key edges at 1:1 (no green fringe).

## Revision 1 (owner feedback, 2026-10-14)
- **Cover caret and pointer were in a weird place** (a thick block with a gap after "shoot", the pointer hanging off it). Now a thin tangerine text caret right after "shoot" on the baseline, and a larger sky-blue pointer resting on the word, the way the source's cursor sits on its headline.
- **Hands should be two different people.** Player 1 (left): light olive skin, charcoal hoodie with a worn cuff, black braided bracelet. Player 2 (right): deep brown skin, light grey hoodie, black watch strap, silver ring. Player 2's generations framed the hand smaller, so the spec evens the size out by wrist thickness (`zoom` 1.36 to 1.45).
- **Paper should show the palm, fingers a bit separated.** Both paper hands regenerated palm toward the camera with small gaps between the fingers and the thumb open. One left-paper take came out with blister-like spots and touching fingers and was redone.
- Hands slightly smaller (`art_scale` 0.28) and the cuff kept 8% inside the frame so both sleeves read on every slide.
- Rejected takes are in `raw/hands/_rejected/`, named by the reason.

## Known limits
- Each gesture image is reused across slides (the source did the same with its fist).
- `cuff_x` finds the sleeve by its low colour; a brightly coloured sleeve would need another rule.

## Tester ratings (1–5)
Pending.

## Owner verdict
Pending.
