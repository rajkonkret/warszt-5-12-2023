import pakiet
from pakiet import fun
import pakiet.fun as pk

print(pakiet)
# <module 'pakiet' from 'C:\\Users\\CSComarch\\PycharmProjects\\warszt-5-12-2023\\pakiet\\__init__.py'>

fun.powitanie()  # from pakiet import fun
pk.powitanie()  # import pakiet.fun as pk
# po dodaniu w pliku __init_.py __all__ = ['powitanie']
pakiet.powitanie()  # import pakiet

# <module 'pakiet' from 'C:\\Users\\CSComarch\\PycharmProjects\\warszt-5-12-2023\\pakiet\\__init__.py'>
# Powitanie
# Powitanie
# Powitanie
# poniewaz metody info() nie ma w ziennej __all__ nie mozemy jej uzyc bezpośrednio z pakietu
# możemy z dedykowanego importu
fun.info()
pk.info()
