def sorted_groups(items: list[int]) -> list[int]:
    # your code here
    result = []
    temp1 = []
    for item in items:
        temp2 = temp1.copy()
        temp1.append(item)
        if temp1 == sorted(temp1) or temp1 == sorted(temp1, reverse=True):
            continue
        else:
            result.append(temp2)
            temp1 = [item]
    result.append(temp1)
    return [item for group in sorted(result) for item in group]


print("Example:")
print(sorted_groups([5, 1, 5, 0, 5]))

# These "asserts" are used for self-checking
assert sorted_groups([]) == []
assert sorted_groups([5]) == [5]
assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
