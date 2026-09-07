#!/usr/bin/env bash
set -euo pipefail
# Deterministically composite generated scene panels into a synchronized 784x1360 deck frame.
# Requires ImageMagick's convert and a 7:12 scene image in generated-deck/scenes/.
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$ROOT/.." && pwd)"
mkdir -p "$ROOT/cards" "$ROOT/proof"
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FRAME="$ROOT/.frame.png"

# Build a repeatable line-art frame with ImageMagick primitives. Keeping this as a
# raster overlay avoids any dependency on an SVG renderer in the checkout.
make_frame() {
  convert -size 784x1360 xc:none \
    -stroke '#8c5b1f' -strokewidth 4 -fill none \
    -draw 'rectangle 0,0 783,1359' \
    -stroke '#d8ae59' -strokewidth 2.6 \
    -draw 'rectangle 18,18 765,1341 rectangle 31,31 752,1328' \
    -stroke '#f0d47f' -strokewidth 1.2 \
    -draw 'rectangle 37,37 746,1322' \
    -stroke '#d8ae59' -strokewidth 3 \
    -draw 'arc 26,25 112,111 185,355 arc 672,25 758,111 5,175 arc 26,1249 112,1335 5,175 arc 672,1249 758,1335 185,355' \
    -draw 'arc 43,43 87,87 180,285 arc 697,43 741,87 255,360 arc 43,1273 87,1317 75,180 arc 697,1273 741,1317 0,105' \
    -stroke '#e2bd68' -strokewidth 2 \
    -draw 'circle 59,58 59,35 circle 725,58 725,35 circle 59,1302 59,1325 circle 725,1302 725,1325' \
    -fill '#171321' -stroke '#d8ae59' -strokewidth 3 \
    -draw 'ellipse 392,62 91,34 0,360 ellipse 392,62 82,27 0,360' \
    -fill '#f2d17d' -stroke '#7c4b17' -strokewidth 1.2 \
    -draw 'polygon 392,40 399,57 416,64 399,71 392,88 385,71 368,64 385,57' \
    -stroke '#d8ae59' -strokewidth 2.5 -fill none \
    -draw 'line 135,1259 326,1262 line 458,1262 649,1259 line 135,1280 250,1280 line 534,1280 649,1280' \
    "$FRAME"
}

compose_one() {
  local scene="$1"; local title="$2"; local out="$3"
  local tmp="$ROOT/.tmp-$(basename "$out")"
  [[ -f "$FRAME" ]] || make_frame
  # card-blank supplies the aged vellum outside the open window. The scene is
  # deliberately inset so the shared line-art frame always sits in front of it.
  convert "$REPO/card-blank.png" \
    \( "$scene" -resize '700x1220^' -gravity center -crop 700x1220+0+0 +repage \) \
    -geometry +42+45 -composite \
    "$FRAME" -composite \
    -font "$FONT" -fill '#f2d17d' -stroke '#6e4112' -strokewidth 1 \
    -gravity south -pointsize 34 -kerning 1 -annotate +0+43 "$title" \
    -quality 90 "$tmp"
  mv "$tmp" "$out"
}

if [[ "${1:-}" == "--all" ]]; then
  python - "$ROOT" <<'PY'
import json,sys,subprocess,pathlib
root=pathlib.Path(sys.argv[1]); m=json.loads((root/'manifest.json').read_text())
for c in m['cards']:
    scene=root/c['scene']; out=root/c['card']
    if scene.exists():
        subprocess.run([str(root/'scripts/compose_cards.sh'),'--one',str(scene),c['title'],str(out)],check=True)
PY
elif [[ "${1:-}" == "--one" ]]; then
  compose_one "$2" "$3" "$4"
else
  echo "usage: $0 --all | --one SCENE TITLE OUTPUT" >&2; exit 2
fi
