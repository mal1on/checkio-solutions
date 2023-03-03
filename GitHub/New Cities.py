def subnetworks(net, crushes):
    for crush in crushes:
        for link in net:
            if crush in link:
                link.remove(crush)
    return len(set(node for link in net for node in link)) - 1





subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2
subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3
subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1
