import datetime


def birthday_party(birthday: datetime.date) -> datetime.date:

    if birthday.isoweekday() in [6, 7]:
        return birthday
    return birthday + datetime.timedelta(6 - birthday.isoweekday())


print('Example:')
print(birthday_party(datetime.date(2022, 1, 5)))

assert birthday_party(datetime.date(2022, 1, 5)) == datetime.date(2022, 1, 8)
assert birthday_party(datetime.date(2022, 2, 21)) == datetime.date(2022, 2, 26)
assert birthday_party(datetime.date(2022, 3, 26)) == datetime.date(2022, 3, 26)
assert birthday_party(datetime.date(2022, 4, 17)) == datetime.date(2022, 4, 17)
assert birthday_party(datetime.date(2022, 3, 30)) == datetime.date(2022, 4, 2)

print("The first mission is done! Click 'Check' to earn cool rewards!")
