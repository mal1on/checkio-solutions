def missing_number(items: list[int]) -> int:
    # your code here
    diffs = []
    items.sort()
    for a, b in zip(items, items[1:]):
        diffs.append(b - a)
    diff = min(diffs)
    whole = [items[0]]
    for item in range(len(items)):
        whole.append(whole[-1] + diff)
    return sum(whole) - sum(items)


print("Example:")
print(missing_number([1, 4, 2, 5]))

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
