from datetime import date, timedelta as td


def weekly_calendar(year, month, day, firstweekday):

    current = date(year, month, day)
    week = []
    fwd = (current - td(current.weekday() - firstweekday))
    for d in range(7):
        week.append((fwd + td(d)).day)
    print(week)
    return week



list(weekly_calendar(2020, 1, 1, 0)) == [30, 31, 1, 2, 3, 4, 5]
list(weekly_calendar(2020, 9, 20, 6)) == [20, 21, 22, 23, 24, 25, 26]
list(weekly_calendar(2020, 9, 30, 0)) == [28, 29, 30, 1, 2, 3, 4]
list(weekly_calendar(2020, 2, 29, 2)) == [26, 27, 28, 29, 1, 2, 3]
