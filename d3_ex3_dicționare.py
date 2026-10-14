d1 = {
    "cheie": "valoare",
    "altă cheie": "altă valoare",
}

# unde cheia poate să fie aproape orice
# iar valoare poate să fie orice

# accesul se face cu sintaxa de item access:
d1['cheie']
# asignarea se face tot cu sintaxa de item access
d1['cheie'] = "overwrite you!"
# nu contează dacă rescriu o cheie existentă
# sau creez una nouă:
d1['xx cheie'] = "ceva nou"


# tot ce se evaluează pe partea de cheie sau valoare
# este python standard

x = "something"

d2 = {
    1 + 2: x
}
print(d2[3])

# obiectele care NU pot fi folosite drept cheie:
list, dict, set

d = {
  "k1": "v1",
  "k2": "v2",
  "k3": "v3",
}
# 1. dicționarul este iterabil:
for elem in d:
    print(elem) # cheia

# 2. suportă operatorul `in`:
"k1" in d
"k15" in d

# 3. metode de iterare specifice
d.keys()
d.values()
d.items()

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for item in d.items():
    print(item)
for k, v in d.items():
    print(k, v)

# dată fiind structura de date
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
# creați un dicționar cu cheia numele orașului
# și valoarea distanța

# creăm un dicționar gol
d = {}
# adăugăm în el element cu element
for name, distance in cities:
    d[name] = distance

# dată fiind structura de date cities
# creați o structură de date nouă:
# o listă al cărei fiecare element este un dicționar
# de forma {"name": numele, "distance": distanța}

cities_as_dicts = []
for name, distance in cities:
    cities_as_dicts.append({
        "name": name,
        "distance": distance,
    })
# și cu list comprehension?
[
    {
        "name": name,
        "distance": distance,
    }
    for name, distance in cities
]

# 4. felurile posibile de a inițializa un dicționar
# a) chei, valori explicit inline:
{"k1": "v1", 'k2': 'v2'}

# b) cu argumente la dict()
dict(k1="v1", k2="v2")
# echivalent cu exemplul de mai sus,
# dar fiind sintaxă de chemare de funcție
# sunt limitat la chei string

# c) inițializare dintr-un obiect iterabil bi-dimensional
#    al cărui fiecare element are două elemente
l = [
    ['ala', 'bala'],
    ['bla', 'blu'],
]
dict(l)
# echivalent cu:
d = {}
for k, v in l:
    d[k] = v

dict(cities)

# d) dictionary comprehension
{
    k: v
    for k, v in cities
}

# e) folosind classmethod-ul
dict.fromkeys

iterabil = range(10, 15)
dict.fromkeys(iterabil)

# divagare:
# am mai întâlnit classmethods?
import datetime
datetime.datetime.now()
datetime.date.today()
dict.fromkeys(iterabil)
# toate au un lucru în comun:
# sunt "factory methods"
#       --> generează un obiect specific, instanță a acelei clase


# Exercițiu:
# presupunem că avem structura cu elemente de forma
# (name, distance, population, altitude)

xcities = [
    ('Cluj-Napoca', 450, 212874, 799),
    ('Timișoara', 550, 228582, 925),
    ('Iași', 390, 261834, 316),
    ('Constanța', 225, 185102, 463),
    ('Brașov', 180, 298251, 758),
    ('Craiova', 230, 104457, 1064),
    ('Galați', 250, 339711, 567),
    ('Ploiești', 60, 237330, 450),
    ('Oradea', 610, 379704, 654),
    ('Sibiu', 275, 238659, 962),
    ('Arad', 560, 235125, 1010),
    ('Bacău', 300, 116213, 221),
    ('Brăila', 200, 162187, 985),
    ('Buzău', 110, 355484, 696),
    ('Suceava', 450, 391470, 695),
    ('Pitești', 120, 130246, 908),
    ('Târgu Mureș', 330, 376434, 516),
    ('Baia Mare', 600, 196689, 1084)
]

# vrem să generăm o listă de dicționare cu cheile
# "name", "distance", "population", "altitude"

columns = "name", "distance", "population", "altitude"

[
    dict(zip(columns, elem))
    for elem in cities
]


# 5. celelelalte metode ale unui dicționar
d = {
  "k1": "v1",
  "k2": "v2",
  "k3": "v3",
}

d.pop("k1") # primește argument cheia
d.popitem() # scoate (cheie, valoare) din dicționar
d.get("k1") # acces după cheie, fără KeyError, returnează un default:
d.get("k1", "v. default") #
d.setdefault("k1", "ceva") # nu setează, returnează "v1"
d.setdefault("k15", "ceva") # setează și returnează "ceva"
d.update({
    'k1': 'valoare nouă',
    'k15': 'altă valoare nouă'
})          # updatează in-place pe d cu cheile/valorile din argumentul primit


# Exercițiu: dată fiind lista
lst = [
    "bla",
    "bli"
    "blu",
    "bla",
    "blu",
    "bli",
    "bla",
]
# aflați de câte ori apare fiecare element în listă
# ce structură de date ați folosi pentru a stoca
# numărul de apariții al fiecărui element?

d = {
    "bla": 3,
    "bli": 2,
    "blu": 2,
}

for elem in lst:
    number = lst.count(elem) # O(n^2)


counts = dict.fromkeys(lst, 0) # a făcut deja o iterație
for elem in lst:               # am mai făcut o iterație
    counts[elem] += 1
# rezultă: O(2 * n)

counts = {}
for elem in lst:             # O(n)
    if elem not in counts:
        # inițializăm
        counts[elem] = 1
    else:
        # incrementăm
        counts[elem] += 1

# rescris cu try / except
counts = {}
for elem in lst:
    try:
        value = counts[elem]
    except KeyError:
        value = 0

    counts[elem] = value + 1

# rescris cu .get()
counts = {}
for elem in lst:
    value = counts.get(elem, 0)
    counts[elem] = value + 1

# rescris cu .setdefault()
counts = {}
for elem in lst:
    counts.setdefault(elem, 0)
    counts[elem] += 1

# pentru pattern-ul acesta, când vrem să avem
# - și acces după cheie
# - și valoare default când nu există
from collections import defaultdict

# defaultdict creează! cheia/valoarea când nu există
def myfunc():
    return 0

counts = defaultdict(myfunc)
for elem in lst:
    counts[elem] += 1

# sau
counts = defaultdict(lambda: 0)
# sau
counts = defaultdict(int)







# TODO:
# să iterăm printr-un dicționar în timp ce consumăm
# toate elementele sale