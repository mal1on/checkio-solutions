def checkio(time_string: str) -> str:
    h, m, s = time_string.split(':')
    h = h.zfill(2)
    h = bin(int(h[0]))[2:].zfill(2) + ' ' + bin(int(h[1]))[2:].zfill(4)
    m = m.zfill(2)
    m = bin(int(m[0]))[2:].zfill(3) + ' ' + bin(int(m[1]))[2:].zfill(4)
    s = s.zfill(2)
    s = bin(int(s[0]))[2:].zfill(3) + ' ' + bin(int(s[1]))[2:].zfill(4)

    return (h + ' : ' + m + ' : ' + s).replace('1', '-').replace('0', '.')


if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(
        "21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(
        "23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
