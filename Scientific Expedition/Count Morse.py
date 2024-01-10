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

    result = 0
    queue = [(message, letters)]

    while queue:
        msg, let = queue.pop(0)
        poss = [c for c in let if msg.startswith(D[c])]

        for char in poss:
            m = msg.removeprefix(D[char])
            l = let.replace(char, '')
            if m and l:
                queue.append((m, l))
            elif not m and not l:
                result += 1

    return result


print("Example:")
print(count_morse("-------.", "omg"))

# These "asserts" are used for self-checking
assert count_morse("-------.", "omg") == 2
assert count_morse(".....-.-----", "morse") == 4
assert count_morse("-..----.......-..-.", "xtmisuf") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
