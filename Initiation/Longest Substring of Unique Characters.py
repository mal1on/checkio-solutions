def longest_substr(s: str) -> int:

    temp = ''
    strings = ['']

    for i in range(len(s)):
        for ch in s[i:]:
            if ch not in temp:
                temp += ch
            else:
                strings.append(temp)
                temp = ch

    return len(max(strings, key=len))


print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
