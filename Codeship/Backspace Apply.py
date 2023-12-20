def backspace_apply(val: str) -> str:

    result = []

    for ch in val:
        if ch == '#':
            if result:
                result.pop()
                continue
            else:
                continue
        result.append(ch)

    return ''.join(result)


print("Example:")
print(backspace_apply("thna#m##e"))

assert backspace_apply("name") == "name"
assert backspace_apply("name#") == "nam"
assert backspace_apply("na##me") == "me"
assert backspace_apply("nam#e#") == "na"
assert backspace_apply("##name") == "name"
assert backspace_apply("name######") == ""
assert backspace_apply("nam######e") == "e"
assert backspace_apply("n###ame") == "ame"
assert backspace_apply("thna#m##e") == "the"
assert backspace_apply("oppo##r##t##u###nity") == "nity"

print("Not bad! Click 'Check' to earn cool rewards!")



