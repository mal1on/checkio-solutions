from string import ascii_lowercase as alphabet

def to_decrypt(cryptotext, delta):

    result = ''
    for char in cryptotext:
        if char in alphabet:
            index = alphabet.find(char) + delta
            if index >= 26:
                index = delta - (26 - alphabet.find(char))
            result += alphabet[index]
        elif char == ' ':
            result += char


    print(result)


to_decrypt("!d! [e] &f*", -3) == "a b c"
to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
