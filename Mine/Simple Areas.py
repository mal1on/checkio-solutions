from math import pi, sqrt

def simple_areas(*args):

    if len(args) == 1:
        return pi * (args[0] / 2) ** 2 
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        a, b, c = args[0], args[1], args[2]
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))





simple_areas(3) == 7.07
simple_areas(2, 2) == 4
simple_areas(2, 3) == 6
simple_areas(3, 5, 4) == 6
simple_areas(1.5, 2.5, 2) == 1.5