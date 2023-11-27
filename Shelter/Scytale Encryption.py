from itertools import zip_longest


def scytale_decipher(ciphertext, crib):

    results = []

    for c in range(1, len(ciphertext)):

        groups = []

        for i in range(0, len(ciphertext), c):
            groups.append(ciphertext[i:i + c])

        decoded = ''.join([''.join(g)
                           for g in list(zip_longest(*groups, fillvalue='_'))])

        if crib in decoded.replace('_', ''):
            results.append(decoded.replace('_', ''))

    return results[0] if len(results) == 1 else None


if __name__ == "__main__":
    print("Example:")
    print(scytale_decipher("aaaatctwtkdn", "dawn"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert scytale_decipher("aaaatctwtkdn", "dawn") == "attackatdawn"
    assert scytale_decipher("hdoeerlallrdow", "world") == "hellodearworld"
    assert (
        scytale_decipher(
            "totetshpmeecisendysescwticsriasraytlaegphet", "sicret")
        == None
    ), "Crib is not in plaintext"
    assert (
        scytale_decipher("aaaatctwtkdn", "at") == None
    ), "More than one possible decryptions"

    print("Coding complete? Click 'Check' to earn cool rewards!")
