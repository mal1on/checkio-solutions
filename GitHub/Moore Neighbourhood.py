def count_neighbours(grid, row, col):
    
    count = 0

    s = row if row == 0 else row - 1

    for r in grid[s:row+2]:
        for i, e in enumerate(r):
            if e and (i == col or i == col - 1 or i == col +1):
                  count += 1
    print(count)                




# count_neighbours(((1, 0, 0, 1, 0),
#                   (0, 1, 0, 0, 0),
#                   (0, 0, 1, 0, 1),
#                   (1, 0, 0, 0, 0),
#                   (0, 0, 1, 0, 0),), 1, 2) == 3

count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0) == 1
