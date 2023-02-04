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


message_1 = HackerLanguage()
message_1.write('Remember: 21.07.2018 at 11:11AM')
message_1.delete(2)
message_1.write('PM')
message_1.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'

message_2 = HackerLanguage()
message_2.read('10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101')
