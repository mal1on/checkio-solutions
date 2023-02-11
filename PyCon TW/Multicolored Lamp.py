from itertools import cycle


class Lamp:
    def __init__(self):
        self.colors = (c for c in cycle(['Green', 'Red', 'Blue', 'Yellow']))
    def light(self):
        return next(self.colors)    




lamp_1 = Lamp()
lamp_2 = Lamp()

print(lamp_1.light()) #Green
print(lamp_1.light()) #Red
print(lamp_2.light()) #Green
    
print(lamp_1.light()) == "Blue"
print(lamp_1.light()) == "Yellow"
print(lamp_1.light()) == "Green"
print(lamp_2.light()) == "Red"
print(lamp_2.light()) == "Blue"