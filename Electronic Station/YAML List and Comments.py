def yaml(a):

    result = {}

    for k, v in [b.split(':') for b in a.splitlines() if b]:

        v = v.strip()

        if v.isdigit():
            result[k] = int(v)
        elif v == 'true':
            result[k] = True
        elif v == 'false':
            result[k] = False
        elif not v or v == 'null':
            result[k] = None
        elif '\\' in v:
            result[k] = v.replace('"', '').replace('\\', '"')
        elif '"' in v:
            result[k] = v.replace('"', '')
        else:
            result[k] = v

    print(result)


yaml('- write some\n- "Alex Chii"\n- 89') == ['write some', 'Alex Chii', 89]