obj = open("test.txt")

# există două modalități de a lucra cu fișiere:
# 1. citim (tot) contentul
obj.read()

# 2. iterăm în fișier:
for elem in open("test.txt"):
    print("»»»", elem)


# modul write:
f = open("newfile.txt", 'w')
# atenție: modul 'w' trunchează fișierul vechi!
f.write("ceva content")
# ^^ nu va ajunge pe drive
#    decât când decide kernel-ul

# în mod normal nu vreți să faceți flush() manual
f.flush()
f.write("Și alt content")
f.flush()
f.write("\nAceasta este o linie nouă")

# închiderea fișierului va face flush automat
f.close()


# modul 'x':
# creează un fișier nou
f = open("anotherfile.txt", 'x')
f.write("povești etc.")
f.close()

# dacă încercăm să deschidem un fișier existent
# în modul 'x', va da excepție:

try:
    f = open("anotherfile.txt", 'x')
except FileExistsError:
    print("fișierul există deja")


# modul 'a', "append".
# vreți să îl folosiți dacă scrieți loguri
f = open("anotherfile.txt", 'a')
f.write("acest content se va duce la sfârșit")


# introducem modul binary
# (pe care cel mai probabil nu veți avea nevoie
# să-l folosiți)

# mai sus, de fapt toate exemplele au fost
# în modul default "text".
# adică: 'rt', 'wt', 'xt', 'at'
#
# în binary mode:
# 'rb', 'wb', 'xb', 'ab'


# [!!!] nu uitați să puneți encoding la citire și scriere
#       (dovezile noi arată că semnele de exclamare sunt exagerate)
open("anotherfile.txt", 'a', encoding="utf-8")

# 1. demonstrație despre de ce există encoding
# și ce se întâmplă când este decodat cu alt charset
# decât cel cu care a fost encodat
mystr = "Şi atunci âm luat şi o ţară la pîcior. Ţţţ"
mystr.encode("iso-8859-2").decode("iso-8859-1")

# 2. demonstrație despre ce se întâmpla pe windows
# înainte de python 3.15:
# (cp1252 era charset-ul default)
f = open("file.txt", "w", encoding="cp1252")
f.write("String cu diăcrîțice") # explodează!

