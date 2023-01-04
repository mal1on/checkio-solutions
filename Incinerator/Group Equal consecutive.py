def group_equal(els):

    result = []

    temp = [els[0]] if els else []

    for ind, el in enumerate(els[1:]):
        if el in temp:
            temp.append(el)
        else:
            result.append(temp)
            temp = [els[ind + 1]]
    if temp:
        result.append(temp)

    return result


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [
        [1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
