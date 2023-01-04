def not_order(data: list[int]) -> int:
    # your code here
    in_order = sorted(data)
    count = 0
    for ind, item in enumerate(in_order):
        if item != data[ind]:
            count += 1
    return count


print("Example:")
print(not_order([1, 1, 4, 2, 1, 3]))

assert not_order([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
