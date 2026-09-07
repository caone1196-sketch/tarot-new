# Sensual Tarot — 78-card clean rebuild package

This folder is the self-contained deliverable generated from the repository sources.

- `cards.json` is an exact copy of the supplied 78-card standard; it is the source of truth for title, scene, character, and count locks.
- `prompts/` contains one fully expanded prompt per card. Each prompt preserves the exact `scene`, `hair`, `age`, `build`, and count instruction from `cards.json`, then adds the individual eye/skin/signature/aura traits from `02-CHARACTER-SPECS.md` when a card has a character.
- `cards/` is the artwork output directory; the manifest reserves one PNG filename per source slug.
- `the moon.png` is the only local image reference used by this clean rebuild. The Star and blank-template references are intentionally excluded from the output folder.
- `prompt-manifest.json` maps all 78 source records to their prompt and image files.
- `upscale_pngs.py` converts newly rendered 784x1360 PNGs to the 2x 1568x2720 delivery size.

Visual lock: `the moon.png` is the only image reference for character rendering, atmospheric fine-art lighting, anatomy, and color depth. Its frame, corner flourishes, parchment margin, medallion, emblem, icon, and banner are intentionally not copied. Every card is borderless full-bleed artwork with the scene reaching all four edges and only the title overlaid at the bottom. Artwork is exported as PNG with a high-detail, high-resolution finish; generated cards are upscaled 2x to 1568x2720 pixels after rendering.

Suit-object counts are hard constraints. For any card whose source `count` is `null`, the prompt explicitly prohibits adding suit objects. The six object-only cards remain object-only.

Generated on 2026-09-07 from the checked-out repository sources.

## Artwork generation status

The prompt package is complete for all 78 cards. The clean rebuild removes every previous JPG and PNG before generation. Prompts request ultra-detailed, high-resolution artwork and PNG output. The image-generation service allows at most ten image generations per assistant turn; artwork is created in batches and the manifest records `generated` or `pending-generation` for each PNG.
