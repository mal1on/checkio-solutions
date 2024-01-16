def create_intervals(data):
    """
    Create a list of intervals out of set of ints.
    """
    data = sorted(data)
    prev = data[0]
    temp = [prev]
    ints = []

    for el in data[1:]:
        if el - prev == 1:
            temp.append(el)
        else:
            ints.append(temp)
            temp = [el]
        prev = el
    ints.append(temp)
    result = [(i[0], i[-1]) for i in ints]
    print(result)




create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]
