class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.north = south + width_NS
        self.east = west + width_WE
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        result = {}
        result['north-west'] = [self.north, self.west]
        result['north-east'] = [self.north, self.east]
        result['south-west'] = [self.south, self.west]
        result['south-east'] = [self.south, self.east]
        return result

    def area(self):
        return (self.east - self.west) * (self.north - self.south)

    def volume(self):
        return (self.east - self.west) * (self.north - self.south) * self.height

    def __repr__(self):
        return f'Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
