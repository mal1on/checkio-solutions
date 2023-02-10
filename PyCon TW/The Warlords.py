from math import floor


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0
        self.heal_power = 0
        self.buddy = None
        self.max_health = self.health

    def hit(self, enemy):
        dmg = max(0, self.attack - enemy.defense)
        enemy.health -= dmg
        self.health += floor(self.vampirism * dmg)
        if self.buddy and isinstance(self.buddy, Healer):
            self.buddy.heal(self)

    def equip_weapon(self, weapon):
        for k, v in vars(self).items():
            if k in vars(weapon) and v:
                vars(self)[k] = max(0, vars(self)[k] + vars(weapon)[k])
        self.max_health += weapon.health

    @property
    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f'{self.__class__.__name__} with {self.health}/{self.max_health} health'


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = self.max_health = 60
        self.attack = 3
        self.defense = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = self.max_health = 40
        self.attack = 4
        self.vampirism = 0.5


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6

    def hit(self, enemy):
        dmg = max(0, self.attack - enemy.defense)
        half_dmg = max(0, self.attack / 2 - enemy.defense)
        enemy.health -= dmg
        if enemy.buddy:
            enemy.buddy.health -= half_dmg
        if self.buddy and isinstance(self.buddy, Healer):
            self.buddy.heal(self)


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = self.max_health = 60
        self.attack = 0
        self.heal_power = 2

    def heal(self, unit):
        unit.health = min(unit.max_health, unit.health + self.heal_power)


class Warlord(Warrior):
    def __init__(self):
        super().__init__()
        self.health = self.max_health = 100
        self.attack = 4
        self.defense = 2


class Army:
    def __init__(self):
        self.units = []
        self.warlord = None

    def add_units(self, unit, num):
        if isinstance(unit(), Warlord):
            num = 0
            if not self.warlord:
                self.warlord = unit()
                self.units.append(self.warlord)

        [self.units.append(unit()) for _ in range(num)]


    def add_buddy(self):
        for unit, buddy in zip(self.units[:-1], self.units[1:]):
            unit.buddy = buddy

    def move_units(self):
        if self.warlord:
            lancers = []
            healers = []
            soldiers = []

            for unit in self.units:
                if isinstance(unit, Lancer):
                    lancers.append(unit)
                elif isinstance(unit, Healer):
                    healers.append(unit)
                elif not isinstance(unit, Warlord):
                    soldiers.append(unit)            

            if lancers:
                self.units = [lancers[0]] + healers + lancers[1:] + soldiers + [self.warlord]
            elif soldiers:
                self.units = [soldiers[0]] + healers + soldiers[1:] + [self.warlord]

        else:
            pass            


class Battle:
    def fight(self, a1, a2):
        a1.add_buddy(), a2.add_buddy()
        a1.move_units(), a2.move_units()
        while a1.units and a2.units:
            if fight(a1.units[0], a2.units[0]):
                a2.units.pop(0)
                a2.move_units()
            else:
                a1.units.pop(0)
                a1.move_units()
        return bool(a1.units)

    def straight_fight(self, a1, a2):
        while a1.units and a2.units:
            for w1, w2 in zip(a1.units, a2.units):
                fight(w1, w2)
            a1.units = [u for u in a1.units if u.is_alive]
            a2.units = [u for u in a2.units if u.is_alive]
        return bool(a1.units)


class Weapon:
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        vars(self).update(locals())
        self.vampirism = vampirism / 100 if vampirism else 0


class Sword(Weapon):
    def __init__(self):
        super().__init__(health=5, attack=2)


class Shield(Weapon):
    def __init__(self):
        super().__init__(health=20, attack=-1, defense=2)


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(health=-15, attack=5, defense=-2, vampirism=0.1)


class Katana(Weapon):
    def __init__(self):
        super().__init__(health=-20, attack=6, defense=-5, vampirism=0.5)


class MagicWand(Weapon):
    def __init__(self):
        super().__init__(health=30, attack=3, heal_power=3)


def fight(w1, w2):
    while w1.is_alive and w2.is_alive:
        w1.hit(w2)
        if w2.is_alive:
            w2.hit(w1)
    return w1.is_alive


ronald = Warlord()
heimdall = Knight()

fight(heimdall, ronald) == False

my_army = Army()
my_army.add_units(Warlord, 1)
my_army.add_units(Warrior, 2)
my_army.add_units(Lancer, 2)
my_army.add_units(Healer, 2)

enemy_army = Army()
enemy_army.add_units(Warlord, 3)
enemy_army.add_units(Vampire, 1)
enemy_army.add_units(Healer, 2)
enemy_army.add_units(Knight, 2)

my_army.move_units()
enemy_army.move_units()

type(my_army.units[0]) == Lancer
type(my_army.units[1]) == Healer
type(my_army.units[-1]) == Warlord

type(enemy_army.units[0]) == Vampire
type(enemy_army.units[-1]) == Warlord
type(enemy_army.units[-2]) == Knight

# 6, not 8, because only 1 Warlord per army could be
len(enemy_army.units) == 6

battle = Battle()

print(battle.fight(my_army, enemy_army)) == True