import re

def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    return True



unix_match("somefile.txt", "*") == True
unix_match("other.exe", "*") == True 
unix_match("my.exe", "*.txt") == False
unix_match("log1.txt", "log?.txt") == True  