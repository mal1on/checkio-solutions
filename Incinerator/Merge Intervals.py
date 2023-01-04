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

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [
        (1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [
        (1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')
