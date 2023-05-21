from datetime import date, timedelta


def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    weekends = 0
    while from_date <= to_date:
        if from_date.isoweekday() in [6, 7]:
            weekends += 1
        from_date += timedelta(1)
    print(weekends)








checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8
checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2
