
class Colour:

    def __init__(self, r, g, b):
        self._red = self.check255(r)
        self._green = self.check255(g)
        self._blue = self.check255(b)


    def check255(self, num):
        if num < 0:
            return 0
        elif num > 255:
            return 255
        else:
            return num

            
    def check1(self, num):
        if num < 0:
            return 0
        elif num > 1:
            return 1
        else:
            return num

    def red(self):
        self._red = self.check255(self._red)
        return self._red

    def green(self):
        self._green = self.check255(self._green)
        return self._green

    def blue(self):
        self._blue = self.check255(self._blue)
        return self._blue


    def __str__(self):
        return f'({self._red}, {self._green}, {self._blue})'

    def __repr__(self):
        return f'Colour(r = {self._red}, g = {self._green}, b = {self._blue})'


    def __add__(self, other):
        redSum = self.check255(self._red + other.red())
        greenSum = self.check255(self._green + other.green())
        blueSum = self.check255(self._blue + other.blue())
        
        return Colour(redSum, greenSum, blueSum)


    def __sub__(self, other):
        redDiff = self.check255(self._red - other.red())
        greenDiff = self.check255(self._green - other.green())
        blueDiff = self.check255(self._blue - other.blue())

        return Colour(redDiff, greenDiff, blueDiff)


    def __eq__(self, other):
        return self._red == other.red() and self._green == other.green() and self._blue == other.blue()


    def hex(self):
        return f'#{self._red:02x}{self._green:02x}{self._blue:02x}'.upper()

    def luminosity(self):
        lumin = 0.5 * ((max(self._red, self._green, self._blue) / 255) + (min(self._red, self._green, self._blue) / 255))
        
        lumin = float(self.check1(lumin))
        
        return lumin

    def saturation(self):
        maxVal = max(self._red, self._green, self._blue)
        minVal = min(self._red, self._green, self._blue)

        if maxVal == minVal:
            satur = 0
        elif self.luminosity() <= 0.5:
            satur = ((maxVal/255) - (minVal/255)) / ((maxVal/255) + (minVal/255)) 
        elif self.luminosity() > 0.5:
            satur = ((maxVal/255) - (minVal/255)) / (2 - (maxVal/255) - (minVal/255))

        satur = float(self.check1(satur))
        
        return satur


    def __lt__(self, other):
        return self.saturation() < other.saturation()

    def __gt__(self, other):
        return self.saturation() > other.saturation()

    def __le__(self, other):
        return self.saturation() <= other.saturation()

    def __ge__(self, other):
        return self.saturation() >= other.saturation()

c = Colour(255, 255, 250)
c2 = Colour(0, 0, 0)
print(c.red())
print(c.green())
print(c.blue())
print(c)
print(c2)
l = [c, c2]
print(l)
print(c+c)
print(c+c2)
print(c-c)
print(c-c2)
print(c==c)
print(c==c2)
print()
print(c.hex())
print(c.luminosity())
print(c.saturation())
print(c2.hex())
print(c2.luminosity())
print(c2.saturation())
print()
print(c < c2)
print(c > c2)
print(c <= c2)
print(c >= c2)