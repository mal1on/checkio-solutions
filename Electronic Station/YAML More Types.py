def yaml(a):

    result = {}

    for k, v in [b.split(': ') for b in a.splitlines() if b]:

        if v.isdigit():
            result[k] = int(v)
        elif v == 'true':
            result[k] = True 
        elif v == 'false':
            result[k] = False
        else: 
            result[k] = v        



    print(result)


yaml('name: "Bob Dylan"\n' "children: 6\n" "coding:") == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }