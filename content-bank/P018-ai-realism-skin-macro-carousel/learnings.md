# P018 learnings

Feedback from runs, turned into general rules.

## Run 01 (2026-10-08, Willow), production rules
- **Macro framing:** "extreme macro, fills the frame" alone gives a half-face close-up with Nano Banana Pro. Say how close ("iPhone macro mode about 3 cm from the skin"), how big the feature is ("the eye is about two thirds of the frame width"), and list what is **not** in the frame ("the nose, the mouth and the edge of the face are not in the frame"). That gave source-level pore size at 2K.
- **Anatomy at macro distance:** a temple/side-of-face macro drew two brows and two eyes. Pick one-feature shots (one eye, one brow, lips, nose, bare cheek) and say "only one brow".
- **Text contrast on bright skin:** white text over a lit cheek measured 1.7. Match the source's brightness first (measured, gamma in code), then put the text on the subject's shadow side (under-eye, lip line). That reached 3.3, inside the source's range.
- **Overlap counts the caption:** `originality.py` compares slide words with the source's caption too. "comment yes or no" and "not … real" failed or needed review because the source caption uses those words. Test candidate lines in code before rendering.
- **Phone finish:** `--phone 0.5` keeps the macro texture. Don't go heavier on this pillar.
