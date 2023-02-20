def reveal_num(line):
    dot = True
    sign = ''
    result = ''
    for char in line:
        if char == '.' and dot:
            result += char
            dot = False
        elif char.isdigit():
            result += char
        elif char in ['-', '+'] and not result:
            sign = char

    return (float(sign + result) if '.' in result else int(sign + result)) \
        if result else None


print("Example:")
print(reveal_num("+A%+-1-0..."))

# These "asserts" are used for self-checking
assert reveal_num("F0(t}") == 0
assert reveal_num("Utc&g") == None
assert reveal_num("-aB%|_-+2ADS.12+3.ADS1.2") == 2.12312
assert reveal_num("-aB%|_+-2ADS.12+3.ADS1.2") == -2.12312
assert reveal_num("zV№1}3;o.vEf``C.WqTY0") == 13.0
assert reveal_num(
    "!3B'j=(}89JQ6aWvN*%5@uy.r)B<?pZ.!545ZD^KF9Sx@gqfa*") == 38965.5459

print("The mission is done! Click 'Check Solution' to earn rewards!")
