# Essentials:

Python este interpretat
Python este whitespace-sensitive

în Python _totul_ este un obiect

în Python totul este o referință

Python is self-documenting
(scriem un string ca primul lucru în definiție)

în Python fiecare operator este implementat
drept o metodă pe obiect


# You should read these:

The Styleguide:
https://peps.python.org/pep-0008/

String formatting examples:
https://docs.python.org/3/library/string.html#format-examples

Date formatting (strptime, strftime):
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# Concepte:

reprezentare

iterable: something that can be iterated (folosit în for)

"duck typing": If it walks like a duck and quacks like a duck, it's good enough for me.

iterator = un iterabil special, ce are cod în spate ce se execută
           și își suspendă execuția după ce returnează fiecare element


în Python excepțiile sunt folosite pentru flow control!

# Basic data-types

int
float
str

list   # mutable
tuple  # immutable

dict   # mutable

set    # mutable
frozenset # immutable


## sequences:

list, tuple and str:

- they are iterable
- they have a length -- suportă funcția len
- suportă operatorul `in`
- sunt accesibile după index
- și slice-uibile
- au metodele .count() și .index()


# Operatori

comportamenul operatorilor
este dependent
de data type-ul pe care se aplică!


## operatori noi:

** ridicare la putere
// partea întreagă a împărțirii
%  restul împărțirii

in # elem in collection


# operatori in-place
(de ținut minte, se pot comporta diferit dacă obiectul este mutable sau nu,
adică pt. obiecte immutable creează un obiect nou, altfel îl modifică pe cel existent)

-=
+=
*=
/=


## operatori boolean:

```
==
!=

>
<
>=
<=

and
or
not

in
```

# Debugging essentials

print()
help()
type() # returnează clasa din care a fost instanțiat obiectul

TODO: hands-on debugging


# Important Exceptions:

NameError   : simbolul nu este declarat

TypeError   : la diverse operațiuni, când există data type mismatch
ValueError  : valoare nepotrivită (for whatever that means, context-dependent)
IndexError  : când nu există indexul respectiv
KeyError    : când nu există cheia respectivă


# Pachete utile:

pip install ipython
pip install rich


# Working with VSCode

Ctrl+F5      run file
Ctrl+/       comment selection
Shift+Enter  run selection
Tab          indent selection
Shift+Tab    unindent selection


pentru a folosi ipython ca terminalul default de python,
adăugați în settings.json

Ctrl+Shift+p --> Open settings.json

```
    "python.terminal.launchArgs": [
        "-m", "IPython", "--no-autoindent"
    ],
```

sau, pentru a păstra autoindent,
dar nu va mai merge Shift+Enter

```
    "python.terminal.launchArgs": [
        "-m", "IPython"
    ],
```


# Working with ipython

useful stuff:

dacă am instalat rich:

```
%load_ext rich
```


# Diverse

părerea lui Ionuț despre metricele cele mai importante
pentru cod de calitate:

1. readability
   adică: whitespace, variable & function names

quoting Linus Torvalds: "code is written once, read many times"

2. eleganță
   arhitectural să fie coerent, logic, iar dacă este complex
   să nu fie complicat

3. performanță


There are 2 most difficult problems in computing:
- naming things
- cache invalidation
- off-by-one errors

"Validation"
https://www.youtube.com/watch?v=Cbk980jV7Ao
