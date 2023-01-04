def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:

    result = {}

    for item in data:
        keyop, value = item
        try:
            key, op = keyop[1:], keyop[0]
        except IndexError:
            key, op = '', keyop
        result[key] = 0

    for item in data:
        keyop, value = item
        try:
            key, op = keyop[1:], keyop[0]
        except IndexError:
            key, op = '', keyop
        if op == '/' and value == 0:
            continue
        if op != '=':
            result[key] = eval(f'{str(result[key])}{op}{str(value)}')
        else:
            result[key] = value

    return {k: v for k, v in result.items() if k and v}


print("Example:")
print(aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]))

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation(
    [("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
