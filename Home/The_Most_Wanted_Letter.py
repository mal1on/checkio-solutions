from string import ascii_lowercase

def checkio(text: str) -> str:

    wanted = []
    most = 0
    text = text.lower()

    for char in text:

        if char in ascii_lowercase:

            if most < text.count(char):

                most = text.count(char)

    for char in text:

        if char in ascii_lowercase:

            if most == text.count(char):

                wanted.append(char)

    return min(wanted, key=ord)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
