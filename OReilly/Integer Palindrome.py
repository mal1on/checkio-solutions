def int_palindrome(number: int, B: int) -> bool:
    # your code here

    result = ''
    while number:
        q, r = divmod(number, B)
        result += str(r)
        number = q
    if B in (16, 100):
        mid = len(result) // 2 if len(result) > 1 else 1
        return result[:mid] == result[-mid:]
    else:
        return result == result[::-1]


print("Example:")
print(int_palindrome(455, 2))

# These "asserts" are used for self-checking
assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
