import re


def find_word(message):

    result = []

    def likeness(w1, w2):

        result = 0
        w1, w2, = w1.lower(), w2.lower()
        unique = len(set(w1 + w2))
        common = len(set([l for l in w1 if l in w2])) if len(
            w1) >= len(w2) else len(set([l for l in w2 if l in w1]))

        if w1[0] == w2[0]:
            result += 10
        if w1[-1] == w2[-1]:
            result += 10
        if len(w1) <= len(w2):
            result += (len(w1) / len(w2)) * 30
        else:
            result += (len(w2) / len(w1)) * 30
        result += (common / unique) * 50

        return result

    message = re.findall(r'\w+', message)

    for word in message:
        temp = message[:message.index(word)] + \
            message[message.index(word) + 1:]
        temp_result = []
        for w in temp:
            temp_result.append(likeness(word, w))
        result.append((word.lower(), sum(temp_result) / len(temp_result)))

    return max(result[::-1], key=lambda a: a[1])[0]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert (
        find_word(
            "The Doors of Durin, Lord of Moria. Speak friend and enter. "
            "I Narvi made them. Celebrimbor of Hollin drew these signs"
        )
        == "durin"
    ), "Durin"
    assert (
        find_word(
            "Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
            " According to a researcher at Cambridge University."
        )
        == "according"
    ), "Research"
    assert find_word(
        "One, two, two, three, three, three.") == "three", "Repeating"
