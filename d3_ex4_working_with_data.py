BOOKS_CSV = "data/books.csv"

import csv

with open(BOOKS_CSV) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Task:
# scrieți o funcție
def read_books(csvfile, filter_genre=None):
    pass
# ce returnează cărțile din csv-ul respectiv
# filtrate după Genre
#
# returnați o listă de dicționare

def read_books(csvfile, filter_genre=None):
    with open(csvfile) as f:
        reader = csv.DictReader(f)

        return [
            item
            for item in reader
            if (
                filter_genre is None
                or filter_genre == item['Genre']
            )
        ]

print(
    read_books(BOOKS_CSV, 'data_science')
)

# Task:
# transformați funcția de mai sus
# să returneze un generator în loc de listă

from time import sleep

def read_books(csvfile, filter_genre=None):
    f = open(csvfile)
    reader = csv.DictReader(f)

    return ( # expresie generator, un caz particular de iterator
        item
        for item in reader
        if sleep(.02) == None and ( # modalitate foarte urâtă de a adăuga un sleep în pipeline
            filter_genre is None
            or filter_genre == item['Genre']
        )
    )

for elem in read_books(BOOKS_CSV, 'signal_processing'):
    print(elem['Title'])
