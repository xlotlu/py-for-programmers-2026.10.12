name = "Ionuț"

print("Salut " + name + "!!!") # concatenare de str

print("Salut %s!!!" % name) # old-school string interpolation

print(f"Salut {name}!!!") # new-style, "f-string" ("formatted string")

# Exercițiu: obțineți numele utilizatorului cu input()
# și salutați-l

name = input("Care este numele tău? ")
print(f"Salut {name}!!!")
