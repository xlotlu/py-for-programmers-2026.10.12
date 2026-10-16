# forma 1 minimală:

try:
    print("» entry code")
    1 / 0
except: # atenție, catch-all
    print("! a fost excepție")


# forma 2 minimală:

try:
    print("» entry code")
    1 / 0
finally:
    print("» mă rulez întotdeauna")


# exception targetat:
try:
    1 / 0
except ZeroDivisionError:
    print("» handled exception")


# exception multi-targetat:
d = {
    'key': ["a", "b", "c"]
}

try:
    d["x"]
except KeyError, IndexError:
    print("» handled some kind of exception")

# exception cu target specific pe branch-uri diferite:
try:
    d["key"][5]
except KeyError:
    print("» dicționar făcut buf")
except IndexError:
    print("» lista făcut buf")

# când vrem să avem acces la excepție:
try:
    1 / 0
except Exception as e: # o să prindă toate excepțiile care derivă din această clasă
    print(type(e), print(e))
    print(repr(e))

# îl introducem pe else:
try:
    1 / 1
except:
    print("» buba")
else:
    print("» ok!")
    
# și forma completă:
try:
    pass
except Exception:
    pass
# except ...
else:
    pass
finally:
    pass


# și ultimul detaliu:
# raise ridică o excepție

class MyError(Exception):
    pass

try:
    raise MyError("na poftim")
except:
    print('aici fac ceva specific faptului că am avut excepție')
    raise # fără argumente face re-raise la ultima excepție
    #       (are sens doar într-un branch de except)



# un exemplu concret de capturare de excepție
# cu acces la detaliile ei, în pydantic:
from pydantic import BaseModel, ValidationError

class MyModel(BaseModel):
    name: str
    age: int

try:
    obj = MyModel(name="Gigel", age="22x")
except ValidationError as e:
    print("am avut erori:")
    for err in e.errors():
        print(err['msg'])




def main():
    from time import sleep
    from random import randint

    if randint(1, 3) == 1:
        raise ValueError("ceva eroare unhandled")
    else:
        print("working")
        sleep(1)

# exemplu dezirabil de catch-all Exception
# my main program
while True:
    try:
        main()
    except Exception as e:
        print("o bubuit aci, da' vrem să ruleze în continuare")
        #log(e)
        print("l-am logat pe", repr(e))
