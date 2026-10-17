# P017 run-02 · Willow × Bolt Pharmacy · "why your face looks fatter than you are"

Second @75evi.page → Bolt Pharmacy post (hook requested by the user). Same system as run-01: Bolt blue tint `#f2f6fc`, navy `#0d1b4c`, Bolt blue `#0964da` italic payoff, Playfair Display + Inter, `tools/gridcards.py`, caption **hard**, 5 slides at 1080 x 1350. The mapping table and brand reasoning are in run-01's `package.md`; only the content differs.

## Hook (mechanic labelled)
"why your face looks *fatter than you are*" / sub "mostly fluid from the night before, and it eases once youre up". Mechanic: **reassuring reframe** (the pillar's `why your face …` formula, kept word for word as trend wording; "looks fatter than you are" is new). Measured hook overlap 50%: the shared words are the formula's "why your face" plus "you". The rest of slide 1 overlaps 25%.

This topic is the source account's biggest theme (puffy face, jawline), so every object, line and the angle are new: the source blames specific foods; this post adds the camera lens and light as the other half of "looks fatter", which also keeps it away from any body-outcome promise.

## Slides
| # | Role | Text | Visual |
|---|---|---|---|
| 1 | Hook grid | **why your face looks** *fatter than you are* / mostly fluid from the night before, and it eases once youre up · late curry (rich sauces hold water) · salted peanuts (a midnight snack full of salt) · a nightcap (alcohol leaves your face puffy) · a short night (shows under your eyes) · tissues (crying puffs up your eyes) · your front camera (wide lenses stretch faces) | curry and rice, salted peanuts, whisky tumbler, satin eye mask, tissue box, phone (screen off) |
| 2 | Swap grid | **lower salt** *dinner swaps* · lemon and herbs (flavour without the salt) · roast chicken tray (home cooked, you salt it) · lentil soup (filling, no stock cube) · unsalted pistachios (crunch minus the salt) · tomatoes (potassium, barely any salt) · lime and soda (fizz without the alcohol) | lemon with rosemary and thyme, roasting tray, lentil soup, pistachios, vine tomatoes, sparkling water with lime |
| 3 | Fix grid | **before you take** *the selfie* · two chilled spoons (cool puffy eyes fast) · your 2x lens (less stretch than the wide one) · a jug of water (start the day topped up) · a cold flannel (calms the swelling for a bit) · a mirror by the window (face the light, not the ceiling) · a walk outside (moving drains fluid) | spoons on ice, phone on a tripod (back, no logo), glass carafe, folded flannel, round brass mirror, navy umbrella |
| 4 | Explainer + product | **your face keeps** *the night before* · ... · salt, alcohol, short sleep and tears all leave fluid sitting in your face, and lying flat lets it gather overnight. / once you are up and moving most of it drains, and a wide phone lens held close exaggerates the rest. / and if you want support with the bigger picture, **Bolt Pharmacy** offers a short online check, reviewed by a uk clinician, no appointment needed. | text card |
| 5 | Closer + CTA | **same face,** *better light* / Bolt Pharmacy, check eligibility via bio | Willow mid-laugh in her kitchen, facing the window in soft morning light, mug of tea, grey tee, claw clip |

## Caption (hard) · `caption.txt`
a fuller face in the morning is mostly last nights fluid plus a wide phone lens held too close. if you want support with the bigger picture, Bolt Pharmacy is an online weight-loss consultation and prescription service. you fill in a short online check, a uk clinician reviews every case, and there is no appointment to sit through. check your eligibility, link in bio 🤍

#puffyface #selfietips #wellnesstok #healthyhabits #boltpharmacy

this is an advertisement.

## Posting
- Photo mode, 5 images in order, calm trending sound picked in TikTok. AI-generated label on, commercial content toggle on.
- Space it a day or more from run-01 (same series look).
- **Bolt Pharmacy's compliance team must approve it before posting.**

## Production
18 objects with `kie.py image --model gpt25s --resolution 1K --aspect 1:1` (prompts in `raw/art/objects.tsv`); closer with `kie.py image --model nbp --resolution 2K --aspect 4:5` and Willow's `real_face.png`, `sheet_real.png`, `rooms/kitchen.jpg`, `light/window_soft.jpg`, `expressions/laugh.jpg`; render `tools/gridcards.py spec.json`. Renderer change in this run: a two-line hook now pushes the subheading down instead of overlapping it (single-line hooks render exactly as before).

## Cost
126 credits ($0.63): 18 GPT Image 2.5 Sunburst calls at 6 credits and 1 Nano Banana Pro call at 18. Itemised in `costs.json`.
