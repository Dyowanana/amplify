# P017 run-01 · Willow × Bolt Pharmacy · "why mondays weigh more"

Account copy: @75evi.page → Bolt Pharmacy (`brands/boltpharmacy.md`), caption **hard**, 5 slides, 1080 x 1350.

## How pillar, persona and brand combine
| @75evi.page (source system) | Bolt Pharmacy version | Why |
|---|---|---|
| Faceless page, lifestyle stock photo of young women on the closer | Willow (fictional UK wellness educator, `personas/willow.md`) on the closer | Human-led closer → a persona from `personas/`; no real person's likeness |
| Cream card `#faf8f4`, near-black serif, pink italic payoff | Light Bolt-blue tint `#f2f6fc`, navy `#0d1b4c` serif, Bolt blue `#0964da` italic payoff, light blue `#9cc3ff` on the photo | Colours sampled from boltpharmacy.co.uk (`raw/shots/home_iphone.png`) |
| Playfair-like serif + Inter-like sans | Playfair Display + Inter (same font roles; Playfair added to `assets/fonts/`, OFL) | Format font roles kept |
| 2 x 3 photoreal object grids | 18 new objects (GPT Image 2.5 Sunburst, one per image, on white, multiply-blended) | Format kept, art new |
| Topics: puffiness, digestion, period week | Why the scale jumps after a weekend (water, not fat) | The brand's category is weight care; the topic teaches something true and general without promising an outcome |
| Plug: first-person testimonial ("the 75 Evi app kept me going") | Third-person service line ("Bolt Pharmacy starts with a short online check, reviewed by a uk clinician, no appointment needed") | A fictional person can't give a testimonial for a regulated healthcare service (no invented reviews) |
| Closer: body-outcome promise ("a sharp jawline at 8am", "flat stomach by 9am") | "trust the trend, not mondays" | No weight or body-outcome claims for Bolt |
| Absurd comment-bait tips in the fix grid ("clap 3 times before water") | Left out: every tip is real | No false health tips |

## Hooks (mechanic labelled)
Pillar mechanics: reassuring reframe (`why X makes you Y` + `its water, not fat`), recognition grid, self-diagnosis checklist, mystery reveal.
1. **Chosen:** "why mondays weigh more" / sub "water, not fat. it usually settles by wednesday". Mechanic: **reassuring reframe** (why + everyday trigger, reframed as water). Formula words kept: "why", "water, not fat". Hook overlap 25% (only "why").
2. "the monday scale jump" / same sub. Mechanic: mystery reveal. 25% overlap.
3. "signs the scale is showing water" / "if three of these happened this weekend, its water". Mechanic: self-diagnosis checklist (not used: too close to source post 7693275909364731150).

## Slides
| # | Role | Text | Visual |
|---|---|---|---|
| 1 | Hook grid | **why mondays** *weigh more* / water, not fat. it usually settles by wednesday · big pasta night (carbs get stored with water) · salty takeaway (salt keeps water in you) · drinks with friends (alcohol throws off your fluids) · period week (hormones shift water too) · leg day (sore muscles hold water) · the flight home (hours sitting still pools fluid) | spaghetti bowl, noodle takeaway box, pint of beer, knitted hot water bottle, kettlebell, travel neck pillow |
| 2 | Swap grid | **the day after,** *try these* · banana (a good potassium hit) · jacket potato (even more potassium, skin on) · water (helps clear the extra salt) · porridge (filling and plain) · cucumber (cool, crunchy, zero salt) · spinach (leafy and nearly salt free) | banana, jacket potato, glass of water, porridge, cucumber, spinach |
| 3 | Fix grid | **how to read** *the scale* · same time daily (after the loo, before breakfast) · the weekly average (one day tells you nothing) · a 20 minute walk (gets fluid moving again) · cooking at home (you choose the salt) · normal meals (no crash diet to make up for it) · water on hand (sipping all day is easier) | bathroom scale (blank display), notebook and pen, plain trainers, frying pan of veg, balanced dinner plate, sage steel bottle |
| 4 | Explainer + product | **the scale weighs** *water too* · ... · salt, carbs, drinks and sore muscles all make your body hold on to extra water, and it usually settles by midweek. / weigh first thing each morning and follow the weekly trend instead of one reading. / and if you want a clinician in your corner, **Bolt Pharmacy** starts with a short online check, reviewed by a uk clinician, no appointment needed. | text card |
| 5 | Closer + CTA | **trust the trend,** *not mondays* / Bolt Pharmacy, check eligibility via bio | Willow laughing on her park path at golden hour, oatmeal jumper, sage bottle; phone_look grain, bottom gradient |

## Caption (hard) · `caption.txt`
a heavier monday is usually water, not fat, and it settles by midweek. if you want a clinician in your corner, Bolt Pharmacy is an online weight-loss consultation and prescription service. you fill in a short online check, a uk clinician reviews every case, and there is no appointment to sit through. check your eligibility, link in bio 🤍

#waterretention #weighin #wellnesstok #healthyhabits #boltpharmacy

this is an advertisement.

## Posting
- Photo mode, 5 images in this order, with a calm trending sound picked inside TikTok (the source uses music only).
- Switch on TikTok's **AI-generated content** label (the objects and Willow are AI images) and the **commercial content** toggle (brand content).
- Source account posts 8pm to 5am Manila time (US daytime); for a UK audience, post in UK evening or Monday morning (the topic is a Monday one).
- **Bolt Pharmacy's compliance team must approve the caption and slides before posting** (brand file compliance note).

## Production
1. Brand colours sampled from a real-site screenshot (`webshot.py --device iphone15`).
2. 18 objects: `kie.py image --model gpt25s --resolution 1K --aspect 1:1`, one object per image on white (prompts in `raw/art/objects.tsv` and `costs.json`).
3. Closer: `kie.py image --model nbp --resolution 2K --aspect 4:5` with Willow's `real_face.png`, `sheet_real.png`, `rooms/park.jpg`, `light/golden_backlit.jpg`, `expressions/laugh.jpg`.
4. Render: `tools/gridcards.py spec.json` (new renderer for P017; text in code, art multiply-blended, records written per slide).
5. Checks: `measure.py check --record` per slide, `originality.py`, `caption.py check`.

## Cost
132 credits ($0.66): 19 GPT Image 2.5 Sunburst calls at 6 credits (18 objects + 1 billed timeout) and 1 Nano Banana Pro call at 18. Itemised in `costs.json`.
