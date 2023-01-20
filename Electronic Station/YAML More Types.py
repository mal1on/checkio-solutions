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

    return result


if __name__ == "__main__":
    print("Example:")
    print(yaml("name: Alex\nage: 12"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("name: Alex\nage: 12") == {"age": 12, "name": "Alex"}
    assert yaml("name: Alex Fox\n" "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": "Alex Fox",
    }
    assert yaml('name: "Alex Fox"\n' "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": "Alex Fox",
    }
    assert yaml('name: "Alex \\"Fox\\""\n' "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": 'Alex "Fox"',
    }
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" "alive: false") == {
        "alive": False,
        "children": 6,
        "name": "Bob Dylan",
    }
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" "coding:") == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" "coding: null") == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" 'coding: "null" ') == {
        "children": 6,
        "coding": "null",
        "name": "Bob Dylan",
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
