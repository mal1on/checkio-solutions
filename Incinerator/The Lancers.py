class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other):
        other.loss(self.attack)

    def damage(self, attack):
        return attack

    def loss(self, attack):
        self.health -= self.damage(attack)


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):

    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defence = 2

    def damage(self, attack):
        return max(0, attack - self.defence)


class Vampire(Warrior):

    def __init__(self):
        self.health = 40
        self.attack = 4
        self.vampirism = 50

    def hit(self, other):
        other.loss(self.attack)
        self.health += other.damage(self.attack) * self.vampirism / 100


class Lancer(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 6


def fight(first_u, second_u):

    while first_u.is_alive and second_u.is_alive:

        first_u.hit(second_u)
        if second_u.is_alive:
            second_u.hit(first_u)

    return first_u.is_alive


class Army:

    def __init__(self):
        self.units = []

    def add_units(self, utype, amount):
        for unit in range(amount):
            self.units.append(utype())

    @property
    def first_alive(self):
        for unit in self.units:
            if unit.is_alive:
                return unit

    @property
    def is_alive(self):
        return any(unit.is_alive for unit in self.units)


class Battle:

    def fight(self, first_a, second_a):
        while first_a.is_alive and second_a.is_alive:
            fight(first_a.first_alive, second_a.first_alive)
        return first_a.is_alive


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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
