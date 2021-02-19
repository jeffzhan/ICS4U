import math

class Planet:
  

    def __init__(self, name, t, orbit, num_moons, r):
        self._name = name
        self._type = t
        self._orbit_days = orbit
        self._num_moons = num_moons
        self._moon_list = []
        self._radius = r

    def name(self):
        return self._name

    def change_type(self, new):
        self._type = new

    def orbit_day(self):
        return self._orbit_days

    def change_orbit_day(self, new):
        self._orbit_days = new

    def num_moons(self):
        return self._num_moons

    def change_number_moons(self, new):
        self._num_moons = new

    def add_moon(self, new):
        self._moon_list.append(new)

    def circumference(self):
        return 2 * math.pi * self._radius
    
