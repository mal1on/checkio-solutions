def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    return True


print(unix_match("log1.txt", "log[1234567890].txt")) == True
print(unix_match("log1.txt", "log[!1].txt")) == False
