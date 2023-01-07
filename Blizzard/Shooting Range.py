def shot(wall1, wall2, shot_point, later_point):

    points = 0

    w1x, w1y = wall1
    w2x, w2y = wall2
    sx, sy = shot_point
    lx, ly = later_point

    m = (w1y - w2y) / (w1x - w2x)
    b = (w1x * w2y - w2x * w1y) / (w1x - w2x)

    x = 3

    y = m * x + b

    print(y)



shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100
   