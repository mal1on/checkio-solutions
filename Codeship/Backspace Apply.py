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

    print(''.join(result))




backspace_apply("name") == "name"
backspace_apply("name#") == "nam"
backspace_apply("na##me") == "me"
backspace_apply("nam#e#") == "na"
