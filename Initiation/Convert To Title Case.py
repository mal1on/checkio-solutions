def count_occurrences(main_str: str, sub_str: str) -> int:

    result = start = 0
    main_str = main_str.lower()
    sub_str = sub_str.lower()

    while start <= (len(main_str) - len(sub_str)):
        if main_str.find(sub_str, start) != -1:
            result += 1
            start += main_str.find(sub_str, start) + 1
        else:
            break

    return result


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
