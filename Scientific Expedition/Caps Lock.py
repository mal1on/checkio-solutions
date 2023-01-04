def caps_lock(text: str) -> str:
    # your code here
    switch = False
    result = ''
    for char in text:
        if char != 'a':
            if not switch:
                result += char
            if switch:
                result += char.upper()
        else:
            if not switch:
                switch = True
                continue
            if switch:
                switch = False
    return result


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock(
        "Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock(
        "Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
