def checkio(opacity):
    age = 0
    age_opac = 10000

    def fib(limit):
        fibs = []
        a, b = 0, 1
        while a <= limit:
            fibs.append(a)
            a, b = b, a + b
        return fibs    

    while age_opac != opacity:
        age += 1
        if age in fib(age):
            age_opac -= age
        else:
            age_opac += 1        

    print(age)                





checkio(10000) == 0
checkio(9999) == 1
checkio(9997) == 2
checkio(9994) == 3
checkio(9995) == 4
checkio(9990) == 5

    