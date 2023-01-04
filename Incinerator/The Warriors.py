class Warrior:

    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        self.health = health
        self.attack = attack
        self.is_alive = True


def fight(first, second):

    while first.is_alive and second.is_alive:
        second.health -= first.attack
        if second.health < 1:
            second.is_alive = False
            break
        first.health -= second.attack
        if first.health < 1:
            first.is_alive = False
            break

    return first.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
