from operator import add, sub
from re import findall


def my_reduce(operators, numbers):
    nums = iter(numbers)
    ops = iter(operators)
    value = next(nums)
    for element in nums:
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

    log = log if log else '0'
    nums = list(map(int, findall('\\d+', log)))
    nums = nums if log[0].isdigit() else [0] + nums
    ops = findall('\\D', log)

    return str(nums[-1]) if log[-1].isdigit() else str(my_reduce(ops, nums))


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
