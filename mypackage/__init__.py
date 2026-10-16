print(f"» eu sunt logica lui {__name__}")

# dacă vrem să expunem acces la un submodul
# folosim cale relativă

# ATENȚIE: căile relative funcționează
#          doar în interiorul unui package

# dacă am vrea să expunem submodule direct
# am face aici
#from . import submodule

from .submodule import functie_importanta


PACKAGE_VAR = 21
