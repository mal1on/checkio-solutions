def weak_point(matrix):

    cols = []
    col = []
    a, b = 0, 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            col.append(matrix[y][x])
        cols.append(col)
        col = []
    weakest_col = min(sum(col) for col in cols)
    weakest_row = min(sum(row) for row in matrix)

    for ind, row in enumerate(matrix):
        if sum(row) == weakest_row:
            #print(row, sum(row))
            a = ind
            break

    for ind, col in enumerate(cols):
        if sum(col) == weakest_col:
            #print(col, sum(col))
            b = ind
            break

    return [a, b]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)
                      ), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
