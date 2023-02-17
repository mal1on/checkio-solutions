def calculator(log):
    ops, nums = [], []
    op, num, screen = None, '', 0
    log = log if log else '0'
    for ch in log:
        if ch.isnumeric():
            num += ch
            if op:
                ops.append(op)
                op = None
        else:
            op = ch
            if num:
                nums.append(num.lstrip('0'))
            num = ''
    if num:
        nums.append(num.lstrip('0'))
    if op:
        ops.append(op)

    nums = nums if any(nums) else ['0']

    if log[0].isnumeric():
        ops = ['+'] + ops
    couples = zip(ops, nums)
    for couple in couples:
        if couple[0] == '=':
            continue
        screen += eval(''.join(couple))

    return nums[-1] if log[-1].isnumeric() else str(screen)


print("Example:")
print(calculator("1+2"))

# These "asserts" are used for self-checking
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"
assert calculator("") == "0"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2-") == "3"
assert calculator("1+2=2") == "2"
assert calculator("=5=10=15") == "15"

print("The mission is done! Click 'Check Solution' to earn rewards!")
