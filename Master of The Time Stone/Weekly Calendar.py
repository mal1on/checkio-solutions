def weekly_calendar(year, month, day, firstweekday):

    return []



list(weekly_calendar(2020, 1, 1, 0)) == [30, 31, 1, 2, 3, 4, 5]
list(weekly_calendar(2020, 9, 20, 6)) == [20, 21, 22, 23, 24, 25, 26]
list(weekly_calendar(2020, 9, 30, 0)) == [28, 29, 30, 1, 2, 3, 4]
