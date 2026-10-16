# 1. dat fiind datasetul friends
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# transformați-l într-o listă de dicționare
# cu cheile 'name', 'age', 'hobbies'
#
# folosiți dict(zip(...))

dfriends = [
    dict(zip(
        ('name', 'age', 'hobbies'),
        elem
    ))
    for elem in friends
]

# 2. dat fiind dicționarul occupations
occupations = {
    "Jane": "nurse",
    "Dan": "firefighter",
    "Mike": "dancer",
    "Sam": "boat captain",
    "Anna": "gardner",
}
# în care cheia este numele persoanei din `friends`,
# adăugați la fiecare dicționar de friend
# ocupația potrivită.
#
# care este strategia potrivită?
# iterăm prin friends, sau iterăm prin occupations?

for df in dfriends:
    name = df['name']

    try:
        occ = occupations[name]
    except KeyError:
        continue

    df['occupation'] = occ


# dar dacă vrem să iterăm pe occupations?
# haideți să să optimizăm accesul la lista de prieteni,
# creând un dicționar intermediar
dfriends_dict = {
    df['name']: df
    for df in dfriends
}

# ^^ un pattern bun, deseori: dicționar de dicționare.
#    deseori = când avem nevoie de acces optimizat via o cheie gen "id".

for name, occ in occupations.items():
    dfriends_dict[name]['occupation'] = occ


# 3. având o listă de dicționare
people = [
  {'name': 'Jane', 'age': 25},
  {'name': 'John', 'age': 38},
  {'name': 'Andrew', 'age': 19},
  {'name': 'Georgia', 'age': 28},
  {'name': 'Lisa', 'age': 46},
  {'name': 'Carmen', 'age': 68},
  {'name': 'Thomas', 'age': 22},
  {'name': 'Bill', 'age': 31},
  {'name': 'Peter', 'age': 47},
  {'name': 'Stephen', 'age': 42},
]
# scrieți un one-liner ce calculează media de vârstă.
#
# folosiți funcția `sum()` ce primește ca argument un iterabil.

sum(
    p['age'] for p in people
) / len(ages)
# este echivalentă cu
sum( ( p['age'] for p in people ) )  / len(ages)

# 4. folosind aceeași structură de date `people`
# calculați într-o singură iterație
# suma, vârsta minimă și vârsta maximă.
#
# există funcțiile `min()` și `max()`.


ages = [
    p['age'] for p in people
]
sum(ages) / len(ages), min(ages), max(ages)
# ^^ aici sunt 4 iterații de fapt ^^

# atunci facem calculele la runtime, în timpul iterației
import math

total = 0
min_age = math.inf # pt. că voiam un număr mai mare decât orice alt număr...
max_age = 0
for elem in people:
    age = elem['age']

    total += age
    min_age = min(age, min_age)
    max_age = max(age, max_age)

print(
    total / len(people),
    min_age,
    max_age
)


# 5. scrieți o funcție
def count_words(txt, insensitive=True):
    pass
# ce primind string-ul `txt`, numără aparițiile
# fiecărui cuvânt din string
# (și returnează un data type potrivit pentru aceasta)
#
# testați-o cu string-ul
s = """
It was the best of times,
it was the worst of times,
it was the age of wisdom,
it was the age of foolishness,
it was the epoch of belief,
it was the epoch of incredulity,
it was the season of Light,
it was the season of Darkness,
it was the spring of hope,
it was the winter of despair…
"""

# avem nevoie de o funcție de splitat cuvinte
# v.1. kinda brute-force:
import string

def split_words(txt):
    for c in string.punctuation + '…—–':
        txt = txt.replace(c, ' ')
    # ^ ineficient că facem multe iterații
    # plus tot ce e în afara tabelului ascii
    # rămâne considerat ca word character
    return txt.split()

# v.2. folosim regular expressions
import re
def split_words(txt):
    return re.findall(r'\w+', txt)


from collections import defaultdict

def count_words(txt, insensitive=True):
    if insensitive:
        txt = txt.lower()

    counts = defaultdict(int)

    for word in split_words(txt):
        counts[word] += 1

    return counts


# 6. scrieți o funcție
def grep(fname, match, insensitive=False):
    if insensitive:
        #match = match.lower()
        # preferat pentru comparațiile case-insensitive:
        match = match.casefold()

    with open(fname) as f:
        for line in f:
            if match in (line.casefold() if insensitive else line):
                print(line.removesuffix("\n"))

# ce printează toate liniile din `fname`
# care conțin `match`
grep('/usr/share/doc/bash/README', 'posix', True)

# 7. să încărcăm ceva dintr-un API
# și să salvăm pe disk

# în shell-ul sistemului, a rula
# $ python /usr/lib/python3.14/json/tool.py
# este echivalent cu
# $ python -m json.tool

# alt modul util:
# $ python -m http.server

# dat fiind REST endpoint-ul
TODOS_URL = 'https://jsonplaceholder.typicode.com/todos'
# scrieți o funcție
def save_todos_to_csv(url, csvfile, completed=False):
    pass
# ce scrie în csv
# todo-urile filtrate conform `completed`

import requests
import csv

# în modulul csv avem:
csv.reader, csv.writer, csv.DictReader, csv.DictWriter

def save_todos_to_csv(url, csvfile, completed=False):
    resp = requests.get(url)
    todos = resp.json()

    with open(csvfile, 'w', encoding='utf-8') as f:
        fields = resp.json()[0].keys()
        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()

        for todo in todos:
            # scrie-l în csv
            writer.writerow(todo)

# v.2., folosind writerows()

def save_todos_to_csv(url, csvfile, completed=None):
    """
    saves the TODOs from the given `url`,
    filtered by `completed` status.

    if `completed=None` it performs no filtering.
    """
    resp = requests.get(url)

    # evoluția unei filtrări:

    # a) filtrare completă în intereiorul conprehension-ului
    todos = (
        todo
        for todo in resp.json()
        if completed is None
           or todo['completed'] is completed
    )

    # b) pre-filtrare selectivă depinzând de argumentul `completed`
    if completed is None:
        todos = resp.json()
    else:
        todos = (
            todo
            for todo in resp.json()
            if todo['completed'] is completed
        )


    # c) o singură expresie comprehension
    #    cu generare de funcții specifice,
    #    depinzând de argumentul `completed`
    #    [*] de ținut minte
    if completed is None:
        def _filter(item):
            return True
    else:
        def _filter(item):
            return item['completed'] is completed

    # d) același lucru ca mai sus
    #    but really pushing it cu lambda
    _filter = (
        (
            lambda item: True
        )
        if completed is None else
        (
            lambda item: item['completed'] is completed
        )
    )

    todos = (
        todo
        for todo in resp.json()
        if _filter(todo)
    )

    with open(csvfile, 'w', encoding='utf-8') as f:
        fields = resp.json()[0].keys()
        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()
        writer.writerows(todos)


# răspuns final:
def save_todos_to_csv(url, csvfile, completed=None):
    """
    saves the TODOs from the given `url`,
    filtered by `completed` status.

    if `completed=None` it performs no filtering.
    """
    resp = requests.get(url)

    if completed is None:
        def _filter(item):
            return True
    else:
        def _filter(item):
            return item['completed'] is completed

    todos = (
        todo
        for todo in resp.json()
        if _filter(todo)
    )

    with open(csvfile, 'w', encoding='utf-8') as f:
        fields = resp.json()[0].keys()
        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()
        writer.writerows(todos)

save_todos_to_csv(TODOS_URL, 'the_todos.csv')