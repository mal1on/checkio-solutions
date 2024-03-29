def create_intervals(data):
    """
    Create a list of intervals out of set of ints.
    """
    if data:
        data = sorted(data)
        prev = data[0]
        temp = [prev]
        ints = []
    else:
        return []

    for el in data[1:]:
        if el - prev == 1:
            temp.append(el)
        else:
            ints.append(temp)
            temp = [el]
        prev = el
    ints.append(temp)

    return [(i[0], i[-1]) for i in ints]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print("Almost done! The only thing left to do is to Check it!")
