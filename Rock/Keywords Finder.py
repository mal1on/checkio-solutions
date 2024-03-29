import re


def checkio(text: str, words: str) -> str:

    found = []
    check = []

    for keyword in words.lower().split():
        matches = re.finditer(re.escape(keyword), text.lower())
        for match in matches:
            found.append(match.span())

    found.sort()

    for ind, find in enumerate(found):
        f_s, f_e = find
        for other in found[ind + 1:]:
            o_s, o_e = other
            if f_s <= o_s < f_e and o_e > f_e:
                f_e = o_e
                found.remove(other)
            elif o_s >= f_s and o_e <= f_e:
                found.remove(other)
        check.append((f_s, f_e))

    check = [(0, len(text) + 1)] if len(set(text)) == 1 else check

    mult = 0
    for s, e in check:
        s += mult * 13
        e += mult * 13
        text = text[:s] + '<span>' + text[s:e] + '</span>' + text[e:]
        mult += 1
    return text


print("Example:")
print(checkio("This is only a text example for task example.", "example"))

assert (
    checkio("This is only a text example for task example.", "example")
    == "This is only a text <span>example</span> for task <span>example</span>."
)
assert (
    checkio("Python is a widely used high-level programming language.", "pyThoN")
    == "<span>Python</span> is a widely used high-level programming language."
)
assert (
    checkio("It is experiment for control groups with similar distributions.", "is im")
    == "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."
)
assert (
    checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE")
    == "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."
)
assert checkio("Did you find anything?",
               "word space tree") == "Did you find anything?"
assert (
    checkio("Hello World! Or LOL", "hell world or lo")
    == "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"
)

print("The mission is done! Click 'Check' to earn cool rewards!")
