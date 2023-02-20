def reveal_num(line):
    dot = True
    sign = ''
    result = ''
    for char in line:
        if char == '.' and dot:
            result += char
            dot = False
        elif char.isdigit():
            result += char
        elif char in ['-', '+'] and not result:
            sign = char

    print(eval(sign + result) if result else None)




reveal_num("F0(t}") == 0
reveal_num("Utc&g") == None
reveal_num("-aB%|_-+2ADS.12+3.ADS1.2") == 2.12312
reveal_num("-aB%|_+-2ADS.12+3.ADS1.2") == -2.12312
