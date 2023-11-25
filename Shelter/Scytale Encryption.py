from typing import Optional


def scytale_decipher(ciphertext: str, crib: str) -> Optional[str]:
    # your code here
    return ""




scytale_decipher('aaaatctwtkdn', 'dawn') == 'attackatdawn'
scytale_decipher('hdoeerlallrdow', 'world') == 'hellodearworld'
scytale_decipher('totetshpmeecisendysescwticsriasraytlaegphet', 'sicret') == None     #Crib is not in plaintext
scytale_decipher('aaaatctwtkdn', 'at') == None                                        #More than one possible decryptions
