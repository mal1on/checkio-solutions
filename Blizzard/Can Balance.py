from typing import Iterable

def can_balance(weights: Iterable) -> int:
    # your code here
    result = -1
    size = len(weights) - 1

    def w_cal(comb):
        weight = 0
        for ind, item in enumerate(comb):
            weight += item * (len(comb) - ind)
        return weight    

    for ind, item in enumerate(weights):
        comb_1, comb_2 = weights[:ind], weights[ind + 1:]
        if w_cal(comb_1) == w_cal(comb_2[::-1]):
            result = ind

    print(result)            





# 6*2 + 1*1 == 5*1 + 4*2
can_balance([6, 1, 10, 5, 4]) == 2
# 10*1 == 3*1 + 2*2 + 1*3
can_balance([10, 3, 3, 2, 1]) == 1