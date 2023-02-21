def checkio(n, m):
    n = str(bin(n))[2:].zfill(20)
    m = str(bin(m))[2:].zfill(20)
    return len(list(filter(lambda a: len(set(a)) > 1, zip(n, m))))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
