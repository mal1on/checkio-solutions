from itertools import product

ss_dict = {'1' : {'b', 'c'},
            '2' : {'a', 'b', 'g', 'e', 'd'},
            '3' : {'a', 'b', 'g', 'c', 'd'},
            '4' : {'f', 'g', 'b', 'c'},
            '5' : {'a', 'f', 'g', 'c', 'd'},
            '6' : {'a', 'f', 'g', 'e', 'c', 'd'},
            '7' : {'a', 'b', 'c'},
            '8' : {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            '9' : {'a', 'b', 'c', 'd', 'f', 'g'},
            '0' : {'a', 'b', 'c', 'd', 'e', 'f'}}

def seven_segment(lit_seg, broken_seg):

    first = {char.lower() for char in lit_seg if char.isupper()}
    second = {char for char in lit_seg if char.islower()}
    print(first, second)
    broken_u = {char.lower() for char in broken_seg if char.isupper()}
    broken_l = {char for char in broken_seg if char.islower()}
    first_w_broken = first.copy()
    second_w_broken = second.copy()
    first_w_broken.update(broken_u)
    second_w_broken.update(broken_l)
    first_dig = [] 
    second_dig = [] 

    for k, i in ss_dict.items():
        if i.issubset(first_w_broken) and first.issubset(i):
            first_dig.append(k)
        if i.issubset(second_w_broken) and second.issubset(i):
            second_dig.append(k)

    print(len(first_dig) * len(second_dig))     




seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2
seven_segment({'B', 'C', 'a', 'c', 'd', 'f', 'g'}, {'A', 'D', 'G', 'e'}) == 6
seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}) == 4
seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6 
seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20
