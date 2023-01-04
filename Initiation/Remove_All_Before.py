from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:

    result = items[::-1]

    if border in items:
        for item in items:
            if item != border:
                result.pop()
            else:
                break
    else:
        result = items[::-1]

    return result[::-1]


print(remove_all_before([1, 2, 3, 4, 5], 3))
print(remove_all_before([1, 1, 5, 6, 7], 2))
