def nonogram_encode(data: list[str]) -> list[list[list[int]]]:
    # your code here

    def rotate(data):
        result = []
        for ind in range(len(data[0])):
            temp = ''
            for row in data:
                temp += row[ind]
            result.append(temp)
        return result

    def clue(side):
        result = []
        for item in side:
            temp = []
            temp_sub = 0
            for sub in item:
                if sub == 'X':
                    temp_sub += 1
                else:
                    if temp_sub:
                        temp.append(temp_sub)
                    temp_sub = 0
            if temp_sub != 0:
                temp.append(temp_sub)
            result.append(temp)

        max_len = len(max(result, key=len))
        filled = []
        for item in result:
            while len(item) < max_len:
                item = [0] + item
            filled.append(item)

        return filled

    rc = clue(data)
    cols = rotate(data)
    cc = list(map(list, zip(*clue(cols))))

    return [cc, rc]


print("Example:")
print(nonogram_encode([" X X ", "X X X", " X X "]))

# These "asserts" are used for self-checking
assert nonogram_encode([" X X ", "X X X", " X X "]) == [
    [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
    [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
]
assert nonogram_encode(["X"]) == [[[1]], [[1]]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
