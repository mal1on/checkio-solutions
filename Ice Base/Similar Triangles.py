from math import degrees, atan2
from typing import List, Tuple
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    def angle(a, b, c):

        ang = degrees(atan2(c[1] - b[1], c[0] - b[0]) - atan2(a[1] - b[1], a[0] - b[0]))

        return ang + 360 if ang < 0 else ang

    angles_1 = set()
    angles_2 = set()

    a, b, c = coords_1
    angles_1.add(angle(a, b, c))
    angles_1.add(angle(c, a, b))
    angles_1.add(180 - sum(angles_1))

    a, b, c = coords_2
    angles_2.add(angle(a, b, c))
    angles_2.add(angle(c, a, b))
    angles_2.add(180 - sum(angles_2))

    print(angles_1 == angles_2) 






similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True
