def checkio(first, second):

    result = {'and': 0, 'or': 0, 'xor': 0}
    first = list(map(int, str(bin(first)[2:]).lstrip('0')))
    second = list(map(int, str(bin(second)[2:]).lstrip('0')))

    for f in first:

        and_r, or_r, xor_r = [], [], []

        for s in second:
            and_r.append(f and s)
            or_r.append(f or s)
            xor_r.append(f ^ s)

        result['and'] += int(''.join(map(str, and_r)), 2)
        result['or'] += int(''.join(map(str, or_r)), 2)
        result['xor'] += int(''.join(map(str, xor_r)), 2)

    return sum(result.values())


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
