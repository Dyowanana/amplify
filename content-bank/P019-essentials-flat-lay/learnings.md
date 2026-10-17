# P019 learnings

Feedback from runs, turned into general rules.

## Production rules (run-01, 2026-10-10)
- Keeping the source's layout plus a dark top in the outfit slot lands at the near-duplicate line on dhash (it measures where the masses sit). Mirror the layout (outfit on the right), or check `originality.py` before finishing.
- Generate each garment alone and say "only the pants and nothing else, no top": asking for one half of a matching set gets the whole set.
- Generic gadgets drift toward famous designs (a square watch with a crown and sport loop). Ask for a shape the market leader doesn't use (round face, plain strap).
- `originality.py` reads `output/slideN.*`: for a variants run, copy the boards into a temporary run folder as slide1 to slide5 and run it there.

## Production rules (run-02, 2026-10-11)
- Silver over-ear headphones come out as a famous brand's design. Ask for round cups and a leather headband, or a colour.
- A real third-party app in a ring slot: crop the real mark from a `webshot.py` screenshot of the company's own site (`--scale 8` for a sharp crop), never redraw it, and use the plan's real name from their pricing page.
- Two items with the same prompt come back as the same image (kie cache, no charge). Vary the prompt when the versions should differ.
