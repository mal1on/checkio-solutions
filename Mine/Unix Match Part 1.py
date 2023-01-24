import re

def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    if pattern == '*' or filename == pattern:
        return True
    if pattern.startswith('*'):
        return filename[- (len(pattern) - 1):] == pattern[1:]
    if len(filename) == len(pattern) and '?' in pattern:
        parts = pattern.split('?')
        return all(part in filename for part in parts)

    return False    
            



print(unix_match("somefile.txt", "*")) == True
print(unix_match("other.exe", "*")) == True 
print(unix_match("my.exe", "*.txt")) == False
print(unix_match("log1.txt", "log?.txt")) == True  