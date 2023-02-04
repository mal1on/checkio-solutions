from math import pi

class Parameters:

    def __init__(self, p):
        self.p = p

    def choose_figure(self, fig):
        self.fig = fig

    def area(self):
        
        return round(self.fig.area(self.p), 2)

    def perimeter(self):

        return round(self.fig.perimeter(self.p), 2)

    def volume(self):

        return round(self.fig.volume(self.p), 2)


class Circle:

    def area(self, par):

        return pi * par ** 2

    def perimeter(self, par):
        
        return 2 * pi * par

    def volume(self, par):
    
        return 0        


class Triangle:
    
    def area(self, par):

        return par ** 2 * 0.433

    def perimeter(self, par):
        
        return par * 3

    def volume(self, par):
    
        return 0    


class Square:

    def area(self, par):

        return par * par

    def perimeter(self, par):
        
        return par * 4

    def volume(self, par):
    
        return 0

class Pentagon:

    def area(self, par):

        return par ** 2 * 1.72

    def perimeter(self, par):
        
        return par * 5

    def volume(self, par):
    
        return 0

class Hexagon:

    def area(self, par):

        return par ** 2 * 2.598

    def perimeter(self, par):
        
        return par * 6

    def volume(self, par):
    
        return 0

class Cube:

    def area(self, par):

        return 6 * par ** 2

    def perimeter(self, par):
        
        return 12 * par

    def volume(self, par):
    
        return par ** 3




figure = Parameters(10)
    
figure.choose_figure(Circle())
print(figure.area()) == 314.16

figure.choose_figure(Triangle())
print(figure.perimeter()) == 30

figure.choose_figure(Square())
print(figure.area()) == 100

figure.choose_figure(Pentagon())
print(figure.perimeter()) == 50

figure.choose_figure(Hexagon())
print(figure.perimeter()) == 60

figure.choose_figure(Cube())
print(figure.volume()) == 1000