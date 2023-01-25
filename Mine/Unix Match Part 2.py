import re

re_dict = {'*': '.*', '?': '.', '!': '^'}
re_special = ['.']


def unix_match(filename: str, pattern: str) -> bool:

    re_pattern = ''
    for char in pattern:
        if char in re_dict.keys():
            re_pattern += re_dict[char]
        elif char in re_special:
            re_pattern += '\\' + char
        else:
            re_pattern += char

    return True if re.match(re_pattern, filename) else False


print("Example:")
print(unix_match("log1.txt", "log[1234567890].txt"))

# These "asserts" are used for self-checking
assert unix_match("log1.txt", "log[1234567890].txt") == True
assert unix_match("log1.txt", "log[!1].txt") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
