# Exercițiu
# scrieți un decorator
def timeit(func):
    pass
# care face print cu durata de execuție
# a funcțiilor pe care le decorează,
# fără să le altereze procesul normal de execuție
# sau return value.


# plecați de le acest template:

def deco(func):
    print("» decorez funcția")

    def _inner(*args, **kwargs):
        # aici fac ceva înainte de execuția
        # funcției obișnuite
        print("- sunt în funcția decorată")

        # "non-local variable"
        result = func(*args, **kwargs)

        # aici fac ceva după execuția
        # funcției obișnuite
        print("- ies din funcția decorată")
        return result

    print("» am decorat funcția")
    return _inner

@deco
def myfunc(x, y):
    print("-- sunt în funcție")
    return "some value"
# ^^ decoratorul face exact același lucru cu:
# myfunc = deco(myfunc)


import sys
import time

def timeit(func):
    def _inner(*args, **kwargs):
        first_time = time.perf_counter()
        result = func(*args, **kwargs)
        last_time = time.perf_counter()

        delta = last_time - first_time

        print(
            f"» {func.__name__} :: {delta * 1000:.04f}ms",
            file=sys.stderr
        )

        return result
    return _inner

import random

@timeit
def sleepy():
    time.sleep(random.randint(1, 10) / 10)
    return "o valoare"

# TODO: ar fi drăguț un output de genul...
'» mymodule.sleepy("valoare", kwarg="altă valoare") :: 1000.0862ms --> "return value"'



# acest decorator este pretty crazy:
from functools import lru_cache

from random import randint

@lru_cache(maxsize=3)
def myfunc(x, y):
    return randint(x, y)

# pentru că mai sus face de fapt:
myfunc = lru_cache(maxsize=3)(myfunc)
# deci în realitate:
_deco = lru_cache(maxsize=3)
#       ^^ funcție ce returnează funcție decorator
myfunc = _deco(myfunc)


# and if that's not crazy enough,
# this works too:
@lru_cache    # <-- și va avea default maxsize=128
def myfunc(x, y):
    return randint(x, y)
