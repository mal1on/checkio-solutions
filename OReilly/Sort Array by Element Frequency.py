from typing import Iterable


def frequency_sort(items):

    return sorted(sorted(items, key=items.index), key=items.count, reverse=True)


print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))

assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
    4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
    4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
