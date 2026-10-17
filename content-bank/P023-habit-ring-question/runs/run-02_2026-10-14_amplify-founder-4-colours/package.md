# P023 run-02 · founder habit ring, new layout, 4 card colours

Owner feedback on run-01 (2026-10-14): remove the rubber duck and add "8h+ sleep"; 4 items at the top and 5 down each side; make 3 more versions on white, blue and orange with the same icons.

Same art as run-01 (copied into `raw/art`, no new generations), same hook and caption. Brand `amplify`, caption style soft.

## Layout (1080 x 1350)
- Top row (4): macbook, iced matcha, 0 meetings (cat), dark mode (moon).
- Left (5): notifications off, clicky keyboard, new user (film-still man), **Amplify icon, "automated content (check bio)"**, touched grass.
- Right (5): credit reset, 10k lines shipped, first try deploy, lofi on loop, **8h+ sleep** (new bed icon drawn in code).
- Title "why does today / feel illegal?" sits above the figure, and the glowing figure fills the middle down to the bottom. With the title under the figure, the pale versions came out too close to the source on the image hash (6 bits), so the title moved up (11 bits).

## Versions
| File | Card | Text contrast |
|---|---|---|
| `output/slide1.png` | pale sage #ebf1ea (as the source) | 16.5 |
| `output/slide2.png` | white #ffffff | 18.9 |
| `output/slide3.png` | blue #5cc8fa (the light blue of the Amplify logo) | 10.0 |
| `output/slide4.png` | orange #ff8a2a (the orange of the Amplify logo) | 8.0 |

These are separate single-image posts. Post them a day or more apart, or test which colour does best. Overview: `all_4_versions.jpg`.

## Caption (soft, same for every version)
```
not explaining the bottom left one, check bio instead

fine. it's Amplify, it takes formats that already work and makes them for your product. the hard part is having enough posts, that's what i use it for

#founder #vibecoding #buildinpublic #saas #productivity

this is an advertisement.
```
Amplify now sits in the left column, fourth down, rather than bottom left. "bottom left one" still reads right, but "the one with the arrows" works too if you'd rather.

## Posting
Photo mode, a calm music bed picked in TikTok, a morning post. Switch on the commercial content toggle and the AI-generated label.

## Production
No new image calls ($0). Render: `tools/ringcard.py spec.json` (the `versions` list changes only the card colour).
