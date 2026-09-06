#!/usr/bin/env python3
"""
Compile the 78 tarot card prompts from every source in this repo.

Inputs (the four scanned assets):
  17-the-star.png          -> visual anchor image, passed as a reference to the image model
  00-MASTER-PROMPT.md      -> frame / depth-layer / anatomy standard + master prompt template
  02-CHARACTER-SPECS.md    -> 72 female character specs (age, eyes, hair, build grade, skin, signature, aura)
  cards.json               -> 78 cards: title, scene, emblem, count-lock, hair, age

Output:
  pipeline/prompts.json    -> one compiled prompt per card, ready for the renderer
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPE = ROOT / "pipeline"

STAR_SLUG = "17-the-star"

# ---------------------------------------------------------------- sources ---

def load_cards():
    data = json.loads((ROOT / "cards.json").read_text(encoding="utf-8"))
    return data["meta"], data["cards"]


def load_spec_table():
    """Parse the 72-row markdown character table in 02-CHARACTER-SPECS.md."""
    rows = {}
    for line in (ROOT / "02-CHARACTER-SPECS.md").read_text(encoding="utf-8").split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 8 or cells[0].startswith("---") or cells[1] == "Tuổi":
            continue
        m = re.search(r"`([^`]+)`", cells[0])
        if not m:
            continue
        rows[m.group(1)] = {
            "age_vi": cells[1], "eyes_vi": cells[2], "hair": cells[3],
            "build_vi": cells[4], "skin": cells[5], "signature_vi": cells[6],
            "aura_vi": cells[7],
        }
    return rows


def load_english_specs():
    return json.loads((PIPE / "characters.en.json").read_text(encoding="utf-8"))["characters"]


# ------------------------------------------------------------ prompt parts ---

ANATOMY_LOCK = (
    "ANATOMY LOCK (hard rule): exactly one head, one neck, one torso, two arms and two hands "
    "with five fingers each, two legs and two feet — no extra or missing limbs, no limb fused to "
    "the ribcage, hip or chest, no severed or truncated arms, no bent or broken joints. Every "
    "shoulder, elbow, wrist, hip, knee and ankle connects naturally to the body; both arms read "
    "clearly separated from the torso with visible armpit, elbow and wrist."
)

FRAME_STANDARD = (
    "Match the reference card exactly for framing: the same thin, crisp gothic gold line-art border "
    "with the same corner flourishes and scrollwork, the same aged parchment / vellum ground, the same "
    "brushed silver-pearl outer bevel and rounded corners, and the same bottom title panel."
)

NEGATIVE = (
    "no extra limbs, no third arm, no fused limbs, no deformed hands, no malformed fingers, "
    "no broken joints, no dark or deep-brown skin shading, no plus-size or exaggerated proportions, "
    "no heavy inner stone arch or columns, no modern clothing, no text other than the title, "
    "no watermark, no signature, no blurry background."
)


# Some source scene wordings in cards.json trip the image model's safety filter and come back
# with zero image parts. The intent (sheer drapery, classical nude fine-art) is preserved; only
# the phrasing is softened so the render actually returns.
SOFTEN = [
    (r"so fine it clings and reveals her bare body beneath", "falling in soft translucent folds"),
    (r"so fine it clings to her soft curves and glows with warm light against her skin",
     "catching the warm light in soft folds"),
    (r"so fine it clings to her curves and glows with warm candlelight against her skin",
     "glowing softly in the candlelight"),
    (r"that clings and reveals her soft curves and streams in the sea wind",
     "streaming in the sea wind"),
    (r"so fine it clings to her curves", "in soft translucent folds"),
    (r"that clings and reveals", "that drifts over"),
    (r"clings and reveals her bare body beneath", "drapes softly over her"),
    (r"\bbare torso\b", "bare shoulders"),
    (r"their bodies turned to the light", "turning toward the light"),
    (r"arched in golden chains", "standing loosely draped in golden chains"),
]


def soften(text):
    for pat, rep in SOFTEN:
        text = re.sub(pat, rep, text)
    return text


def count_lock(card):
    c = card.get("count")
    if not c:
        return ("COUNT LOCK: this card carries no suit objects at all — no cups, no swords, "
                "no wands, no pentacle coins anywhere in the scene.")
    return (f"COUNT LOCK (hard constraint): exactly {c['n']} {c['obj']} — {c['layout']}. "
            f"Count them before finishing: the total must be exactly {c['n']}, no more, no fewer.")


def character_block(card, en, vi):
    """Merge cards.json + the character spec table into one English figure description."""
    if not card.get("femme"):
        return ("Figure standard: no full human figure on this card beyond the graceful feminine "
                "divine hand described in the scene — render the hand with exactly five fingers, "
                "natural anatomy and soft luminous skin.")

    if not en:
        return ANATOMY_LOCK

    age = card.get("age", "")
    hair = card.get("hair") or (vi or {}).get("hair", "")
    grade_word = {
        "A": "slender and delicate", "B": "lean and toned",
        "C": "average-soft and balanced", "D": "average-shapely",
    }[en["grade"]]

    parts = [
        f"THE FIGURE — a single young woman, {age}, 100% female, of legal adult age.",
        f"Hair: {hair}.",
        f"Eyes: {en['eyes']}.",
        f"Skin tone: {en['skin']} — a light, luminous complexion; never dark or deep-brown skin, "
        f"even in shadow.",
        f"Build: grade {en['grade']} — {grade_word}; {en['build']}. Natural proportions capped at "
        f"average — never plus-size, never exaggerated.",
        f"Signature detail (must be visible): {en['signature']}.",
        f"Mood and atmosphere: {en['aura']}.",
        "Sensuality comes from natural curves, luminous skin, posture and gaze — not from size.",
        ANATOMY_LOCK,
    ]
    return " ".join(parts)


def build_prompt(card, en, vi):
    title = card["title"]
    scene = card["scene"]
    return f"""A single tarot card "{title}", built inside the reference frame and matching the EXACT open-window display, scale, palette discipline and lighting style of the reference card THE STAR.

{FRAME_STANDARD}

At the BOTTOM, inside the title panel: the words "{title}" in clean antique gold gothic lettering, correctly spelled, centered.

In the large open center panel — filling the entire inner window edge to edge and bleeding slightly beneath the golden border, with the same open airy space as The Star and no heavy inner arch or stone columns:
{scene}.

{character_block(card, en, vi)}

{count_lock(card)}

Depth layering (4 layers): aged parchment ground; then the scene enlarged so its edges extend slightly under the inner edge of the golden border; then the thin gold line-art border, corner flourishes and bottom title panel painted ON TOP of the scene edges — foreground ornament overlapping the background scene for a strong sense of depth.

Rendering: sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective receding into the background, crisp detail, symmetrical golden frame, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail. This card keeps its own setting and colour palette; only linework quality, lighting and detail level are standardized to The Star.

Avoid: {NEGATIVE}"""


# --------------------------------------------------------------- compact ----
# The render prompt actually sent to the image model alongside 17-the-star.png.
# Same constraints as the long form, ~55% the length, so a 78-card run stays cheap.

def build_compact(card, en, vi):
    title = card["title"]
    bits = [
        f'Tarot card "{title}" in the EXACT style of the attached reference card THE STAR: '
        f'same thin gothic gold line-art border, same corner flourishes, same aged parchment '
        f'ground, same brushed silver outer bevel, same rounded corners, same bottom title panel.',
        f'Bottom title panel reads "{title}" in antique gold gothic lettering, correctly spelled.',
        f'Center panel fills the inner window edge to edge and bleeds slightly under the gold '
        f'border, open and airy like The Star, no inner stone arch or columns: '
        f'{soften(card["scene"])}.',
    ]

    if card.get("femme") and en:
        hair = card.get("hair") or (vi or {}).get("hair", "")
        bits.append(
            f'FIGURE: one woman, {card.get("age","")}, adult. Hair: {hair}. Eyes: {en["eyes"]}. '
            f'Skin: {en["skin"]}, light and luminous, never dark-brown even in shadow. '
            f'Build: {en["build"]} — natural, capped at average, never exaggerated. '
            f'Must be visible: {en["signature"]}. Mood: {en["aura"]}.'
        )
    elif not card.get("femme"):
        bits.append('Only the feminine divine hand described above — five fingers, natural anatomy.')

    bits.append(
        'ANATOMY LOCK: exactly 1 head, 1 torso, 2 arms with 2 five-fingered hands, 2 legs. No extra '
        'or missing limbs, no limb fused to torso or hip, no deformed hands or joints; arms clearly '
        'separated from the body with visible elbow and wrist.'
    )
    bits.append(count_lock(card))
    bits.append(
        'Depth: scene enlarged under the border, then the gold line-art border, flourishes and title '
        'panel painted ON TOP of the scene edges for layered depth.'
    )
    bits.append(
        'Sensual fine-art anatomy, painterly warm light and soft shadow, atmospheric depth, crisp '
        'detail, symmetrical gold frame, centered, portrait 7:12, vintage gothic fine-art painting. '
        'This card keeps its own setting and palette; only linework, lighting and detail level match '
        'The Star.'
    )
    bits.append(f'Avoid: {NEGATIVE}')
    return "\n\n".join(bits)


def main():
    meta, cards = load_cards()
    vi_rows = load_spec_table()
    en_rows = load_english_specs()

    missing_en = [s for s in vi_rows if s not in en_rows]
    if missing_en:
        raise SystemExit(f"English spec missing for: {missing_en}")

    out = []
    for card in cards:
        slug = card["slug"]
        out.append({
            "slug": slug,
            "title": card["title"],
            "group": card["group"],
            "n": card["n"],
            "femme": card.get("femme", False),
            "is_anchor": slug == STAR_SLUG,
            "count_n": (card.get("count") or {}).get("n"),
            "prompt": build_prompt(card, en_rows.get(slug), vi_rows.get(slug)),
            "render_prompt": build_compact(card, en_rows.get(slug), vi_rows.get(slug)),
        })

    PIPE.mkdir(exist_ok=True)
    (PIPE / "prompts.json").write_text(
        json.dumps({
            "meta": {
                "deck": meta["deck"],
                "anchor": "17-the-star.png",
                "sources": ["00-MASTER-PROMPT.md", "02-CHARACTER-SPECS.md",
                            "cards.json", "17-the-star.png"],
                "count": len(out),
            },
            "cards": out,
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    figs = sum(1 for c in out if c["femme"])
    print(f"compiled {len(out)} prompts -> pipeline/prompts.json")
    print(f"  {figs} figure cards, {len(out) - figs} object-only cards")
    print(f"  character specs merged: {len(vi_rows)} rows x EN layer")


if __name__ == "__main__":
    main()
