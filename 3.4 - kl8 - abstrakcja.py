# abstrakcja -
from abc import ABC, abstractmethod


# po oznaczeniu metody jako abstrakcyjnej klasa staje sie abstrakcyjna
# nie można zbudowac obiektu takiej klasy
class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod  # metoda abstrkcyjna
    def drukuj(self):
        pass

    @staticmethod  # metoda statyczna
    def from_string():
        print("Metoda statyczna")

    @classmethod
    def from_counter(cls, counter):
        return cls(counter.values)  # osyłamy nowy obiekt klasy Counter


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartość nie może być większa niż MAX")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje... ", self.values)


class NewCounter(Counter):
    """
    Licznik bez metody drukuj()
    """


# po oznaczeniu metody jako abstrakcyjnej
# TypeError: Can't instantiate abstract class Counter with abstract method drukuj
# c = Counter()
# c.increment()
# c.drukuj()

bc = BoundedCounter()
bc.increment()
bc.drukuj()  # Drukuje...  1

# TypeError: Can't instantiate abstract class NewCounter with abstract method drukuj
# nie da sie stworzyc bo nie nadpisuje metody drukuj()
# nc = NewCounter()

# metoda statyczna
# używamy bez konieczności tworzenia obiektu klasy
Counter.from_string()  # Metoda statyczna

# chcemy z licznika bc utworzyc nowy licznik startujacy juz od wartości licznika bc
d = BoundedCounter(bc.values)
d.drukuj()  # 1 - wzieły wartość licznika z aktualnej wartości licznika bc

e = BoundedCounter.from_counter(bc)
e.drukuj()  # 1
