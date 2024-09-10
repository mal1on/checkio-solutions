def quadratic_roots(a, b, c):

    d = b*b - 4*a*c
    sd = pow(d, 1/2)

    if d > 0:
        return [int((-b+sd)/2*a), int((-b-sd)/2*a)]
    elif d == 0:
        return [int((-b+sd)//2*a), int((-b+sd)/2*a)]
    return ["No real roots"]




print(quadratic_roots(1, -3, 2))
print(quadratic_roots(1, 0, -1))
print(quadratic_roots(1, 2, 1))
print(quadratic_roots(1, 0, 1))
