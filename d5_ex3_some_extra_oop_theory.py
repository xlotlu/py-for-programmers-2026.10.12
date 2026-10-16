# 1. class-level attributes

class MyClass:
    attr = 25 # class-level attribute

    _cache = {}

obj1 = MyClass()
obj2 = MyClass()

MyClass.attr is obj1.attr is obj2.attr

obj1.attr = 35 # se pierde referința
# ^^ este override local obiectului

# (adică o instanță nu are voie să schimbe atributul clasei)
# deci
obj1.attr is not MyClass.attr

MyClass.attr = "schimbat"
# în continuare
obj2.attr is MyClass.attr
obj1.attr is not MyClass.attr


# 2. classmethod și staticmethod

def myfunc(a, b):
    pass

class MyClass:
    def metoda(self):
        print("» instance is:", self)

    @classmethod
    def clsmethod(cls):
        # în loc să primească primul argument instanța,
        # primește clasa (obiectul-clasă)
        print("» class is:", cls)

        # folosit pentru "factory methods":
        return cls() # instanțiat cu ceva

    @staticmethod
    def myfunc(a, b):
        # nu mai primește nici-un prim argument automat
        # este literalmente o funcție
        # pusă în namespace-ul clasei
        print(a, b)


obj = MyClass()
obj.clsmethod()
# și
MyClass.clsmethod()
# fac același lucru

# rescriem clasa Point
# pentru a da sens unui staticmethod

# (și cu alte modificări pentru inheritance)


from math import sqrt

class Vector:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def __repr__(self):
        return f'Vector({self.length}, {self.angle})'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return (self.x, self.y)

    def __repr__(self):
        return f'{self.__class__.__name__}{repr(self.as_tuple())}'

    def __str__(self):
        return str(self.as_tuple())

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.as_tuple() == other.as_tuple()

    @property
    def distance_from_origin(self):
        return self.distance_between(
            self.as_tuple(),
            (0, 0)
        )

    @staticmethod
    def distance_between(coords1, coords2):
        if len(coords1) != len(coords2):
            raise ValueError("Coordinates must be of the same order!")

        x1, y1 = coords1
        x2, y2 = coords2

        return sqrt(
            (x2 - x1) ** 2 + (y2 - y1) ** 2
        )

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        distance = self.distance_between(
            other.as_tuple(),
            self.as_tuple(),
        )

        angle = 55 # conform calculului trigonometric avansat

        return Vector(distance, angle)

    def copy(self):
        return self.__class__(*self.as_tuple())

    def __mul__(self, value):
        return self.__class__(*(
            coord * value
            for coord in self.as_tuple()
        ))

    def __imul__(self, value):
        self.x *= 2
        self.y *= 2

        return self


# 3. inheritance

class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        # vrem să rulăm logica de inițializare a părintelui
        # (fără să dăm copy-paste)
        super().__init__(x, y)

        # pe vremuri făceam
        #Point.__init__(self, x, y)

        # adăugăm logica noastră
        self.z = z

        # super() dă o referință la obiectul curent
        # în contextul clasei părinte

    def as_tuple(self):
        return (self.x, self.y, self.z)

    def translate(self, dx, dy, dz):
        super().translate(dx, dy)
        self.z += dz

class FourDPoint(ThreeDPoint):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self.w = w

    def as_tuple(self):
        return (self.x, self.y, self.z, self.w)
