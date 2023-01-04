class AbstractCook:
    def __init__(self):
        self.order = {'food_bill': 0, 'drinks_bill': 0}

    def add_food(self, amount, price):
        self.order['food_bill'] += amount * price

    def add_drink(self, amount, price):
        self.order['drinks_bill'] += amount * price

    # def total(self):
    #     self.bill = self.order['food_bill'] + self.order['drinks_bill']
    #     return f"Food: {self.order['food_bill']}, Drinks: {self.order['drinks_bill']}, Total: {self.bill}"


class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__()

    def total(self):
        self.bill = self.order['food_bill'] + self.order['drinks_bill']
        return f"Sushi: {self.order['food_bill']}, Tea: {self.order['drinks_bill']}, Total: {self.bill}"


class RussianCook(AbstractCook):
    def __init__(self):
        super().__init__()

    def total(self):
        self.bill = self.order['food_bill'] + self.order['drinks_bill']
        return f"Dumplings: {self.order['food_bill']}, Compote: {self.order['drinks_bill']}, Total: {self.bill}"


class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__()

    def total(self):
        self.bill = self.order['food_bill'] + self.order['drinks_bill']
        return f"Pizza: {self.order['food_bill']}, Juice: {self.order['drinks_bill']}, Total: {self.bill}"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
