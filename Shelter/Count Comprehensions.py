import ast


def count_comprehensions(source):

    result = {'ListComp': 0, 'SetComp': 0, 'DictComp': 0,  'GeneratorExp': 0}
    output = ast.dump(ast.parse(source))

    if 'ListComp' in output:
        result['ListComp'] += output.count('ListComp')
    else:
        result.pop('ListComp')
    if 'SetComp' in output:
        result['SetComp'] += output.count('SetComp')
    else:
        result.pop('SetComp')
    if 'DictComp' in output:
        result['DictComp'] += output.count('DictComp')
    else:
        result.pop('DictComp')
    if 'GeneratorExp' in output:
        result['GeneratorExp'] += output.count('GeneratorExp')
    else:
        result.pop('GeneratorExp')

    print(result)


count_comprehensions('[n ** 2 for n in range(5)]') == {'ListComp': 1}
count_comprehensions('list(n ** 2 for n in range(5))') == {'GeneratorExp': 1}
count_comprehensions('''\
limit = 100
assert all(
    sum(n ** 3 for n in range(N)) == (N * (N - 1) // 2) ** 2
    for N in range(1, limit)
)
''') == {'GeneratorExp': 2}
