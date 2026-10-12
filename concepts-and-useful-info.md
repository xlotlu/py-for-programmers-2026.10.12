# Essentials:

Python este interpretat
Python este whitespace-sensitive

în Python _totul_ este un obiect

în Python totul este o referință


# Concepte:

reprezentare

iterable: something that can be iterated (folosit în for)


# Basic data-types

int
float
str

list   # mutable
tuple  # immutable

## sequences:

list, tuple and str:

- they are iterable
- they have a length -- suportă funcția len
- suportă operatorul `in`
- sunt accesibile după index


# Operatori

comportamenul operatorilor
este dependent
de data type-ul pe care se aplică!


## operatori noi:

** ridicare la putere
// partea întreagă a împărțirii
%  restul împărțirii

in # elem in collection


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


# Important Exceptions:

TypeError   : la diverse operațiuni, când există data type mismatch
ValueError  : valoare nepotrivită (for whatever that means, context-dependent)
IndexError  : când nu există indexul respectiv


# Pachete utile:

pip install ipython


# Working with VSCode

Ctrl+F5      run file
Ctrl+/       comment selection
Shift+Enter  run selection
Tab          indent selection
Shift+Tab    unindent selection


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
