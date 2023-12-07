# __eq__ porównaie (==)
# __lt__ mniejsza niz (<)

class MyNumber:
    def __init__(self, value):
        self.value = value


class MyNumber2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        """Porównuje obiekty po wartości value"""
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num1 = MyNumber(5)
num2 = MyNumber(15)
# brak metody __lt__
# print(num1 < num2)  # TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'

num3 = MyNumber2(5)
num4 = MyNumber2(15)
num5 = MyNumber2(15)

print(num3 < num4)  # True
print(num3 == num4)  # False
print(num4 == num5)  # True
