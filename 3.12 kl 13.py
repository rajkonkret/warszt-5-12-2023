# Exception
# tworzyć wyjątki nadpisując klase Exception
# class

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całkowitą"))
    if x < 0:
        raise MyException("Liczba musi być dodatnia")
except MyException as e:
    print("Wystąpił wyjątek MyException")
except ValueError:
    print("Wystąpił błąd wartości")
except TypeError:
    print("Błąd typu")
except Exception as e:
    print("Bład", e)
else:
    print(f"Wprowadziłęś poprawna wartośc {x}")
finally:
    print("Dane zostały wprowadzone")
