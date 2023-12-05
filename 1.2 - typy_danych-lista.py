# lista - kolekcja prechowujaca dowolna ilosc , dowolnych danych na raz
# zachowanie kolejności przy dodawaniu

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

lista.append("Radek")
lista.append("Tomek")
lista.append("Maciek")
lista.append("Zenek")

print(lista)  # ['Radek', 'Tomek', 'Maciek', 'Zenek']
print(lista[0])  # Radek
print(lista[3])  # Zenek
print(lista[-1])  # Zenek

print(lista[0:3])  # ['Radek', 'Tomek', 'Maciek']  0,1,2
print(lista[0:3:2])  # ['Radek', 'Maciek']  start, stop, krok
print(lista[-1::-1])  # ['Zenek', 'Maciek', 'Tomek', 'Radek'] lista odwrócona

lista[0] = "Piotr"
print(lista)  # ['Piotr', 'Tomek', 'Maciek', 'Zenek']

# wstawienie elemntu w konkretny index
lista.insert(1, "Kamil")
print(lista)  # ['Piotr', 'Kamil', 'Tomek', 'Maciek', 'Zenek']

# usuniecie elemntu
lista.remove("Piotr")
print(lista)  # ['Kamil', 'Tomek', 'Maciek', 'Zenek']
# usunięcie po indeksie
print(lista.pop(1))  # Tomek

lista2 = lista  # kopia referencji (adresu w pamięci)
lista_copy = lista.copy()  # kopia elemntów listy
lista.clear()  # usunięcie elemntow z listy
print(lista)
print(lista2)
print(lista_copy)
print(id(lista))
print(id(lista2))
print(id(lista_copy))
# 2036446712064
# 2036446712064
# 2036447032448

liczby = [54, 999, 34, 22, 12.34, 876]
# liczby = [54, 999, 34, 22, 12.34, 876, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(liczby)  # [54, 999, 34, 22, 12.34, 876]
liczby.sort()
print(liczby)

# rozpakowanie sekwencji
lista3 = "Definicja"
lista4 = []
lista4.extend(lista3)
print(lista4)  # ['D', 'e', 'f', 'i', 'n', 'i', 'c', 'j', 'a']

lista5 = [lista3]
print(lista5)  # ['Definicja'] -> append()
lista_z_tekstu = list(lista3)
print(lista_z_tekstu)  # ['D', 'e', 'f', 'i', 'n', 'i', 'c', 'j', 'a'] -> extend

krotka = tuple(lista_z_tekstu)
print(type(krotka))
print(krotka)  # ('D', 'e', 'f', 'i', 'n', 'i', 'c', 'j', 'a')
