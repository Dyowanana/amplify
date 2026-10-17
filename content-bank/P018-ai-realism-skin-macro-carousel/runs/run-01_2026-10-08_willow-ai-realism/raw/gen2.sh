cd /c/Users/joana/amplify
R="content-bank/P018-ai-realism-skin-macro-carousel/runs/run-01_2026-10-08_willow-ai-realism"
REF="personas/willow/refs"
for k in "$@"; do
  P=$(./.venv/python.exe -c "import sys;sys.path.insert(0,'$R/raw');import prompts;print(prompts.prompt2('$k'))")
  ./.venv/python.exe tools/kie.py image --model nbp --resolution 2K --aspect 9:16 --prompt "$P" --ref $REF/real_face.png $REF/sheet_real.png $REF/closeups/skin_macro.jpg $REF/light/window_soft.jpg --out $R/raw/$k.png --run $R --run-cap 400 && echo "DONE $k"
done
