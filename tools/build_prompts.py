#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the per-card generation prompt for all 78 tarot cards, strictly following
the master template in 00-MASTER-PROMPT.md and the per-card data in cards.json
(scene / hair / age / build / count-locks). Outputs cards/prompts.json.
"""
import json, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(REPO, "cards.json"), encoding="utf-8"))
cards = data["cards"]

# --------------------------------------------------------------------------
# Scene overrides — reconcile stale scene texts in cards.json with the deck's
# hard standards (00-MASTER-PROMPT.md §2: 100% female figures 18–25; skin
# palette §1.1 of 02-CHARACTER-SPECS.md) and with each card's count lock.
# --------------------------------------------------------------------------
SCENE_OVERRIDES = {
    "06-lovers": (
        "two nude young women standing hand in hand beneath a great winged angel, "
        "the first lover turned three-quarters toward the viewer with silk fallen to "
        "her hip and her lover's hand at the small of her back, the tree of knowledge "
        "with a serpent behind the first, the tree of flames behind the second"
    ),
    "cups-02": (
        "two nude young women facing one another in a tender toast, the first turned "
        "three-quarters toward the viewer with one arm across her breast, each raising "
        "one chalice toward the other, a caduceus with a lion head above them"
    ),
    "cups-10": (
        "two blissful young women embracing in a sunlit meadow, she in slipping silk "
        "with one bare shoulder and the long line of her back to the light, her arms "
        "wound around the other's waist, ten chalices arranged along a rainbow arc, a "
        "cottage and a flower garden beyond"
    ),
    "swords-06": (
        "a cloaked young woman seated quietly in a boat gliding across a misty river, "
        "a second young woman ferry guide poling the boat behind her, six swords "
        "standing upright along the boat"
    ),
    "pentacles-03": (
        "a young woman sculptor in an open workshop apron slipping off one shoulder, "
        "hair loose, chiseling a column while two admiring young women companions — an "
        "architect in a headscarf and a maiden in a flowing dress — study her work, "
        "three coins set in the stone arch above"
    ),
    "pentacles-05": (
        "a shivering young woman beggar wrapped in worn snow-dusted cloaks walking "
        "past a glowing church in the snow, her eyes raised to the tall stained-glass "
        "window, five coins shining in the window"
    ),
    "pentacles-06": (
        "a generous young woman in rich robes holding balanced scales before two "
        "kneeling maidens in a warm marketplace, three golden pentacle coins stacked "
        "on the left pan and three stacked on the right pan, her open hand extended "
        "in charity toward the maidens"
    ),
    "pentacles-10": (
        "a sunlit family hall — a warm young matriarch with a braided crown of "
        "honey-brown hair seated at the center, two young women of her kin standing "
        "beside her, a small dog resting at her feet, ten coins in a tree-of-life "
        "pyramid emblem on the wall behind"
    ),
    "20-judgement": (
        "a serene winged female angel draped only in a diaphanous transparent silk "
        "veil that clings to her soft curves and glows with warm light, gently lifting "
        "a golden trumpet with a white banner; below, rising from calm waters, three "
        "beautiful young women with softly open arms turning toward the divine light — "
        "one fair-skinned with flowing blonde hair, one warm-toned with dark auburn "
        "curls, and one light honey-toned with tight dark curls — each with a distinct "
        "face and figure, each draped in sheer transparent silk"
    ),
    "wands-03": (
        "a serene young woman merchant seen from behind on a high rocky headland, "
        "standing tall with her long back line turned to us, draped only in a "
        "diaphanous transparent silk veil that clings and reveals her soft curves and "
        "streams in the sea wind, one hand raised to shade her eyes as she gazes far "
        "out to sea, three leafy staves planted upright in one evenly spaced diagonal "
        "row before her, sailing ships on a golden sea"
    ),
    "wands-06": (
        "a serene young woman on a white horse, draped in a diaphanous transparent "
        "silk veil, a laurel wreath on her brow, one crowned wand raised gently in her "
        "hand, five graceful young women admirers behind her each holding one wand "
        "upright well above shoulder height"
    ),
    "17-the-star": None,  # provided sample — never regenerated
    "18-moon": None,      # provided sample — never regenerated
}

# --------------------------------------------------------------------------
# Style prelude — identical for every card (keeps border/type/ornament synced)
# --------------------------------------------------------------------------
FRAME_BLOCK = (
    'Create a single tarot card titled "{TITLE}", matching the EXACT frame, scale, '
    "border and lighting of the FIRST reference image (THE STAR): the intricate thin "
    "golden line-art border in vintage gothic style, aged parchment background, corner "
    "flourishes, oval medallion, and a bottom ribbon banner carrying the title "
    '"{TITLE}" in clean antique gold lettering styled exactly like "THE STAR" lettering.'
)

CENTER_OPEN = (
    "The large open center panel fills the entire inner window edge to edge and bleeds "
    "slightly beneath the golden border, with no heavy inner arch barriers."
)

CHARACTER_STYLE = (
    "Render her in the same sensual fine-art painterly character style, face painting "
    "quality and warm lighting treatment as the young woman in the SECOND reference "
    "image (THE MOON), but with her own unique features as described below."
)

ANATOMY_LOCK = (
    "Perfect anatomy — exactly two arms, two legs, one head, one body, no extra or "
    "merged limbs, arms clearly separated from the torso, natural joints and fingers."
)

DEPTH_BLOCK = (
    "Depth layering: let the scene extend slightly beneath the inner edge of the golden "
    "border, then paint the thin golden border, corner flourishes, oval medallion and "
    "ribbon banner ON TOP of the scene edges so the ornament overlaps the background "
    "content. Painterly warm lighting, subtle shadows, rich atmospheric depth, "
    "symmetrical golden frame, perfectly centered, portrait 7:12, vintage gothic "
    "fine-art illustration, high detail."
)

def count_lock(c):
    ck = c.get("count")
    if ck is None:
        return ("No suit objects anywhere on the card: no wands, no chalices, no "
                "swords and no pentacle coins.")
    n, obj = ck["n"], ck["obj"]
    layout = ck.get("layout", "")
    return (f'Count lock, HARD RULE: exactly {n} {obj}. {layout} '
            f"Count them carefully — {n}, no more, no fewer.")

def character_spec(c):
    if c.get("femme"):
        parts = []
        if c.get("age"):
            parts.append(f"She is a {c['age']} young woman.")
        if c.get("hair"):
            parts.append(f"Her hair: {c['hair']}.")
        if c.get("build"):
            parts.append(f"Her build: {c['build']}, slender to soft-average feminine "
                         "figure, natural curves, never heavy.")
        return " ".join(parts)
    return "No human figure in the scene — only the described subject."

def build_prompt(c):
    title = c["title"]
    scene = SCENE_OVERRIDES.get(c["slug"], c["scene"]).strip()
    spec = character_spec(c)
    lock = count_lock(c)
    lines = [
        FRAME_BLOCK.format(TITLE=title),
        "",
        CENTER_OPEN,
        "",
        f"Scene: {scene}",
        "",
        spec,
    ]
    if c.get("femme"):
        lines += ["", CHARACTER_STYLE, "", ANATOMY_LOCK]
    lines += ["", lock, "", DEPTH_BLOCK]
    return "\n".join(lines)

out = {}
for c in cards:
    skip = c["slug"] in ("17-the-star", "18-moon")
    out[c["slug"]] = {
        "n": c.get("n"),
        "title": c["title"],
        "group": c["group"],
        "femme": c.get("femme"),
        "provided_sample": skip,
        "prompt": "" if skip else build_prompt(c),
    }

# sanity: all fields used, no empty scene
assert len(out) == 78
os.makedirs(os.path.join(REPO, "cards"), exist_ok=True)
with open(os.path.join(REPO, "cards", "prompts.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

print("built", len(out), "prompts -> cards/prompts.json")
for s in ("00-fool", "01-magician", "03-empress", "10-wheel", "wands-05",
          "cups-09", "swords-08", "pentacles-10"):
    print("=" * 20, s)
    print(out[s]["prompt"][:700])
