def flatten(d, key=''):
    items = [] if d else [(key, '')]
    for k, v in d.items():
        new_key = key + '/' + k if key else k
        try:
            items.extend(flatten(v, new_key).items())
        except:
            items.append((new_key, v))
    return dict(items)


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
