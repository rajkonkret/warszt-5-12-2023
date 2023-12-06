# klasa - szablon
# pola klasy name
# funkcje - np.: gadanie
import math


# definicja klasy
class MyFirstClass:
    """
    Klasa w Pythonie, opisująca punkty w przestrzeni x i y
    """

    # metoda inicjalizująca (konstruktor)
    def __init__(self, x=0, y=0):
        """
        metoda inicjalizująca
        :param x: położenie na osi x w przestrzeni
        :param y: położenie na osi y w przestrzeni
        """
        # self.x = x
        # self.y = y
        # po dodaniu metody move() mozemy jej uzyc w konstruktorze
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    # funkcje magiczne, ospowiada za sposób reprezentacji obiektu np.: przy wypisywaniu
    def __repr__(self):
        return f"x = {self.x}, y = {self.y}"


# tworzenie obiektu klasy
p1 = MyFirstClass()
print(p1)  # <__main__.MyFirstClass object at 0x000001E6F746D7D0>
# po nadpisaniu repr print(p1) -> x = 0, y = 0
print(MyFirstClass.__doc__)  # Klasa w Pythonie, opisująca punkty w przestrzeni x i y
print(print.__doc__)
print(p1.x)
print(p1.y)
p1.move(45, 89)
print(p1)
# x = 45, y = 89
p1.reset()
print(p1)  # x = 0, y = 0

p2 = MyFirstClass(78, 999)
print(p2)
print(p1.calculate(p2))  # 1002.0404183464857
