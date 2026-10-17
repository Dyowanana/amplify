# P023 run-03 · founder habit ring, full ring, 4 card colours

Owner feedback on run-02 (2026-10-14): the items have to go all the way round, and run-02 had none at the bottom. Bring "why does today feel illegal?" closer to the centre image.

Layout: 4 across the top, 4 across the bottom, 3 between them on each side. The corners belong to both a row and a side, so each side reads as 5. That makes 14 items. The title sits right under the figure (`gap_below_centre` in the spec, so the title follows the figure if it moves). Same art, hook and caption as run-02 (rubber duck out, 8h+ sleep in).

- Top: macbook · iced matcha · 0 meetings · dark mode
- Left: notifications off · clicky keyboard · new user
- Right: credit reset · 10k lines shipped · first try deploy
- Bottom: **Amplify, automated content (check bio)** · touched grass · lofi on loop · 8h+ sleep

| File | Card | Text contrast |
|---|---|---|
| `output/slide1.png` | pale sage #ebf1ea | 16.5 |
| `output/slide2.png` | white #ffffff | 18.9 |
| `output/slide3.png` | blue #5cc8fa (logo blue) | 10.0 |
| `output/slide4.png` | orange #ff8a2a (logo orange) | 8.0 |

## Caption (soft, same for every version; Amplify is bottom left again, so "bottom left one" is right)
```
not explaining the bottom left one, check bio instead

fine. it's Amplify, it takes formats that already work and makes them for your product. the hard part is having enough posts, that's what i use it for

#founder #vibecoding #buildinpublic #saas #productivity

this is an advertisement.
```

## Posting
Photo mode, a calm music bed picked in TikTok, a morning post, the colours a day or more apart. Switch on the commercial content toggle and the AI-generated label.

## Production
No new image calls ($0). Render: `tools/ringcard.py spec.json`.
