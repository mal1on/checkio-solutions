import re

re_dict = {'.': '\\.', '*': '.+', '?': '.', '[!': '[^'}

def unix_match(filename: str, pattern: str) -> bool:

    re_pattern = pattern
    for key in re_dict:
        re_pattern = re_pattern.replace(key, re_dict[key]).replace('[.+', '[*').replace('[.', '[?')

    try:
        return bool(re.match(re_pattern, filename))
    except:
        return filename == pattern          

    


# unix_match('somefile.txt', '*') == True
# unix_match('other.exe', '*') == True
# unix_match('my.exe', '*.txt') == False
# unix_match('log1.txt', 'log?.txt') == True
# unix_match('log1.txt', 'log[1234567890].txt') == True
# unix_match('log12.txt', 'log?.txt') == False
# unix_match('log12.txt', 'log??.txt') == True
# print(unix_match("name.txt","name[]txt")) == False
# print(unix_match("1name.txt","[!1234567890]*")) == False
# print(unix_match("[!]check.txt","[!]check.txt")) == True
print(unix_match("[?*]","[[][?][*][]]")) == True