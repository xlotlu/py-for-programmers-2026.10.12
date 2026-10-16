# A. formele de import:
# 1. "import module"
import os

os.path # submodule
os.path.join # simbol în interiorul modulului

# 2. "from module import symbol"
from os import path


#B: variațiunile:

# aliasuri:
import os as myos
from os import path as mypath
from os.path import join as pathjoin

mypath is os.path is path # totul pointează în același loc

# import multiplu:
from os.path import (
    join as pathjoin,
    abspath,
    dirname,
)

# o formă interesantă de import:
import os.path # fully qualified namespace

# import toate simbolurile:
from os.path import *
# (generally frowned-upon, because namespace pollution)


# C. let's talk modules and packages

# 1) un modul este un fișier python:
import mymodule
print(mymodule.MY_VAR)

# 2) un "package" este un director.
#    și este și el de fapt tot modul.
import mypackage

print(mypackage.PACKAGE_VAR)

try:
    mypackage.submodule
except AttributeError:
    print("» NU există", 'mypackage.submodule')
else:
    print("»    există", 'mypackage.submodule')

from mypackage import submodule # merge
print(submodule.SUB_VAR)

# acesta merge doar pentru că în __init__.py
# s-a făcut import functie_importanta
from mypackage import functie_importanta
functie_importanta()

# vs. varianta fully qualified
from mypackage.submodule import functie_importanta as funimp
funimp()

print(funimp is functie_importanta)


# un package fiind un director nu are "corp"
# de logică.
#
# decât dacă creăm fișierul special `__init__.py`
# care reprezintă codul pachetului
