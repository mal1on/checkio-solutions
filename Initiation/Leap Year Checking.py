def is_leap_year(year: int) -> bool:

    if year % 100 == 0 and year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 > 0:
        return True
    return False





print(is_leap_year(2000))
print(is_leap_year(1900))
print(is_leap_year(2004))
print(is_leap_year(2100))
