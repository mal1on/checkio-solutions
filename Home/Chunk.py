from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    # your code here
    chunks = []
    start = 0
    for item in range(0, len(items), size):
        chunk = items[start:start + size]
        chunks.append(chunk)
        start += size
    return chunks    


print("Example:")
print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []
assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]

print("The mission is done! Click 'Check Solution' to earn rewards!")