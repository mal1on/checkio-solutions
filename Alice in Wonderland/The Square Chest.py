from typing import List


def checkio(lines_list: List[List[int]]) -> int:
    """Return the quantity of squares"""

    small_s = 0
    med_s = 0
    big_s = []
    wall = len(lines_list) / 4
    lines_list = [set(item) for item in lines_list]
    for dot in [1, 2, 3, 5, 6, 7, 9, 10, 11]:
        if all(w in lines_list for w in [{dot, dot + 1}, {dot + 1, dot + 5},
                                         {dot + 4, dot + 5}, {dot, dot + 4}]):
            small_s += 1
    for dot in [1, 2, 5, 6]:
        if all(w in lines_list for w in [{dot, dot + 1}, {dot + 1, dot + 2},
                                         {dot + 2, dot + 6}, {dot + 6,
                                                              dot + 10}, {dot + 9, dot + 10},
                                         {dot + 8, dot + 9}, {dot + 4, dot + 8}, {dot, dot + 4}]):
            med_s += 1
    big = [list(range(1, 5)), list(range(4, 17, 4)),
           list(range(13, 17)), list(range(1, 14, 4))]
    for wall in big:
        temp_wall = []
        for ind, num in enumerate(wall):
            if ind + 1 < len(wall):
                temp_wall.append({num, wall[ind + 1]})
        big_s.append(temp_wall)
    big_s = [a for b in big_s for a in b]
    big_s = 1 if all(con in lines_list for con in big_s) else 0
    return sum([small_s, med_s, big_s])


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                   [10, 14], [12, 16], [14, 15], [15, 16]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]])
            == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10],
                     [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")
