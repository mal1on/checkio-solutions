from datetime import date, timedelta as td


def weekly_calendar(year, month, day, firstweekday):

    current = date(year, month, day)
    week = []
    if current.weekday() >= firstweekday:
        fwd = (current - td(current.weekday() - firstweekday))
    else:
        fwd = (current - td(7 - firstweekday + current.weekday()))
    for d in range(7):
        week.append((fwd + td(d)).day)

    return week


if __name__ == '__main__':
    print("Example:")
    print(list(weekly_calendar(2020, 1, 1, 0)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(weekly_calendar(2020, 1, 1, 0)) == [
        30, 31, 1, 2, 3, 4, 5], "01/01/2020 Monday"
    assert list(weekly_calendar(2020, 9, 20, 6)) == [
        20, 21, 22, 23, 24, 25, 26], "09/20/2020 Sunday"
    assert list(weekly_calendar(2020, 9, 30, 0)) == [
        28, 29, 30, 1, 2, 3, 4], "09/30/2020 Monday"
    assert list(weekly_calendar(2020, 2, 29, 2)) == [
        26, 27, 28, 29, 1, 2, 3], "02/29/2020 Wednesday"
    print("Coding complete? Click 'Check' to earn cool rewards!")
