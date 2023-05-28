from datetime import datetime
from typing import List, Optional, Union, Tuple
from itertools import groupby


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None,) -> int:

    for i, el in enumerate(els):
        if isinstance(el, datetime):
            els[i] = (el, 1)

    start_watching = els[0][0] if not start_watching else start_watching
    end_watching = els[-1][0] if not end_watching else end_watching
    els += [end_watching] if len(els) % 2 else []

    bulbs = {k: [d[0] for d in list(g)] for k, g in groupby(
        sorted(els, key=lambda el: el[1]), key=lambda el: el[1])}

    lighted = []

    for l in [list(zip(bulbs[k][0::2], bulbs[k][1::2])) for k in bulbs]:
        lighted += l

    lighted.sort(key=lambda t: t[0])
    light_ints = [lighted[0]]
    for on, off in lighted[1:]:
        if on <= light_ints[-1][1] < off:
            light_ints[-1] = (light_ints[-1][0], off)
        else:
            light_ints.append((on, off))

    new_els = []

    for on, off in light_ints:
        if end_watching > on and start_watching < off:
            new_els.append((max(on, start_watching), min(off, end_watching)))

    print(sum([(off - on).total_seconds() for on, off in new_els]))


sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    (datetime(2015, 1, 12, 10, 0, 0), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
]) == 60


sum_light([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 3),
    (datetime(2015, 1, 12, 10, 1, 20), 3),
]) == 60

sum_light([
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
], datetime(2015, 1, 12, 10, 0, 30)) == 20

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    (datetime(2015, 1, 12, 10, 0, 0), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40
