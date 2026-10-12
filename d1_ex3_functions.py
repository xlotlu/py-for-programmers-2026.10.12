def numefunctie():
    print("wow, o funcție")

def myfunc():
    return 42

retval = myfunc()
print(retval)

def multiply(a, b):
    return a * b


# Exercițiu:
# scrieți o funcție
def get_greeting(hour):
    pass # statement no-op
# ce returnează string-ul cu salutul potrivit
# conform argumentului `hour`


def get_greeting(hour):
    if 5 <= hour < 10:
        return "Buna dimineata"
    elif 10 <= hour < 18:
        return "Buna ziua"
    elif 18 <= hour < 22:
        return "Buna seara"
    else:
        return "Noapte buna"

"""
if conditie_ce_nu_ma_intereseaza:
    pass
else:
    fac_ceva_interesant()

# echivalent cu:
if not conditie_ce_nu_ma_intereseaza:
    fac_ceva_interesant()
"""

# știind că în modulul datetime există clasa datetime,
# care are metoda `.now()` ce returnează timpul curent,
# și că un obiect de tip datetime are atributul `.hour`
#
# scrieți o funcție
def get_current_greeting():
    pass
# ce folosește funcția `get_greeting()` de mai sus
# pentru a returna salutul potrivit pentru acest moment al zilei.

from datetime import datetime

def get_current_greeting():
    now = datetime.now()
    return get_greeting(now.hour)


# Exercițiu, wrapping-up:
# cereți numele utilizatorului
# și salutați-l potrivit cu ora curentă

name = input("Cum te numesti? ")
greeting = get_current_greeting()
print(f"{greeting} {name}!")

# în interiorul f-string-ului, între acolade se evaluează Python!
print(f"{get_current_greeting()}, {name}!")

# testăm un pic funcția
for hour in [1, 4, 5, 6, 9, 10, 11, 14, 17, 18, 19, 21, 22, 23]:
    print(hour, get_greeting(hour))
