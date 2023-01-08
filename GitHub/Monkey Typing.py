def count_words(text: str, words: set) -> int:

    count = []

    for word in words:
        for item in text.lower().split():
            if word in item:
                print(item, word)
                count.append(word)

    return len(set(count))




count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}) == 1
