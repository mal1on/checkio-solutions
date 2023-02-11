from collections import deque


def letter_queue(commands):
    result = deque()
    for i in commands:
        c, a = i.split() if len(i.split()) == 2 else [i, '']
        if c == 'PUSH':
            result.append(a)
        elif c == 'POP' and result:
            result.popleft()

    return ''.join(result)


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
                        'POP',
                        'POP',
                        'PUSH Z',
                        'PUSH D',
                        'PUSH O',
                        'POP',
                        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
                         'POP',
                         'POP',
                         'PUSH Z',
                         'PUSH D',
                         'PUSH O',
                         'POP',
                         'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
