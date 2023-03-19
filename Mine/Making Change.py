def checkio(price, denominations):
    """
        return the minimum number of coins that add up to the price
    """
    result = float('inf')

    for i in range(len(denominations)):
        temp = []
        for coin in denominations[::-1][i:]:
            while sum(temp + [coin]) <= price and len(temp) < result:
                temp.append(coin)
        if sum(temp) == price:
            result = len(temp)
        print(temp)

    print(result if result < float('inf') else None)



checkio(8, [1, 3, 5]) == 2
checkio(12, [1, 4, 5]) == 3
checkio(1,[3,4,5]) == None
checkio(4,[3,5]) == None
checkio(123456,[1,6,7,456,678]) == 187
