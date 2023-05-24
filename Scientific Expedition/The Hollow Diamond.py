from string import ascii_lowercase as alphabet
from collections import deque


def hollow_diamond(side: int, length: int, cw: bool) -> str:

    letters = deque(alphabet[:length] + (4 * side - 4 - length) * '*')
    diamond = (side - 1) * ' ' + letters.popleft() + '\n'
    outer = list(range(side - 2, -1, -1)) + list(range(1, side - 1))
    inner = [1]
    for el in range(side - 2):
        inner.append(inner[-1] + 2)
    inner += inner[:-1][::-1]
    for i in range(len(outer)):
        if cw:
            diamond += outer[i] * ' ' + letters.pop() + \
                inner[i] * ' ' + letters.popleft() + '\n'
        else:
            diamond += outer[i] * ' ' + letters.popleft() + \
                inner[i] * ' ' + letters.pop() + '\n'
    diamond += (side - 1) * ' ' + letters.pop()

    return diamond


print("Example:")
print(hollow_diamond(3, 6, False))

# These "asserts" are used for self-checking
assert hollow_diamond(3, 8, True) == "  a\n h b\ng   c\n f d\n  e"
assert hollow_diamond(3, 6, False) == "  a\n b *\nc   *\n d f\n  e"
assert (
    hollow_diamond(
        4, 10, False) == "   a\n  b *\n c   *\nd     j\n e   i\n  f h\n   g"
)
assert (
    hollow_diamond(5, 16, True)
    == "    a\n   p b\n  o   c\n n     d\nm       e\n l     f\n  k   g\n   j h\n    i"
)
assert (
    hollow_diamond(5, 14, False)
    == "    a\n   b *\n  c   *\n d     n\ne       m\n f     l\n  g   k\n   h j\n    i"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
