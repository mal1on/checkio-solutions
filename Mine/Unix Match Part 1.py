import re

re_dict = {'*': '.*', '?': '.'}
re_special = {'.': '\\.'}

def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    re_pattern = ''
    for char in pattern:
        if char in re_dict.keys():
            re_pattern += re_dict[char]
        elif char in re_special.keys():
            re_pattern += re_special[char]
        else:
            re_pattern += char        

    return True if re.match(re_pattern, filename) else False            
            



print(unix_match("somefile.txt", "*")) == True
print(unix_match("other.exe", "*")) == True 
print(unix_match("my.exe", "*.txt")) == False
print(unix_match("log1.txt", "log?.txt")) == True
print(unix_match('log12.txt', '**')) == True
print(unix_match('l.txt', '???*')) == True  