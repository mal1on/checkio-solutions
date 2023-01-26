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

    print(True if re.match(re_pattern, filename) else False)


unix_match('somefile.txt', '*') == True
unix_match('other.exe', '*') == True
unix_match('my.exe', '*.txt') == False
unix_match('log1.txt', 'log?.txt') == True
unix_match('log1.txt', 'log[1234567890].txt') == True
unix_match('log12.txt', 'log?.txt') == False
unix_match('log12.txt', 'log??.txt') == True  