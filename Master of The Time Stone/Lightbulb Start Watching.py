from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
    how long the light bulb has been turned on
    """

    new_els = []
    for on, off in zip(els[0::2], els[1::2]):
        if (on <= start_watching and off > start_watching):
            new_els.append([start_watching, off])
        elif on > start_watching:
            new_els.append(on, off)

    print(sum([(off - on).total_seconds() for on, off in new_els]))





sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
datetime(2015, 1, 12, 10, 0, 5)) == 5

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
], datetime(2015, 1, 12, 10, 0, 0)) == 10

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
], datetime(2015, 1, 12, 11, 0, 0)) == 610
