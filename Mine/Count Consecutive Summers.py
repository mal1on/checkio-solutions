def count_consecutive_summers(num):

    diffs = 1

    for f_num in range(1, num + 1):
        for s_num in range(f_num + 1, num + 1):
            f_num += s_num
            if f_num == num:
                diffs += 1
                break

    return diffs                


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")   