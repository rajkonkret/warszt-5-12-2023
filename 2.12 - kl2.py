# dziedziczenie
class Contact:
    all_contact = []  # pusta lista, wspolna lista dla wszystkich obiektów tej klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

    def __repr__(self):
        return f"{self.name} {self.email}"


class Suplier(Contact):  # dziedziczymy po klasie Conatct
    """
    Dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "admin1@wp.pl")
c3 = Contact("Tomek", "admin2@wp.pl")
print(c1.all_contact)  # [Adam admin@wp.pl, Radek admin1@wp.pl, Tomek admin2@wp.pl]
s = Suplier("Marek", "marek@wp.pl")
print(s)  # Marek marek@wp.pl
print(c1.all_contact)  # [Adam admin@wp.pl, Radek admin1@wp.pl, Tomek admin2@wp.pl, Marek marek@wp.pl]
s.order("Kawa")  # Kawa zamówiono od Marek
print(s.all_contact)  # [Adam admin@wp.pl, Radek admin1@wp.pl, Tomek admin2@wp.pl, Marek marek@wp.pl]
# 15:15
