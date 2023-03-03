def subnetworks(net, crushes):
    subs = []
    for crush in crushes:
        for a, b in net:
            if crush == a:
                subs.append([b])
            elif crush == b:
                subs.append([a])
            elif [a] not in subs and [b] not in subs:
                subs.append([a, b])
    print(subs)





# subnetworks([
#         ['A', 'B'],
#         ['B', 'C'],
#         ['C', 'D']
#     ], ['B']) == 2
# subnetworks([
#         ['A', 'B'],
#         ['A', 'C'],
#         ['A', 'D'],
#         ['D', 'F']
#     ], ['A']) == 3
subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1
