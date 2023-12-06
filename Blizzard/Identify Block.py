def identify_block(numbers):

    result = None

    diff = max(numbers) - min(numbers)
    order = sorted(numbers)
    if diff == 3 or diff == 12:
        result = 'I'
    elif order[1] - order[0] == 1 and order[3] - order[2] == 1:
        if diff == 5:
            result = 'O'
        elif diff == 4:
            result = 'S'
        elif diff == 6:
            result = 'Z'
    elif order[1] - order[0] == 4 and order[3] - order[2] == 4 and diff == 9:
        result = 'S'
    elif order[1] - order[0] == 3 and order[3] - order[2] == 3 and order[0] in [2, 3, 4, 6, 7, 8]:
        result = 'Z'
    elif order[2] - order[0] == 2:
        base = order[:2]
        if max(numbers) - base[1] == 4:
            result = 'T'
        elif diff == 6:
            result = 'J'
        elif diff == 4:
            result = 'L'
    elif order[3] - order[1] == 2:
        base = order[1:]
        if base[1] - min(numbers) == 4:
            result = 'T'
        elif diff == 6:
            result = 'J'
        elif diff == 4:
            result = 'L'
    elif diff == 8:
        if order[2] - order[1] == 1:
            result = 'T'
        elif order[3] - order[1] == 7:
            result = 'J'
    elif diff == 9 and (order[1] - order[0] == 1 or order[3] - order[2] == 1):
        result = 'L'

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
    print('"Run" is good. How is "Check"?')
