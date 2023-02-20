from operator import add, sub
from re import findall


def plusminus(op_list):
    result = []
    plus_minus = op_list[0] if op_list[0] in ['+', '-'] else None
    for op in op_list:
        if op in ['+', '-']:
            plusminus = op
        else:
            if plus_minus:
                result.append(plus_minus)
                plus_minus = None
            result.append(op)
    if op_list[-1] in ['+', '-']:
        result.append(op_list[-1])

    return result


def my_reduce(operators, numbers):
    ops = iter(operators)
    value = numbers[0]
    for ind, element in enumerate(numbers[1:]):
        op = next(ops)
        opss = [op] if op == '==' else findall('\\+=|-=|=|\\+|-', op)
        opss = plusminus(opss)
        prev_op = None
        for oop in opss:
            if oop == '+':
                function = add
            elif oop == '-':
                function = sub
            elif oop == '==':
                value = function(value, numbers[ind])
                if abs(value) > 99999:
                    return 'error'
                continue
            elif oop == '=':
                if prev_op:
                    value = function(value, numbers[ind])
                    if abs(value) > 99999:
                        return 'error'
                    continue
                elif len(opss) > 1:
                    def function(a, b): return a
                else:
                    def function(a, b): return b
            elif oop == '+=':
                function = add
                value = function(value, value)
                if value > 99999:
                    return 'error'
                prev_op = oop
                continue
            elif oop == '-=':
                function = sub
                value = function(value, value)
                if abs(value) > 99999:
                    return 'error'
                prev_op = oop
                continue
            else:
                def function(a, b): return b
            value = function(value, element)
            if value > 99999:
                return 'error'
            prev_op = oop
    return value


def calculator(log):

    log = log if log else '0'
    log = log if log and any(i.isdigit() for i in log) else '0'
    nums = [int(str(num)[:5]) for num in list(map(int, findall('\\d+', log)))]
    nums = [0] + nums if log[0] == '-' else nums
    ops = findall('\\D+', log)
    nums = nums if (ops and not any(ops[-1].startswith(i) for i in [
                    '==', '+=', '-='])) or all(e.isdigit() for e in log) == 1 else nums + [0]

    return str(nums[-1]) if log[-1].isdigit() else str(my_reduce(ops, nums))


print("Example:")
print(calculator("100000"))

# These "asserts" are used for self-checking
assert calculator("90000+10000=") == "error"
assert calculator("90000+10000-10000=") == "error"
assert calculator("90000+10000-10000") == "10000"
assert calculator("123456789") == "12345"
assert calculator("123456789+5=") == "12350"
assert calculator("5+123456789") == "12345"
assert calculator("50000+=") == "error"
assert calculator("3+=") == "6"
assert calculator("3+2==") == "7"
assert calculator("3+-2=") == "1"
assert calculator("-=-+3-++--+-2=-") == "1"
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
