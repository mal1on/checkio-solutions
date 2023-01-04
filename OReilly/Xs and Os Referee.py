from typing import List


def checkio(game_result: List[str]) -> str:

    combs = [item for item in game_result]
    combs += [''.join(l) for l in list(zip(*game_result))]
    combs.append(''.join([game_result[i][i] for i in range(3)]))
    combs.append(''.join([game_result[i][abs(i - 2)] for i in range(3)]))

    if any(l == 'XXX' for l in combs):
        return 'X'
    elif any(l == 'OOO' for l in combs):
        return 'O'
    else:
        return 'D'


if __name__ == "__main__":
    print("Example:")
    print(checkio(["X.O", "XX.", "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
