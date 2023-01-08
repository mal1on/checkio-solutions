from math import degrees, atan2
from typing import List, Tuple
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    def angle(a, b, c):

        ang = degrees(atan2(c[1] - b[1], c[0] - b[0]) -
                      atan2(a[1] - b[1], a[0] - b[0]))

        return ang + 360 if ang < 0 else ang

    angles_1 = set()
    angles_2 = set()

    a, b, c = coords_1
    angles_1.add(round(angle(a, b, c)))
    angles_1.add(round(angle(c, a, b)))
    angles_1.add(180 - sum(angles_1))

    a, b, c = coords_2
    angles_2.add(round(angle(a, b, c)))
    angles_2.add(round(angle(c, a, b)))
    angles_2.add(180 - sum(angles_2))

    return angles_1 == angles_2


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles(
        [(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [
                             (3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(
        3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [
                             (2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [
                             (3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(
        3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(
        3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
