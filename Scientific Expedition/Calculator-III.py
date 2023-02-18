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
        elif op == '==':
            value = function(value, numbers[ind])
            continue
        elif op == '+=':
            value = add(value, value)
            if value > 99999: return 'error'
            continue
        elif op == '-=':
            value = sub(value, value)
            continue
        else:
            def function(a, b): return b
        value = function(value, element)
        if value > 99999: return 'error'
    return value


def calculator(log):

    log = log if log else '0'
    nums = [int(str(num)[:5]) for num in list(map(int, findall('\\d+', log)))]
    nums = nums if log[0].isdigit() else [0] + nums
    ops = findall('\\D+', log)
    nums = nums if (ops and ops[-1] not in ['==',
                                            '+=', '-=']) or all(e.isdigit() for e in log) == 1 else nums + [0]

    return str(nums[-1]) if log[-1].isdigit() else str(my_reduce(ops, nums))


# calculator("90000+10000=") == "error"
# calculator("90000+10000-10000=") == "error"
# calculator("90000+10000-10000") == "10000"
# calculator("123456789") == "12345"
# calculator("123456789+5=") == "12350"
# calculator("5+123456789") == "12345"
# calculator("50000+=") == "error"
# calculator("3+=") == "6"
# calculator("3+2==") == "7"
# calculator("3+-2=") == "1"
# calculator("-=-+3-++--+-2=-") == "1"
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

calculator('50000-====') == 'error'
