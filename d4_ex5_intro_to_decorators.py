# un decorator este o funcție
# ce primește ca argument o funcție
# și returnează o altă funcție

# un decorator super-util
from functools import cache

@cache
def myfunc():
    print("mă rulez")
myfunc()
myfunc()

from random import randint

@cache
def myfunc():
    return randint(1, 15)
myfunc()
myfunc()

# ce se întâmplă în spate?

# dacă am defini:
def myfunc():
    return randint(1, 15)

# și apoi rulăm funcția cache:
my_deco_func = cache(myfunc)
# acum my_deco_func este funcția noastră inițială
# "decorată" de către cache()
my_deco_func()
my_deco_func()

# iar sintaxa
@cache
def myfunc():
    pass

# este echivalentă cu:
def myfunc():
    pass
myfunc = cache(myfunc) # <--- aici este sosul secret


def doubleit(func):
    def _inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return _inner

@doubleit
def myfunc(x, y):
    return x * y