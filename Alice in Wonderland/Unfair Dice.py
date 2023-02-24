def winning_die(enemy_die):
    return []




winning_die([3, 3, 3, 3, 6, 6]) == [4, 4, 4, 4, 4, 4] # Or [3, 3, 4, 4, 5, 5]
winning_die([4, 4, 4, 4, 4, 4]) == [2, 2, 5, 5, 5, 5] # Or [5, 5, 2, 2, 5, 5]
winning_die([2, 2, 5, 5, 5, 5]) == [3, 3, 3, 3, 6, 6]
winning_die([1, 1, 3]) == [1, 2, 2]
winning_die([1, 2, 3, 4, 5, 6]) == [] # Any 6-sided die totaling 21 has a 50/50 chance of winning against the standard die.
winning_die([2, 3, 4, 5, 6, 7]) == [1, 1, 3, 7, 7, 8] # This can be beat though.
winning_die([1, 2, 3, 4, 5, 6]) == []
