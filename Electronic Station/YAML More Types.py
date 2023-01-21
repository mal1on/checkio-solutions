def yaml_converter(yaml_str):

    yaml_str = yaml_str.strip()

    if yaml_str.isdigit():
        return int(yaml_str)
    elif yaml_str in ('true', 'false'):
        return yaml_str == 'true'
    elif yaml_str in ('', 'null'):
        return None
    else:
        return yaml_str.replace('"', '').replace('\\', '"')


def yaml(a):

    result = {}

    for k, sep, v in [line.partition(':') for line in a.splitlines()]:
        if sep:
            result[k] = yaml_converter(v)

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
