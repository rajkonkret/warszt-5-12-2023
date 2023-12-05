# while - petla sterowana warunkiem

licznik = 0
while licznik < 10:
    licznik += 1  # licznik = licznik +1
    print("Komunikat !!!")

lista = []
lista2 = []
while True:
    print("Działam")
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)
print(lista2)
