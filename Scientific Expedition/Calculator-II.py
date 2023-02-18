from operator import add, sub
from re import findall


def my_reduce(operators, numbers):
    nums = iter(numbers)
    ops = iter(operators)
    value = next(nums)
    for ind, element in enumerate(nums):
        op = next(ops)
        if op.endswith('+'):
            function = add
        elif op.endswith('-'):
            function = sub
        elif op == '=':
            function = lambda a, b: b
        elif op == '==':
            value = function(value, numbers[ind])
            continue
        elif op == '+=':
            value = add(value, numbers[ind])
            continue
        elif op == '-=':
            value = sub(value, numbers[ind])
            continue
        value = function(value, element)
    return value


def calculator(log):

    log = log if log else '0'
    nums = list(map(int, findall('\\d+', log)))
    nums = nums if log[0].isdigit() else [0] + nums
    ops = findall('\\D+', log)
    nums = nums if ops[-1] not in ['==', '+=', '-='] else nums + [0]

    print(str(nums[-1]) if log[-1].isdigit() else str(my_reduce(ops, nums)))


# calculator("000000") == "0"
# calculator("0000123") == "123"
# calculator("12") == "12"
# calculator("+12") == "12"
# calculator("") == "0"
# calculator("1+2") == "2"
# calculator("2+") == "2"
# calculator("1+2=") == "3"
# calculator("1+2-") == "3"
# calculator("1+2=2") == "2"
# calculator("=5=10=15") == "15"
# calculator('000005+003=') == '8'
# calculator('-5-10+15') == '15'

calculator("3+=") == "6"
calculator("3+2==") == "7"
calculator("3+-2=") == "1"
calculator("-=-+3-++--+-2=-") == "1"
