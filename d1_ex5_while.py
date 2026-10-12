# while conditie:
#    do_stuff()

# unde `conditie` este ceva evaluabil
# în context boolean.

x = 5
while x >= 0:
    print(x)
    x -= 1
    # echivalent cu
    #x = x - 1


# notă: în Python totul este evaluabil în context boolean!

# toate elementele "goale" sunt False-y:
for elem in 0, "", [], (), {}:
    print(elem, bool(elem))

for elem in int(), str(), list(), tuple(), dict():
    print(elem, bool(elem))


# Exercițiu:
# scrieți o funcție
def ask_for_name():
    pass
# ce promptează utilizatorul pentru numele său
# și repetă procesul dacă input-ul a fost gol
def ask_for_name():
    name = input("Numele tău? ")

    while not name:
        print("Numele este obligatoriu")
        name = input("Numele tău? ")

    return name

# rescrisă cu while True și break:
def ask_for_name():
    while True:
        name = input("Numele tău? ")

        if name:
            break
        else:
            print("Numele este obligatoriu")

    return name

# rescrisă cu continue:
def ask_for_name():
    while True:
        name = input("Numele tău? ")

        if not name:
            print("Numele este obligatoriu")
            continue
        else:
            break

    return name


# valabile și în for, și în while:
# break
# continue


# Exercițiu:
# scrieți o funcție
def ask_for_int(prompt=""):
    pass
# ce promptează utilizatorul cu prompt-ul opțional `prompt`
# și returnează dacă a primit un număr întreg valid
# sau altfel printează un mesaj de eroare
# și cere în mod repetat input-ul.
#
# sosul secret: folosiți metoda `.isdecimal()` a str-ului.

def ask_for_int(prompt=""):
    number = input(prompt)

    while not number.isdecimal():
        print("Număr invalid. Încearcă din nou.")
        number = input(prompt)

    return int(number)


ask_for_int("Zi-mi un număr întreg: ")

