from typing import Iterable, Any


def remove_after_kth(items: list[Any], k: int) -> Iterable[Any]:
    # your code here
    result = []
    for item in items:
        if result.count(item) < k:
            result.append(item)
    return result


print("Example:")
print(list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)))

# These "asserts" are used for self-checking
assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]

print("The mission is done! Click 'Check Solution' to earn rewards!")
