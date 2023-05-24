def next_birthday(today, birthdates):

    return []




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
