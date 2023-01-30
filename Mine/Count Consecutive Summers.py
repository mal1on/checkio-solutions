def count_consecutive_summers(num):
    # your code here
    diffs = 1

    for f_num in range(1, num + 1):
        for s_num in range(f_num + 1, num + 1):
            f_num += s_num
            if f_num == num:
                diffs += 1
                break
    print(diffs)                




count_consecutive_summers(42) == 4
count_consecutive_summers(99) == 6    