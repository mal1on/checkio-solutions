from datetime import timedelta, datetime as dt


def working_hours(date1, date2, start_time, end_time, holy):

    daily = dt.strptime(end_time, '%H:%M') - dt.strptime(start_time, '%H:%M')
    holy = len(holy)
    c_date = dt.strptime(date1, '%Y-%m-%d')

    while c_date <= dt.strptime(date2, '%Y-%m-%d'):
        if c_date.weekday() > 4:
            holy += 1
        c_date += timedelta(days=1)

    days = (dt.strptime(date2, '%Y-%m-%d') -
            dt.strptime(date1, '%Y-%m-%d')).days + 1 - holy

    return round(days * (daily.seconds / 3600), 2)


print("Example:")
print(working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", []))

# These "asserts" are used for self-checking
assert working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", []) == 8
assert working_hours("2023-03-01", "2023-03-02", "09:00", "17:00", []) == 16
assert working_hours("2023-03-01", "2023-03-03", "09:00",
                     "17:00", ["2023-03-01"]) == 16
assert (
    working_hours("2023-03-01", "2023-03-05", "08:45",
                  "17:10", ["2023-03-03"]) == 16.83
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
