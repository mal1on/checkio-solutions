def safe_pawns(pawns: set) -> int:

    indexes = set()

    for pawn in pawns:

        row = int(pawn[1])
        col = ord(pawn[0]) - 96
        indexes.add((row, col))

    safe = 0

    for row, col in indexes:

        if (row - 1, col - 1) in indexes or (row - 1, col + 1) in indexes:

            safe += 1

    return safe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
