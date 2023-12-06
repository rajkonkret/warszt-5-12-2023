from pprint import pprint


class ContactList(list['Contact']):
    def serach(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    all_contact = ContactList()  # pusta lista, wspolna lista dla wszystkich obiektów tej klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name!r} {self.email!r}"


class Suplier(Contact):  # dziedziczymy po klasie Conatct
    """
    Dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")

    def __repr__(self):
        return f"Suplier {self.__class__.__name__} {self.name!r} {self.email!r}"


class Friend(Suplier):
    """"""

    def __init__(self, name, mail, phone):
        super().__init__(name, mail)  # super() - klasa nadrzedna
        self.phone = phone

    def __repr__(self):
        return f"Friend {self.__class__.__name__} {self.name!r} {self.email!r} +48 {self.phone}"


contact_list = ContactList()
print(contact_list)  # []
print(type(contact_list))  # <class '__main__.ContactList'>
c1 = Contact("Adam", "adam@wp.pl")
contact_list.append(c1)
print(contact_list)  # [Adam adam@wp.pl]
print(contact_list.serach('Adam'))  # [Adam adam@wp.pl] [Contact 'Adam' 'adam@wp.pl'] !r dodaje '' do stringów
f1 = Friend("Tomek", "tomek@wp.pl", "687678987")
print(f1)  # Friend Friend 'Tomek' 'tomek@wp.pl' po nadpisaniu __repr__ w Friend
# po dopisaniu phone: Friend Friend 'Tomek' 'tomek@wp.pl' +48 687678987
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
f1.order("herbata z miodem")  # herbata z miodem zamówiono od Tomek
s1 = Suplier("Jarek", 'jarek@wp.pl')
pprint(c1.all_contact)
# [Contact 'Adam' 'adam@wp.pl',
#  Friend Friend 'Tomek' 'tomek@wp.pl' +48 687678987,
#  Suplier Suplier 'Jarek' 'jarek@wp.pl']
