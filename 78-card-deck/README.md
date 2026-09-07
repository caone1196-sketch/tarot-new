# Sensual Tarot — 78-card clean rebuild package

This folder is the self-contained deliverable generated from the repository sources.

- `cards.json` is an exact copy of the supplied 78-card standard; it is the source of truth for title, scene, character, and count locks.
- `prompts/` contains one fully expanded prompt per card. Each prompt preserves the exact `scene`, `hair`, `age`, `build`, and count instruction from `cards.json`, then adds the individual eye/skin/signature/aura traits from `02-CHARACTER-SPECS.md` when a card has a character.
- `cards/` is the artwork output directory; the manifest reserves one PNG filename per source slug.
- `the moon.png` is the only local image reference used by this clean rebuild. The Star and blank-template references are intentionally excluded from the output folder.
- `prompt-manifest.json` maps all 78 source records to their prompt and image files.

Visual lock: `the moon.png` is the only image reference for generation. Its open full-height window, thin gold Gothic border, corner flourishes, title placement, and atmospheric fine-art rendering are kept consistent without copying its scene objects or pose. Every card removes the top frame medallion/emblem/icon entirely so the scene fills the full inner area from the top border to the title; symbols explicitly required inside a card scene remain. Artwork is exported as PNG with a high-detail, high-resolution finish.

Suit-object counts are hard constraints. For any card whose source `count` is `null`, the prompt explicitly prohibits adding suit objects. The six object-only cards remain object-only.

Generated on 2026-09-07 from the checked-out repository sources.

## Artwork generation status

The prompt package is complete for all 78 cards. The clean rebuild removes every previous JPG and PNG before generation. Prompts request ultra-detailed, high-resolution artwork and PNG output. The image-generation service allows at most ten image generations per assistant turn; artwork is created in batches and the manifest records `generated` or `pending-generation` for each PNG.
