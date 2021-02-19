import math


class Sun:

    def __init__(self, name, r, m, temp):
        self._name = ''
        self._radius = r
        self._mass = m
        self._temperature = temp

    def name(self):
        return self._name

    def radius(self):
        return self._radius

    def temperature(self):
        return self._temperature

    def volume(self):
        return (4/3) * math.pi * (self._radius ** 3)

    def surface_area(self):
        return 4 * math.pi * (self._radius ** 2)

    def change_name(self, new):
        self._name = new

    def change_radius(self, new):
        self._radius = new

    
        
