def super_root(number):

    sr = 1
    while True:
        sr += 0.1
        if sr ** sr == number:
            return sr 
        elif sr ** sr > number:
            break        

    sr -= 0.1
    print(number, sr)        
    while True:
        if number - 0.001 < sr ** sr < number + 0.001:
            return sr
        else:
            sr += 0.00001    

    
        




print(super_root(4)) == 2
print(super_root(27)) == 3
print(super_root(81)) == 3.504339593597054
print(super_root(2))
print(super_root(10000000000))
