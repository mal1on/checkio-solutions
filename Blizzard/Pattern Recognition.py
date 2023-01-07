def checkio(pattern, image):

    for v_ind in range(len(image) - len(pattern) + 1):
        for h_ind in range(len(image[0]) - len(pattern[0]) + 1):
            check = True
            if image[v_ind][h_ind:h_ind + len(pattern[0])] != pattern[0]:
                check = False    
            #print('v_ind:', v_ind, image[v_ind][h_ind:h_ind + len(pattern[0])], 'check:', check)    
            for vert in range(1, len(pattern)):
                #if check == True:
                    #print(image[v_ind + vert][h_ind:h_ind + len(pattern[0])])
                if image[v_ind + vert][h_ind:h_ind + len(pattern[0])] != pattern[vert]:
                    check = False                                
            if check:
                for c_ind in range(len(pattern[0])):
                    if image[v_ind][h_ind + c_ind] == 0:
                        image[v_ind][h_ind + c_ind] = 2
                    else:
                        image[v_ind][h_ind + c_ind] = 3
                    for vert in range(1, len(pattern)):    
                        if image[v_ind + vert][h_ind + c_ind] == 0:
                            image[v_ind + vert][h_ind + c_ind] = 2
                        else:
                            image[v_ind + vert][h_ind + c_ind] = 3    
    print(image)                                         


checkio([[1,0,0],[0,1,0],[0,0,1]],[[1,0,0,0,1,0,1,0,1],[0,1,0,0,0,1,0,1,0],[0,0,1,0,0,0,1,0,1],[1,0,0,1,0,0,0,1,0],[0,0,0,0,1,0,0,0,1],[0,1,0,0,0,1,0,0,0],[0,1,0,0,0,0,1,0,1]])


checkio([[1, 0], [1, 1]],
        [[0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                               [0, 3, 3, 0, 0],
                               [3, 2, 1, 3, 2],
                               [3, 3, 0, 3, 3],
                               [0, 1, 1, 0, 0]]


checkio([[1, 1], [1, 1]],
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]) == [[3, 3, 1],
                         [3, 3, 1],
                         [1, 1, 1]]


checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]                                                           