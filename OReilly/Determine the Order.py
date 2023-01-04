def checkio(data):

    data = [''.join(dict.fromkeys(d)) for d in data]
    unique = sorted(set(''.join(data)))
    result = ''

    while unique:
        for char in unique:
            if not any(char in d[1:] for d in data):
                result += char
                break
        data = [d.replace(char, '') for d in data]
        unique.remove(char)

    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", "Paste in"
    assert (
        checkio(["a", "b", "c"]) == "abc"
    ), "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]
                   ) == "dfrtyg", "Concatenate and paste in"
