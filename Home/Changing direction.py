def changing_direction(elements: list[int]) -> int:
    # your code here

    direction = []
    for f, s in zip(elements, elements[1:]):
        if s > f and (not direction or direction[-1] == 'desc'):
            direction.append('asc')
        elif s < f and (not direction or direction[-1] == 'asc'):
            direction.append('desc')

    return len(direction) - 1 if len(elements) > 1 else 0


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
