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

    print(result)



atbash('testing') == 'gvhgrmt'
atbash('Hello, world!') == 'Svool, dliow!'
