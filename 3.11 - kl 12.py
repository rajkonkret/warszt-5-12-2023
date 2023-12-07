# hermetyzacja, enkapsulacji

class Boat:
    """
    Dokumentacja klasy
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # __ - pole prywatne, hermetyzacja

    def sail(self):
        self.__speed += 10

    def speedometer(self):  # enkapsulacja - wystawieni dedykowanych metod do zmiany lub odczytu pola
        print(f"Speed in knots {self.__speed}")

    def break_(self):
        self.__private()
        self.__speed -= 10

    def __private(self):  # metoda prywatna
        print("Private")


b1 = Boat("Omega", 2023)
b1.sail()
b1.sail()
b1.sail()
b1.sail()
b1.sail()
# po ustawieniu pola jako prywatne
# AttributeError: 'Boat' object has no attribute '__speed'
# print(b1.__speed)  # 50
b1.speedometer()  # Speed in knots 50
b1.__speed = 0
print(b1.__speed)  # pole globalne dla obiektu, stworzone w tym miejscu
b1.speedometer()
# 0
# Speed in knots 50
b1.break_()
b1.break_()
b1.break_()
b1.break_()
b1.break_()
b1.speedometer()
# 14:35
