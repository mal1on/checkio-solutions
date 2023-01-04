def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    # your code here
    result = []
    for row in range(rows):
        if row % 2 == 0:
            result.append([col for col in range(start, cols + start)])
        else:
            result.append(sorted([col for col in range(start, cols + start)], reverse=True))
        start += cols

    return result          


print("Example:")
print(create_zigzag(3, 5))

assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")