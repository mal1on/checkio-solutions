import re


def halloween_monsters(spell: str) -> int:

    monsters = sorted(['skeleton', 'ghost', 'jack', 'vampire',
                'witch', 'mummy', 'zombie', 'werewolf', 'frankenstein'], key=len)

    found = []
    for monster in monsters:
        while all(c in spell for c in monster):
            found.append(monster)
            for c in set(monster):
                spell = spell.replace(c, '', monster.count(c))
    print(found, spell)




halloween_monsters('tkjagchso') == 2               # jack, ghost
halloween_monsters('finhtiistchwwaerecnnkt') == 3  # witch, witch, frankenstein
