import re

def unix_match(filename: str, pattern: str) -> bool:

    re_trans = str.maketrans({'.': '\\.', '*': '.+', '?': '.'})
    re_pattern = pattern.translate(re_trans)
    re_pattern = re_pattern.replace('[!', '[^').replace(
            '[.+', '[*').replace('[.', '[?')

    try:
        return bool(re.match(re_pattern, filename))
    except:
        return filename == pattern


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

