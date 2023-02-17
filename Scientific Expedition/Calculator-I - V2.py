from operator import add, sub


def my_reduce(operators, numbers):
    it = iter(numbers)
    ops = iter(operators)
    value = next(it)
    for element in it:
        op = next(ops)
        match op:
            case '+':
                function = add
            case '-':
                function = sub
            case '=':
                def function(a, b): return b
        value = function(value, element)
    return value


def calculator(log):
    ops, nums = [], []
    op, num = None, ''
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
    nums = list(map(int, nums))

    if not log[0].isnumeric():
        nums = [0] + nums

    return str(nums[-1]) if log[-1].isnumeric() else str(my_reduce(ops, nums))


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
