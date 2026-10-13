# dată fiind structura de date
# de forma (nume, vârstă)
candidates = [
    ('Mara', 28),
    ('George', 16),
    ('Dragoș', 42),
    ('Ana', 74),
    ('Mircea', 31),
    ('Carmen', 17),
    ('Andreea', 38),
    ('Vasi', 61),
]
# creați două liste noi
# `accepted` și `rejected`
# astfel încât persoanele cu vârstă între 18 și 60 de ani
# sunt accepted, iar restul rejected.
accepted = []
rejected = []

for candidate in candidates:
    if 18 <= candidate[1] < 60:
        accepted.append(candidate)
    else:
        rejected.append(candidate)


# dată fiind structura de date
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# de forma [name, age, hobbies]

# îmbătrâniți-o pe jane cu an
friends[0][1] += 1
jane = friends[0]
jane[1] += 1

# scrieți o funcție
def get_friend_by_name(friends, name):
    pass
# ce returnează elementul din colecția `friends` primită
# al cărui nume este `name`
def get_friend_by_name(friends, name):
    for friend in friends:
        if friend[0] == name:
            return friend

# scrieți o funcție
def find_friends_by_hobby(friends, hobby):
    pass
# ce returnează o listă nouă cu prietenii cu acel hobby


# scrieți o funcție
def find_friends_by_age(min_age=None, max_age=None):
    pass
# ce returnează o listă nouă cu prietenii cu vârsta cuprinsă
# între `min_age` și `max_age`

def find_friends_by_hobby(friends, hobby):
    "returnează o listă nouă cu prietenii cu acel hobby"
    # ^^ dacă avem un string ce apare ca primul lucru
    #    într-o funcție, clasă sau modul,
    #    acesta se numește "docstring"
    #
    # (și este accesibil drept atributul __doc__)

    out = []
    for friend in friends:
        hobbies = friend[2]
        if hobby in hobbies:
            out.append(friend)

    return out


#find_friends_by_hobby()

# v.1: construim if-uri
def find_friends_by_age(friends, min_age=None, max_age=None):
    lista_noua = []
    for people in friends:
        age = people[1]
        conditie_min = (min_age is None) or (age >= min_age)
        conditie_max = (max_age is None) or (age <= max_age)

        if conditie_max and conditie_min:
            lista_noua.append(people)

    return lista_noua

# v.2: construim anti-if-uri
def find_friends_by_age(friends, min_age=None, max_age=None):
    result = []
    for friend in friends:
        age = friend[1]
        if min_age is not None and age < min_age:
            continue
        if max_age is not None and age > max_age:
            continue

        result.append(friend)

    return result

# toate următoarele utilizări sunt valide:
# 1) min și max ca argumente poziționale
find_friends_by_age(18, 60)

# 2) doar min ca argument pozițional
find_friends_by_age(18)
# echivalent cu keyword argument:
find_friends_by_age(min_age=18)

# 3) doar max, ca keyword argument
find_friends_by_age(max_age=60)



### list comprehension ###

hobby = "hiking"
[
    friend
    for friend in friends
    if hobby in friend[2]
]

def find_friends_by_hobby(friends, hobby):
    "returnează o listă nouă cu prietenii cu acel hobby"
    return [
        friend
        for friend in friends
        if hobby in friend[2]
    ]

# introducem filter(func, iterable):

def filter_by_hiking(elem):
    return "hiking" in elem[2]

for elem in filter(filter_by_hiking, friends):
    print(elem)

# filter() returnează un iterator

[
    f
    for f in friends
    if filter_by_hiking(f)
]

lambda: 15 # face o funcție anonimă
lambda arg1, arg2: arg1 * arg2


list(
    filter(
        filter_by_hiking,
        friends
    )
)
# echivalent, rescris cu lambda:
list(
    filter(
        lambda elem: "hiking" in elem[2],
        friends
    )
)

def mkfilter(hobby):
    def filterer(elem):
        return hobby in elem[2]
    return filterer

list(
    filter(
        mkfilter("hiking"),
        friends
    )
)

def find_friends_by_hobby(friends, hobby):
    "returnează un iterator cu prietenii cu acel hobby"
    return list(filter(
        lambda elem: hobby in elem[2],
        friends
    ))


# haideți să găsim toți prietenii care sunt mai în
# vârstă de 30 de ani și fac "reading"
old_reading_friends = find_friends_by_hobby(
    find_friends_by_age(friends, min_age=30),
    'reading'
)
# și adăugați-le hobby-ul "knitting"
for friend in old_reading_friends:
    friend[2].append("knitting")

# observăm cum totul este o referință
# și Dan a primit "knitting"
print(friends)


# Task:
# sortați lista de orașe de mai jos
# în ordinea ascendentă a distanței
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
cities.sort(key=lambda elem: elem[1])

# să sortăm după lungimea numelui
cities.sort(key=lambda elem: len(elem[0]))

# Notă: există și sorted, ce merge pe orice iterabil:
sorted(cities, key=lambda elem: len(elem[0]))
