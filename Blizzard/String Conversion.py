def steps_to_convert(line1, line2):

    changes = 0

    if len(line1) == len(line2):
        for ind, char in enumerate(line2):
            if line1[ind] != char:
                changes += 1
    else:
        changes += abs(len(line2) - len(line1))

    return changes


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert("line1", "line1") == 0, "eq"
    assert steps_to_convert("line1", "line2") == 1, "2"
    assert steps_to_convert("line", "line2") == 1, "none to 2"
    assert steps_to_convert("ine", "line2") == 2, "need two more"
    assert steps_to_convert("line1", "1enil") == 4, "everything is opposite"
    assert steps_to_convert("", "") == 0, "two empty"
    assert steps_to_convert("l", "") == 1, "one side"
    assert steps_to_convert("", "l") == 1, "another side"
    print("You are good to go!")
