from math import pow

def super_root(number):

    sr = 1
    while True:
        sr += 0.5
        if sr ** sr > number:
            break

    sr -= 0.5        
    while True:
        print(sr, sr ** sr)
        if number - 0.001 < pow(sr, sr) < number + 0.001:
            return sr
        else:
            sr += 0.00001    

    
        




print(super_root(4)) == 2
print(super_root(27)) == 3
print(super_root(81)) == 3.504339593597054
 
