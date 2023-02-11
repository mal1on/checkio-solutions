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


letter_queue(['PUSH A',
              'POP',
              'POP',
              'PUSH Z',
              'PUSH D',
              'PUSH O',
              'POP',
              'PUSH T']) == 'DOT'
letter_queue(['POP', 'POP']) == ''
letter_queue(['PUSH H', 'PUSH I']) == 'HI'
letter_queue([]) == ''
