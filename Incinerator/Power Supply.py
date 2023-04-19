def power_supply(network, power_plants):

    supplied = []

    for pp in power_plants:
        if power_plants[pp] == 0:
            tree = []
        elif power_plants[pp] == 1:
            tree = [[pp]] + [mult * [] for mult in range(power_plants[pp])]
            for a, b in sorted(network, key=lambda con: pp in con, reverse = True):
                if a == pp:
                    tree[1].append(b)
                if b == pp:
                    tree[1].append(a)
        else:
            tree = [[pp]] + [mult * [] for mult in range(power_plants[pp])]
            for depth in range(1, power_plants[pp]):
                for a, b in sorted(network, key=lambda con: pp in con, reverse = True):
                    if a == pp:
                        tree[1].append(b)
                    if b == pp:
                        tree[1].append(a)
                    if power_plants[pp] > 1:
                        if a in tree[depth] and b not in [i for l in tree[:depth] for i in l]:
                            tree[depth + 1].append(b)
                        if b in tree[depth] and a not in [i for l in tree[:depth] for i in l]:
                            tree[depth + 1].append(a)
        chunk = set([i for l in tree for i in l if i not in power_plants])
        supplied.append(chunk)

    print(set([i for l in network for i in l if i not in [i for s in supplied for i in s] + list(power_plants.keys())]))



power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['с2'])
power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3'])
power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([])
power_supply([["c0", "p1"], ["p1", "c2"]], {"p1": 0}) == set(["c0", "c2"])
power_supply([["p0", "c1"], ["p0", "c2"], ["c2", "c3"], ["c3", "p4"], ["p4", "c5"]],{"p0": 1, "p4": 1},) == set([])
power_supply(
        [
            ["p0", "c1"],
            ["p0", "c2"],
            ["p0", "c3"],
            ["p0", "c4"],
            ["c4", "c9"],
            ["c4", "c10"],
            ["c10", "c11"],
            ["c11", "p12"],
            ["c2", "c5"],
            ["c2", "c6"],
            ["c5", "c7"],
            ["c5", "p8"],
        ],
        {"p0": 1, "p12": 4, "p8": 1},
    ) == set(["c6", "c7"]), "complex cities 2"
