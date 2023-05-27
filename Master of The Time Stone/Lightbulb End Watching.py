from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None,) -> int:
    """
    how long the light bulb has been turned on
    """

    new_els = []
    start_watching = els[0] if not start_watching else start_watching
    end_watching = els[-1] if not end_watching else end_watching
    if len(els) % 2:
        els.append(end_watching)
    for on, off in zip(els[0::2], els[1::2]):
        if on <= start_watching and off > start_watching:
            new_els.append((start_watching, off))
        elif on <= start_watching and off >= end_watching:
            new_els.append((start_watching, end_watching))
        elif end_watching > on > start_watching and off >= end_watching:
            new_els.append((on, end_watching))

    print(sum([(off - on).total_seconds() for on, off in new_els]))


sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
],
datetime(2015, 1, 12, 10, 10, 0),
datetime(2015, 1, 12, 11, 0, 10)) == 20

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
],
datetime(2015, 1, 12, 9, 9, 0),
datetime(2015, 1, 12, 10, 0, 0)) == 0

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
],
datetime(2015, 1, 12, 9, 0, 0),
datetime(2015, 1, 12, 10, 5, 0)) == 300
