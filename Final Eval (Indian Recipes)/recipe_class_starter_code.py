
class Recipe:

    def __init__(self, id_no, name, ingredients, prep_time, cook_time, total_time, servings, cuisine, course, diet, instructions, URL):
        self._id = id_no
        self._name = name
        self._ingredients = ingredients
        self._preptime = prep_time
        self._cooktime = cook_time
        self._totaltime = total_time
        self._servings = servings
        self._cuisine = cuisine
        self._course = course
        self._diet = diet
        self._instructions = instructions
        self._url = URL
    
    def ID(self):
        return self._id
    
    def name(self):
        return self._name
    
    def ingredients(self):
        return self._ingredients

    def preptime(self):
        return self._preptime
    
    def cooktime(self):
        return self._cooktime

    def totaltime(self):
        return self._totaltime
    
    def servings(self):
        return self._servings
    
    def cuisine(self):
        return self._cuisine
    
    def course(self):
        return self._course
    
    def diet(self):
        return self._diet

    def instructions(self):
        return self._instructions
    
    def URL(self):
        return self._url
    
    def __str__(self):
        return f'({self._id}, {self._name}, {self._ingredients}, {self._preptime}, {self._cooktime}, {self._totaltime}, {self._servings}, {self._cuisine}, {self._course}, {self._diet}, {self._instructions}, {self._url})'
    
    def __repr__(self):
        return f'Recipe(id={self._id}, name={self._name}, ingredients={self._ingredients}, preptime={self._preptime}, cooktime={self._cooktime}, totaltime={self._totaltime}, servings={self._servings}, cuisine={self._cuisine}, course={self._course}, diet={self._diet}, instructions={self._instructions}, url={self._url})'

    def __lt__(self, other):
        return self._totaltime < other.totaltime()
    
    def __le__(self, other):
        return self._totaltime <= other.totaltime()
    
    def __gt__(self, other):
        return self._totaltime > other.totaltime()
    
    def __ge__(self, other):
        return self._totaltime >= other.totaltime()

    def __eq__(self, other):
        return self._totaltime == other.totaltime()
    
    def __ne__(self, other):
        return self._totaltime != other.totaltime()