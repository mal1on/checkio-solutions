import math


def nearest_square(number):

    small = 0
    big = 0
    first = number
    second = number
    current = math.sqrt(number)

    while current != int(current):
        first += 1
        current = math.sqrt(first)
        big = int(current ** 2)

    current = math.sqrt(number)

    while current != int(current):
        second -= 1
        current = math.sqrt(second)
        small = int(current ** 2)

    if abs(number - big) > abs(number - small):
        result = small
    else:
        result = big

    return result


if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")
