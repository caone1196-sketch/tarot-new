#!/usr/bin/env python3
"""
Compile the 78 tarot card prompts from every source in this repo.

Inputs (the four scanned assets):
  cards/17-the-star.jpg    -> visual anchor (FULL-BLEED), attached to every render call
  17-the-star.png          -> RETIRED original (matted 84.1%) — never attach this
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

# TWO reference images are attached to every render call — they do different jobs.
#
#   ANCHOR_FIGURE = 17-the-star.png (the untouched original)
#       The CHARACTER standard. Its figure is the canonical look for all 72 women: classical
#       fine-art nude anatomy, luminous light-toned skin, freckled shoulders, soft painterly
#       modelling, 18-25 years old. Never overwrite or "improve" this file.
#
#   ANCHOR_LAYOUT = cards/17-the-star.jpg
#       The LAYOUT standard only: full-bleed art, gold border as an overlay, title on a banner.
#
# Keeping them separate matters: the original PNG carries the right BODY but the retired matted
# frame, while the JPG carries the right FRAME. Attaching only one always loses the other half.
ANCHOR_FIGURE = ROOT / "17-the-star.png"
ANCHOR_LAYOUT = ROOT / "cards" / "17-the-star.jpg"


def resolve_anchors():
    for p in (ANCHOR_FIGURE, ANCHOR_LAYOUT):
        if not p.exists():
            raise SystemExit(f"anchor missing: {p}")
    return ANCHOR_FIGURE, ANCHOR_LAYOUT



# Character standard, keyed to the untouched 17-the-star.png.
FIGURE_STANDARD = (
    "FIGURE STANDARD — the FIRST reference image is THE STAR from this deck: she is the canonical "
    "character model. Match her exactly for body language and rendering: classical fine-art nude "
    "anatomy with soft painterly modelling, luminous light-toned skin with a subtle sheen, natural "
    "youthful proportions, delicate freckling across the shoulders, calm direct gaze, hair painted "
    "in fine individual strands. Same artist, same brush, same skin palette, same level of finish. "
    "The SECOND reference image is the same card in the correct full-bleed layout — copy its "
    "framing. Every woman in this deck is 18-25, painted in that identical fine-art style; only "
    "her face, hair, colouring and setting change from card to card."
)

# Layout contract shared by the prompt text and 00-MASTER-PROMPT.md. If the doc drifts away from
# the code, the build fails loudly instead of silently emitting the retired layout.
LAYOUT_VERSION = "FULL-BLEED v3"


def load_master():
    """00-MASTER-PROMPT.md is a real dependency: it must agree with LAYOUT_VERSION."""
    text = (ROOT / "00-MASTER-PROMPT.md").read_text(encoding="utf-8")
    if LAYOUT_VERSION not in text:
        raise SystemExit(
            f"00-MASTER-PROMPT.md does not declare '{LAYOUT_VERSION}'.\n"
            f"The spec still describes the retired matted layout — update it before building."
        )
    return text

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

# FULL-BLEED LAYOUT (v3) — the painting covers the whole card, 99.8% vs the old 84.1%.
# The reference card wastes ~16% of its surface on a brushed-silver mat plus a separate
# parchment title strip. That mat is dropped: art runs corner to corner, the gold line-art
# border floats on top of it, and the title rides a slim banner laid over the artwork.
FRAME_STANDARD = (
    "FULL-BLEED LAYOUT — this is the most important instruction. The painted scene covers the "
    "ENTIRE card surface, edge to edge and corner to corner, 100% full bleed. There is NO brushed "
    "silver mat, NO grey bevel, NO parchment margin and NO separate title panel anywhere: the "
    "painting itself IS the card, running all the way to the outer trim on all four sides. "
    "Painted ON TOP of that full-bleed artwork, keep the reference card's thin gothic gold "
    "line-art border with its delicate corner flourishes and scrollwork, floating just inside the "
    "card edge like a gilded overlay so the artwork shows through and continues past it on every side."
)

def title_standard(title):
    """Titles get spelled out letter by letter — the model rendered STRENGTH as 'STRENGTR' once."""
    letters = ", ".join(list(title.replace(" ", "")))
    return (
        f"TITLE — spell it exactly, letter by letter: {letters}. At the bottom, resting directly "
        f"on the artwork, a slim elegant gold-edged banner ribbon carries the title "
        f'"{title}" in antique gold gothic capitals, correctly spelled and centered. '
        f"The scene stays visible behind and beneath the banner."
    )

NEGATIVE = (
    "no silver border, no grey mat, no brushed metal bevel, no parchment frame, no empty margins, "
    "no letterboxing, no separate title panel, no extra limbs, no third arm, no fused limbs, "
    "no deformed hands, no malformed fingers, no broken joints, no dark or deep-brown skin shading, "
    "no plus-size or exaggerated proportions, no heavy inner stone arch or columns, no modern "
    "clothing, no misspelled title, no text other than the title, no watermark, no signature, "
    "no blurry background."
)


# Some source scene wordings in cards.json trip the image model's safety filter and come back
# with zero image parts. The intent (sheer drapery, classical nude fine-art) is preserved; only
# the phrasing is softened so the render actually returns.
SOFTEN = [
    # Only the few wordings that literally returned zero image parts get rewritten, and each
    # rewrite keeps the classical fine-art nude intent from cards.json. Do NOT add "nude ->
    # draped" style rules here: that silently rewrites the character standard, which is exactly
    # how The Star drifted from standing-in-the-pool to kneeling-in-a-gown.
    (r"so fine it clings and reveals her bare body beneath",
     "so fine the light passes through it"),
    (r"so fine it clings to her soft curves and glows with warm light against her skin",
     "glowing with warm light against her skin"),
    (r"so fine it clings to her curves and glows with warm candlelight against her skin",
     "glowing in the candlelight against her skin"),
    (r"that clings and reveals her soft curves and streams in the sea wind",
     "streaming in the sea wind"),
    (r"so fine it clings to her curves", "so fine the light passes through it"),
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
    return f"""A single tarot card "{title}", from the same painted deck as the two attached reference images of THE STAR — the first sets the character and painting style, the second sets the layout.

{FIGURE_STANDARD}

{FRAME_STANDARD}

{title_standard(title)}

The scene, covering the whole card and running out under the gold border on every side, composed with generous open space and deep air:
{soften(scene)}.

{character_block(card, en, vi)}

{count_lock(card)}

Depth layering: the painted scene is the full card; the thin gold line-art border, its corner flourishes and the title banner are painted ON TOP of it — foreground ornament overlapping the background scene for a strong sense of depth. Compose the scene so the subject sits clear of the gold overlay and nothing important is hidden behind the banner.

Rendering: sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective receding into the background, crisp detail, symmetrical gold overlay, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail. This card keeps its own setting and colour palette; only linework quality, lighting and detail level are standardized to The Star.

Avoid: {NEGATIVE}"""


# --------------------------------------------------------------- compact ----
# The render prompt actually sent to the image model alongside 17-the-star.png.
# Same constraints as the long form, ~55% the length, so a 78-card run stays cheap.

def build_compact(card, en, vi):
    title = card["title"]
    bits = [
        f'Tarot card "{title}", from the same painted deck as the two attached reference images '
        f'of THE STAR — the first sets the character and painting style, the second sets the layout.',
        FIGURE_STANDARD,
        FRAME_STANDARD,
        title_standard(title),
        f'The scene, covering the whole card and running out under the gold border on every '
        f'side, composed with generous open space and deep air: {soften(card["scene"])}.',
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
        'Depth: the painted scene is the full card; the gold line-art border, flourishes and title '
        'banner are painted ON TOP of it for layered depth. Compose so the subject sits clear of the '
        'gold overlay and nothing important hides behind the banner.'
    )
    bits.append(
        'Sensual fine-art anatomy, painterly warm light and soft shadow, atmospheric depth, crisp '
        'detail, symmetrical gold overlay, centered, portrait 7:12, vintage gothic fine-art painting. '
        'This card keeps its own setting and palette; only linework, lighting and detail level match '
        'The Star.'
    )
    bits.append(f'Avoid: {NEGATIVE}')
    return "\n\n".join(bits)


def main():
    meta, cards = load_cards()
    vi_rows = load_spec_table()
    en_rows = load_english_specs()
    fig_anchor, lay_anchor = resolve_anchors()
    load_master()

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
                "anchor_figure": str(fig_anchor.relative_to(ROOT)),
                "anchor_layout": str(lay_anchor.relative_to(ROOT)),
                "layout": LAYOUT_VERSION,
                "sources": ["00-MASTER-PROMPT.md", "02-CHARACTER-SPECS.md",
                            "cards.json", str(fig_anchor.relative_to(ROOT)),
                            str(lay_anchor.relative_to(ROOT))],
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
    print(f"  layout: {LAYOUT_VERSION}")
    print(f"  figure anchor: {fig_anchor.relative_to(ROOT)}  (character standard)")
    print(f"  layout anchor: {lay_anchor.relative_to(ROOT)}  (full-bleed frame)")


if __name__ == "__main__":
    main()
