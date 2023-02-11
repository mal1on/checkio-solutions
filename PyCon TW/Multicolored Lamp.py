class Lamp:
    pass




lamp_1 = Lamp()
lamp_2 = Lamp()

lamp_1.light() #Green
lamp_1.light() #Red
lamp_2.light() #Green
    
lamp_1.light() == "Blue"
lamp_1.light() == "Yellow"
lamp_1.light() == "Green"
lamp_2.light() == "Red"
lamp_2.light() == "Blue"    