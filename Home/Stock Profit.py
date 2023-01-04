def stock_profit(stock: list) -> int:
    # your code here
    profit = []
    for pos, price in enumerate(stock[::-1]):
        for price2 in stock[:len(stock) - pos]:
            profit.append(price - price2)

    return max(profit)


print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")
