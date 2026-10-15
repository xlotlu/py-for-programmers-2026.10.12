# în Python toate obiectele sunt derivate dintr-o clasă

class NumeleClasei:
    pass

NumeleClasei()
# ^^ acesta este un obiect, instanță a lui NumeleClasei


class NumeleClasei:
    # orice metodă a clasei primește automat
    # ca prim argument obiectul curent:
    def metoda_mea(self, value):
        print("eu sunt", self)
        print("am primit", value)

        self.value = value

obj = NumeleClasei()
obj.metoda_mea(5)


class NumeleClasei:
    # funcția, adică metoda __init__
    # dă semnătura clasei
    def __init__(self):
        # toate metodele primesc automat ca argument
        # instanța curentă
        print("» în clasă", self)

obj = NumeleClasei()
# devine evident că self din __init__ este chiar acest obj
print(obj)


# detaliu de implementare:
# în Python toate clasele moștenesc de la clasa `object`

# deci următoarele sunt perfect echivalente:
class MahCls:
    pass

class MahCls():
    pass

class MahCls(object):
    pass



class Point:
    # __init__ dă semnătura clasei
    def __init__(self, x, y):
        # atașăm x și y ca atribute la self
        self.x = x
        self.y = y

p = Point(2, 5)
print(p.x, p.y)

# haideți să facem pe Point() să arate frumos
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # reprezentarea default este ceva de genul
    def __repr__(self):
        return f'<{__name__}.{self.__class__.__name__} pe la {hex(id(self))}>'

    # override la __repr__ să arate frumos:
    def __repr__(self):
        return f'Point({self.x}, {self.y})'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y


from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    @property # transformă o metodă în atribut (aparent)
    def distance_from_origin(self):
        return sqrt(
            self.x ** 2 + self.y ** 2
        )

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __mul__(self, value):
        return Point(self.x * 2, self.y * 2)

    def __imul__(self, value):
        self.x *= 2
        self.y *= 2

        return self
