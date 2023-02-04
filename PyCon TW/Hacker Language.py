def encrypt(text):
    result = ''
    for char in text:
        if char.isalpha():
            result += bin(ord(char))[2:]
        elif char == ' ':
            result += '1000000'
        else:
            result += char
    return result


def decrypt(text):
    result = ''
    while text:
        if text[:7] == '1000000':
            result += ' '
            text = text[7:]
        elif all(c == '0' or c == '1' for c in text[:7]):
            result += chr(int(text[:7], 2))
            text = text[7:]
        else:
            result += text[:1]
            text = text[1:]
    return result


class HackerLanguage:
    def __init__(self):
        self.source = ''

    def write(self, msg):
        self.source += msg

    def delete(self, pos):
        self.source = self.source[:-pos]

    def send(self):
        return encrypt(self.source)

    def read(self, msg):
        return decrypt(msg)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")