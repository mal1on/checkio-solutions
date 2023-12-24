from typing import Dict


def count_comprehensions(source: str) -> Dict[str, int]:

    pass


count_comprehensions('[n ** 2 for n in range(5)]') == {'ListComp': 1}
count_comprehensions('list(n ** 2 for n in range(5))') == {'GeneratorExp': 1}
count_comprehensions('''\
limit = 100
assert all(
    sum(n ** 3 for n in range(N)) == (N * (N - 1) // 2) ** 2
    for N in range(1, limit)
)
''') == {'GeneratorExp': 2}
