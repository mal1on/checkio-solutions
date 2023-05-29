from datetime import datetime as dt


def time_converter(time: str) -> str:

    return dt.strptime(time, '%H:%M').strftime('%I:%M %p').replace('PM', 'p.m.').replace('AM', 'a.m.').lstrip('0')


print("Example:")
print(time_converter("12:30"))

assert time_converter("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."

print("The mission is done! Click 'Check Solution' to earn rewards!")
