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

    def straight_fight(self, a1, a2):
        while a1.units and a2.units:
            for w1, w2 in zip(a1.units, a2.units):
                fight(w1, w2)
            a1.units = [u for u in a1.units if u.is_alive]
            a2.units = [u for u in a2.units if u.is_alive]
        return bool(a1.units)


def fight(w1, w2):
    while w1.is_alive and w2.is_alive:
        w1.hit(w2)
        if w2.is_alive:
            w2.hit(w1)
    return w1.is_alive


ogre = Warrior()
lancelot = Knight()
richard = Defender()
eric = Vampire()
freelancer = Lancer()
priest = Healer()

sword = Sword()
shield = Shield()
axe = GreatAxe()
katana = Katana()
wand = MagicWand()
super_weapon = Weapon(50, 10, 5, 150, 8)

ogre.equip_weapon(sword)
ogre.equip_weapon(shield)
ogre.equip_weapon(super_weapon)
lancelot.equip_weapon(super_weapon)
richard.equip_weapon(shield)
eric.equip_weapon(super_weapon)
freelancer.equip_weapon(axe)
freelancer.equip_weapon(katana)
priest.equip_weapon(wand)
priest.equip_weapon(shield)

ogre.health == 125
lancelot.attack == 17
richard.defense == 4
eric.vampirism == 200
freelancer.health == 15
priest.heal_power == 5

fight(ogre, eric) == False
fight(priest, richard) == False
fight(lancelot, freelancer) == True

my_army = Army()
my_army.add_units(Knight, 1)
my_army.add_units(Lancer, 1)

enemy_army = Army()
enemy_army.add_units(Vampire, 1)
enemy_army.add_units(Healer, 1)

my_army.units[0].equip_weapon(axe)
my_army.units[1].equip_weapon(super_weapon)

enemy_army.units[0].equip_weapon(katana)
enemy_army.units[1].equip_weapon(wand)

battle = Battle()

battle.fight(my_army, enemy_army) == True