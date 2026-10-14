# scrieți două funcții
def readfile(path, encoding="utf-8"):
    pass
# ce citește și returnează conținutul fișierului `path`

def writefile(path, contents, overwrite=False, encoding="utf-8"):
    pass
# respectiv scrie string-ul `contents` în fișierul `path`


def readfile(path, encoding="utf-8"):
    return open(path, encoding=encoding).read()

def writefile(path, contents, overwrite=False, encoding="utf-8"):
    if overwrite:
        mode = 'w'
    else:
        mode = 'x'

    f = open(path, mode, encoding=encoding)
    f.write(contents)

# facem rewrite folosind ternary operator
def writefile(path, contents, overwrite=False, encoding="utf-8"):
    mode = 'w' if overwrite else 'x'
    f = open(path, mode, encoding=encoding)
    f.write(contents)


# ce facem cu așa ceva? cum închidem fișierul?
def readfile(path, encoding="utf-8"):
    f = open(path, 'r', encoding=encoding)
    # mai multe operațiuni
    r = f.read()
    # și alte operațiuni

    1 / 0

    f.close()
    return r

# pe vremuri făceam așa:
def readfile(path, encoding="utf-8"):
    f = open(path, 'r', encoding=encoding)

    try:
        # mai multe operațiuni
        r = f.read()
        # și alte operațiuni

        1 / 0

    finally:
        f.close()

    return r


# zilele acestea folosim un "context manager"
with something as var: # `something` este context manager-ul
    do_stuff()
    1 / 0


with open(path) as f:
    f.read()
    1 / 0


f = open(path)
with f as f:
    # stuff
    pass
f.closed is True


# un context manager garantează:
# 1) că la intrarea în context se execută cod custom
#    definit de ctx manager-ul respectiv, și
# 2) că la ieșirea din context se execută cod custom
#    definit de ctx manager-ul respectiv

# de ce există? primar pentru a putea defini obiecte
# ce își fac cleanup-ul singure,
# fără să fie nevoie de try / finally

# în cazul obiectelor - fișier, acestea își fac close() singure



# exemple de context managere din stdlib:

# 1. sqlite
import  sqlite3

db = sqlite3.connect("sqlite.db")
db.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
db.execute("insert into lang values(1, 'ceva nou')")
db.execute("insert into lang values(2, 'ceva nou 2')")
db.commit()

try:
    with db: # transaction manager, face auto-commit / auto-rollback
        db.execute("insert into lang values(4, 'ceva bun')")
        db.execute("insert into lang values(5, 'ceva nou')") # crapă
except sqlite3.IntegrityError:
    print("a crăpat")
# verificăm atomicitate:
for elem in db.execute("select * from lang"):
    print(elem)


# 2. tempfile
from tempfile import TemporaryFile
with TemporaryFile() as f:
    f.write(b"chestii")


#3. change current working directory
import contextlib
with contextlib.chdir("/tmp"):
    open("test.txt", 'w').close()
# echivalent cu:
import os
_old_cwd = os.getcwd()
os.chdir("/tmp")
print("face ceva local în /tmp")
open("test.txt", 'w').close()
os.chdir(_old_cwd)



# rescriem funcțiile cu context manager:
def readfile(path, encoding="utf-8"):
    with open(path, encoding=encoding) as f:
        return f.read()

def writefile(path, contents, overwrite=False, encoding="utf-8"):
    mode = 'w' if overwrite else 'x'
    with open(path, mode, encoding=encoding) as f:
        f.write(contents)


# Exercițiu: scriem o funcție ce copiază un fișier în altul
def cp(srcpath, targetpath, overwrite=False):
    with open(srcpath) as infile:
        # entry statements

        with open(targetpath, 'w') as outfile:
            # other entry statements
            outfile.write(infile.read())

# cu un singur `with` statement:
def cp(srcpath, targetpath, overwrite=False):
    with open(srcpath) as infile, open(targetpath, 'w') as outfile:
        outfile.write(infile.read())

# dacă vrem să facem codul mai spațiat:
# v1) cu paranteze:
def cp(srcpath, targetpath, overwrite=False):
    with (
        open(srcpath) as infile,
        open(targetpath, 'w') as outfile
    ):
        outfile.write(infile.read())

# v2) cu line-continuation:
def cp(srcpath, targetpath, overwrite=False):
    # line-continuation character = backslash la sfârșitul liniei
    with open(srcpath) as infile, \
         open(targetpath, 'w') as outfile:
        outfile.write(infile.read())


# funcția fixată,
# ține cont de overwrite, face chunked read/write,
# și folosește "walrus operator"

def cp(srcpath, targetpath, overwrite=False, chunksize=4096):
    mode = 'wb' if overwrite else 'xb'

    with (
        open(srcpath, 'rb') as infile,
        open(targetpath, mode) as outfile
    ):
        while chunk := infile.read(chunksize):
            outfile.write(chunk)
