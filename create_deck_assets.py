#!/usr/bin/env python3
"""Create the reproducible prompt package for the 78-card deck.

The artwork is generated separately, but every prompt is derived from cards.json
without rewriting its card data.  The character table is joined only as an
additional trait block for the 72 character cards.
"""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "78-card-deck"
PROMPTS = OUT / "prompts"
CARDS = OUT / "cards"

for p in (OUT, PROMPTS, CARDS):
    p.mkdir(parents=True, exist_ok=True)

# Keep an exact copy of the supplied source data in the deliverable.
shutil.copy2(ROOT / "cards.json", OUT / "cards.json")
shutil.copy2(ROOT / "00-MASTER-PROMPT.md", OUT / "00-MASTER-PROMPT.md")
shutil.copy2(ROOT / "01-CARD-TABLE.md", OUT / "01-CARD-TABLE.md")
shutil.copy2(ROOT / "02-CHARACTER-SPECS.md", OUT / "02-CHARACTER-SPECS.md")
# Only the Moon reference is copied into the clean rebuild package. The Star
# and blank-template files remain in the repository as historical source files,
# but they are intentionally not used for this rebuild.
shutil.copy2(ROOT / "the moon.png", OUT / "the moon.png")

# Parse the character table's markdown rows. The source table is intentionally
# left untouched; this is just a lookup for prompt enrichment.
traits: dict[str, dict[str, str]] = {}
text = (ROOT / "02-CHARACTER-SPECS.md").read_text(encoding="utf-8")
for line in text.splitlines():
    if not line.startswith("|") or "`" not in line:
        continue
    slugs = re.findall(r"`([^`]+)`", line)
    if len(slugs) != 1:
        continue
    slug = slugs[0]
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    # Table columns: card, age, eyes, hair, build, skin, signature, aura.
    if len(cells) < 8:
        continue
    traits[slug] = {
        "age": cells[1],
        "eyes": cells[2],
        "hair": cells[3],
        "build": cells[4],
        "skin": cells[5],
        "signature": cells[6],
        "aura": cells[7],
    }

# Common art/layout lock. The scene, count lock, hair, age, and build below are
# copied from the exact cards.json record, not paraphrased.
COMMON = """A finished single tarot card in a portrait 7:12 composition. Use the supplied the moon.png as the ONLY visual reference: preserve its open edge-to-edge central window, dark atmospheric fine-art lighting, full-height scene, thin double-line gilded Gothic border, symmetric corner flourishes, and large antique-gold blackletter title at the bottom. The entire top area must remain open scene with no oval top medallion, no frame emblem, no top icon, and no decorative badge; any symbol explicitly required inside the cards.json scene remains part of that scene. Do not use another card as a visual reference and do not copy The Moon's specific scene objects or pose.

The border and title treatment must be consistent across every card: same border thickness, same corner ornaments, same placement and scale, same typography, same portrait crop. The central scene must bleed slightly underneath the foreground gold border and fill the whole card interior from the top inner edge to the bottom title area. No stone arch, columns, or extra inner frame may squeeze the image unless they are part of the card's own scene. Only the card title may be lettered; no captions, labels, watermark, signature, or decorative top emblem/icon anywhere else. Preserve any named object or symbol that is explicitly part of the cards.json scene.

Render ultra-detailed, high-resolution classical fine-art tarot imagery with crisp painterly brushwork, fine hair and fabric microdetail, precise natural anatomy, clean edges, warm painterly light, rich atmospheric depth, and high pixel-density finish. Use razor-sharp focal detail and clear line separation; never use soft focus, motion blur, muddy textures, smeared hands, plastic skin, or low-resolution haze. All specified people are adult women or adults as stated by the supplied record. Preserve natural anatomy: every person has one head, one torso, no more than two arms and two legs, correctly joined shoulders, elbows, wrists, hips, knees, ankles, and natural hands. Keep every named character visually distinct. Do not add people, animals, props, suit objects, blades, staffs, cups, coins, or other countable items beyond the exact scene and count lock below. Do not borrow the Moon card's specific wolves, crayfish, towers, or nymph pose unless the record asks for them.
"""

with (OUT / "prompt-manifest.json").open("w", encoding="utf-8") as mf:
    manifest = []
    source = json.loads((ROOT / "cards.json").read_text(encoding="utf-8"))
    for card in source["cards"]:
        slug = card["slug"]
        count = card.get("count")
        count_block = "COUNT LOCK: no suit objects are required by this record; do not introduce countable suit objects." if count is None else (
            f"COUNT LOCK: exactly {count['n']} {count['obj']}. {count['layout']}."
        )
        trait = traits.get(slug)
        trait_block = ""
        if trait:
            trait_block = (
                "\nCHARACTER-SPECS identity lock (preserve these individual traits):\n"
                f"Eyes: {trait['eyes']}\n"
                f"Skin tone: {trait['skin']}\n"
                f"Signature detail: {trait['signature']}\n"
                f"Aura: {trait['aura']}\n"
            )
        prompt = (
            COMMON
            + f"\nCARD TITLE: {card['title']}\n"
            + "TOP SYMBOL LOCK: the cards.json emblem is metadata only and must NOT be drawn as a top frame emblem; remove the entire top medallion/icon area while preserving symbols explicitly required inside the scene.\n"
            + f"SCENE FROM cards.json (follow verbatim): {card['scene']}\n"
            + (f"HAIR FROM cards.json: {card['hair']}\n" if card.get("hair") else "")
            + (f"AGE FROM cards.json: {card['age']}\n" if card.get("age") else "")
            + (f"BUILD FROM cards.json: {card['build']}\n" if card.get("build") else "")
            + trait_block
            + f"\n{count_block}\n"
            + "\nFinal quality lock: complete card visible edge to edge, no cropped border, no duplicated limbs, no extra fingers, no accidental duplicate objects, razor-sharp details without blur, exact title spelling, title centered at the bottom in the same antique-gold Gothic type as the Moon reference."
        )
        path = PROMPTS / f"{slug}.txt"
        path.write_text(prompt, encoding="utf-8")
        image_path = CARDS / f"{slug}.png"
        manifest.append({
            "slug": slug,
            "title": card["title"],
            "group": card["group"],
            "prompt_file": f"prompts/{slug}.txt",
            "image_file": f"cards/{slug}.png",
            "character_traits_included": bool(trait),
            "count_lock": count_block,
            "artwork_status": "generated" if image_path.exists() else "pending-generation",
        })
    generated = sum(item["artwork_status"] == "generated" for item in manifest)
    payload = {
        "source": "cards.json",
        "cards": manifest,
        "artwork_generated_count": generated,
        "artwork_pending_count": len(manifest) - generated,
    }
    json.dump(payload, mf, ensure_ascii=False, indent=2)
    mf.write("\n")

readme = """# Sensual Tarot — 78-card clean rebuild package

This folder is the self-contained deliverable generated from the repository sources.

- `cards.json` is an exact copy of the supplied 78-card standard; it is the source of truth for title, scene, character, and count locks.
- `prompts/` contains one fully expanded prompt per card. Each prompt preserves the exact `scene`, `hair`, `age`, `build`, and count instruction from `cards.json`, then adds the individual eye/skin/signature/aura traits from `02-CHARACTER-SPECS.md` when a card has a character.
- `cards/` is the artwork output directory; the manifest reserves one PNG filename per source slug.
- `the moon.png` is the only local image reference used by this clean rebuild. The Star and blank-template references are intentionally excluded from the output folder.
- `prompt-manifest.json` maps all 78 source records to their prompt and image files.
- `upscale_pngs.py` converts newly rendered 784x1360 PNGs to the 2x 1568x2720 delivery size.

Visual lock: `the moon.png` is the only image reference for generation. Its open full-height window, thin gold Gothic border, corner flourishes, title placement, and atmospheric fine-art rendering are kept consistent without copying its scene objects or pose. Every card removes the top frame medallion/emblem/icon entirely so the scene fills the full inner area from the top border to the title; symbols explicitly required inside a card scene remain. Artwork is exported as PNG with a high-detail, high-resolution finish; generated cards are upscaled 2x to 1568x2720 pixels after rendering.

Suit-object counts are hard constraints. For any card whose source `count` is `null`, the prompt explicitly prohibits adding suit objects. The six object-only cards remain object-only.

Generated on 2026-09-07 from the checked-out repository sources.

## Artwork generation status

The prompt package is complete for all 78 cards. The clean rebuild removes every previous JPG and PNG before generation. Prompts request ultra-detailed, high-resolution artwork and PNG output. The image-generation service allows at most ten image generations per assistant turn; artwork is created in batches and the manifest records `generated` or `pending-generation` for each PNG.
"""
(OUT / "README.md").write_text(readme, encoding="utf-8")
print(f"Created {len(source['cards'])} prompt files in {PROMPTS}")
print(f"Character trait rows joined: {len(traits)}")
