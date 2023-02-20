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
            #print(value, oop, element, prev_op)
            if oop == '+':
                function = add
            elif oop == '-':
                function = sub
            elif oop == '==':
                value = function(value, numbers[ind])
                if abs(value) > 99999: return 'error'
                continue
            elif oop == '=':
                if prev_op:
                    value = function(value, numbers[ind])
                    if abs(value) > 99999: return 'error'
                    continue
                else:
                    def function(a, b): return a
            elif oop == '+=':
                function = add
                value = function(value, value)
                if value > 99999: return 'error'
                prev_op = oop
                continue
            elif oop == '-=':
                function = sub
                value = function(value, value)
                if abs(value) > 99999: return 'error'
                prev_op = oop
                continue
            else:
                def function(a, b): return b
            value = function(value, element)
            if value > 99999: return 'error'
            prev_op = oop
    return value


def calculator(log):

    log = log if log else '0'
    log = findall('-\\d+.*|\\d+.*',  log)[0]
    nums = [int(str(num)[:5]) for num in list(map(int, findall('\\d+', log)))]
    nums = [0] + nums if log[0] == '-' else nums
    ops = findall('\\D+', log)
    nums = nums if (ops and not any(ops[-1].startswith(i) for i in ['==', '+=', '-='])) or all(e.isdigit() for e in log) == 1 else nums + [0]

    return str(nums[-1]) if log[-1].isdigit() else str(my_reduce(ops, nums))


print(calculator("90000+10000=")) == "error"
print(calculator("90000+10000-10000=")) == "error"
print(calculator("90000+10000-10000")) == "10000"
print(calculator("123456789")) == "12345"
print(calculator("123456789+5=")) == "12350"
print(calculator("5+123456789")) == "12345"
print(calculator("50000+=")) == "error"
print(calculator("3+=")) == "6"
print(calculator("3+2==")) == "7"
print(calculator("3+-2=")) == "1"
print(calculator("-=-+3-++--+-2=-")) == "1"
print(calculator("000000")) == "0"
print(calculator("0000123")) == "123"
print(calculator("12")) == "12"
print(calculator("+12")) == "12"
print(calculator("")) == "0"
print(calculator("1+2")) == "2"
print(calculator("2+")) == "2"
print(calculator("1+2=")) == "3"
print(calculator("1+2-")) == "3"
print(calculator("1+2=2")) == "2"
print(calculator("=5=10=15")) == "15"
print(calculator('50000-====')) == 'error'
print(calculator('+-=12=')) == '12'
print(calculator('2+3=+7=')) == '12'
