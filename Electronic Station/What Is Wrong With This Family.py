def is_family(tree: list[list[str]]) -> bool:

    result = len(tree) == 1

    if len(tree) > 1:

        for item in tree:
            result = all(len(set(item)) == 2 for item in tree)
            ttree = [titem for titem in tree if titem != item]
            fathers = [titem[0] for titem in ttree]
            sons = [titem[1] for titem in ttree]
            if item[0] in fathers and item[1] in fathers:
                result = False
            if item[0] in sons or item[1] in sons:
                result = False
            for titem in ttree:
                if titem[0] not in sons and titem[0] != item[1] and titem[0] != item[0]:
                    result = False
            if len(ttree) > 1:
                if sorted(ttree[0]) == sorted(ttree[1]):
                    result = False
            if result == True:
                break

    return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    assert is_family([
        ['Jack', 'Mike'],
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
    ]) == False, 'Two fathers'
    print("Looks like you know everything. It is time for 'Check'!")
