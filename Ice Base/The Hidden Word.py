def checkio(text, word):

    text = text.replace(' ', '').lower()
    row_s = col_s = row_e = col_e = 0
    for ind, line in enumerate(text.split('\n')):
        if word in line:
            row_s = row_e = ind + 1
            col_s = line.index(word) + 1
            col_e = col_s + len(word) - 1

    if not any([row_s, col_s, row_e, col_e]):
        longest = len(max(text.split('\n'), key=len))
        edited = []
        for line in text.split('\n'):
            if len(line) < longest:
                edited.append(line + ((longest - len(line)) * '#'))
            else:
                edited.append(line)
        rotated = [''.join(l) for l in list((zip(*edited)))]
        for ind, line in enumerate(rotated):
            if word in line:
                row_s = line.index(word) + 1
                row_e = row_s + len(word) - 1
                col_s = col_e = ind + 1

    return [row_s, col_s, row_e, col_e]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert (
        checkio(
            """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""",
            "ten",
        )
        == [2, 14, 2, 16]
    )
    assert (
        checkio(
            """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""",
            "noir",
        )
        == [4, 16, 7, 16]
    )
print("Coding complete? Click 'Check' to earn cool rewards!")
