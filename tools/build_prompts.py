#!/usr/bin/env python3
"""Build 78 per-card image prompts from cards.json using 00-MASTER-PROMPT.md template.

Visual anchor: "the moon.png" (frame + inner painting standard),
secondary reference: "17-the-star.png".

NOTE: explicit-nudity wording from cards.json is normalised into
tasteful draped-fabric wording; all other scene content is preserved.
"""
import json, os, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "deck-78" / "prompts"
OUT.mkdir(parents=True, exist_ok=True)

# ---- wording normalisation (keeps scene, removes explicit nudity) ----
SUBS = [
    (r"\bdraped only in a (?:diaphanous |fine |delicate )?transparent (\w+ )?silk veil so fine it clings and reveals her bare body beneath\b",
     r"robed in a flowing \1silk gown that drapes softly over her figure"),
    (r"\bdraped only in a (?:diaphanous |fine |delicate )?transparent\b", "robed in a flowing opaque"),
    (r"\bdraped only in\b", "robed in"),
    (r"\bclad only in\b", "robed in"),
    (r"\bwearing only\b", "robed in"),
    (r"\btransparent silk veil\b", "flowing silk gown"),
    (r"\btransparent silk\b", "flowing silk"),
    (r"\bsheer transparent\b", "softly flowing"),
    (r"\bdiaphanous transparent\b", "softly flowing"),
    (r"\btransparent\b", "flowing"),
    (r"\bdiaphanous\b", "flowing"),
    (r"\bsheer\b", "flowing"),
    (r"\bsemi-nude\b", "elegantly robed"),
    (r"\bfully nude\b", "elegantly robed"),
    (r"\bnude\b", "elegantly robed"),
    (r"\bnaked\b", "robed"),
    (r"\bbare body\b", "graceful figure"),
    (r"\bbare torso\b", "draped torso"),
    (r"\bbare breasts?\b", "draped bodice"),
    (r"\bone breast bared\b", "a softly draped bodice"),
    (r"\bbreasts?\b", "bodice"),
    (r"\bbared\b", "draped"),
    (r"\bbare(?=\s+(?:shoulder|back|hip|thigh|leg|arm|skin|form|figure|chest|belly|waist|midriff|body))",
     "softly draped"),
    (r"\bbare\b", ""),
    (r"\brevealing\b", "graceful"),
    (r"\bslipping from one shoulder\b", "gathered at one shoulder"),
    (r"\bvoluptuous\b", "gracefully curved"),
    (r"\bclings to her soft curves\b", "falls in soft folds"),
    (r"\bclings and reveals her soft curves\b", "falls in soft folds"),
    (r"\bfalls softly and reveals her soft curves\b", "falls in soft folds"),
    (r"\bclings and\b", "falls softly and"),
    (r"\bclings to (her|the) (curves|bodice|hip[s]?|form|figure|body)\b", r"drapes over \1 \2"),
    (r"\bclings\b", "drapes"),
    (r"\bveils and reveals\b", "softly drapes"),
    (r"\bveiled and revealed by\b", "warmly lit by"),
    (r"\bveiled only by\b", "covered by"),
    (r"\bslung low across her hips\b", "wrapped about her waist"),
    (r"\bslips from her (?:softly draped )?shoulders and pools low around her hips\b",
     "falls from her shoulders to the ground in deep folds"),
    (r"\bslides fully off one shoulder to (?:softly draped )?\b", "drapes across "),
    (r"\bleft softly draped\b", "softly draped"),
    (r"\bfallen to her hip\b", "draped to her hip"),
    (r"\bin golden chains\b", "beside golden chains"),
    (r"\barched in golden chains\b", "standing beside golden chains"),
    (r"\bwith no armor\b", "with a jewelled breastplate"),
    (r"\bapron slipping off one shoulder\b", "apron"),
    (r"\bopen robe\b", "robe"),
    (r"\bflowing flowing\b", "flowing"),
    (r"\bsoftly draped softly draped\b", "softly draped"),
    (r"\ba (?=elegantly robed\b)", "an "),
    (r"\berotic\b", "romantic"),
    (r"\bsensual\b", "graceful"),
    (r"\bseductive\b", "serene"),
]

def normalise(text: str) -> str:
    out = text
    for pat, rep in SUBS:
        out = re.sub(pat, rep, out, flags=re.I)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


def character_spec(c: dict) -> str:
    bits = []
    if c.get("age"):
        bits.append(f"She is {c['age']}")
    if c.get("build"):
        bits.append(c["build"])
    if c.get("hair"):
        bits.append(f"hair: {c['hair']}")
    if not bits:
        return ""
    s = "; ".join(bits) + "."
    return normalise(s)


ANATOMY = ("ANATOMY LOCK: exactly one head, one torso, two arms and two hands with five fingers each, "
           "two legs — no extra or missing limbs, no limbs fused to the torso, every joint naturally connected.")

MODESTY = ("All figures are respectfully and fully covered in flowing opaque fabric — "
           "no nudity, no transparent clothing, no exposed anatomy.")


def count_lock(c: dict) -> str:
    ct = c.get("count")
    if not ct:
        return "COUNT LOCK: no suit objects (no cups, no swords, no wands, no pentacles) anywhere in the scene unless named above."
    return (f"COUNT LOCK (HARD): exactly {ct['n']} {ct['obj']} — {ct['layout']}. "
            f"Do not add or remove any; the count must be exactly {ct['n']}.")


TEMPLATE = """A single tarot card "{title}" built inside the reference frame, matching the EXACT open window display, scale, lighting and painterly fine-art style of the reference card THE MOON: keep the intricate thin golden line-art border in vintage gothic style, the four ornate gold corner flourishes, the double thin gold rule inset, and the aged parchment / deep atmospheric background texture.

At the BOTTOM: the title "{title}" centered in clean antique-gold blackletter/gothic capitals, identical typeface, size, gold gradient and drop shadow to the word "THE MOON" on the reference card.

In the large open center panel (filling the entire inner window edge to edge and bleeding slightly beneath the golden border, open and airy with no inner stone arch or column barriers):
{scene}. {character} {count}

{anatomy}
{modesty}

Depth layering: enlarge the scene so its edges extend slightly beneath the inner edge of the golden border, then paint the thin golden line-art border and corner flourishes ON TOP of the scene edges — foreground ornament overlapping the background content for a strong sense of depth.

Refined fine-art anatomy, painterly warm lighting against soft atmospheric shadows, rich aerial perspective and depth receding into the background, perfectly symmetrical golden frame, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail.
"""


def build(c: dict) -> str:
    return TEMPLATE.format(
        title=c["title"],
        scene=normalise(c["scene"]),
        character=character_spec(c),
        count=count_lock(c),
        anatomy=ANATOMY,
        modesty=MODESTY,
    )


def main():
    data = json.loads((ROOT / "cards.json").read_text(encoding="utf-8"))
    cards = data["cards"]
    index = []
    for i, c in enumerate(cards, 1):
        p = OUT / f"{c['slug']}.txt"
        p.write_text(build(c), encoding="utf-8")
        index.append({"i": i, "slug": c["slug"], "title": c["title"], "group": c["group"],
                      "prompt_file": f"prompts/{c['slug']}.txt",
                      "image_file": f"cards/{c['slug']}.png"})
    (ROOT / "deck-78" / "index.json").write_text(
        json.dumps({"deck": data["meta"]["deck"], "anchor": "the moon.png",
                    "secondary_ref": "17-the-star.png", "count": len(index),
                    "cards": index}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(index)} prompts to {OUT}")


if __name__ == "__main__":
    main()
