# 1) accesul după index poate fi negativ:
lst = ["ala", "bala", "porto", "cala"]

lst[-1] # -> "cala"
lst[-2] # -> "porto"


# 2) există și acces după "slice"
lst[1:3] # -> ['bala', 'porto']


# 3) fiecare parte a slice-ului poate să
# fie omisă
lst[2:] # []"porto", "cala"]

# combinând cele trei concepte:
# ultimele 2 elemente?
lst[-2:]

# primele două elemente?
lst[:2]

# toate elementele fără ultimele 2?
lst[:-2]


### metodele listei ###
lst.append("un element") # adaugă "un element"

lst.extend(["unul", "doiul"]) # adaugă fiecare dintre elemente

lst.pop() # șterge și returnează ultimul element

lst.pop(2) # șterge și returnează elementul de la indexul 2

lst.remove("ala") # șterge prima apariție a elementului
# echivalentul său este:
def remove_from_list(lst, value):
    idx = 0
    while idx < len(lst):
        _v = lst[idx]

        if _v == value:
            del lst[idx]
            break

        idx += 1
