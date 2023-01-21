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

    lines = [b.split(':') for b in a.splitlines() if b and not b.startswith('#')]

    if all(len(line) == 2 for line in lines):

        result = {}

        for k, v in lines:

            result[k] = yaml_converter(v)

    elif all(line[0].startswith('-') for line in lines):

        result = []

        for line in lines:
            line = line[0].replace('- ', '')
            if line.startswith('"') and '#' in line:
                result.append(line.replace('"', ''))
            else:
                line = yaml_converter(line.split('#')[0])
                result.append(line)    

    print(result)


yaml("-\n-\n-\n- 7") == [None, None, None, 7]