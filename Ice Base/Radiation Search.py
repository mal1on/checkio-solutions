from itertools import groupby

def checkio(matrix):
    #replace this for solution

    counter = {1:0, 2:0, 3:0, 4:0, 5:0}

    for l in matrix:
        for key, group in groupby(l):
            counter[key] += len(list(group))
    print(counter)        



checkio([
    [1, 2, 3, 4, 5],
    [1, 1, 1, 2, 3],
    [1, 1, 1, 2, 2],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]]) == [14, 1]    