# P023 run-01 · founder and vibe coder habit ring, Amplify in the brand slot

Owner request (2026-10-14): the @mentalapp "why does today feel unreal?" post, made for founders and vibe coders. Amplify's logo goes where the source had its own app ("state tracking"), labelled as automated content. Founder items (credit reset, new user, macbook), no magnesium. Icons should look collected and meme-like, not AI.

Pillar P023 (format) + brand `amplify` (the product slot and the caption). Caption style: soft (Amplify's logo is on the card).

## Hook
| Option | Mechanic | Overlap with the source hook |
|---|---|---|
| **why does today feel illegal?** (used) | mystery recipe. The trend phrase "why does today feel" is kept word for word and the state word is new | 80% (4 of 5 words are the formula phrase) |
| why does shipping feel this easy today? | mystery recipe, reworded | 40% |
| why is today so productive? | mystery recipe, plain | 20% |

## The board (1 slide, 1080 x 1350, card #ebf1ea)
| Zone | Item | Label | How it's made |
|---|---|---|---|
| Centre | violet glowing figure floating cross-legged, laptop on its knees | | gpt25s on white, cut as a glow in code |
| Centre | title | why does today / feel illegal? | code, Inter 300, tight tracking |
| Top row | open silver laptop, no logo | macbook | gpt25s stock-photo look, "stock" finish |
| Top row | iced matcha | iced / matcha | gpt25s, stock |
| Top row | screaming hairless cat | 0 meetings | gpt25s on green, "flash" finish (old meme photo) |
| Top row | rubber duck | rubber / duck | gpt25s, stock |
| Top row | full moon | dark / mode | gpt25s, stock |
| Left | red no sign over a bell | notifications / off | drawn in code |
| Left | **Amplify app icon** (the real logo file) | automated / content / (check bio) | the owner's logo, rounded tile |
| Right | battery with a bolt | credit / reset | drawn in code |
| Right | outlined tile with >_ | 10k lines / shipped | drawn in code |
| Bottom row | mechanical keyboard, blank keys | clicky / keyboard | gpt25s, stock |
| Bottom row | fictional 90s office film-still man, fists up | new user | gpt25s on green, "film" finish |
| Bottom row | olive headphones, leather band | lofi on / loop | gpt25s, stock |
| Bottom row | black tick circle | first try / deploy | drawn in code |
| Bottom row | patch of turf | touched / grass | gpt25s, stock |

The item mix follows the source's recipe: photo objects, 2 meme cut-outs, flat black pictograms with one red no sign, one element-style tile and the app icon. Every item and label is new.

## Caption (soft, `caption.txt`)
```
not explaining the bottom left one, check bio instead

fine. it's Amplify, it takes formats that already work and makes them for your product. the hard part is having enough posts, that's what i use it for

#founder #vibecoding #buildinpublic #saas #productivity

this is an advertisement.
```

## Posting
- Photo mode, one image, a calm music bed (the source used a trending original sound; pick one in TikTok).
- Morning post (the source went out at 08:57 local on a Tuesday).
- Switch on TikTok's commercial content toggle and the AI-generated label.
- No handle line under the title: `brands/amplify.md` has no handle yet. Add it (small, grey) once there is one.

## Production
10 × `kie.py image --model gpt25s` (prompts in `raw/art/prompts.tsv`), 68 credits ($0.34), all first takes. Render: `tools/ringcard.py spec.json` (new renderer for P023: white or green cut-outs, mixed finishes, code-drawn pictograms, real logo tile).
