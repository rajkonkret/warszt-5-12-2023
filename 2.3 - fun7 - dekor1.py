# dekorator @dekorator_nazwa
# jako argument przyjmuje inną funkcję
# dodanie nowej funkcjonalności do funkcji
# wykorzystuje zasdę funkcji wewnętrznej
def dekor(funk):
    def wew():
        print("Dekorujemy!!!")
        return funk()

    return wew  # zwraca adres funkcji wewnętrznej


@dekor
def hej():
    # print("Dekorujemy!!!")
    print("Hej!!!")


hej()
# po dodaniu dekoratora
# Dekorujemy!!!
# Hej!!!
