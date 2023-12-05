# lambda - skrócony zapis funkcji
# mozliwośc dekalracji w miejscu użycia
from functools import reduce


def liczymy(x, y):
    return x * y


print(liczymy(5, 6))

liczymy2 = lambda x, y: x * y  # lambda z założenia ma return
print(liczymy2(7, 6))

lista = [1, 2, 3, 4, 6, 7, 20, 55, 100, 123]
# przemnożenie każdego elementu przez 2
lista2 = []
for i in lista:
    lista2.append(i * 2)

print(lista2)
print([i * 2 for i in lista])  # [2, 4, 6, 8, 12, 14, 40, 110, 200, 246]


def zmien(x):
    return x * 2


print([zmien(i) for i in lista])  # [2, 4, 6, 8, 12, 14, 40, 110, 200, 246]

# map() - wez wszystkie wartości z kolekcji i wykonaj na nich dziłąnie zadane funkcją
print(f"Użycie map(){list(map(zmien, lista))}")
# Użycie map()[2, 4, 6, 8, 12, 14, 40, 110, 200, 246]
# użycie lambdy w miejscu deklaracji
print(f"Użycie map(){list(map(lambda x: x * 2, lista))}")
# Użycie map()[2, 4, 6, 8, 12, 14, 40, 110, 200, 246]
# filter() - filtruje kolekcje i zwraca spełniajace warunek zadany funkcja
# x > 8
print(f"Użycie filter(){list(filter(lambda x: x > 8, lista))}")
# Użycie filter()[20, 55, 100, 123]
print(f"Użycie filter(){list(filter(lambda x: x < 30, lista))}")
# Użycie filter()[1, 2, 3, 4, 6, 7, 20]
print(f"Użycie filter(){list(filter(lambda x: 3 < x < 50, lista))}")
# Użycie filter()[4, 6, 7, 20]
print(f"Użycie filter(){list(map(lambda x: x ** 2, lista))}")
# Użycie filter()[1, 4, 9, 16, 36, 49, 400, 3025, 10000, 15129]
a = map(lambda x: x ** 2, lista)
for i in a:
    print(i)

r0 = {"miasto": "Kielce"}
r1 = {"miasto": "Kielce", "ZIP": "25-900"}
print(r0['miasto'])
print(r1['miasto'])
# print(r0['ZIP'])  # KeyError: 'ZIP'
print(r1['ZIP'])

print(r0.get('ZIP', '00-000'))

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(min(lata))
print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)


def iloczyn(a, b):
    return a * b


# reduce()
liczby = [1, 2, 3, 4, 5]
wynik = reduce(iloczyn, liczby)
print(wynik)  # 120
print(reduce(lambda a, b: a + b, liczby))  # 15
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# ctrl / szybki komentarz
