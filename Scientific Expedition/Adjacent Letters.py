def adjacent_letters(line: str) -> str:
    # your code here
    result = []
    turn = 0
    while turn < len(line):
        if len(result) != 0 and result[-1] == line[turn]:
            result.pop(-1)
            turn += 1
        else:
            result.append(line[turn])
            turn += 1
    return ''.join(result)                            


print("Example:")
print(adjacent_letters("abbaca"))

# These "asserts" are used for self-checking
assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
