def convert(code: int) -> list[list[int]]:

    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(
    map(
        convert,
        [
            1,
            3,
            9,
            25,
            17,
            11,
            27,
            19,
            10,
            26,
            5,
            7,
            13,
            29,
            21,
            15,
            31,
            23,
            14,
            30,
            37,
            39,
            62,
            45,
            61,
            53,
            47,
            63,
            55,
            46,
            26,
        ],
    )
)
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {
    ",": convert(2),
    "-": convert(18),
    "?": convert(38),
    "!": convert(22),
    ".": convert(50),
    "_": convert(36),
}
WHITESPACE = convert(0)


from string import ascii_lowercase, ascii_uppercase


def braille_page(text: str) -> list[list[int]]:

    brailles = []

    for ch in text:
        if ch in ascii_lowercase:
            brailles.append(LETTERS_NUMBERS[ord(ch) - 97])
        elif ch in ascii_uppercase:
            brailles.append(CAPITAL_FORMAT)
            brailles.append(LETTERS_NUMBERS[ord(ch) - 65])
        elif ch.isdigit():
            brailles.append(NUMBER_FORMAT)
            brailles.append(LETTERS_NUMBERS[ord(ch) - 49])
        elif ch in PUNCTUATION.keys():
            brailles.append(PUNCTUATION[ch])
        elif ch == ' ':
            brailles.append([[0, 0], [0, 0], [0, 0]])

    # result = [[e[0], e[1], 0] for b in list(zip(*brailles)) for e in b]

    result = []
    row = []
    count = 0

    for b in list(zip(*brailles)):
        for e in b:
            if count < 9:
                temp = []
                temp.append(e[0])
                temp.append(e[1])
                temp.append(0)
                row.extend(temp)
                count += 1
            else:
                temp = []
                temp.append(e[0])
                temp.append(e[1])
                row.extend(temp)
                result.append(row)
                result.extend([[0] * 29])

                count = 0
                row = []

    print(result)

    return result




print(braille_page('hello 1st World!'))
