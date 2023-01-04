def longest_palindromic(a):
    # your code here
    substrings = [a[x:x + y]
                  for y in range(1, 1 + len(a)) for x in range(1 + len(a) - y)]
    palyndromic = list(filter(lambda substring: substring ==
                              substring[::-1], substrings))
    return max(palyndromic, key=len)


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
