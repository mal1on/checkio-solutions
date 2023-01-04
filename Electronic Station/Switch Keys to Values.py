def switch_dict(data: dict[str, str]) -> dict[str, str]:
    # your code here

    result = {}

    for k, v in data.items():
        if v in result.keys():
            result[v].add(k)
        else:
            result[v] = {k}

    return result


print("Example:")
print(switch_dict({"rouses": "red", "car": "red", "sky": "blue"}))

# These "asserts" are used for self-checking
assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
    "red": {"car", "rouses"},
    "blue": {"sky"},
}
assert switch_dict({"1": "one", "2": "two", "3": "one", "4": "two"}) == {
    "one": {"3", "1"},
    "two": {"4", "2"},
}
assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
    "b": {"a"},
    "c": {"b"},
    "a": {"c"},
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
