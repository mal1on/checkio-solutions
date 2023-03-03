def subnetworks(net, crushes):
    for crush in crushes:
        for link in net:
            if crush in link:
                link.remove(crush)
    singles = [sub for sub in net if len(sub) == 1]
    doubles = [sub for sub in net if len(sub) == 2]
    print(singles, doubles)
    subs = len(doubles)
    for single in singles:
        if single[0] not in [node for link in doubles for node in link]:
            subs += 1
    print(subs)



subnetworks([['A', 'B'],['B', 'C'],['C', 'D']], ['B']) == 2
subnetworks([['A', 'B'],['A', 'C'],['A', 'D'],['D', 'F']], ['A']) == 3
subnetworks([['A', 'B'],['B', 'C'],['C', 'D']], ['C', 'D']) == 1
subnetworks([["A","B"],["A","C"],["A","D"],["D","F"],["B","C"]],["A"]) == 2
