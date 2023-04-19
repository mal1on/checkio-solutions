def power_supply(network, power_plants):

    supplied = []

    for pp in power_plants:
        if power_plants[pp] == 0:
            chunk = set()
        else:
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

            chunk = set([i for l in tree for i in l if i not in power_plants])
        supplied.append(chunk)

    print(set([i for l in network for i in l if i not in [i for s in supplied for i in s] + list(power_plants.keys())]))



power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['с2'])
power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3'])
power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([])
power_supply([["c0", "p1"], ["p1", "c2"]], {"p1": 0}) == set(["c0", "c2"])
power_supply([["p0", "c1"], ["p0", "c2"], ["c2", "c3"], ["c3", "p4"], ["p4", "c5"]],{"p0": 1, "p4": 1},) == set([])
