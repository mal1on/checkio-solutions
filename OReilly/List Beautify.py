def list_beautify(data):
    temps = []
    for l in zip(*data):
        mlen = len(max(map(str, l), key=len))
        temp = []
        for i in l:
            temp.append((mlen - len(str(i))) * ' ' + str(i))
        temps.append(temp)
    blists = []
    for blist in zip(*temps):
        blists.append('[' + ', '.join(blist) + ']')
    return '[' + ',\n '.join(blists) + ']'


print("Example:")
print(list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]))

# These "asserts" are used for self-checking
assert (
    list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]])
    == "[[ 1,   2,   10,  150],\n [10,   2, 1000,    2],\n [ 1, 120,    1, 1000]]"
)
assert list_beautify([[1, 10, 100, -1000]]) == "[[1, 10, 100, -1000]]"
assert (
    list_beautify([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1]]"
)
assert (
    list_beautify([[1, 1, -1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, -1, 1, 1],\n [1, 1,  1, 1, 1],\n [1, 1,  1, 1, 1]]"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
