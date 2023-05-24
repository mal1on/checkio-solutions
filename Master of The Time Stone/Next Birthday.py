from datetime import date
from calendar import isleap


def next_birthday(today, birthdates):

    today = date(*today)
    next_bds = {}

    for bd in birthdates.items():
        try:
            temp_date = date(today.year, bd[1][1], bd[1][2])
        except(ValueError):
            temp_date = date(today.year, bd[1][1] + 1, 1)
        if today <= temp_date:
            try:
                next_bd = date(today.year, bd[1][1], bd[1][2])
                next_bds[bd[0]] = ((next_bd - today).days, {bd[0]:next_bd.year - date(*bd[1]).year})
            except(ValueError):
                next_bd = date(today.year, bd[1][1] +1, 1)
                next_bds[bd[0]] = ((next_bd - today).days, {bd[0]:next_bd.year - date(*bd[1]).year})
        else:
            try:
                next_bd = date(today.year + 1, bd[1][1], bd[1][2])
                next_bds[bd[0]] = ((next_bd - today).days, {bd[0]:next_bd.year - date(*bd[1]).year})
            except(ValueError):
                next_bd = date(today.year + 1, bd[1][1] + 1, 1)
                next_bds[bd[0]] = ((next_bd - today).days, {bd[0]:next_bd.year - date(*bd[1]).year})

    print(min(next_bds.items(), key=lambda t: t[1][0])[1])




birthdates = {
    'Brian': (1967, 5, 31),
    'Léna': (1970, 10, 3),
    'Philippe': (1991, 6, 15),
    'Yasmine': (1996, 2, 29),
    'Emma': (2000, 12, 25),
}
next_birthday((2020, 9, 8), birthdates) == (25, {'Léna': 50})
next_birthday((2021, 10, 4), birthdates) == (82, {'Emma': 21})
next_birthday((2022, 3, 1), birthdates) == (0, {'Yasmine': 26})
