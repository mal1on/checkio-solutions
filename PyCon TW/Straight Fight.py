class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0
        self.vampirism = 0
        self.buddy = None
        self.max_health = self.health

    def hit(self, enemy):
        dmg = max(0, self.attack - enemy.defence)
        enemy.health -= dmg
        self.health += self.vampirism * dmg
        if self.buddy and isinstance(self.buddy, Healer):
            self.buddy.heal(self)

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


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6

    def hit(self, enemy):
        dmg = max(0, self.attack - enemy.defence)
        half_dmg = max(0, self.attack / 2 - enemy.defence)
        enemy.health -= dmg
        if enemy.buddy:
            enemy.buddy.health -= half_dmg
        if self.buddy and isinstance(self.buddy, Healer):
            self.buddy.heal(self)


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 0

    def heal(self, unit):
        unit.health = min(unit.max_health, unit.health + 2)


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, num):
        [self.units.append(unit()) for _ in range(num)]

    def add_buddy(self):
        for unit, buddy in zip(self.units[:-1], self.units[1:]):
            unit.buddy = buddy


class Battle:
    def fight(self, a1, a2):
        a1.add_buddy(), a2.add_buddy()
        while a1.units and a2.units:
            if fight(a1.units[0], a2.units[0]):
                a2.units.pop(0)
            else:
                a1.units.pop(0)
        return bool(a1.units)


def fight(w1, w2):
    while w1.is_alive and w2.is_alive:
        w1.hit(w2)
        if w2.is_alive:
            w2.hit(w1)
    return w1.is_alive


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
freelancer = Lancer()
vampire = Vampire()
priest = Healer()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False
fight(bob, mike) == False
fight(lancelot, rog) == True
fight(eric, richard) == False
fight(ogre, adam) == True
fight(freelancer, vampire) == True
freelancer.is_alive == True
freelancer.health == 14    
priest.heal(freelancer)
freelancer.health == 16

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Healer, 1)
my_army.add_units(Vampire, 2)
my_army.add_units(Lancer, 2)
my_army.add_units(Healer, 1)
my_army.add_units(Warrior, 1)
    
enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Lancer, 4)
enemy_army.add_units(Healer, 1)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)
enemy_army.add_units(Healer, 1)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Healer, 1)
army_3.add_units(Defender, 2)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 1)
army_4.add_units(Healer, 1)
army_4.add_units(Lancer, 2)

army_5 = Army()
army_5.add_units(Warrior, 10)

army_6 = Army()
army_6.add_units(Warrior, 6)
army_6.add_units(Lancer, 5)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True
battle.straight_fight(army_5, army_6) == False