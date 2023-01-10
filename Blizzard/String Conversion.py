def steps_to_convert(line1, line2):
    
    changes = 0

    if len(line1) == len(line2):
        for ind, char in enumerate(line2):
            if line1[ind] != char:
                changes += 1
    else:
        changes += abs(len(line2) - len(line1))

    print(changes)    






steps_to_convert('line1', 'line2') == 1
steps_to_convert('line1', 'line1') == 0
steps_to_convert('line1', 'line2') == 1
steps_to_convert('ine', 'line2') == 2    