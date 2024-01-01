class Car:

    wheels = 'four'
    doors = 4
    working_engine = False

    def __init__(self, brand='', model=''):

        self.brand = brand
        self.model = model

    def start_engine(self):

        self.working_engine = True
        print('Engine has started')

    def stop_engine(self):

        self.working_engine = False
        print('Engine has stopped')


class ElectricCar(Car):

    def __init__(self, battery_capacity, brand='', model=''):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def start_engine(self):

        self.working_engine = True
        print('Electric motor has started')

    def stop_engine(self):

        self.working_engine = False
        print('Electric motor has stopped')


my_car = Car()
some_car1 = Car('Ford', 'Mustang')
some_car2 = Car(model='Camaro')

some_car1.start_engine()
some_car2.start_engine()

my_electric_car = ElectricCar(100, brand='Tesla', model='Model 3')

my_electric_car.start_engine()

my_electric_car2 = ElectricCar(60, 'Toyota', 'Prius')

my_electric_car2.start_engine()
my_electric_car2.stop_engine()
