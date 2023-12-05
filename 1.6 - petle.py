# for petla iteracyjna
for i in range(10):  # 0..9
    print(i)

for i in range(1, 10):  # 1..9
    print(i)

for i in range(10):
    for j in range(10):
        print(i, j)

# list coprehesions
lista2 = [j for j in range(10)]
print(lista2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for c in lista2:
    print(c)

# if - warunek
# if warunek:
#     wykonaj komendę

if True:
    pass  # nic nie rób

a = 1
if a == 1:
    print(f"A równa się 1")
else:  # wartość domyslna
    print("A nie równa się 1")

a = 20
if a == 1:
    print("1")
elif a == 20:
    print("20")
else:
    print("Nie wiem")

for c in lista2:
    if c % 2 == 0:  # reszta z dzielenie (modulo)
        print(c, "parzysta")

lista4 = [j for j in range(10) if j % 2 == 0]
print(lista4)  # [0, 2, 4, 6, 8]
