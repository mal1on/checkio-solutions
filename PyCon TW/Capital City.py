class Capital:

    __instance = None
    city_name = ''
    
    def __new__(cls, city_name):
        if cls.__instance is None:
            cls.city_name = city_name
            cls.__instance = super().__new__(cls)
            
        return cls.__instance

    def name(cls):
        print(cls.city_name)    


ukraine_capital_1 = Capital("Kyiv")
ukraine_capital_2 = Capital("London")
ukraine_capital_3 = Capital("Marocco")
ukraine_capital_2.name() == "Kyiv"
ukraine_capital_3.name() == "Kyiv"                        