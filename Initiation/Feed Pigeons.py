def checkio(food: int) -> int:
    # your code here
    new = 1
    pigeons = 1
    fed = 0

    while food >= pigeons:

        food -= pigeons
        fed = pigeons
        new += 1
        pigeons += new

    return max(food, fed)


print("Example:")
print(checkio(5))

assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6

print("The mission is done! Click 'Check Solution' to earn rewards!")
