def checkio(price, denominations):
    """
        return the minimum number of coins that add up to the price
    """
    result = []

    for i in range(len(denominations)):
        temp = []
        for coin in denominations[::-1][i:]:
            while sum(temp + [coin]) <= price:
                temp.append(coin)
        result.append(temp)

    print(len(min(result, key=len)))



checkio(8, [1, 3, 5]) == 2
checkio(12, [1, 4, 5]) == 3
