from datetime import datetime, timedelta


def vacation(date, days):
    #replace this for solution
    fwd = datetime.strptime(date, '%Y-%m-%d') + timedelta(days)
    match fwd.isoweekday():
        case 6:
            fwd += timedelta(2)
        case 7:
            fwd += timedelta(1)


    print(fwd.date())



vacation('2018-07-01', 14) == '2018-07-16'
vacation('2018-02-19', 10) == '2018-03-01'
vacation('2000-02-28', 5) == '2000-03-06'
vacation('1999-12-20', 14) == '2000-01-03'
