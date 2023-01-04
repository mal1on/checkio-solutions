class Capital:

    city_name = None

    def __init__(self, city_name):
        if Capital.city_name is None:
            Capital.city_name = city_name

    def name(self):
        return self.city_name


test = Capital('Sofia')
print(test.name())
test2 = Capital('Zagreb')
print(test2.name())                