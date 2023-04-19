def power_supply(network, power_plants):

    supplied = []

    for pp in power_plants:
        if power_plants[pp] == 0:
            tree = []
        elif power_plants[pp] == 1:
            tree = [[pp]] + [mult * [] for mult in range(power_plants[pp])]
            for a, b in sorted(network, key=lambda con: pp in con, reverse=True):
                if a == pp:
                    tree[1].append(b)
                if b == pp:
                    tree[1].append(a)
        else:
            tree = [[pp]] + [mult * [] for mult in range(power_plants[pp])]
            for depth in range(1, power_plants[pp]):
                for a, b in sorted(network, key=lambda con: pp in con, reverse=True):
                    if a == pp:
                        tree[1].append(b)
                    elif b == pp:
                        tree[1].append(a)
                    elif a in tree[depth] and b not in [i for l in tree[:depth] for i in l]:
                        tree[depth + 1].append(b)
                    elif b in tree[depth] and a not in [i for l in tree[:depth] for i in l]:
                        tree[depth + 1].append(a)
        supplied.append(
            set([i for l in tree for i in l if i not in power_plants]))

    return set([i for l in network for i in l if i not in [i for s in supplied for i in s] + list(power_plants.keys())])


if __name__ == "__main__":
    assert power_supply([["p1", "c1"], ["c1", "c2"]], {"p1": 1}) == set(
        ["c2"]
    ), "one blackout"
    assert power_supply(
        [["c0", "c1"], ["c1", "p1"], ["c1", "c3"], ["p1", "c4"]], {"p1": 1}
    ) == set(["c0", "c3"]), "two blackout"
    assert power_supply([["p1", "c1"], ["c1", "c2"], ["c2", "c3"]], {"p1": 3}) == set(
        []
    ), "no blackout"
    assert power_supply([["c0", "p1"], ["p1", "c2"]], {"p1": 0}) == set(
        ["c0", "c2"]
    ), "weak power-plant"
    assert power_supply(
        [["p0", "c1"], ["p0", "c2"], ["c2", "c3"], ["c3", "p4"], ["p4", "c5"]],
        {"p0": 1, "p4": 1},
    ) == set([]), "cooperation"
    assert power_supply(
        [
            ["c0", "p1"],
            ["p1", "c2"],
            ["c2", "c3"],
            ["c2", "c4"],
            ["c4", "c5"],
            ["c5", "c6"],
            ["c5", "p7"],
        ],
        {"p1": 1, "p7": 1},
    ) == set(["c3", "c4", "c6"]), "complex cities 1"
    assert power_supply(
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
    assert power_supply([["c1", "c2"], ["c2", "c3"]], {}) == set(
        ["c1", "c2", "c3"]
    ), "no power plants"
    assert power_supply(
        [["p1", "c2"], ["p1", "c4"], ["c4", "c3"], ["c2", "c3"]], {"p1": 1}
    ) == set(["c3"]), "circle"
    assert power_supply([["p1", "c2"], ["p1", "c4"], ["c2", "c3"]], {"p1": 4}) == set(
        []
    ), "more than enough"
    print("Looks like you know everything. It is time for 'Check'!")
