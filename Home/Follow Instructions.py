def follow(instructions: str):
    # your code here
    pos_a, pos_b = 0, 0
    for letter in instructions:
        if letter == 'f':
            pos_b += 1
        elif letter == 'b':
            pos_b -= 1
        elif letter == 'r':
            pos_a += 1
        elif letter == 'l':
            pos_a -= 1
    return pos_a, pos_b


print("Example:")
print(list(follow("fflff")))

assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
