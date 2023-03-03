def subnetworks(net, crushes):
    for crush in crushes:
        for link in net:
            if crush in link:
                link.remove(crush)
    singles = [sub for sub in net if len(sub) == 1]
    doubles = [sub for sub in net if len(sub) == 2]
    subs = len(doubles)
    for single in singles:
        if single[0] not in [node for double in doubles for node in double]:
            subs += 1
    return subs


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2, "First"
    assert subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3, "Second"
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
