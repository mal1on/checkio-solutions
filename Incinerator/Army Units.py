class Army:
    def __init__(self):
        self.descend = ''

    def train_swordsman(self, name):
        unit = Swordsman(name)
        if self.descend == 'Asian':
            unit.descend = 'Asian'
            unit.descend_type = 'Samurai'
        elif self.descend == 'European':
            unit.descend = 'European'
            unit.descend_type = 'Knight'
        return unit

    def train_lancer(self, name):
        unit = Lancer(name)
        if self.descend == 'Asian':
            unit.descend = 'Asian'
            unit.descend_type = 'Ronin'
        elif self.descend == 'European':
            unit.descend = 'European'
            unit.descend_type = 'Raubritter'
        return unit

    def train_archer(self, name):
        unit = Archer(name)
        if self.descend == 'Asian':
            unit.descend = 'Asian'
            unit.descend_type = 'Shinobi'
        elif self.descend == 'European':
            unit.descend = 'European'
            unit.descend_type = 'Ranger'
        return unit


class Swordsman:
    def __init__(self, name):
        self.name = name
        self.type = 'swordsman'
        self.descend = ''
        self.descend_type = ''

    def introduce(self):
        return f'{self.descend_type} {self.name}, {self.descend} {self.type}'


class Lancer:
    def __init__(self, name):
        self.name = name
        self.type = 'lancer'

    def introduce(self):
        return f'{self.descend_type} {self.name}, {self.descend} {self.type}'


class Archer:
    def __init__(self, name):
        self.name = name
        self.type = 'archer'

    def introduce(self):
        return f'{self.descend_type} {self.name}, {self.descend} {self.type}'


class AsianArmy(Army):
    def __init__(self):
        super().__init__()
        self.descend = 'Asian'


class EuropeanArmy(Army):
    def __init__(self):
        super().__init__()
        self.descend = 'European'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
