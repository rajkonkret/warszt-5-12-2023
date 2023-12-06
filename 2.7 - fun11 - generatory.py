# generatory - zwracaja wynik operacji
# maja wskaźnik, który ustawiaja na nstepny po każdej operacji
# odczyt sekwencyjny

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):  # 0..n-1, start 0, 1,2....
        yield x ** 2  # zwraca wynik i zapamietuje, ustawia wskaźnik na nstepny


kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x0000026D81A7FED0>
print(next(kwa))  # next() - odczytanie kolejnych wyników generatora
print(next(kwa))  # next() - odczytanie kolejnych wyników generatora
print(next(kwa))  # 9 next() - odczytanie kolejnych wyników generatora
print("Wykonaj cokolwiek")
lista = []
lista.append("123456")
print(lista)
print(next(kwa))  # 16

kwa2 = kwadrat2(10)
print(next(kwa2))
print(next(kwa2))
print(next(kwa2))
print(" Kolejna liczba z kwa2:", next(kwa2))
print(" Kolejna liczba z kwa:", next(kwa))  # Kolejna liczba z kwa: 16
try:
    print(next(kwa))  # StopIteration
except StopIteration:
    print("Zakończyłęm działanie")

print(range(10))
print(type(range(10)))  # <class 'range'>
