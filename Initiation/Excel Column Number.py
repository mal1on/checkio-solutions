def column_number(name: str) -> int:
    # your code here
    result = 0
    for ind, let in enumerate(name[::-1]):
        result += (ord(let) - 64) * 26**ind

    return result


print("Example:")
print(column_number("AA"))

# These "asserts" are used for self-checking
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701

print("The first mission is done! Click 'Check' to earn cool rewards!")
