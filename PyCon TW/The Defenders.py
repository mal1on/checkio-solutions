class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0

    def get_hit(self, enemy):
        self.health -= max(0, enemy.attack - self.defence)

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defence = 2


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, num):
        [self.units.append(unit()) for _ in range(num)]


class Battle:
    def fight(self, a1, a2):
        while a1.units and a2.units:
            if fight(a1.units[0], a2.units[0]):
                a2.units.pop(0)
            else:
                a1.units.pop(0)
        return bool(a1.units)


def fight(w1, w2):
    while w1.is_alive and w2.is_alive:
        w2.get_hit(w1)
        if w2.is_alive:
            w1.get_hit(w2)
    return w1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
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

    # battle tests
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
