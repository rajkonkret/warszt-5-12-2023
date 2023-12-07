# stworzenie ksiaki telefonicznej z wykorzystaniem petli while
# dodaj kontakt, usun kontakt, wyszukaj, wyswietl lisste kontaktow


# stworzyc system zarzadzanai biblioteka
# dodaj ksiazke, usun ksiazke, wypozycz ksiazke, zwroc ksiazke
# uzyc klass np.: Book, Library
# obsłuzyc błedu
# mozna dodac klase user - bedzie pamietał jakie ksiazki wypozyczył
# 11:20
contacts = {}
while True:
    print(f"""
    1. Dodaj kontakt
    2. Usuń kontakt
    3. Wyszukaj kontakt
    4. Wyswietl liste kontaktów
    5. Koniec
    """)
    try:
        odp = input("Wybierz opcję")
        if odp == "1":
            name = input("Poadj imie")
            number = input("Podaj numer telefonu").replace(" ", "").replace("-", "")
            if not number.isdigit():
                raise ValueError("Numer telefonu powinien zawierać cyfry")
            else:
                contacts[name.lower()] = number
                print(f"Kontakt został dodany")
        elif odp == "2":
            name = input("Podaj imię kontaktu do usunięcia")
            if name.lower() in contacts:
                contacts.pop(name.lower())
                # del contacts[name]
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "3":
            name = input("Podaj imię kontaktu do wyszukania")
            if name.lower() in contacts:
                print(f"Kontakt {name} nr telefonu {contacts[name.lower()]}")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "4":
            print(f"Lista kontaktów {contacts.keys()}")
        elif odp == "5":
            break
        else:
            print("Nie znam takiego działania")
    except Exception as e:
        print("Bład", e)
