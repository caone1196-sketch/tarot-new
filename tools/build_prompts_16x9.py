#!/usr/bin/env python3
"""Build 78 prompts for the 16:9 frameless manhua-style deck.

Style contract (approved on 17-the-star-16x9-nude-implied):
  - wide 16:9 full-bleed landscape, NO border / frame / ribbon / text
  - modern colored manhua style, heroine = the girl in refs/style-manhua.jpg
  - implied-nude museum style: garments stripped from scenes; hair, mist and
    shadow are the only coverings (positive wording only, no filter-bait)
Outputs -> prompts-16x9/  (prompts.json, prompts.txt, per-card/*.txt, README.md)
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import build_prompts as bp  # reuse SCENE_OVERRIDES + loaders

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "prompts-16x9")

# ---------------------------------------------------------------- substitutions
# Ordered, case-insensitive. Garment / nudity phrases -> natural covering vocab.
SUBS = [
    # ---- major arcana specifics
    (r"draped only in a transparent silk veil so fine it clings and reveals her bare body beneath, the veil slipping from one shoulder and streaming behind her",
     ", her long hair and the drifting morning mist streaming behind her"),
    (r"draping over cloaked shoulders", "draping over her bare shoulders"),
    (r"sitting up in bed at night", "sitting up in a dark rippling pool at night"),
    (r"bare torso with a length of silk slung low across her hips",
     "bare shoulders, her flowing hair and the soft shadow gracefully outlining her figure"),
    (r"bare shoulders and the soft line of her breasts veiled only by a drift of sheer gauze",
     "her long hair draped softly across her chest"),
    (r"draped only in a diaphanous transparent red silk veil so fine it clings to her curves and glows with warm candlelight against her skin, the gossamer-thin fabric slipping from one shoulder",
     "her loose hair slipping over one shoulder and glinting in the warm candlelight"),
    (r"draped only in a diaphanous transparent silk veil so fine it clings to her soft curves and glows with warm light against her skin, the gossamer fabric slipping from one shoulder",
     "her loose hair slipping over one shoulder and glowing in the warm light"),
    (r"draped only in a diaphanous transparent silk veil that clings to her soft curves and glows with warm light",
     "her long hair catching the warm light"),
    (r"in flowing transparent silk reclining softly",
     "reclining softly with long flowing hair"),
    (r"wrapped in loose sheer white silk with no armor",
     "wearing no armor, her long hair streaming in the wind"),
    (r"draped only in a loose sheer white silk gauze that slips from her bare shoulders and pools low around her hips, her bare back and the curve of one breast veiled and revealed by the golden lantern light",
     "her bare shoulders glowing in the golden lantern light, her long hair loose down her bare back"),
    (r"a length of sheer silk sliding fully off one shoulder to bare one breast and one hip",
     "her long hair sliding over one bare shoulder"),
    (r"draped in sheer black silk that veils and reveals her bare form",
     "her pale form softened by drifting shadow"),
    # ---- wands
    (r"nude but for a sheer transparent silk veil draped across her form",
     "her long hair draped across her form"),
    (r"nearly bare with only a wisp of sheer transparent silk draped across her form",
     "her long braid whipping in the wind"),
    (r"draped in a diaphanous transparent silk veil sliding off one shoulder",
     "her long hair sliding over one shoulder"),
    (r"draped only in a diaphanous transparent silk veil",
     "her long hair catching the sunlight"),
    (r"draped in a diaphanous transparent silk veil",
     "her long hair catching the sunlight"),
    # ---- cups
    (r"with silk fallen to her hip",
     "with her hair fallen to her hip"),
    (r"in a dark cloak slipping off one bare shoulder",
     "her head bowed, hair curtaining her face"),
    (r"in a deep crimson cloak walking away",
     "walking away wrapped in deepening crimson twilight shadow"),
    (r"in sheer summer dresses",
     "with flowers woven into their hair"),
    (r"silk slipping from one shoulder",
     "her hair slipping over one shoulder"),
    (r"she in slipping silk with one bare shoulder and the long line of her back to the light",
     "her long hair swept aside, baring the long line of her back to the light"),
    (r"in an open robe sliding off one shoulder",
     "her hair sliding over one shoulder"),
    (r"wearing a gown of antique WHITE SILK GAUZE so sheer and transparent that the light shines through it and the long line of her body reads clearly beneath",
     "moonlight shining through her long wet hair so the line of her body reads clearly beneath"),
    # ---- swords
    (r"in a very thin veil of antique silk gauze, almost transparent, her shoulders bare",
     "her shoulders bare, a thin antique ribbon binding her eyes"),
    (r"lying at rest on a stone tomb in a chapel",
     "lying at rest on a stone tomb in a chapel, her hair spread around her like a dark pool"),
    (r"nearly bare in only a sheer silk wisp",
     "her long braid whipping in the wind"),
    (r"in a flowing gown loosened from one shoulder and loosely bound",
     "loosely bound in flowing ribbons of shadow, her hair loose over one shoulder"),
    (r"her bare shoulder and back above the sheet",
     "her bare shoulder and back rising above the dark water"),
    (r"lying draped in crimson silk",
     "lying with her dark hair spread across the sand, touched crimson by dawn"),
    (r"wrapped in a single sheet of TRANSPARENT antique silk gauze, one shoulder and the curve of her breast left bare",
     "one bare shoulder luminous, her hair wrapped around her like a single sheet of mist"),
    (r"a cloaked young woman seated quietly in a boat",
     "a young woman shadow-hooded, seated quietly in a boat"),
    (r"in a flowing cape on a windy mound",
     "on a windy mound, her cape of flowing hair whipping in the wind"),
    # ---- pentacles
    (r"in an open workshop apron slipping off one shoulder",
     "her hair tied back and slipping over one bare shoulder"),
    (r"in an apron slipping off one shoulder, sleeves rolled",
     "with sleeves rolled up and her hair pinned back"),
    (r"wrapped in worn snow-dusted cloaks",
     "her bare shoulders dusted with snow"),
    (r"in rich robes",
     "adorned with golden armbands"),
    (r"in a sheer flowing gown that clings to breast and hip",
     "her long hair clinging in soft strands to her chest and hip"),
    (r"in an open robe studying",
     "her hair loose, studying"),
    # ---- hair / build metadata cleanups (from cards.json fields)
    (r"like a sleek silk curtain", "like a sleek dark curtain"),
    (r"cascading beneath a sheer gossamer veil", "cascading beneath a soft silver circlet"),
    (r"wrapped in sheer black silk", "wrapped in drifting black mist"),
    (r"drifting gently with white silk ribbons", "drifting gently with white ribbons"),
    (r"deep brown hair tucked under a travel cloak", "deep brown hair loose in the desert wind"),
    # ---- generic multi-figure nudity labels
    (r"two nude young women", "two young women"),
    (r"three nude maidens", "three maidens"),
    (r"a serene nude", "a serene"),
    (r"a slender nude", "a slender"),
    (r"a nude young woman", "a young woman"),
    (r"a nude woman", "a woman"),
    (r"\bnude\b", ""),
    (r"one breast bared", "her hair swept forward across her chest"),
    (r"\bbreasts\b", "chest"),
    (r"\bbreast\b", "chest"),
    (r"draped in diaphanous transparent silk veils standing", "with long flowing hair, standing"),
    # ---- targeted fixes verified by grammar audit
    (r"draped in sheer black silk upon a dark pedestal", "posed regally upon a dark pedestal"),
    (r"each draped in sheer transparent silk", "each with long flowing hair"),
    (r"draped only in a diaphanous transparent white silk veil that clings to her soft curves and streams softly behind her",
     "her long hair streaming softly behind her"),
    (r"both draped in diaphanous transparent silk veils and both with fair skin tones",
     "both with long flowing hair and both with fair skin tones"),
    # ---- catch-alls for any remaining garment wording
    (r",?\s*(?:draped|wrapped|cloaked|veiled|dressed)(?: only)? in (?:a |an |the )?(?:diaphanous |transparent |sheer |gossamer[- ]thin |loose |flowing |worn |rich |antique )*(?:red |white |black |crimson |summer )?(?:silk|gauze|veil|gown|dress|robe|cloak|drape|fabric|sash|sheet|garment)s?(?:\s+[a-z]+){0,3}",
     ", softly covered by drifting mist and flowing hair"),
    (r"\b(diaphanous|transparent|sheer|gossamer|silken)\b", "soft"),
    (r"\bsilk\b", "hair"),
    (r"\bgauze\b", "mist"),
    (r"\bveil(s)?\b", "drift of mist"),
    (r"\bgown(s)?\b", "cascade of hair"),
    (r"\bdress(ed|es)?\b", "adorned"),
    (r"\brobe(s)?\b", "cascade of hair"),
    (r"\bgarment(s)?\b", "mist"),
    (r"\bfabric(s)?\b", "mist"),
    (r"\bapron\b", "bare shoulders"),
    (r"\b(his|him)\b", "her"),
]

FLAG_RE = re.compile(
    r"\b(nude|naked|topless|unclothed|nudity|transparent|diaphanous|sheer|gossamer|silk|gauze|veil|gown|dress|robe|garment|fabric|cloak|drapery|apron|bodice|corset|stocking|underwear)\b",
    re.I,
)


def apply_subs(text):
    for pat, rep in SUBS:
        text = re.sub(pat, rep, text, flags=re.I)
    return text


def tidy(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r",{2,}", ",", text)
    text = re.sub(r"\s+-\s+", " - ", text)
    text = re.sub(r"\(\s*", "(", text)
    return text.strip().strip(",").strip()


# ---------------------------------------------------------------- special scenes
STAR_SCENE = (
    "the young woman standing waist-deep in a calm moonlit pool, the dark glassy waterline rising to just above her hips, "
    "seen from behind at a graceful three-quarter back angle, her bare back and bare shoulders luminous in the moonlight, "
    "the smooth line of her back descending into the glowing water, her long wet hair swept over one shoulder and hanging "
    "down across her collarbone and chest as nature's covering, soft silver mist floating low across the pool around her, "
    "one knee gently bending beneath the reflected glow, her pose serene and dignified like an antique goddess sculpture, "
    "both arms raised high pouring water from exactly two antique silver jugs, one jug in each hand, both fully visible. "
    "Above her shines one great radiant eight-pointed star surrounded by exactly seven smaller stars, distant blue mountains under the Milky Way"
)

NO_FIGURE = {"wands-ace", "wands-08", "cups-ace", "swords-ace", "swords-03", "pentacles-ace"}

# ---- implied-nude pose sentences (safe vocabulary only: bare/hair/mist/shadow)
NUDE_STAND = (
    "Her figure follows the classical canon - bare shoulders and bare back luminous in the light, "
    "the smooth unbroken line of her sides, her long flowing hair and soft drifting shadow her only covering, "
    "posed with the serene dignity of an antique goddess statue in a museum masterpiece."
)
NUDE_SEATED = (
    "Her figure follows the classical canon - bare shoulders and the smooth line of her back luminous, "
    "her long hair falling freely across her chest, soft shadow and drifting silver mist flowing over her lap "
    "as her only covering, enthroned with the serene dignity of an antique goddess statue in a museum masterpiece."
)
NUDE_RECLINE = (
    "She reclines like a classical Venus of the Renaissance masters - bare shoulders and the smooth flowing "
    "line of her shoulder and back, her long hair cascading softly across her chest, graceful shadow her only covering, "
    "serene and dignified like an antique goddess statue."
)
NUDE_RIDE = (
    "An equestrian goddess of a classical frieze - bare shoulders and bare back catching the light, "
    "her long hair streaming, soft mist and graceful shadow her only covering as she rides, serene and dignified."
)
NUDE_MULTI = (
    "Every woman follows the classical canon - bare shoulders and bare backs, long flowing hair and soft drifting "
    "mist as their only covering, each pose serene and dignified like antique goddess statues in a museum masterpiece."
)

POSE_SEATED = {
    "02-priestess", "04-emperor", "10-wheel", "11-justice", "swords-02", "swords-06", "swords-09",
    "cups-04", "cups-09", "cups-queen", "cups-king", "pentacles-04",
    "wands-queen", "wands-king", "swords-queen", "swords-king", "pentacles-queen", "pentacles-king",
}
POSE_RECLINE = {"03-empress", "swords-04", "swords-10", "wands-10"}
POSE_RIDE = {"13-death", "wands-knight", "cups-knight", "swords-knight", "pentacles-knight"}
POSE_MULTI = {
    "06-lovers", "cups-02", "cups-03", "cups-06", "cups-10", "wands-04", "wands-05", "wands-06",
    "20-judgement", "pentacles-03", "swords-05",
}


# ---- uniform pose: the approved three-quarter back angle (THE STAR formula)
def _uni(ctx=""):
    return (
        f"Seen from a graceful three-quarter back angle{ctx}, her bare back and bare shoulders luminous "
        "in the light, the smooth line of her back descending, her long hair swept over one shoulder and "
        "hanging down as nature's covering, serene and dignified like an antique goddess statue in a museum masterpiece."
    )


def nude_sentence(slug):
    if slug in POSE_SEATED:
        return _uni(" as she sits enthroned")
    if slug in POSE_RECLINE:
        return _uni(" as she reclines")
    if slug in POSE_RIDE:
        return _uni(" as she rides")
    if slug in POSE_MULTI:
        return (
            "Each woman seen from a graceful three-quarter back angle, bare backs and bare shoulders luminous "
            "in the light, long hair swept over one shoulder as nature's covering, each pose serene and dignified "
            "like antique goddess statues in a museum masterpiece."
        )
    return _uni()


# ---- bathing motif: per-card action sentence (water naturally covers the figure)
BATH_TAIL = (
    "Wet skin glistening in the light, warm steam and drifting silver mist rising around her, "
    "a serene classical bathing scene in a museum masterpiece."
)

BATH = {
    "00-fool": "She wades in a cliff-top spring pool above the morning mountains, one foot kicking a soft splash, the white rose laid on a sun-warmed stone at the pool's edge, the small white dog drinking beside the pool.",
    "01-magician": "A shallow black-stone ritual pool mirrors her beside the altar, the four suit objects still resting dry upon the altar stone, candlelit steam curling up.",
    "02-priestess": "She sits waist-deep in the sacred temple pool between the pillars, the mystery scroll held dry in her lap above the mirror-still water.",
    "03-empress": "She reclines in a great scallop-shell of clear water amid the golden wheat, ripe fruits floating beside her.",
    "04-emperor": "She reclines on the ram-carved throne set within a steaming thermae pool, thermal steam curling around the carved ram heads.",
    "05-hierophant": "She stands waist-deep in the marble baptismal pool before the temple pillars, one hand raised in blessing, the two acolytes kneeling at the pool's marble edge.",
    "06-lovers": "The two lovers stand hand in hand waist-deep in a clear forest pool beneath the angel, soft splashes and drifting steam around them.",
    "07-chariot": "The stone chariot thunders through a shallow sacred ford, wheels throwing arcs of spray, mist and spray veiling the charioteer's bare back.",
    "08-strength": "She stands waist-deep in a golden rose-ringed pool as she calmly closes the lion's jaws, the great lion drinking at the water's edge.",
    "09-hermit": "She sits waist-deep in a steaming mountain hot-spring on the bare peak, the lantern's golden light glowing across water and steam.",
    "10-wheel": "The great wheel rises from a sacred pool, silver cascades falling around it, the winged sphinx glistening with spray.",
    "11-justice": "She sits enthroned waist-deep in a mirror-still reflecting pool between the pillars, the scales and sword held above the water.",
    "12-hanged": "She hangs above a mirror-calm sacred pool, her loose hair dipping the water, rings of ripple spreading below her.",
    "13-death": "The black charger wades chest-deep through misty dawn shallows, spray and silver steam veiling the rider's bare back.",
    "14-temperance": "She pours between the two jugs while waist-deep in a twilight pool among the reeds, water spiraling between them in glowing ribbons.",
    "15-devil": "The chain-bound pair stand in a steaming obsidian hot-spring within the cavern, candlelight shimmering on the dark water.",
    "16-tower": "The falling figure plunges toward the dark plunge pool at the tower's base, the water erupting in a crown of golden spray.",
    "18-moon": "She stands waist-deep in a silver moonlit pool along the winding path between the towers, the wolf and the little dog watching from the shore.",
    "19-sun": "She kicks bright sprays of water in a sunlit pool beside the sunflower wall, warm mist turned golden.",
    "20-judgement": "The three rise from the calm shimmering waters, beads of shining water streaming from their open arms.",
    "21-world": "She dances within the great laurel wreath above a sacred spring, ribbons of falling water spiraling around her.",
    "wands-02": "She bathes in a cistern pool on the battlement, the globe of the world held dry above the water in one palm.",
    "wands-03": "She bathes waist-deep in the sunlit rowing pool, the three staves planted in their even diagonal row in the shallow water before her.",
    "wands-04": "The two women dance splashing through the shallow festal pool beneath the garlanded canopy, spray in the warm light.",
    "wands-05": "The five women dance in a splash war within a shallow meadow pool, spray and laughter, one wand still held upright in each hand.",
    "wands-06": "She bathes waist-deep in the stream as the six wands stand upright along the bank, admirers cheering from the shore.",
    "wands-07": "She bathes in a hilltop spring on the high crag, her great wand held upright above the water, six wands rising from the rocks below.",
    "wands-09": "She stands waist-deep in a quiet palisade pool, her hands resting on her one wand, the eight wands upright in the shallows behind her.",
    "wands-10": "She reclines with her feet in a warm spring beside the boulder, the bundled ten wands leaning against the stone.",
    "wands-page": "She stands waist-deep in a desert oasis pool, pyramids shimmering beyond, her one living wand held high.",
    "wands-knight": "The white horse splashes through a shallow desert oasis ford, the wand flourishing high, spray and steam around them.",
    "wands-queen": "Her lion-carved throne stands in the birch spring pool at the grove's edge, water lapping gently around it.",
    "wands-king": "Her flame-carved throne rises from the oak forest's clearing pool, golden light and drifting embers on the steaming water.",
    "cups-02": "The two women face one another waist-deep in a lily pool, raising their chalices in a tender toast above the water.",
    "cups-03": "The three maidens dance in a ring within a shallow sunlit pool, wreaths in their hair, splashes at every step.",
    "cups-04": "She sits waist-deep in the pool beneath the tree, arms crossed, regarding the three cups on the water.",
    "cups-05": "She stands bowed waist-deep in the misty river, three spilled chalices floating empty on the water.",
    "cups-06": "The two women stand waist-deep in the old courtyard fountain as they exchange the flower-filled chalice.",
    "cups-07": "She sits in a shallow glowing pool while seven cups float on the glowing water around her.",
    "cups-08": "She wades through misty moonlit shallows, leaving the eight stacked cups on the dark shore behind.",
    "cups-09": "She sits waist-deep in a warm marble pool beside the banquet table, the nine golden chalices arrayed on the shelf behind.",
    "cups-10": "The two women embrace waist-deep in the sunlit meadow pool beneath the rainbow of chalices.",
    "cups-page": "She kneels in the sea's edge shallows, the curious fish leaping from her chalice.",
    "cups-knight": "The white steed wades chest-deep through a glowing stream, spray and steam around rider and chalice.",
    "cups-queen": "Her shell throne stands in the sea shallows, waves lapping at her waist, sea foam sparkling.",
    "cups-king": "Her throne floats upon the rolling waves, water beading down its carved sides, a dolphin arcing beyond.",
    "swords-02": "She sits waist-deep in the still sea pool by the stones, the two swords crossed above the water, the moon rising.",
    "swords-04": "The chapel floor lies flooded with a shallow mirror of still rain water around the tomb, reflecting her and the swords.",
    "swords-05": "She stands waist-deep in the storm surf, three swords over her shoulder, watching her companions retreat along the shore.",
    "swords-06": "She leans over the boat's edge, her long hair trailing into the misty river below.",
    "swords-07": "She creeps through a shallow moonlit stream between the reeds, the five swords held high above the water.",
    "swords-08": "She stands bound in the ring of eight swords within a tide pool on the fortress shore, water still around her knees.",
    "swords-09": "Her face buried in her hands, wet hair streaming down her bare back, ripples still spreading around her.",
    "swords-10": "She lies in the shallow dawn surf, water sheeting gently around her beneath the ten upright swords.",
    "swords-page": "She splashes through a windy river ford, spray whipping, the raised sword flashing above the water with both hands.",
    "swords-knight": "The galloping horse charges through a storm-flooded ford, spray and steam exploding around rider and sword.",
    "swords-queen": "Her butterfly-carved throne stands in a mirror-still mountain lake above the sea of clouds, water at her waist.",
    "swords-king": "Her high stone throne rises from a still blue pool beneath clear skies, water calm around it.",
    "pentacles-02": "She dances in the waist-deep seaside terrace pool, juggling the two coins looped in the infinity ribbon above the water.",
    "pentacles-03": "The workshop's deep soaking basin steams beside her bench as she chisels the column.",
    "pentacles-04": "She sits waist-deep in a quiet vault pool, clutching one coin to her chest, one on her crown, two clearly visible beneath the clear water at her feet.",
    "pentacles-05": "She steps through the steaming snowmelt channel beside the glowing church, snow melting on her bare shoulders.",
    "pentacles-06": "She stands waist-deep among the marketplace fountain waters as she weighs the coins in the balanced scales.",
    "pentacles-07": "She leans on her staff waist-deep in the vineyard's irrigation pool, seven pentacles blooming on the vine above the water.",
    "pentacles-08": "She chisels at the bench, her feet soaking in a steaming basin beneath it, eight coins in a row along the bench edge.",
    "pentacles-09": "She stands waist-deep in the garden pool beneath the arbor, falcon on her glove, nine coins along the beam above.",
    "pentacles-10": "The matriarch's seat stands in the hall's shallow reflecting pool, ten coins gleaming in the tree-of-life emblem, the small dog drinking at its edge.",
    "pentacles-page": "She kneels in the flooded furrow's shallow water, studying the large coin in both hands, wet earth gleaming.",
    "pentacles-knight": "The steadfast horse stands in a flooded plow furrow, water beading on the golden pentacle held with calm reverence.",
    "pentacles-queen": "Her goat-carved throne stands in the garden pool among flowering water plants, water lapping gently, the rabbit watching from the bank.",
    "pentacles-king": "Her bull-carved throne rises from a pool among the blooming grapevines, calm water around it, vine tendrils trailing into the water.",
}

WATER_NOTE = {
    "wands-ace": "Below, a sacred spring pool glitters, the wand's fresh leaves dipping toward the water.",
    "swords-ace": "Below the peaks, a mirror-thin mountain tarn reflects the upright blade.",
    "pentacles-ace": "Beside the garden gateway, a lily-ringed fountain pool catches the golden coin's glow.",
}


def bath_sentence(slug):
    b = BATH.get(slug)
    if not b:
        return ""
    return b


def scene_for(c):
    ov = bp.SCENE_OVERRIDES.get(c["slug"], "__default__")
    if c["slug"] == "17-the-star":
        return STAR_SCENE
    if ov == "__default__":
        base = c["scene"]
    elif ov is None:  # provided samples -> fall back to original scene
        base = c["scene"]
    else:
        base = ov
    return tidy(apply_subs(base))


# ---------------------------------------------------------------- prompt template
def suit_lock(c):
    cnt = c.get("count")
    if cnt is None:
        return ("No suit objects anywhere in the scene: no wands, no chalices, no swords and no pentacle coins.", "")
    n = cnt["n"]
    obj = cnt["obj"]
    layout = re.sub(r"his cloak", "her flowing hair", cnt["layout"])
    layout = re.sub(r"\b(his|him)\b", "her", layout)
    lock = f"Hard count constraint: {layout}."
    anatomy = f"Exactly {n} {obj}."
    return lock, anatomy


def build_prompt(c):
    scene = scene_for(c)
    lock, anatomy = suit_lock(c)
    parts = []
    parts.append("A classical museum masterpiece scene, wide 16:9 full-bleed landscape composition, no border, no frame, no title and no text anywhere.")
    if c["slug"] in NO_FIGURE:
        parts.append(
            "Art style: the modern colored manhua / manga style of the reference image - clean linework, soft cel shading, "
            "vibrant colors, glossy highlights, crisp high-detail digital finish."
        )
        parts.append(f"Scene: {scene}. An elegant figure-free still-life composition, richly detailed and perfectly centered.")
        wn = WATER_NOTE.get(c["slug"])
        if wn:
            parts.append(wn)
    else:
        parts.append(
            "Art style: the modern colored manhua / manga style of the reference image - clean linework, soft cel shading, "
            "vibrant colors, glossy highlights, crisp high-detail digital finish. The heroine is the same girl as the main "
            "female character in the reference image, with her exact face, hairstyle and eyes."
        )
        desc = []
        if c.get("age"):
            age = str(c["age"]).strip()
            desc.append(f"She is {age}." if "old" in age else f"She is a {age} young woman.")
        if c.get("hair"):
            desc.append(tidy(apply_subs(f"Her hair: {c['hair']}.")))
        if c.get("build"):
            desc.append(tidy(apply_subs(f"Her build: {c['build']}.")))
        parts.append(f"Scene: {scene}.")
        parts.append(nude_sentence(c["slug"]))
        bs = bath_sentence(c["slug"])
        if bs:
            parts.append(bs)
        if desc:
            parts.append(" ".join(desc))
        parts.append(
            "Long flowing hair, drifting silver mist and elegant shadows lend every figure the graceful dignity "
            "of a Renaissance masterpiece."
        )
    if lock:
        parts.append(lock)
    if c["slug"] not in NO_FIGURE:
        parts.append(
            "Perfect anatomy - exactly two arms, two legs, one head and one body per figure, no extra or merged limbs, "
            "arms clearly separated from the torso, natural joints and fingers."
            + ((" " + anatomy) if anatomy else "")
        )
    elif anatomy:
        parts.append(anatomy)
    parts.append(
        "Tasteful museum standard - poetic, elegant and dignified, like a classical oil masterpiece."
    )
    parts.append(
        "Wide cinematic 16:9 landscape, luminous lighting, rich atmospheric depth, modern manhua fine-art illustration, "
        "high detail. Absolutely no text, no letters, no frame and no border anywhere in the image."
    )
    return tidy("\n\n".join(parts))


# ---------------------------------------------------------------- main
def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.join(OUT, "per-card"), exist_ok=True)
    cards = json.load(open(os.path.join(ROOT, "cards.json")))
    lst = cards if isinstance(cards, list) else cards.get("cards", cards)

    out = {}
    blocks = []
    flagged = []
    for c in lst:
        p = build_prompt(c)
        if FLAG_RE.search(p):
            flagged.append(c["slug"])
        out[c["slug"]] = {
            "title": c["title"],
            "group": c.get("group", ""),
            "no_figure": c["slug"] in NO_FIGURE,
            "prompt": p,
        }
        blocks.append(f"### {c['slug']} | {c['title']}\n{p}\n")
        with open(os.path.join(OUT, "per-card", c["slug"] + ".txt"), "w") as f:
            f.write(p + "\n")

    with open(os.path.join(OUT, "prompts.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    with open(os.path.join(OUT, "prompts.txt"), "w") as f:
        f.write("\n".join(blocks))

    print(f"built {len(out)} prompts -> {OUT}")
    print("flagged for manual review:", ", ".join(flagged) if flagged else "NONE")


if __name__ == "__main__":
    main()
