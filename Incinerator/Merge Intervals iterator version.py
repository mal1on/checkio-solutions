def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    # Your code here
    result = []

    for i in intervals:
        if not result or result[-1][1] + 1 < i[0]:
            result.append(i)
        else:
            result[-1] = result[-1][0], max(result[-1][1], i[1])

    return iter(result)


print(list(merge_intervals(iter([(1, 4), (2, 6), (8, 10), (12, 19)])))) == [(1, 6), (8, 10), (12, 19)]
# list(merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))) == [(1, 12)]
# list(merge_intervals(iter([(1, 5), (6, 10), (10, 15), (17, 20)]))) == [(1, 15), (17, 20)]
