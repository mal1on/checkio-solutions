import re
from datetime import datetime
from operator import itemgetter


def checkio(log_text):

    lines = log_text.splitlines()
    session, result, session_time = [], [], 1
    pattern = '(https?://)(\w+\.)?(\w+\.\w+)'

    while lines:
        session.append(lines.pop(0))
        t, u, a = session[0].lower().split(';;')
        t = datetime.strptime(t, '%Y-%m-%d-%H-%M-%S')
        d = re.search(pattern, a).group(3)
        for line in lines:
            t_l, u_l, a_l = line.lower().split(';;')
            t_l = datetime.strptime(t_l, '%Y-%m-%d-%H-%M-%S')
            d_l = re.search(pattern, a_l).group(3)
            if (t_l - t).total_seconds() <= 1800 and u_l == u and d == d_l:
                session.append(line)
                session_time += int((t_l - t).total_seconds())
                t = t_l
        result.append([u, d, session_time, len(session)])
        lines = [l for l in lines if l not in session]
        session, session_time = [], 1

    result = sorted(result, key=itemgetter(0, 1, 2))

    return '\n'.join([';;'.join(list(map(str, l))) for l in result])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(
        """2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
        ==
        """name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"
