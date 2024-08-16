def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    # your code here
    return False



assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
