from calendar import monthcalendar


def most_frequent_days(a):

    first_week = monthcalendar(a, 1)[0]
    last_week = monthcalendar(a, 12)[-1]
    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    first_week = list(zip(first_week, weekdays))
    last_week = list(zip(last_week, weekdays))

    pool = list(filter(lambda day: day[0] != 0, first_week + last_week))
    pool_dict = {}

    for day in weekdays:
        pool_dict[day] = 0

    for day in weekdays:
        for item in pool:
            if item[1] == day:
                pool_dict[day] += 1

    most_frequent = max(pool_dict.values())

    return [day[0] for day in pool_dict.items() if day[1] == most_frequent]


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
