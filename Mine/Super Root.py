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


print(super_root(4)) == 2
print(super_root(27)) == 3
print(super_root(81)) == 3.504339593597054
print(super_root(2))
print(super_root(10000000000))
