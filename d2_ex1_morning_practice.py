#1. partea întreagă a împărțirii lui 17 la 4
17 // 4

#2. restul împărțirii lui 17 la 4
17 % 4

#3. 2 ridicat la puterea a 6a?
2 ** 6

#4. scrieți o funcție cube(x) ce returnează
# cubul numărului x
def cube(x):
    return x ** 3

#5. obțineți un nr. întreg de la utilizator
# și printați string-ul
# "Cubul numărului <număr> este <cubul său>."
# folosind funcția `cube()` de mai sus.
num = int(input("Scrie un numar intreg: "))
print(f"Cubul numărului {num} este {cube(num)}.")


#6. dat fiind string-ul
s = "Cri, cri, ce dimineața aurie de toamnă!"

# a) obțineți primele 8 caractere
s[:8]

# b) ultimele 10 caractere
s[-10:]

# c) caracterul de la indexul 5
s[5]

# d) cele 12 caractere ce încep de la indexul 10
s[10:22]

# e) știind că sintaxa completă de slice este
# start:stop:step
# și că step-ul default este 1,
# printați string-ul `s` de la coadă la cap.
s[::-1]

#7. printați numerele de la 125 la 100 folosind while
while x >= 100:
    print(x)
    x -= 1

#8. printați numerele de la 125 la 100 folosind for și range.
# țineți cont că funcția range() are al 3lea parametru opțional
# step=1.
for x in range(125, 99, -1):
    print(x)

#9. dat fiind variabila globală
M_TO_FT = 3.28084
# scrieți două funcții `feet_to_meters(ft)` și `meters_to_ft(m)`
def feet_to_meters(ft):
    return ft / M_TO_FT

def meters_to_ft(m):
    return m * M_TO_FT

#10. scrieți o funcție
def format_seconds(s):
    pass
# ce primind un număr întreg
# returnează un string de forma "[M]M:SS".

def format_seconds(s):
    minutes = s // 60
    seconds = s % 60
    # brute-force, algoritmic
    if seconds < 10:
        seconds = "0" + str(seconds)
    return f"{minutes}:{seconds}"


def format_seconds(s):
    minutes = s // 60
    seconds = s % 60
    # metodele string-ului
    seconds = str(seconds).rjust(2, "0")
    return f"{minutes}:{seconds}"


def format_seconds(s):
    # mai compact
    minutes, seconds = divmod(s, 60)
    # facilitate de string formatting:
    return f"{minutes}:{seconds:02}"

format_seconds(100) == "1:40"
format_seconds(124) == "2:04"



#11. [opțional pentru cine a terminat]
#    [are nevoie de research. aveți voie cu google.]
# scrieți o funcție
def get_seconds_from_now(timespec):
    pass
# ce returnează numărul de secunde dintre momentul curent
# și următoarea apariție a lui `timespec`, ce este un string
# de forma "[H]H:MM". exemplu: "9:40", "8:40".
#
# considerați că două `datetime.datetime`-uri pot fi scăzute
# și că rezultatul este un obiect de tip `datetime.timedelta`.

from datetime import datetime, timedelta

def get_seconds_from_now(timespec: str) -> float: # annotation
    hour, minute = timespec.split(":")
    hour, minute = int(hour), int(minute)

    now = datetime.now()
    future = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if future < now:
        # this is in the past, it needs to be tomorrow:
        future += timedelta(days=1)

    delta = future - now
    return delta.total_seconds()

from datetime import time

# îmbunătățire folosind metoda de parsare a timpului
def get_seconds_from_now(timespec: str) -> float:
    ts = time.strptime(timespec, "%H:%M")
    # sau
    ts = time.fromisoformat(timespec)

    now = datetime.now()
    future = now.replace(hour=ts.hour, minute=ts.minute, second=0, microsecond=0)

    if future < now:
        # this is in the past, it needs to be tomorrow:
        future += timedelta(days=1)

    delta = future - now
    return delta.total_seconds()