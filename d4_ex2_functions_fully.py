# dar înainte de toate:
from functools import partial

print = partial(print, sep=": ")

# acum putem trece la treabă:
# argumente poziționale
def myfunc(arg1, arg2):
    print("» arg1", arg1)
    print("» arg2", arg2)

myfunc(1, 2)


# argumente poziționale cu "catch-all"
# (positional argument packing)
def myfunc(arg1, arg2, *args):
    print("» arg1", arg1)
    print("» arg2", arg2)
    print("» args", args) # [!!] o tuplă

myfunc(1, 2, 3, 4, 5)
# 3, 4, 5 --> intră în tupla args


# keyword arguments
# (argumente cu valoare default)
def myfunc(arg1, arg2, *args, kw1="un default", kw2="alt default"):
    print("» arg1", arg1)
    print("» arg2", arg2)
    print("» args", args)
    print("» kw1", kw1)
    print("» kw2", kw2)

myfunc(1, 2, 3, 4) # toate poziționalele sunt deja capturate
myfunc(1, 2, 3, 4, kw2="aha!")


# acceptăm _orice_ keyword argument
# (keyword argument packing)
def myfunc(arg1, arg2, *args, kw1="un default", kw2="alt default", **kwargs):
    print("» arg1", arg1)
    print("» arg2", arg2)
    print("» args", args)
    print("» kw1", kw1)
    print("» kw2", kw2)
    print("» kwargs", kwargs) # [!!] un dicționar


# capitolul 2: din partea cealaltă
# chemarea funcțiilor

print = partial(print, sep='  ..  ')

def myfunc(a, b):
    print(a, b)
# putem să chemăm funcția
myfunc(1, 2) # și cu args poziționale
myfunc(b=2, a=1) # și cu kwargs

def myfunc(a, b, c=None):
    print(a, b, c)

myfunc(1, 2, 3) # kwarg pasat ca pozițional
myfunc(1, 2, c=3) # sau explicit
myfunc(a=1, b=2, c=3) # sau toate explicite


def myfunc(a, b, c):
    print(a, b, c)

lst = ["ala", "bala", "porto"]

# în loc de:
myfunc(lst[0], lst[1], lst[2])
# putem face positional argument unpacking:
myfunc(*lst) # demontează orice iterabil


# și în loc de
myfunc(a="ceva", b="altceva", c="aha aha")
# putem face
d = {
    "a": "ceva",
    "b": "altceva",
    "c": "aha aha",
}
myfunc(**d) # keyword argument unpacking



# capitolul final. extra, cireașă pe tort:
# a forța unele argumente ca poziționale
# sau ca keyword

# să luăm exemplul lui `sorted()` din standard library:
# care are semnătura
def sorted(iterable, /, *, key=None, reverse=False):
    pass

def sorted(iterable, key=None, reverse=False):
    pass
sorted(1, 2, 3) # merge
sorted(iterable=1) # merge

# simbolul /
# spune că argumentele dinaintea sa sunt obligatoriu
# poziționale:

def sorted(iterable, /, key=None, reverse=False):
    pass

sorted(1, 2) # merge

try:
    sorted(iterable=1)
except TypeError:
    print("ridică TypeError")


# simbolul *
# spune că argumentele după el sunt obligatoriu
# keywords:
def sorted(iterable, *, key=None, reverse=False):
    pass

sorted(iterable=1) # merge
try:
    sorted(1, 2)
except TypeError:
    print("ridică TypeError")

# și combinate
def sorted(iterable, /, *, key=None, reverse=False):
    pass

sorted(1, key=2) # doar așa merge
