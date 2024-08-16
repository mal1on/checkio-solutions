from itertools import zip_longest

def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:

    print(len([x for x in map(set, zip_longest(str1, str2)) if len(x) > 1]) <= threshold)


fuzzy_string_match("apple", "appel", 2)
fuzzy_string_match("apple", "bpple", 1)
fuzzy_string_match("apple", "bpple", 0)
fuzzy_string_match("apple", "apples", 1)
