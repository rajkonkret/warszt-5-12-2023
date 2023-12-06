# napiać funkcje ktora przyjmie age, first, last
# z tych parametrów zbuduje słownik
# age moze byc opcjonalne
# za pomoca petli while pobrac te dane od usera i wywołąc z parametrami ta funkcje
# zastosowa  "klawisz ucieczki"

def build_dict(first, name, age=None):
    person = {'first': first, 'name': name}
    if age:
        person['age'] = age

    return person


print(build_dict("Radek", "Kowalski"))  # {'first': 'Radek', 'name': 'Kowalski'}

while True:
    print("Podaj imię i nazwisko")
    print("wpisz q by zakończyć")
    f_name = input("Imię:")
    if f_name == 'q':
        break
    l_name = input("Nazwisko:")
    if l_name == 'q':
        break
    age = input("Wiek:")
    if age == 'q':
        break
    print(build_dict(f_name, l_name, age))
