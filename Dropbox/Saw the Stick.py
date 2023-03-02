def checkio(number):
    triangulars = [0]
    current = 1
    while triangulars[-1] < number:
        triangulars.append(triangulars[-1] + current)
        current += 1
    results = []
    for ind, num in enumerate(triangulars):
        result = []
        for item in triangulars[ind:]:
            result.append(item)
            if sum(result) == number:
                results.append(result)
                break
            elif sum(result) > number:
                result = []
    print(results[0] if results else [])




checkio(64) == [15, 21, 28]
checkio(371) == [36, 45, 55, 66, 78, 91]
checkio(225) == [105, 120]
checkio(882) == []
