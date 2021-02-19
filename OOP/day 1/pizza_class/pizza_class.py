import random as r

class Pizza:

    def __init__(self, status, distance, time, price):
        self._status = status
        self._distance = distance
        self._time = time
        self._price = price

    def change_status(self, new):
        self._status = new

    def change_distance(self, new):
        self._distance = new

    def change_time(self, new):
        self._time = new
        
    def change_price(self, new):
        self._price = new
