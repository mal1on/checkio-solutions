def flatten(d, key=''):
    items = [] if d else [(key, '')]
    for k, v in d.items():
        new_key = key + '/' + k if key else k
        try:
            items.extend(flatten(v, new_key).items())
        except:
            items.append((new_key, v))
    return dict(items)


# print(flatten({"key": "value"})) == {"key": "value"}
# print(flatten({"key": {"deeper": {"more": {"enough": "value"}}}})) == {"key/deeper/more/enough": "value"}
print(flatten({"empty": {}})) == {"empty": ""}
