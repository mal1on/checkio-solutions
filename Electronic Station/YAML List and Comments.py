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

    return yaml_str


def yaml(a):

    lines = [b.split(':')
             for b in a.splitlines() if b and not b.startswith('#')]

    if all(len(line) == 2 for line in lines):

        result = {}

        for k, v in lines:

            result[k] = yaml_converter(v)

    elif all(line[0].startswith('-') for line in lines):

        result = []

        for line in lines:
            line = line[0].replace('- ', '')
            if line == '-':
                result.append(None)
            elif line.startswith('"') and '#' in line:
                result.append(line.replace('"', ''))
            else:
                result.append(yaml_converter(line.split('#')[0]))

    return result


if __name__ == "__main__":
    print("Example:")
    print(yaml('- write some\n- "Alex Chii"\n- 89'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml(
        '- write some\n- "Alex Chii"\n- 89') == ["write some", "Alex Chii", 89]
    assert yaml(
        "# comment\n"
        "- write some # after\n"
        "# one mor\n"
        '- "Alex Chii #sir "\n'
        "- 89 #bl"
    ) == ["write some", "Alex Chii #sir ", 89]
    assert yaml("- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5") == [1, 2, 3, 4, 5]
    assert yaml("-\n-\n-\n- 7") == [None, None, None, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
