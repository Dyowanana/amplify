ID = ("the same woman as the reference photos: Willow, 31, light-olive skin, warm brown eyes, freckles across the nose bridge and upper cheeks, "
      "two small flat moles on her left cheek (right side of the picture) and one near her left jaw, oval face with a slightly square jaw, straight nose "
      "with a small bump on the bridge, fuller lower lip, dark brown shoulder-length loose waves with frizz and flyaways at the crown, small gold hoops in both ears. "
      "Her moles are small, flat and subtle, light brown, exactly as in the reference face; no other moles or dark spots on her face. ")
REAL = ("Unretouched iPhone photo, natural skin texture with every pore, fine peach fuzz and tiny dry lines visible, slight sensor noise and grain, "
        "true-to-life colour, uneven soft natural daylight from one side (not evenly bright), a hint of glare, no beauty filter, no retouching, no makeup "
        "except lip balm, no studio lighting, not a polished stock photo, not a studio photo, not CGI. ")
MACRO = ("Extreme macro close-up taken with an iPhone's macro mode a few centimetres from her face: the feature fills the whole vertical frame edge to edge "
         "and is cropped hard, a thin plane of focus with the edges falling softly out of focus, flat grey overcast daylight from a window on her right. "
         "She wears a chunky rust-orange knit crew-neck jumper. ")
END = " Vertical 9:16. No text, no letters, no numbers, no logos."
SHOTS = {
 "s1_eye": MACRO + "Her right eye fills the upper middle of the frame: warm medium brown iris with a darker outer ring and amber flecks near the pupil, a soft window reflection in the eye, natural medium lashes with a few clumped, slightly hooded lid with a visible crease, faint fine lines and light shadow under the eye, the whites a little pink at the inner corner. Below it the freckles across her upper cheek and the side of the nose bridge in sharp detail, pores, peach fuzz. The tail of her brow at the top edge with stray hairs. ",
 "s2_selfie": "A selfie (no phone visible in the shot) of her standing on her terraced street in Bristol on a grey overcast afternoon, head and shoulders to mid-chest, arm's-length front-camera framing with slight wide-lens distortion, her face in the upper third. Brick and painted render terraces, a plane tree and parked cars soft in the background (number plates blank). She wears a chunky rust-orange knit crew-neck jumper, hair down with frizz at the crown and a strand across her cheek, tucking hair behind her left ear with her left hand. Calm, direct look into the lens, lips closed and relaxed, no smile. Flat soft grey light, slightly cool background, her freckles visible even at this distance. ",
 "s3_lips": MACRO + "Her lips fill the middle of the frame, slightly parted and relaxed (not pouting): fuller lower lip, soft cupid's bow, natural rosy-beige, a little dry with fine vertical lines and one small dry flake, a thin sheen of lip balm catching the window light. Peach fuzz and pores on the skin above the upper lip, the base of the nose at the top edge, the chin falling soft at the bottom edge. A few rust knit fibres soft at one bottom corner. ",
 "s4_nose": MACRO + "Her nose in profile from her left side, seen slightly from below: the small bump on the bridge, softly rounded tip, slight redness around the nostril, enlarged pores on the nose and inner cheek, freckles across the bridge, fine hairs catching the light along the edge. Her eye and lashes soft and blurred at the top of the frame, the upper lip soft at the bottom edge, a dark strand of hair crossing the cheek. ",
 "s5_cheek": MACRO + "Her left cheek fills the whole frame, almost abstract: bare skin with pores, scattered freckles, fine peach fuzz lit up by side light, the two small flat light-brown moles of her left cheek in focus, a faint hint of redness. A strand of dark brown hair curving across the skin. At the bottom edge the soft chunky rust-orange knit of the jumper collar, out of focus. ",
 "s6_temple": MACRO + "The side of her face from the brow tail to the ear: her left temple and hairline with baby hairs and frizz, a few flyaways crossing the frame, the tail of her brow with stray hairs, pores and a few freckles on the temple, the top of her ear with a small gold hoop soft at the edge. The middle of the frame is calm skin (forehead and temple), even in tone, with room in the middle for nothing else. ",
}
def prompt(k):
    return ID + (REAL if k == "s2_selfie" else REAL) + SHOTS[k] + END

# v2 (2026-10-08): v1 macros came out as half-face close-ups. The source crops much tighter: one feature fills the
# frame and the rest of the face is outside it. Say what is NOT in the frame.
MACRO2 = ("Extreme macro photo taken with an iPhone in macro mode held about 3 centimetres from her skin. Only the part described below is in the "
          "frame; the rest of her face is outside the frame. At this distance every pore is large and clearly visible, individual fine vellus hairs "
          "stand out, skin has tiny dry lines and uneven tone. A thin plane of focus: the middle is sharp, the edges fall softly out of focus. "
          "Flat grey overcast daylight from a window on her right. ")
SHOTS2 = {
 "s1_eye": "Her right eye fills the frame from edge to edge: the eye is about two thirds of the frame width, centred slightly above the middle. Warm medium brown iris with a darker outer ring and amber flecks near the pupil, a soft window reflection in the eye, natural lashes with a few clumped, the hooded lid crease, faint fine lines under the eye. Below the eye the freckles of her upper cheek in sharp detail. The brow hairs at the top edge. The nose, the mouth and the edge of the face are not in the frame. ",
 "s3_lips": "Her lips fill the frame from edge to edge, the mouth wider than the frame so the corners are cut off: fuller lower lip, soft cupid's bow, slightly parted and relaxed, natural rosy-beige, dry with fine vertical lines and one small dry flake, a thin sheen of lip balm catching the window light. Peach fuzz and pores on the skin above the upper lip at the top. The nose and the eyes are not in the frame. A little rust-orange knit soft in one bottom corner. ",
 "s4_nose": "The side of her nose from her left side, slightly from below, filling the frame: the small bump on the bridge, softly rounded tip, slight redness around the nostril, large pores on the nose and the inner cheek, freckles across the bridge, fine hairs catching the light along the edge. Her lashes blurred at the very top edge. The mouth and the rest of the face are not in the frame. A dark strand of hair across the cheek. ",
 "s5_cheek": "Only bare skin of her left cheek fills the whole frame, almost abstract: large pores, scattered freckles, fine peach fuzz lit by side light, the two small flat light-brown moles of her left cheek in focus, faint redness, uneven tone. One strand of dark brown hair curving across. The eye, nose and mouth are not in the frame. At the bottom edge the rust-orange chunky knit collar, out of focus. ",
 "s6_temple": "Her left temple and hairline fill the frame: baby hairs and frizz at the hairline, a few flyaways crossing the skin, the tail of her brow with stray hairs at the bottom left, pores and a few freckles on the temple, the top of her ear with a small gold hoop soft at one edge. The eye, nose and mouth are not in the frame. The middle of the frame is calm, even skin. ",
}
def prompt2(k):
    return ID + REAL + MACRO2 + SHOTS2[k] + "She wears a chunky rust-orange knit crew-neck jumper." + END

# v3 s6: the temple shot drew two brows and two eyes on one side. One brow, no eye.
SHOTS2["s6_brow"] = ("Her forehead and her left brow fill the frame. The single brow runs across the lower third of the frame: medium-full, soft angle, "
  "natural stray hairs, the tail slightly sparse. Above it, filling the middle and top of the frame, calm forehead skin with pores, a few freckles, "
  "faint horizontal forehead lines and a little shine; at the very top edge her dark brown hairline with baby hairs and a few flyaways. "
  "Her eye is not in the frame, and there is only one brow. The nose, the mouth and the ear are not in the frame. ")
