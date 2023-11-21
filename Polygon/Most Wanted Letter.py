from collections import Counter

def most_wanted(text: str) -> str:

    c = Counter(char for char in text.lower() if char.isalpha())
    max_count = c.most_common(1)[0][1]
    print([el for el in c if c[el] == max_count])





most_wanted("Hello World!") == ["l"]
most_wanted("How do you do?") == ["o"]
most_wanted("One") == ["o", "n", "e"]
most_wanted("Oops!") == ["o"]
most_wanted("AAaooo!!!!") == ["a", "o"]
most_wanted("abe") == ["a", "b", "e"]
