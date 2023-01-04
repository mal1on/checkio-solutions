def is_acceptable_password(password: str) -> bool:

    cond_1 = len(password) > 6
    cond_2 = any(item.isdigit() for item in password)
    cond_3 = not all(item.isdigit() for item in password)

    return cond_1 and cond_2 and cond_3


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
