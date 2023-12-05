# set - zbiór -  brak duplikatów, przechowuje unikalne wartości
# nie zachowuje kolejnosci przy dodawaniu elementów

lista = [44, 55, 66, 77, 33, 31, 33, 55, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 11, 44, 77, 55, 31}
zbior.add(18)
zbior.add(33)
zbior.add(18)
zbior.add(55)
print(zbior)

zbior.remove(55)
print(zbior)

# pop() - usuniecie pierwszzego elemntu
print(zbior.pop())  # 33
print(zbior.pop())  # 66
print(zbior.pop())  # 11
print(sorted(zbior))  # [18, 31, 44, 77] - wypisze posortowaną listę

zb2 = set()  # pusty set
print(zb2)  # set() - puste set

zbior2 = {66, 11, 44, 55, 62, 999, 999}
print(zbior2)  # {66, 55, 999, 11, 44, 62}

print(zbior | zbior2)  # suma zbiorów {66, 999, 11, 44, 77, 18, 55, 62, 31}
print(zbior & zbior2)  # częśc wspólna zbiorów {44}
print(zbior - zbior2)  # różnica {18, 77, 31}
print(zbior.difference(zbior2))  # {18, 77, 31}

print(zbior.union(zbior2))  # suma zbiorów {66, 999, 11, 44, 77, 18, 55, 62, 31}
print(zbior)
print(zbior2)
# zbiory nie zostały zmodyfikowane - union()

# update() - modyfikuje zbior
zbior.update(zbior2)
print(zbior)
print(zbior2)
# 13:25
