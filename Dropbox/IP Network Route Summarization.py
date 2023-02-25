def binary_prefix(prefix):
    return ''.join(format(o, '08b') for o in map(int, prefix.split('.')))


def checkio(data):
    b_prefixes = [binary_prefix(p) for p in data]
    b_mask = []
    for i in zip(*b_prefixes):
        if len(set(i)) == 1:
            b_mask.append(i[0])
        else:
            break

    subnet = str(len(b_mask))
    d_mask, octet = '', ''
    while b_mask:
        if len(octet) < 8:
            octet += b_mask.pop(0)
        elif len(octet) == 8:
            d_mask += str(int(octet, 2)) + '.'
            octet = ''
    d_mask += str(int(octet[::-1].zfill(8)[::-1], 2))
    mask = d_mask + (4 - len(d_mask.split('.'))) * '.0'

    print(mask + '/' + subnet)


checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"
