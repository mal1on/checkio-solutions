def checkio(n, m):
    n = str(bin(n))[2:].zfill(20)
    m = str(bin(m))[2:].zfill(20)
    print(len(list(filter(lambda a: len(set(a)) > 1, zip(n, m)))))




checkio(117, 17) == 3
checkio(1, 2) == 2
checkio(16, 15) == 5
