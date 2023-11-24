from string import ascii_lowercase as low, ascii_uppercase as upp


def atbash(plaintext: str) -> str:

    result = ''

    for ch in plaintext:
        if ch in low:
            result += low[- low.index(ch) - 1]
        elif ch in upp:
            result += upp[- upp.index(ch) - 1]
        else:
            result += ch

    return result


if __name__ == "__main__":
    print("Example:\nplaintext: testing")
    print(atbash("testing"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert atbash("testing") == "gvhgrmt"
    assert atbash("attack at dawn") == "zggzxp zg wzdm"
    assert atbash("Hello, world!") == "Svool, dliow!"

    print("Coding complete? Click 'Check' to earn cool rewards!")
