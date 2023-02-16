def fibo_poem(text: str) -> str:
    result = ''
    text = text.split()
    a, b = 0, 1
    while b < len(text):
        a, b = b, a + b
        result += (' '.join(text[:a]) + '\n')
        text = text[a:]

    if text:
        result += ' '.join(text) + ' _' * (b - len(text))

    return result.rstrip()


print("Example:")
print(fibo_poem("Zen of Python"))

# These "asserts" are used for self-checking
assert fibo_poem("") == ""
assert fibo_poem("Django framework") == "Django\nframework"
assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
assert (
    fibo_poem(
        "There are three kinds of lies: Lies, damned lies, and the benchmarks.")
    == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
