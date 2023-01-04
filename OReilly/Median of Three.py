from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    # your code here

    def med(items):
        items.sort()
        ind, rem = divmod(len(items), 2)
        return (items[ind - 1], items[ind])[rem]

    result = els[:2]

    for ind, item in enumerate(els[2:]):
        result.append(med(sorted([item, els[ind], els[ind + 1]])))

    return result


print('Example:')
print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

assert median_three([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 2, 3, 4, 5, 6]
assert median_three([1]) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
