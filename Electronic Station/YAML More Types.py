def yaml(a):

    result = {}

    for k, v in [b.split(': ') for b in a.splitlines() if b]:

        result[k] = int(v) if v.isdigit() else v

    return result



yaml("""name: Alex Fox
age: 12
class: 12b""") == {"age": 12, "class": "12b", "name": "Alex Fox"}