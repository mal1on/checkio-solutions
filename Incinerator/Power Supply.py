def power_supply(network, power_plants):

    for pp in power_plants:
        tree = [[pp]] + [mult * [] for mult in range(power_plants[pp])]
        for a, b in sorted(network, key=lambda con: pp in con, reverse = True):
            if a == tree[0][0]:
                tree[1].append(b)
                continue
            if b == tree[0][0]:
                tree[1].append(a)
            if power_plants[pp] > 1:
                for depth in range(1, power_plants[pp]):
                    if a in tree[depth] and b not in [i for l in tree[:depth] for i in l]:
                        tree[depth + 1].append(b)

        result = set([i for l in network for i in l]).difference(set([i for l in tree for i in l]))

        print(result)



power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['с2'])
power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3'])
power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([])
