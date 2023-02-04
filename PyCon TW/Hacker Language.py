class HackerLanguage:
    def __init__(self):
        self.source = ''
    def write(self, msg):
        self.source += msg
    def delete(self, pos):
        self.source = self.source[:-pos]
    def send(self):
        pass        




message_1 = HackerLanguage()
message_1.write('Remember: 21.07.2018 at 11:11AM')
message_1.delete(2)
print(message_1.source)
message_1.write('PM')
print(message_1.source)
message_1.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'    