# krotka - kolekcja niezmienna(immutable)
# zmienna
tupla = "Radek"
print(type(tupla))  # <class 'str'>
tupla1 = ("Radek")
print(type(tupla1))  # <class 'str'>
tupla2 = "Radek",
print(type(tupla2))  # <class 'tuple'>
temp = 36, 6
print(type(temp))  # <class 'tuple'>
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>
tupla4 = "Radek", "Tomek", "Marek", "Zenek"
print(type(tupla4))  # <class 'tuple'>
tupla5 = 44, 55, 66, 34, 22.43, 11, 200
print(type(tupla5))  # <class 'tuple'>
print(tupla5[0])  # 44

print(tupla4.count("Tomek"))
print(tupla4.index("Radek"))

# rozpakowanie tupli
a, b = 1, 2
print(type((1, 2)))  # <class 'tuple'>
print(a)
print(b)

# a, b = 1, 2, 3 ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * worek na pozostałe dane
print(b)  # [2, 3]
print(type(b))  # <class 'list'>

# rozpakowac tupla4 do trzech zmiennych
# "Radek", "Tomek", "Marek", "Zenek"
imie1, *imie2, imie3 = tupla4
print(imie2)  # ['Tomek', 'Marek']

lista_krotka = list(tupla4)
print(lista_krotka)  # ['Radek', 'Tomek', 'Marek', 'Zenek']
print(type(lista_krotka))  # <class 'list'>
