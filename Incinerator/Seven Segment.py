ss_dict = {'1' : {'b', 'c'},
            '2' : {'a', 'b', 'g', 'e', 'd'},
            '3' : {'a', 'b', 'g', 'c', 'd'},
            '4' : {'f', 'g', 'b', 'c'},
            '5' : {'a', 'f', 'g', 'c', 'd'},
            '6' : {'a', 'f', 'f', 'e', 'c', 'd'},
            '7' : {'a', 'b', 'c'},
            '8' : {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            '9' : {'a', 'b', 'c', 'd', 'f', 'g'},
            '0' : {'a', 'b', 'c', 'd', 'e', 'f'}}

def seven_segment(lit_seg, broken_seg):

    first = second = set()
    
    for char in lit_seg:
        if char.isupper():
            first.add(char)
        else:
            second.add(char)

    print(first, second)            
    


seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2
