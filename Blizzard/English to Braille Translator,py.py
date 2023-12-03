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

    first_row, second_row, third_row, result = [], [], [], []
    count = 1

    for b in brailles:
        if count < 10:
            first_row.extend([b[0][0], b[0][1], 0])
            second_row.extend([b[1][0], b[1][1], 0])
            third_row.extend([b[2][0], b[2][1], 0])
            count += 1
        else:
            first_row.extend([b[0][0], b[0][1]])
            second_row.extend([b[1][0], b[1][1]])
            third_row.extend([b[2][0], b[2][1]])
            result.extend([first_row, second_row, third_row, [0] * 29])
            first_row, second_row, third_row = [], [], []
            count = 1

    if len(brailles) < 10:
        result.extend([first_row[:-1], second_row[:-1], third_row[:-1]])
    elif len(brailles) % 10 == 0:
        result = result[:-1]
    else:
        ext = [(29 - len(first_row)) * [0]][0]
        result.extend([first_row + ext, second_row + ext, third_row + ext])

    return result


print("Example:")
print(braille_page("hello 1st World!"))

# These "asserts" are used for self-checking
assert braille_page("hello 1st World!") == [
    [
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
    ],
    [
        1,
        1,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        1,
    ],
    [
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
    ],
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],
    [
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        0,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
    ],
    [
        0,
        0,
        0,
        0,
        1,
        0,
        1,
        1,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],
]
assert braille_page("42") == [
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
]
assert braille_page("CODE") == [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
