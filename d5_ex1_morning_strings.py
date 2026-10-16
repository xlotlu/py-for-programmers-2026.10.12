s = "Cri, cri, toamnă gri..."

# de câte ori apare substring-ul
s.count("ri")

# primul index al substr-ului
s.index("ri") # raises ValueError if not found
# tot primul index, dar
s.find("rix") == -1

# .index() și .find() au prietenii
# .rfind() și .rindex()


# începe cu / se termină cu substr
s.startswith("Cri")
s.endswith("i...")

template = """
Acesta este un mail către {nume}.
Bună ziua {nume},
scrie-ne la {adresa:_>24s}
în maxim {zile:04d}.
"""
template.format(nume="Gigel",
                adresa="Str. X nr. 17",
                zile=2)

"123".isdecimal() # mod de verificare preferat pt. user input


s.lower()
s.upper()
s.title() # poate util în engleză
s.capitalize() # posibil mai util


"o coloană | a doua coloană".split(" | ")
# inversul său:
cols = ['o coloană', 'a doua coloană']
" | ".join(cols)

# split cu argument nr.
"o poveste lungă despre ceva".split(" ", 2)
# are sens prietenul său rsplit()


"""ceva
multiline
""".splitlines() # mai bun decât .split("\n")


"     \t\n povești și chestii    ".strip()
"     \t\n povești și chestii    ".strip(" i")
# și are prietenii .lstrip() și .rstrip()


s.replace("ri", "XX")