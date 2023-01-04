from typing import Iterable


def replace_biggest(data: list[int]) -> Iterable[int]:
    # your code here
    result = []
    for ind, el in enumerate(data[:-1]):
        result.append(max(data[ind + 1:]))
    result.append(-1)

    return result if data else []


print("Example:")
print(list(replace_biggest([17, 18, 5, 4, 6, 1])))

# These "asserts" are used for self-checking
assert list(replace_biggest([17, 18, 5, 4, 6, 1])) == [18, 6, 6, 6, 1, -1]
assert list(replace_biggest([1, 2, 3, 4, 5, 6])) == [6, 6, 6, 6, 6, -1]
assert list(replace_biggest([1, 1, 1])) == [1, 1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
