import random as r

class Die:
    def __init__(self, sides):
        self._sides = sides

    def sides(self):
        return self._sides

    def roll(self):
        return r.randint(1, self._sides)

    def __str__(self):
        return self._sides

    def __repr__(self):
        return self._sides

    def __eq__(self, other):
        return self._sides == other.sides()

    def __lt__(self, other):
        return self._sides < other.sides()

    def __gt__(self, other):
        return self._sides > other.sides()
        
