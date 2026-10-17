cd /c/Users/joana/amplify
R="content-bank/P018-ai-realism-skin-macro-carousel/runs/run-01_2026-10-08_willow-ai-realism"
REF="personas/willow/refs"
for k in s1_eye s2_selfie s3_lips s4_nose s5_cheek s6_temple; do
  P=$(./.venv/python.exe -c "import sys;sys.path.insert(0,'$R/raw');import prompts;print(prompts.prompt('$k'))")
  if [ "$k" = s2_selfie ]; then EX="$REF/rooms/street.jpg $REF/light/overcast_street.jpg $REF/wardrobe/home.jpg"; EX="$REF/rooms/street.jpg $REF/light/overcast_street.jpg"; else EX="$REF/closeups/skin_macro.jpg $REF/light/window_soft.jpg"; fi
  ./.venv/python.exe tools/kie.py image --model nbp --resolution 2K --aspect 9:16 --prompt "$P" --ref $REF/real_face.png $REF/sheet_real.png $EX --out $R/raw/$k.png --run $R --run-cap 400
done
