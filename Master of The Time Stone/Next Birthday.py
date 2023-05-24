from datetime import date


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
                next_bds[bd[0]] = ((next_bd - today).days,
                                   {bd[0]: next_bd.year - date(*bd[1]).year})
            except(ValueError):
                next_bd = date(today.year, bd[1][1] + 1, 1)
                next_bds[bd[0]] = ((next_bd - today).days,
                                   {bd[0]: next_bd.year - date(*bd[1]).year})
        else:
            try:
                next_bd = date(today.year + 1, bd[1][1], bd[1][2])
                next_bds[bd[0]] = ((next_bd - today).days,
                                   {bd[0]: next_bd.year - date(*bd[1]).year})
            except(ValueError):
                next_bd = date(today.year + 1, bd[1][1] + 1, 1)
                next_bds[bd[0]] = ((next_bd - today).days,
                                   {bd[0]: next_bd.year - date(*bd[1]).year})

    next = ([bd[1] for bd in next_bds.items() if bd[1][0] ==
             min(next_bds.items(), key=lambda t: t[1][0])[1][0]])

    return next[0] if len(next) == 1 else (next[0][0], {**next[0][1], **next[1][1]})


if __name__ == '__main__':
    FAMILY = {
        'Brian': (1967, 5, 31),
        'Léna': (1970, 10, 3),
        'Philippe': (1991, 6, 15),
        'Yasmine': (1996, 2, 29),
        'Emma': (2000, 12, 25),
    }

    TESTS = [
        ((2020, 9, 8), (25, {'Léna': 50})),
        ((2021, 10, 4), (82, {'Emma': 21})),
        ((2022, 3, 1), (0, {'Yasmine': 26})),
    ]

    for nb, (day, answer) in enumerate(TESTS, 1):
        user_result = tuple(next_birthday(day, FAMILY.copy()))
        if user_result != answer:
            print(f'You failed the test #{nb}.')
            print(f'Your result: {user_result}')
            print(f'Right result: {answer}')
            break
    else:
        print('Well done! Click on "Check" for real tests.')
