class Chat:

    def __init__(self):
        self.dialogue = []
        self.human = ''
        self.robot = ''
    
    def connect_human(self, human):
        self.human = human.name
        human.chat = self

    def connect_robot(self, robot):
        self.robot = robot.sn
        robot.chat = self

    def show_human_dialogue(self):
        human_dialogue = ''
        for speaker, line in self.dialogue:
            human_dialogue += f'{speaker} said: {line} \n'
        print(human_dialogue)    

    def show_robot_dialogue(self):
        robot_dialogue = ''
        for speaker, line in self.dialogue:
            for char in line:
                if char in "aeiouAEIOU":
                    line = line.replace(char, '0')
                else:
                    line = line.replace(char, '1')       
            robot_dialogue += f'{speaker} said: {line} \n'
        print(robot_dialogue)            



class Human:
    
    def __init__(self, name):
        self.name = name
        self.chat = ''
    def send(self, msg):
        self.chat.dialogue.append((self.name, msg))
            

class Robot:
    
    def __init__(self, sn):
        self.sn = sn
    def send(self, msg):
        self.chat.dialogue.append((self.sn, msg))    




chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi! What's new?")
bot.send("Hello, human. Could we speak later about it?")
chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""
    