absolute_path = '/tmp/un_director/alt_director/file.txt'

with open(absolute_path) as f:
    print(f.read())

# acesta este python invalid
# 'C:\Users\myuser\etc...'
# pentru că:


# \ <- escape character
#      introduce un escape sequence
'\n', '\t', '\r'

'\x4e' # indicele hexadecimal

'\u265B' # tot în hexa, 4 caractere, indicele din tabelul unicode

'\U0001F39C' # tot în hexa, 8 caractere, indicele din tabelul unicode

'\N{MUSIC NATURAL SIGN}' # numele din tabelul unicode

# ce facem?
# ori dublu backslash:
'C:\\Users\\myuser\\etc...'

# ori "raw string"
r'C:\Users\myuser\etc...'


# haideți să compunem path-uri

DATA_DIR = '/tmp/un_director/alt_director'

def read_data_file(name):
    path = DATA_DIR + '/' + name

    with open(path) as f:
        return f.read()

read_data_file('file.txt')


from os import path # old-school path handling, string-based

def read_data_file(name):
    fpath = path.join(DATA_DIR, name)

    with open(fpath) as f:
        return f.read()

read_data_file('file.txt')


from pathlib import Path

# rescrieți `read_data_file()` folosind pathlib.Path


def read_data_file(name):
    fpath = path.join(DATA_DIR, name)

    with open(fpath) as f:
        return f.read()

read_data_file('file.txt')


# inspectați metodele unui obiect Path
p = Path("myfile.txt")
p.resolve()  # rezolvă căile relative și symlink-urile
p.absolute() # doar adaugă partea absolută (în cazul căilor relative)
             # fără să rezolve
p.exists()   # evident

p.is_file()  # obvious
p.is_dir()   # same


p = Path(".")
p.iterdir() # un iterator
for elem in p.iterdir():
    print(type(elem), elem)

p.parent # directorul părinte
p.parents # un iterabil cu toți ancestors
for parent in p.parents:
    print(parent)
p.parts # toți ancestors, fiecare individual
p.suffix # extensia fișierului

p.glob('*.txt') # un iterabil cu files matching the glob pattern
for elem in p.glob('*.txt'):
    print(elem)
