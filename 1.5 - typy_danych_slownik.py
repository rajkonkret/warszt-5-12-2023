# słownik
# para klucz wartosc
# {"name":"Radek"}
# klucze nie mogą się powtórzyć

slownik = {}  # pusty słownik
print(slownik)  # {}
print(type(slownik))  # <class 'dict'>

slownik['imie'] = "Radek"
print(slownik)
slownik['wiek'] = 39
print(slownik)  # {'imie': 'Radek', 'wiek': 39}
print(slownik['wiek'])  # 39

print(slownik.keys())
print(slownik.values())
print(slownik.items())  # dict_items([('imie', 'Radek'), ('wiek', 39)])

# print(slownik['age'])  # KeyError: 'age'
print(slownik.get('age'))  # None
print(slownik.get('age', "default"))  # default
print(slownik.pop('wiek'))
print(slownik)
print(slownik.popitem())  # ('imie', 'Radek')
print(slownik)  # {}
