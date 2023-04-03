def sort_by_removing(values: list) -> list:
    if values:
        next_val = values[0]
        result = [values[0]]
    else:
        return values
    for i in values[1:]:
        if i >= next_val:
            result.append(i)
            next_val = i
    return result


if __name__ == '__main__':
    print("Example:")
    print(sort_by_removing([3, 5, 2, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_removing([3, 5, 2, 6]) == [3, 5, 6]
    assert sort_by_removing([7, 6, 5, 4, 3, 2, 1]) == [7]
    assert sort_by_removing([3, 3, 3, 3]) == [3, 3, 3, 3]
    assert sort_by_removing([5, 6, 7, 0, 7, 0, 10]) == [5, 6, 7, 7, 10]
    assert sort_by_removing([1, 5, 2, 3, 4, 7, 8]) == [1, 5, 7, 8]
    assert sort_by_removing([1, 7, 2, 3, 4, 5]) == [1, 7]
    assert sort_by_removing([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
