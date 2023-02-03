class Capital:

    __instance = None
    city_name = ''

    def __new__(cls, city_name):
        if cls.__instance is None:
            cls.city_name = city_name
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def name(cls):
        return cls.city_name


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
