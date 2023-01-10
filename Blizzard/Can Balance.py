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

    return result


if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
