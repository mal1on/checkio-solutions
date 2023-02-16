def fibo_poem(text: str) -> str:
    result = ''
    text = text.split()
    a, b = 0, 1
    while a < len(text):
        a, b = b, a + b
        result += (''.join(text[:a]) + '\n')
        text = text[a:]

    if text:
        text += '_' * (b - len(text))
        result += (''.join(text) + '\n')

    print(result.rstrip())


fibo_poem("") == ""
fibo_poem("Django framework") == "Django\nframework"
fibo_poem("Zen of Python") == "Zen\nof\nPython _"
fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.") == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
