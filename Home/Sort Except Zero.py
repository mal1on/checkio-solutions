from typing import Iterable


def except_zero(items: list) -> Iterable:
    # your code here
    zeros = []
    for ind, item in enumerate(items):
        if item == 0:
            zeros.append(ind)
    no_zeros = sorted(list(filter(lambda item: item != 0, items)))
    for index in zeros:
        no_zeros.insert(index, 0)
    return no_zeros


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [
    1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
