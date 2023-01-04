from typing import Tuple
Coordinate = Tuple[int, int]


def square_board(side: int, token: int, steps: int) -> Coordinate:

    board = []

    turn = side
    for x in range(side):
        turn -= 1
        board.append((side - 1, turn))
    turn = side - 1
    for x in range(side - 2):
        turn -= 1
        board.append((turn, 0))
    turn = -1
    for x in range(side):
        turn += 1
        board.append((0, turn))
    turn = 0
    for x in range(side - 2):
        turn += 1
        board.append((turn, side - 1))

    move = token + steps
    if move >= len(board):
        move = move % len(board)

    return board[move]


if __name__ == '__main__':
    print("Example:")
    print(square_board(4, 1, 4))
    assert square_board(4, 1, 4) == (1, 0)
    assert square_board(6, 2, -3) == (4, 5)

    print("Coding complete? Click 'Check' to earn cool rewards!")
