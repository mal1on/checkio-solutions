def is_majority(items: list[bool]) -> bool:
    # your code here
    trues = 0
    falses = 0
    for condition in items:
        if condition:
            trues += 1
        else:
            falses += 1
    return trues > falses


print("Example:")
print(is_majority([True, True, False, True, False]))

assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
