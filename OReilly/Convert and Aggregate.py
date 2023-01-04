def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    # your code here
    result = {key[0]: 0 for key in data if key[0] != ''}
    for item in data:
        if item[0] in result.keys():
            result[item[0]] += item[1]
    return dict(filter(lambda pair: pair[1] != 0, result.items()))


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

# These "asserts" are used for self-checking
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
