from itertools import zip_longest

def scytale_decipher(ciphertext, crib):

    results = []

    for c in range(1, len(crib) + 1):

        groups = []

        for i in range(0, len(ciphertext), c):
            groups.append(ciphertext[i:i+c])

        decoded = ''.join([''.join(g) for g in list(zip_longest(*groups, fillvalue ='_'))])

        if crib in decoded:
            results.append(decoded.rstrip('_'))


    print(results[0] if len(results) == 1 else None)




scytale_decipher('aaaatctwtkdn', 'dawn') == 'attackatdawn'
scytale_decipher('hdoeerlallrdow', 'world') == 'hellodearworld'
scytale_decipher('totetshpmeecisendysescwticsriasraytlaegphet', 'sicret') == None     #Crib is not in plaintext
scytale_decipher('aaaatctwtkdn', 'at') == None                                        #More than one possible decryptions
