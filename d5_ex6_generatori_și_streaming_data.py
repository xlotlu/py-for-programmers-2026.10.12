# o "funcție" care conține statement-ul
# `yield`
# este automată transformată
# într-o "funcție generator"

# generatorii sunt cazuri speciale de iteratori

# iteratorii sunt obiecte iterabile,
# ce execută cod în timp ce sunt iterate,
# și își suspendă execuția după fiecare valoare
# ce o returnează celui ce le iterează.


def func():
    print("am intrat în funcție")
    yield "aa"
    print("sunt după primul yield")
    yield "be"
    print("sunt după al doilea yield")
    yield "ce"
    print("ies din funcție")

genobj = func()
for elem in genobj:
    print("»", elem)

# este echivalent cu:
genobj = func()
while True:
    try:
        elem = next(genobj)
        print("»", elem)
    except StopIteration:
        break

# task
# scrieți o funcție generator
def squares(start, stop):
    pass
# ce, atunci când este iterată,
# generează pătratele numerelor
# dintre start și stop inclusiv

def squares(start, stop):
    for nr in range(start, stop + 1):
        yield nr ** 2

for x in squares(10, 20):
    print(x)

# în cazul generatoarelor simple,
# putem să înlocuim funcția cu comprehension expression:

(
    nr ** 2
    for nr in range(start, stop + 1)
)

# putem de altfel scrie o funcție
# ce returnează direct expresia generator
def squares(start, stop):
    return (
        nr ** 2
        for nr in range(start, stop + 1)
    )


# Exercițiu:
# dat fiind dataset-ul "data/temp_sesor_data.csv"
# scrieți o funcție ce returnează un iterabil
# cu mediile temperaturilor fiecărei ore.
#
# faceți ca elementele acestui iterabil să fie
# de forma (hour, average).

import csv
import datetime as dt

# implementarea 1:
# un ciocan mare, dicționar, cu valori listă
# în care așezăm toate valorile și gata.
def process_temps(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)

        from collections import defaultdict
        averages = defaultdict(list)

        for timestamp, value in reader:
            timestamp = dt.time.fromisoformat(timestamp)
            value = float(value)

            averages[timestamp.hour].append(value)

        return [
            (k, sum(v) / len(v))
            for k, v in averages.items()
        ]


# ceva mai finuț, păstrăm doar running total & running count
def process_temps(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)

        from collections import defaultdict
        averages = defaultdict(lambda: {
            'total': 0,
            'count': 0,
        })

        for timestamp, value in reader:
            timestamp = dt.time.fromisoformat(timestamp)
            value = float(value)

            averages[timestamp.hour]['total'] += value
            averages[timestamp.hour]['count'] += 1

        return [
            (k, v['total'] / v['count'])
            for k, v in averages.items()
        ]


# next-level improvement:
# streaming data
def process_temps(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)

        old_hour = None
        total = 0
        count = 0

        for timestamp, value in reader:
            timestamp = dt.time.fromisoformat(timestamp)
            value = float(value)

            if old_hour is not None and timestamp.hour != old_hour:
                # calculăm, average-ul orei vechi
                yield old_hour, total / count

                # și resetăm valorile
                total = 0
                count = 0

            total += value
            count += 1

            old_hour = timestamp.hour

        # else:
        #     pass
        #     # for suportă "else", care se execută
        #     # doar când iterația a fost cu succes
        #     # (adică nu s-a făcut break)

        # la final trebuie să calculăm și ora finală:
        yield old_hour, total / count


TEMP_DATA = "data/temp_sensor_data.csv"
#TEMP_DATA = "data/mini_temp_data.csv"

#for elem in process_temps(TEMP_DATA):
#    print(elem)


# next-next level improvement:
# exact aceeași logică, dar separăm parsarea de fișier
# de logica de agregare

def load_temps(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)

        for timestamp, value in reader:
            timestamp = dt.time.fromisoformat(timestamp)
            value = float(value)

            yield timestamp, value

# (același lucru, scris ca generator expression)
def load_temps(csvfile):
    # dar atenție, nu avem voie să folosim `with`
    reader = csv.reader(open(csvfile))

    return (
        (dt.time.fromisoformat(timestamp), float(value))
        for timestamp, value in reader
    )

def process_temperatures(iterable):
    old_hour = None
    total = 0
    count = 0

    for timestamp, value in iterable:
        if old_hour is not None and timestamp.hour != old_hour:
            # calculăm, average-ul orei vechi
            yield old_hour, total / count

            # și resetăm valorile
            total = 0
            count = 0

        total += value
        count += 1

        old_hour = timestamp.hour

    # la final trebuie să calculăm și ora finală:
    yield old_hour, total / count


if __name__ == "__main__":
    for elem in process_temperatures(
        load_temps(TEMP_DATA)
    ):
        print(elem)
