def repeat_inside(line: str) -> str:
    """
    first the longest repeating substring
    """
    # your code here
    substrings = [line[x:x + y]
                  for y in range(1, 1 + len(line)) for x in range(1 + len(line) - y)]
    repeated = []
    for substring in substrings:
        for rep in range(2, len(line) + 1):
            if substring * rep in line:
                repeated.append(substring * rep)
    return max(repeated, key=len, default='')


print("Example:")
print(repeat_inside("aaaaa"))

assert repeat_inside("aaaaa") == "aaaaa"
assert repeat_inside("aabbff") == "aa"
assert repeat_inside("aababcc") == "abab"
assert repeat_inside("abc") == ""
assert repeat_inside("abcabcabab") == "abcabc"

print("The mission is done! Click 'Check Solution' to earn rewards!")
