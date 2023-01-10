def checkio(number: int) -> int:
    print(str(bin(number)).count('1'))




checkio(4) == 1
checkio(15) == 4
checkio(1) == 1
checkio(1022) == 9
