from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    # replace this for solution
    h, m = map(int, time.split(':'))
    if h < 6 or (h >= 18 and m > 0):
        return "I don't see the sun!"
    return round((h - 6) * 15 + m * 0.25, 2)


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")
