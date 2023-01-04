def translate(text: str) -> str:
    # your code here
    vowels = 'aeiouy'
    result = ''
    index = 0
    while index < len(text):
        if text[index] not in vowels:
            result += text[index]
        elif text[index] in vowels and text[index: index + 3] == text[index] * 3:
            result += text[index]
            index += 2     
        index += 1    
    return result       


print("Example:")
print(translate("hieeelalaooo"))

assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")