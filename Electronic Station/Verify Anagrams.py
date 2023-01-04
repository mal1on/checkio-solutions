def verify_anagrams(a, b):

    a = a.replace(' ', '').lower()
    b = b.replace(' ', '').lower()
    result = True if len(a) == len(b) else False

    for ch in a:
        if a.count(ch) != b.count(ch):
            result = False
            break

    return result


if __name__ == '__main__':
    print("Example:")
    print(verify_anagrams('Programming', 'Gram Ring Mop'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
