def yaml_converter(yaml_str):

    yaml_str = yaml_str.strip()

    if yaml_str.isdigit():
        yaml_str = int(yaml_str)
    elif yaml_str == 'true':
        yaml_str = True
    elif yaml_str == 'false':
        yaml_str = False
    elif not yaml_str or yaml_str == 'null':
        yaml_str = None
    elif '\\' in yaml_str:
        yaml_str = yaml_str.replace('"', '').replace('\\', '"')
    elif '"' in yaml_str:
        yaml_str = yaml_str.replace('"', '')
    else:
        yaml_str = yaml_str

    return yaml_str


def yaml(a):

    result = {}
    lines = [b.split(':') for b in a.splitlines() if b and not b.startswith('#')]

    if all(len(line) == 2 for line in lines):

        for k, v in lines:

            result[k] = yaml_converter(v)

    elif all(line[0].startswith('-') for line in lines):

        result = [yaml_converter(line[0].replace('- ', '')) for line in lines]

                    

    print(result)


yaml('- write some\n- "Alex Chii"\n- 89') == ['write some', 'Alex Chii', 89]

yaml('# comment\n'
 '- write some # after\n'
 '# one mor\n'
 '- "Alex Chii #sir "\n'
 '- 89 #bl') == ['write some', 'Alex Chii #sir ', 89]

yaml('name: "Bob Dylan"\n' "children: 6\n" "coding:") == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }