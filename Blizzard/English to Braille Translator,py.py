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


def braille_page(text: str) -> list[list[int]]:
    # your code here
    print(LETTERS_NUMBERS)
    return []



print(braille_page('42'))
