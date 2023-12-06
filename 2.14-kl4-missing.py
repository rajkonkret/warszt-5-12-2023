# __missing__ - metoday wykonywana gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


# dopuszczajacy wywołanie kluczy nie uwzgledniajac duze/małe litery
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        # return self[key.lower()]
        if isinstance(key, str):
            return self.get(key.lower())


d_python = {}
d_python['name'] = "Radek"
print(d_python['name'])
# print(d_python['imie'])  # KeyError: 'imie'
d1 = DefaultDict()
d1['name'] = "Radek"
print(d1)
print(d1['name'])
print(d1['imie'])
# Radek
# {'name': 'Radek'}
# Radek
# default

d2 = AutoKeyDict()
print(d2)  # {}
print(d2['imie'])  # imie
print(d2)  # {'imie': 0}

d3 = CaseInsensitiveDict()
d3['name'] = 'Radek'
print(d3['NAMe'])  # Radek
