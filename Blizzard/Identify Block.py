def identify_block(numbers):

    result = None

    diff = max(numbers) - min(numbers)
    order = sorted(numbers)
    if diff == 3 or diff == 12:
        result = 'I'
    elif order[1] - order[0] == 1 and order[3] - order[2] == 1 and order[2] - order[1] > 1:
        result = 'O'
    elif order[2] - order[0] == 2 or order[2] - order[0] == 8 or order[3] - order[1] == 2 or order[3] - order[1] == 8:
        result = 'TJL'



    print(result)



identify_block({1, 2, 3, 4}) == 'I'
identify_block({11, 12, 15, 16}) == 'O'
identify_block({1, 2, 3, 6}) == 'T'
identify_block({1, 5, 6, 10}) == 'S'
identify_block({10, 13, 14, 15}) == 'T', 'T'
identify_block({1, 5, 9, 6}) == 'T', 'T'
