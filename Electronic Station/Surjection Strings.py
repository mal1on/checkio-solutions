def isometric_strings(a, b):

    combs = []
    cdict = dict()
    result = True

    for ind, char in enumerate(a):
        ttuple = (char, b[ind])
        combs.append(ttuple)
        cdict[char] = b[ind]

    for x, y in combs:
        if y != cdict[x]:
            result = False
            break

    return result


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
