def calculator(log):
    screen = ''
    ops = ['=', '+', '-']
    log = log.lstrip('0')
    log = log if log else '0'
    for ch in log:
        if ch.isnumeric():
            screen += ch

    print(screen)



# calculator("000000") == "0"
# calculator("0000123") == "123"
# calculator("12") == "12"
# calculator("+12") == "12"
# calculator("") == "0"
# calculator("1+2") == "2"
# calculator("2+") == "2"
# calculator("1+2=") == "3"
# calculator("1+2-") == "3"
# calculator("1+2=2") == "2"
calculator("=5=10=15") == "15"
