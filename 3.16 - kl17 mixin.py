# klasy mixin
# wykorzystuja wielodziedziczenie
# uzywaja klas, których nie warto tworzyc instancji
import json


class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


class XmlMixin:
    def to_xml(self):
        pass


class Contact(JsonMixin, XmlMixin):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


contact = Contact("Jan", "Kowalski")
print(contact.to_json())  # {"first_name": "Jan", "last_name": "Kowalski"}
