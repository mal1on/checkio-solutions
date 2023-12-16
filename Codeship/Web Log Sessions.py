import re
from datetime import datetime
from operator import itemgetter

def checkio(log_text):

    lines = log_text.splitlines()
    session, sessions, session_data, result = [], [], [], []
    session_time = 1
    pattern = '(https?://)(\w+\.)?(\w+\.\w+)'

    while lines:
        session.append(lines.pop(0))
        t, u, a = session[0].lower().split(';;')
        t = datetime.strptime(t, '%Y-%m-%d-%H-%M-%S')
        d = re.search(pattern, a).group(3)
        session_data.append(u)
        session_data.append(d)
        for line in lines:
            t_l, u_l, a_l = line.lower().split(';;')
            t_l = datetime.strptime(t_l, '%Y-%m-%d-%H-%M-%S')
            d_l = re.search(pattern, a_l).group(3)
            if (t_l - t).total_seconds() <= 1800 and u_l == u and d == d_l:
                session.append(line)
                session_time += int((t_l - t).total_seconds())
                t = t_l
        session_data.append(session_time)
        session_data.append(len(session))
        result.append(session_data)
        sessions.append(session)
        lines = [l for l in lines if l not in session]
        session, session_data = [], []
        session_time = 1

    result = sorted(result, key=itemgetter(0, 1, 2))
    result = '\n'.join([';;'.join(list(map(str, l))) for l in result])
    print(result)


checkio("""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
