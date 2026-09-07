import sys, pathlib
HEAD = ('Use the attached tarot card ONLY as style/frame reference: copy its exact thin golden gothic '
        'line-art border, four ornate gold corner flourishes, double thin gold rule inset, painterly '
        'atmospheric rendering, and the identical antique-gold blackletter title typeface at the bottom. '
        'Produce a NEW tarot card titled "{t}" with that title in the same gold blackletter capitals at bottom center. '
        'Center scene fills the whole inner window edge to edge, no inner arch or columns: ')
TAIL = (' Fully clothed, modest, no nudity, no transparent fabric. Scene bleeds slightly beneath the inner '
        'edge of the golden border with gold ornament painted on top of the scene edges for depth. '
        'Portrait 7:12, vintage gothic fine-art illustration, high detail.')
for slug in sys.argv[1:]:
    p = pathlib.Path('deck-78/prompts')/f'{slug}.txt'
    lines = p.read_text(encoding='utf-8').splitlines()
    title = lines[2].split('"')[1]
    scene = lines[5]
    anat = lines[7]
    print('<<<'+slug)
    print(HEAD.format(t=title)+scene+' '+anat+TAIL)
    print('>>>')
