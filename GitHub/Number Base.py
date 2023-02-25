def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except:
        return -1




checkio("AF", 16) == 175
checkio("101", 2) == 5
checkio("101", 5) == 26
checkio("Z", 36) == 35
checkio("AB", 10) == -1
