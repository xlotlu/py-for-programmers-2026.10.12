# for element in iterable:
#    do_something_with(element)

# în interiorul parantezelor nu avem
# whitespace constraints
lst = [
    1, 2, 3,
    4, 5, 6,
]

tup = (1, 2, 3, 4, 5)

s = "Bună ziua"

for elem in lst:
    print(elem)

for elem in tup:
    print(elem)

for elem in s:
    print(elem)


# Exercițiu:
# dată fiind lista de orașe
cities = [
 'Cluj-Napoca',
 'Timișoara',
 'Iași',
 'Constanța',
 'Brașov',
 'Craiova',
 'Galați',
 'Ploiești',
 'Oradea',
 'Sibiu',
 'Arad',
 'Bacău',
 'Brăila',
 'Buzău',
 'Suceava',
 'Pitești',
 'Târgu Mureș',
 'Baia Mare',
]

# iterați în listă
# și printați elementele care încep cu litera "B"

for elem in cities:
    # if elem.startswith("B"):
    # echivalent cu:
    if elem[0] == "B":
        print(elem)


# dată fiind structura bi-dimensională
cities = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 390),
    ('Constanța', 225),
    ('Brașov', 180),
    ('Craiova', 230),
    ('Galați', 250),
    ('Ploiești', 60),
    ('Oradea', 610),
    ('Sibiu', 275),
    ('Arad', 560),
    ('Bacău', 300),
    ('Brăila', 200),
    ('Buzău', 110),
    ('Suceava', 450),
    ('Pitești', 120),
    ('Târgu Mureș', 330),
    ('Baia Mare', 600),
]
# formată din tuple de forma (name, distance)
# printați elementele cu distanță < 300

# 1. iterăm în listă
# 2. fiecare element este o tuplă cu 2 elemente
# 3. accesăm indexul 1 al tuplei pentru a afla distanța
# 4. filtrăm cu if

for elem in cities:
    if elem[1] < 300:
        print(elem)

# "iterable unpacking":
# (asignăm mai multe variabile deodată)
x, y = [1, 2]
x, y = 1, 2
# echivalent cu
x, y = (1, 2)

# despachetează orice iterabil se află la dreapta egalului
x, y, z = range(10, 13)

from itertools import repeat
a, b, c, d, e, f, g = repeat("wow!", 7)


# rescriem
for elem in cities:
    if elem[1] < 300:
        print(elem)

# cu iterable unpacking
for elem in cities:
    name, distance = elem
    if distance < 300:
        print(name)

# next-level, inline unpacking în for:
for name, distance in cities:
    if distance < 300:
        print(name)


cities = [
    ('Cluj-Napoca', 450, 199990, 1100),
    ('Timișoara', 550, 2000000, 800),
    ('Iași', 390, 1900000, 700),
]
for name, distance, population, altitude in cities:
    print("something")
# vs.
for elem in cities:
    name = elem[0]
    distance = elem[1]
    population = elem[2]
    altitude = elem[3]
    print("something")

# sintaxa completă de iterable unpacking:
name, distance, *the_rest = ('Cluj-Napoca', 450, 199990, 1100)
name, *_, altitude = ('Cluj-Napoca', 450, 199990, 1100)
*_, population, altitude = ('Cluj-Napoca', 450, 199990, 1100)


# Exercițiu:
# scrieți o funcție
def filter_by_distance(cities, distance):
    pass
# ce, primind o structură de date ca `cities` de mai sus
# și un număr, returnează o listă nouă formată din tuplele
# orașelor cu distanța mai mică decât `distance`

for elem in cities:
    if elem[1] < 300:
        print(elem)
        # ^^ aici o să vrem să adăugăm programatic la o listă


def filter_by_distance(cities, distance):
    # pattern de acumulare:
    # 1. ne declarăm obiectul în care acumulăm
    out = []

    # 2. iterăm în sursă
    for elem in cities:
        # 3. filtrăm
        if elem[1] < distance:
        # 4. acumulăm
            out.append(elem)

    # 5. returnăm
    return out

for elem in filter_by_distance(cities, 200):
    print("»", elem)