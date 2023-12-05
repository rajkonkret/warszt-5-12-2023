# funkcje - wydzielony fragment kodu, który mozemy wykonac w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana - w miejscu deklaracji nie wykonuje sie
# dopiero po zadeklarowaniu może byc uzyta

a = 9
b = 8


# dekalracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a, b)


# int - to tylko podpowiedź
def odejmij(a: int, b: int, c=0):  # c ma wartość domyslną
    print(a - b - c)


def mnozenie(a, b, c):
    return a * b * c


def mnozenie2(a, b):
    return a, b, a * b  # 1, 2, 2


dodaj()  # 17
dodaj2(2, 3)
odejmij(1, 2, 3)
odejmij(1, 2)

print(odejmij(1, 2, 3))  # None
print(mnozenie(1, 2, 3))
print(mnozenie(b=3, a=7, c=9))
print(mnozenie(1, 2, 3) + mnozenie(2, 3, 4))
a, b, c = mnozenie2(1, 2)
print(f"Wynik {a} * {b} = {c}")  # Wynik 1 * 2 = 2
