def checkio(pattern, image):

    for v_ind in range(len(image) - len(pattern) + 1):
        print(v_ind)
        for h_ind in range(len(image[0]) - len(pattern[0]) + 1):
            print(image[v_ind][h_ind:h_ind + len(pattern[0])])





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