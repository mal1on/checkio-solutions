def calc(sr, step, number):

    while True:
        sr += step
        if number - 0.001 < sr ** sr < number + 0.001:
            return sr
        elif sr ** sr > number:
            sr -= step
            return sr


def super_root(number):

    sr, step = 1, 0.1

    while True:
        res = calc(sr, step, number)
        if number - 0.001 < res ** res < number + 0.001:
            return res
        else:
            sr = res
            step /= 10


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
