def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    strings = []
    for pos, char in enumerate(line):
        sub_string = char
        for next_char in line[pos + 1:]:
            if next_char == char:
                sub_string += next_char
            else:
                break
        strings.append(sub_string)

    return len(max(strings, key=len)) if line else 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
