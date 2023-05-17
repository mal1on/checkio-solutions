from collections import deque


def diffs(num1, num2):

    return sum([1 for ind, dig in enumerate(str(num1)) if str(num2)[ind] != dig])


def min_diffs(num1, elements):

    count = [(el, diffs(el, num1)) for el in elements]
    return min(count, key=lambda a: a[1])[0]


def checkio(numbers):

    chain = deque([numbers[-1]])
    elements = {number:[n for n in numbers[:-1] if diffs(number, n) == 1] for number in numbers}

    while chain[0] != numbers[0]:
        for number in numbers:
            if number == chain[0]:
                close_nums = [num for num in elements[number] if num not in chain]
                count = [(el, diffs(el, numbers[0])) for el in close_nums]
                chain.appendleft(min(count, key=lambda a: a[1])[0])
    print(list(chain))








checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999]
checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777]
checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654]  # or [456, 656, 654]
