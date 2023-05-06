from itertools import permutations as pm

D = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def count_morse(message: str, letters: str) -> int:

    print(len([perm for perm in pm(letters) if message == ''.join([D[c] for c in perm])]))



count_morse("-------.", "omg") == 2
count_morse(".....-.-----", "morse") == 4
count_morse("-..----.......-..-.", "xtmisuf") == 4
