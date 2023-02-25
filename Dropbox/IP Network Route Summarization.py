def binary_prefix(prefix):
    return ''.join(format(o, '08b') for o in map(int, prefix.split('.')))


def checkio(data):
    b_prefixes = [binary_prefix(p) for p in data]
    mask = ''
    for i in zip(*b_prefixes):
        if len(set(i)) == 1:
            mask += i[0]
        else:
            break
    print(mask, len(mask))






checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"
# checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"
# checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"
