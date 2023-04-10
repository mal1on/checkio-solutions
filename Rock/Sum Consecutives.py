def sum_consecutives(a):
    if not a:
        return []
    else:
        result = []
        current = current_sum = a[0]
        for i in a[1:]:
            if i == current:
                current_sum += i
            else:
                result.append(current_sum)
                current_sum = current = i
        result.append(current_sum)
        print(result)


sum_consecutives([1, 1, 1, 1]) == [4]
sum_consecutives([1, 1, 2, 2]) == [2, 4]
sum_consecutives([1, 1, 2, 1]) == [2, 2, 1]
sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6]) == [9, 8, 5, 12]
sum_consecutives([1]) == [1]
sum_consecutives([]) == []
