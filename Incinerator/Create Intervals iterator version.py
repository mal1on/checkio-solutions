def create_intervals(data):
    """
    Create a list of intervals out of set of ints.
    """

    lefts = [l for l in data if l - 1 not in data]
    rights = [r for r in data if r + 1 not in data]

    return list(zip(lefts, rights))


list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
                                      (1, 5), (7, 8), (12, 12)]
list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
                                      (1, 8)]
