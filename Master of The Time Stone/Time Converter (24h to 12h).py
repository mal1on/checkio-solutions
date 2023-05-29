from datetime import datetime as dt

def time_converter(time: str) -> str:
    # replace this for solution
    print(dt.strptime(time, '%H:%M').strftime('%I:%M %p').replace('PM', 'p.m.').replace('AM', 'a.m.').lstrip('0'))



time_converter("12:30") == "12:30 p.m."
time_converter("09:00") == "9:00 a.m."
