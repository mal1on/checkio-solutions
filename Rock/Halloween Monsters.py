from collections import Counter as ct


def halloween_monsters(spell: str) -> int:

    monsters = ['skeleton', 'ghost', 'jack', 'vampire',
                'witch', 'mummy', 'zombie', 'werewolf', 'frankenstein']

    counts = []
    for turn in range(len(monsters)):
        found = []
        working_spell = spell
        for monster in monsters:
            while all(ct(working_spell)[char] >= ct(monster)[char] for char in ct(monster)):
                found.append(monster)
                for c in monster:
                    working_spell = working_spell.replace(c, '', 1)
        counts.append(len(found))
        monsters = monsters[1:] + monsters[:1]

    return max(counts)


if __name__ == "__main__":
    assert halloween_monsters("casjokthg") == 2, "jack ghost"
    assert halloween_monsters(
        "leumooeeyzwwmmirbmf") == 3, "mummy zombie werewolf"
    assert halloween_monsters(
        "nafrweiicttwneshhtikcn") == 3, "witch witch frankenstein"
    assert halloween_monsters(
        "kenoistcepajmlvre") == 2, "skeleton vampire (not jack)"
    assert halloween_monsters(
        "miaimavrurymepepv") == 2, "vampire vampire (not mummy)"
    print("Your spell seem to be okay. It's time to check.")
