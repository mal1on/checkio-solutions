rn = {'1':'I', '5':'V', '10':'X', '50':'L', '100':'C', '500':'D', '1000':'M'}

def checkio(data):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    ths = m[data // 1000]
    hs = c[(data % 1000) // 100]
    ts = x[(data % 100) // 10]
    os = i[data % 10]

    print(ths+hs+ts+os)




checkio(6) == 'VI'
checkio(76) == 'LXXVI'
checkio(13) == 'XIII'
checkio(44) == 'XLIV'
checkio(3999) == 'MMMCMXCIX'
