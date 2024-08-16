from itertools import zip_longest

def longest_prefix(arr: list[str]) -> str:

    prefix = ''

    for ch in map(list, map(set, zip_longest(*arr))):
        if len(ch) == 1:
            prefix += ch[0]
        else:
            break

    print(prefix)

longest_prefix(["flower", "flow", "flight"])
longest_prefix(["dog", "racecar", "car"])
longest_prefix(["apple", "application", "appetizer"])
longest_prefix(["a"])
