def checkio(time_string: str) -> str:
    h, m, s = time_string.split(':')
    h = h.zfill(2)
    h = bin(int(h[0]))[2:].zfill(2) + ' ' + bin(int(h[1]))[2:].zfill(4)
    m = m.zfill(2)
    m = bin(int(m[0]))[2:].zfill(3) + ' ' + bin(int(m[1]))[2:].zfill(4)
    s = s.zfill(2)
    s = bin(int(s[0]))[2:].zfill(3) + ' ' + bin(int(s[1]))[2:].zfill(4)

    print((h + ' : ' + m + ' : ' + s).replace('1', '-').replace('0', '.'))



checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
