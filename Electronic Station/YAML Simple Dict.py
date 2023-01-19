def yaml(a):

    result = {}

    for k, v in [b.split(':') for b in a.splitlines() if b]:
        result[k] = v

    print(result)


yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}

yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
