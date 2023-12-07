# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z kalsy A")


class B:
    def method(self):
        print("Metoda z kalsy B")


class C(B, A):  # kolejnośc ma znaczenie
    """
    Klasa dziedziczy po klasach A i B
    """


class D(A, B):
    """
    Klasa D
    """


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


class F(B, A):
    def method(self):
        A.method(self)  # wskazanie, ze  ma byc to metoda z klasy A


class G(A, B):
    def method(self):
        super().method()  # wykona metode z kalsy nadrzednej, tutaj: A
        print("Dopisane")


a = A()
a.method()

b = B()
b.method()

c = C()
c.method()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

d = D()
d.method()  # Metoda z kalsy A

e = E()
print(E.__mro__)  # (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
e.method()  # Metoda z klasy E

f = F()
f.method()  # Metoda z kalsy A

g = G()
g.method()
# Metoda z kalsy A
# Dopisane
