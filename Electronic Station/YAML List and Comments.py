def yaml_converter(yaml_str):

    if yaml_str.strip() in ('', 'null'):
        return None
    elif yaml_str[0] in ('"\''):
        return yaml_str.replace('"', '')

    yaml_str = yaml_str.split('#')[0].strip()

    if yaml_str.isdigit():
        return int(yaml_str)
    elif yaml_str in ('true', 'false'):
        return yaml_str == 'true'

    return yaml_str.replace('"', '').replace('\\', '"')


def yaml(a):

    lines = [line.strip()
             for line in a.splitlines() if line and not line.startswith('#')]

    if lines[0].startswith('-'):
        return [yaml_converter(line[2:]) for line in lines]
    return {k: yaml_converter(v) for k, v in [l.split(':') for l in lines]}


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
