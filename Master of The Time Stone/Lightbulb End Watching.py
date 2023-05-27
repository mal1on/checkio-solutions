from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
    how long the light bulb has been turned on
    """

    new_els = []
    start_watching = els[0] if not start_watching else start_watching
    for on, off in zip(els[0::2], els[1::2]):
        if on <= start_watching and off > start_watching:
            new_els.append([start_watching, off])
        elif on > start_watching:
            new_els.append((on, off))

    print(sum([(off - on).total_seconds() for on, off in new_els]))


sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
],
datetime(2015, 1, 12, 10, 10, 0),
datetime(2015, 1, 12, 11, 0, 10)) == 20

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
# ],
# datetime(2015, 1, 12, 9, 9, 0),
# datetime(2015, 1, 12, 10, 0, 0)) == 0

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
#     datetime(2015, 1, 12, 11, 10, 10),
# ],
# datetime(2015, 1, 12, 9, 0, 0),
# datetime(2015, 1, 12, 10, 5, 0)) == 300
