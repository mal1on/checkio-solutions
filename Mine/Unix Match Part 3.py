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

    if '[]' in re_pattern:
        re_pattern = '\\[\\]'.join(re_pattern.split('[]'))
    elif '[^]' in re_pattern:
        re_pattern = '\\[\\!\\]'.join(re_pattern.split('[^]'))    

    return True if re.match(re_pattern, filename) else False


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")  