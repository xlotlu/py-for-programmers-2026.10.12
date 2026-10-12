# if conditie:
#     statement_1
#     statement_2

#     if altceva:
#         alt_statement
# print("am ieșit din if")

# în alte limbaje:
# if (conditie) {
#     statement_1;
#     statement_2;
# }


"""
# v.1
if conditie:
    statement

# v.2
if conditie:
    statement
else:
    statement

# v.3
if conditie1:
    statement
elif conditie2:
    statement

# v.4
if condition1:
    statements
elif condition2:
    statements:
# ... elif
else:
    final_statement
"""



# Exercițiu:
# cereți vârsta utilizatorului cu input
# dacă este mai tânăr de 18 ani,
# printați "ești prea tânăr",
# altfel printați "ești acceptat".
#
# Atenție: ce este primit de la input()
#          este întotdeauna string



# age = int(input("Vârsta ta: "))

# if age < 18:
#     print("Esti prea tanar!")
# else:
#     print("Esti acceptat!")


# Exercițiu:
# scrieți un condițional
# care să printeze salutul corect pentru ora curentă
# astfel:
# între 5 și 10:  "Bună dimineața"
# între 10 și 18: "Bună ziua"
# între 18 și 22: "Bună seara"
# între 22 și 5:  "Noapte bună"

ora = 3

if ora >= 5 and ora < 10:
    print("Buna dimineata")
elif ora >= 10 and ora < 18:
    print("Buna ziua")
elif ora >= 18 and ora < 22:
    print("Buna seara")
elif ora >= 22 or ora < 5:
    print("Noapte buna")

"sql-style: ora BETWEEN 5 AND 10"

if 5 <= ora < 10:               # operator chaining !
    print("Buna dimineata")
elif 10 <= ora < 18:
    print("Buna ziua")
elif 18 <= ora < 22:
    print("Buna seara")
else:
    print("Noapte buna")
