class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2


def fight(first, second):

    while first.is_alive and second.is_alive:

        if isinstance(first, Defender):
            second.health -= first.attack
            if second.is_alive:
                if second.attack > first.defence:
                    first.health -= (second.attack - first.defence)

        elif isinstance(second, Defender):
            if first.attack > second.defence:
                second.health -= (first.attack - second.defence)
                if second.is_alive:
                    first.health -= second.attack            

        else:            
            second.health -= first.attack
            if second.is_alive:
                first.health -= second.attack

    return first.is_alive


class Army:

    def __init__(self):
        self.units = []

    def add_units(self, utype, amount):
        for unit in range(amount):
            unit = utype()
            self.units.append(unit)


class Battle:

    def fight(self, first, second):
        while first.units and second.units:
            if fight(first.units[0], second.units[0]):
                second.units.pop(0)
            else:
                first.units.pop(0)

        return len(first.units) > 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
