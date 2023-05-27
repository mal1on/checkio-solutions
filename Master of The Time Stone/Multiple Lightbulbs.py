from datetime import datetime
from typing import List, Optional, Union, Tuple


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None,) -> int:

    new_els = []
    start_watching = els[0] if not start_watching else start_watching
    end_watching = els[-1] if not end_watching else end_watching
    if len(els) % 2:
        els.append(end_watching)
    for on, off in zip(els[0::2], els[1::2]):
        if end_watching > on and start_watching < off:
            new_els.append((max(on, start_watching), min(off, end_watching)))

    print(sum([(off - on).total_seconds() for on, off in new_els]))


sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    (datetime(2015, 1, 12, 10, 0, 0), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
]) == 60

# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 3),
#     (datetime(2015, 1, 12, 10, 1, 20), 3),
# ]) == 60

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], datetime(2015, 1, 12, 10, 0, 30)) == 20

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
#     (datetime(2015, 1, 12, 10, 0, 0), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40
