def non_empty_lines(text: str) -> int:

    lines = text.split('\n')
    result = 0

    for line in lines:

        if line and not all([item == ' ' for item in line]):
            result += 1

    return result


if __name__ == '__main__':
    print("Example:")
    print(non_empty_lines('one simple line\n'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
