def checkio(opacity):

    age = 0
    age_opac = 10000

    def fib(limit):
        fibs = []
        a, b = 0, 1
        while a <= limit:
            fibs.append(a)
            a, b = b, a + b
        return fibs

    while age_opac != opacity:
        age += 1
        if age in fib(age):
            age_opac -= age
        else:
            age_opac += 1

    return age


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
