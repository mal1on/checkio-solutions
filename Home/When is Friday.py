from datetime import date


def friday(day):

    d = day.split('.')
    date_obj = date(int(d[2]), int(d[1]), int(d[0]))
    wday = date_obj.weekday()
    return 4 - wday if wday <= 4 else wday + 1


if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
