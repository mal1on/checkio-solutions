def checkio(number):
    triangulars = [0]
    current = 1
    while triangulars[-1] < number:
        triangulars.append(triangulars[-1] + current)
        current += 1
    for ind, num in enumerate(triangulars):
        result = []
        for item in triangulars[ind + 1:]:
            result.append(item)
            if sum(result) == number:
                return result
            elif sum(result) > number:
                result = []
    return []


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
