def middle(text):

    result = ''
    if len(text) % 2 == 0:
        result = text[len(text) // 2 - 1] + text[len(text) // 2]
    else:
        result = text[len(text) // 2]

    return result


if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
