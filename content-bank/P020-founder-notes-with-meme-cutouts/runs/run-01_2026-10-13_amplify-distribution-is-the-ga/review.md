# Review

## Format match (7 points)
1. Structure: yes. 7 slides in the source's roles (hook, game changed, proof, main lesson with bio plug, second lesson, next step, centred conclusion with CTA).
2. Hook: yes. A pov reality check aimed at founders, one bold line, a swipe arrow.
3. Camera and motion: yes. Warm grey card #e4e3df, black and white waist-up cutouts with a white sticker outline, cropped by the bottom edge, halftone on the cover and closer.
4. Pacing: yes. Body slides 33 to 55 words in 3 to 4 short paragraphs (source 45 to 75; ours run shorter, as the owner asked "dont blabber").
5. Text overlay: yes. Bold grotesk heading 2.7% (Inter, the source's Roboto measures 2.9%), monospace body 1.95% at a 2.3% pitch, left at x 12.8%, centred conclusion.
6. Audio: to pick in TikTok (not attached).
7. Arc: yes. Identity call-out, old edge gone, proof, how, system, cut and double down, recap and CTA.

## Originality check (`output/originality.json`): REVIEW, no FAIL
| Slide | Raw overlap | Content words | Longest shared run | Status |
|---|---|---|---|---|
| 1 | 43% | 20% | 1 | review (shared: pov, you, and) |
| 2 | 34% | 20% | 1 | review |
| 3 | 32% | 22% | 2 ("the game") | review |
| 4 | 34% | 29% | 2 ("link in") | review |
| 5 | 22% | 9% | 1 | pass |
| 6 | 33% | 17% | 1 | review |
| 7 | 24% | 19% | 2 ("link in") | pass |
- Hook overlap 14% (formula word "pov" kept as trend wording). Images: closest source slide 14 bits (near-duplicate at 10 or less): pass.
- Review slides are over 30% raw only on function words; every content-word share is under 30%. "distribution is the game" is the owner's own phrase.
- First render had slide 1 at 40% content words ("pov you shipped the saas and nobody came") and slide 2 at 9 bits from source slide 6. Rewritten, and slide 2's cutout moved to the right.
- People: all original, generated. No film stills, no real likeness, no source poses copied (the source's leaning-back, phone-call and headphones poses aren't used).

## Caption check
`caption.py check`: **PASS**, soft, 222 characters, 5 hashtags, disclosure last.

## Text by eye
Lowercase except Amplify and TikTok. No dashes, colons or semicolons (the renderer refuses them). No emoji on the slides.

## Measured slide checks
`measure.py check --record` on all 7 slides: boxes drawn in `output/checks/slideN_boxcheck.jpg`, all on their elements. Text contrast #111 on #e4e3df (about 15:1, same as the source).

## Known limits
- `brands/amplify.md` was drafted in this run from the owner's message. Handle and site aren't filled in. The only result claimed is the owner's own "30 posts for my saas, for free". Amplify is never said to post or schedule. Scheduling is general advice.
- Slide 3's 17.4M figure is a post we collected (P013 source), not a saas account. The line says "tiktoks that blow up", not "in my niche", so it stays accurate.
- Body font is DejaVu Sans Mono standing in for Space Mono (Space Mono is not bundled). It's slightly narrower in feel.
- One source post: pillar confidence Low.

## Re-render (2026-10-13)
Re-rendered with the new fill layout (owner rule: no empty bottom corners). Same art and text. Cover art sits left with the arrow in the free corner. Slide 7 uses `max_cut` 0.44 because her crossed-arms pose is narrow. The first render is kept in `raw/output_v1/`. Originality after the re-render: REVIEW, no FAIL, closest image 19 bits. Caption PASS.

## Tester ratings (1–5)
Pending.

## Owner verdict
Pending.

## Feedback
