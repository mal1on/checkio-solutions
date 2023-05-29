from datetime import datetime
from typing import List, Optional, Union, Tuple
from itertools import groupby


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None,) -> int:

    for i, el in enumerate(els):
        if isinstance(el, datetime):
            els[i] = (el, 1)

    start_watching = start_watching or els[0][0]
    end_watching = end_watching or els[-1][0]
    bulbs = {k: [d[0] for d in list(g)] for k, g in groupby(
        sorted(els, key=lambda el: el[1]), key=lambda el: el[1])}

    for k in bulbs:
        bulbs[k] += [end_watching] if len(bulbs[k]) % 2 else []

    lighted = []

    for l in [list(zip(bulbs[k][0::2], bulbs[k][1::2])) for k in bulbs]:
        lighted += l

    lighted.sort(key=lambda t: t[0])

    light_ints = [lighted[0]]
    for on, off in lighted[1:]:
        if on <= light_ints[-1][1] <= off:
            light_ints[-1] = (light_ints[-1][0], off)
        else:
            light_ints.append((on, off))

    new_els = []

    for on, off in light_ints:
        if on < end_watching and off > start_watching:
            new_els.append((max(on, start_watching), min(off, end_watching)))

    return sum([(off - on).total_seconds() for on, off in new_els])


if __name__ == "__main__":
    print("Example:")

    print(
        sum_light(
            els=[
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 0),
            end_watching=datetime(2015, 1, 12, 10, 1, 0),
        )
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ]
        )
        == 60
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 11, 0, 0), 2),
                (datetime(2015, 1, 12, 11, 1, 0), 2),
            ]
        )
        == 70
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ]
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ]
        )
        == 40
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 0), 3),
                (datetime(2015, 1, 12, 10, 1, 20), 3),
            ]
        )
        == 60
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 50),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 50),
        )
        == 0
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 20), 2),
                (datetime(2015, 1, 12, 10, 1, 40), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 50
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 40
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 40
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 0
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 10
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 10
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            els=[
                (datetime(2015, 1, 11, 0, 0, 0), 3),
                datetime(2015, 1, 12, 0, 0, 0),
                (datetime(2015, 1, 13, 0, 0, 0), 3),
                (datetime(2015, 1, 13, 0, 0, 0), 2),
                datetime(2015, 1, 14, 0, 0, 0),
                (datetime(2015, 1, 15, 0, 0, 0), 2),
            ],
            start_watching=datetime(2015, 1, 10, 0, 0, 0),
            end_watching=datetime(2015, 1, 16, 0, 0, 0),
        )
        == 345600
    )

    print(
        "The forth mission in series is completed? Click 'Check' to earn cool rewards!"
    )
