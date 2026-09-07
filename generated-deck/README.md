# Sensual Tarot — 78-card production deck

This folder is the isolated deliverable. It contains one final card for every entry in the supplied `cards.json`, plus the prompt used for each illustration.

## References and synchronization

- `the moon.png` is the character/mood anchor.
- `17-the-star.png` is the fine-art lighting and open-window composition reference.
- `card-blank.png` is the parchment/template reference.
- Every final card is composited to one fixed 784 × 1360 px portrait frame (7:12), with the same double gold gothic border, corner ornaments, medallion treatment, title ribbon, antique-gold typography, and sepia parchment edge.
- AI-generated files in `scenes/` intentionally contain no border or lettering. The synchronized frame and title are applied by `scripts/compose_cards.sh` so titles never drift or hallucinate.

## Contents

- `cards/` — the 78 finished cards, in canonical Major Arcana → Wands → Cups → Swords → Pentacles order.
- `scenes/` — generated center-panel artwork used to build the finished cards.
- `prompts/` — one prompt per card, based on the supplied master prompt and card table, including the object count locks.
- `manifest.json` — machine-readable index.
- `MASTER-PROMPT-USED.md` — provenance copy of the supplied master prompt.
- `scripts/compose_cards.sh` — deterministic frame/title compositor.

